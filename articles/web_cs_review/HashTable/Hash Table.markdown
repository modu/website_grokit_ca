
# C++ Interview Question: Hash Table

## Question

Implement a hash table.

Then:

- Discuss the complexity.
- Discuss different ways to handle collision.
- Discuss different hashing strategies.
- Explain how an overly simplistic hashing strategy could be exploited by a hacker.

References:

- \[CormenT_1990\]\(book\) - Introduction to Algorithms::12.2
    - Have to be careful when retrieving items: have to have a stored version
    of the key to make sure the right item is returned in case of hash collision.

## Notes

Hash tables are simply a way to efficiently retrieve information given a key.

Let's say you have a billing system with 1 billion customers. Each customer is represented by a unique name (e.g: {Alice, Bob, Sergio, ...}, no duplicates allowed). If you store them in a simple list, every time you lookup an employee, you have to go through every name in your array and check if the name matches, which is O(n):

        Array of int -> string.
        [0]: Alice
        [1]: Bob
        ...
        [10^9-1]: Sergio

The claim is that we can do lookups in O(1) using a hash table.
        
Wouldn't it be convenient if instead of having to go through the 'n' keys of the array, to have a simple function that maps the name to the integer? For example, convenientFunction("Alice") would yield 0, convenientFunction("Bob") 1, etc. This is the fundamental thing that a hash table does: it uses a __hash function__ to map the key to an integer, then references an internal array with that integer.

However, there are two important problem to solve:

1. A hash function will have collisions (it is possible that hash("Alice") == hash("Bob")). How do you handle those cases?

2. What size should your internal array be? When should you resize it?

For (1.) the answer is that once you get the key to use in the internal array, you have to do a full comparison of that value against the possible collisions. Therefore, your array maps to _list of values_.

        Array of int -> [string].
        [0]: Maurice
        [1]: [Alice, Bob]
        ...
        [N]: Sergio
        
(2.) is a bit harder to answer. Evidently, if your internal array is too small, you will have to do n/s operations for a lookup, which is still O(n). So you need to dynamically expand that internal array as the number of items in the hash table grows in order to keep the O(1) performance.
        
## Short Review on Hash Function

Hash functions are fundamentally simple: they map an large (sometimes infinite) set to a smaller finite set. For example, consider the following function:

        unsigned int hash(unsigned int value)
        {
            return value % 100;
        }
        
It takes any number in [0 ... 2^32] and returns a number in [0 ... 100]. You can implement a hash table by using your internal array size instead of the 100 (then any value is mapped to a valid key of you internal array).

However, in our example, we wanted to convert strings to keys, not integer to keys. You can use a [linear congruential generator](http://en.wikipedia.org/wiki/Linear_congruential_generator) in order to map a string to an integer:

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

Note that the values 1013904223, 1664525 and 4294967296 are not random. The math behind it is not trivial. You want your hash function to have equal probability to yield any key. Not picking those numbers properly will not have that property, which will negatively impact performance.

@@TODO_C: simple example and explanation of what happens when you pick back numbers.
        
### Cryptographic Hash

Note that I am not covering _cryptographic_ hashes here. All the functions that I showed here are trivial to _reverse_: given a key, I can easily find a value that will collide with that key. This is not such a problem in a hash table, but those hash functions could not be used to sign a file for example (it would be trivial to generate a hacked file that passes the hash check).

## Advanced Topic: Why Does The Internal Array Need to Have A Size that is a Prime Number?

This is an advanced topic. Feel free to skip.

@@TODO_B: [...] will finish this section later...

## A Gentle Warning: Never Implement your Own

It is very important to understand how the internals of a hash-table works. However, never implement your own. There are so many ways to implement a hash table that will see to be right, but hide simple bugs or major performance ramifications. Hash tables are so common that they ship in the standard library of almost every language. There is almost never a good reason to build one in-house.

In C++, use:

        #include <unordered_map>

You will need to tell your compiler to use C++11:

        g++ -std=c++11 hash_table.cpp -o hash_table.cpp.bin
        
## Code

Note that this is a simple, non-complete example. This hash table doesn't resize its internal lookup-table, it would never scale in reality. However, it is simple enough to be a good example of the internals of a hash table without being too complicated.

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


## Code Output

        Begin
        Example hashes:
            hash(Alice): 8
            hash(Bob): 10
            hash(Montreal): 25
            hash(Amherst): 66
        HashTable of size 9:
        HashTable[0]: I am a dog, wan wan.
        HashTable[1]: I am a cow, moo moo.
        HashTable[1]: I am an overlord, bahbahabhmaghuuu.
        HashTable[1]: aa
        HashTable[4]: zzz
        HashTable[6]: a
        N.Hash collisions: 2
        zzz
        InvalidEntryAdd
        HashTable of size 9:
        HashTable[0]: I am a dog, wan wan.
        HashTable[0]: InvalidEntryAdd
        HashTable[1]: I am a cow, moo moo.
        HashTable[1]: I am an overlord, bahbahabhmaghuuu.
        HashTable[1]: aa
        HashTable[4]: zzz
        HashTable[6]: a
        N.Hash collisions: 3
        End
        abcd

        map[10]: abcd
        map[132]: 
        g++ -std=c++11 hash_table.cpp -o hash_table.cpp.bin
