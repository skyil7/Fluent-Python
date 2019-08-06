lax_coordinates = (33.9425, -118.408056) #LA 국제공항의 위도와 경도, 튜플
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014) #도쿄의 지명, 년도, 백만 단위 인구수, 인구 변화율, 제곱킬로미터 단위 면적
traveler_ids = [('USA','31195855'), ('BRA', 'CE342567'), ('ESP','XDA205856')]#여행자들의 국가 코드, 여권번호 형태의 튜플 리스트

for passport in sorted(traveler_ids): #리스트를 반복할 때, passport 변수가 각 튜플에 바인딩 된다.
    print('%s/%s' % passport) #포맷 연산자는 튜플을 이해하고 항목을 하나의 필드로 처리한다.

for country, _ in traveler_ids: #각 튜플을 언패킹하여 정보를 두 변수에 담는다. 우리는 country만 필요하므로, 더미 변수를 활용한다.
    print(country)