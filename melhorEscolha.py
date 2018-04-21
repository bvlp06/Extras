def procuraNaMatriz(i,p,nos,vis,u,noFinal,g):
    if (len(p) > 0):
        p.pop(0)
    for j in range (0,10):
        if matrizAdj[i][j]>0:
            if vis[j][i]!=1:
                p.append([nos[j], matrizAdj[i][j]+u[0][1] ])
                g.append([u[0][0]+str(u[0][1]), nos[j]+str(matrizAdj[i][j]+u[0][1])] )
                p.sort(key=lambda x: x[1])
                vis[i][j]=1
    return p,g
nos = ['A','B','C','D','E','F','G','H','I','J']
matrizAdj=[[0, 10, 2, 3, -1, -1, -1, -1, -1, -1] , [10,0,3,-1,2,3,-1,-1,-1,-1],[2,3,0,-1,-1,-1,11,-1,-1,-1],[3,-1,-1,0,-1,-1,-1,8,-1,-1],[-1,2,-1,-1,0,4,-1,-1,3,-1],[-1,3,-1,-1,4,0,4,-1,-1,10],[-1,-1,11,-1,-1,4,0,1,-1,14],[-1,-1,-1,8,-1,-1,1,0,-1,16],[-1,-1,-1,-1,3,-1,-1,-1,0,9],[-1,-1,-1,-1,-1,10,14,16,9,0] ]
vis=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
noInicio=input('Qual o no inicial?   ')
noFinal=input('Qual o no final?   ')
i=nos.index(noInicio)
p=[]
u=[]
u.append([noInicio,0])
g=[]
G={}
print('lista de prioridade')
while(nos.index(noFinal) != i):
    p,g=procuraNaMatriz(i,p,nos,vis,u,noFinal,g)
    print(u)
    u[0] = p[0]
    i=nos.index(p[0][0])
    print(p)
    aux=0
    while(i==nos.index(noFinal) and (aux<len(p))):
          x=p.pop(0)
          i=nos.index(p[0][0])
          p.append(x)
          aux=aux+1
          u[0]=p[0]
          
print('arvore')
print(g)
