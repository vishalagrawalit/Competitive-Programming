#include <bits/stdc++.h>

#define ll long long int
using namespace std;

const long double range=0.000005;
long double R,H,ans,temp,A,B,C;
long double F(long double x)
{
    return x*x*x*A + B*x*x + C;
}
long double binarySearch()
{
    long double low=0, high=200,mid;
    while(low < high)
    {
        mid=(low + high ) / 2;
        ans=F(mid);
        if ( ans < range && ans > (-range))
        {
            return mid;
        }
        if (ans > -range)
        {
            high=mid;
        }
        else
        {
            low=mid;
        }
    }
}
int main()
{    
    int test;
    cin >> test;
    while(test--)
    {
        cin >> R >> H; 
        A = R*R;
        temp=sqrt(R*R + H*H);
        B = 3*R*temp;
        C = -6*R*H*H*temp;
 
        ans=binarySearch();
        if (ans>H)
        {
             cout << fixed << setprecision(6) << H << endl;
        }
        else
            cout<< fixed << setprecision(6) << ans << endl;
    }
    return 0;
}