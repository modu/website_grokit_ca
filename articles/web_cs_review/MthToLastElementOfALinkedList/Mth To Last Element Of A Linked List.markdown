
# C++ Interview Question: Mth To Last Element Of A Linked List

## Question and Notes



## Code

    
    #include <iostream>
    //#include <cinttypes>
    
    using namespace std;
    
    class Node
    {
    public:
    
      Node(int valIn = -1)
      {
        next = 0;
        val = valIn;
      }
    
      //virtual
      ~Node()
      {
        delete next;
      }
    
      void add(int val)
      {
        Node* n = this;
        while(n->next!=0)
        {
          n = n->next;
        }
        n->next = new Node(val);
      }
    
      void print()
      {
        Node* n = this;
        cout<<"--"<<endl;
        while(n->next!=0)
        {
          cout<<n->val<<endl;
          n = n->next;
        }
        cout<<n->val<<endl;
        cout<<"--"<<endl;
      }
    
      //would usually be private but example...
      Node* next;
      int val;
    };
    
    Node* buildList()
    {
      Node* root = new Node(1);
      root->add(2);
      root->add(3);
      root->add(4);
      root->add(5);
      return root;
    }
    
    //@tag REDO -- easy to make mistake!
    void printNthToLast(Node* root, int n)
    {
      Node* cur = root;
      Node* nToLast = 0;
      
      int nodeNum = 0;
      while(1)
      {
        if(nodeNum == n)
          nToLast = root;
    
        cur = cur->next;
        if(cur == 0)
          break;
    
        if(nToLast != 0)
          nToLast = nToLast->next;
    
        ++nodeNum;
      }
    
      if(nToLast == 0)
        cout<< -1 << endl;
      else
        cout<< nToLast->val << endl;
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
    
      Node* root = buildList();
      root->print();
    
      printNthToLast(root, 0);
      printNthToLast(root, 1);
      printNthToLast(root, 2);
      printNthToLast(root, 3);
      printNthToLast(root, 4);
      printNthToLast(root, 5);
      printNthToLast(root, -1);
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    --
    1
    2
    3
    4
    5
    --
    5
    4
    3
    2
    1
    -1
    -1
    End

