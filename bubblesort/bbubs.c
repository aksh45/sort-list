#include<stdio.h>
int swap(int*x,int*y){
int temp=*x;
*x=*y;
*y=temp;
}
int bbs(int arr[],int n){
for(int x=0;x<n-1;x++){
   for(int i=0;i<n-x-1;i++){
      if (arr[i]>arr[i+1]){
         swap(&arr[i],&arr[i+1]);
      }
   }
}
}
int main(){
int n;
scanf("%d",&n);
int array[n];
for(int x=0;x<n;x++){
scanf("%d",&array[x]);
}
bbs(array,n);
for(int i=0;i<n;i++){
printf("%d",array[i]);
}
}

