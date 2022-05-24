#include <string>
#include <vector>

using namespace std;

string solution(vector<string> seoul) {
    string answer = "";
    int sell;
    for(int i = 0 ; i < seoul.size(); i++){
        if(seoul[i] == "Kim"){
             sell = i;
        }
    }
    answer += "김서방은 ";
    answer+= to_string(sell);
    answer += "에 있다";
    
    return answer;
}