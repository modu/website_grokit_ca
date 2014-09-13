
# C++ Interview Question: Maintain Linked List Tail Pointer

## Question and Notes



## Code

    
    #include <iostream>
    #include <cassert>
    
    using namespace std;
    
    class Node;
    static Node* head = 0;
    static Node* tail = 0;
    
    class Node
    {
    public:
    
      Node(int valueIn = -1)
      {
        next = 0;
        value = valueIn;
      }
    
      //virtual if expect inheritance
      ~Node()
      {
        delete next;
        //would have a 'supervisor class' (class LinkedList) 
        //to handle this, point out thought about memory leaks
      }
    
      void quickNext(int val)
      {
        if(next != 0)
          delete next;
        next = new Node(val);
      }
    
      void print()
      {
        cout<<"---"<<endl;
        Node* n = this;
        while(n != 0)
        {
          cout<< n->value;
          if(n == head)
            cout<<" (head)";
          if(n == tail)
            cout<<" (tail)";
          cout<< endl;
          n = n->next;
        }
        cout<<"---"<<endl;
      }
    
      Node* next;
      int value;
    };
    
    int deleteNode(Node* delMe)
    {
      if(head == 0)
      {
        cerr<<"deleteNode return -1"<<endl;
        return -1;
      }
    
      if(delMe == head)
      {
        if(head == tail)
          tail = 0;
        Node* nodeDel = head;
        head = head->next;//OK if next == 0
        nodeDel->next = 0;
        delete nodeDel;
        return 0;
      }
      if(delMe == tail)
      {
        Node* n = head;
        while(n->next != tail)
        {
          n = n->next;
        }
        Node* nodeDel = tail;
        n->next = 0;
        delete nodeDel;
        tail = n;
        return 0;
      }
    
      Node* n = head;
      while(n->next != delMe)
      {
        n = n->next;
      }
      n->next = delMe->next;
      delMe->next = 0;
      delete delMe;
      return 0;
    }
    
    int insertAfter(Node* node, int value)
    {
      if(node == 0 && head == 0)
      {
        assert(tail == 0);
        head = new Node(value);
        tail = head;
        return 0;
      }
      if(node == 0 && head != 0)
      {
        Node* n = new Node(value);
        n->next = head;
        head = n;
        return 0;
      }
      if(node == tail)
      {
        Node* n = new Node(value);
        tail->next = n;
        tail = n;
        return 0;
      }
      if(head == 0)
        return -1;
    
      Node* n = new Node(value);
      Node* temp = node->next;
      node->next = n;
      n->next = temp;
      return 0;
    }
    
    void buildTree()
    {
      Node* locHead = new Node(1);
      locHead->quickNext(2);
      locHead->next->quickNext(3);
      locHead->next->next->quickNext(4);
      locHead->next->next->next->quickNext(5);
      locHead->next->next->next->next->quickNext(6);
      head = locHead;
      tail = locHead->next->next->next->next->next;
      locHead->print();
    }
    
    void testDelete()
    {
      buildTree();
    
      deleteNode(head->next);
      head->print();
      deleteNode(head);
      head->print();
      deleteNode(tail);
      head->print();
      deleteNode(head->next);
      head->print();
      deleteNode(head);
      head->print();
      deleteNode(head);
      head->print();
    
      cout<<endl<<"==================================="<<endl<<endl;
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
    
      //testDelete();
    
      buildTree();
      
      insertAfter(0, 0);
      head->print();
      insertAfter(head, 100);
      head->print();
      insertAfter(tail, 200);
      head->print();
      insertAfter(head->next->next, 500);
      head->print();
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    ---
    1 (head)
    2
    3
    4
    5
    6 (tail)
    ---
    ---
    0 (head)
    1
    2
    3
    4
    5
    6 (tail)
    ---
    ---
    0 (head)
    100
    1
    2
    3
    4
    5
    6 (tail)
    ---
    ---
    0 (head)
    100
    1
    2
    3
    4
    5
    6
    200 (tail)
    ---
    ---
    0 (head)
    100
    1
    500
    2
    3
    4
    5
    6
    200 (tail)
    ---
    End

