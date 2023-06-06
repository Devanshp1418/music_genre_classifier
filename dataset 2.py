from classi import clasi as cl
from analyzer import getfr
import os
music={'pop':[(7521, 456), (5735, 598), (4073, 842), (4495, 763), (5523, 621), (13943, 246)],
       'rock':[(6699, 512), (6191, 554), (4666, 735), (6846, 501), (7866, 436)],
       'classical':[(4414, 777), (5444, 630), (5014, 684), (4203, 816), (5317, 645)],
       }
while(True):
    path=str(input(""))
    if os.path.exists(path)== True:
        sam=getfr(path)
        music['country'].append(sam)
        print(music['country'])
    else: break

