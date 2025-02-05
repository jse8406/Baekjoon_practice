#include <iostream>
#include <algorithm>

using namespace std;

int dp[1000][3];

int main(){
    int N;
    int a,b,c;
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> a >> b >> c;
        if(i==0){
            dp[0][0] = a;
            dp[0][1] = b;
            dp[0][2] = c;
        }
        else{
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + a;
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + b;
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + c;
        }
    }
    cout << *min_element(dp[N-1], dp[N-1]+3);


    return 0;
}