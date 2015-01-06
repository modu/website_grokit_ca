
#include <iostream>
#include <deque>
#include <stack>
#include <utility>
#include <cassert>
#include <limits>
#include <cstdlib>

using namespace std;

class Node
{
public:

    Node()
    {
        left = 0;
        right = 0;
        parent = 0;
        value = -1;
    }

    Node* left;
    Node* right;
    Node* parent;
    int value;
};

class BinarySearchTree
{
public:

    BinarySearchTree()
    {
        root = 0;
    }

    Node* getRoot()
    {
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
                    np->left->parent = np;
                    return;
                }
                else
                {
                    np = np->left;
                }
            }
            else
            {   // >=
                if(np->right == 0)
                {
                    np->right = new Node;
                    np->right->value = v;
                    np->right->parent = np;
                    return;
                }
                else
                {
                    np = np->right;
                }
            }
        }
    }

    Node* find(float v)
    {
        Node* n = root;

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

    void deleteNode(float v)
    {
        Node* nDel = this->find(v);

        // Node doesn't exist, return.
        if(nDel == 0)
        {
            return;
        }

        // If leaf.
        if(nDel->left == 0 && nDel->right == 0)
        {
            if(nDel == this->root)
            {
                this->root = 0;
            }

            delLeaf(nDel);
            return;
        }

        Node* nSwitch = 0;
        if(nDel->left != 0 && nDel->right == 0 || nDel->left != 0 && nDel->right != 0)
        {
            nSwitch = findRightmost(nDel->left);
        }
        else
        {
            nSwitch = findLeftmost(nDel->right);
        }

        if(nSwitch->left == 0 && nSwitch->right == 0)
        {
            if(nSwitch == nSwitch->parent->left)
            {
                nSwitch->parent->left = 0;
            }
            else
            {
                nSwitch->parent->right = 0;
            }
        }
        else if(nSwitch->left != 0)
        {
            nSwitch->left->parent = nSwitch->parent;
            if(nSwitch == nSwitch->parent->left)
            {
                nSwitch->parent->left = nSwitch->left;
            }
            else
            {
                nSwitch->parent->right = nSwitch->left;
            }
        }
        else if(nSwitch->right != 0)
        {
            nSwitch->right->parent = nSwitch->parent;
            if(nSwitch == nSwitch->parent->left)
            {
                nSwitch->parent->left = nSwitch->right;
            }
            else
            {
                nSwitch->parent->right = nSwitch->right;
            }
        }

        nDel->value = nSwitch->value;

        delete nSwitch;
    }

private:

    static void delLeaf(Node* leaf)
    {
        if(leaf->parent != 0)
        {
            if(leaf->parent->left == leaf)
            {
                leaf->parent->left = 0;
            }
            else
            {
                leaf->parent->right = 0;
            }
        }

        delete leaf;
    }

    static Node* findRightmost(Node* n)
    {
        while(n->right != 0)
            n = n->right;

        return n;
    }

    static Node* findLeftmost(Node* n)
    {
        while(n->left != 0)
            n = n->left;

        return n;
    }

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

void inorderTraversal(const Node* n, stack<const Node*>* accumulator = 0)
{
    //inorder: left, visit, right
    if(n == 0)
        return;

    if(n->left != 0)
        inorderTraversal(n->left);

    cout<< n->value << endl;

    if(accumulator != 0)
    {
        accumulator->push(n);
    }

    if(n->right != 0)
        inorderTraversal(n->right);
}

bool isValidBST(const Node* root)
{
    stack<const Node*> inOrder;

    inorderTraversal(root, &inOrder);

    float last = numeric_limits<float>::min();
    while(inOrder.size() > 0)
    {
        const Node* n = inOrder.top();
        inOrder.pop();

        if(n->value < last)
        {
            return false;
        }

        if(n != root && n->parent == 0)
        {
            return false;
        }

        last = n->value;
    }

    return true;
}

// Note that each node in the tree is definitely not equally likely.
Node* getRandomNodeInBST(Node* root)
{
    int choice = rand() % 5;

    if( choice == 0 )
    {
        return root;
    }
    else if( choice >= 1 && choice <= 2 && root->left != 0)
    {
        return getRandomNodeInBST(root->left);
    }
    else if( choice >= 3 && choice <= 4 && root->right != 0)
    {
        return getRandomNodeInBST(root->right);
    }

    return root;
}

// This is not an efficient way to create a BST (copies needlessly), but let's
// aim for code that's not hard to read here.
BinarySearchTree makeBST()
{
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

    return bst;
}

int main()
{
    cout<<"Begin"<<endl;

    BinarySearchTree bst = makeBST();

    cout<<"Start delete"<<endl;

    // Make sure delete doesn't screw-up the BST.
    while( bst.getRoot() != 0 )
    {
        assert ( isValidBST(bst.getRoot()) );
        //inorderTraversal((Node*)bst.getRoot());

        Node* nDel = getRandomNodeInBST( bst.getRoot() );
        cout<<"Node to delete: "<<nDel->value<<endl;

        bst.deleteNode( nDel->value );
    }
    cout<<"End delete"<<endl;

    bst = makeBST();

    cout<<"--levelOrderTraversal:"<<endl;

    levelOrderTraversal(bst.getRoot());

    cout<<"--preorderTraversal:"<<endl;

    preorderTraversal(bst.getRoot());

    cout<<"--:postorderTraversal:"<<endl;

    postorderTraversal(bst.getRoot());

    cout<<"--:inorderTraversal:"<<endl;

    inorderTraversal(bst.getRoot());

    cout<<"--"<<endl;

    cout<<"End"<<endl;
    return 0;
}


