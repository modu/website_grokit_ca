
# C++ Interview Question: String Searching

## Question and Notes



## Code

    
    #include <iostream>
    #include <cassert>
    
    using namespace std;
    
    int stringSearch(const char* str, const char* w)
    {
      size_t strSize = strlen(str);
      size_t wSize = strlen(w);
    
      if( (wSize == 0) || (wSize > strSize) )
        return -1;
    
      int matchPos = -1;
      //@tag check condition
      for(size_t i = 0; (i < strSize) && (matchPos == -1); ++i)
      {
        if( (strSize-i) >= wSize )
          for(size_t j = 0; j < wSize; ++j)
          {
            if(str[i+j] != w[j])
            {
              break;
            }
            else
            {
              if(j == wSize - 1)
                matchPos = i;
            }
          }
      }
    
      return matchPos;
    }
    
    //This is not a currect solution, see tests-cases that fail for that function
    int stringSearch_faster(const char* str, const char* w)
    {
      size_t strSize = strlen(str);
      size_t wSize = strlen(w);
      for(size_t i = 0; i < strSize; ++i)
      {
        size_t nSkip = 0;
        for(size_t j = 0; j < wSize; ++j)
        {
          if(i + j >= strSize)
            break;
          if(str[i+j] != w[j])
            break;
          
          //Do not increment the first time around,
          //i increments by one anyway
          if(j != 0)
            ++nSkip;
    
          if(j == wSize - 1)
            return i;
        }
    
        i += nSkip;
      }
      return -1;
    }
    
    // KMP (Knuth-Morris-Pratt) algorithm
    // http://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
    // http://www.inf.fh-flensburg.de/lang/algorithmen/pattern/kmpen.htm
    int stringSearch_KNP(const char* str, const char* w)
    {
      //@tag TODO KNP O(n) string search
      return -1;
    }
    
    int useStd(const char* str, const char* w)
    {
      char* rv = strstr((char*)str, w);
      if(rv == 0)
        return -1;
    
      for(size_t i = 0; i < strlen(str); ++i)
      {
        if( rv == &str[i])
          return i;
      }
      return -1;
    }
    
    void test_fn( int(*pt2Func)(const char* str, const char* w) )
    {
    
      //cout<< pt2Func("This is a cucucucucup of tea.", "cup") << endl;
    
      //cout<< pt2Func("ABC ABCDAB ABCDABCDABDE", "ABCDABD") << endl;
      
      assert( pt2Func("aabc", "abc") == 1 );
      assert( pt2Func("ababc", "abc") == 2 );
      assert( pt2Func("This is a cucucucucup of tea.", "cup") == 18 );
      assert( pt2Func("This is a cup of tea.", "cup") == 10 );
      assert( pt2Func("This is a cup of tea.", "cups") == -1 );
      assert( pt2Func("This is a cusp of tea.", "cup") == -1 );
      assert( pt2Func("This is cu a cusp cup of tea.", "cup") == 18 );
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
    
      test_fn( useStd );
      test_fn( stringSearch );
      //test_fn( stringSearch_faster );
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    End

