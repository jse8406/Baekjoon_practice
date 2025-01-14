//math

#include <iostream>

using namespace std;

int main(){
    double a,b,c,d,e,f; //int로 하면 나눗셈 연산시 버림으로 인한 오차발생? 왜 틀리냐 이건
    cin>>a>>b>>c>>d>>e>>f;
    int y = (c * d - a * f) / (b * d - a * e);
	int x = (c * e - b * f) / (a * e - b * d);
    
    cout<<x<<" "<<y;

    return 0;
}


// // brute force
// #include <iostream>

// using namespace std;

// int main(){
//     int a,b,c,d,e,f;
//     cin>>a>>b>>c>>d>>e>>f;

//     for(int x=-999;x<1000;x++){
//         for(int y=-999;y<1000;y++){
//             if(a*x+b*y==c){
//                 if(d*x+e*y==f){
//                     cout<<x<<" "<<y;
//                     break;
//                 }
//             }
//         }
//     }

//     return 0;
// }