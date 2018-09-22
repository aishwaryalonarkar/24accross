import random 
global row,column

def forg():
    global i,row,column
    row=[0,0,0,0,0]
    column=[0,0,0,0,0]
    i=1
    generate()
    i=0
    generate()
    c=1
    for i in range (2,5):
        generate()

def generate():
    global a,b
    a=random.randint(1,9)
    b=random.randint(1,9)
    check()

def check(): 
    global i,row,column,c,a,b,rowsum,colsum
    rowsum=sum(row)+a
    colsum=sum(column)+b

    if i==1:
        c=0
        putx()

    if i!=1 and i<4:
        if rowsum>=24 or colsum>=24:
            generate()
        else:
            c=1
            putx()

    if i==4:
        rowsum=rowsum-a
        colsum=colsum-b
        if rowsum<24 and colsum<24:
            if 24-rowsum<10 and 24-colsum<10:
                a=24-rowsum
                b=24-colsum
        if rowsum+a!=24 and colsum+b!=24:
            forg()
        else:
            c=1
            putx()


def putx():
    global c,i,a,b,rowsum,colsum
    if c==0:
        row[i]=a
        column[i]=a
    else:
        row[i]=a
        column[i]=b
    #print "row",row
    #print "rowsum",sum(row)
    #print "col",column
    #print "colsum",sum(column)

forg()
print '   ___'
print '  |',column[0],'|'
print ''
print '___________________'
for i in row:
    print i,'|',
print ''
print '____________________'
for i in range(2,5):
        print '  |',column[i],'|'
print '   ___'