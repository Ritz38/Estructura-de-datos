from collections import deque
Casos=int(input())
for _ in range(Casos):
	A=deque(range(int(input()),0,-1))
	A1="A"
	B=deque()
	B1="B"
	C=deque()
	C1="C"
	error=False
	while True:
		m=deque(input().split())
		if m[0]=="X": break
		if error: continue
		if (m[0]==A1 and len(A)==0) or (m[0]==B1 and len(B)==0) or (m[0]==C1 and len(C)==0): error=True
		if error: continue

		if m[0]=="A":
			d= A.pop()
			if m[1]=="A": A.apppend(d)
			elif m[1]=="B":
				if B:
					if d>B[-1]: error=True
					else: B.append(d)
				else: B.append(d)
			else: 
				if C:
					if d>C[-1]: error=True
					else: C.append(d)
				else: C.append(d)


		elif m[0]=="B":
			d= B.pop()
			if m[1]=="A": 
				if A:
					if d>A[-1]: error=True
					else: A.append(d)
				else: A.append(d)
			elif m[1]=="B": B.apppend(d)
			else: 
				if C:
					if d>C[-1]: error=True
					else: C.append(d)
				else: C.append(d)


		else:
			d= C.pop()
			if m[1]=="A": 
				if A:
					if d>A[-1]: error=True
					else: A.append(d)
				else: A.append(d)
			elif m[1]=="B":
				if B:
					if d>B[-1]: error=True
					else: B.append(d)
				else: B.append(d)
			else: C.apppend(d)

		
		
			
		
	if error:
		print("secuencia invalida")
	elif not A and not B: print("soluciona la torre")
	else: print("no soluciona la torre")