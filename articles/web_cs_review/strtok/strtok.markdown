
# C++ Interview Question: strtok

## Question and Notes

    - If expect a lot of tokens, could speed-up by building a lookup table of
      the lookup chars.
    - Careful of keeping the original ptr to string through a static pointer
    - Dont use memcpy(...) for copying string -- it is easy to forget the NULL terminator

## Code

    
    #include <iostream>
    
    using namespace std;
    
    char* myStrtok (char* str_, const char* delims)
    {
      size_t delimSize = strlen(delims);
      
      static size_t strLen = 0;
      static size_t wBeg = 0;
      static size_t wEnd = 0;
      static char* str = 0;
      
      if(str_ != 0)
      {
        str = str_;
        strLen = strlen(str_);
        wBeg = 0;
        wEnd = 0;
      }
      else
      {
        wBeg = wEnd + 1;
      }
    
      if(wBeg >= strLen)
        return 0;
    
      size_t loc = wBeg;
      
      //Forward to first non-delim
      while( str[loc] != 0 )
      {
        bool foundToken = false;
        for(size_t i = 0; i < delimSize; ++i)
        {
          if( str[loc] == delims[i] )
          {
            wBeg = loc + 1;
            foundToken = true;
          }
        }
        
        if( foundToken == false )
        {
          wBeg = loc;
          break;
        }
    
        ++loc;
      }
    
      //Advance to next delim
      while( str[loc] != 0 )
      {
        for(size_t i = 0; i < delimSize; ++i)
        {
          if( str[loc] == delims[i] )
          {
            str[loc] = 0;
            wEnd = loc;
            return &str[wBeg];
          }
        }
        ++loc;
      }
    
      wEnd = loc;
      return &str[wBeg];
    }
    
    void test_strtok(char* str, char* delims)
    {
      cout<<endl<<"Orig. str: "<<str<<endl;
    
      char* str_c1 = new char[ strlen(str)+1 ];
      char* str_c2 = new char[ strlen(str)+1 ];
      strcpy(str_c1, str);
      strcpy(str_c2, str);
    
      cout<<endl<<"C lib. result:"<<endl;
      char * pch = 0;
      pch = strtok (str_c1, delims);
      while (pch != 0)
      {
        cout<<pch<<endl;
        pch = strtok(0, delims);
      }
    
      cout<<endl<<"My result:"<<endl;
      pch = 0;
      pch = myStrtok (str_c2, delims);
      while (pch != 0)
      {
        cout<<pch<<endl;
        pch = myStrtok(0, delims);
      }
    
      delete[] str_c1;
      delete[] str_c2;
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
    
      char str_q1[] ="- This, a sample string.";
      test_strtok(str_q1, " ,.-");
    
      char str_q2[] ="- This, a sample string";
      test_strtok(str_q2, " ,.-");
    
      char str_q3[] ="- This, a sample string.";
      test_strtok(str_q3, "");
    
      char str_q4[] ="";
      test_strtok(str_q4, "");
    
      char str_q5[] ="";
      test_strtok(str_q5, "asdasd");
    
      char str_q6[] =".,.,..,,..,,.";
      test_strtok(str_q6, ".,");
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    
    Orig. str: - This, a sample string.
    
    C lib. result:
    This
    a
    sample
    string
    
    My result:
    This
    a
    sample
    string
    
    Orig. str: - This, a sample string
    
    C lib. result:
    This
    a
    sample
    string
    
    My result:
    This
    a
    sample
    string
    
    Orig. str: - This, a sample string.
    
    C lib. result:
    - This, a sample string.
    
    My result:
    - This, a sample string.
    
    Orig. str: 
    
    C lib. result:
    
    My result:
    
    Orig. str: 
    
    C lib. result:
    
    My result:
    
    Orig. str: .,.,..,,..,,.
    
    C lib. result:
    
    My result:
    
    End

