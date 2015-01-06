#include <iostream>
#include <cassert>
#include <exception>
#include <limits>
#include <string>

using namespace std;

unsigned int factorialRecursive(unsigned int n)
{
    assert(n >= 0);
    if(n > 1)
        return n * factorialRecursive(n - 1);
    else
        return 1;
}

unsigned int factorialLoop(unsigned int n)
{
    if(n <= 1)
        return 1;

    int fact = 1;
    for(int i = 2; i <= n; ++i)
    {
        // Here you cannot simply check that fact*i < fact in order
        // to guard against overflows -- you have no guarantee that
        // fact*i won't overflow into something > fact.
        fact = fact * i;
    }

    return fact;
}

// This is slow: O(n^2) instead of O(n), but you are guaranteed to
// know when there is an overflow.
unsigned int factorialAdd(unsigned int n)
{
    if(n <= 1)
        return 1;

    int fact = 1;
    for(int i = 2; i <= n; ++i)
    {
        if(fact > numeric_limits<unsigned int>::max())
        {
            throw "Overflow pre-detect.";
        }

        // Implement multiplication as an addition.
        int sum = 0;
        for(int j = 0; j < i; ++j)
        {
            if(sum + fact < sum)
            {
                throw "Overflow detect";
            }

            sum = sum + fact;
        }
        fact = sum;
    }

    return fact;
}

unsigned char factorialLoopShowOverflow(unsigned char n)
{
    if(n <= 1)
        return 1;

    unsigned char fact = 1;
    for(unsigned char i = 2; i <= n; ++i)
    {
        fact = fact * i;
    }

    return fact;
}

// This is a nice "academic" example of using the C++ template system,
// but not very useful in practice.
template<int N>
class Factorial
{
public:
    static const int value = N * Factorial<N - 1>::value;
};

template<>
class Factorial<0>
{
public:
    static const int value = 1;
};

void testFactorial(unsigned int(*fnPtr)(unsigned int))
{
    assert( fnPtr(10) == 3628800 );
    assert( fnPtr(0) == 1 );
    assert( fnPtr(1) == 1 );
    assert( fnPtr(3) == 6 );
}

void printFactorial(unsigned int(*fnPtr)(unsigned int), string name)
{
    cout<<name<<":"<<endl;
    try
    {
        for(unsigned int i = 0; i < 15; ++i)
        {
            cout<<i<<": "<<fnPtr(i)<<endl;
        }
    }
    catch(...)
    {
        cout<<"Function signaled error, stopping."<<endl;
    }
}

int main()
{
    cout<<"Begin"<<endl;

    //Cannot be used in a function with arbitrary parameter,
    //the value has to be known at compile time to be used
    //in template.
    //(see C2971)
    cout<< Factorial<10>::value <<endl;
    // cout<< Factorial<100>::value <<endl; This would blow-up the compiler.


    printFactorial( &factorialLoop, "factorialLoop" );
    printFactorial( &factorialRecursive, "factorialRecursive" );
    printFactorial( &factorialAdd, "factorialAdd" );

    cout<<"factorialLoopShowOverflow:"<<endl;
    for(unsigned char i = 0; i < 12; ++i)
    {
        cout<<(unsigned int)i<<": "<<(unsigned int)factorialLoopShowOverflow(i)<<endl;
    }

    testFactorial( &factorialLoop );
    testFactorial( &factorialRecursive );
    testFactorial( &factorialAdd );

    cout<<"End"<<endl;
    return 0;
}