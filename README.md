# Baekjoon_practice
PS practice for algorithm

[![Solved.ac Profile](http://mazassumnida.wtf/api/generate_badge?boj=ya8406)](https://solved.ac/ya8406)

# Major algorithm

## Sort  
sort 자체는 메서드로 대부분 구현이 되어있어서,,sort만하는 문제는 거의 없다.
## Greedy  
우선 순위별로 sort를 해서 현재 가장 우선 순위가 높은 것부터 조건에 맞게 연산하는 방식.
## DFS/BFS, brute force (완전 탐색)  
brute force는 주로 for문으로 탐색
DFS는 python에서 재귀나 stack으로, BFS는 deque로 구현한다.  
재귀도 결국 call stack에 의한 순서로 탐색을 하는 거라 재귀 max_depth recursion error가 나지 않으려면 stack으로 푸는 것이 좋다.
## Binary search  
찾고자하는 대상을 정렬되어있는 후보에서 절반씩 후보를 줄여가며 찾아가는 방식. 
## Dynamic programming
Problem을 Subproblem으로 쪼갠 뒤 겹치는 Subproblem에 대해서 memorization을 통해 중복 연산 횟수를 줄여 더 적은 연산으로 문제를 해결하는 방법.
Overlapping 되는 문제를 저장해둔 값으로 바로 대체. 재귀로 주로 구현.
## BackTracking
모든 탐색 후보군을 탐색해 가며 그 중 promising 조건에 부합하지 않는 후보군에 대해서는 탐색을 종료하여 pruning. 연산을 더 효율적으로 할 수 있음. BFS/DFS의 완전탐색에 promising 함수를 더해 가지치기 효과를 더해 연산 수를 줄인다. Decision space를 정하여 이를 탐색한다. Decision space가 더 이상 늘어나지 않고 끝나는 순간 recursion call을 멈추고 결과를 return 한다.
## Shortest Path
## Graph Theory

