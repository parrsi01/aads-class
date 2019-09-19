#!/usr/bin/env python3
# encoding: UTF-8
"""Turning in-order and post-order tree traversals into pre-order"""


def get_preorder(inorder: str, postorder: str) -> str:
    """Return pre-order traversal of a tree based on its in-order and post-order traversals"""
    if inorder:
        ind = inorder.index(postorder[0])
        root = str(inorder[ind])
        root.right = get_preorder(inorder[ind+1:], postorder)
        root.left = get_preorder(inorder[:ind], postorder)
        return root
    #raise NotImplementedError