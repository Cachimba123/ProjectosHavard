import re

strings="Learn Analize Data with Scientific Python"
#No se puede en Scientific por que busca una palabra despues con esto (.*?) y luego una ultima palabra, al no haber no regresa nada
mapeo=re.match(r'(.*) with (.*?) .*',strings,re.M|re.I)

print(mapeo)

if mapeo:
    print("mapeo.group()",mapeo.group())
    print("mapeo.group(1)",mapeo.group(1))
    print("mapeo.group(2)",mapeo.group(2))


else:
    print("La cadena no la puedes chupar")