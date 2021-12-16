def comma_code(lst):
    if len(lst)==0:    
        print("Enter non-empty list")
    else:
        for i in range(len(lst)-2):
            print(lst[i]+', ',end='')
        print(lst[-2],' and',lst[-1])    
        
spam = ['apples', 'bananas', 'tofu', 'cats']
comma_code(spam)


