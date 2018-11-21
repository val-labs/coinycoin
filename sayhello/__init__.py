import os, sys, time

from util import rmd160hd, isonow

from cStringIO import StringIO

def make_msg():
    sio = StringIO()
    sio.write("Date: {}\n".format(isonow()))
    sio.write("Text: test message\n")
    return sio.getvalue()

def main():
    time.sleep(3)
    msg = make_msg()
    sys.stdout.write("$Id: {}\n".format(rmd160hd(msg)))
    sys.stdout.write(msg)
