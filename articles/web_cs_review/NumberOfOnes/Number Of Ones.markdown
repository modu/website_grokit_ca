
# C++ Interview Question: Number Of Ones

## Question and Notes



## Code

    
    #include <iostream>
    #include <vector>
    #include <cassert>
    
    using namespace std;
    
    int nOnes(unsigned int n)
    {
      int nOnes = 0;
      while(n > 0)
      {
        if((n & 0x1) == 1)
          ++nOnes;
        n = n >> 1;
      }
      return nOnes;
    }
    
    int nOnes_Fast(unsigned int n)
    {
      int nOnes = 0;
      while(n > 0)
      {
        n = n & (n - 1);
        ++nOnes;
      }
      return nOnes;
    }
    
    bool isMultipleOfTwo(unsigned int n)
    {
      if(n <= 1)
        return false;
      return (n & (n - 1)) == 0 ? true : false;
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
      
      cout<< nOnes(0) <<endl;
      cout<< nOnes(1) <<endl;
      cout<< nOnes(2) <<endl;
      cout<< nOnes(3) <<endl;
      cout<< nOnes(7) <<endl;
      cout<< nOnes(255) <<endl;
      cout<< nOnes(256) <<endl;
    
      cout<< nOnes_Fast(0) <<endl;
      cout<< nOnes_Fast(1) <<endl;
      cout<< nOnes_Fast(2) <<endl;
      cout<< nOnes_Fast(3) <<endl;
      cout<< nOnes_Fast(7) <<endl;
      cout<< nOnes_Fast(255) <<endl;
      cout<< nOnes_Fast(256) <<endl;
    
      cout<<"--"<<endl;
    
      cout<< isMultipleOfTwo(0) << endl;
      cout<< isMultipleOfTwo(1) << endl;
      cout<< isMultipleOfTwo(2) << endl;
      cout<< isMultipleOfTwo(3) << endl;
      cout<< isMultipleOfTwo(4) << endl;
      cout<< isMultipleOfTwo(200) << endl;
      cout<< isMultipleOfTwo(201) << endl;
      cout<< isMultipleOfTwo(255) << endl;
      cout<< isMultipleOfTwo(256) << endl;
      
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    0
    1
    1
    2
    3
    8
    1
    0
    1
    1
    2
    3
    8
    1
    --
    0
    0
    1
    0
    1
    0
    0
    0
    1
    End

