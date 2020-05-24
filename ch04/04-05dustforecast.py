PM = float(input('미세먼지(10마이크로그램)의 농도는 ? '))
if PM >= 151:
    print('미세먼지 농도 : {:.2f}, 등급 : {}'.format(PM, '매우 나쁨'))
elif PM >= 81:
    print('미세먼지 농도 : {:.2f}, 등급 : {}'.format(PM, '나쁨'))
elif PM >= 31:
    print('미세먼지 농도 : {:.2f}, 등급 : {}'.format(PM, '보통'))
else:
    print('미세먼지 농도 : {:.2f}, 등급 : {}'.format(PM, '좋음'))    
