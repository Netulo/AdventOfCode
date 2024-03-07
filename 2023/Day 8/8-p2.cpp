#include<iostream>
#include<string>
#include<fstream>
#include<map>
#include<vector>
#include<algorithm>

using namespace std;

int countStep(int mapID, string &instruction, map<string, string> &maps, vector<vector<string>> &startingPoints, bool isFirst);

int main()
{
    fstream myFile("input.txt");

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

    // for(auto x : maps)
    //     cout << x.first << " -> " << x.second << endl;

    vector<vector<string>> startingPoints;
    for(auto x : maps)
        if(x.first[2] == 'A')
            startingPoints.push_back({x.first, "0"});

    // for(auto x : startingPoints)
    //     cout << x.first << " -> " << x.second << endl;

    int count;
    int temp = 0;
    while(true)
    {
        // for(int x = 0; x < startingPoints.size(); ++x)
        // {
        //     countStep(x, instruction, maps, startingPoints, true);
        //     count = stoi(startingPoints[x][1]);
        // }

        countStep(temp%startingPoints.size(), instruction, maps, startingPoints, true);
        count = stoi(startingPoints[temp%startingPoints.size()][1]);
        temp++;

        // for(int x = 0; x < startingPoints.size(); ++x)
        //     cout << startingPoints[x][0] << " -> " << startingPoints[x][1] << endl;
        
       
        
        //cout << endl;
        // if(all_of(startingPoints.begin(), startingPoints.end(), [&](auto i){return i[1] == startingPoints[i];}))
        //     break;
        bool isAllEq = true;

        for (int i = 0; i < startingPoints.size()-1; i++)
        {
            if(startingPoints[i][1] == startingPoints[i+1][1])
                isAllEq = true;
            else
            {
                isAllEq = false;
                break;
            }

        }
        
        if(isAllEq)
            break;
    }


    printf("Step count is: %d", count);
}



int countStep(int mapID, string &instruction, map<string, string> &maps, vector<vector<string>> &startingPoints, bool isFirst)
{

    if(startingPoints[mapID][0].substr(2, 1) == "Z" && !isFirst)
        return 0;
        

    int count = stoi(startingPoints[mapID][1]);
    //startingPoints.erase(mapID);
    //auto nodeHandler = startingPoints.extract(mapID);
    //auto nextt = next(mapID);

    if(instruction[count%instruction.length()] == 'L')
        startingPoints[mapID][0] = maps[startingPoints[mapID][0]].substr(1, 3);
    else
        startingPoints[mapID][0] = maps[startingPoints[mapID][0]].substr(6, 3);

    //nodeHandler.key() = mapID;
    //startingPoints.insert(move(nodeHandler));
    count++;
    startingPoints[mapID][1] = to_string(count);

    return countStep(mapID, instruction, maps, startingPoints, false) + 1;
}