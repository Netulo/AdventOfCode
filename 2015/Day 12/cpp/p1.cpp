#include <iostream>
#include<string>
#include <fstream>

using namespace std;



int main(){
    ifstream f("../input.txt");
    string inp;
    getline(f, inp);

    int sum = 0;
    for(int i = 0; i < inp.length(); i++){
        if((int(inp[i]) >= (int)'0' && (int)inp[i]<=(int)'9') || inp[i] == '-'){
            int sub = 1;
            if(inp[i] == '-'){
                sub = -1;
                i++;
            }
            string num = "";
            while(true){
                if(int(inp[i]) >= (int)'0' && (int)inp[i]<=(int)'9'){
                    num += inp[i];
                    i++;
                }
                else{
                    sum += stoi(num) * sub;
                    break;
                }
            }
        }
    }
    cout << sum;
    return 0;
}