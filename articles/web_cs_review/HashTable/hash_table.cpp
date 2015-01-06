
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <cassert>

using namespace std;

//! Assumes the data stored has STLVector-like interface
//! (.size(), operator[], ...)
template<class T_>
class HashTable
{
public:

    typedef T_ DataType;

    class DataWithKey
    {
    public:

        DataWithKey()
        {
            key = 0;
        }

        T_ data;
        int key;
    };

    HashTable()
    {
        m_size = 9;
        m_vListIndex.resize(m_size, list<DataWithKey>());
    }

    size_t hashIntKey(int key) const
    {
        //Using the division method
        return key % m_size;
    }

//! Assumes that the data can be interpreted as a string
    void print() const
    {
        int nCollision = 0;
        cout<<"HashTable of size "<<m_size<<":"<<endl;
        for(size_t i = 0; i < m_vListIndex.size(); ++i)
        {
            if(m_vListIndex[i].size() > 1)
                nCollision += m_vListIndex[i].size() - 1;
            for(typename list<DataWithKey>::const_iterator it = m_vListIndex[i].begin();
                    it != m_vListIndex[i].end();
                    ++it)
            {
                cout<<"HashTable["<<i<<"]: "<<it->data<<endl;
            }
        }

        cout<<"N.Hash collisions: "<<nCollision<<endl;
    }

    void add(int key, const T_& data)
    {
        size_t posInArray = hashIntKey(key);
        DataWithKey dk;
        dk.data = data;
        dk.key = key;
        //Collision resolution by chaining
        list<DataWithKey>& lst = m_vListIndex.at(posInArray);
        //If key already store, replace data
        if(lst.size() != 0)
        {
            for(typename list<DataWithKey>::iterator it = lst.begin();
                    it != lst.end();
                    ++it)
            {
                if(it->key == key)
                {
                    it->data = data;
                    return;
                }
            }
        }
        //No items with that key, store a new one
        m_vListIndex[posInArray].push_back(dk);
    }

    T_& operator[](int key)
    {
        size_t posInArray = hashIntKey(key);
        list<DataWithKey>& lst = m_vListIndex.at(posInArray);
        assert( lst.size() != 0 );

        for(typename list<DataWithKey>::iterator it = lst.begin();
                it != lst.end();
                ++it)
        {
            if(it->key == key)
            {
                return it->data;
            }
        }

        //key not found, user requested invalid data
        add(key, "InvalidEntryAdd"); //@note not sure hot to make work with a complete template system
        return operator[](key);
    }

private:
    size_t                      m_size;
    vector< list<DataWithKey> > m_vListIndex;
};

unsigned int hashString(const string& s)
{
    unsigned int key = 33;

    for(unsigned int i = 0; i < s.size(); ++i)
    {
        // % 4294967296 not necessary, but there for the example.
        key = (1013904223 + key*1664525) % 4294967296;
    }

    return key % 100;
}

int main()
{
    cout<<"Begin"<<endl;

    cout<<"Example hashes:"<<endl;
    cout<<"    hash(Alice): "<<hashString("Alice")<<endl;
    cout<<"    hash(Bob): "<<hashString("Bob")<<endl;
    cout<<"    hash(Montreal): "<<hashString("Montreal")<<endl;
    cout<<"    hash(Amherst): "<<hashString("Amherst")<<endl;

    HashTable<string> ht;
    ht.add(1234, string("I am a cow, moo moo."));
    ht.add(0, string("I am a dog, wan wan."));
    ht.add(1, string("I am an overlord, bahbahabhmaghuuu."));
    ht.add(546, string("a"));
    ht.add(100, string("aa"));
    ht.add(22, string("aaa"));
    ht.add(22, string("zzz"));//should replace

    ht.print();

    cout<<ht[22]<<endl;

    cout<<ht[999]<<endl; //does not exist, will create an empty entry and return it

    ht.print();

    //Note: would be better to have interface like: ht[22] = "a", cout<<ht[22] -> "a"

    cout<<"End"<<endl;

    //Check if same 'add on lookup-non-exist' behavior with STL map
    map<int, string> mTest;
    mTest[10] = "abcd";
    cout<<mTest[10]<<endl;
    cout<<mTest[132]<<endl;

    for(map<int, string>::iterator it = mTest.begin(); it != mTest.end(); ++it)
    {
        cout<<"map["<<it->first<<"]: "<<it->second<<endl;
    }



    return 0;
}
