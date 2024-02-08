import time

def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        duration = float(end_time - start_time)
        print("The function took",duration," to get executed")
        return result
    return wrapper

@timer
def square(num):
    res =num ** 2
    return res


res = square(3)
print("the Results are :", res)
