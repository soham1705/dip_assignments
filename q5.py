import cv2
import numpy as np


def D(u,v,P,Q):
	return np.sqrt((u-P/2)**2+(v-Q/2)**2)


def IdealFilter(f):

	N,M=f.shape
	D0=100
	H=np.zeros([N,M])

	for row in range(N):
		for col in range(M):
			if D(row,col,N,M)<=D0:
				H[row][col]=1

	G=np.multiply(H,f)
	#print G
	return G


def ButterworthFilter(f):

	N,M=f.shape
	D0=100
	n=3
	H=np.zeros([N,M])

	for row in range(N):
		for col in range(M):
			H[row][col]=1/(1+(D(row,col,N,M)/D0)**(2*n))

	G=np.multiply(H,f)
	return G



if __name__=='__main__':

	img=cv2.imread('q5_input.jpg')
	img=cv2.split(img)[0]

	#ideal low pass filter

	f=np.fft.rfft(img)
	g=IdealFilter(f)
	final1=np.fft.irfft(g)
	print "final",final1

	cv2.imwrite('q5_output_ideal.jpg',final1)

	#butterworth low pass filter

	f=np.fft.rfft(img)
	g=ButterworthFilter(f)
	final2=np.fft.irfft(g)
	#print "final",final1

	cv2.imwrite('q5_output_butterworth.jpg',final2)


