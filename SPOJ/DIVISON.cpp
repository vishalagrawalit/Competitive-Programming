#include <bits/stdc++.h>
using namespace std;
#define ULL unsigned long long 
#define M 1000000007
#define INV 333333336
ULL power(ULL n)
{
    ULL res=1,p=2;
    while(n)
    {
        if(n&1)
            res=(res*p)%M;
        p=(p*p)%M;
        n>>=1;
    }
    return res;
}
int main()
{
    ULL n,value;
    while(scanf("%llu",&n)!=EOF)
    {
        if(n&1){
            value = ((power(n)+1)*INV)%M;
            printf("%llu\n",value);
        }
        else{
            value = ((power(n)+2)*INV)%M;
            printf("%llu\n",value);
        }
    }
    return 0;
}