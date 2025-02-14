#include <iostream>
#include <algorithm>

using namespace std;

int dp[101][10];

int main(){

    int N;
    cin >> N;

    for(int i=1;i<10;i++){
        dp[1][i] = 1;
    }
    for(int i=2; i<N+1; i++){
        // 이 앞 숫자가 0 or 9인 경우는 1개만 올 수있고 나머지는 2개
        dp[i][0] = dp[i-1][1];
        dp[i][9] = dp[i-1][8];
        for(int j=1;j<9;j++){
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])% 1000000000;
        }
    }
    int sum = 0;
    for(int i=0;i<10;i++){
        sum = (sum + dp[N][i])% 1000000000;
    }
    cout << sum;

    return 0;


}