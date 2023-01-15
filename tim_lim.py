import msvcrt
import time

class TimeoutExpired(Exception):
    pass
import sys
def input_with_timeout(prompt, timeout, timer=time.monotonic):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    endtime = timer() + timeout
    result = []
    while timer() < endtime:
        if msvcrt.kbhit():
            result.append(msvcrt.getwche()) #XXX can it block on multibyte characters?
            if result[-1] == '\r':
                return ''.join(result[:-1])
        time.sleep(0.04) # just to yield to other processes/threads
    raise TimeoutExpired
if __name__=="main":
    try:
        prompt="hello"
        answer = input_with_timeout(prompt, 10)
    except TimeoutExpired:
        print('Sorry, times up')
    else:
        print('Got %r' % answer)