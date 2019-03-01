#!/usr/bin/env python

'''thread_app1.py: a multithreaded app'''

__author__      = "@Code.on.Tap"
__copyright__   = "Copyright 2019"
__license__     = "MIT"
__source__      = "https://github.com/code-on-tap/examples/thread_app1.py"


# worker reads from queue and doubles the value
def worker_run( *args ):
    # use the args from line 35
    q = args[0]

    while True:
        # wait for a task from the queue
        value = q.get( True )

        # perform some work
        print( '{}\n'.format( 2*value ) )
        
        # important: mark the task complete
        q.task_done()


from Queue import Queue
from threading import Thread
        
if __name__ == '__main__':
    q = Queue()

    workers = []
    for i in range( 3 ):
        # create a thread to do worker_run() and sharing the "q"
        worker = Thread( target = worker_run, args = ( q, ) )

        # bind this thread to our main thread
        worker.daemon = True

        # remember to start the thread
        worker.start()

    # use the main thread to create work
    for i in range( 10 ):
        q.put( i )

    q.join()
