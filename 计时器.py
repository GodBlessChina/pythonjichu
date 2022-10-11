import time

def time_calc(f):
    def inner():
        print('开始计时')
        t1 = time.time()
        f()
        t2 = time.time()
        print('计时结束')
        print(f'花费时间{t2-t1}')
    return inner

@time_calc
def f():
    print('f开始执行')
    time.sleep(0.5)
    print('f结束执行')
f()
