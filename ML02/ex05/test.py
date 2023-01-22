from my_minipack.progressbar import ft_progress
from my_minipack.logger import log
from time import sleep


@log
def main():
    listy = range(100)

    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)


if __name__ == '__main__':
    main()
