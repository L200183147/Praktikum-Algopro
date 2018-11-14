Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Name = "Nur Annida I'ffah Supardi"
>>> NIM = 147
>>> Height = 1.58
>>> Weight = 45
>>> YearOfBirth = 2000
>>> Me = (YearOfBirth, Weight, Height, NIM, Name)
>>> Data = [YearOfBirth, Weight, Height, NIM, Name]
>>> type(Me)
<class 'tuple'>
>>> #because (me) is a data in the form of an object that uses parentheses to start and end data ()
>>> Me[0]
2000
>>> #because me [0] will display the first index tuple element. The first tuple index in Me is my birth year, 2000. Whereas for the sequence, the year of birth is first
>>> a = NIM%4; Me[a]
147
>>> #because if nim, which is assumed in variable (a) 147 is divided by 4, it will produce 36.75 it shows the fourth index element of tuple ME. and nim in ordered third
>>> type(Me[a])
<class 'int'>
>>> #because Me[a] to show number 147, and that number including integers. integers is the number who doesn't have number behind comma
>>> Me[a:4]
(147,)
>>> #because it will display a and end before index 4. A is 147, and before index 4 is NIM. So that appears is 147
>>> type(Me[4])
<class 'str'>
>>> #because ME [4] shows the index element 4 in tuple Me, the fourth index is Name. The data from the name is Nur Annida I'ffah Supardi, this data is of type string because it contains more than one letter and is written using double quotes.
>>> Me[0]='ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Me[0]='ok'
TypeError: 'tuple' object does not support item assignment
>>> #because the type of Me is tuple. Therefore the tuple elements can't be changed to ok or anything else
>>> type(Data)
<class 'list'>
>>> #the reason for the data type is the list because the list is written in square brackets
>>> type(Data[4])
<class 'str'>
>>> #because Data [4] shows the index element 4 in list Data, the fourth index is Name. The data from the name is Nur Annida I'ffah Supardi, this data is of type string because it contains more than one letter and is written using double quotes
>>> Data[4][5]
'n'
>>> #because the fourth index of Data is Name, and the fifth index Name is letter n
>>> Data[4][a:6]
' An'
>>> #because the fourth index of Data is Name, and the index between (a) to the sixth index in Name is ' An'
>>> Data[0] = 'ok'; Data
['ok', 45, 1.58, 147, "Nur Annida I'ffah Supardi"]
>>> #because the data type is the list, the elements in the list can be changed   so the command to change the data to 0 becomes ok, it can be executed
>>> Data[-a]
1.58
>>> #because the data [-a] shows the order of data -3 or the third place from behind, and the order of -3 in the data is height which is worth 1.58
>>> range(a)
range(0, 3)
>>> #because giving output the range from starts 0 until a, and a is worth 3
