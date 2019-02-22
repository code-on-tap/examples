#!/usr/bin/env python

'''fibonacci_cls.py: Fibonacci sequence generator using a class'''

__author__      = "@Code.on.Tap"
__copyright__   = "Copyright 2019"
__license__     = "MIT"
__source__      = "https://github.com/code-on-tap/examples/generators/fibonacci_cls.py"

class Fibonacci( object ):
  def __init__( self, qty ):
    self.i = 0
    
    self.fib  = 0 # fib
    self.fib_ = 1 # fib prime (next)
    self.qty  = qty
  
  # initialize iterator
  def __iter__( self ):
    self.i = 0
    
    self.fib  = 0 # fib
    self.fib_ = 1 # fib prime (next)
    return self
  
  # python 3 iterator helper
  def __next__( self ):
    return self.next()
  
  # python 2 iterator helper
  def next( self ):
    self.i += 1
    if self.i >= self.qty:
      raise StopIteration()
    
    else:
      current_value = self.fib + self.fib_
      self.fib, self.fib_ = self.fib_, current_value
      return current_value


for f in Fibonacci( 10 ):
  print( f )
#> 1
#> 2
#> 3
#> 5
#> 8
#> 13
#> 21
#> 34
#> 55
#> 89
