text = input()
revered_text = ''.join([text[x] for x in range(len(text)-1,-1,-1)])
print(1 if revered_text == text else 0 )