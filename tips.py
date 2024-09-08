# 조기 반환
# 코드 실행 과정이 함수 끝까지 도달하기 전에 반환하는 기법

def total_price(quantity, price):
    total = quantity * price
    if total > 100:
        return total * 0.9
    return total


print(total_price(4, 50))


# 보호 구문
# 초기에 입력값이 유효한지 검사하고 그렇지 않으면 바로 함수를 종료

def calculate_average(numbers):
    if numbers is None:
        return None

    if not isinstance(numbers, list):  # numbers가 리스트가 아니면 종료(예외)
        return None

    if len(numbers) == 0:  # numbers의 길이가 0이면 종료(예외)
        return None

    total = sum(numbers)
    average = total / len(numbers)
    return average


print(calculate_average([1, 2, 3, 4, 5]))


# 합성 함수
# 2개 이상의 함수를 활용하여 함수를 추가로 만드는 기법, 보통은 람다식을 활용

def add_three(x):
    return x + 3


def square(x):
    return x ** 2


composed_function = lambda x: square(add_three(x))
print(composed_function(3))  # ( 3 + 3 )^2 = 36

print("hello world")
