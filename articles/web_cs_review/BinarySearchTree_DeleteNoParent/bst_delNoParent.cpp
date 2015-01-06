
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
        Node* n = this->root;
        Node* parent = 0;

        bool progress = true;
        while (progress)
        {
            progress = false;
            if (v == n->value)
            {
                Node t = *n;

                // Convention: always use successor: the leftmost child on the right.
                if(n->right == 0)
                {
                    if(n == this->root)
                    {
                        delete this->root;
                        this->root = n;
                    }
                    else if(parent->left == n)
                    {
                        parent->left = 0;
                    }
                    else
                    {
                        parent->right = 0;
                    }
                }
                else
                {
                    Node* s = findLeftmost(n->right);
                    n->value = s->value;
                    delLeftmost(n->right, n);
                }
            }
            else if(v < n->value && n->left != 0)
            {
                parent = n;
                n = n->left;
                progress = true;
            }
            else if(v > n->value && n->right != 0)
            {
                parent = n;
                n = n->right;
                progress = true;
            }
        }
    }

private:

    static Node* findRightmost(Node* n)
    {
        while(n->right != 0)
            n = n->right;

        return n;
    }

    static void delLeftmost(Node* n, Node* parent)
    {
        while(n->left != 0)
        {
            parent = n;
            n = n->left;
        }

        if(parent->left == n)
            parent->left = 0;
        else
            parent->right = 0;

        delete n;
    }

    static Node* findLeftmost(Node* n)
    {
        while(n->left != 0)
            n = n->left;

        return n;
    }

    Node* root;
};

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

        last = n->value;
    }

    return true;
}

// Note that each node in the tree is definitely not equally likely.
// @@a1: fun math problem, devise a function that would yield every node with equal probability.
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

    cout<<"Start delete (with no up pointer)."<<endl;

    // Make sure delete doesn't screw-up the BST.
    while( bst.getRoot() != 0 )
    {
        assert ( isValidBST(bst.getRoot()) );

        Node* nDel = getRandomNodeInBST( bst.getRoot() );
        cout<<"Node to delete: "<<nDel->value<<endl;

        bst.deleteNode( nDel->value );
    }

    cout<<"End delete"<<endl;

    cout<<"End"<<endl;
    return 0;
}


