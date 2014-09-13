
# C++ Interview Question: Null Termination Oddness

## Question and Notes

    There are many ways to define a C-string:
      const size_t size = 3;
      char str_1[] = {'a', 'b', 'c'};
      char str_2[] = "abc";
      char* str_3 = "abc";
      char* str_4 = new char[size];
    
    Explain what the memory looks like after the using the different ways to declare the string.

## Code

    
    
    #include <iostream>
    
    using namespace std;
    
    //! Not safe, but serves the purpose of the example.
    bool isNullTerminated(char* str, size_t size)
    {
      //This is NOT legal for all strings passed. It may crash on some compilers.
      //This is done as a way to illustrate what the memory looks like after the different
      //methods of allocations.
      //Note: on MSVC compiler in debug mode, the compiler adds magic numbers before and
      //      after the memory allocated.
      //See details at: http://en.wikipedia.org/wiki/Magic_number_(programming)
      //  CCCCCCCC	Used by Microsoft's C++ debugging runtime library to mark uninitialised stack memory
      //  CDCDCDCD	Used by Microsoft's C++ debugging runtime library to mark uninitialised heap memory
      if(str[size] == 0)
        return true;
      else
        return false;
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
    
      const size_t size = 3;
      char str_1[] = {'a', 'b', 'c'};
      char str_2[] = "abc";
      char* str_3 = "abc";
      char* str_4 = new char[size];
    
      cout<< isNullTerminated(str_1, size) << endl;
      cout<< isNullTerminated(str_2, size) << endl;
      cout<< isNullTerminated(str_3, size) << endl;
      cout<< isNullTerminated(str_4, size) << endl;
    
      /*
      Prognosis only these two constructs automatically put a NULL termination at size +1
      in the array of characters:
        - char str_2[] = "abc";
        - char* str_3 = "abc";
      */
      
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    0
    1
    1
    0
    End

