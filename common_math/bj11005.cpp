#include <iostream>

using namespace std;

int main(){
    int N, B;
    string ans;
    cin>>N>>B;
    // ASCII - 55 = A:10, B:11 ....
    while(N>0){
        int remainder = N%B;
        if(remainder>=0 && remainder <=9){
            ans += remainder+'0';
        }
        else{
            ans += remainder+'A'-10;
        }
        N /= B;
    }
    for(int i=ans.length()-1;i>=0;i--){
        cout << ans[i];
    }
        
}