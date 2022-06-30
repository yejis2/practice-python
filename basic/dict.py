
#dictionary
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(list(a.keys()))         #dic_keys 객체를 list 형태로 출력함
print(list(a.values()))         #dic_values 객체를 list 형태로 출력함
print(list(a.items()))         #dic_items 객체를 list 형태로 출력함

print(a.get('name'))
print(a.get('goo', 'bar'))
print('name' in a)

a.clear()
print(a)

