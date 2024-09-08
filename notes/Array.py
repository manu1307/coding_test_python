# 데이터 추가
# append() 메서드로 데이터 추가

my_list = [1, 2, 3]
my_list.append(4)

# + 연산자로 데이터 추가
my_list = my_list + [5, 6]  # [1,2,3,4,5,6]

# insert 메서드로 데이터 삽입

my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 9999)  # [1,2,9999,3,4,5]

# 데이터 삭제

# pop() 메서드
# 특정 위치를 팝
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop(2)  # 3
print(my_list)  # [1,2,4,5]

# remove() 메서드
# 특정 데이터 자체를 삭제

my_list = [1, 2, 3, 2, 4, 5]
my_list.remove(2)  # [1,3,2,4,5]

# 리스트 컴프리헨션
# 기존 리스트를 기반해 새 리스트를 만들거나 반복문, 조건문을 이용해 복잡한 리스트 생성

numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]  # [1, 4, 9, 16, 25]

# 이외의 깨알 같은 4가지 메서드

fruits = ["apple", "banana", "orange", "grape", "banana", "apple", "kiwi"]

# len()
# 리스트의 전체 데이터 개수 반환

len(fruits)  # 7

# index()
# 특정 데이터가 처음 등장한 인덱스를 반환, 없으면 -1

fruits.index("banana")  # 1

# sort()
# 사용자가 정한 기준에 따라 리스트 데이터 정렬
# reverse=True면 내림차순

fruits.sort()  # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
fruits.sort(reverse=True)  # ['orange', 'kiwi', 'grape', 'banana', 'banana', 'apple', 'apple']

# count()
# 특정 데이터 개수를 반환

fruits.count("apple")  # 2
