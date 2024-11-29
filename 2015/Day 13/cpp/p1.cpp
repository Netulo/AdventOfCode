#include<iostream>
#include<map>
#include<fstream>
#include<sstream>
#include<set>

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
    fstream file("../test.txt");
    map< set<string> , int> dict;

    string inp;
    while(getline(file, inp)){
        inp = inp.substr(0,inp.size()-1);
        string firstPerson, secondPerson;
        vector<string> vec = splitString(inp, ' ');

        if(inp.find("lose"))
            dict[{vec[0],vec[vec.size()-1]}] -= stoi(vec[3]);
        else{
            dict[{vec[0],vec[vec.size()-1]}] += stoi(vec[3]);
        }
    }


//     for(map< set<string> ,int>::iterator it = dict.begin(); it != dict.end(); ++it) {
//         for (string const& str : it->first)
//         {
//             cout << str << ' ';
//         }
//         cout << endl;
// }
    cout << dict.size();
    return 0;
}