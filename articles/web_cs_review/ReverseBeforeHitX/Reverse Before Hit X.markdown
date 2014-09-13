
# C++ Interview Question: Reverse Before Hit X

## Question and Notes

    Reverse all the words in a string before you encounter a word which has 'x' in it.
    "Hi, I like Microsoft's axis on Seattle." -> "Microsoft's like I Hi, axis on Seattle."
    
    Notes:
    - &((*ans)[writePos]) addressing is it correct?
      -->
      -->
    - @tag review DONT FORGET the \0 at the end of str!

## Code

    
    #include <iostream>
    #include <cassert>
    
    using namespace std;
    
    //! Not in place version (not optimal)
    void invertStringBeforeWordWithX(const char* str, char** ans)
    {
      //1. Allocate memory and return for simple cases
      size_t strSize = strlen(str);// O(n)
      (*ans) = new char[strSize + 1];
      //memset(*ans, 0, strSize);// O(n) -- for debug
      (*ans)[strSize] = 0;
      if(strSize <= 1)
      {
        memcpy(*ans, str, strSize);//Copy in case len of 1
        return;
      }
    
      //2. Locate first X
      bool foundX = false;
      size_t wordEndBefX = 0;
      for(size_t i = 0; i < strSize; ++i)
      {
        if( (str[i] == ' ') && (i >= 1) )
        {
          wordEndBefX = i - 1;
        }
        if( (str[i] == 'x') || (str[i] == 'X') )
        {
          foundX = true;
          break;
        }
      }
      if(!foundX)
      {
        wordEndBefX = 0;
      }
      
      //3.1 Invert string between 0 and X word
      size_t writePos = 0;
      size_t endWord = wordEndBefX;
      for(int i = (int)endWord; i >= 0; --i)
      {
        if( ((str[i] == ' ') || (i == 0)) && (i + 1 < (int)strSize) )
        {
          if( i == 0 )
            i = -1;//This is not very clean, 'last pass fix' :(
          memcpy( &((*ans)[writePos]), &str[i+1], endWord - i );
          writePos += endWord - i;
          if(i - 1 > 0)
            endWord = i - 1;
          else
            endWord = 0;
    
          if( writePos < wordEndBefX )
          {
            (*ans)[writePos] = ' ';
            ++writePos;
          }
        }
      }
    
      //3.2 Copy rest of string
      if( wordEndBefX + 1 < strSize )
      {
        memcpy( &((*ans)[writePos]), &str[wordEndBefX + 1], strSize - (wordEndBefX + 1) );
      }
    }
    
    //@tag not trivial, review
    void inplaceInvert(char* str, size_t wBegin, size_t wEnd)
    {
      if( wBegin >= wEnd )
        return;
    
      for(size_t i = wBegin; i < wBegin + (wEnd - wBegin + 1)/2; ++i)
      {
        char tmp = str[i];
        str[i] = str[wEnd - (i - wBegin)];
        str[wEnd - (i - wBegin)] = tmp;
      }
    }
    
    void inplaceWordInvert(char* str, size_t strSize, size_t invEnd)
    {
      if(invEnd == 0)
        return;
      if(strSize <= 1)
        return;
    
      inplaceInvert(str, 0, invEnd);
    
      size_t wBegin = 0;
      for(size_t i = 0; i <= invEnd; ++i)
      {
        if( (i < strSize - 1) && (str[i] == ' ') && (str[i+1] != ' ') )
        {
          wBegin = i + 1;
        }
        if( ((i == strSize - 1) && (str[i] != ' ')) ||
            ( (str[i] != ' ') && (str[i+1] == ' ')) )
    
        {
          inplaceInvert(str, wBegin, i);
        }
      }
    }
    
    //! Inplace version @tag DID MANY MISTAKES, REVIEW
    void invertStringBeforeWordWithX_Inplace(char* str)
    {
      size_t strSize = strlen(str);
    
      if(strSize <= 1)
        return;
    
      size_t invEnd = 0;
      size_t lastLetBefLastSpace = 0;
      bool isXDetected = false;
      for(size_t i = 0; i < strSize; ++i)
      {
        if(str[i] == 'x' || str[i] == 'X')
        {
          isXDetected = true;
          break;
        }
        if((i + 1 < strSize) && ((str[i] != ' ') && (str[i+1] == ' ')) )
        {
          invEnd = i;
        }
      }
    
      if(!isXDetected)
        return;
      else
        inplaceWordInvert(str, strSize, invEnd);
    }
    
    bool test_answer_1(const char* str, const char* expectedAns)
    {
      bool success = false;
    
      char* ans = 0;
      invertStringBeforeWordWithX(str, &ans);
      if( strcmp(ans, expectedAns) != 0 )
      {
        success = false;
        cout<<ans<<" != "<<expectedAns<<endl;
      }
      else
      {
        success = true;
      }
      delete[] ans;
      return success;
    }
    
    bool test_answer_2(const char* str, const char* expectedAns)
    {
      bool success = false;
      size_t strLen = strlen(str);
      char* ans = new char[strLen + 1];
      ans[strLen] = 0;
      memcpy(ans, str, sizeof(char)*strLen);
      
      invertStringBeforeWordWithX_Inplace(ans);
      if( strcmp(ans, expectedAns) != 0 )
      {
        success = false;
        cout<<ans<<" != "<<expectedAns<<endl;
      }
      else
      {
        success = true;
      }
      delete[] ans;
      return success;
    }
    bool test_answer(const char* str, const char* expectedAns)
    {
      bool r = test_answer_1(str, expectedAns);
      r = r & test_answer_2(str, expectedAns);
      return r;
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
      
      assert( test_answer(
                "Hi I axe wear.", 
                "I Hi axe wear.") );
    
      assert( test_answer(
                "Hi, I like Microsoft's axis on Seattle.", 
                "Microsoft's like I Hi, axis on Seattle.") );
    
      assert( test_answer(
                "Hi, I like Microsoft's aXis on Seattle.", 
                "Microsoft's like I Hi, aXis on Seattle.") );
    
      assert( test_answer(
                "", 
                "") );
    
      assert( test_answer(
                "A", 
                "A") );
    
      assert( test_answer(
                "x", 
                "x") );
    
      assert( test_answer(
                "Two words withX I am xtreme crazy.", 
                "words Two withX I am xtreme crazy.") );
    
      assert( test_answer(
                "No letter that contains secret char.", 
                "No letter that contains secret char.") );
    
      assert( test_answer(
              "sent with xlast", 
              "with sent xlast") );
    
      assert( test_answer(
            "a solitary x", 
            "solitary a x") );
    
      assert( test_answer(
            "x is begin", 
            "x is begin") );
    
      assert( test_answer(
              "xfirst in sent", 
              "xfirst in sent") );
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    End

