#include <iostream>
#include <map>

using namespace std;

// ASCII 'A' = 65, 'a' = 97

int arr[26] = {0,};

int main(){
    string word;
    cin >> word;
    for(int i=0;i<word.length();i++){
        if(word[i]<91){ // lowwer
            arr[word[i]-65]++;
        }
        else{
            arr[word[i]-97]++;
        }
    }
    int max = 0, max_idx = 0, cnt=0;
    for(int i=0;i<26;i++){
        if(arr[i]>max){
            max_idx = i;
            max = arr[i];
        }
    }
    for(int i=0;i<26;i++){
        if (max == arr[i]){
            cnt++;
        }
    }
    if(cnt>1) cout << "?";
    else cout << char(max_idx+65);
    



    return 0;
}