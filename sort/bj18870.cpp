#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<int> v, back;
    int N, input;
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> input;
        v.push_back(input);
        back.push_back(input);
    } 

    sort(v.begin(), v.end());
    // unique의 반환값: std::unique는 중복되지 않은 요소 다음을 가리키는 반복자(v.begin() + 5)를 반환합니다.
    // 즉 중복되는 요소의 시작부터 끝까지를 삭제하여 set으로 집합으로 남김.
    v.erase(unique(v.begin(), v.end()), v.end());

    for(int i=0;i<N;i++){
        // v의 시작, 끝 반복자 사이에서 back[i]보다 크거나 같은 값이 제일 먼저 나오는 값
        auto it = lower_bound(v.begin(), v.end(), back[i]);
        cout << it-v.begin() << ' ';
    }



    return 0;
}
