# RSA algorithm

from math import gcd

def main():

	p = int(input('Enter p: '))
	q = int(input('Enter q: '))

	#step 1
	
	n = p * q
	print(f'N is {n}')
	
	#step 2:
	
	phiOfN = (p-1) * (q-1)
	e = 2
	while e < phiOfN:
		if gcd(e,phiOfN)==1:
			break
		else:
			e = e+1
			
	
	k = 2
	d = (1+(k * phiOfN)) / e
	d = int(d)
	
	msg = int(input('Enter the message you want to encrypt: '))
	
	c = pow(msg, e, n)

	m = pow(c, d, n)
	
	print('Enc', bin(c)[2:])
	print('Dec', m)


main()

'''
Output:

Enter p: 5       
Enter q: 7
N is 35
Enter the message you want to encrypt: 6
Enc 110
Dec 6


'''


