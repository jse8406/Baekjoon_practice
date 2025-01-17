#include <iostream>
#include <algorithm>
#include <vector>


using namespace std;


int main(){
    int N,n;
    cin >> N;
    vector<int> v;
    for(int i=0;i<N;i++){
        cin >> n;
        v.push_back(n);
    }
    sort(v.begin(), v.end());
    for(int i=0;i<N;i++){
        cout << v[i] << '\n';
    }

    return 0;
}