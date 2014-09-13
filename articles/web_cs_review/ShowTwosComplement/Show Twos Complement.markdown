
# C++ Interview Question: Show Twos Complement

## Question and Notes

    Explain what two's complement is.
    Why is it used (why not only use a bit for the negation)?
    Explain the code below. 
      What would happen with an int? 
      With an undigned int?
    
    Notes:
      - http://en.wikipedia.org/wiki/Two%27s_complement
      - http://en.wikipedia.org/wiki/Signed_number_representations
      - http://en.wikipedia.org/wiki/Method_of_complements

## Code

    
    #include <iostream>
    
    using namespace std;
    
    int main()
    {
      cout<<"Begin"<<endl;
    
      char a = 1;
      while( a != 0 )
      {
        cout<<(int)a<<endl;
        a = a << 1;
      }
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    1
    2
    4
    8
    16
    32
    64
    -128
    End

