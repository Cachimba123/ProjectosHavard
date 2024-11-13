import re

num="10 + 6 - 3"

mapeo=re.match(r'(\d+)\+(\d+)\-(\d+)',num)

print(mapeo)

if mapeo:
    print("mapeo.group()",mapeo.group())
    print("mapeo.group(1)",mapeo.group(1))
    print("mapeo.group(2)",mapeo.group(2))
    npart={"Exponente":mapeo.group(1),"Fraccion":mapeo.group(2)}
    print(npart)

else:
    print("La cadena no la puedes chupar")