#include <iostream>
#include <string>
#include <map>
#include <fstream>

using namespace std;
int main()
{
    fstream myFile("input.txt");
    if(!myFile.is_open())
        return -1;

    string input;
    getline(myFile, input);

    map<string, int> coords;
    int x, y;
    x = y = 0;
    coords[to_string(x) + "," + to_string(y)] = 1;
    for(int i = 0; i < input.length(); ++i)
    {
        switch (input[i])
        {
        case '^':
           y++;
            break;
        case 'v':
           y--;
            break;
        case '>':
           x++;
            break;
        case '<':
           x--;
            break;
        
        default:
            break;
        }
        coords[to_string(x) + "," + to_string(y)] = 1;
    }

    cout << coords.size();
}