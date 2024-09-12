def solution(dirs):
    # 시작 좌표 [0,0] 설정
    current = [0, 0]
    # (시작좌표) , (도착좌표) 형태의 키를 가진 객체 생성
    roads = {}
    # 방향에 따른 좌표 변화량 객체 생성
    dx_dy_dir = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}

    # 이동 방향에 따른 현재 좌표 계산
    for d in dirs:
        cx, cy = current
        nx = cx + dx_dy_dir[d][0]
        ny = cy + dx_dy_dir[d][1]
        # 만약 좌표평면을 벗어나면 무시
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        # 출발 좌표, 도착 좌표 객체 안에 있는지 확인
        # 좌표가 바뀌어도 길은 똑같으므로 반대방향도 체크
        key1 = f"{cx}{cy},{nx}{ny}"
        key2 = f"{nx}{ny},{cx}{cy}"
        # 현재 좌표 이동
        current = [nx, ny]
        # 있으면 패스
        if key1 in roads or key2 in roads:
            continue
        # 없으면 새로 넣어준다
        roads[key1] = 1
    # 가지고 있는 키값들의 개수가 답이 된다.
    answer = len(roads.keys())
    return answer

# 시간 복잡도 : O(N)