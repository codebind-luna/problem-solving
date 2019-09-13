#include <iostream>
#include <algorithm>
#define abs(x) (((x)>=0)?(x):-(x))
using namespace std;

int N,K,A[3000]; bool picked[3000];
void input(){
    cin>>N>>K; if(K*2>N) K=N-K;
    for(int i=0;i<N;i++) {cin>>A[i]; picked[i]=false;}
    sort(A,A+N); int m=(N-K*2)/2+1,i;
    for(i=0;i<K;i++) picked[m+i*2]=true;
}
long result(){
    int i,j; long total=0;
    for(i=0;i<N;i++) if(picked[i])
        for(j=0;j<N;j++) if(!picked[j])
            total+=abs(A[i]-A[j]);
    return total;
}
int main() {
    input(); cout<<result()<<endl;
    return 0;
}