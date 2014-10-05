
# CS Interview Question: Build Tree From Preorder and Inorder List of Nodes

## Question and Notes

Given a list of nodes from a binary tree given in preorder and inorder fashion, can you reconstruct the tree without ambiguity?

You can use this tree as an example:

      int preorder[] = {7, 10, 4, 3, 1, 2, 8, 11};
      int inorder[] = {4, 10, 3, 1, 7, 11, 8, 2};

Note that this is not a binary _search_ tree: the nodes are not in sorted order in the tree.

## Code C++

    
    #include <iostream>
    #include <vector>
    #include <cassert>
    
    using namespace std;
    
    class Node
    {
    public:
      Node()
      {
        left = 0;
        right = 0;
        val = -1;
      }
    
      virtual ~Node()
      {
        delete left;
        delete right;
      }
    
      Node* left;
      Node* right;
      int val;
    };
    
    int findValueIndex(int val, const int* array, size_t size)
    {
      for(size_t i = 0; i < size; ++i)
      {
        if(val == array[i])
          return i;
      }
      return -1;
    }
    
    //! This assumes that there are no duplicate values
    Node* buildTree(const int* preorder, const int* inorder, size_t size)
    {
      if(size <= 0)
        return 0;
    
      Node* root = new Node;
      root->val = preorder[0];
    
      if(size > 1)
      {
        int inorderRootIndex = findValueIndex(root->val, inorder, size);
        //The root is not always contained in the inorder array.
        if(inorderRootIndex == -1)
          return root;
        root->left = buildTree(&preorder[1], &inorder[0], inorderRootIndex);
    
        if((size_t)inorderRootIndex + 1 < size)
        {
          root->right = buildTree( 
            &preorder[inorderRootIndex + 1], 
            &inorder[inorderRootIndex + 1], 
            size - inorderRootIndex - 1);
        }
      }
      return root;
    }
    
    //left, root, right
    void inorderTransverse(const Node* root, vector<int>& flatTree_inorder)
    {
      if(root == 0)
      {
        cerr<< "Warning: NULL root" <<endl;
        return;
      }
    
      if(root->left != 0)
        inorderTransverse(root->left, flatTree_inorder);
      
      //visit
      flatTree_inorder.push_back( root->val );
    
      if(root->right != 0)
        inorderTransverse(root->right, flatTree_inorder);
    }
    
    // root, left, right
    void preorderTransverse(const Node* root, vector<int>& flatTree_preorder)
    {
      if(root == 0)
      {
        cerr<< "Warning: NULL root" <<endl;
        return;
      }
    
      //visit
      flatTree_preorder.push_back( root->val );
    
      if(root->left != 0)
        preorderTransverse(root->left, flatTree_preorder);
    
      if(root->right != 0)
        preorderTransverse(root->right, flatTree_preorder);
    }
    
    template<class T_>
    void printVect( const vector<T_>& v )
    {
      for(size_t i = 0; i < v.size(); ++i)
      {
        cout<< v[i] << endl;
      }
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
      
      int preorder[] = {7, 10, 4, 3, 1, 2, 8, 11};
      int inorder[] = {4, 10, 3, 1, 7, 11, 8, 2};
      size_t size = sizeof(preorder) / sizeof(int);
    
      Node* root = buildTree(preorder, inorder, size);
    
      cout<<"flatTree_inorder"<<endl;
      vector<int> flatTree_inorder;
      inorderTransverse(root, flatTree_inorder);
      printVect( flatTree_inorder );
      assert( memcmp(inorder, &flatTree_inorder[0], sizeof(inorder)) == 0 );
    
      cout<<"flatTree_preorder"<<endl;
      vector<int> flatTree_preorder;
      preorderTransverse(root, flatTree_preorder);
      printVect( flatTree_preorder );
      assert( memcmp(preorder, &flatTree_preorder[0], sizeof(preorder)) == 0 );
    
      delete root;
    
      cout<<"End"<<endl;
      return 0;
    }

## Code C++ Output

    Begin
    flatTree_inorder
    4
    10
    3
    1
    7
    11
    8
    2
    flatTree_preorder
    7
    10
    4
    3
    1
    2
    8
    11
    End

## Discussion

Here is the order of nodes visit for preorder and inorder:
	preorder: visit, left, right
	inorder:  left, visit, right

Here by visit we mean that we take some action on the node, for example printing it out to the console.

So the preorder array has information on which node is highest in the tree, and the inorder array gives information on if the nodes are left of right relative to each other (since if you are on the left, you will be visited before if you are on the right).

For example, using:
      int preorder[] = {7, 10, 4, 3, 1, 2, 8, 11};
      int inorder[] = {4, 10, 3, 1, 7, 11, 8, 2};

... we can decuce that 7 is the root of the tree (first node in preorder). Then, we know that the nodes {4, 10, 3, 1} are on the left of 7 and {11, 8, 2} on the right. Out of {4, 10, 3, 1}, 10 is the first node of the preorder array, it will therefore be the left root. Out of {11, 8, 2}, 2 is the first node in the preorder array so it will be the root right node. You can apply this process recursively to build the whole tree.

## Further Reading

http://www.leetcode.com/2011/04/construct-binary-tree-from-inorder-and-preorder-postorder-traversal.html

