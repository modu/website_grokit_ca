#include <thread>
#include <condition_variable>
#include <iostream>
#include <mutex>

using namespace std;

class Counter
{
public:
    static const int N = 10000;
    //unique_ptr<mutex> counter_lock;
    //unique_ptr<condition_variable> cv;
    //unique_lock<mutex> lock1; // (*counter_lock, defer_lock); 

    unique_ptr<mutex> lock;

    Counter()
    {
        unique_lock<mutex> signal_lock = unique_lock<mutex>(*unique_ptr<mutex>(new mutex()));
      unique_ptr<condition_variable>  cv = unique_ptr<condition_variable>(new condition_variable());
        //// defer_lock just means that it does not try to grab the lock at object creation.
        //lock1 = unique_lock<mutex>(*counter_lock, defer_lock);
        //
        //oooasd

        lock = unique_ptr<mutex>(new mutex());
    }

    void add()
    {
        lock->lock();

        //if(val > N)
        //{
        //    cout << "Too high! v: " << val << endl;
        //    cout.flush();
        //    lock->unlock();
        //    cv->wait(lock2);
        //    lock->lock();
        //}

        ++val;
        lock->unlock();
        
        //cv->notify_all();
    }

    void remove()
    {
        lock->lock();

        //if(val <= 0)
        //{
        //    cout << "Too low! v: " << val << endl;
        //    cout.flush();
        //    lock->unlock();
        //    cv->wait(lock2);
        //    lock->lock();
        //}

        --val;
        lock->unlock();

        //cv->notify_all();
    }

    int val = 0;
};

void fn1(Counter& counter)
{
    for(int i = 0; i < Counter::N; ++i)
    {
        counter.add();
    }

    // cout<< "thread done: " << counter.val << endl;
}

void tests()
{
    for(int i = 0; i < 10; ++i)
    {
        Counter counter = Counter();
        thread t1(fn1, ref(counter));
        thread t2(fn1, ref(counter));
        t1.join();
        t2.join();
        cout << counter.val << endl;
    }
}

int main()
{
    cout << "start" << endl;
    tests();
    return 0;
}

