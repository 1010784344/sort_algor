# -*- coding: utf-8 -*-
# python 二叉树老版


# 需要往二叉树上添加的节点
class Node(object):
    def __init__(self,item):
        self.item = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        # 根节点刚开始赋值为None
        self.root = None

    def add(self,item):
        node = Node(item)
        # 如果树的根为空的话，那将节点本身直接赋值为树
        if not self.root:
            self.root = node
            return
        # 模拟队列遍历二叉树（广度优先），所有的队列的起始都是根节点
        queue = [self.root]
        while queue:
            # 想象图解过程，把二叉树节点放在一个动态的队列里，根据数据的变化，有出队列和入队列。
            # 所以把他放在一个列表里去读取
            # 而且遍历的时候，也是一层一层的概念去遍历。
            # 代表的意思是出队列
            cur_node = queue.pop(0)
            # 如果没有节点就追加
            if not cur_node.lchild:
                cur_node.lchild = node
                return
            # 有节点的话，代表的意思是入队列
            else:
                queue.append(cur_node.lchild)

            if not cur_node.rchild:
                cur_node.rchild = node
                return
            # 代表的意思是入队列
            else:
                queue.append(cur_node.rchild)

    def breath_travel(self):
        """广度遍历（只是将数据一一打印出来，整体思想跟添加数据add很像）"""
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item)

            if cur_node.lchild:
                queue.append(cur_node.lchild)

            if cur_node.rchild:
                queue.append(cur_node.rchild)

    def pre_order(self,node):
        """先序遍历 传入的是根节点"""
        if not node:
            return
        print(node.item)
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def mid_order(self,node):
        """中序遍历 传入的是根节点"""
        if not node:
            return

        self.mid_order(node.lchild)
        print (node.item)
        self.mid_order(node.rchild)

    def last_order(self, node):
        """后序遍历 传入的是根节点"""
        if not node:
            return

        self.last_order(node.lchild)
        self.last_order(node.rchild)
        print(node.item)


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breath_travel()
    print('')
    tree.pre_order(tree.root)
    print('')
    tree.mid_order(tree.root)
    print ('')
    tree.last_order(tree.root)
