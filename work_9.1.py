# import json
# number = [2,3,5,9,11]
# filename = 'number.json'
# with open (filename,'w') as f_obj:
#     json.dump(number,f_obj)


import json
with open ('number.json') as f_obj:
    number = json.load(f_obj)
print(number)


# import json
# username = input('what\'s your name ?')
# filename = 'username.json'
# with open (filename,'w') as f_obj:
#     json.dump(username,f_obj)
#     print('hello ' + username)

# import json
# filename = 'username.json'
# with open (filename) as f_obj:
#     username = json.load(f_obj)
#     print('welcome back ' + username)


# import json
# filename = 'username1.json'
# try:
#     with open (filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input('what\'s your name? ')
#     with open(filename,'w') as f_obj:
#         json.dump(username,f_obj)
#         print('hello ' + username)
# else:
#     print('welcome back ' + username)