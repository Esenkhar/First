import time


def stringTimeTest(starting=1):
    def innerFunc(func):
        def wrapper(*args):
            start = time.time()
            for i in range(starting):
                func(*args)
            end = time.time() - start
            print(end)

        return wrapper

    return innerFunc


count = 1_000_000
cycle = 1


@stringTimeTest(cycle)
def str1(i):
    l = [f'{item}{item}' for item in range(i)]


@stringTimeTest(cycle)
def str2(i):
    abc = 5
    l = ['{0}{1}'.format(item, item) for item in range(i)]


@stringTimeTest(cycle)
def str3(i):
    abc = 5
    l = ['%s%s' % (item, item) for item in range(i)]


@stringTimeTest(cycle)
def str4(i):
    l = [str(item) + str(item) for item in range(i)]


# str1(count)
# str2(count)
# str3(count)
# str4(count)