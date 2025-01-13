#include <iostream>

using namespace std;

int basket[101] = {0,};
int main(){
    int N, M;
    int i,j;

    cin >> N >> M;

    for(int i=1;i<N+1;i++){
        basket[i] = i;
    }

    for(int a=1;a<M+1;a++){
        cin >> i >> j;
        swap(basket[i], basket[j]);
    }

    for(int a=1;a<N+1;a++){
        cout << basket[a] << ' ';
    }

    return 0;
}

void swap(int idx1, int idx2){
    int spare;
    spare = basket[idx1];
    basket[idx1] = basket[idx2];
    basket[idx2] = spare;

    return;
}