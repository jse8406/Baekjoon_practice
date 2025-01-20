#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int,string> a, pair<int,string> b){
    return a.first < b.first;
}

int main(){

    int N; 
    cin >> N;

    pair<int, string> tmp;
    vector<pair<int, string>> arr;

    for(int i=0; i<N; i++){
        cin >> tmp.first >> tmp.second;
        arr.push_back(tmp);
    }
    // stable sort == 키 값이 동일하면 기존 순서를 유지한다.
    stable_sort(arr.begin(), arr.end(), compare);
    for(int i = 0; i < N; i++)
        cout << arr[i].first << ' ' << arr[i].second << '\n';
}
