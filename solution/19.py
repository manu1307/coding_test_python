def polynomial_hash(str):
    p = 31
    m = 1000000007
    hash_value = 0
    for char in str:
        hash_value = (hash_value * p + ord(char)) % m
    return hash_value


def solution(string_list, query_list):
    d = {}
    for s in string_list:
        if polynomial_hash(s) in d:
            d[polynomial_hash(s)] += 1
        else:
            d[polynomial_hash(s)] = 1

    answer = []
    for query in query_list:
        answer.append(polynomial_hash(query) in d)
    return answer


print(solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"]))
