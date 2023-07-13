import threading
import time
from ArticleMeta import getArticleMeta

def count():
    num = 0
    while(num < 10):
        num += 1
        yield num

counts = count()

def test():
    for i in counts:
        print(threading.current_thread().name, i)
        time.sleep(0.5)

if __name__ == "__main__":
    getArticleMeta('https://doi.org/10.1145/3514221.3523274')