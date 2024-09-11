def solution(N, stages):
    # 실패한 사람들의 수를 담기 위한 객체 생성
    fail_result = {}
    for i in range(N):
        fail_result[i + 1] = 0

    # 각 단계별 실패한 사람들의 수를 계산해준다.
    for j in stages:
        if j == N + 1:
            continue
        fail_result[j] += 1

    # 실패율을 계산하기 위한 리스트 생성
    fail_rate = [0] * N
    total_people = len(stages)

    # 각 단계별 실패한 사람들의 수의 객체에 대하여
    for stage, people in fail_result.items():
        # 실패율을 계산한다
        fail_rate[stage - 1] = [stage, (people / total_people) if total_people != 0 else 0]
        total_people -= people

    # 실패율을 기준으로 정렬 (sort의d default는 오름차순이므로 reverse 까먹으면 안된다.)
    fail_rate.sort(key=lambda element: element[1], reverse=True)
    answer = list(map(lambda x: x[0], fail_rate))

    return answer

# 시간 복잡도 : O(M + NlogN)

