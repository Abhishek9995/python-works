def add(a,b):
    """add value"""
    print (a + b)
# add(5,1)

def multi(a,b):
    """multi"""
    print(a*b)
# multi(5,5)

def sub(a,b):
    """substraction"""
    if a>=0 & b>=0:
        if a>b:
            print(a-b)
        else:
            a=b
            b=a
            print(a-b)
# sub(5,2)

def division(a,b):
    """division"""
    if a>0 & b>0:
        print(a/b)
    else:
        print("wrong")
# division(10,2)

def percentage(a,b):
    """percentage"""
    print(((a+b)/2)*100)
# percentage(100,2)


# def doctappo():