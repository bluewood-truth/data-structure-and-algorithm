# Part1. Intro

* 자료구조: 데이터 + 연산

* 알고리즘: 주어진 문제의 해결을 위한 자료구조와 연산 방법에 대한 선택
  * 해결하고자 하는 문제에 따라 최적의 선택을 하기 위해 자료구조를 알아야 함

<br>

# Part2. Linear Array

### 배열(Array)

* (일반적으로 동일한 자료형의) 자료들을 순서대로 늘어놓은 것.

### Python의 리스트(List)

* 자료들을 순서대로 늘어놓은 것. 자료형이 동일하지 않아도 됨.

### Python 리스트의 대표적인 연산들

#### 상수 시간 연산 - O(1)

* 리스트의 길이에 상관 없이 빠르게 처리됨
* `.append(element)`: 리스트의 끝에 원소를 추가함
* `.pop()`: 리스트의 끝에서 원소를 제거하고 해당 원소를 반환함

#### 선형 시간 연산 - O(n)

* 리스트의 길이에 비례하여 처리 시간이 늘어남

* `.insert(index, element)`: 해당 위치에 원소를 추가함
* 크기 n의 리스트에서, n+1번째 자리를 만들고 n번째 원소의 값을 넣음.
  * n-1번째 원소의 값을 n번째 자리에 옮김.
  * 지정한 index까지 위 작업을 반복하고, 지정한 index에 주어진 원소를 추가함.
* `del(list[index])`: 해당 요소를 삭제함
* index의 원소를 index+1의 원소로 바꿈.
  * 리스트의 끝까지 위 작업을 반복하고, 리스트의 마지막 자리를 삭제함.
  
* `.index(element)`: 해당 원소의 index를 반환함.

<br>

# Part3. Sorting & Searching

### Python의 정렬 기능

* `sorted(List)`: 정렬된 리스트를 반환함
* `.sort()`: 리스트를 정렬함
* `reverse=True` 인자를 추가하여 역순으로 정렬도 가능

#### 숫자형이 아닌 자료형의 정렬

* `key=함수 또는 람다식` 인자를 추가함

### 탐색 알고리즘

#### 선형 탐색(Linear Search)

* 리스트의 첫 요소부터 순서대로 찾으려는 값과 비교하며 찾음

* 리스트의 길이에 비례하는 O(n) 연산
* 최악의 경우(마지막 요소거나 없는 요소일 경우) 리스트의 모든 원소를 탐색해야 함

#### 이진 탐색(Binary Search)

* 탐색하려는 리스트가 크기순으로 정렬되어 있는 경우
* 찾으려는 값을 리스트의 중앙값을 비교 -> 해당하지 않는 범위를 버리기를 반복
* 한번 비교가 일어날 때마다 리스트가 반씩 줄어드는(divide & conquer) O(log n) 연산

	```python
def solution(L, x):
    if x < L[0] or x > L[-1]:
        return -1
    
    lower = 0
    upper = len(L) - 1
    
    while lower <= upper:
        if upper - lower == 1:
            break
        
        median = (lower + upper) // 2
        if L[median] > x:
            upper = median
        elif L[median] < x:
            lower = median
        else:
            return median
    
    return -1
  ```

<br>

# Part4. Recursive Algorithms - Basic

### 재귀 함수(Recursive Function)

* 하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것
* 많은 문제가 재귀를 통해 해결이 가능함

### 재귀 호출의 종결 조건

```python
# 일반적인 재귀함수의 형태
def func(n):
    if n ...:
        # 종결조건을 반드시 넣어줘야 함!
    else:
        ...
        return func(...) # 종결조건을 만족하지 못하면 재귀호출
```

### Recursive vs Iterative

* 재귀함수는 항상 반복문으로 표현 가능함

* 효율성 면에서는 반복문이 나으나, 재귀함수는 사람이 직관적으로 이해하기 쉬움

* 피보나치 수열을 구하는 함수 (재귀 vs 반복)

	```python
	# Recursive
	def solution(x):
	    if x <= 1:
	        return x
	    else:
	        return solution(x-2) + solution(x-1)
	```
	
	```python
	# Iterative
	def solution(x):
	    if x <= 1:
	        return x
	    
	    iter_A = 0
	    iter_B = 1
	    
	    for n in range(2, x):
	        iter_A, iter_B = iter_B, iter_A + iter_B
	
	    return iter_A + iter_B
	```

<br>

# Part5. Recursive Algorithms - Applied

