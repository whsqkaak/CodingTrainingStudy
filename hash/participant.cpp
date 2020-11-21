#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    int i;
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    for(i=0; i<completion.size(); i++){
        if (completion[i].compare(participant[i]) != 0){
            return participant[i];
        }
    }
    return participant[i];
}