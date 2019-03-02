#!/usr/bin/env python

'''thread_app3.py: a multithreaded app, v3, OOP'''

__author__      = "@Code.on.Tap"
__copyright__   = "Copyright 2019"
__license__     = "MIT"
__source__      = "https://github.com/code-on-tap/examples/server/thread_app3.py"

import signal, time
from Queue import Queue
from threading import Thread

class Server( object ):
    def __init__( self, queue, thread_qty ):
        self.running = False
        self.worker_pool = WorkerPool( queue, thread_qty )

    # our server listens for "interrupt" CTRL + C
    def signal_interrupt( self, sig, frame ):
        if sig == signal.SIGINT:
            print( 'Received: signal.SIGINT( {} )'.format( sig ) )
            self.running = False

        else:
            print( 'Unsupported signal: {}'.format( sig ) )

    def start( self ):
        # register a signal handler
        signal.signal( signal.SIGINT, self.signal_interrupt )
        self.worker_pool.start()
        self.running = True

    def stop( self ):
        self.worker_pool.stop()


class Worker( Thread ):
    def __init__( self, queue ):
        super( Worker, self ).__init__()
        # bind this thread to our main thread
        self.daemon = False
        self.queue = queue

    def run( self ):
        while True:
            # wait for a task from the queue
            value = self.queue.get( True )

            # poison pill: tell the thread when to quit
            if value is None:
                # important: mark the task complete
                self.queue.task_done()
                break

            else:
                # make the worker slow so we can test interrupt
                time.sleep( 5 )

                # perform some work
                print( '{}\n'.format( 2*value ) )
            
                # important: mark the task complete
                self.queue.task_done()


class WorkerPool( object ):
    def __init__( self, queue, thread_qty ):
        self.queue = queue
        self.workers = []
        for i in range( thread_qty ):
            w = Worker( queue )
            self.workers.append( w )

    def start( self ):
        for w in self.workers:
            w.start()

    # method to quit workers/threads
    def stop( self ):
        # send "poison pill" to each worker/thread
        for w in self.workers:
            self.queue.put( None )


if __name__ == '__main__':
    q = Queue()
    server = Server( q, 3 )
    server.start()
    
    # use the main thread to create work
    for i in xrange( 10 ):
        if server.running:
            q.put( i )
            time.sleep( 3 )
        else:
            break

    # our work is done
    server.stop()

    q.join()
    
    if server.running:
        print( 'work complete' )
    else:
        print( 'work canceled' )


'''Without interrupt'''
#>0
#>2
#>4
#>6
#>8
#>10
#>12
#>14
#>16
#>18
#>work complete

'''With interrupt'''
#>0
#>2
#>4
#>6
#>^CReceived: signal.SIGINT( 2 )
#>8
#>10
#>work canceled
