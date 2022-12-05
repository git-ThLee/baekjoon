def solution(strings, n):
    str_dict = {key: key[n] for key in strings}
    answer = [x[0] for x in sorted(str_dict.items() ,key= lambda x : (x[1],x[0]))]
    return answer