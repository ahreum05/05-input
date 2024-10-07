when = input('경기장은 어디입니까? ')
Wteam = input('이긴 팀은 어디입니까? ')
Lteam = input('진 팀은 어디입니까? ')
score = input('스코어는 몇대몇 입니까? ')

result = """
======================================
오늘 %s에서 야구 경기가 열렸습니다
%s와 %s의 치열한 공방전을 펼쳤습니다.
결국 %s은 %s를 %s로 이겼습니다.
======================================
""" %(when, Wteam, Lteam,  Wteam, Lteam, score)

print(result)


when = input('경기장은 어디입니까?')
Wteam = input('이긴 팀은 어디입니까?')
Lteam = input('진 팀은 어디입니까?')
score = input('스코어는 몇대몇 입니까?')

result = """
===========================================

오늘 %s에서 야구 경기가 열렸습니다.
%s와 %s의 치열한 공방전을 펼쳤습니다.
결국 %s은 %s를 %s로 이겼습니다.

===========================================
""" %(when, Wteam, Lteam, Wteam, Lteam, score)

print(result)