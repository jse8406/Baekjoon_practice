#include <iostream>

using namespace std;


int N;
int dp[1000001] = {0,};

// dp[i] = i를 1로 만드는데 필요한 최소 연산 횟수

//이렇게 하면 답이 틀림, 10은 1을 뺴고 3으로 2번 나누는게 더 빠르다. 따라서 다 해봐야함.
// 따라서 연산의 우선순위가 없고 셋다 해보면서 연산 횟수가 가장 적은 걸 채택

int main(){

    cin >> N;

    for(int i=2;i<N+1;i++){
        dp[i] = dp[i-1] + 1;

        if(i%3 == 0) dp[i] = min(dp[i], dp[i/3]+1);
        if(i%2==0) dp[i] = min(dp[i], dp[i/2]+1);
    }
    cout << dp[N];

    return 0;
}