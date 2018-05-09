from ex11 import is_inside


check = is_inside([250, 270], [140, 60, 100, 200])
if check == False:
    print('Your function is correct')
else:
    print('Oops, bugs detected')
