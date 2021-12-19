import re
def validpass(pass_):
    regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}')
    validation = regex.search(pass_)
    return validation



pass_ = input()

if validpass(pass_):
    print('Valid')
else:
    print('Invalid')