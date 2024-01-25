#include<iostream>
#include<string>
#include<fstream>
#include<map>
#include<vector>
#include <algorithm>

using namespace std;

int countStep(string mapID, string instruction, map<string, string> maps, map<string, int> &startingPoints, bool isFirst);

int main()
{
    fstream myFile("test-p2.txt");

    if(!myFile.is_open())
    {
        cout << "File oppening failed";
        return -1;
    }

    string instruction;
    getline(myFile, instruction);
    
    
    string input;
    map<string, string> maps;
    
    getline(myFile, input);
    while(getline(myFile, input))
    {
        string key;
        key = input.substr(0,3);
        
        input = input.substr(input.find('('));
        
        maps[key] = input;
        
    }

    for(auto x : maps)
        cout << x.first << " -> " << x.second << endl;

    map<string, int> startingPoints;
    for(auto x : maps)
        if(x.first[2] == 'A')
            startingPoints[x.first] = 0;

    // for(auto x : startingPoints)
    //     cout << x.first << " -> " << x.second << endl;

    int count;
    while(true)
    {
        for(auto x : startingPoints)
        {
            countStep(x.first, instruction, maps, startingPoints, true);
            count = startingPoints[x.first];
        }

        for(auto x : startingPoints)
            cout << x.first << " -> " << x.second << endl;
        
        cout << endl;

        if(all_of(startingPoints.begin(), startingPoints.end(), [&](auto i){return i.second == startingPoints.begin() -> second;}))
            break;
    }


    printf("Step count is: %d", count);
}



int countStep(string mapID, string instruction, map<string, string> maps, map<string, int> &startingPoints, bool isFirst)
{

    if(mapID.substr(2, 1) == "Z" && !isFirst)
        return 0;

    int count = startingPoints[mapID];
    startingPoints.erase(mapID);
    if(instruction[count%instruction.length()] == 'L')
        mapID = maps[mapID].substr(1, 3);
    else
        mapID = maps[mapID].substr(6, 3);

    startingPoints[mapID] = count+1;

    return countStep(mapID, instruction, maps, startingPoints, false) + 1;
}