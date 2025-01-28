#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int stats[21][21];
bool check[21];
int N;
int ans = 1000000000;



// pseudo code
/* 
	팀 구성을 한명씩 이룬다.
	n/2 : n/2로 팀이 나눠지면 각 팀의 stat의 합을 계산한다.
	차를 계산하고 이를 init 변수와 비교해서 더 작으면 갱신한다
	새로운 팀을 구성 시켜서 위 과정을 반복한다.
	=> 팀을 새롭게 구성하는 과정 : 
		그냥 for문 : 브루트 포스
		사전에 안되는 경우는 탐색 x (pruning) : backtracking
		backtracking은 주로 재귀로 구현한다.

*/
// DFS에 필요한 args?
// 언제 return 할지에 대한 index값 => 현재 팀원 배분이 전체 사람의 절반까지 되었다면 반씩 나눠진 것이므로 return, 결과 return 값 등,,
void DFS(int n, int next){
		int start, link;
		start = 0;
		link = 0;


	if (N/2 == n){

		for(int i=1;i<=N;i++){
			for(int j=1;j<=N;j++){
				if(check[i] == true && check[j] == true) start += stats[i][j];
				if(check[i] == false && check[j] ==false) link += stats[i][j];
			}
		}
		int temp = abs(start -link);
		ans = min(temp, ans);
		return;
	};
	for(int i=next; i<N; i++){
		check[i] = true;
		DFS(n+1, i+1);
		check[i] = false;
	}
}

int main(){
	cin >> N;

	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			cin >> stats[i][j];
		}
	}

	DFS(0, 1); // 카운트 0회부터 숫자는 1부터 시작

	cout << ans;
}