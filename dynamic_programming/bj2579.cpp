#include <iostream>
#include <algorithm>

using namespace std;

int dp[300] = {0,};
int steps[301] = {0,};
int main(){

    int N;
    cin >> N;

    for(int i=1;i<=N;i++){
        cin >> steps[i];
    }
    dp[1] = steps[1];
    dp[2] = steps[1] + steps[2];

    for(int i = 3; i<N+1; i++){
        dp[i] = max(steps[i] + steps[i-1]+dp[i-3], steps[i] + dp[i-2]);
    }

    cout << dp[N];
    // i번 쨰 = i-1번쨰 + i-3번쨰 or i-2번째의 합합


    return 0;
}