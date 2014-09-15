
# C++ Interview Question: Lowest Common Ancestor

## Question and Notes

    http://en.wikipedia.org/wiki/Lowest_common_ancestor
    http://www.leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-i.html
    http://www.leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-ii.html
    - Assumes a parent pointer exists
    
    - Is not the best solution
    
    @tag code the best solution (see link) -- no parent pointers BUT passes parent around

## Code

    
    #include <iostream>
    #include <vector>
    #include <cassert>
    
    using namespace std;
    
    class Node
    {
    public:
      Node(int val_in = -1)
      {
        left = 0;
        right = 0;
        parent = 0;
        val = val_in;
      }
      
      //Point-out that virtual will add a
      //virtual fn pointer to the class (32 or 64 bit larger)
      //-->probably would not declare virtual in 'real-life'
      //   until there is a need for it, but shows you know
      //   your stuff.
      virtual ~Node()
      {
        delete left;
        delete right;
      }
    
      Node* left;
      Node* right;
      Node* parent;
      int val;
    
      void addLeft(int val)
      {
        if(left != 0)
          delete left;
        left = new Node(val);
        left->parent = this;
      }
    
      void addRight(int val)
      {
        if(right != 0)
          delete right;
        right = new Node(val);
        right->parent = this;
      }
    };
    
    Node* buildTestGraph()
    {
      Node* root = new Node(3);
      root->addLeft(5);
      root->left->addLeft(6);
      root->left->addRight(2);
      root->left->right->addLeft(7);
      root->left->right->addRight(4);
      root->addRight( 1 );
      root->right->addLeft(0);
      root->right->addRight(8);
      return root;
    }
    
    bool isExistInChildren(const Node* root, const Node* target)
    {
      if(target == root)
        return true;
    
      if(root->left != 0)
      {
        if(isExistInChildren(root->left, target))
          return true;
      }
      if(root->right !=0)
      {
        if(isExistInChildren(root->right, target))
          return true;
      }
    
      return false;
    }
    
    const Node* lowestCommonAncestor_AssumeParents(const Node* root, const Node* node1, const Node* node2)
    {
      const Node* child = node1;
      const Node* p1 = node1;
    
      while(1)
      {
        p1 = p1->parent;
        if(p1 == root)
          return root;
        if(node1 == node2)
          return p1;
        if(p1 == node2)
          return p1;
    
        bool found = false;
        if(p1->left == child)
        {
          found = isExistInChildren(p1->right, node2);
        }
        else if (p1->right == child)
        {
          found = isExistInChildren(p1->left, node2);
        }
    
        if(found)
          return p1;
    
        child = p1;
      }
    }
    
    static const int BothLeft = 0;
    static const int BothRight = 1;
    static const int OneLeftOneRight = 2;
    static const int NodeInRoot = 3;
    static const int Error = -1;
    
    int searchNodePos(const Node* root, const Node* node1, const Node* node2)
    {
      if(node1 == root || node2 == root)
        return NodeInRoot;
    
      bool node1Left = false;
      bool node1Right = false;
      bool node2Left = false;
      bool node2Right = false;
    
      if(root->left != 0)
      {
        node1Left = isExistInChildren(root->left, node1);
        node2Left = isExistInChildren(root->left, node2);
      }
    
      if(node1Left && node2Left)
        return BothLeft;
    
      if(root->right != 0)
      {
        node1Right = isExistInChildren(root->right, node1);
        node2Right = isExistInChildren(root->right, node2);
      }
    
      if(node1Right && node2Right)
        return BothRight;
    
      if( (node1Right && node2Left) || (node1Left && node2Right) )
      {
        return OneLeftOneRight;
      }
    
      return Error;
    }
    
    //This is a O(n*log(n)) solution with worst case O(n^2).
    const Node* lowestCommonAncestor_noParentPtr(const Node* root, const Node* node1, const Node* node2)
    {
      int nodesPosInTree = searchNodePos(root, node1, node2);
      assert( nodesPosInTree != Error );
    
      if(nodesPosInTree == NodeInRoot)
        return root;
      if(nodesPosInTree == OneLeftOneRight)
        return root;
      if(nodesPosInTree == BothLeft)
        return lowestCommonAncestor_noParentPtr(root->left, node1, node2);
      if(nodesPosInTree == BothRight)
        return lowestCommonAncestor_noParentPtr(root->right, node1, node2);
    
      return 0;
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
      
      Node* root = buildTestGraph();
    
      assert( lowestCommonAncestor_AssumeParents(root, root->left, root->right)->val == 3 );
      assert( lowestCommonAncestor_AssumeParents(root, root->left->left, root->left->right->left)->val == 5 );
      assert( lowestCommonAncestor_AssumeParents(root, root->left->right->left, root->left->left)->val == 5 );
      assert( lowestCommonAncestor_AssumeParents(root, root->right->left, root->right->right)->val == 1 );
      assert( lowestCommonAncestor_AssumeParents(root, root->left->right, root->right->left)->val == 3 );
      assert( lowestCommonAncestor_AssumeParents(root, root->left->right->left, root->left->right)->val == 2 );
    
      assert( lowestCommonAncestor_noParentPtr(root, root->left, root->right)->val == 3 );
      assert( lowestCommonAncestor_noParentPtr(root, root->left->left, root->left->right->left)->val == 5 );
      assert( lowestCommonAncestor_noParentPtr(root, root->left->right->left, root->left->left)->val == 5 );
      assert( lowestCommonAncestor_noParentPtr(root, root->right->left, root->right->right)->val == 1 );
      assert( lowestCommonAncestor_noParentPtr(root, root->left->right, root->right->left)->val == 3 );
      assert( lowestCommonAncestor_noParentPtr(root, root->left->right->left, root->left->right)->val == 2 );
    
      delete root;
    
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    End

