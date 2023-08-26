num_list = [i for i in range(1,10000)]
remove_list = []

for number in num_list:
    a = number
    for num in str(number):
        a = a + int(num)
    if a < 10000:
        remove_list.append(a)

for x in remove_list:
    if x in num_list:
        num_list.remove(x)

for num in num_list:
    print(num)