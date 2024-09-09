def solution(answers):
    # 각각의 수포자가 찍는 방식의 규칙을 파악한다.
    # 일정한 숫자 모음이 반복적으로 등장하고 있다.
    # 문제 길이에 따라 각각의 답안 생성
    # 답안 비교하여 정답 개수 확인
    # 정댑 개수 제일 많은 애를 리턴
    answer = [0, 0, 0]
    questions = len(answers)
    answer1 = [1, 2, 3, 4, 5] * (questions // 5) + [1, 2, 3, 4, 5][:questions % 5]
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5] * (questions // 8) + [2, 1, 2, 3, 2, 4, 2, 5][:questions % 8]
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (questions // 10) + [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][:questions % 10]

    for i in range(len(answers)):
        if answers[i] == answer1[i]:
            answer[0] += 1
        if answers[i] == answer2[i]:
            answer[1] += 1
        if answers[i] == answer3[i]:
            answer[2] += 1

    highest_scorer = []
    max_answer = max(answer)
    for a in range(3):
        if answer[a] == max_answer:
            highest_scorer.append(a + 1)
    return highest_scorer


# enumerate 활용해보자
def solution(answers):
    scores = [0, 0, 0]
    questions = len(answers)
    answer1 = [1, 2, 3, 4, 5] * (questions // 5) + [1, 2, 3, 4, 5][:questions % 5]
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5] * (questions // 8) + [2, 1, 2, 3, 2, 4, 2, 5][:questions % 8]
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (questions // 10) + [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][:questions % 10]

    for i, a in enumerate(answers):
        if a == answer1[i]:
            scores[0] += 1
        if a == answer2[i]:
            scores[1] += 1
        if a == answer3[i]:
            scores[2] += 1

    highest_scorer = []
    max_score = max(scores)
    for i, score in enumerate(scores):
        if score == max_score:
            highest_scorer.append(i + 1)
    return highest_scorer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
