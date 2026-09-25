#include<iostream>
#include<vector>
#include<fstream>
#include<bitset>
using namespace std;

int F(uint32_t B, uint32_t C, uint32_t D, uint32_t i){
    if(i <= 15) return (B & C) | ((~B) & D);
    if(i <= 31) return (D & B) | ((~D) & C);
    if(i <= 47) return B ^ C ^ D;
    if(i <= 63) return C ^ (B | (~D));
    return -1;
}

uint32_t rotate(uint32_t num, int i){
    int s[64] = { 7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
                5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
                4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
                6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21};
    return num << s[i];
}

string strToBinary(string s)
{
string output = "";

    for (size_t i = 0; i < s.size(); ++i){
      output += bitset<8>(s.c_str()[i]).to_string();
    }
    return output;
}

string intToBinary(uint32_t n) {
    if (n==0) return "0";
    else if (n==1) return "1";
    else if (n%2 == 0) return intToBinary(n/2) + "0";
    else if (n%2 != 0) return intToBinary(n/2) + "1";
    return "-1";
}

uint32_t binaryToDecimal(string n)
{
    string num = n;
    uint32_t dec_value = 0;
 
    uint32_t base = 1;
 
    int len = num.length();
    for (int i = len - 1; i >= 0; i--) {
        if (num[i] == '1')
            dec_value += base;
        base = base * 2;
    }
    return dec_value;
}

uint32_t K[64] = {
0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391 };

uint32_t a = 0x67452301;
uint32_t b = 0xefcdab89;
uint32_t c = 0x98badcfe;
uint32_t d = 0x10325476;

int main(){
    fstream f("../input.txt");
    string input;
    getline(f, input);
    input = strToBinary("abcd") + '1';
    int originalLength = input.length()-1;
    int counter = 0;
    if(input.length()%512 < 448){
        counter =(448-input.length()%512);
    }
    else if(input.length()%512 > 448){
        counter =(512-input.length()%512)+448;
    }

    for(int x = 0; x < counter; ++x){
        input += '0';
    }

    input += intToBinary(originalLength);

    counter = 512-input.length()%512;
    for(int x = 0; x < counter; ++x){
        input += '0';
    }
    //cout << input.length();

    vector<string> blocks;

    for(int x = 0; x < input.length(); x+=512){
        blocks.push_back(input.substr(x, 512));
    }

    for(int x = 0; x < blocks.size(); ++x){
        vector<uint32_t> M;
        for(int y = 0; y < blocks[x].length(); y+=16)
            M.push_back(binaryToDecimal(blocks[x].substr(y, 16)));
        
        uint32_t A = a;
        uint32_t B = b;
        uint32_t C = c;
        uint32_t D = d;

        for(int i = 0; i < 64; ++i){
            uint32_t temp = F(B, C, D, i);
            int g;
            if(i < 16) g = i;
            else if(i < 32) g = (5*i + 1)%16;
            else if(i < 48) g = (3*i + 5)%16;
            else if(i < 64) g = (7*i)%16;
        
            temp = temp + A + K[i] + M[g];
            A = D;
            D = C;
            C = B;
            B = B + rotate(temp, i);
        }

        a = A;
        b = B;
        c = C;
        d = D;
    }

    cout << a;
}


//Nie działa