* 피보나치 수를 구할 경우, 재귀와 반복의 효율 차이가 큼
  * n번째 피보나치 수를 구할 경우, 반복은 n번의 계산만 하면 되지만 재귀는 (중복을 포함하여) 2^n번의 계산을 하게 됨
* 단 이진 트리나 하노이의 탑 같은 경우처럼 재귀로 간단하게 구현 가능하지만 반복으로 구현하기 힘든 문제도 있음

<br>

# Part6. Complexity of Algoritms

### 복잡도(Complexity)의 종류

#### 시간 복잡도(Time Complexity)

* 문제의 크기와 이를 해결하는 데 걸리는 시간 사이의 관계

#### 공간 복잡도(Space Complexity)

* 문제의 크기와 이를 해결하는 데 필요한 메모리 공간 사이의 관계

### 시간 복잡도에서 고려하는 점

#### 평균 시간 복잡도(Average Time Complexity)

* 임의의 입력 패턴을 가정했을 때 소요되는 시간의 평균

#### 최악 시간 복잡도(Worst-case Time Complexity)

* 가장 긴 시간을 소요하게 만드는 입력에 따라 소요되는 시간

### Big-O Notation

* 점근 표기법(asymptotic notation)의 하나
  * 함수의 증감 추세를 비교하는 표기법
* 예를 들어 입력의 크기가 n일 때,
  * O(log n): 입력의 크기의 로그에 비례하는 시간 소요
  * O(n): 입력의 크기에 비례하는 시간 소요

#### 선형 시간 알고리즘 - O(n)

* n개의 임의로 나열된 수에서 최댓값 찾기: 모든 수를 확인하는 선형 탐색을 해야 함
  * 평균과 최악 모두 O(n)

#### 로그 시간 알고리즘 - O(log n)

* n개의 크기 순으로 정렬된 수에서 특정 값을 찾기: 이진 탐색을 이용 가능

#### 이차 시간 알고리즘 - O(n^2)

* 삽입 정렬(insertion sort): n개의 수(n)를 삽입 방식(n)으로 정렬하기에 최선의 경우 O(n), 최악의 경우 O(n^2)의 시간 복잡도를 가짐

#### 보다 낮은 복잡도를 갖는 정렬 알고리즘 - O(n log n)

* 병합 정렬(merge sort): 나누는 과정(log n)과 병합하며 정렬하는 과정(n)을 거침
* 수학적으로 정렬 알고리즘은 O(n log n)보다 나은 복잡도를 가질 수 없다는 게 증명됨

<br>

# Part7. Linked List 1

### 추상적 자료구조(Abstract Data Structure)

* 데이터와 추상적으로 표현되는 일련의 연산들을 제공하는 자료구조
  * Data: 정수, 문자열, 레코드...
  * Operations: 삽입, 삭제, 순회... / 정렬, 탐색...

### 연결 리스트(Linked List)

* 각 요소가 노드(node)로 구성됨
  * 노드는 데이터와 다음 노드(link)에 대한 정보를 가짐
* 첫번째 노드를 head, 마지막 노드를 tail이라고 함

|                | 배열        | 연결 리스트 |
| -------------- | ----------- | ----------- |
| 저장 공간      | 연속한 위치 | 임의의 위치 |
| 특정 원소 조회 | O(1)        | O(n)        |

### 연결 리스트 구현

* 기본 자료구조

	```python
	class Node:
	    def __init__(self, value, nextNode = None):
	        self.value = value
	        self.next = nextNode
	
	class LinkedList:
	    def __init__(self):
	        self.nodeCount = 0
	        self.head = None
	        self.tail = None
	```

* 특정 원소 참조

  ```python
  # class LinkedList
  	def getAt(self, position):
          if position <= 0 or position > self.nodeCount:
              return None
         	
          index = 1
          current = self.head
          while index < position:
              current = current.next
              index += 1
          return current
  ```

* 연결 리스트 순회 (연결 리스트 요소들을 리스트로 반환)

  ```python
  # class LinkedList
  	def getList(self):
          result = []
          current = self.head
          while current:
              result.append(current.value)
              current = current.next
          return result
  ```

<br>

# Part8. Linked List 2

