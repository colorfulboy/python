# -*- coding: utf-8 -*-

heigth=float(input('heigth:'))
weigth=float(input('weigth:'))
weigth=80.5
bmi=weigth/(heigth*heigth)
if bmi<=18.5:
    print('体重过轻')
elif 18.5<bmi<=25:
    print('体重正常')
elif 25<bmi<=28:
    print('体重过重')
elif 28<bmi<=32:
    print('肥胖')
else:
    print('严重肥胖')
