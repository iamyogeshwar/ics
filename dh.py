# Diffie Hellman

from random import randint

if __name__ == '__main__':

	# Both the persons will be agreed upon the 
	# public keys G and P 
	# A prime number P is taken 
	P = int(input('Enter Prime Number P: '))
	
	# A primitve root for P, G is taken
	G = int(input('Enter another prime number G: '))
	
	
	print('The Value of P is :%d'%(P))
	print('The Value of G is :%d'%(G))
	
	# Alice will choose the private key a 
	a = int(input('Alice please enter your private key: '))
	print('The Private Key a for Alice is :%d'%(a))
	
	# gets the generated key
	x = int(pow(G,a,P)) 
	
	# Bob will choose the private key b
	b = int(input('Bob please enter your private key: '))
	print('The Private Key b for Bob is :%d'%(b))
	
	# gets the generated key
	y = int(pow(G,b,P)) 
	
	
	# Secret key for Alice 
	ka = int(pow(y,a,P))
	
	# Secret key for Bob 
	kb = int(pow(x,b,P))
	
	
	print('Secret key for the Alice is : %d'%(ka))
	print('Secret Key for the Bob is : %d'%(kb))
	
	
'''
Output:

Enter Prime Number P: 5
Enter another prime number G: 7
The Value of P is :5
The Value of G is :7
Alice please enter your private key: 2
The Private Key a for Alice is :2
Bob please enter your private key: 3
The Private Key b for Bob is :3
Secret key for the Alice is : 4
Secret Key for the Bob is : 4


'''
	
