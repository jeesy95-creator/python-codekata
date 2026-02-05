# 베스트앨범
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 알고리즘: 해시, 정렬
# 작성자: 지소윤
# 작성일: 2026. 02. 05. 09:54:40

from typing import List

def solution(genres: List[str], plays: List[int]) -> List[int]:
    genre_total = {}
    genre_songs = {}
    result = [] 
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        
        genre_total[g] = genre_total.get(g, 0) + p
        
        if g not in genre_songs:
            genre_songs[g] = []
        genre_songs[g].append((i, p))
    
    sorted_genres = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)
    
    for genre, total in sorted_genres:
        songs = genre_songs[genre]
        songs_sorted = sorted(songs, key=lambda x: (-x[1], x[0]))
        top_two = songs_sorted[:2]
        for idx, play in top_two:
            result.append(idx)
    return result 


    
   




    
 