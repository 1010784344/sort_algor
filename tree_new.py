# -*- coding:utf-8 -*-
# python 二叉树新版

class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinTree(object):
    def __init__(self):
        self.root = None

    def add_node(self, val):

        node_list = [self.root]
        # 真正全局使用的变量不是 node_list 这个列表，而是 self.root
        # append 并没有追加到 node_list 这个列表，而是 self.root 后面的节点上
        # nodelist 根据动态图理解的时候是[1,2,3,4] 这样的，但真正用代码实现的时候
        # 看到代码里的数据结构不是 [1,2,3,4] 这样的，而是一个树状的结构

        # 一次只添加一个数据，添加完毕立马 return

        # 每次添加一条数据都是需要从头开始遍历一遍，找到空缺的位置
        # 可以这样说，添加数据自带了遍历的功能

        if not self.root:
            self.root = Node(val)
            print('<--%s' % val)
            return

        while len(node_list) > 0:
            tmp_node = node_list.pop(0)
            if not tmp_node.left:
                tmp_node.left = Node(val)
                print('<--%s' % val)
                return
            else:
                node_list.append(tmp_node.left)
            if not tmp_node.right:
                tmp_node.right = Node(val)
                print('<--%s' % val)
                return
            else:
                node_list.append(tmp_node.right)

    # 广度优先遍历
    def board(self):
        node_list = [self.root]

        while len(node_list) > 0:
            tmp_node = node_list.pop(0)
            print('-->%s' % tmp_node.val)
            if tmp_node.left:
                node_list.append(tmp_node.left)
            if tmp_node.right:
                node_list.append(tmp_node.right)

    # 深度优先遍历考察递归, 将子节点为空作为终止递归的条件
    # 入参都是给一个完整的树，
    # 记忆法：将打印放在左右递归前面就是先序遍历，将打印放在左右递归中间就是中序遍历，将打印放在左右递归后面就是后序遍历
    # 从代码里就可以看出是那种遍历，代码里的 print 就代表 根的位置
    # 深度优先遍历之先序遍历（根左右）
    # 先打印出根的值，然后一直往左递归到底，左边的节点为空之后，再然后一直往右递归到底，右边的节点为空
    def first_for(self, node):
        if not node:
            return
        print(node.val)
        self.first_for(node.left)
        self.first_for(node.right)

    # 深度优先遍历之中序遍历
    # 先打印出根的值，然后一直往左递归到底，左边的节点为空之后，再然后一直往右递归到底，右边的节点为空
    def mid_for(self, node):
        if not node:
            return
        self.mid_for(node.left)
        print(node.val)
        self.mid_for(node.right)

    # 深度优先遍历之后序遍历
    def last_for(self, node):
        if not node:
            return
        self.last_for(node.left)
        self.last_for(node.right)
        print(node.val)


if __name__ == '__main__':

    bb = BinTree()
    bb.add_node(1)
    bb.add_node(2)
    bb.add_node(3)
    bb.add_node(4)
    bb.add_node(5)
    bb.add_node(6)
    bb.add_node(7)
    bb.add_node(8)
    bb.add_node(9)
    bb.add_node(10)
    bb.board()
    print('\n')
    bb.first_for(bb.root)
    print('\n')
    bb.mid_for(bb.root)
    print('\n')
    bb.last_for(bb.root)


