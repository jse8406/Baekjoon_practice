//과목명, 학점, 등급

#include <iostream>

using namespace std;

float changeScore(string rate){
    if(rate == "A+") return 4.5;
    else if(rate == "A0") return 4.0;
    else if(rate == "B+") return 3.5;
    else if(rate == "B0") return 3.0;
    else if(rate == "C+") return 2.5;
    else if(rate == "C0") return 2.0;
    else if(rate == "D+") return 1.5;
    else if(rate == "D0") return 1.0;
    else if(rate == "F") return 0.0;
}

int main(){
    
    string subname, rate;
    float credit;


    float totalCredit = 0;
    float totalScore = 0;
    for(int i=0;i<20;i++){
        cin >> subname >> credit >> rate;
        if(rate!="P"){
            totalCredit += credit;
            totalScore += changeScore(rate)*credit;
        }
    }
        cout << totalScore/totalCredit;
    return 0;
}

