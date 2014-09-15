
# C++ Interview Question: Stack Implementation

## Question and Notes

    Implement a stack with a singly-linked list.
    
    Notes:
    - The delete code for the singly linked list is more difficult that it seems.
    - 'new' throws an exception (std::bad_alloc) on failure, use "new(std::nothrow)" 
      to have a 0 returned if does not want exception to be thrown.

## Code

    
    #include <iostream>
    #include <limits>
    
    using namespace std;
    
    class LinkedListNode
    {
    public:
    
      LinkedListNode()
      {
        data = -1.0f;
        next_node = 0;
      }
      
      void setData(float v)
      {data = v;}
    
      float getData() const
      {return data;}
    
      void setNext(LinkedListNode* lln)
      {next_node = lln;}
    
      LinkedListNode* next() const
      {return next_node;}
    
    private:
      float data;
      LinkedListNode* next_node;
    };
    
    //! Singly linked list
    class LinkedList
    {
    public:
    
      LinkedList()
      {
        firstNode = 0;
      }
    
      LinkedListNode* add(float data)
      {
        if(firstNode == 0)
        {
          firstNode = new(std::nothrow) LinkedListNode;
          if( firstNode == 0 )
            return 0;
          firstNode->setData(data);
          return firstNode;
        }
        else
        {
          LinkedListNode* llp = firstNode;
          while(llp->next() != 0)
            llp = llp->next();
    
          llp->setNext( new(std::nothrow) LinkedListNode );
          if(llp->next() == 0)
            return 0;
          llp->next()->setData( data );
          return llp->next();
        }  
      }
    
      int delete_node(LinkedListNode* ll_del)
      {
        //Special case: empty list
        if(firstNode == 0)
          return -1;
    
        //Special case: delete only element
        
        if(ll_del == firstNode)
        {
          //Warning: do not fail to keep the rest of the li
          if(firstNode->next() != 0)
          {
            firstNode = firstNode->next();
          }
          else
          {
            firstNode = 0;
          }
    
          delete ll_del;
          return 0;
        }
    
        LinkedListNode* last = firstNode;
        LinkedListNode* llp = firstNode->next();
        for(; llp != 0; llp = llp->next())
        {
          if(ll_del == llp)
          {
            //Case 1: we are the last pointer
            if(llp->next() == 0)
            {
              last->setNext(0);
              delete llp;
              return 0;
            }
            else
            {
              last->setNext( llp->next() );
              delete llp;
              return 0;
            }
          }
          last = llp;
        }  
    
        return -1;
      }
    
      LinkedListNode* head()
      {
        LinkedListNode* lli = firstNode;
        if(lli == 0 )
          return 0;//Empty list
    
        while(lli->next() != 0)
        {
          lli = lli->next();
        }
        return lli;
      }
    
      void print()
      {
        cout<<"LinkedList Content:"<<endl;
        int nodeNo = 0;
        for(LinkedListNode* llp = firstNode; llp != 0; llp = llp->next())
        {
          cout<<"["<<nodeNo<<"]: "<<llp->getData()<<endl;
          ++nodeNo;
        }
      }
    
    private:
      LinkedListNode* firstNode;
    };
    
    class Stack
    {
    public:
    
      void push(float data)
      {
        ll.add(data);
      }
    
      float pop()
      {
        //Note: this would be MUCH more efficient if
        //      we have a head and tail pointer in the
        //      linked-list.
        LinkedListNode* head = ll.head();
        if(head == 0)
          return numeric_limits<float>::min();//Error reporting
        float data = head->getData();
        ll.delete_node(head);
        return data;
      }
    
      void print()
      {
        ll.print();
      }
    
    private:
      LinkedList ll;
    };
    
    int main()
    {
      cout<<"Begin"<<endl;
    
      cout<<"Test Linked List"<<endl;
    
      LinkedList ll;
    
      ll.print();
    
      LinkedListNode* ll0 = ll.add(0);
      LinkedListNode* ll1 = ll.add(1);
      LinkedListNode* ll2 = ll.add(2);
      LinkedListNode* ll3 = ll.add(3);
      ll.print();
    
      ll.delete_node(ll1);
      ll.print();
    
      ll.delete_node(ll0);
      ll.print();
    
      ll.delete_node(ll2);
      ll.print();
    
      ll.delete_node(ll3);
      ll.print();
    
      LinkedListNode* ll4 = ll.add(4);
      ll.print();
    
      cout<<"Test Stask"<<endl;
    
      Stack stack;
    
      stack.push(4);
      stack.push(3);
      stack.push(2);
      stack.push(1);
      stack.push(0);
      stack.print();
    
      cout<<"POP!: "<<stack.pop()<<endl;
      stack.print();
      cout<<"POP!: "<<stack.pop()<<endl;
      stack.print();
      cout<<"POP!: "<<stack.pop()<<endl;
      stack.print();
      cout<<"POP!: "<<stack.pop()<<endl;
      stack.print();
      cout<<"POP!: "<<stack.pop()<<endl;
      stack.print();
      cout<<"POP!: "<<stack.pop()<<endl;
      stack.print();
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    Test Linked List
    LinkedList Content:
    LinkedList Content:
    [0]: 0
    [1]: 1
    [2]: 2
    [3]: 3
    LinkedList Content:
    [0]: 0
    [1]: 2
    [2]: 3
    LinkedList Content:
    [0]: 2
    [1]: 3
    LinkedList Content:
    [0]: 3
    LinkedList Content:
    LinkedList Content:
    [0]: 4
    Test Stask
    LinkedList Content:
    [0]: 4
    [1]: 3
    [2]: 2
    [3]: 1
    [4]: 0
    POP!: 0
    LinkedList Content:
    [0]: 4
    [1]: 3
    [2]: 2
    [3]: 1
    POP!: 1
    LinkedList Content:
    [0]: 4
    [1]: 3
    [2]: 2
    POP!: 2
    LinkedList Content:
    [0]: 4
    [1]: 3
    POP!: 3
    LinkedList Content:
    [0]: 4
    POP!: 4
    LinkedList Content:
    POP!: 1.17549e-38
    LinkedList Content:
    End

