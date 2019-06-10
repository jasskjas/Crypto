from Crypto.Util.number import *
import gmpy
from Crypto.Util import number
from Crypto.PublicKey.RSA import construct
from Crypto.PublicKey import RSA
import sympy

#b=e  y a=d 
print "__________##### RSA #####_________"


exponente =101
mensaje=72 
p=409
q=503
phi=(p-1) * (q-1)
n=p*q

# ya tenemos p, q, N, e, mensaje_encriptado
print "mensaje: " + str(mensaje)
print "n: " + str(n)
print "p: " + str(p)
print "q: " + str(q)
print "phi(n): "+ str(phi)
print "b: " + str(exponente)

#para examen (axbmod n) = 1 mod phi
#a=long(gmpy.invert(b,phi)) ->  a=b^-1 mod phi(n)

# calcular d, llave privada En clase es la a
d = long(gmpy.invert(exponente,phi)) # comprobar con (a x b mod phin) = (1 mod phin)
#FIRMA
hasha=71		
F=pow(hasha,d,n) # h=67  #				 F=h^a mod n 
h=pow(F,exponente,n) #comprobar funcion hasha    h=F^b mod n
print "a: " + str(d)
print "****************************************************************************"
print "Has-sha: ",hasha
print "Firma: "+ str(F)
print "h: " + str(h)

cipher= pow(mensaje, exponente, n)#para cifrar el mensaje
descipher = pow(cipher, d, n)#para descifrar el mensaje
print "Mensaje cifrado: " + str(cipher)
print "Mensaje decifrado: " + str(descipher)
#print bin(mensaje_desencriptado)#mensaje en binario

msj = long_to_bytes(descipher)
print "Mensaje en texto plano: " +str(msj)	




