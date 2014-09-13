
# C++ Interview Question: Byte Padding

## Question and Notes

    Explain the concept of memory padding.
    Given the classes declarations below, can you predict how big they will be?
    Can you re-order the member data to have smaller classes?
    What would be the output compiled on a 32 bit system? On a 64 bit system?
    
    Notes:
      - The output is architecture/compiler dependent. Be able to __explain__ the result obtained, and discuss what may vary on a diffent compiler/architecture.
      - Compiled/executed as a 32 bit program.
      - See: http://en.wikipedia.org/wiki/Byte_padding

## Code

    
    #include <iostream>
    
    using namespace std;
    
    class Class0
    {
    public:
    };
    
    class Class1
    {
    public:
      static void fn(){}
    };
    
    class ClassA
    {
    public:
    
      void aFn(){};
    
      int* a;
    };
    
    class ClassB
    {
    public:
    
      virtual void aFn(){};
    
      int* a;
    };
    
    //http://en.wikipedia.org/wiki/Virtual_function_pointer#Implementation
    class ClassC
    {
    public:
    
      virtual void aFn(){};
      virtual void aFn_2(){};
    
      int* a;
    };
    
    //http://en.wikipedia.org/wiki/Byte_padding#Data_structure_padding
    class PaddingLoss
    {
    public:
      char a;
      int b;
    };
    
    class PaddingLoss2
    {
    public:
      int a;
      char b;
    };
    
    class PaddingLoss3
    {
    public:
      int a;
      char b;
      char c;
    };
    
    class NoPaddingLoss
    {
    public:
      int a;
      char b;
      char c;
      char d;
      char e;
    };
    
    class PaddingLoss4
    {
    public:
      int a;
      char b;
      char c;
      char d;
      char e;
      char f;
    };
    
    int main()
    {
      cout<<"Begin"<<endl;
      
      cout<< sizeof(Class0) <<endl; //1 byte, see http://stackoverflow.com/questions/621616/c-what-is-the-size-of-an-object-of-an-empty-class
      cout<< sizeof(Class1) <<endl; //same
      cout<< sizeof(ClassA) <<endl; //4 bytes for 1 pointer
      cout<< sizeof(ClassB) <<endl; //8 bytes: 1 pointer, 1 virtual table pointer
      cout<< sizeof(ClassC) <<endl; //same, not bigger when add functions
    
      cout<< sizeof(PaddingLoss) <<endl;   // 8 bytes, char takes 1, int is 4-byte aligned
      cout<< sizeof(PaddingLoss2) <<endl;  // 8 bytes -- class must be 4-byte aligned
      cout<< sizeof(PaddingLoss3) <<endl;  // 8 bytes -- class must be 4-byte aligned
      cout<< sizeof(NoPaddingLoss) <<endl; // 8 bytes: 4 for int, 4*1 for char 
      cout<< sizeof(PaddingLoss4) <<endl;  // 12 bytes -- class must be 4-byte aligned, 
                                           //             one additional byte 'takes' 4
    
      // 64 bits: still 4-byte-aligned, but pointer consume 8 bytes
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    1
    1
    4
    8
    8
    8
    8
    8
    8
    12
    End

