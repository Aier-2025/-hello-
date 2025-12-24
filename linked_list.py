'''
链表的组成单位是节点，节点包括值和对下一个节点的引用
我们通常把头节点当作链表的代称
''' 
class ListNode:
    def __init__(self,val:int):
        self.val:int = val                  # 节点值
        self.next: ListNode | None = None   # 指向下一个节点的引用 
                                            # |表示类别可以是ListNode或None 
        
# 初始化链表 1->3->2->5->4
# 初始化各个节点
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)

# 构建节点之间的引用
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4


def traverse(head:ListNode | None):
    '''遍历该链表的所有节点'''
    tmp = n0
    print('begin')
    while tmp!=None:
        print(tmp.val)
        #print('->')
        tmp = tmp.next
    print('end')
traverse(n0)

def insert(node:ListNode,P:ListNode):
    '''在链表的节点node之后插入节点P'''
    tmp = node.next
    node.next = P
    P.next = tmp

P = ListNode(8)
    
insert(n2,P)
traverse(n0)
    
def remove(node:ListNode):
    '''删除链表node后的第一个节点'''
    
    if not node.next:
        return
    tmp = node.next
    nex = tmp.next
    node.next = nex # 虽然tmp的指针仍然指向next，但是遍历此链表已经无法访问到tmp，所以tmp已经
                    # 不属于该链表
    
remove(n1)
traverse(n0)

def find(head:ListNode,target:int):
    '''在链表中查找值为target的第一个元素'''
    index = 0
    while head:
        if head.val == target:
            return index
        index += 1
        head = head.next
    return -1

res = find(n0,8)
print(res)








