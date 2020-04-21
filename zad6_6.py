import numpy as np 
sl = ['kajots','aahqke','peczka','eygzwn','lxbaki','apteka']
s =[[],[],[],[],[],[]]
for i in range(0,6,1):
    s[i] = np.array(list(sl[i]))
    s[i] = np.fromiter(sl[i], dtype='U1')
    print(s[i])