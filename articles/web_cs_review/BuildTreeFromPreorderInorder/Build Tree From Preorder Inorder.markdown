
# C++ Interview Question: Build Tree From Preorder Inorder

## Question and Notes

    //http://www.leetcode.com/2011/04/construct-binary-tree-from-inorder-and-preorder-postorder-traversal.html
    
    - Don't forget to point-out have to delete memory at the end

## Code

    
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

## Code Output

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

