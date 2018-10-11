def Rc(error,ACF):
    import math as mt
    import numpy as np
    import scipy.io as sio

    ACF = sio.loadmat('R_BPSK_2MHz.mat')
    aa = (ACF['rr_pic_sI'])
    aaa = aa[0][:]

    L = len(aaa)
    error = 0.25

    if (abs(error)>=1):
        Rc = 0
    else:
        index=(L-1)/2*error+(L+1)/2
        id1 = mt.floor(index)
        if id1<L:

            id2=id1+1

            argum1 = [id1,id2]
            argum2 = [aaa[id1],aaa[id2]]
            rc_res = np.interp(index, argum1,argum2 )

            return rc_res

        else:

            print('getACFvalue error!: error%f index1%d' %(error ,id1) )

            return 0