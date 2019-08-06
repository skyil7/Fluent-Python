#지능형 리스트
print('지능형 리스트')
colors = ['white', 'black']
sizes = ['S', 'M', 'L', 'XL']

shirts = [(color, size) for color in colors
                        for size in sizes]
print(shirts)

#제네레이터 표현식
print('제네레이터 표현식')
for shirt in ('%s %s' %(c, s) for c in colors for s in sizes):
    print(shirt)