#include<iostream>

using namespace std;

int main()
{
    int test;
    cin >> test;
    while(test--)
    {
        string str;
        cin >> str;
        int count=0, ans=1;
        for (int i=0; i<str.length()-1; i++)
        {
            if (str[i]!=str[i+1])
            {
                ans *= pow(2, count);
                count = 0
            }
            else if (i==str.length()-2) ans*=pow(2, count+1);
            else count+=1;
        }
        cout << ans << endl;
    }
}
