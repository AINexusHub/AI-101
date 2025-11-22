# 数据结构和算法知识库

## 数据结构基础概念

### 什么是数据结构
- **数据结构**: 数据元素之间的逻辑关系和存储关系的集合
- **算法**: 解决特定问题的一系列清晰指令
- **时间复杂度**: 算法执行时间随输入规模增长的趋势
- **空间复杂度**: 算法执行所需内存空间随输入规模增长的趋势

### 复杂度分析
- **大O表示法**: 描述算法性能的上界
- **常见时间复杂度**:
  - O(1): 常数时间
  - O(log n): 对数时间
  - O(n): 线性时间
  - O(n log n): 线性对数时间
  - O(n²): 平方时间
  - O(2ⁿ): 指数时间

## 线性数据结构

### 数组 (Array)
```python
# Python数组示例
arr = [1, 2, 3, 4, 5]

# 基本操作
arr[0]          # 访问: O(1)
arr.append(6)   # 插入末尾: O(1)
arr.pop()       # 删除末尾: O(1)
arr.insert(0, 0) # 插入开头: O(n)
```

**特点**:
- 连续内存空间
- 随机访问高效
- 插入删除效率低（除末尾外）

### 链表 (Linked List)
```python
# 链表节点定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 链表操作
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        # 在末尾添加节点: O(n)
        pass
    
    def prepend(self, val):
        # 在开头添加节点: O(1)
        pass
    
    def delete(self, val):
        # 删除节点: O(n)
        pass
```

**类型**:
- **单向链表**: 每个节点指向下一个节点
- **双向链表**: 每个节点指向前后节点
- **循环链表**: 尾节点指向头节点

### 栈 (Stack)
```python
# 栈实现
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)  # O(1)
    
    def pop(self):
        return self.items.pop()  # O(1)
    
    def peek(self):
        return self.items[-1]    # O(1)
    
    def is_empty(self):
        return len(self.items) == 0
```

**特点**:
- LIFO (后进先出)
- 主要操作: push, pop, peek
- 应用: 函数调用栈、表达式求值、浏览器历史

### 队列 (Queue)
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)  # O(1)
    
    def dequeue(self):
        return self.items.popleft()  # O(1)
    
    def is_empty(self):
        return len(self.items) == 0
```

**类型**:
- **普通队列**: FIFO (先进先出)
- **双端队列**: 两端都可插入删除
- **优先队列**: 按优先级出队

## 树形数据结构

### 二叉树 (Binary Tree)
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 遍历算法
def preorder_traversal(root):
    """前序遍历: 根 -> 左 -> 右"""
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

def inorder_traversal(root):
    """中序遍历: 左 -> 根 -> 右"""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def postorder_traversal(root):
    """后序遍历: 左 -> 右 -> 根"""
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]
```

### 二叉搜索树 (BST)
```python
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """插入节点: O(log n) 平均, O(n) 最坏"""
        if not self.root:
            self.root = TreeNode(val)
            return
        
        current = self.root
        while current:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = TreeNode(val)
                    return
                current = current.right
    
    def search(self, val):
        """搜索节点: O(log n) 平均, O(n) 最坏"""
        current = self.root
        while current:
            if val == current.val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False
```

**特点**:
- 左子树所有节点值 < 根节点值
- 右子树所有节点值 > 根节点值
- 中序遍历得到有序序列

### 平衡二叉树
- **AVL树**: 严格平衡，旋转操作多
- **红黑树**: 近似平衡，插入删除效率高
- **B树**: 多路搜索树，适合磁盘存储
- **B+树**: 数据库索引常用

### 堆 (Heap)
```python
import heapq

# 最小堆
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 2)
heapq.heappop(min_heap)  # 返回1

# 最大堆（通过取负实现）
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -2)
-heapq.heappop(max_heap)  # 返回3
```

**类型**:
- **最小堆**: 父节点值 ≤ 子节点值
- **最大堆**: 父节点值 ≥ 子节点值
- 应用: 优先队列、堆排序

## 哈希结构

### 哈希表 (Hash Table)
```python
# Python字典就是哈希表实现
hash_table = {}

# 基本操作
hash_table['key'] = 'value'  # 插入: O(1) 平均
value = hash_table['key']    # 查找: O(1) 平均
del hash_table['key']        # 删除: O(1) 平均

# 哈希冲突解决
# 1. 链地址法: 每个桶使用链表
# 2. 开放地址法: 线性探测、二次探测
```

**哈希函数要求**:
- 确定性: 相同输入产生相同输出
- 均匀性: 输出均匀分布
- 高效性: 计算速度快

## 图结构

### 图的表示
```python
# 邻接矩阵
graph_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

# 邻接表
graph_list = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

# 类表示
class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
```

### 图遍历算法
```python
def bfs(graph, start):
    """广度优先搜索"""
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex)  # 处理节点
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def dfs(graph, start, visited=None):
    """深度优先搜索"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start)  # 处理节点
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

## 排序算法

### 比较排序
```python
def bubble_sort(arr):
    """冒泡排序: O(n²)"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    """快速排序: O(n log n) 平均, O(n²) 最坏"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """归并排序: O(n log n)"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### 非比较排序
```python
def counting_sort(arr):
    """计数排序: O(n + k), k为数值范围"""
    if not arr:
        return []
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])
    
    return result
```

## 搜索算法

### 二分查找
```python
def binary_search(arr, target):
    """二分查找: O(log n)"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

### 深度优先搜索 (DFS)
```python
def dfs_recursive(graph, node, visited=None):
    """递归DFS"""
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    """迭代DFS"""
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            # 逆序添加邻居以保证顺序
            stack.extend(reversed(graph[node]))
```

### 广度优先搜索 (BFS)
```python
from collections import deque

def bfs_shortest_path(graph, start, end):
    """BFS求最短路径"""
    if start == end:
        return [start]
    
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        current, path = queue.popleft()
        
        for neighbor in graph[current]:
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None
```

## 动态规划

### 经典问题
```python
def fibonacci(n):
    """斐波那契数列: O(n)"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def knapsack(weights, values, capacity):
    """0-1背包问题"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

def longest_common_subsequence(text1, text2):
    """最长公共子序列"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

## 贪心算法

### 经典问题
```python
def coin_change_greedy(coins, amount):
    """硬币找零（贪心）"""
    coins.sort(reverse=True)
    count = 0
    result = []
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
            result.append(coin)
    
    return count if amount == 0 else -1

def activity_selection(start, end):
    """活动选择问题"""
    activities = list(zip(start, end))
    activities.sort(key=lambda x: x[1])  # 按结束时间排序
    
    selected = []
    last_end = 0
    
    for s, e in activities:
        if s >= last_end:
            selected.append((s, e))
            last_end = e
    
    return selected
```

## 字符串算法

### 模式匹配
```python
def kmp_search(text, pattern):
    """KMP算法: O(n + m)"""
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    lps = build_lps(pattern)
    i = j = 0
    result = []
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return result
```

## 算法设计技巧

### 分治法
- **思想**: 将问题分解为子问题，递归解决，合并结果
- **应用**: 归并排序、快速排序、最近点对问题

### 回溯法
```python
def solve_n_queens(n):
    """N皇后问题"""
    def is_valid(board, row, col):
        # 检查列
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # 检查左上对角线
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # 检查右上对角线
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(row):
        if row == n:
            result.append([''.join(row) for row in board])
            return
        
        for col in
