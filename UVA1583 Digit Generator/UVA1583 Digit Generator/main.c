#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAXNUM 100010
int main()
{
    int ar[MAXNUM];
    memset(ar, 0, sizeof(ar));
    
    for (int i=1;i<MAXNUM;i++)
    {
        int total=i;
        int c=i;
        while (c>0)
        {
            total+=(c%10);
            c/=10;
        }
        if (total<MAXNUM&&ar[total]==0) ar[total]=i;
    }
    
    int num,count;
    scanf("%d",&count);
    for (int i=0;i<count;i++)
    {
        scanf("%d",&num);
        printf("%d\n",ar[num]);
    }
    return 0;
}
