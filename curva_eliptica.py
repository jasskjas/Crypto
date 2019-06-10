#Python2.7
#Cadena Martinez Fernando
#ESCOM IPN
from sympy.ntheory import isprime
from Crypto.Util.number import *
import gmpy
from Crypto.Util import number
import sympy
import math
import random

#sumas de alfa  (para valores impares hacer las sumas a mano)
def suma(x1,y1,x2,y2,p,a):
	if (x1!=x2 or y1!=y2):
		landa=((y2-y1)*(long(gmpy.invert(x2-x1,p))))%p
		x3=((landa**2)-(x1+x2)) % p		
		y3=(((landa)*(x1-x3))-y1) % p
		return x3,y3
	if (x1==x2 and y1==y2):
		landa=(((3*(x1**2))+a)*(long(gmpy.invert((2*y1),p))))%p
		x3=((landa**2)-(2*x1))%p
		y3=((landa*(x1-x3))-y1)%p
		return x3,y3
#obtener p,q
def curva(p,q,m):
	p=p#p#int(input())
	q=q			
	m=m
	print "p: ",p,"q: ",q
	print "numero de soluciones: ",(p+1+2*a)
	x0=55211#random.randint(2, p-1)
	y0=443096#random.randint(2, p-1)	
	print "x0:",x0,"y0:",y0
	#k=(x^3-y^2)(x)^-1 mod p
	rest=((x0**3)-(y0**2)) % p
	invx=long(gmpy.invert(x0,p))
	k= (rest * invx) % p
	print "k: ",k
	print "###################"
	print "condiciones de k"
	print "###################"
	primera=((k**((p-1)/4))%p)
	segunda=((k**((p-1)/2))%p)
	if (primera != 1 and segunda == 1):
		
			
		print "k^((p-1)/4)modp = ",primera,"no es congruente con 1 , no es potencia cuarta"
		print "k^((p-1)/2)modp = ",segunda," es congruente con 1 , es potencia cuadrada"		
		print "###########################"
		print "comprobando Y^2=x^3-kxmod p"
		print "###########################"		
		#Y**2=x**3-kxmod p
		y2=((x0**3)-(k*x0))%p
		print "curva eliptica: y^2 = x^3 -kx mod p -> ", y2
		ecu=(y0**2)%p
		print "y0^2 mod p -> ", ecu
		soluciones=[(x0,y0)]
		num=bin(q-1)
		conv=str(num[2:])
		print "########################"
		print "Calculando sumas de alfa"		
		print "########################"
		print "q-1 en binario: ",conv
		rango=len(conv)
		print "numero de sumas echas: ",rango
		for cont in range(0,rango):
			soluciones.append(suma(soluciones[cont][0],soluciones[cont][1],soluciones[cont][0],soluciones[cont][1],p,-k))#calcular (q-1)alfa=(x1,y1), condiciones: x1=x0 y y1=p-y0
		j=1		
		for i in range(len(soluciones)):				
			print "alfa",j,soluciones[i]
			j=j*2
			
		
		print "#############################"
		print "condiciones de curva eliptica"
		print "#############################"
		if(((4*((-k**3)))%p) != 0):
			print "es No Singular"
		if((q%p) != 1 ):
			print "es No Super Singular"
		if(q != p):
			print "No es de traza uno"
		



	#nuevos valores para x0,y0 en caso de ser random
	else:
		curva(p,q,a)

#main
print "__________##### Curva Eliptica #####_________\n\n"
print "###################"
print "Valores Necesarios"
print "###################"
print "proponga una a que sea un numero primo"
a=651#int(input())
b=170
m=3
print "a: ",a
print "b: ",b

#en caso de proponer "a" calcula el primo p y q, etc..
while (True):
	p= (a**2) + (b**2)
	if (isprime(p)):
		if ( ((p%4)==1)and((a+b)%4 == 1)):
			print "p:",p," es un candidato para q" 
			print "p%4: ",(p%4)
			q=(p+2*a+1)/(4)
			if (isprime(q)):
				p=p
				q=q
				curva(p,q,m)
				break	
				
			else: 
				b+=2
				
		else: 
			b+=2
			
	else: 
		b+=2
			


