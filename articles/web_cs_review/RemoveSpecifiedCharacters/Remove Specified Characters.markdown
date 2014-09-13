
# C++ Interview Question: Remove Specified Characters

## Question and Notes

    Given two arrays: one of source characters, one of characters to remove.
    Remove all the characters of the second array in the first one.
    
    Ex:
      I am a cow. Moo Moo.", "cow" --> "I am a . M M."
      (The cow was transformed by an M&M by our function)
      
    Tricky:
      - Pass the pointer to allow modification of the pointer, not the
        data pointed to.
      --> char** out
      --> mod: (*out)[i] = ... ; *out[i] = would CRASH

## Code

    
    #include <iostream>
    #include <cassert>
    #include <cmath>
    
    using namespace std;
    
    void removeChars(const char str[],const char remove[], char** out)
    {
      //build lookup-table of caracters to delete for fast-lookup
      bool charRem[256];
      memset( charRem, false, 256*sizeof(bool) );
      for(size_t i = 0; i < strlen(remove); ++i)
      {
        charRem[remove[i]] = true;
      }
    
      const int size_str = strlen(str);
      *out = new char[size_str];
      memset(*out, 0, size_str * sizeof(char) );
      
      int out_i = 0;//out ptr
      for(int i = 0; i < size_str; ++i)
      {
        if(charRem[str[i]] == false)
        {
          (*out)[out_i] = str[i];
          out_i++;
        }
        //else: nop
      }
    
      //zero-terminate output string
      (*out)[out_i] = 0;
    }
    
    void removeChars_InPlace(char str[], const char remove[])
    {
      size_t remTableSize = (size_t)pow(2.0, sizeof(char)*8.0 );
      bool* remTable = new bool[ remTableSize ];
      memset(remTable, false, remTableSize);
    
      for(size_t i = 0; i < sizeof(remove); ++i)
      {
        remTable[ (unsigned char)remove[i] ] = true;
      }
    
      size_t wPos = 0;
      size_t rPos = 0;
      for(size_t i = 0; i < strlen(str); ++i)
      {
        if( remTable[ (unsigned char)str[i] ] == false )
        {
          if( rPos > wPos )
          {
            str[wPos] = str[rPos];
          }
          ++wPos;
        }
        ++rPos;
      }
    
      if( rPos > wPos )
        str[wPos] = 0;
    }
    
    void test(char* str, const char* remove, const char* answer)
    {
      char* out = 0;
      //removeChars(str, remove, &out);
    
      //assert(out != 0);
      //if(strcmp(out, answer) != 0)
      //{
      //  cout<<"Error: "<<out<<" != "<<answer<<endl;
      //}
      
      string str_(str);//Just to make the input string modifiable
      removeChars_InPlace((char*)str_.c_str(), remove);
      if(strcmp(str_.c_str(), answer) != 0)
      {
        cout<<"Error: "<<str_.c_str()<<" != "<<answer<<endl;
      }
    
      delete[] out;
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
      
      test("abcdef", "c", "abdef");
      test("I am a cow. Moo Moo.", "cow", "I am a . M M.");
      test("This is a bird, it flies higher than a 787.", "b8.,", "This is a ird it flies higher than a 77");
      
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    Error: def != abdef
    End

