
from multiprocessing import Queue

q=Queue(3)
q.put(1)
q.put(2)
print(q.full())
q.put(3)
print(q.full())


try:
    q.put('消息4', True, 2)
except:
    print('队列满')

try:
    q.put_nowait('消息4')
except:
    print('队列满')

if not q.full():
    q.put_nowait('消息4')

if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())

q.put(block=False)