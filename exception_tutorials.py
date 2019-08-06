'''
Exception Tutorial

'''
# with open("not_exist_file.txt", "r") as xf:
#     the_truth = xf.read()

# print(the_truth)

'''
output:
Traceback (most recent call last):
  File "/Users/mbilgen/python_ws/exception_tutorials.py", line 7, in <module>
    with open("not_exist_file.txt", "r") as xf:
FileNotFoundError: [Errno 2] No such file or directory: 'not_exist_file.txt'

'''

# print(1 + 2+ "three")

'''
Output:

Traceback (most recent call last):
  File "/Users/mbilgen/python_ws/exception_tutorials.py", line 21, in <module>
    print(1 + 2+ "three")
TypeError: unsupported operand type(s) for +: 'int' and 'str'

'''

import logging
import time

#create logger
logging.basicConfig(filename = "./problems.log",level = logging.DEBUG)

logger = logging.getLogger()

def read_file_timed(path):
    """ Return the contents of the files at 'path' and measure time required."""
    start_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
    stop_time = time.time()
    dt = stop_time - start_time
    logger.info("Time required for {file}  = {time}".format(file=path, time=dt))


# data  = read_file_timed("./audio_file.wav")   # No error

data  = read_file_timed("./video_file.mov")  # 1.2 GB
