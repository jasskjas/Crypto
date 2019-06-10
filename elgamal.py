#Python2
#CadenaMartinezFernando
#ESCOM IPN

from Crypto.Util.number import *
import gmpy
from Crypto.Util import number
import random  
from sympy.ntheory import isprime
import math
import sys
import subprocess
import commands

def genk(p_a):
	k=random.randint(2, p_a-1)  # 2 < k <p*-1
	if(mcd(k,p_a-1)==1):
		return k
	else:
		genk(p_a)

def mcd(a, b):

	resto = 0

	while(b > 0):

		resto = b

		b = a % b

		a = resto

	return a

def exp(a, b, n):
    bina = []
    bina = tobase2(b)
    x = 1
    k = 0
    while k < len(bina):
        if bina[k] == 0:
            x = (x ** 2) % n
        elif bina[k] == 1:
            x = (x ** 2 * a) % n
        k = k + 1
    return x

def modexp( base, exp, modulus ):
	return pow(base, exp, modulus)

def primep():
	p=113#long((commands.getoutput('openssl prime -generate -bits 2048 -hex')),16)
	q=127#long((commands.getoutput('openssl prime -generate -bits 2048 -hex')),16)
	n=2	
	while (True): 	
		pas= n * (p * q) + 1
		if (isprime(pas)):
			alfa=find_primitive_root(pas)#buscar un generador con algoritmo de la raiz primitiva mod n
			
			if((alfa**((p-1)/q))%p !=1):		
				genkeys(pas,alfa)
				break
			

		else:
			n=n+2
	

def find_primitive_root( p ):
	if p == 2:
			return 1
	#the prime divisors of p-1 are 2 and (p-1)/2 because
	#p = 2x + 1 where x is a prime
	p1 = 2
	p2 = (p-1) // p1
	#test random g's until one is found that is a primitive root mod p
	while( 1 ):
			g = random.randint( 2, p-1 )
			#g is a primitive root if for all prime factors of p-1,. p[i]
			#g^((p-1)/p[i]) (mod p) is not congruent to 1
			if not (modexp( g, (p-1)//p1, p ) == 1):
					if not modexp( g, (p-1)//p2, p ) == 1:
						return g

def cifrar(x):
	print "ingresa la ruta de la llave publica: "
	ruta=raw_input()	
	f=open(str(ruta))
	alfa=long(f.next())
	p_a=long(f.next())
	B=long(f.next())	
	k=random.randint(2, p_a-1)
	print "k: ",k	
	print "alfa:",alfa 
	print "p*: ",p_a
	print "B: ",B	
	y1=modexp(alfa,k,p_a)   #y1=(alfa)^k modp*
	print y1	
	y2=pow(B,k,p_a)*(x%p_a)   #y2=x(B)^k mod p*
	print "Cifrado\n"
	print "Y1: " + str(y1)
	print "Y2: " + str(y2)
	lista=[]
	lista.append(str(y1))
	lista.append('\n')
	lista.append(str(y2))
	cifrado=open("cipher.txt","w")
	cifrado.write("".join(lista))
	cifrado.close()
	

def descifrar():
	print "ingres la ruta de la clave priada: "
	ruta=raw_input()	
	f=open(str(ruta),"r")
	a=long(f.next())
	p_a=long(f.next())
	f.close()
	print "a:",a,"p*:",p_a	
	#print "ingresa la ruta del archivo cifrado: "
	#ruta1=raw_input()
	cip=open("cipher.txt","r")
	y1=long(cip.next())
	y2=long(cip.next())
	print "y1:",y1,"y2:",y2	
	cip.close()
	pot=p_a-a-1
	descipher=pow(y1,pot,p_a) * y2%p_a
	print "archivo Decifrado"
	print descipher
	des=long_to_bytes(descipher)
	print str(des)	
	texto=open("Decifrado.txt","w")
	texto.write(des)
	texto.close()


def genkeys(p_a,alfa):
	p_a=p_a	
	alfa=alfa
	# int((commands.getoutput('openssl prime -generate -bits 10 -hex')),16)
	a=random.randint(0, p_a-1) #clave privada
	B=modexp(alfa,a,p_a) #clave publica
	lista=[]
	lista.append(str(alfa))
	lista.append('\n')
	lista.append(str(p_a))
	lista.append('\n')
	lista.append(str(B))
	lista.append('\n')
	keypub=open("pub.key","w")
	keypub.write(''.join(lista))
	keypub.close()
	
	lista2=[]
	lista2.append(str(a))
	lista2.append('\n')
	lista2.append(str(p_a))
	lista2.append('\n')
	keypri=open("priv.key","w")
	keypri.write(''.join(lista2))
	keypri.close()
	



print "__________##### ElGamal #####_________"


print "*******************************************************"
print "Elige una opcion: \n0.-Generar llaves\n1.-Cifrar\n2.-Decifrar\n3.-Salir"
op=int(input())

#llaves	
if(op==0):
	primep()
#cifrado
if(op==1):
	print "ingresa la cadena a cifrar: "
	nombre=raw_input()	 	
	#nuevo=open(str(nombre),"r")
	#mensaje=nuevo.next()
	#print mensaje
	mensaje=str(nombre)	
	x=bytes_to_long(mensaje)
	print x	
	cifrar(x)
	#	nuevo.close()

#descifrado     d(y1,y2)=[y1^(p*-a-1)][y2] mod p*
if (op==2):
		descifrar()
		



