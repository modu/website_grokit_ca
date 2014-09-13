
# C++ Interview Question: Permutations Of A String

## Question and Notes

    TODO: Recursive version for comparison 
    @tag review and be able to do fast as a 'list all possible cases given realm X'
    
    @tag ERROR review: 
      
      char* items = "abc";
      allPermutations(items, sizeof(items)/sizeof(char));
      --> THIS IS AN ERROR: because the item size contains the NULL-termination!

## Code

    
    #include <iostream>
    #include <deque>
    #include <string>
    #include <cassert>
    
    using namespace std;
    
    //!@brief 'Insertion' solution: each letter
    //!@note This is a very space-inneficient solution: requires to store
    //!      all the possible answers in memory at once.
    deque<string> getAllPossiblePermutationsOfStr(const char* cc_str)
    {
      //Assume a character that will never be used, for debug
      const char unused_space = '_';
      string str(cc_str);
    
      string init_str;
      init_str.resize( str.size(), unused_space );
    
      deque<string> q1;
      deque<string> q2;
      deque<string>& next_queue = q1;
      deque<string>& curr_queue = q2;
    
      curr_queue.push_back( init_str );
      
      for(size_t i = 0; i < str.size(); ++i)
      {
        while(!curr_queue.empty())
        {
          string str_curr = curr_queue.front();
          curr_queue.pop_front();
          for(size_t j = 0; j < str_curr.size(); ++j)
          {
            if(str_curr[j] == unused_space)
            {
              string str_add = str_curr;
              str_add[j] = str[i];
              next_queue.push_back(str_add);
            }
          }
        }
        //Swap the queues references
        deque<string>& tmp = curr_queue;
        curr_queue = next_queue;
        next_queue = tmp;
        next_queue.clear();
      }
      
      return curr_queue;
    }
    
    //! @brief 'Insertion' solution, recursive
    //! More efficient than the queue version: 1/(strSize) of the tree at time is completely
    //! expanded in memory. This has the disadvantage that one char is 'forbidden'.
    void allPossiblePermutationsOfStrMarkInStr_Recursive(const char* str, size_t strSize, char* ans, int level = 0)
    {
      static const char emptyChar = '_';
      if(level == 0)
        memset(ans, emptyChar, strSize);
      else if (level == strSize)
      {
        cout<<ans<<endl;
        return;
      }
    
      for(size_t i = 0; i < strSize; ++i)
      {
        if(ans[i] == emptyChar)
        {
          string ans_nextLevel(ans);
          ans_nextLevel[i] = str[level];
          allPossiblePermutationsOfStrMarkInStr_Recursive(str, strSize, (char*)ans_nextLevel.c_str(), level + 1);
        }
      }
    }
    
    //! Use a 'bool mask' in order to keep track which letter was used
    void allPossiblePermutationsOfStrMarkInArray_RecurseFn(
      const char* str, size_t strSize, char* ans, bool* letterUsed, int recurseLevel)
    {
      if(strSize == recurseLevel)
      {
        cout<<ans<<endl;
        return;
      }
    
      for(size_t iLet = 0; iLet < strSize; ++iLet)
      {
        if(letterUsed[iLet] == false)
        {
          letterUsed[iLet] = true;
          ans[recurseLevel] = str[iLet];
          allPossiblePermutationsOfStrMarkInArray_RecurseFn(str, strSize, ans, letterUsed, recurseLevel + 1);
          letterUsed[iLet] = 0;
        }
      }
    }
    
    void allPossiblePermutationsOfStrMarkInArray_Recursive(const char* str, size_t strSize, char* ans)
    {
      bool* letterUsed = new bool[strSize];
      memset(letterUsed, false, strSize);
      allPossiblePermutationsOfStrMarkInArray_RecurseFn(str, strSize, ans, letterUsed, 0);
      delete[] letterUsed;
    }
    
    template<class T>
    void print(const T& v)
    {
      for(T::const_iterator it = v.begin(); it!= v.end(); ++it)
      {
        cout<<*it<<endl;
      }
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
      
      const char* str = "abc";//auto null-terminated
      const size_t strLen = strlen(str);
    
      cout<<"Queue solution:"<<endl;
      print( getAllPossiblePermutationsOfStr(str) );
        
      char* ans = 0 ;
    
      cout<<"Recursive solution (str marks):"<<endl;
      ans = new char[strLen + 1];
      ans[strLen] = 0;
      allPossiblePermutationsOfStrMarkInStr_Recursive(str, strLen, ans);
      delete[] ans;
    
      cout<<"Recursive solution (bitmask):"<<endl;
      ans = new char[strLen + 1];
      ans[strLen] = 0;
      allPossiblePermutationsOfStrMarkInArray_Recursive(str, strLen, ans);
      delete[] ans;
    
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    Queue solution:
    abc
    acb
    bac
    cab
    bca
    cba
    Recursive solution (str marks):
    abc
    acb
    bac
    cab
    bca
    cba
    Recursive solution (bitmask):
    abc
    acb
    bac
    bca
    cab
    cba
    End

