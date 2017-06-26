#include<stdio.h>
#include<algorithm>
using namespace std;
int binarySearch(int arr[], int l, int r, int x)
{
   if (r >= l)
   {
        int mid = l + (r - l)/2;

        if (arr[mid] == x)  return mid;

        if (arr[mid] > x) return binarySearch(arr, l, mid-1, x);

        return binarySearch(arr, mid+1, r, x);
   }

   return -1;
}
int main(void)
{
    signed int n,k,count=0,i;
    scanf("%u %u",&n,&k);
    signed int arr[n];
    for(i=0;i<n;i++)
        scanf("%u",&arr[i]);
    sort(arr,arr+n);
    for(i=0;i<n;i++)
    {
        int result = binarySearch(arr, 0, n-1, arr[i]+k);
        if (result!=-1){
        	count+=1;
    }
    }
    printf("%u\n",count);
    return 0;
}