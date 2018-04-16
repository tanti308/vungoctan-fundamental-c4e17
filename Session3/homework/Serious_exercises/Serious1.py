crud=['C','R','U','D']
items=['T-shirt','Sweater']

while True:
    f= str(input("Welcome to our shop, what do you want (C, R, U, D)?").upper())
    print('If you want to exit, please type Ctrl+C and then press Enter, thanks!')
    if f == crud[1]:                            #function Read
        print(*items, sep='')

    elif f == crud[0]:                          #function Create
        c = str(input('Enter new item: '))
        items.append= c
        print(*items, sep=', ')

    elif f == crud[2]:                          #function Update
        u = int(input('Update position: '))
        n = str(input('New item:'))
        items[u+1] == n
        print(*items, sep=', ')

    elif f == crud[3]:                          #function Delete
        d = int(input('Delete position: '))
        del items[d+1]
        print(*items, sep=', ')

    else:
        print('No such function, please try again!')
