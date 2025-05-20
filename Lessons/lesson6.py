# итераторы

# iter() возвращает сам итератор
# next() возвращает следующий элемент или вызывает StopIteration

class Counter:

    def init(self, limit):
        self.limit = limit
        self.current = 0

    def iter(self):
        return self

    def next(self):
        if self.current < self.limit:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration


# for i in Counter(5):
#     print(i)

def counter_up_to(limit):
    current = 0
    while current < limit:
        yield current
        current += 1

# for num in counter_up_to(5):
#     print(num)

tt = [1, 23, 4, 56, 34, 23, 10]
#
# def return_num(list, index):
#     return list[index]

# O(n) - Линейная сложность

def find_element(lst, target):
    for i in lst:
        if target == 1:
            return i
    return "Нету"

# print(find_element(tt, 5738))

def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "Нету"

my_array = [1, 3, 5, 7, 9, 11, 13]

# print(binary_search(my_array, 13))

tt = [1, 23, 4, 56, 34, 25, 10]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# print(bubble_sort(tt))

# O(n)

def two_sum(arr, target):
    num_map = {}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_map:
            return [num_map[complement, i]]
        num_map[num] = i

arr = [3, 2 ,4]

print(two_sum(arr, 6))