import re

strings="Learn Data, Python"

mapeo=re.match(r'(\w+) (\w+)',strings,re.M|re.I)

print(mapeo)

if mapeo:
    print("mapeo.group()",mapeo.group())
    print("mapeo.group(1)",mapeo.group(1))
    print("mapeo.group(2)",mapeo.group(2))


else:
    print("La cadena no la puedes chupar")