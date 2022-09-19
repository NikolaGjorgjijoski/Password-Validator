import string

print('\nYour password should: ')
print('\t- Have a minimum length of 6;')
print('\t- Have a maximum length of 12;')
print('\t- Contain at least an uppercase letter or a lowercase letter')
print('\t- Contain at least a number;')
print('\t- Contain at least a special character (such as @,+,£,$,%,*^,etc);')
print('\t- Not contain space(s).')
userPassword = input('\nEnter a valid password: ').strip()

if not(6 <= len(userPassword) <= 12):
    message = 'Invalid Password..your password should have a minimum '
    message += 'length of 6 and a maximum length of 12'
    print(message)
if ' ' in userPassword:
    message = 'Invalid Password..your password shouldn\'t contain space(s)'
    print(message)
if not any(i in string.ascii_letters for i in userPassword):
    message = 'Invalid Password..your password should contain at least '
    message += 'an uppercase letter and a lowercase letter'
    print(message)
if not any(i in string.digits for i in userPassword):
    message = 'Invalid Password..your password should contain at least a number'
    print(message)
if not any(i in string.punctuation for i in userPassword): 
    message = 'Invalid Password..your password should contain at least a special character'
    print(message)
else:
    print('Valid Password!')