* 원소의 삽입

  * position이 가리키는 위치에(1 <= position <= nodeCount + 1) newNode를 삽입하고 성공/실패에 따라 True/False를 리턴
  * 맨 앞, 맨 뒤에 삽입하는 경우 O(1), 중간에 삽입하는 경우 O(n)의 시간복잡도를 가짐.

  ```python
  # class LinkedList
  	def insertAt(self, position, newNode) -> bool:
          if position < 1 or position > self.nodeCount + 1:
              return False
          
          if position == 1:
              newNode.next = self.head
              self.head = newNode
          else:
              if position == self.nodeCount + 1:
                  prev = self.tail
              else:
                  prev = self.getAt(position - 1)
              newNode.next = prev.next
              prev.next = newNode
             
         	if position == self.nodeCount + 1:
              self.tail = newNode
             
          self.nodeCount += 1
          return True
  ```

* 원소의 삭제

  * position이 가리키는 위치의 node를 삭제해고 그 값을 리턴

  ```python
  # class LinkedList
  	def popAt(self, position):
          if position < 1 or position > self.nodeCount:
              raise IndexError
          
          if self.nodeCount == 1:
              value = self.head.value
              self.nodeCount -= 1
              self.head = self.tail = None
              return value
          
          if position == 1:
              value = self.head.value
              self.head = self.head.next
          else:
              prev = self.getAt(position - 1)
              current = prev.next
              value = current.value
              prev.next = current.next
              if position == self.nodeCount:
                  self.tail = prev
          
          self.nodeCount -= 1
          return value
  ```

* 두 리스트의 연결

  ```python
  # class LinkedList
  	def concat(self, otherList):
          self.tail.next = otherList.head
          if otherList.tail:
  	        self.tail = otherList.tail
          self.nodeCount + otherList.nodeCount
  ```

<br>

# Part9. Linked List 3

* 조회의 효율성이 떨어지는 대신 삽입과 삭제가 쉬운 것이 연결 리스트의 장점인데, 앞서 구현한 `insertAt()`이나 `popAt()`은 항상 `getAt()`을 사용하므로 연결 리스트의 장점을 살리지 못한다.

* 효율적으로 노드를 삽입하고 삭제하기 위해, 특정 노드의 뒤에 삽입, 삭제를 하는 기능을 구한한다.

* 그 전에 리스트의 맨 앞에 삽입, 삭제하는 경우를 위해 리스트의 첫번째 노드를 더미 노드로 두도록 구현을 변경한다.

  ```python
  class LinkedList:
      def __init__(self):
          self.nodeCount = 0
          self.head = Node(None)
          self.tail = None
          self.head.next = self.tail
      
      # 다른 연산들도 이에 맞춰 변경
  ```

* 원소의 삽입

  * prev가 가리키는 node의 다음에 newNode를 삽입하고 성공여부에 따라 True/False를 리턴

  ```python
  # class LinkedList
  	def insertAfter(self, prev, newNode):
          newNode.next = prev.next
          if prev.next is None:
              self.tail = newNode
          prev.next = newNode
          self.nodeCount += 1
          return True
      
      def insertAt(self, position, newNode):
          if position < 1 or position > self.nodeCount + 1:
              return False
          if position != 1 and position == self.nodeCount + 1:
              prev = self.tail
          else:
              prev = self.getAt(position - 1)
          return self.insertAvter(self, prev, newNode)
  ```

* 원소의 삭제

  * prev의 다음 노드를 삭제해서 그 노드의 값을 리턴
    * prev가 마지막 노드일 때는 None을 리턴

  ```python
  # class LinkedList
      def popAfter(self, prev):
          if prev.next is None:
              return None
          
          current = prev.next
          value = current.value
          prev.next = current.next
          if prev.next is None:
              self.tail = prev
          
          self.nodeCount -= 1
          return value
  
  
      def popAt(self, position):
          if position < 1 or position > self.nodeCount:
              raise IndexError
          
          prev = self.getAt(position - 1)
          return self.popAfter(prev)
  ```

<br>

# Part10. Doubly Linked List

### 양방향 연결 리스트 (Doubly Linked List)

* 앞, 뒤 양방향으로 링크가 존재하는 연결 리스트

* 리스트 양 끝에 더미 노드를 추가함으로써 head와 tail을 수정할 필요가 없어지고, 코드가 훨씬 깔끔해진다.

  ```python
  class Node:
      def __init__(self, item, prevNode=None, nextnode=None):
          self.value = item
          self.prev = prevNode
          self.next = nextNode
  
  class DoublyLinkedList:
      def __init__(self)
          self.nodeCount = 0
          self.head = Node(None)
          self.tail = Node(None)
          self.head.next = self.tail
          self.tail.prev = self.head
  ```

