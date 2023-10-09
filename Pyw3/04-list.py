class Listnode(object):
    def __init__(self, data=0):
        self.data = data
        self.next = None


class List(object):
    def __init__(self):
        self.head = None

    def create(self, alldata):
        self.head = Listnode(alldata[0])
        cur = self.head
        for i in alldata[1:]:
            p = Listnode(i)
            cur.next = p
            cur = p
        return self.head

    def travel(self):
        if self.head:
            cur = self.head
            while cur:
                print(cur.data, end=' ')
                cur = cur.next
            print(' ')
        else:
            return None
    # 增

    def add(self, value, n):
        p = Listnode(value)
        if self.head:
            if n == 0:
                p.next = self.head
                self.head = p
                print('插入成功！结果如下')
            else:
                cur = self.head
                count = 1
                while count < n:
                    count += 1
                    cur = cur.next
                p.next = cur.next
                cur.next = p
                print('插入成功！结果如下')
        else:
            self.head = p
            print('插入成功！结果如下')
    # 删

    def rmv(self, value):
        if self.head:
            p = self.head
            while p:
                if p.next.data == value:
                    p.next = p.next.next
                    print('删除成功！结果如下')
                else:
                    p = p.next
        else:
            return None
    # 查

    def search(self, value):
        if self.head:
            p = self.head
            count = 1
            while p:
                if p.data == value:
                    print('查找成功，在第{}个节点'.format(count))
                    break
                else:
                    p = p.next
                    count += 1
            if p == None:
                print('不存在！')
        else:
            return None
    # 改

    def cor(self, value, n):
        if self.head:
            p = self.head
            count = 1
            while count < n:
                p = p.next
                count += 1
            p.data = value
            print('修改成功！结果如下')
        else:
            return None


list = List()
list.create([x for x in range(10)])
list.travel()
# 增
list.add(15, 0)
list.travel()
# 改
list.cor(0, 3)
list.travel()
# 查
list.search(6)
list.travel()
# 删
list.rmv(9)
list.travel()
