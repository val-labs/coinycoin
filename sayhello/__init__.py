import os, sys, time, peer2peer, datetime, hashlib

from cStringIO import StringIO

def rmd160hd(x):
    h = hashlib.new('ripemd160')
    h.update(x)
    return h.hexdigest()

def isonow(millis=False):
    dt = datetime.datetime.utcnow()
    if not millis:
        dt = dt.replace(microsecond=0)
        pass
    return dt.isoformat() + 'Z'

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
