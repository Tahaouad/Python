a = {1,4,5,6,7,7}
a.append('hiba')
a.sort()
a.insert(2,4)
del(a[0])
a.pop()
a.remove(5)
del(a[5])
a.index(6)
a.reverse()
b = [9,10,11]
print(a.index(5))
print(len(a))
b = (3,6,7)
1,15,18
a.remove(4)
a.update([1,15,18])
a.add('hiba')
a.pop()
print(a)
dictio = {'nom':'heeeeba','age':22,'fammille' :'dakir','note':{'math':{
    'moyenne':15.3}}}
print(dictio.keys())
for key in dictio:
    print(key,dictio[key])
print(dictio.get('nom'))
print(dictio.values())
for key,value in dictio.items():
    print(key,value)
# invalid syntax dictio it s not a function
dictio['note']['math']=19
del(dictio['fammille'])
dictio['fammille']='last name'
dictio.clear()
print(dictio)
print(dictio['note']['math']['moyenne'])
a.clear()
print(a)
dictio['note']['math']['moyenne']=19
print(dictio)
set()
a = 5
if a != 5:
    pass
else :
    print('ok')