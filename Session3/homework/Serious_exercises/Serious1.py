crud=['C','R','U','D']
items=['T-shirt','Sweater']

while True:
    f= str(input("Welcome to our shop, what do you want (C, R, U, D)?").upper())        #chuyen input ng dung thanh viet hoa het
    print('If you want to exit, please type Ctrl+C and then press Enter, thanks!')
    if f == crud[1]:                            #function Read
        print(*items, sep=', ')

    elif f == crud[0]:                          #function Create
        c = str(input('Enter new item: '))
        items.append(c)
        print(*items, sep=', ')

    elif f == crud[2]:                          #function Update
        while True:
            u = int(input('Update position: '))-1
            if u not in range(len(items)):
                print("invalid index!")
            else:
                n = str(input('New item:'))
                items[u] = n
                print(*items, sep=', ')
                break

    elif f == crud[3]:                          #function Delete
        while True:
            d = int(input('Delete position: '))-1
            if d not in range(len(items)):
                print("invalid index!")
            else:
                del items[d]
                print(*items, sep=', ')
                break
    else:
        print('No such function, please try again!')
