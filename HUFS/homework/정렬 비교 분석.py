import random, timeit
import sys

sys.setrecursionlimit(10**9)
'''
추가로 고려할 사항 
[1 quick sort] 
굳이 하나가 남을때 까지 분할할 필요는 없다. 경우에 따라서 10과 40 사이의 상수 k에 대해서 
k개 이하가 되면 분할을 멈추고 insetion sort로 정렬을 하면 더빠를지도 모른다. 이방법을 구현해 비교해 보아라 

[2 quick sort]
적당한 k개가 남을 때까지 분할한 후, 따로 insertion sort들으로 정렬을 하지 않은 채 재귀를 계속 한다면,
전체 값이 완전히 정렬이 되지는 않음. 그래도 대부분이 값이 정렬이 된 상태가 된다. 
정렬을 완료하기 위해 전체 값들을 대상으로 insertion sort를 이용하면 정렬을 완료할 수도 있다. 
이 방법을 구현해 비교해라.

[3 merge sort]
왼쪽 반과 오른쪽 반으로 나누지 않고, 3등분해서 재귀적으로 정렬한 후 merge하는 3-way
merge sort 알고리즘도 구현해 보고 함께 비교해 보아라 

[4 Tim sort]
python의 sort 함수 tim sort 알고리즘을 구현한 것이다. 
이함수의 수행 시간을 다른 세가지 알고리즘의 수행시간과 비교해 보아라

'''

##
## 여기에 세 가지 정렬함수를 위한 코드를...
##
##퀵 소트
class Quick:
	def __init__(self, array:list,first:int, last:int, mode = "std"):
		self.array = array
		self.length = len(array)
		self.quick_count = 0
		self.quick_swap = 0
		self.select_quick_sort(first, last, mode)

	def select_quick_sort(self, first:int, last:int, state_mode:str)-> None:
		# 세가지 모드
		# 1. standard mode : std
		# 2. 분할 한 재귀 함수가 k개 이하일때 삽입정렬: k-deep
		# 3. 분할 하고 정렬하지 않은채 계속 재귀 한 뒤 삽입정렬: part-insert

		if state_mode == "std": self.std_quick_sort(first, last)
		elif state_mode == "k-deep": self.kindeep_quick_sort(first, last)
		elif state_mode == "part-insrt": self.part_quick_sort(first, last)

	# 1. standard mode : std
	def std_quick_sort(self, first:int, last:int)-> None:
		if first >= last: return
		left, right = first+1, last
		pivot = self.array[first]

		while left<=right:
			while left <= last and self.array[left] <pivot:
				self.quick_count+=1
				left+=1
			while right >first and self.array[right] >pivot:
				self.quick_count += 1
				right-=1

			if left <= right:
				self.quick_swap += 1
				self.array[left], self.array[right] = self.array[right], self.array[left]
				left+=1; right-=1

		self.quick_swap += 1
		self.array[first], self.array[right] = self.array[right], self.array[first]

		self.std_quick_sort(first, right-1)
		self.std_quick_sort(right+1, last)

	# 2. 분할 한 재귀 함수가 k개 이하일때 삽입정렬: k-deep - 미완
	def kindeep_quick_sort(self, first:int, last:int)-> None:
		if first >= last: return
		left, right = first + 1, last
		pivot = self.array[first]

		while left <= right:
			while left <= last and self.array[left] < pivot: left += 1
			while right > first and self.array[right] > pivot: right -= 1

			if left <= right:
				self.array[left], self.array[right] = self.array[right], self.array[left]
				left += 1; right -= 1

		self.array[first], self.array[right] = self.array[right], self.array[first]

		self.std_quick_sort(first, right - 1)
		self.std_quick_sort(right + 1, last)

	# 3. 분할 하고 정렬하지 않은채 계속 재귀 한 뒤 삽입정렬: part-insert -미완
	def part_quick_sort(self, first, last):
		if first >= last: return
		left, right = first + 1, last
		pivot = self.array[first]

		while left <= right:
			while left <= last and self.array[left] < pivot: left += 1
			while right > first and self.array[right] > pivot: right -= 1

			if left <= right:
				self.array[left], self.array[right] = self.array[right], self.array[left]
				left += 1;right -= 1

		self.array[first], self.array[right] = self.array[right], self.array[first]

		self.std_quick_sort(first, right - 1)
		self.std_quick_sort(right + 1, last)


