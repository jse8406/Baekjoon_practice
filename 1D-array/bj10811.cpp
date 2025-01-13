#include <iostream>

using namespace std;

int basket[101] = {0,};

void swap(int idx1, int idx2){
    int spare;
    while(idx2 > idx1){
        spare = basket[idx1];
        basket[idx1] = basket[idx2];
        basket[idx2] = spare;
        idx1++;
        idx2--;
    }
}

int main(){
    int N,M;
    cin >> N >> M;
    for(int i=1;i<N+1;i++){
        basket[i] = i;
    }
    for(int a=0;a<M;a++){
        int i,j;
        cin >> i >> j;
        swap(i,j);
    }

    for(int i=1;i<N+1;i++){
        cout << basket[i] << " ";
    }

    return 0;
}