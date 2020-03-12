import queue
from hw4_tweepy import tweets_get
from hw4_imageToVideo import image_to_video
import multiprocessing
import time
import threading

def producer(key_list):
    for name in key_list:
        q.put(name)

def worker():
    while True:
        get_item = q.get()
        print(get_item)
        if get_item is None:
            print("No name put into the queue. Should break!")
            break
        try:
            tweets_get(get_item)
            image_to_video(get_item)
        except:
            pass
    print('#########Task End#######')
    q.task_done()


if __name__ == '__main__':
    key = ['Tesla', 'Honda', 'Benz', 'Bmw']
    threads_count = len(key)
    q = queue.Queue()
    threads = []

    producer(key)
    for n in range(len(key)):
        t = threading.Thread(target=worker)
        threads.append(t)
        threads[n].start()

    for n in range(threads_count):
        q.put(None)

    for t in threads:
        t.join()
