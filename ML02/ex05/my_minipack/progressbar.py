import time


def ft_progress(lst):
    start_time = time.time()
    lst_length = len(lst)
    for i, elem in enumerate(lst):
        elapsed_time = time.time() - start_time
        progress = int(i / lst_length * 100)
        eta = (lst_length - i) * elapsed_time / i if i > 0 else 0
        bar = "[" + "=" * int(progress / 2) + ">" + " " * \
            (50 - int(progress / 2)) + "]"
        print('ETA: {:.2f}s {} {:d}/{:d} | elapsed time {:.2f}s\r'.format(eta,
                                                                          bar, i, lst_length, elapsed_time), end='\r', flush=True)
        yield elem
    i = lst_length
    elapsed_time = time.time() - start_time
    progress = int(i / lst_length * 100)
    eta = (lst_length - i) * elapsed_time / i if i > 0 else 0
    bar = "[" + "=" * int(progress / 2) + ">" + " " * \
        (50 - int(progress / 2)) + "]"
    print('ETA: {:.2f}s {} {:d}/{:d} | elapsed time {:.2f}s\r'.format(eta,
                                                                      bar, i, lst_length, elapsed_time), end='\r', flush=True)
