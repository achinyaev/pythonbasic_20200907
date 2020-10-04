import datetime as dt
def log_deco(func):
    def wrapper(*arg, **kwargs):
        with open('some_log.log','a',encoding="UTF-8") as file:
            result = func(*arg, **kwargs)
            file.write(f'{dt.datetime.utcnow()} -- run {func.__name__} = {result}\n')
            return result
    return wrapper

@log_deco
def some(x):
    return x**2

@log_deco
def some2(x):
    return x**3


if __name__ == '__main__':
    res1 = some(2)
    res2 = some2(2)
    res2 = some2(3)


