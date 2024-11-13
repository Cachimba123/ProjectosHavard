import re

num="123.456"

mapeo=re.match(r'(?P<Exponente>\d+)\.(?P<Fracccion>\d+)',num)

print(mapeo)

if mapeo:
    print("mapeo.group()",mapeo.groupdict())


else:
    print("La cadena no la puedes chupar")