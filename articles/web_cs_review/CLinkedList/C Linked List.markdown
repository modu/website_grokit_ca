
# C++ Interview Question: C Linked List

## Question and Notes

    Implement a simple linked list in C (not C++).
    It can be compiled on a C++ compiler, but do not use any feature of C++.
    
    Notes:
      - Be careful at implementation: a generic add and delete that check all cases
      - How to use malloc(...):
        StructName* sInst = (StructName*)malloc( sizeof(StructName) );

## Code

    
    #include <cstdio>
    #include <cstdlib> 
    
    struct LL_Element
    {
      LL_Element* prev;
      LL_Element* next;
    
      float data;
    };
    
    void ll_new(LL_Element* ll)
    {
      ll->prev = 0;
      ll->next = 0;
      ll->data = -1;
    }
    
    void ll_print_node(LL_Element* ll)
    {
      printf("this: 0x%x\n", ll);
      printf("prev: 0x%x\n", ll->prev);
      printf("next: 0x%x\n", ll->next);
      printf("data: %f\n", ll->data);
    }
    
    void ll_print_seq(LL_Element* ll)
    {
      int item_no = 0;
      while(ll->prev != 0)
      {
        ll = ll->prev;
      }
      while(ll != 0)
      {
        printf("Item No: %i\n", item_no);
        ll_print_node(ll);
        ll = ll->next;
        item_no++;
      }
    }
    
    int ll_add(LL_Element* ll, LL_Element* add)
    {
      //Case 1: ll at the end
      if(ll->next == 0)
      {
        ll->next = add;
        return 0;
      }
      
      //Case 2: ll has a next
      add->next = ll->next;
      ll->next->prev = add;
      ll->next = add;
      add->prev = ll;
      return 0;
    }
    
    int ll_del(LL_Element* ll)
    {
      //ll is only element
      if(ll->prev == 0 && ll->next == 0)
      {
        printf("Error: cannot delete only element.\n");
        return -1;
      }
      
      //ll is between two elements
      if(ll->prev != 0 && ll->next != 0)
      {
        ll->prev->next = ll->next;
        ll->next->prev = ll->prev;
        free(ll);
        return 0;
      }
      
      //ll has prev only
      if(ll->prev != 0)
      {
        ll->prev->next = 0;
        free(ll);
        return 0;
      }
      
      //ll has next only
      if(ll->next != 0)
      {
        ll->next->prev = 0;
        free(ll);
        return 0;
      }
      
      return -1;
    }
    
    int main()
    {
      printf("Begin\n");
    
      LL_Element ll;
      ll_new(&ll);
      ll.data = 0;
      
      LL_Element ll2;
      ll_new(&ll2);
      ll2.data = 1;
    
      LL_Element ll3;
      ll_new(&ll3);
      ll3.data = 2;
    
      LL_Element ll4;
      ll_new(&ll4);
      ll4.data = 3;
      
      //Build list
      ll_add(&ll, &ll2);
      ll_add(&ll2, &ll3);
      ll_add(&ll3, &ll4); 
      
      ll_print_seq(&ll);
      
      printf("\nAfter insertion:\n");
      LL_Element* ll_btw_2_and_3 = (LL_Element*)malloc( sizeof(LL_Element) );
      ll_new(ll_btw_2_and_3);
      ll_btw_2_and_3->data = 2.5;
      ll_add(&ll2, ll_btw_2_and_3);
      ll_print_seq(&ll);
      
      printf("\nAfter deletion:\n");
      ll_del(ll_btw_2_and_3);
      ll_print_seq(&ll);
      
      printf("End\n");
      
      return 0;
    }

## Code Output

    Begin
    Item No: 0
    this: 0x28ac10
    prev: 0x0
    next: 0x28ac00
    data: 0.000000
    Item No: 1
    this: 0x28ac00
    prev: 0x0
    next: 0x28abf0
    data: 1.000000
    Item No: 2
    this: 0x28abf0
    prev: 0x0
    next: 0x28abe0
    data: 2.000000
    Item No: 3
    this: 0x28abe0
    prev: 0x0
    next: 0x0
    data: 3.000000
    
    After insertion:
    Item No: 0
    this: 0x28ac10
    prev: 0x0
    next: 0x28ac00
    data: 0.000000
    Item No: 1
    this: 0x28ac00
    prev: 0x0
    next: 0x20028a40
    data: 1.000000
    Item No: 2
    this: 0x20028a40
    prev: 0x28ac00
    next: 0x28abf0
    data: 2.500000
    Item No: 3
    this: 0x28abf0
    prev: 0x20028a40
    next: 0x28abe0
    data: 2.000000
    Item No: 4
    this: 0x28abe0
    prev: 0x0
    next: 0x0
    data: 3.000000
    
    After deletion:
    Item No: 0
    this: 0x28ac10
    prev: 0x0
    next: 0x28ac00
    data: 0.000000
    Item No: 1
    this: 0x28ac00
    prev: 0x0
    next: 0x28abf0
    data: 1.000000
    Item No: 2
    this: 0x28abf0
    prev: 0x28ac00
    next: 0x28abe0
    data: 2.000000
    Item No: 3
    this: 0x28abe0
    prev: 0x0
    next: 0x0
    data: 3.000000
    End

