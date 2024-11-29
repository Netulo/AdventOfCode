#include<iostream>
#include<map>
#include<fstream>
#include<sstream>
#include<set>
#include <algorithm>

using namespace std;

vector<string> splitString(string str, char delimeter){

    stringstream stream(str);
    vector<string> arr;
    string token;
    while(getline(stream, token, delimeter)){
        arr.push_back(token);
    }

    return arr;
}

int main(){
    fstream file("../input.txt");
    map< set<string> , int> dict;
    vector<int> happinessSum;
    vector<string> names{"Me"};

    string inp;
    while(getline(file, inp)){
        inp = inp.substr(0,inp.size()-1);
        string firstPerson, secondPerson;
        vector<string> vec = splitString(inp, ' ');

        if(count(names.begin(), names.end(), vec[0]) == 0){
            names.push_back(vec[0]);
            dict[{vec[0],"Me"}] = 0;
        }

        if(inp.find("lose") != string::npos)
        {
            dict[{vec[0],vec[vec.size()-1]}] -= stoi(vec[3]);
        }
        else{
            dict[{vec[0],vec[vec.size()-1]}] += stoi(vec[3]);
        }
    }
    int maxSum = 0;
    int sum;
    do{
        sum = 0;
        for(int i = 0; i < names.size(); i++){
            sum += dict[{names[i], names[(i+1)%names.size()]}];
            if(sum > maxSum)
                maxSum = sum;
        }
    }
    while(next_permutation(names.begin(), names.end()));

    cout << maxSum;
    return 0;
}