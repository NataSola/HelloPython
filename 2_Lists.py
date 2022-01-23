friends = ['tom', 'sara', '' , 'julia', 'peter', 'lena', 'jim']
message = f'My oldest friend is {friends[3].title()}'
print (message)
print (friends[-2].title())

friends.append('alex')  # добавление элемента в конец списка
print(friends)

friends.insert(2,'georg')  # добавление элемента в любое место списка
print(friends)

del friends[1]  # удаление элемента из списка (навсегда)
print(friends)


# greeting = f'Hello, {friends[i].title()}'
# i = 0
# print (greeting)