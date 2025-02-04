#include <iostream>
#include <algorithm>

using namespace std;
int dp[1000001];

int main(){

    dp[1] = 1;
    dp[2] = 2;

    int N;
    cin >> N;

    for(int i=3; i<N+1;i++){
        dp[i] = (dp[i-1] + dp[i-2]) % 15746;
    }
    cout << dp[N];
}