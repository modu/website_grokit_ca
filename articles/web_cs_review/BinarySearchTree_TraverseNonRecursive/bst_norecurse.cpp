
#include <iostream>
#include <deque>
#include <stack>
#include <utility>
#include <cassert>

using namespace std;

class Node
{
public:

Node()
{
    left = 0;
    right = 0;
    value = -1;
}

Node* left;
Node* right;
int value;
};

class BinarySearchTree
{
public:

BinarySearchTree()
{
    root = 0;
}

const Node* getRoot(){
    return root;
}

void insert(float v)
{
    if(root == 0)
    {
        root = new Node;
        root->value = v;
        return;
    }

    Node* np = root;

    while(1)
    {
        if( v < np->value )
        {
            if(np->left == 0)
            {
                np->left = new Node;
                np->left->value = v;
                return;
            }
            else
            {
                np = np->left;
            }
        }
        else
        { // >=
            if(np->right == 0)
            {
                np->right = new Node;
                np->right->value = v;
                return;
            }
            else
            {
                np = np->right;
            }
        }
    }
}

const Node* find(float v)
{
    const Node* n = root;
    
    bool progress = true;
    while (progress)
    {
        progress = false;
        if (v == n->value)
        {
            return n;
        }
        else if(v < n->value && n->left != 0)
        {
            n = n->left;
            progress = true;
        }
        else if(v > n->value && n->right != 0)
        {
            n = n->right;
            progress = true;
        }
    }
    
    return 0;
}

private:

Node* root;
};

void levelOrderTraversal(const Node* n) // ~= Breadth First Search (BFS)
{
    cout<<"levelOrderTraversal()"<<endl;
    if(n == 0)
        return;

    deque<const Node*> queue_node;
    queue_node.push_back(n);

    while(queue_node.size() > 0)
    {
        const Node* nd = queue_node.back();
        queue_node.pop_back();

        cout<<nd->value<<endl;

        if(nd->left != 0)
            queue_node.push_front(nd->left);
        if(nd->right != 0)
            queue_node.push_front(nd->right);
    }
}

void preorderTraversal(const Node* n)
{
    //preorder: visit, left, right
    if(n == 0)
        return;

    cout<< n->value << endl;

    if(n->left != 0)
        preorderTraversal(n->left);
    if(n->right != 0)
        preorderTraversal(n->right);
}

void postorderTraversal(const Node* n)
{
    //postorder: left, right, visit
    if(n == 0)
        return;

    if(n->left != 0)
        postorderTraversal(n->left);
    if(n->right != 0)
        postorderTraversal(n->right);

    cout<< n->value << endl;
}

void preorderTraversal_NoRecurse(Node* n)
{
    //preorder: visit, left, right
    if(n == 0)
        return;

    stack<Node*> st;
    st.push(n);

    while(st.size() != 0)
    {
        Node* c = st.top();
        st.pop();

        if(c != 0)
        {
            cout<< c->value << endl;

            if(c->right != 0)
                st.push( c->right );
            if(c->left != 0)
                st.push( c->left );
        }
    }
}

// Relevant: discussion in http://leetcode.com/2010/04/binary-search-tree-in-order-traversal.html.
void inorderTraversal_NoRecurse(Node* root)
{
    // inorder: left, visit, right
    if(root == 0)
        return;

    stack< pair<bool, Node*> > st;
    st.push( make_pair(false, root) );

    while(!st.empty())
    {
        pair<bool, Node*> pn = st.top();

        st.pop();

        // Mark node as touched.
        if(pn.first == true)
        {
            cout<< pn.second->value << endl;
        }
        else
        {
            pn.first = true;
            
            if(pn.second->right != 0)
                st.push( make_pair(false, pn.second->right) );

            st.push( pn );

            if(pn.second->left != 0)
                st.push( make_pair(false, pn.second->left) );
        }
    }
}

// Relevant: http://www.leetcode.com/2010/10/binary-tree-post-order-traversal.html.
void postorderTraversal_NoRecurse(Node* root)
{
    // postorder: left, right, visit
    if(root == 0)
        return;
        
    stack< pair<bool, Node*> > st;
    st.push( make_pair(false, root) );

    while(!st.empty())
    {
        pair<bool, Node*> pn = st.top();

        st.pop();

        // Mark node as touched.
        if(pn.first == true)
        {
            cout<< pn.second->value << endl;
        }
        else
        {
            pn.first = true;
            st.push( pn );
                        
            if(pn.second->right != 0)
                st.push( make_pair(false, pn.second->right) );

            if(pn.second->left != 0)
                st.push( make_pair(false, pn.second->left) );
        }
    }     
}

void inorderTraversal(const Node* n)
{
    //inorder: left, visit, right    
    if(n == 0)
        return;

    if(n->left != 0)
        inorderTraversal(n->left);
    
    cout<< n->value << endl;
    
    if(n->right != 0)
        inorderTraversal(n->right);
}

int main()
{
    cout<<"Begin"<<endl;

    BinarySearchTree bst;

    bst.insert(7);
    bst.insert(3);
    bst.insert(10);
    bst.insert(2);
    bst.insert(4);
    bst.insert(777);
    bst.insert(500);
    bst.insert(1001);
    
    assert (bst.find(12345) == 0);
    assert (bst.find(bst.getRoot()->value) == bst.getRoot());
    assert (bst.find(bst.getRoot()->left->value) == bst.getRoot()->left);
    assert (bst.find(bst.getRoot()->right->value) == bst.getRoot()->right);
    assert (bst.find(bst.getRoot()->right->right->left->value) == bst.getRoot()->right->right->left);

    cout<<"--levelOrderTraversal:"<<endl;
    
    levelOrderTraversal(bst.getRoot());

    cout<<"--preorderTraversal:"<<endl;

    preorderTraversal(bst.getRoot());

    cout<<"--preorderTraversal_NoRecurse:"<<endl;

    preorderTraversal_NoRecurse((Node*)bst.getRoot());

    cout<<"--:inorderTraversal:"<<endl;

    inorderTraversal((Node*)bst.getRoot());
    
    cout<<"--:inorderTraversal_NoRecurse:"<<endl;

    inorderTraversal_NoRecurse((Node*)bst.getRoot());

    cout<<"--:postorderTraversal:"<<endl;

    postorderTraversal((Node*)bst.getRoot());

    cout<<"--:postorderTraversal_NoRecurse:"<<endl;
    
    postorderTraversal_NoRecurse((Node*)bst.getRoot());
    
    cout<<"--"<<endl;

    cout<<"End"<<endl;
    return 0;
}
