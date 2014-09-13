
#include <iostream>
#include <cmath>

using namespace std;

bool isPowerOfTwo(unsigned int n)
{
    if(n < 2) return 0;
    return (n & (n-1)) == 0;
}

int main()
{
    cout<<"Begin"<<endl;

    cout<<"isPowerOfTwo"<<endl;
    for(int x = 0; x < 10000; ++x)
    {
    if( isPowerOfTwo(x) )
        cout<<x<<endl;
    }

    cout<<"End"<<endl;
    return 0;
}
