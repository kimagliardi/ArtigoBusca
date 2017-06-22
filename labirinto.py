### LABIRINTO ###
#!/usr/bin/env python
# -*- coding: utf-8 -*
# UFBA – Bacharelado em Ciência da Computação
# Turma I.A 
# Danilo Azevedo Santos

import random
TAM = 15
M = []
M = [[-1 for col in range(TAM)] for row in range(TAM)] ## preenche matriz


class Pilha(object):
    def __init__(self):
        self.dados = []
 
    def empilha(self, elemento):
        self.dados.append(elemento)
 
    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)
 
    def vazia(self):
        return len(self.dados) == 0
    
    def topo(self):
		return self.dados[len(self.dados)-1]    

def criarTab(M):
	
	for i in range(TAM):
		M[0][i] = 1 ##//	
		M[i][0] = 1
		M[i][TAM-1] = 1
		M[TAM-1][i] = 1
	for i in range(TAM -1):
		for j in range(TAM -1):
			if j!= 0 and j != TAM -1:
				sort = random.randint(0,15)
				if(sort % 4 == 0):
					M[i][j] = 1
				else:
					M[i][j] = 0
	M[1][1] = 0
	M[TAM-2][TAM-1] = 0
	mostraMatriz(M)
	
def moveAgent(M):
	
	## defini pilha ou estrutura stack P;
	P = Pilha()
	i = 1
	j = 1
	while((i != TAM-1) and (j != TAM-2)):
		M[i][j] = 2 ## agente visita a posicao indicada e marca
		if(M[i][j+1] == 0): ##// movePdireita()
			P.empilha(j+100*i)
			j+= 1
		elif(M[i][j-1] == 0): ##// movePesquerda()
			P.empilha(j+100*i)
			j-= 1
		elif(M[i+1][j] == 0): ##// movePbaixo()
			P.empilha(j+100*i)
			i+=1
		elif(M[i-1][j] == 0): ##// movePcima()
			P.empilha(j+100*i)
			i-=1
		
		elif(P.vazia()): ## sem saida
			return 0
		
		else:
			M[i][j] == 4 # trecho sem saida
			i = P.topo()/100
			j = P.desempilha() % 100 ##desempilha
		##exibirMat(i, j, M)
	return 1
	
def exibirMat(a, b, M):
	
	for i in range(TAM):
		for j in range(TAM):
			if a == i and b == j:
				print(1)
			else:
				if M[i][j] == 0: 
					print " "
					pass
				
				elif M[i][j] == 1:
					print chr(219)
					pass
				
				elif M[i][j] == 2:
					print "."
					pass
			
				else:
					print chr(176)
					pass
		print("\n")	
		## mostraMatriz(M)		
def mostraMatriz(M):
	## mudaMatriz(M)
	for i in range(TAM):
		print M[i][:]
	print "\n"	
		
def main():
	criarTab(M)
	if moveAgent(M):
		print "LABIRINTO SOLUCIONADO OK!"
		##custo
	else:
		print "SEM SOLUCAO"
		
if __name__ == "__main__":
	main()
	
	mostraMatriz(M)		
	
			
	
