#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
# hasil_kecerdasan = [ 6 , 9 , 3 , 8 , 7 , 5 , 8 , 10 ]
# hasil_produksi_lusin = [ 30 , 49 , 18 , 42 , 39 , 25 , 41 , 52 ]

def inputnilai():
    x = []
    y = []
    z = int(input("Banyak Data : "))
    print("-------------------------")
    for i in range(0,z):
        x2 = int(input("Masukkan Nilai X : "))
        x.append(x2)
    print("-------------------------")
    for i in range(0,z):
        y2 = int(input("Masukkan Nilai Y : "))
        y.append(y2)
    print("-------------------------")
    return x,y
def linearRegresion(data):
	'''
		indeks[0] -> response variable -> x
		indeks[1] -> predictor variable -> y
	'''
	x2=[]
	y2=[]
	xy=[]
	n = len(data[0])

	for x in data[0]:
		x2.append(x**2)

	for y in data[0]:
		y2.append(y**2)

	i=0;
	while(i<n):
		dump = data[0][i]*data[1][i]
		xy.append(dump)
		i+=1
	jmlhx = sum(data[0])
	jmlhy = sum(data[1])
	jmlhx2 = sum(x2)
	jmlhy2 = sum(y2)
	jmlhxy = sum(xy)

	a = ((jmlhy*jmlhx2)-(jmlhx*jmlhxy))/(n*jmlhx2-(jmlhx**2))
	b = ((n*jmlhxy)-(jmlhx*jmlhy))/(n*jmlhx2-(jmlhx**2))

	return(a,b)

def gambarGrafik(dataProses):
	a,b = linearRegresion(dataProses)
	print("Nilai a adalah %.2f"%(a))
	print("Nilai b adalah %.2f"%(b))
	print("Y' = ", '%.2f' %a ," + ",'%.2f'%b,"x")
	print("-------------------------")

	z = dataProses[0]

	for i in z:
		c = (a+b*i)
		print("Y' = %8.2f"%(c))
	# for x in range(0,z):
	# 	x2.append(x**2)
	# 	c = (b+(a*x2))
	# 	print("Y' = %.2f"%(c))

	def f1(keanggotaan,a,b):
		hit = []
		for x in keanggotaan:
			y = b*x+a
			hit.append(y)
		return(hit)
	plt.scatter(dataProses[0],dataProses[1],label='data aktual',s=10)
	plt.plot(dataProses[0],f1(dataProses[0],a,b),c='k',label='hasil regresi without',linewidth=0.5)
	plt.title("Diagram Pencar")
	plt.ylabel("Hasil Produksi (lusin)")
	plt.xlabel("Hasil Tes Kecerdasan")
	plt.legend()
	fig = plt.figure(1)
	fig.canvas.set_window_title("Regresi Python")
	plt.show()

hasil_kecerdasan,hasil_produksi_lusin = inputnilai()
gambarGrafik([hasil_kecerdasan,hasil_produksi_lusin])