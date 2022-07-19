def solution(s):
    s = s.replace('{','').replace('}','').split(',')
    s_index = list(set(s))
    s_dict = {}
    answer = []
    
    #print('s :', s)
    #print('s_index :',s_index)
    for i in s_index:
        s_dict[int(i)] = s.count(i)
    #print('s_dict :',s_dict)
    s_dict_sorted = sorted(s_dict.items(), key=lambda x: x[1], reverse=True)
    #print('s_dict_sorted :',s_dict_sorted)
    for key,value in s_dict_sorted:
        answer.append(key)
    return answer