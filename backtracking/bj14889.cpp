#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int stats[21][21];
int init = INT8_MAX;

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

void DFS(){

	return;

}

int main(){



	return 0;
}