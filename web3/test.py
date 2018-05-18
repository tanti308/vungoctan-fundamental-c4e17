from random import randint,choice
def measurements():
    mesurements = [randint(80,100), randint(55,80), randint(80,100)]

    return (mesurements)
mesure = measurements()
print(mesure)

def description():
    characters = ['dễ tính', 'vui vẻ', 'hòa đồng', 'lạc quan',
                  'khéo léo', 'hài hước', 'nóng tính', 'ích kỉ',
                  'nhẹ nhàng', 'thảo mai', 'thân thiện', 'cẩn thận',
                  'tỉ mỉ', 'cầu toàn', 'kỹ tính']
    description = []
    for i in range(4):
        character = choice(characters)
        description.append(character)
    return (description)
des = description()
print(*des, sep=', ')
