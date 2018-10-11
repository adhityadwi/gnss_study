#Standalone Acquisition Program
#created by Dicky Dwiantoro

import math as mt
import numpy as np
import time as tt
import scipy.io as sio
import matplotlib.pyplot as figplot
import getACFvalue as autocorr

ACF = sio.loadmat('R_BPSK_2MHz.mat')

cel = 299792458
Fcarr = 1176.45 * pow(10,6)
Fcode = 10.23*pow(10,6)
Nchip = 10230
Tp = 8*Nchip/Fcode
CNo = 25
gain = 3
CNo = CNo + gain

A=mt.sqrt(2*pow(10,CNo/10)*Tp)

Tint = Tp
noncoh = 13
Threshold = 5.5

# define doppler search bin
dopmin = -1200
dopstep = 1/2/Tint
dopmax = 1200
dopest = np.arange(dopmin,dopmax,dopstep)
ndopbin = len(dopest)

# define code search bin
delmin = -600*Fcode/cel
delstep = 1/2
delmax = 600*Fcode/cel
delest = np.arange(delmin,delmax,delstep)
ndelbin = len(delest)

# simulated true range
doppler = 1000
range0=507.5

# define the store matrix for acq result

temp_prompt = np.zeros((ndopbin,ndelbin),dtype=complex)
prompt = np.zeros((ndopbin,ndelbin))

for i in range(1):

    for k in range(0,noncoh+1):

         for j in range(ndopbin):
            distance = range0+(doppler*cel/Fcarr*(k-1)*Tint)

            phase_true = distance*Fcarr/cel
            doppler_true= doppler
            delay_true=distance*Fcode/cel

            dop_er = doppler_true-dopest[j]
            phase_er = 2*mt.pi*np.fmod(phase_true,1)

            for m in range(ndelbin):
                #print(m)
                delay_er = delay_true - delest[m]
                #print(delay_er)
                noise = np.random.randn()
                #print(noise)
                temp_prompt[j,m] = A*autocorr.Rc(delay_er,ACF)*np.sinc(dop_er*Tint)*np.exp(1j*phase_er) + (noise + 1j*noise )




    prompt = prompt + pow(abs(temp_prompt),2)

    figplot.plot(prompt)
    figplot.show()

  

