import datetime, hashlib

def isonow(millis=False):
    dt = datetime.datetime.utcnow()
    if not millis:
        dt = dt.replace(microsecond=0)
        pass
    return dt.isoformat() + 'Z'

def rmd160hd(x):
    h = hashlib.new('ripemd160')
    h.update(x)
    return h.hexdigest()
