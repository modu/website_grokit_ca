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

        int val = 0;
};

void fn1(Counter& counter)
{
    for(int i = 0; i < Counter::N; ++i)
    {
        counter.add();
    }
}

int main()
{
    Counter counter = Counter();

    thread t1(fn1, std::ref(counter));
    thread t2(fn1, std::ref(counter));
    t1.join();
    t2.join();

    cout << counter.val << endl;

    return 0;
}

