#include<iostream>
#include<algorithm>
#include<cstdio>

using namespace std;

int countPair(int arr[], int length, int sum)
{
    int count=0;
    if(length < 1 )
        return count;

    int high = length - 1;
    int low = 0;

    while(low < high)
    {
        long long add = arr[low] + arr[high];

        if(add == sum)
        {
            count+=1;
            low+=1;
            high-=1;
        }
        else if(add > sum)
            high-=1;
        else
            low+=1;
    }

    return count;
}
int main(){
    int t,m,n;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&n,&m);
		int arr[n];      
	
		for(int i=0;i<n;i++){
			scanf("%d",&arr[i]);
		}
		sort(arr,arr+n);
		cout<<countPair(arr,n,m)<<endl;
	}
	return 0;
}