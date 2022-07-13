import random as r
import re

def ctr(message):
    d=0
    dlist = []
    dice = ''
    ndice = ''
    calc = 0
    con = message.replace('$roll',"").strip()
    dlst = re.findall('(?:\d|)d\d+', con)
    clst = re.sub('(?:\d|)d\d+','H', con)
    for l in dlst:
        for i in l:
            if i == 'd':
                d = 1
            elif (i in '0123456789') and (d==0):
                dice+=i
            elif (i in '0123456789') and (d == 1):
                ndice+=i
        if dice!='':
            for n in range(0,int(dice)):
                calc+=r.randint(1,int(ndice))
            dlist.append(calc)
        elif dice == '':
            dlist.append(r.randint(1,int(ndice)))
        dice = ''
        ndice = ''

    for i in dlist:
        clst = clst.replace('H',str(i), 1)

    return(clst+' = '+str(eval(clst)))

