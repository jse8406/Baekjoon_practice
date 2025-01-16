#include <iostream>

using namespace std;

int main(){
    int N;
    cin >> N;

    int q = N/5;
    while (q>=0){
        int left = N-q*5;
        if(left%3==0){
            cout << q+left/3;
            return 0;
        }
        else{
            q--;
        }
    }
    cout << -1;
    

    return 0;
}