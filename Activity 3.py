Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Nur Annida I'ffah Supardi"
>>> NIM = "L200183147"
>>> X = '1' + NIM[7:]
>>> a = int (X)
>>> b = len (Nama)
>>> type(a)
<class 'int'>
>>> #because a is integers
>>> type(b)
<class 'int'>
>>> #because b is integers
>>> a/b
45.88
>>> type(a/b)
<class 'float'>
>>> #because results of a/b is float
>>> a//b
45
>>> type(a//b)
<class 'int'>
>>> #because results of a//b is integers. Integers is the number doesn't have numbers behind comma
>>> 10*(a-999)
1480
>>> type(10*(a-999))
<class 'int'>
>>> #because 10*(a-999) is integers who the number  doesn't have numbers behind comma
>>> b**2
625
>>> type(b**2)
<class 'int'>
>>> #because b**2 is integers. This integers because the number doesn't have numbers behind comma
>>> a%b
22
>>> type(a%b)
<class 'int'>
>>> #because a%b is integers. This includes integers the reason is the number doesn't have numbers behind comma
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #the reason c is float because the number have numbers behind comma
>>> a/c
91.76
>>> type(a/c)
<class 'float'>
>>> #because the result of a/c is float. Float is another form of fraction. The hallmark of decimal fractions is a comma
>>> a//c
91.0
>>> type(a//c)
<class 'float'>
>>> #because the results of a// c is float. This is a division arithmetic operation with rounding down
>>> a%c
9.5
>>> type(a%c)
<class 'float'>
>>> #because a%b is float. This includes float the reason is the number have numbers behind comma
>>> c > b
False
>>> type(c>b)
<class 'bool'>
>>> #the reason c > b is false because the value of b is greater than c. Bool is a data type that only has two values. That is true or false.
>>> a > b and b > c
True
>>> type (a > b and b > c)
<class 'bool'>
>>> #the reason is the value of a is greater than b and the value of b is greater than c. The results of a > b and b > c are true. This includes the Boollen data type because, this data type has two possibilities, true and false
>>> a > 1100 or b < 10
True
>>> type (a > 110 or b <10)
<class 'bool'>
>>> #the two logic results of the comparison, namely a > 100 or b < 10, are true. Because in the boolen data type that has two possibilities namely true or false, for symbols or if the comparison is true or false then the results that will appear are true
