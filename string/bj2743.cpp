#include <iostream>

using namespace std;

int main(){
    char str[100] = {'0',};
    cin >> str;
    
    int answer = 0;
    cout << str << endl;
    while(str[answer] != '0'){
        answer++;
    }
    cout << answer;
    return 0;
}