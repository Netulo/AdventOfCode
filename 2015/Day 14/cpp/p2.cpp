#include<iostream>
#include<vector>
#include<sstream>
#include<fstream>

using namespace std;

struct Raindeer {
    int speed;
    int speedDuration;
    int restDuration;
    int points = 0;
};

vector<string> splitString(string& str, char delimeter){
    stringstream sstream(str);
    
    vector<string> outputVec{};
    string temp;
    while(getline(sstream, temp, delimeter)){
        outputVec.push_back(temp);
    }

    return outputVec;
}

int main(){
    fstream file("../test.txt");
    vector<Raindeer> raindeers;
    int raceDuration = 1000;

    string inputStr;
    while(getline(file, inputStr)){
        vector<string> inputVec = splitString(inputStr, ' ');
        raindeers.push_back(Raindeer{
            .speed = stoi(inputVec[3]), 
            .speedDuration = stoi(inputVec[6]),
            .restDuration = stoi(inputVec[13])});
    }

    int maxDistance = 0;
    for(Raindeer raindeer : raindeers){
        
    }

    cout << maxDistance;
    return 0;
}