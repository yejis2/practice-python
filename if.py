# pocket = ['paper', 'money', 'cellphone']
# card = 1
#
# if 'money' in pocket:
#     pass
# else:
#     print("카드를 꺼내라")
#
# if 'money' in pocket:
#     print("택시")
# elif card:
#     print("택시")
# else:
#     print("걷기")

#while
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """
number = 0

while number != 4:
    print(prompt)
    number = int(input())