

username=input('enter username:')
email=input('enter your email:')
password=input('enter password:')

if username=='':
    print('username cannot be empty')
elif'@' not in email:
        print('invalid email')
        
elif len(password)<8 :
            print('password must contain more than 8 characters')

elif not any (c.isupper() for c in password):
        print('Password must contain an uppercaser')
elif not any(c.islower() for c in password):
        print('Password must contain a lower case')
        specialcharacters='!@#$%^&*()":?|)'
elif not any ( 'specialcharacters' in password):
    print('password must contain a special character')
else:
       print('login sucessful!')





