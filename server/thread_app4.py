#!/usr/bin/env python

'''thread_app4.py: a multithreaded app, v4, adding socket'''

__author__      = "@Code.on.Tap"
__copyright__   = "Copyright 2019"
__license__     = "MIT"
__source__      = "https://github.com/code-on-tap/examples/server/thread_app4.py"

import json, signal, socket, time
from Queue import Queue
from threading import Thread

class Server( Thread ):
    def __init__( self, queue, thread_qty ):
        super( Server, self ).__init__()

        # bind this thread to our main thread
        self.daemon = False

        # use to pass the socket to worker
        self.queue = queue

        self.running = False

        # listen for TCP connections
        self.socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        # allow the socket to reconnect after restarting the app
        self.socket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, True )

        self.worker_pool = WorkerPool( queue, thread_qty )

    # override Thread.run so we can listen to socket
    def run( self ):
        while self.running:
            try:
                client, addr = self.socket.accept()
                self.queue.put( client )

            except socket.timeout:
                # ignore timeout set on line 77
                pass

            except socket.error as ex:
                if ex.errno == 4:
                    # application is existing
                    self.stop()
                    break

            except:
                if client:
                    client.shutdown( socket.SHUT_RDWR )
                    client.close()

    # our server listens for "interrupt" CTRL + C
    def signal_interrupt( self, sig, frame ):
        if sig == signal.SIGINT:
            print( 'Received: signal.SIGINT( {} )'.format( sig ) )
            self.stop()

        else:
            print( 'Unsupported signal: {}'.format( sig ) )

    def start( self ):
        # register a signal handler
        signal.signal( signal.SIGINT, server.signal_interrupt )

        self.worker_pool.start()

        # after the pool starts, start our socket listener
        self.socket.bind(( '127.0.0.1', 12321 ))

        # allow 10 connections in backlog
        self.socket.listen( 10 )

        # allow socket.accept to break every 1/2 second
        self.socket.settimeout( 0.5 )

        print( 'Server is listening at 127.0.0.1:12321' )

        self.running = True
        super( Server, self ).start()

    def stop( self ):
        self.running = False
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
            client = self.queue.get( True )

            # poison pill: tell the thread when to quit
            if client is None:
                # important: mark the task complete
                self.queue.task_done()
                break

            else:
                # our protocol:  ffff{ "key": "value", "bool": True, "this is": "the JSON", 1: 567 }
                hex_length = client.recv( 4 )
                length = int( hex_length, 16 )

                json_data = client.recv( length )
                print( json_data )

                # protext against bad JSON
                try:
                    data = json.loads( json_data )
                    print( data )
                except:
                    print( 'Bad request' )

                else:
                    # write the input back to the client
                    response = {
                        'received': data,
                        'response': 'thanks!'
                    }

                    response_data = json.dumps( response )
                    hex_length = '%0.4X' % ( len( response_data ) )
                    client.sendall( '{}{}'.format( hex_length, response_data ) )

                client.shutdown( socket.SHUT_RDWR )
                client.close()

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

    while server.running:
        time.sleep( 0.5 );

    # block main thread until server is done
    server.join()