* 리스트 순회

  ```python
  	def traverse(self):
          result = []
          current = self.head
          while current.next.next:
              current = current.next
              result.append(current.value)
          return result
      # 조금만 고치면 역방향 순회도 가능!
  ```

* 원소의 삽입

  ```python
  	def insertAfter(self, prev, newNode):
          next = prev.next
          newNode.prev = prev
          newNode.next = next
          prev.next = newNode
          next.prev = newNode
          self.nodeCount += 1
          return True
  ```

* 특정 원소 조회

  ```python
  	def getAt(self, position):
          if position < 0 or position > self.nodeCount:
              return None
          
          # head나 tail 중 가까운 곳에서부터 탐색을 시작함
          if position > self.nodeCount // 2:
              i = 0
              current = self.tail
              while i < self.nodeCount - pos + 1:
                  current = current.prev
                  i += 1
          else
          	...
  ```

<br>

# Part11. Stack

### 스택(stack)

* 자료(data element)를 보관할 수 있는 선형 구조
* 자료를 넣을 때는 한쪽 끝에 밀어 넣고(push), 꺼낼 때는 넣은 쪽에서 꺼냄(pop) -> 후입선출(LIFO)

#### 스택에서 발생하는 오류

* 빈 스택에서 pop하려 할 때 -> stack underflow

* 꽉 찬 스택에 데이터를 넣으려 할 때 -> stack overflow

#### 스택의 연산

* `size()`: 현재 스택에 있는 원소 수를 리턴
* `isEmpty()`: 현재 스택이 비어 있는지 판단
* `push(x)`: 데이터 원소 x를 스택에 추가
* `pop()`: 스택의 맨 위에 저장된 데이터 원소를 제거하고 리턴
* `peek()`: 스택의 맨 위에 저장된 데이터 원소를 리턴 (제거하지 않음)

### 스택의 활용 - 수식의 괄호 유효성 검사

* 올바른 수식: `(A + B)`, `{(A + B) * C}`, `[(A + B) * (C + D)]` 등

* 올바르지 않은 수식: `(A + B`, `A + B)`, `{A * (B + C})`, `[(A + B) * (C + D)}` 등

  ```python
  def checkBracket(expression: str):
      brackets = {"(":")", "{":"}", "[":"]"}
      match = brackets.values()
      expression = expression.replace(" ","")
      stack = []
      for c in expression:
          if c in brackets:
              stack.append(c)
          if c in match:
              if len(stack) == 0:
                  retrun False
              if brackets[stack.pop()] != c:
                  return False
      return len(stack) == 0
  ```

<br>

# Part12. Stack Application - Postfix Notation

### 중위 표기법과 후위 표기법

#### 중위 표기법(infix notation)

* `(A + B) * (C + D)`  (연산자 계산순서: 1 3 2)

* 연산자가 피연산자들의 사이에 위치함

#### 후위 표기법(postfix notation)

* ` A B + C D + *` (연산자 계산순서: 1 2 3)
* 연산자가 피연산자들의 뒤에 위치

### 중위 표현식 -> 후위 표현식

* 수식을 한 단위(연산자, 피연산자)씩 읽으며 다음을 수행한다.

  * 피연산자가 등장하면 후위 표현식에 추가한다.
  * 연산자가 등장했을 때, 스택이 비어 있으면 스택에 연산자를 추가한다.
  * 연산자가 등장했을 때, 스택이 비어 있지 않으면 스택 맨 위의 연산자와 우선순위를 비교하여
    * 스택의 연산자가 우선순위가 높거나 같으면 pop하여 후위 표현식에 추가한다. 이후 현재 연산자를 스택에 추가한다.
    * 현재 연산자가 우선순위가 높으면 스택에 추가한다.
  * 여는 괄호가 등장하면 스택에 추가한다.
  * 닫는 괄호가 등장하면 여는 괄호가 나올 때까지 pop하여 연산자를 후위 표현식에 추가한다.

  * 수식의 끝에 다다르면 스택에 있는 모든 연산자를 pop하여 후위 표현식에 추가한다. 

<br>

# Part13. Calculate Postfix Expression

### 스택을 이용한 후위 표현식 계산

*  수식을 한 단위(연산자, 피연산자)씩 읽으며 다음을 수행한다.
  * 피연산자가 등장하면 스택에 추가한다.
  * 연산자가 등장하면 피연산자 2개를 스택에서 pop하고, 해당 연산자에 대한 계산을 한다. 이후 계산 결과를 스택에 추가한다.
    * 먼저 꺼낸 피연산자가 뒤에 있어야 한다!

