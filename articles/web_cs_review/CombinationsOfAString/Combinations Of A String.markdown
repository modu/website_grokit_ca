
# CS Interview Question: Combinations Of A String

## Code C++

    
    #include <iostream>
    #include <string>
    #include <list>
    #include <cassert>
    
    using namespace std;
    
    void display(const char* letters, const int* num, size_t size)
    {
      string ans;
      ans.resize(size);
      for(size_t i = 0; i < size; ++i)
      {
        ans[i] = letters[ num[i] ];
      }
      cout<<ans<<endl;
    }
    
    //!
    void allUniqueCombinations(const char* letters, size_t nLetters, size_t nBoxesMax)
    {
      for(size_t nBoxes = 1; nBoxes <= nBoxesMax; ++nBoxes)
      {
        int* ansPos = new int[nBoxes];
        for(size_t bn = 0; bn < nBoxes; ++bn)
        {
          ansPos[bn] = bn;
        }
    
        display(letters, ansPos, nBoxes);
    
        for(int bn = nBoxes - 1; bn >= 0; --bn)
        {
          while( ansPos[bn] < (int)(nLetters - 1) && ((bn == nBoxes-1)||(ansPos[bn] + 1 < ansPos[bn+1])) )
          {
            ++ansPos[bn];
            display(letters, ansPos, nBoxes);
          }
        }
    
        delete[] ansPos;
      }
    }
    
    int numOfBinaryOnes(int v)
    {
      int sum = 0;
      while( v > 0 )
      {
        if(v & 0x1)
          ++sum;
        v = v >> 1;
      }
      return sum;
    }
    
    void binMaskToStr(const char* str, size_t strSize, int binMask)
    {
      string ans;
      ans.resize( numOfBinaryOnes(binMask) );
      
      int strPos = 0;
      int ansPos = 0;
      while(binMask > 0)
      {
        if( (binMask & 1) == 1 )
        {
          ans[ansPos] = str[strSize - strPos - 1];
          ++ansPos;
        }
        binMask = binMask >> 1;
        ++strPos;
      }
    
      cout<<ans<<endl;
    }
    
    //! Inneficient (bytes incrementing and counting takes a long time), but original solution
    void allUniqueCombinations_BinaryIncrement(const char* str, size_t strSize, size_t targetLen)
    {
      assert( targetLen <= strSize );
    
      for(size_t i = 0; i <= targetLen; ++i)
      {
        int binMask = 0;
        int nBinOnes = 0;
        while(nBinOnes < (int)strSize)
        {
          ++binMask;
          nBinOnes = numOfBinaryOnes(binMask);
          if(nBinOnes == i)
          {
            binMaskToStr(str, strSize, binMask);
          }
        }
      }
    }
    
    void allUniqueCombinations_BinaryIncrement_Test(const char* str, size_t strSize, size_t nBoxesMax)
    {
      assert( numOfBinaryOnes(0) == 0 );
      assert( numOfBinaryOnes(1) == 1 );
      assert( numOfBinaryOnes(2) == 1 );
      assert( numOfBinaryOnes(3) == 2 );
      assert( numOfBinaryOnes(255) == 8 );
      allUniqueCombinations_BinaryIncrement(str, strSize, nBoxesMax);
    }
    
    void allUniqueCombinationsRecurse(
                                      const char* items, size_t itemsSize, 
                                      size_t nBoxes, char* ans, 
                                      size_t itemLevel, size_t ansLevel)
    {
      if(ansLevel >= nBoxes)
      {
        cout<< ans << endl;
        return;
      }
    
      if( (itemsSize - itemLevel) < (nBoxes-ansLevel) )
        return;
    
      for(size_t i = itemLevel; i < itemsSize; ++i)
      {
        ans[ansLevel] = items[i];
        allUniqueCombinationsRecurse(items, itemsSize, nBoxes, ans, i + 1, ansLevel + 1);
      }
    }
    
    void allUniqueCombinationsRecursive(const char* items, size_t itemsSize, size_t nBoxes)
    {
      for(size_t i = 1; i <= nBoxes; ++i)
      {
        char* ans = new char[i + 1];
        ans[i] = 0;
        allUniqueCombinationsRecurse(items, itemsSize, i, ans, 0, 0);
        delete[] ans;
      }
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
    
      const char letters[] = {'A', 'B', 'C', 'D'};
      const size_t nLetters = sizeof(letters)/sizeof(char);
      const size_t nBoxesMax = nLetters;
      assert( nBoxesMax <= nLetters );
    
      cout<<"allUniqueCombinations:"<<endl;
      allUniqueCombinations(letters, nLetters, nBoxesMax);
      cout<<"allUniqueCombinations_BinaryIncrement_Test:"<<endl;
      allUniqueCombinations_BinaryIncrement_Test(letters, nLetters, nBoxesMax);
      cout<<"allUniqueCombinationsRecursive:"<<endl;
      allUniqueCombinationsRecursive(letters, nLetters, nBoxesMax);
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    allUniqueCombinations:
    A
    B
    C
    D
    AB
    AC
    AD
    BD
    CD
    ABC
    ABD
    ACD
    BCD
    ABCD
    allUniqueCombinations_BinaryIncrement_Test:
    D
    C
    B
    A
    DC
    DB
    CB
    DA
    CA
    BA
    DCB
    DCA
    DBA
    CBA
    DCBA
    allUniqueCombinationsRecursive:
    A
    B
    C
    D
    AB
    AC
    AD
    BC
    BD
    CD
    ABC
    ABD
    ACD
    BCD
    ABCD
    End

