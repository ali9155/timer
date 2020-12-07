
import time
import datetime
import timeit


def countdown_timer(x):
    while x >= 0 :
        x += 1
        print("{}".format(str(datetime.timedelta(seconds=x))))
        time.sleep(1)


if __name__ == '__main__':
    print(timeit.timeit(lambda:countdown_timer(0), number=1))
