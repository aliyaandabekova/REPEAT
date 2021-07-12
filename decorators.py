import time

def decorator(func):        #not right
    print('start')
    func()
    print('finish')

@decorator
def f1():
    print('Send request!')





def decorator(func):        # right
    print('start')
    return func

@decorator
def f1():
    print('Send request!')
    print('finish')
f1 = f1()





def timer(func):
    start_time = time.time()
    func()
    print(time.time() - start_time)

@timer
def func1():
    for i in range(1000000):
        pass


def func(*args,**kwargs):
    print(args,kwargs)

func(1,2,3,4,name='john',last_name='snow')


def archieve(*args):
    print(args)
l1 = [1,2,3,4]
archieve(*l1)
