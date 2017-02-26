t=int(input("Apo posa stoixeia tha apoteleite h lista? "))
x=[""]*t
for i in range (1,t+1):
    print "dwse to ",i,"o stoixeio ths listas: "
    x[i-1]=raw_input()
for a in range (1,t+1):
    for i in  range (1,t+1):
        if (x[i-1]=="0"):
            del x[i-1]
            x.extend(['0'])
if (t==0):
	print "H lista einai kenh!"
else:
	print "H lista einai: ",x