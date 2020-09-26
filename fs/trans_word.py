def solution(begin, target, words):
    answer = 0
    min_val = 100
    if not target in words:
        return answer

    def rec_solution(main_word,  words, result, min_val):
        if main_word in words:
            words.remove(main_word)

        tmps = list(filter(lambda x:diff_word(main_word, x)==1, words))
        
        if target in tmps and result+1 < min_val:
            min_val = result+1
            return min_val

        for word in tmps:
            min_val = rec_solution(word,  words, result+1, min_val)
        
        return min_val

    min_val = rec_solution(begin, words, 0, min_val)

    return min_val



def diff_word(word_1, word_2):
    return sum(list(map(lambda x,y: 1 if x != y else 0, word_1, word_2)))

if __name__ == "__main__":
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))