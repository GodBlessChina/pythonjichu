def wrapper(funnc):
    def inner(x,y):
        type_x = type(x)
        type_y = type(y)
        if type_x==int and type_y==int:
            return funnc(x,y)
        else:
            print('参数类型不正确,只接受int类型')
            return None
    return inner


@wrapper
def f(x:int,y:int):
    return x+y

# res = f(1,2)
res = f(1,"hello")
print(res)