
# C++ Interview Question: Swap Without Temporary Variable

## Question and Notes


## Code

    
    #include <iostream>
    
    using namespace std;
    
    //Would not do that in real code, but more readable for the example
    #define xor ^
    
    template<class T>
    void switchInPlace(T& a, T&b)
    {
      a = a xor b;
      b = a xor b;
      a = a xor b;
    }
    #undef xor
    
    void strInverInPlace(char* str)
    {
      size_t strLen = strlen(str);
      for(size_t i = 0; i < strLen/2; ++i)
      {
        switchInPlace( str[i], str[strLen-i-1] );
      }
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
    
      char str[] = "This is a string to invert.";
      
      strInverInPlace(str);
    
      cout<<str<<endl;
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    .trevni ot gnirts a si sihT
    End

