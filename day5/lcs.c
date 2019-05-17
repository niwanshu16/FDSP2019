#include<stdio.h>
#include<string.h>
int lc(char *x,char *y,int m,int n)
{
 int i,j,lcs[m+1][n+1];
 for(i=0;i<n+1;i++)
  lcs[0][i]=0;
 for(i=0;i<m+1;i++)
  lcs[i][0]=0;
 for(i=1;i<=m;i++)
 {
  for(j=1;j<=n;j++)
  {
   if(x[i-1]==y[j-1])
    lcs[i][j]=1+lcs[i-1][j-1];
   else
    {
     if(lcs[i-1][j]>lcs[i][j-1])
      lcs[i][j]=lcs[i-1][j];
     else
      lcs[i][j]=lcs[i][j-1];
    }
  }
 }
 for(i=0;i<m+1;i++)
 {
  for(j=0;j<n+1;j++)
   printf("%d ",lcs[i][j]);
  printf("\n");
 }
// Find the characters
 i=m;
 j=n;
 int t=lcs[m][n]; 
 printf("\n%d ",t);
 char k[t];
 t-=1;
 while(i!=0 && j!=0)
 {
   if(lcs[i][j]!=lcs[i][j-1])
   {
    k[t]=y[j-1];
    t-=1;
    i-=1;
    j-=1;
   }
   else
    j-=1;
 }
 //printf("%c%c",k[0],k[1]);
 printf("%s\n",k);
}
int main(void)
{
 char x[10],y[10];
 scanf("%s%s",x,y);
 int m,n;
 m=strlen(x);
 n=strlen(y);
 lc(x,y,m,n);
 return 0;
}
  
 