<br>

# Part14. Queue

### 큐(Queue)

* 자료를 보관할 수 있는 선형 구조
* 자료를 넣을 때는 한쪽 끝에 넣고(enqueue), 꺼낼 때는 반대쪽에서 꺼냄(dequeue) -> 선입선출(FIFO)

#### 큐의 연산

* `size()`: 현재 큐에 있는 원소 수를 리턴
* `isEmpty()`: 현재 큐가 비어 있는지 판단
* `enqueue(x)`: 데이터 원소 x를 스택에 추가
* `dequeue()`: 큐의 맨 앞에 저장된 데이터 원소를 제거하고 리턴
* `peek()`: 큐의 맨 앞에 저장된 데이터 원소를 리턴 (제거하지 않음)

<br>

# Part15. Circular Queue

### 큐의 활용

* 자료를 생성하는 작업과 그 자료를 이용하는 작업이 비동기적으로 일어나는 경우
  * 자료의 생성과 이용이 여러 군데에서 일어나는 경우
* 자료를 처리하여 새로운 자료를 생성하고, 나중에 그 자료를 또 처리해야 할 경우

### 환형 큐(Circular Queue)

* 정해진 개수의 저장 공간을 빙 돌려가며 사용함
* 데이터를 넣는 front, 데이터를 꺼내는 rear 포인터(인덱스)를 가짐
  * 최초에 front와 rear는 인덱스 범위 밖(e.g. -1)에서 시작함.
  * `enqueue()`하면 front는 인덱스 0을 가리키고, 이후 `enqueue()`할때마다 front는 +1함.
  * 마찬가지로 `dequeue()`하면 rear는 인덱스 0을 가리키고 이후 `dequeue()` 할때마다 rear는 +1함.
  * front나 rear가 마지막 인덱스에 다다랐을때 +1하면 0으로 돌아감.

#### 환형 큐의 연산

* 큐의 모든 연산
* `isFull()`: 큐가 꽉 찼는지 판단

<br>

# Part16. Priority Queue

### 우선순위 큐(Priority Queue)

* 큐가 FIFO 방식을 따르지 않고 원소들의 우선순위에 따라 원소를 꺼내는 방식.

* 기존 큐에서 `enqueue()`시에 우선순위에 맞추어 삽입하도록 수정하면 우선순위 큐가 된다.

<br>

# Part17. Tree

### 트리(Tree)

* 정점(node)과 간선(edge)을 이용하여 데이터의 배치 형태를 추상화한 자료구조.

#### 용어

* root: 첫번째 노드 (부모가 없는 노드)
* leaf: 마지막 노드 (자식이 없는 노드)
* level: root 노드와의 최단거리의 간선 수
* height(depth): 최대 level + 1
* subtree: 특정 노드를 기준으로 해당 노드 위를 잘라낸 트리
* degree: 어떤 노드의 차수 (자식 수)

### 이진 트리(Binary Tree)

* 모든 노드의 차수가 2 이하인 트리
* 트리는 재귀적으로 정의할 수 있음
  * 이진 트리 = root 노드 + 왼쪽 subtree + 오른쪽 subtree (단, 빈 tree도 subtree로 취급한다)

#### 포화 이진 트리 (Full Binary Tree)

* 모든 레벨에서 노드들이 모두 채워져 있는 이진 트리

#### 완전 이진 트리 (Complete Binary Tree)

* 다음의 조건을 만족하는 레벨 k의 이진 트리
  * 레벨 k-2까지는 모든 노드가 2개의 자식을 가짐
  * 레벨 k-1에서는 왼쪽부터 노드가 순차적으로 채워짐

<br>

# Part18. Binary Tree

#### 이진 트리의 연산

* `size()`: 현재 트리에 포함된 노드 수를 구함
* `depth()`: 현재 트리의 깊이를 구함
* 순회(traversal): 각 노드를 방문함

### 이진 트리 구현

#### 노드

* 자료, left child, right child 멤버를 가짐

```python
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
```

#### 트리

```python
class BinaryTree:
	def __init__(self, root):
		self.root = root
```

#### size()

* 트리는 재귀적으로 정의되므로 size도 재귀적으로 처리할 수 있음
* 전체 트리의 사이즈 = left subtree의 사이즈 + right subtree의 사이즈 + 1 (자기자신)

```python
# class Node:
	def size(self):
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return left_size + right_size + 1

# class BinaryTree:
	def size(self):
        return self.root.size() if self.root else 0
```

