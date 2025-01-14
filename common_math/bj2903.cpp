#include <iostream>
#include <cmath>

using namespace std;

int main(){
    // 3 5 9 17 33 : 2 4 8 16 증가
    int N;
    cin>>N;
    int ans = 3;
    for(int i=1;i<N;i++){
        ans += pow(2, i);
    }
    // cout<< ans* ans;
    cout << int(pow(ans,2));
    // 왜 pow(ans, 2)로 하면 오답? => 소수점 오차
    return 0;

}