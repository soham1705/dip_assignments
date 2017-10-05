import cv2
import numpy as np


def D(u,v,P,Q):
	return np.sqrt((u-P/2)**2+(v-Q/2)**2)


def IdealFilter(f):

	N,M=f.shape
	D0=300
	H=np.zeros([N,M])

	for row in range(N):
		for col in range(M):
			if D(row,col,N,M)<=D0:
				H[row][col]=1

	G=np.multiply(H,f)
	return G


def ButterworthFilter(f):

	N,M=f.shape
	D0=300
	n=3
	H=np.zeros([N,M])

	for row in range(N):
		for col in range(M):
			H[row][col]=1/(1+(D(row,col,N,M)/D0)**(2*n))

	G=np.multiply(H,f)
	return G

def GaussianFilter(f):

	N,M=f.shape
	D0=300
	H=np.zeros([N,M])

	for row in range(N):
		for col in range(M):
			H[row][col]=np.exp(-D(row,col,N,M)**2/(2*D0**2))

	G=np.multiply(H,f)
	return G
	

if __name__=='__main__':

	img=cv2.imread('3.jpg')
	img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img=cv2.resize(img,(img.shape[1]/4,img.shape[0]/4))

	#ideal low pass filter

	f=np.fft.fft2(img)
	g=IdealFilter(f)
	final1=np.fft.ifft2(g).real

	cv2.imwrite('q5_output_ideal.jpg',final1)

	#butterworth low pass filter

	f=np.fft.fft2(img)
	g=ButterworthFilter(f)
	final2=np.fft.ifft2(g).real

	cv2.imwrite('q5_output_butterworth.jpg',final2)

	#gaussian low pass filter

	f=np.fft.fft2(img)
	g=GaussianFilter(f)
	final3=np.fft.ifft2(g).real

	cv2.imwrite('q5_output_gaussian.jpg',final3)