#합병 소트
class Merge:
	def __init__(self, array:list, first:int, last:int, mode = "std"):
		self.array = array
		self.length = len(array)
		self.merge_count = 0
		self.merge_swap = 0
		self.merge_sort(first, last, mode)

	def merge_sort(self,first, last, state_mode):
		#두가지 모드
		#1. standard mode : std
		#2. 3-way mode : three-way
		if state_mode == "std": self.std_merge_sort(first, last)
		elif state_mode == "three-way": self.three_way_marge_sort(first, last)

	def std_merge_sort(self, first:int, last:int)-> None:
		if first >= last: return
		middle = (first+last)//2
		self.merge_count+=1
		self.std_merge_sort(first, middle)
		self.std_merge_sort(middle+1, last)
		self.merge_two_sorted_lists(first, last)

	def merge_two_sorted_lists(self, first, last):
		middle =(first + last)//2
		i, j = first, middle+1
		renew = []
		while i<=middle and j<=last:
			self.merge_swap+=1
			if self.array[i] <= self.array[j]: renew.append(self.array[i]); i+=1
			else: renew.append(self.array[j]);j+=1

		for k in range(i, middle+1):
			renew.append(self.array[k])

		for k in range(j, last+1):
			renew.append(self.array[k])

		for k in range(first, last):
			self.array[k] = renew[k-first]

	def three_way_marge_sort(self, first, last):
		pass

	def merge_three_sorted_lists(self, first, last):
		pass

#힙 소트
class Heap:
	def __init__(self, array: list):
		self.array = array
		self.length = len(array)
		self.heap_count = 0
		self.heap_swap =0
		self.heap_sort()

	#삽입 연산
	def heap_up(self, index:int)-> None:
		while True:
			if index == 0 or self.array[index] < self.array[(index-1)//2]:
				self.heap_count+=1
				break
			elif self.array[index] > self.array[(index-1)//2]:
				self.heap_count += 1
				self.heap_swap+=1
				self.array[index], self.array[(index-1)//2] = self.array[(index-1)//2], self.array[index]
				index//=2

	#우선순위 큐로 인한 재 정렬 연산
	def heap_down(self, index:int)-> None:
		root, child  =0, 1



		while True:
			#자식중에 더 큰 값을 찾기
			child = (root * 2) + 1
			if child > index-1: break
			if self.array[child]<self.array[child+1] and child <index-1:
				self.heap_count += 1
				child+=1
			#루트노드 보다 자식이 더 크다면 교환
			if self.array[root] < self.array[child]:
				self.heap_count += 1
				self.heap_swap += 1
				self.array[root], self.array[child] = self.array[child], self.array[root]
				root = child

			#힙 규칙 위해 경우 종료
			elif self.array[root] > self.array[child]:
				self.heap_count += 1
				break

	#전체적으로 heap sort를 실행 해주는 연산
	def heap_sort(self)-> None:
		for inx in range(self.length): self.heap_up(inx)
		for index in range(self.length-1,-1, -1):
			self.heap_swap+=1
			self.array[0], self.array[index] = self.array[index], self.array[0]
			self.heap_down(index-1)




# 정렬 여부를 검사하는 check_sorted함수는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
# 그 외 코드는 자유롭게 수정해도 됩니다.

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n): A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]
D = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("Quick(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Quick(A, 0, len(A)-1).quick_count,
														Quick(A, 0, len(A)-1).quick_swap))

print("Merge sort:")
print("time =", timeit.timeit("Merge(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Merge(B, 0, len(B)-1).merge_count,
														Merge(B, 0, len(B)-1).merge_swap))

print("Heap sort:")
print("time =", timeit.timeit("Heap(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Heap(C).heap_count, Heap(C).heap_swap))

print("Tim sort:")
print("time =", timeit.timeit("D.sort()", globals=globals(), number=1))


# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D))