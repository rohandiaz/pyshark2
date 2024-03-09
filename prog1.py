def decode(text):
    wrd=''
    finalout=''
    rawtext=text  #00:00:00:36:00:e8:2d:fc:b5:e3:00:00:11:19:00:00:00:0e:00:00:00:0a:00
    #print(rawtext)
    #print(len(rawtext))
    for i in range(len(rawtext)):
     ch=rawtext[i]
     if(ch!=':'):
        wrd=wrd+ch
     #print(wrd)
     if(len(wrd)==2):
       finalout=finalout+str(chr(hextoascii(wrd)))
       wrd=''
    return finalout


def hextoascii(chr):#chr must be of 2 letters
    toconvert=chr #e8

    #1st var
    if(toconvert[0]=='0'):
        a=0
    if(toconvert[0]=='1'):
        a=1
    if(toconvert[0]=='2'):
        a=2
    if (toconvert[0]=='3'):
        a=3
    if (toconvert[0] == '4'):
        a=4
    if (toconvert[0] == '5'):
        a=5
    if (toconvert[0] == '6'):
        a=6
    if (toconvert[0] == '7'):
        a=7
    if (toconvert[0] == '8'):
        a=8
    if (toconvert[0] == '9'):
        a=9
    if (toconvert[0] == 'a'):
        a=10
    if (toconvert[0] == 'b'):
        a=11
    if (toconvert[0] == 'c'):
        a=12
    if (toconvert[0] == 'd'):
        a=13
    if (toconvert[0] == 'e'):
        a=14
    if (toconvert[0] == 'f'):
        a=15

    #2nd var
    if (toconvert[1] == '0'):
        b = 0
    if (toconvert[1] == '1'):
        b = 1
    if (toconvert[1] == '2'):
        b = 2
    if (toconvert[1] == '3'):
        b = 3
    if (toconvert[1] == '4'):
        b = 4
    if (toconvert[1] == '5'):
        b = 5
    if (toconvert[1] == '6'):
        b = 6
    if (toconvert[1] == '7'):
        b = 7
    if (toconvert[1] == '8'):
        b = 8
    if (toconvert[1] == '9'):
        b = 9
    if (toconvert[1] == 'a'):
        b = 10
    if (toconvert[1] == 'b'):
        b = 11
    if (toconvert[1] == 'c'):
        b = 12
    if (toconvert[1] == 'd'):
        b = 13
    if (toconvert[1] == 'e'):
        b = 14
    if (toconvert[1] == 'f'):
        b = 15
    deci=b+(16*a)
    return deci
#print (hextoascii('41'))
#print (chr(hextoascii('41')))
#print("output is")
#print(decode("0a:fc:00:36:41:e8:2d:fc:b5:e3:00:00:11:19:00:00:00:0e:00:00:00:0a:00"))
