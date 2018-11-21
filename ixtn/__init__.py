import os, sys, time, peer2peer, datetime, hashlib
from cStringIO import StringIO

def rmd160hd(x):
    h = hashlib.new('ripemd160')
    h.update(x)
    return h.hexdigest()

def process(idline, msg, whole_msg):
    rmd = idline.split()[-1]
    rmd2 = rmd160hd(msg)
    print("PROCESS {} {} {}".format(rmd, rmd2, repr(msg)))
    if rmd != rmd2:
        return sys.stderr.write("no way, dropping")
    print("OK FINE")
    fname =  "t/xtn.{}".format(rmd)
    with open(fname, 'w') as f: f.write(whole_msg)
    os.system("ln {} n".format(fname))

def main():
    os.system('mkdir -p xtns')
    time.sleep(0.25)
    ws = peer2peer.conn(sys.argv[1])
    peer2peer.subscribe(ws, '0 1 2 i.xtn')
    while 1:
        msg = peer2peer.recv(ws)
        process(*msg[2].split('\n',1), whole_msg=msg[2])
        time.sleep(0.1)
