// Trees: Is This a Binary Search Tree?
// https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.  

The Node struct is defined as follows:
    struct Node {
        int data;
        Node* left;
        Node* right;
    }
*/
#include <limits.h>

    bool checkBST(Node* node, int min, int max) {
        if (node == NULL) {
            return true;
        }
        if (node->data > max ||  node->data < min) {
            return false;
        }
        return checkBST(node->left, min, node->data - 1) && 
               checkBST(node->right, node->data + 1, max);
    }    

    bool checkBST(Node* root) {
        return checkBST(root, INT_MIN, INT_MAX);
    }