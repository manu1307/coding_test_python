def solution(phone_book):
    # 정렬을 한다
    # 반복문을 돌면서 2개씩 묶어서 비교
    # 앞의 거랑 뒤의 거의 포함관계 판단
    phone_book.sort()
    answer = "true"
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            answer = "false"
            break

    return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
