from StringIO import StringIO
import random 
import pycurl
import decimal
import time

def gen_random_decimal(d):
   return decimal.Decimal('%d.%d' % (0,random.randint(0,d)))

out = open("data.txt","w")

urll = 'http://inscripciones.fi-a.unam.mx/consulta_horarios/index.php/horarios/consulta/'

dormir = 0
for x in xrange(4000,5000):
		num = str(x)
		dormidiro = str(dormir)
		print("Voy a checar la clave  "+ num + " y estoy en el ciclo de "+ dormidiro)
		url = urll + num
		storage = StringIO()
		c = pycurl.Curl()
		c.setopt(c.URL, url)
		c.setopt(c.WRITEFUNCTION, storage.write)
		c.perform()
		c.close()
		dormir = dormir + 1
		content = storage.getvalue()
		if not content[180] == 'N':
			print(" La clave "+num+' Si existe ')
			nombrefile = num + ".txt"
			out1 = open(nombrefile,'w')
			out.write(num +'\n')
			out1.write(storage.getvalue())
		if dormir == 35:
			print('me voy a dormir')
			time.sleep(65)
			print("revivi")
			dormir = 0
		time.sleep(gen_random_decimal(99))
out.close()