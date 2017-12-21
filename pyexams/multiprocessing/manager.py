from multiprocessing import Manager, Pool
import os
from Queue import Empty
import signal
import traceback


PROCESSOR = 8


def signal_handler():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def callback(retvalue):
    print "Process return value is: %s" % str(retvalue)


def worker(*args, **kwargs):
    # do some work with parameters.
    # when handling exceptions use `traceback` module
    # to print full traceback.
    # remember to handle exceptions properly, so that
    # the subprocess can exit gracefully.
    pass


def main():
    pool = Pool(PROCESSOR, signal_handler)
    # when using pool, don't try to use multiprocessing.Queue()
    queue = Manager().Queue()
    try:
        for i in range(PROCESSOR):
            pool.apply_async(worker, args=(queue,), callback=callback)
        pool.close()
        pool.join()
    except KeyboardInterrupt:
        pool.terminate()
        pool.join()

