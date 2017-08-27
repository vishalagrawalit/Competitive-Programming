#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

struct act{
    int starting, ending;
}arr[100000];

bool compare(act a, act b){
    if(a.ending < b.ending)
        return true;
    if(a.ending == b.ending)
        return (a.starting < b.starting);
    return false;
}

int main(){
    int test, n, count, last;
    cin >> test;
    while(test--){
        scanf("%d", &n);
        for(int i=0;i<n;i++)
            scanf("%d%d", &arr[i].starting, &arr[i].ending);
        sort(arr, arr + n, compare);
        count = 1;
        last = arr[0].ending;
        for(int i=1;i<n;i++){
            if(last <= arr[i].starting){
                count++;
                last = arr[i].ending;
            }
    }
   cout << count << endl;
}
return 0;
}
