
#include <iostream>
#include <vector>
#include <limits>
#include <stdexcept>
#include <cassert>

using namespace std;

class Heap
{
public:
    
    size_t size()
    {
        return v.size();
    }
    
    int popMax()
    {
        if(v.size() == 0)
            throw runtime_error("Can't pop() empty heap.");
        
        int ret = v[0];
        
        // Remove max, put element that occupies the stop "to empty".
        v[0] = v[v.size()-1];
        v.pop_back();
        
        // "Bubble down".
        int i = 0;
        while(1)
        {
            int l = left(i);
            int r = right(i);
            
            int ilargest = -1;
            if(l == -1 && r == -1)
            {
                return ret;
            }
            else if(l == -1)
            {
                ilargest = r;
            }
            else
            {
                ilargest = v[l] > v[r] ? l : r;
            }
            
            if(v[i] < v[ilargest])
            {
                int t = v[ilargest];
                v[ilargest] = v[i];
                v[i] = t;            
                i = ilargest;
            }
            else
            {
                break;
            }
        }
        
        return ret;
    }
    
    void insert(int vi)
    {
        v.push_back(vi);
        
        int i = v.size() - 1;
        int ui = up(i);
        
        while(ui >= 0)
        {
            if( v[i] > v[ui] )
            {
                int t = v[ui];
                v[ui] = v[i];
                v[i] = t;
            }
            else
            {
                break;
            }
            
            i = ui;
            ui = up(ui);
        }        
    }
    
    const vector<int>& getV()
    {
        return v;
    }
    
private:
    
    int up(int i)
    {
        if(i <= 0)
            return -1;
        
        i = (i -1)/2;
        
        return i;
    }
    
    int left(int i)
    {
        i = 2*i + 1;
        
        if(i >= v.size())
            return -1;
        
        return i;
    }
    
    int right(int i)
    {
        i = 2*i + 2;
        
        if(i >= v.size())
            return -1;
        
        return i;
    }
    
    vector<int> v;
};

int main()
{
    cout<<"begin"<<endl;
    
    vector<int> testV;
    testV.push_back(10);
    testV.push_back(100);
    testV.push_back(40);
    testV.push_back(50);
    testV.push_back(4);
    testV.push_back(35);
    testV.push_back(64);
    testV.push_back(30);
    testV.push_back(12);
    testV.push_back(0);
    testV.push_back(28);
    
    Heap h;
    for(int i = 0; i < testV.size(); ++i)
    {
        h.insert( testV[i] );
    }
    
    cout<<"Heap-as-vector:"<<endl;
    const vector<int>& v = h.getV();
    
    for(int i = 0; i < v.size(); ++i)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl;
    
    int max = numeric_limits<int>::max();
    assert( v.size() == testV.size() );
    while(h.size() > 0)
    {
        int pm = h.popMax();
        cout<<pm<<" ";
        assert( max > pm ); // Assumes no duplicates.
        max = pm;
    }
    cout<<endl;
    
    cout<<"end"<<endl;
    return 0;
}
