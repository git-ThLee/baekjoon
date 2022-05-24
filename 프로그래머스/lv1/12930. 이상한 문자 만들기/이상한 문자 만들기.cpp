#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string s) {
    string answer = "";
    int count=0;
    for(int i = 0 ; i < s.size(); i++){
        if(s[i] == ' '){
            count = 0;
           
        }else{
            if(count % 2 == 0){
                s[i] =toupper(s[i]);
            }else{
                s[i] = tolower(s[i]);
            }
            count++;
        }
        
    }
    for(int i = 0 ; i < s.size(); i++){
        answer.push_back(s[i]);
    }
    return answer;
}