import pygeoip,os

def ipLocation(ip):
    path,f = os.path.split(__file__)
    fname = os.path.join(path, "GeoIP.dat")
    gi = pygeoip.GeoIP(fname)
    return gi.country_code_by_addr(ip)
