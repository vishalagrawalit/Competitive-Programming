#include<bits/stdc++.h>
using namespace std;

#define ll long long int

int evaluate(char *str, ll &n, char &operand)
{
        n = 0;
        
        if(str[0]<'0' || str[0]>'9')
        {
                operand = str[0];
                return 0;
        }
        
        for(int i=0; str[i]; i++)
                n = n*10 + (str[i]-'0');
        
        return 1;
}

int main()
{
        char s[100], operand;
        ll  T;
        ll res, num;
        cin >> T;
        while(T--)
        {
                res = 0;
                operand = '+';
                while(cin >> s)
                {
                        if(evaluate(s, num, operand))
                        {
                                switch(operand)
                                {
                                        case '+': res += num; break;
                                        case '-': res -= num; break;
                                        case '*': res *= num; break;
                                        case '/': res /= num; break;
                                }
                        }
                        else if(operand == '=')
                        {
                                cout << res << endl;
                                break;
                        }
                }
        }
        return 0;
}
