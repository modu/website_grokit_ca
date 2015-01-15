#include <thread>
#include <iostream>

using namespace std;

class Counter
{
    public:
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

void hello()
{
    std::cout << "Hello from thread " << std::endl;
}

int main()
{
    Counter counter = Counter();

    thread t1(hello);
    t1.join();

    return 0;
}

