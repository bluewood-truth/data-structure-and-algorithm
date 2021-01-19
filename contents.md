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
              return Node
          
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

