
valid_username='Hayyan'
valid_password='12345678'
attempts=0
max_attempts=3
while attempts<max_attempts:
     user=input('Please Enter Your Username: ')
     Password=input('Please Enter Your Password: ')
     if user == valid_username and Password == valid_password:
        print('Login Successful') 
        break
     else:
        attempts+=1 
        print(f'login unsuccesful. Try again Please. You have {max_attempts - attempts} attempt(s) left.')

if attempts == max_attempts:
        print('Maximum login exceeded.')
        print('Please wait while we connect to administator.')
        import sys
        sys.exit()
