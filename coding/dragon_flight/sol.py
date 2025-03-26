import sys

data = sys.stdin.read().split()

class Node:
    __slots__ = 'total', 'prefix', 'suffix', 'best'
    def __init__(self, total, prefix, suffix, best):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.best = best

def combine(left, right):
    total = left.total + right.total
    
    prefix = max(left.prefix, left.total + right.prefix)
    suffix = max(right.suffix, right.total + left.suffix)
    best = max(left.best, right.best, left.suffix + right.prefix)
    
    return Node(total, prefix, suffix, best)

def build(arr, tree, idx, l, r):
    if l == r:
        val = arr[l]
        tree[idx] = Node(val, val, val, val)
        return
    mid = (l + r) // 2
    
    build(arr, tree, idx * 2, l, mid)
    build(arr, tree, idx * 2 + 1, mid + 1, r)
    
    tree[idx] = combine(tree[idx * 2], tree[idx * 2 + 1])


def update(tree, idx, l, r, pos, val):
    if l == r:
        tree[idx] = Node(val, val, val, val)
        return
    
    mid = (l + r) // 2
    
    if pos <= mid:
        update(tree, idx * 2, l, mid, pos, val)
    else:
        update(tree, idx * 2 + 1, mid + 1, r, pos, val)
    
    tree[idx] = combine(tree[idx * 2], tree[idx * 2 + 1])

def query(tree, idx, l, r, ql, qr):
    if ql > r or qr < l:
        return Node(0, float('-inf'), float('-inf'), float('-inf'))
    
    if ql <= l and r <= qr:
        return tree[idx]
    
    mid = (l + r) // 2
    left_node = query(tree, idx * 2, l, mid, ql, qr)
    right_node = query(tree, idx * 2 + 1, mid + 1, r, ql, qr)
    
    return combine(left_node, right_node)

N = int(data[0])
Q = int(data[1])

arr = list(map(int, data[2:2+N]))

tree = [None] * (4 * N)
build(arr, tree, 1, 0, N - 1)

pointer = 2 + N
output_lines = []

for _ in range(Q):
    op = data[pointer]
    if op == 'U':
        i = int(data[pointer + 1])
        x = int(data[pointer + 2])

        update(tree, 1, 0, N - 1, i - 1, x)
        pointer += 3
    elif op == 'Q':
        l = int(data[pointer + 1])
        r = int(data[pointer + 2])

        res = query(tree, 1, 0, N - 1, l - 1, r - 1)
        output_lines.append(str(res.best))
        pointer += 3

print("\n".join(output_lines))