from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
print(City._fields) #namedtuple이 가진 필드들을 출력한다.

delhi_data = ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))

delhi = City._make(delhi_data) #시퀀스를 기반으로 namedtuple 을 만든다.
delhi._asdict() #명명된 튜플 객체에서 만들어진 OrderedDict 객체를 반환한다.

for key, value in delhi._asdict().items():
    print(key + ':',value)