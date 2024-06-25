my_list= [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

t=0
while t < len(my_list):
    if my_list [t] > 0:
        print (my_list [t])
        t += 1
        continue
    if my_list [t] < 0:
        break
    else:
        t += 1

