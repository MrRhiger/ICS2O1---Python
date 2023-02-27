user_input = ''

while True:
    user_input = input('Enter letters only: ')

    if not user_input.isalpha():
        print('Enter only letters')
    else:
        print(user_input)
        break