#### depth()

* 전체 트리의 깊이 = left subtree의 깊이와 right subtree의 깊이 중 더 큰것 + 1

### 이진 트리의 순회(Traversal)

* 깊이 우선 순회 (depth fist traversal)
  * 중위 순회 (in-order traversal)
  * 전위 순회 (pre-order traversal)
  * 후위 순회 (post-order traversal)
* 넓이 우선 순회 (breadth first traversal)

#### 중위 순회 (In-order Traversal)

* 순회의 순서: left subtree -> 자기 자신 -> right subtree

```python
# class Node:
	def inorder(self):
        traversal = []
        if self.left:
        	traversal += self.left.inorder()
        traversal.append(self.data)
       	if self.right:
            traversal += self.right.inorder()
        return traversal

# class BinaryTree:
	def inorder(self):
        return self.root.inorder() if root else []
```

#### 전위 순회 (Pre-order Traversal)

* 순회의 순서: 자기 자신 -> left subtree -> right subtree

#### 후위 순회 (Post-order Traversal)

* 순회의 순서: left subtree -> right subtree -> 자기 자신

<br>

# Part19. Binary Tree - BFS; Breadth First Trabersal

### 넒이 우선 순회 (Breadth First Traversal)

* root부터 한 단계씩 낮은 level의 노드들을 방문한다.
* level이 같은 노드들 사이에서는,
  * 부모 노드의 방문 순서에 따라 방문한다.
  * 부모가 같으면 왼쪽 자식 노드를 오른쪽 자식보다 먼저 방문한다.

* BFS는 재귀로 구현하기 어렵다.-> 큐를 이용!

#### 알고리즘 설계

* root 노드를 큐에 넣고 시작한다.
* 큐에서 하나씩 노드를 꺼내서 값을 저장한다. 이후 해당 노드의 left, right를 차례로 큐에 넣는다.
* 큐가 비워질 때까지 계속 반복한다.

<br>

# Part20. Binary Search Tree

### 이진 탐색 트리(Binary Search Tree)

* 모든 노드에 대해서 다음의 성질을 만족하는 이진 트리. (중복되는 데이터 원소는 없는 것으로 가정)
  * 왼쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 작다
  * 오른쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 크다

#### 정렬된 배열과 비교

* 장점: 데이터 원소의 추가, 삭제 용이 (트리 구조이므로 노드 추가, 삭제가 편함)
* 단점: 공간 소요가 큼

#### 연산의 정의

* `insert(key, data)`: 트리에 주어진 데이터 원소를 추가
* `remove()`: 특정 원소를 트리로부터 삭제
* `lookup()`: 특정 원소를 검색
* `inorder()`: 키의 순서대로 데이터 원소들을 나열
* `min()`, `max()`: 최소 키, 최대 키를 가지는 원소를 각각 탐색

### 이진 탐색 트리 구현

#### 노드와 트리

```python
class Node;
	def __init__(self, key, value):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BinSearchTree:
    def __init__(self):
        self.root = None
```

#### 중위 순회 (In-order Traversal)

```python
# class Node:
	def inorder(self):
        traversal = []
        if self.left:
        	traversal += self.left.inorder()
        traversal.append(self)
       	if self.right:
            traversal += self.right.inorder()
        return traversal

# class BinSearchTree:
	def inorder(self):
        return self.root.inorder() if root else []
```

#### min(), max()

```python
# class Node:
	def min(self):
        return self.left.min() if self.left else self
    
    def max(self):
        return self.right.min() if self.right else self

# class BinSearchTree:
	def min(self):
        return self.root.min() if self.root else None
    
    def max(self):
        return self.root.max() if self.root else None
```

#### lookup()

* 입력: 찾으려는 대상 키
* 리턴: 찾은 노드와 그것의 부모 노드 (없으면 각각 None)

```python
# class Node:
	def lookup(self, key, parent=None):
        if key < self.key:
            return self.left.lookup(key, self) if self.left else None, None
        elif key > self.key:
            return self.right.lookup(key, self) if self.left else None, None
        else:
            return self, parent
    
# class BinSearchTree:
	def lookup(self, key):
        return self.root.lookup(key) if self.root else None, None
```

#### insert()

* 입력: 키, 데이터 원소
* 리턴: 없음

```python
# class Node:
	def insert(self, key, data):
        if key < self.key:
            
        else key > self.key:
        
        else:
            raise KeyError("BinSearchTree contains duplicated key.")

# class BinSearchTree:
	def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)
```

