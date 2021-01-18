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

