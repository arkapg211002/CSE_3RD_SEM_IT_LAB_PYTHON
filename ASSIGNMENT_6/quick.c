/*Write a program to perform quick sort*/
#include<stdio.h>
#include<stdlib.h>
void quick_sort(int *a,int low,int high)
{
    int i,j,pivot,temp;
    if(low<high)
    {
        pivot=low;
        i=low;
        j=high;
        while(i<j)
        {
            while(a[i]<=a[pivot] && i<=high)
            {
                i++;
            }
            while(a[j]>a[pivot] && j>=low)
            {
                j--;
            }
            if(i<j)
            {
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
        temp=a[j];
        a[j]=a[pivot];
        a[pivot]=temp;
        quick_sort(a,low,j-1);
        quick_sort(a,j+1,high);
    }
}
int main()
{
    int *a,i,n;
    printf("Enter the number of elements in the array:");
    scanf("%d",&n);
    a=(int*)malloc(n*sizeof(int));
    printf("Enter the elements of the array:");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    quick_sort(a,0,n-1);
    printf("The sorted array is:");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
    return 0;
}
