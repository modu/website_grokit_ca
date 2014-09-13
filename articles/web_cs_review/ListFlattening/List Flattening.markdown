
# C++ Interview Question: List Flattening

## Question and Notes

Given a fancy linked-list with a next node as well as a child node, write an algorithm to flatten the list (only next nodes, no more child nodes -- the list must contain all the original elements).

## Code

    #include <iostream>
    #include <cassert>
    
    using namespace std;
    
    class node
    {
    public:
    
      node()
      {
        next = 0;
        prev = 0;
        child = 0;
        value = -1;
      }
    
      virtual ~node()
      {
        delete next;
        delete child;
      }
    
      void addNext(int val)
      {
        next = new node;
        next->prev = this;
        next->value = val;
      }
    
      void addChild(int val)
      {
        child = new node;
        child->prev = this;
        child->value = val;
      }
    
      void print()
      {
        class node* n = this;
        while(n != 0)
        {
          cout<<n->value<<endl;
          if(n->child != 0)
            n->child->print();
          
          n = n->next;
        }
      }
    
      class node* next;
      class node* prev;
      class node* child;
      int value;
    };
    
    void build_list(node& head)
    {
      head.value = 5;
      head.addNext( 33 );
      head.next->addNext( 17 );
      head.next->next->addNext( 2 );
      head.next->next->next->addNext( 1 );
    
      head.addChild( 6 );
      head.child->addNext( 25 );
      head.child->next->addNext( 6 );
      head.child->next->addChild( 8 );
      head.child->next->next->addChild( 9 );
      head.child->next->next->child->addChild( 7 );
    
      head.next->next->next->addChild( 2 );
      head.next->next->next->child->addNext( 7 );
      head.next->next->next->child->addChild( 12 );
      head.next->next->next->child->child->addNext( 5 );
      head.next->next->next->child->child->addChild( 21 );
      head.next->next->next->child->child->child->addNext( 3 );
    }
    
    void appendAllTo(node* n, node** appendTo)
    {
      while(n != 0)
      {
        (*appendTo)->addNext( n->value );
        //Update append ptr
        *appendTo = (*appendTo)->next;
    
        if(n->child != 0)
        {
          appendAllTo(n->child, appendTo);
        }
        n = n->next;
      }
    }
    
    void flattenList(node& lst)
    {
      //1. Find the node that end list
      node* appendNode = &lst;
      while(appendNode->next != 0)
      {
        appendNode = appendNode->next;
      }
    
      //2. Go through list, issue recursive call to all children to 
      //   append at the end and delete
      node* n = &lst;
      while(n != 0)
      {
        if(n->child != 0)
        {
          appendAllTo(n->child, &appendNode);
          delete n->child;
          n->child = 0;
        }
        n = n->next;
      }
    }
    
    void linearPrint(const node& nr)
    {
      const node* n = &nr;
      while(n != 0)
      {
        cout<<n->value<<", ";
    
        if( n->child != 0 )
          cout<<"(child), ";
    
        n = n->next;
      }
      cout<<endl;
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
      
      node head;
      build_list( head );
      //head.print();
    
      linearPrint( head );
      flattenList( head );
      linearPrint( head );
    
      //Check memory leak
      //while(1)
      //{
      //  node tH;
      //  build_list( tH );
      //  flattenList( tH );
      //}
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    5, (child), 33, 17, 2, (child), 1, 
    5, 33, 17, 2, 1, 6, 25, 8, 6, 9, 7, 2, 12, 21, 3, 5, 7, 
    End

