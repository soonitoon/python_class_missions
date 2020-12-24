MAX_QSIZE = 10
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None]*MAX_QSIZE
    
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QSIZE
    
    def clear(self):
        self.front = self.rear

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]
    
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]
    
    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
        
    def display(self):
        if self.front < self.rear:
            out = self.items[self.front + 1:self.rear + 1]
        
        else:
            out = self.items[self.front + 1:MAX_QSIZE] + self.items[:self.rear + 1]
        
        return out

# 이진트리 클래스

class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# 전위 순회 함수
def preorder(n):
    if n is not None:
        print(n.data, end=' ') # 루트노드 화면 출력
        preorder(n.left) # 순환적으로 서브트리 처리...
        preorder(n.right)

# 중위 순회 함수
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

# 후위 순환 함수
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

# 레벨 순회(순환 구조로 만들 수 없음!)
def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

# 노드 계산 함수
def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)

# 단말 노드 개수
def count_leaf(n): 
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

# 트리 높이 구하기
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1

# 모르스 부호 결정트리
table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..')]

def make_morse_tree():
    root = TNode(None, None, None)
    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if c == '.':
                if node.left == None:
                    node.left = TNode(None, None, None)
                node = node.left
            elif c == '-':
                if node.right == None:
                    node.right = TNode(None, None, None)
                node = node.right
        node.data = tp[0]
    return root

def decode(root, code):
    node = root
    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right
    return node.data

def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]

# 힙 트리
class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self):
        return len(self.heap) - 1
    
    def isEmpty(self):
        return self.size() == 0

    def Parent(self, i):
        return self.heap[i//2]

    def Left(self, i):
        return self.heap[i*2]
    
    def Right(self, i):
        return self.heap[i*2+1]
    
    def display(self, msg='힙 트리: '):
        print(msg, self.heap[1:])

    def insert(self, n):
        self.heap.append(n)
        i = self.size()
        while i != 1 and n > self.Parent(i):
            self.heap[i] = self.Parent(i)
            i = i // 2
        self.heap[i] = n

    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while child <= self.size():
                if child < self.size() and self.Left(parent) < self.Right(parent):
                    child += 1
                if last >= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot

# test
heap = MaxHeap()
data = [2, 5, 4, 8, 9, 3, 7, 3]
print("[삽입연산]:", data)
for elem in data:
    heap.insert(elem)
heap.display('[삽입 후]')
heap.delete()
heap.display('[삭제 후]')
heap.delete()
heap.display('[삭제 후]')