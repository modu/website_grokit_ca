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
    unique_lock<mutex> lock1; // (*counter_lock, defer_lock); 

    Counter()
    {
        counter_lock = unique_ptr<mutex>(new mutex());
        cv = unique_ptr<condition_variable>(new condition_variable());
        lock1 = unique_lock<mutex>(*counter_lock, defer_lock);
    }

    void add()
    {
        lock1.lock();

        if(val > N)
        {
            cout << "Too high! v: " << val << endl;
            cout.flush();
            // defer_lock just means that it does not try to grab the lock at object creation.
            lock1.unlock();
            cv->wait(lock1);
        }

        ++val;
        cv->notify_all();
        lock1.unlock();
    }

    void remove()
    {
        lock1.lock();

        if(val <= 0)
        {
            cout << "Too low! v: " << val << endl;
            cout.flush();
            // defer_lock just means that it does not try to grab the lock at object creation.
            lock1.unlock();
            cv->wait(lock1);
        }

        --val;
        cv->notify_all();
        lock1.unlock();
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

