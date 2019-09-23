#!/usr/bin/env python3
# encoding: UTF-8
"""Turning in-order and post-order tree traversals into pre-order"""

# Printing the post order
post_order = []
def postorder(inorder, preorder, n):
    if preorder[0] in inorder:
        root = inorder.index(preorder[0])

    if root != 0:  # left subtree exists
        postorder(inorder[:root],
                       preorder[1:root + 1],
                       len(inorder[:root]))

    if root != n - 1:  # right subtree exists
        postorder(inorder[root + 1:],
                       preorder[root + 1:],
                       len(inorder[root + 1:]))

    post_order.append(preorder[0])

def get_preorder(inorder: str, postorder: str) -> str:
    """Return pre-order traversal of a tree based on its in-order and post-order traversals"""
    postorder(inorder, preorder, len(inorder))

    #return get_preorder(inorder, postorder)
    #raise NotImplementedError