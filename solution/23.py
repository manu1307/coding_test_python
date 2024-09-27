def solution(genres, plays):
    # 장르별 재생횟수를 담을 dict 선언
    # 장르별 인덱스 및 재생횟루를 담을 dict 선언
    # generes와 plays를 돌면서 장르별 재생횟수 더해주고
    # 디른 dict에 장르별로 (인덱스, 재생횟수)를 저장
    # 장르별 재생횟수 비교하여 수록 순서 결정
    # 수록 순서에 따라 다른 dict에서 재생횟수가 가장 많은 노래 추출
    # 1개면 바로 팝하면 되고
    # 2개 이상이면 정렬한 후에 팝을 2번하면 된다
    answer = []
    genre_dict = {}
    song_dict = {}
    for i in range(len(genres)):
        genre_dict[genres[i]] = genre_dict.get(genres[i], 0) + plays[i]
        if genres[i] not in song_dict:
            song_dict[genres[i]] = [(i, plays[i])]
        else:
            song_dict[genres[i]].append((i, plays[i]))
    sorted_genres = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)
    for g in sorted_genres:
        if len(song_dict[g[0]]) == 1:
            answer.append(song_dict[g[0]][0][0])
        else:
            sorted_song = sorted(song_dict[g[0]], key=lambda x: x[1])
            a = sorted_song.pop()
            b = sorted_song.pop()
            if a[1] == b[1]:
                if a[0] > b[0]:
                    answer.append(b[0])
                    answer.append(a[0])
            else:
                answer.append(a[0])
                answer.append(b[0])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic", "pop", "classic", "classic"], [800, 600, 150, 800]))
