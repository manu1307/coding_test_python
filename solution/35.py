def solution(n, words):
    # 지금까지 말한 단어를 담을 리스트
    # nums를 인덱스로 돌면서
    # 1. 이미 말했는지 확인
    # 2. 앞 단어의 끝자리와 현재 단어의 앞자리가 같은지 확인
    total = []
    for i in range(len(words)):
        if words[i] not in total:
            total.append(words[i])
        else:
            turn = i // n + 1
            person = (i % n) + 1
            return [person, turn]

        if i > 0:
            if words[i][0] != words[i - 1][-1]:
                turn = i // n + 1
                person = (i % n) + 1
                return [person, turn]

    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,
               ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
                "gather", "refer", "reference", "estimate", "executive"])
      )
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
