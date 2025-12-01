#include<iostream>
#include<vector>
#include<sstream>
#include<fstream>

using namespace std;

struct Raindeer {
    int speed;
    int speedDuration;
    int restDuration;
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
    fstream file("../input.txt");
    vector<Raindeer> raindeers;
    int raceDuration = 2503;

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
        int sumOfDurations = raindeer.speedDuration + raindeer.restDuration;
        int fullCycles = raceDuration / sumOfDurations;
        int distance = fullCycles*raindeer.speed*raindeer.speedDuration;
        int moduloDurations = raceDuration % sumOfDurations;
        
        if(moduloDurations < raindeer.speedDuration && moduloDurations > 0)
            distance += moduloDurations*raindeer.speed;
        if(moduloDurations > raindeer.speedDuration)
            distance += raindeer.speedDuration*raindeer.speed;
        
        if(maxDistance < distance)
            maxDistance += distance;
    }

    cout << maxDistance;
    return 0;
}