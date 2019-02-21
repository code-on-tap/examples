#!/usr/bin/env python

'''fibonacci.py: Fibonacci sequence generator'''

__author__      = "@Code.on.Tap"
__copyright__   = "Copyright 2019"
__license__     = "MIT"
__source__      = "https://github.com/code-on-tap/examples/generators/fibonacci.py"

def fibonacci( n ):
  x = 0
  y = 1
  for i in xrange( n ):
    x, y = y, x+y
    yield y

for f in fibonacci( 10 ):
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
