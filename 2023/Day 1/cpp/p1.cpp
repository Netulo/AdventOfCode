#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){

    fstream inputFile ("input.txt");
    string input = "";
    
    int counter = 0;
    while(getline(inputFile, input)){
        string sNum = "0";
        for(int i = 0; i < input.length(); i++){
            if(input[i] >= '0' && input[i] <= '9'){
                sNum += input[i];
                break;
            }
        }

        for(int i = input.length()-1; i >= 0; i--){
            if(input[i] >= '0' && input[i] <= '9'){
                sNum += input[i];
                break;
            }
        }

        counter += stoi(sNum);
    }

    cout << counter;
    return 0;
}