#include <iostream>
#include <algorithm>
#include <vector>


using namespace std;

// bool compare(int a, int b){
//     if(a>b) return true;
//     else return false;
// }


int main(){
    int N,n;
    cin >> N;
    vector<int> v;
    for(int i=0;i<N;i++){
        cin >> n;
        v.push_back(n);
    }
    // callback 함수 추가로 내림차순 정렬로 바꿀 수 있음
    sort(v.begin(), v.end());
    for(int i=0;i<N;i++){
        cout << v[i] << '\n';
    }

    return 0;
}