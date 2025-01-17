#include <iostream>

using namespace std;

int O(int a1, int a0, int c, int n);

int main(){
    int a1, a0,c,n;
    cin >> a1 >> a0;
    cin >> c;
    cin >> n;


    // 최고차항이 작으면 볼 것 도 없음. 같을 경우 상수 a0가 반드시 음수여야함. 클 경우는 n일 때만 비교
    cout << O(a1,a0,c,n);
    

    return 0;
}

int O(int a1, int a0, int c, int n){

    if (a1 > c) {
        return 0;
    }

    else if (a1 == c)
    {
        /* code */
        if(a1 == c) if(a0<0) return 1;
        else return 0;
    }
    else{
        if(a1*n+a0<=c*n) return 1;
        else return 0;
    }
    

    return 0;
}