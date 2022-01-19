#for doni's account
#how to make a dictionary in dictionary

acc_info = {
    'Google Mail 44': {
        'email' : 'donimaulanas44@gmail.com',
        'password' : 'WhereTheWildRosesGrow?21',
    },
    'Google Mail 23': {
        'email' : 'smokeyquartz23@gmail.com',
        'password' : 'GoldBearing!21',
    },
    'Yahoo Mail 1': {
        'email' : 'smokeyquartz23@gmail.com',
        'password' : 'GoldBearing!21',
    },
    'Yahoo Mail 2': {
        'email' : 'smokeyquartz23@gmail.com',
        'password' : 'GoldBearing!21',
    },
    'Facebook': {
        'email' : 'donimaulanas44@gmail.com',
        'password' : 'WhereTheWIldRosesGrow?21',
    },
    'Xiaomi Account': {
        'email' : 'smokeyquartz23@gmail.com',
        'password' : 'GoldBearing!21',
    },
    'gmail23': {
        'email' : 'smokeyquartz23@gmail.com',
        'password' : 'GoldBearing!21',
    },
    'gmail23': {
        'email' : 'smokeyquartz23@gmail.com',
        'password' : 'GoldBearing!21',
    },
}


for email, acc_info in acc_info.items():
    print(f"\naccount type: {email}")
    email = acc_info['email']
    password = acc_info['password']

    print(f"\temail: {email}")
    print(f"\tpassword: {password}")

