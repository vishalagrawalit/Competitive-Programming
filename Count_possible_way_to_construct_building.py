#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	long long int A[100002]={0};
	int i, t;
	A[1] = 2; A[2] = 3;
	for(i = 3; i <= 100000; i++) A[i] = (A[i-1]+A[i-2])%1000000007;
	cin>>t;
	while(t--) {
		int n;
		cin>>n;
		long long int ans = (A[n]*A[n])%1000000007;
		cout<<ans<<endl;
	}
	// cout<<A[100000]<<endl;
	return 0;
}
