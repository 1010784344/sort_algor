# python 实现链表
'''需要注意的点是：

（1）有一个没啥意义的head 节点，只是用来记录链表的起始位置

（2）链表的遍历的起始位置都是：cur=self.head

（3）链表遍历的方式是 list = list.next

（4）remove 和 insert 方法都有使用了两个变量小技巧
    remove:
    pre.next = cur.next

    insert:
    tmp = cur.next
    cur.next=node
    node.next = tmp'''




# 定义节点类
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 定义链表类
class SingleLinkList():
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        return self.head==None

    def length(self):
        cur=self.head
        cnt=0
        while cur!=None:
            cnt+=1
            cur=cur.next
        return cnt

    def travel(self): #遍历链表中的元素
        cur=self.head
        while cur!=None:
            print(cur.val,' ')
            cur=cur.next
        print('\n')

    # 向表头添加val，传进来的是数字（在表头添加一个节点）
    def addToHead(self,item):
        node=ListNode(item)
        # 将之前的链表加在新的节点之后
        node.next=self.head
        # 调整 head 节点总在链表的头部
        self.head=node

    def append(self,item): #向表尾添加val，传进来的是数字
        node=ListNode(item)
        if self.is_empty():
            self.head=node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

    def appendNode(self,node): #向表尾添加节点
        if self.is_empty():
            self.head=node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

    def insert(self,pos,item): #将指定val值插到pos位置
        if pos<=0:
            self.addToHead(item)
        elif pos>=self.length():
            self.append(item)
        else:
            cur=self.head
            cnt=1
            while cnt<pos:
                cur=cur.next
                cnt+=1
            next=cur.next
            node=ListNode(item)
            cur.next=node
            node.next=next

    def remove(self,item): #删除指定的val值
        cur=self.head
        pre=None
        while cur.next!=None:
            if cur.val==item:
                if cur==self.head:
                    self.head=cur.next
                else:
                    pre.next=cur.next
            else:
                pre=cur
                cur=cur.next

    def search(self,item): #搜索指定的val值
        cur=self.head
        while cur.next!=None:
            if cur.val==item:
                return True
            cur=cur.next
        return False


if __name__ == '__main__':
    nums = SingleLinkList()
    node1 = ListNode(1)
    node2 = ListNode(2)
    nums.appendNode(node1)
    nums.appendNode(node2)
    print(nums.travel())
    print(node2.val, ' ', node1.val)
