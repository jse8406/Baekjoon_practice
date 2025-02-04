#include <iostream>
#include <vector>

using namespace std;


int count0=0;
int count1=0;
int arr[41];


int fib(int n){
    if (n == 1 || n == 2) {
        ++count0; 
        return 1;
    }
    else {
        return (fib(n-1)+ fib(n-2));
    }    
}


int fibonacci(int n){

    for(int i=3;i<n+1;i++){
        arr[i] = arr[i-1]+arr[i-2];
        ++count1;

    }
    return arr[n];

}

int main(){
    arr[1] = 1;
    arr[2] = 1;
    int n;
    cin >> n;
    fib(n);
    fibonacci(n);

    cout << count0 << " " << count1;
}