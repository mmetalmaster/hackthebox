import binascii
import struct

# return (g, x, y) a*x + b*y = gcd(x, y)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def decryptRSA(p,q,e,ct):
	# compute n
	n = p * q
	phi = (p - 1) * (q - 1)	
	gcd, a, b = egcd(e, phi)
	d = a
	print "d: " + str(d)
	pt = pow(ct, d, n)
	return pt

def encryptRSA(p,q,e,pt):
	# compute n
	n = p * q
	phi = (p - 1) * (q - 1)
	gcd, a, b = egcd(e, phi)
	d = a
	print "d: " + str(d)
	ct = pow(pt, e, n)
	return ct


def convert(int_value):
   encoded = format(int_value, 'x')
   length = len(encoded)
   encoded = encoded.zfill(length+length%2)
   return encoded.decode('hex')

# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def main():
	# By implementing Chinese remainder algorithm
	# 1) p and q are the primes
	# 2) dp = d mod (p - 1)
	# 3) dq = d mod (q - 1)
	# 4) Qinv = 1/q mod p *This is not integer devision but multiplicative inverse
	# 5) m1 = pow(c, dp, p)
	# 6) m2 = pow(c, dq, q)
	# 7-1) h = Qinv(m1 - m2) mod p  ; if m1 < m2
	# 7-2) h = Qinv * (m1 + q/p) 
	# 8) m = m2 + hq

	# m = 65
	# p = 61
	# q = 53
	# dp = 53
	# dq = 49
	# c = 2790

	p = 7901324502264899236349230781143813838831920474669364339844939631481665770635584819958931021644265960578585153616742963330195946431321644921572803658406281 
	q = 12802918451444044622583757703752066118180068668479378778928741088302355425977192996799623998720429594346778865275391307730988819243843851683079000293815051 
	dp = 5540655028622021934429306287937775291955623308965208384582009857376053583575510784169616065113641391169613969813652523507421157045377898542386933198269451 
	dq = 9066897320308834206952359399737747311983309062764178906269475847173966073567988170415839954996322314157438770225952491560052871464136163421892050057498651 
	c = 62078086677416686867183857957350338314446280912673392448065026850212685326551183962056495964579782325302082054393933682265772802750887293602432512967994805549965020916953644635965916607925335639027579187435180607475963322465417758959002385451863122106487834784688029167720175128082066670945625067803812970871

	Qinv = mulinv(q,p)
	print "Qinv: " + str(Qinv)

	m1 = pow(c, dp, p)
	print "m1: " + str(m1)

	m2 = pow(c, dq, q)
	print "m2: " + str(m2)

	h = (Qinv * (m1 - m2)) % p
	print "h: " + str(h)

	m = m2 + (h*q)
	print "m: " + str(int(m))

	hexadecimals = str(hex(m))[2:-1]
	print "solved: " + str(binascii.unhexlify(hexadecimals))

if __name__ == "__main__":
	main()


# http://crypto.stackexchange.com/questions/19413/what-are-dp-and-dq-in-encryption-by-rsa-in-c
# https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Using_the_Chinese_remainder_algorithm
# https://zzundel.blogspot.com/2011/02/rsa-implementation-using-python.html