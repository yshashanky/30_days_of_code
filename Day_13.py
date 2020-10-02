n = int(input())
my_dict = dict()
for i in range (n):
    user_input = input()
    key, value = user_input.split(" ")
    my_dict[key] = value
for i in range (n):
    query = input()
    if query in my_dict.keys():
        print(query+"="+my_dict[query])
    else:
        print('Not found')
