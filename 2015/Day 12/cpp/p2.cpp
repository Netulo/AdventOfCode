#include <iostream>
#include<string>
#include <fstream>

using namespace std;



int main(){
    ifstream f("../input.txt");
    string inp;
    getline(f, inp);

    int temp = 0;
    int i = 0;
    while(true){
        if(i >= inp.length()){
            if(temp == 0)
                break;
            temp = 0;
            i = 0;
            continue;
        }

        cout << temp;

        int leftClose = inp.find("{", i);
        int rightClose = inp.find("}", i);
        if(leftClose < rightClose){
            i = leftClose;
            continue;
        }
        else if(leftClose > rightClose){
            if(inp.find("red", i, rightClose-i+1) != string::npos){
                inp.erase(i, rightClose-i+1);
                temp++;
                cout << temp;
            }
        }

        i++;
    }






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