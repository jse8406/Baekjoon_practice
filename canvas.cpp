#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    
    vector<int> mymap = {1,2,3,4};
        
    auto target = find(mymap.begin(), mymap.end(), 3);
    cout << *target;

    return 0;
}
