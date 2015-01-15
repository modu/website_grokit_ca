#include <thread>
#include <iostream>

using namespace std;

class Counter
{
    public:
        static const int N = 10000;

        void add()
        {
            ++val;
        }

        void remove()
        {
            --val;
        }

    private:
        int val = 0;
};

void fn1(Counter& counter)
{
    for(int i = 0; i < Counter.N; ++i)
    {
        counter.add();
    }
}

int main()
{
    Counter counter = Counter();

    thread t1(fn1);
    thread t2(fn1);
    thread t3(fn2);
    thread t4(fn2);
    t1.join();

    return 0;
}

