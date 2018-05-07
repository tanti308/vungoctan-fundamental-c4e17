def get_even_list(l):
    even_list =[]
    for i in range(len(l)):
        if l[i] % 2 ==0:
            even_list.append(l[i])
    print(even_list)
    return even_list        
