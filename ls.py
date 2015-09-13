import os
import sys
A=os.listdir()
u=sys.argv
a=[]
b=[]
arg=""
l=0
c=[]
er="."
ar=".."
if len(u)==1:
	for i in A:
		if i[0]!=".":
			
			a.append(i)
	for h in a:
		if l<len(h):
			l=len(h)
	for h in a:
		while len(h)<l+2:
			h=h+" "
			
		b.append(h)
	
	while len(b)-1!=-1:
		if len(arg+b[0])>80:
			c.append(arg)
			arg=""
		else:
			arg=arg+b[0]
			b.pop(0)
	c.append(arg)
	for k in c:
		print(k)


elif u[1]=="-a":
	for h in A:
		if l<len(h):
			l=len(h)
	for h in A:
		while len(er)<l+2:
			er=er+" "
		
		while len(ar)<l+2:
			ar=ar+" "
	b.append(er)
	b.append(ar)
	for h in A:

		while len(h)<l+2:
			h=h+" "
			
		b.append(h)
	
	while len(b)-1!=-1:
		if len(arg+b[0])>80:
			c.append(arg)
			arg=""
		else:
			arg=arg+b[0]
			b.pop(0)
	c.append(arg)
	for k in c:
		print(k)