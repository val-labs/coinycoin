import os, sys, time, peer2peer, datetime, hashlib
from util import rmd160hd, isonow

def validate(idline, msg):
    rmd = idline.split()[-1]
    rmd2 = rmd160hd(msg)
    print("PROCESS {} {} {}".format(rmd, rmd2, repr(msg)))
    return rmd if rmd == rmd2 else False

def save(rmd, whole_msg):
    if not rmd:
        return sys.stderr.write("no way, dropping")
    fname1 = "t/xtn.{}".format(rmd)
    fname2 = "n/xtn.{}".format(rmd)
    with open(fname1, 'w') as f: f.write(whole_msg)
    os.link(fname1, fname2)
    pass
    
def main():
    os.system('mkdir -p xtns')
    time.sleep(0.25)
    ws = peer2peer.conn(sys.argv[1])
    peer2peer.subscribe(ws, '0 1 2 i.xtn')
    while 1:
        msg = peer2peer.recv(ws)
        save(validate(*msg[2].split('\n', 1)), msg[2])
        time.sleep(0.1)
