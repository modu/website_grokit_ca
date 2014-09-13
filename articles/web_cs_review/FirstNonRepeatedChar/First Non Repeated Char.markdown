
# C++ Interview Question: First Non Repeated Char

## Question and Notes

Find the first non-repeated character in a string.

        Ex: 
            total -> o
            aabbccddeeffgig -> i
            aabb -> (nothing)

You can assume that the encoding is ASCII. (Extra: how to solve it if alphabet is UTF-8?).
            
## Code

    
    #include <iostream>
    #include <cassert>
    
    using namespace std;
    
    char firstNonRepeatedChar(const char* str)
    {
      unsigned int occurence_histogram[256];
      memset(occurence_histogram, 0, sizeof(occurence_histogram));
      for(size_t i = 0; str[i] != 0; ++i)
      {
        ++occurence_histogram[str[i]];
      }
      for(size_t i = 0; str[i] != 0; ++i)
      {
        if( occurence_histogram[str[i]] == 1 )
          return str[i];
      }
      return 0;
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
    
      const char* test1 = "total";
      const char* test2 = "teeter";
      const char* test3 = "abcdefghijkllmnopqwrst";
      const char* test4 = "abcdee";
    
      assert( firstNonRepeatedChar(test1) == 'o' );
      assert( firstNonRepeatedChar(test2) == 'r' );
      assert( firstNonRepeatedChar(test3) == 'a' );
      assert( firstNonRepeatedChar(test4) == 'a' );
    
      cout<<"End"<<endl;
      return 0;
    }

## Discussion

Instead of the array, you can use a hash table in the case where the alphabet is not ASCII (UTF-8, etc).
