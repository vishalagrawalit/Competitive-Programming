#include<iostream>
using namespace std;

#define ll long long int

int main()
{
	int test;
	cin >> test;
	while (test--)
	{
		ll s, ans;
		cin >> s;
		if (s>=0){
			if ((s>=0) && (s<10)) ans = 1;
			else
			{
				ans = 1;
				while (s>=10)
				{
					ans*=10;
					s=s/10;
				}
			}
		}
		else
		{
			ll n = abs(s);
			s = abs(s);
			if ((s>=0) && (s<10)) ans = 1;
			else
			{
				ans = 1;
				while (s>=10)
				{
					ans*=10;
					s=s/10;
				}
			}
			ans += 2*n;
		}
		cout << ans << endl;
	}
	return 0;
}