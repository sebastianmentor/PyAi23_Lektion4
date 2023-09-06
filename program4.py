# Kom ihåg 

# import termcolor as T

# print([T.colored(text='Hejsan',color='blue',on_color='on_white')])

# T.cprint(text='Hej igen', color="magenta", on_color="on_blue")

# l = {'start':10,'stop':0,'step':-1}
# l = (10,0,-2)
i = 34
l = [1,2,3,4,5]
for i in l:
# for i in range(10,0,-2):
    print(i)

for i in range(len(l)):
    print(l[i])
l.reverse()
for i in l:
    print(i)

print(l)