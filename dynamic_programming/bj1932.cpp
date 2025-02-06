#include <iostream>
#include <algorithm>

using namespace std;

int dp[500][500];

int main(){

    int N;
    cin >> N;
    // 배열로 입력받기
    for (int i=0; i<N; i++){
        for(int j=0;j<=i;j++){
            cin >> dp[i][j];
        }
    }

    for (int i=1; i<N; i++){
        for(int j=0;j<=i;j++){
            if(j==0){
                dp[i][j] += dp[i-1][j]; 
            }
            else if(j==i){
                 dp[i][j] += dp[i-1][j-1];
            }
            else{
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1]); 
            }
        }
    }
    int ans = *max_element(dp[N-1], dp[N-1]+N);
    cout << ans;

    return 0;

}
