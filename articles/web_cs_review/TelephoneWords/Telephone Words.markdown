
# C++ Interview Question: Telephone Words

## Question and Notes

    On a typical touch-tone telephone, output all the possible letter-numbers combination that a given number can have.
    
    Ex: 
      1 -> A, B or C
      12 -> AD, AE, AF, BD, BE, BF, CD, ...
    
    Notes:
      - Do not forget dealing with C-string: \0 terminated

## Code

    
    #include <iostream>
    #include <cassert>
    #include <deque>
    #include <string>
    
    using namespace std;
    
    //@tag find if can have arythmetic way to have this
    static const char keypadLookup[] = 
      {
        'A', 'B', 'C', 
        'D', 'E', 'F', 
        'G', 'H', 'I', 
        'J', 'K', 'L', 
        'M', 'N', 'O', 
        'P', 'R', 'S',
        'T', 'U', 'V',
        'W', 'X', 'Y'};
    
    char getCharKey(int telephoneKey, int place)
    {
      assert( telephoneKey >= 0 && telephoneKey <= 9);
      assert( place >= 0 && place <= 2 );
      if( (telephoneKey == 0 || telephoneKey == 1) && place == 0 )
      {
        return telephoneKey + (char)'0';
      }
    
      return keypadLookup[ (telephoneKey-2)*3 + place ];
    }
    
    void enumPossibleThenPrint_RecursiveSol(int phoneNumber[], size_t size, char* phoneChars, size_t i)
    {
      if(i == size)
      {
        phoneChars[i] = 0;//we allocated size+1 to allow for the null-termination
        cout<<phoneChars<<endl;
        return;
      }
    
      if(phoneNumber[i] <= 1 || phoneNumber[i] == 9)
      {
        phoneChars[i] = phoneNumber[i] + (int)'0'; //int to char trick
        enumPossibleThenPrint_RecursiveSol(phoneNumber, size, phoneChars, i + 1);
      }
      else
      {
        for(size_t j = 0; j < 3; ++j)
        {
          phoneChars[i] = getCharKey( phoneNumber[i], j );
          enumPossibleThenPrint_RecursiveSol(phoneNumber, size, phoneChars, i + 1);
        }
      }
    }
    
    //! Relies on the creation of a queue -- very similar to a breadth-first
    //! search in a tree algorithm. This has the disadvantage of requiring to
    //! store all the child nodes when visiting a level of the tree -- memory
    //! inneficient compared to a depth-first search that does not require that
    //! (like the recursive case implemented above or non-recursive after).
    void enumPossibleThenPrint(int phoneNumber[], size_t size, deque<string>& dq)
    {
      assert( dq.size() == 1 );
      size_t lastLevelCases = 1;
      for(size_t i = 0; i < size; ++i)
      {
        size_t thisLevelCases = 0;
        for(size_t j = 0; j < lastLevelCases; ++j)
        {
          string phoneChars = dq.front();
          phoneChars.append("_");
          dq.pop_front();
    
          if(phoneNumber[i] <= 1 || phoneNumber[i] == 9)
          {
            phoneChars[i] = phoneNumber[i] + (int)'0'; //int to char trick
            dq.push_back(phoneChars);
            ++thisLevelCases;
          }
          else
          {
            for(size_t k = 0; k < 3; ++k)
            {
              phoneChars[i] = getCharKey( phoneNumber[i], k );
              dq.push_back(phoneChars);
              ++thisLevelCases;
            }
          }
        }
        lastLevelCases = thisLevelCases;
      }
    
      for(deque<string>::iterator it = dq.begin(); it != dq.end(); ++it)
      {
        cout<<*it<<endl;
      }
    }
    
    bool increment_ifCannotGoBackToLowest(char& c, int no)
    {
      if(c == '0' || c == '1')
        return false;
      else
      {
        if( c == getCharKey(no, 0) )
        {
          c = getCharKey(no, 1);
          return true;
        }
        else if( c == getCharKey(no, 1) )
        {
          c = getCharKey(no, 2);
          return true;
        }
        else
        {
          c = getCharKey(no, 0);
          return false;
        }
      }
    }
    
    void enumPossibleThenPrint_NonRecurFast(int phoneNum[], size_t size)
    {
      //Init lowest-value string
      char* phoneNumChars = new char[size+1];
      phoneNumChars[size] = 0;
      for(size_t i = 0; i < size; ++i)
      {
        phoneNumChars[i] = getCharKey( phoneNum[i], 0 );
      }
    
      //Print base case
      cout<<phoneNumChars<<endl;
    
      int level = size - 1;
      while(1)
      {
        bool incrSuccess = 
          increment_ifCannotGoBackToLowest( phoneNumChars[level], phoneNum[level] );
        if(incrSuccess == true)
        {
          level = size - 1;
          cout<<phoneNumChars<<endl;
        }
        else
          --level;
    
        if(level < 0)
          break;
      }
    
      delete[] phoneNumChars;
    }
    
    
    void printTelephoneWords(int phoneNumber[], size_t size)
    {
      cout<<"Recursive solution:"<<endl;
      char* phoneChars = new char[ size + 1 ];
      phoneChars[size] = 0;
      enumPossibleThenPrint_RecursiveSol(phoneNumber, size, phoneChars, 0);
      delete[] phoneChars;
    
      cout<<"Non-recursive solution:"<<endl;
      deque<string> dq;
      dq.push_back("");//base case
      enumPossibleThenPrint(phoneNumber, size, dq);
    
      cout<<"Non-recursive solution (fast):"<<endl;
      enumPossibleThenPrint_NonRecurFast(phoneNumber, size);
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
      
      int phoneNum[] = {1, 8, 0, 0, 3};
      printTelephoneWords(phoneNum, sizeof(phoneNum)/sizeof(int));
      
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    Recursive solution:
    1T00D
    1T00E
    1T00F
    1U00D
    1U00E
    1U00F
    1V00D
    1V00E
    1V00F
    Non-recursive solution:
    1T00D
    1T00E
    1T00F
    1U00D
    1U00E
    1U00F
    1V00D
    1V00E
    1V00F
    Non-recursive solution (fast):
    1T00D
    1T00E
    1T00F
    1U00D
    1U00E
    1U00F
    1V00D
    1V00E
    1V00F
    End

