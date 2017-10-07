from itertools import chain

import cv2
import numpy as np
import matplotlib.pyplot as plt


def histogramify(mat,img_name):

	dic=dict()
	N,M=mat.shape

	for i in range(N):
		for j in range(M):
			if mat[i][j] in dic:
				dic[mat[i][j]]+=1
			else:
				dic[mat[i][j]]=1

	#print dic
	plt.bar(range(len(dic)), dic.values(), align='center')
	plt.savefig(img_name)
	plt.clf()


def histogramify2(mat,img_name):

	dic=dict()
	N,M=mat.shape
	for i in range(N):
		for j in range(M):
			if mat[i][j] in dic:
				dic[mat[i][j]]+=1
			else:
				dic[mat[i][j]]=1

	dic = list(chain.from_iterable([k]*v for k, v in dic.items()))
	bins=np.arange(0,1.01,0.01)
	plt.hist(dic,bins=bins)
	plt.savefig(img_name)
	plt.clf()


if __name__=='__main__':

	img=cv2.imread('anadka.jpg')
	#img=cv2.resize(img,(img.shape[1]/4,img.shape[0]/4))
	b,g,r=cv2.split(img)
	N,M=b.shape

	H=np.zeros([N,M])
	S=np.zeros([N,M])
	I=np.zeros([N,M])

	for i in range(N):
		for j in range(M):

			R=float(r[i][j])
			B=float(b[i][j])
			G=float(g[i][j])

			I[i][j]=int((R+G+B)/3)

			S[i][j]=1-(3/(R+G+B)*min(R,G,B))

			if R==G==B:
				H[i][j]=0
			else:
				theta=np.arccos(0.5*((R-G)+(R-B))/(((R-G)**2+(R-B)*(G-B))**0.5))
				if B<=G:
					H[i][j]=theta
				elif B>G:
					H[i][j]=2*np.pi-theta
				H[i][j]=int(H[i][j]*360/(2*np.pi))

	histogramify(H,'q1_output_hue.png')
	histogramify2(S,'q1_output_saturation.png')
	histogramify(I,'q1_output_intensity.png')

