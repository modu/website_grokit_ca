#include <thread>
#include <condition_variable>
#include <iostream>
#include <mutex>

using namespace std;

class Counter
{
public:
    static const int N = 10000;
    unique_ptr<mutex> counter_lock;
    unique_ptr<condition_variable> cv;

    Counter()
    {
        counter_lock = unique_ptr<mutex>(new mutex());
        cv = unique_ptr<condition_variable>(new condition_variable());
    }

    void add()
    {
        counter_lock->lock();

        if(val > N)
        {
            cout << "Too high! v: " << val << endl;
            // cv->wait(counter_lock);
        }

        ++val;
        counter_lock->unlock();
    }

    void remove()
    {
        counter_lock->lock();
        --val;
        counter_lock->unlock();
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

    thread t1(fn1, ref(counter));
    thread t2(fn1, ref(counter));
    t1.join();
    t2.join();

    cout << counter.val << endl;

    return 0;
}

