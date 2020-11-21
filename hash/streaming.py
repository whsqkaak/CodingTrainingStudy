def solution(genres, plays):
    answer = []
    song_dict = dict()
    
    for i in range(len(genres)):
        if genres[i] in song_dict:
            song_dict[genres[i]][i] = plays[i]
        
        else:
            song_dict[genres[i]] = {}
            song_dict[genres[i]][i] = plays[i]
            
    sum_song = dict(map(lambda x : (x, sum(song_dict[x].values())), song_dict))
    sorted_genres = sorted(sum_song, key = lambda k : sum_song[k], reverse=True)

    for genre in sorted_genres:
        sorted_songs = sorted(song_dict[genre], key = lambda k : song_dict[genre][k], reverse=True)[:2]

        for song in sorted_songs:
            answer.append(song)
    return answer

if __name__ == "__main__":
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
    