
# C++ Interview Question: Detect Cycle In S L L

## Question and Notes

    - Be careful: the cycle is not necessary at the beginning!
    - The fast solution is not intuitive (I would not have found it).

## Code

    
    #include <iostream>
    #include <cassert>
    
    using namespace std;
    
    class Node;
    bool isCycle(const Node& head);
    
    class Node
    {
    public:
    
      Node()
      {
        next = 0;
        prev = 0;
        child = 0;
        value = -1;
      }
    
      virtual ~Node()
      {
        if(!isCycle(*this))
        {
          delete next;
          delete child;
        }
        else
        {
          //Disable memory cleanup: cycles in graph: would need a
          //class that does the cleanup, not individual nodes.
          // --> Leak that memory!
        }
      }
    
      void addNext(int val)
      {
        next = new Node;
        next->prev = this;
        next->value = val;
      }
    
      void addChild(int val)
      {
        child = new Node;
        child->prev = this;
        child->value = val;
      }
    
      void print()
      {
        class Node* n = this;
        while(n != 0)
        {
          cout<<n->value<<endl;
          if(n->child != 0)
            n->child->print();
          
          n = n->next;
        }
      }
    
      class Node* next;
      class Node* prev;
      class Node* child;
      int value;
    };
    
    void buildListNoCycle(Node& head)
    {
      head.value = 5;
      head.addNext( 33 );
      head.next->addNext( 17 );
      head.next->next->addNext( 2 );
      head.next->next->next->addNext( 1 );
    }
    
    void buildListCycle(Node& head)
    {
      head.value = 5;
      head.addNext( 33 );
      head.next->addNext( 17 );
      head.next->next->addNext( 2 );
      head.next->next->next->next = head.next;
    }
    
    bool isCycle(const Node& head)
    {
      const Node* n = &head;
      if(n->next == 0)
        return false;
      else
        n = n->next;
    
      while(n->next != 0)
      {
        for(const Node* l = &head; l != n; l = l->next)
        {
          if(n->next == l)
            return true;
        }
    
        n = n->next;
      }
    
      return false;
    }
    
    bool isCycle_fast(const Node& head)
    {
      const Node* nSlow = &head;
      const Node* nFast = &head;
    
      if(nFast->next != 0 && nFast->next->next != 0)
      {
        nFast = nFast->next->next;
      }
      else
      {
        return false;
      }
    
      while(nSlow->next != 0 && nFast->next != 0)
      {
        if(nSlow == nFast)
          return true;
    
        if(nSlow->next == 0)
          return false;
        else
          nSlow = nSlow->next;
    
        if(nFast->next != 0 && nFast->next->next == 0)
          return false;
        else
          nFast = nFast->next->next;
      }
    
      return false;
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
      
      Node headCycle;
      buildListCycle( headCycle );
    
      Node headNoCycle;
      buildListNoCycle( headNoCycle );
    
      assert( isCycle(headCycle) == true );
      assert( isCycle_fast(headCycle) == true );
      assert( isCycle(headNoCycle) == false );
      assert( isCycle_fast(headNoCycle) == false );
        
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    End

