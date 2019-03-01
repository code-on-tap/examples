#!/usr/bin/env python

'''xrange.py: userland version of xrange'''

__author__      = "@Code.on.Tap"
__copyright__   = "Copyright 2019"
__license__     = "MIT"
__source__      = "https://github.com/code-on-tap/examples/generators/thread_app2.py"

import time

# worker reads from queue and doubles the value
# use the args from line 35
def worker_run( q ):
    while True:
        # wait for a task from the queue
        value = q.get( True )

        # poison pill: tell the thread when to quit
        if value is None:
            # important: mark the task complete
            q.task_done()
            break

        else:
            # make the worker slow so we can test interrupt
            time.sleep( 5 )

            # perform some work
            print( '{}\n'.format( 2*value ) )
        
            # important: mark the task complete
            q.task_done()




import signal
from Queue import Queue
from threading import Thread
        
if __name__ == '__main__':
    global q, running
    running = True

    # our server listens for "interrupt" CTRL + C
    def signal_interrupt( sig, frame ):
        global running
        if sig == signal.SIGINT:
            print( 'Received: signal.SIGINT( {} )'.format( sig ) )
            running = False

        else:
            print( 'Unsupported signal: {}'.format( sig ) )

    # register a signal handler
    signal.signal( signal.SIGINT, signal_interrupt )

    q = Queue()
    for i in range( 3 ):
        # create a thread to do worker_run() and sharing the "q"
        worker = Thread( target = worker_run, args = ( q, ) )

        # bind this thread to our main thread
        worker.daemon = False

        # remember to start the thread
        worker.start()


    # function to quit workers/threads
    def quit_threads():
        global q
        # send "poison pill" to each worker/thread
        for i in range( 3 ):
            q.put( None )

    
    # use the main thread to create work
    for i in xrange( 10 ):
        if running:
            q.put( i )
            time.sleep( 3 )
        else:
            break

    # our work is done
    quit_threads()

    q.join()
    
    if running:
        print( 'work complete' )
    else:
        print( 'work canceled' )
