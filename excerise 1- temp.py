# convert from (C)elsius to farhenheit or (F)ahreheit to celsius
temp = int(input('enter the temperature celsius: '))
fahrenheit = (temp  +32) * 9/5
print('the convert value is', fahrenheit, 'fahrenheit')
while temp < 30:
    print(' the weather is cold today')
    temp = temp

temp = int(input('enter the temperature fahreheit: '))
celsius =( temp - 32)* 5/9
print ('the convert value is', celsius,'celsius')
while temp > 30:
    print (' the weather is hot today')
    temp=temp