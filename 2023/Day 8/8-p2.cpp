#include<iostream>
#include<string>
#include<fstream>
#include<map>

using namespace std;

int countStep(string mapID, string instruction, map<string, string> maps, int count);

int main()
{
    fstream myFile("test.txt");

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

    printf("Step count is: %d", countStep("aaa", instruction, maps, 0));
}



int countStep(string mapID, string instruction, map<string, string> maps, int count)
{

    if(mapID == "ZZZ")
        return 0;

        if(instruction[count%instruction.length()] == 'L')
            mapID = maps[mapID].substr(1, 3);
        else
             mapID = maps[mapID].substr(6, 3);

        count++;

    return countStep(mapID, instruction, maps, count) + 1;
}