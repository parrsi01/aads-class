#!/usr/bin/env python3
# encoding: UTF-8
"""Turning in-order and post-order tree traversals into pre-order"""


def get_preorder(inorder: str, postorder: str) -> str:
    """Return pre-order traversal of a tree based on its in-order and post-order traversals"""
    if postorder == [] or inorder == []:
        return None
    key = str(postorder[-1])
    node = key
    index = inorder.index(key)
    node.left = get_preorder(postorder[:index], inorder[:index])
    node.right = get_preorder(postorder[index:-1], inorder[index + 1:])
    return node
    postorder = input('Input post-order traversal: ').split()
    postorder = [int(x) for x in postorder]
    inorder = input('Input in-order traversal: ').split()
    inorder = [int(x) for x in inorder]
    btree = get_preorder(postorder, inorder)
    print('Binary tree constructed.')
    print('Verifying:')
    #print('Post-order traversal: ', end='')
    #btree.postorder()
    print(btree)
    #print('In-order traversal: ', end='')
    #btree.inorder()
    print()


    #return get_preorder(inorder, postorder)
    #raise NotImplementedError