#include<iostream>
using namespace std;
int getPower(int x,int y){
    int ans=1;
    if (y<0) return 0;
    else if (y==0) return 1;

    for(int i=0;i<y;i++){
        ans=ans*x;
    }
    return ans;

}
double getPower(double x, int y){
    double ans=1;
    if (y<0) return 0.0;
    else if (y==0) return 1;

    while(y!=0){
        y=y-1;
        ans*=x;

    }
    return ans;



}

int main(){
    int a,m=0;
    double b=0.0;
    int ansi=0;
    double ansd=0.0;

    cin>>a>>b>>m;
    ansi=getPower(a,m);
    ansd=getPower(b,m);
    cout<<ansi<<" "<<ansd;

}
