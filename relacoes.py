def classifica_funcao(r,b):
    classe=""
    flag1=0
    for y in range(4):
        x=0
        if(b[x][y] == True):
            flag1 +=1
            if(flag1==1):
                y1=y

    flag2=0
    for y in range (4):
        x=1
        if(b[x][y] == True):
            flag2 +=1
            if(flag2==1):
                y2=y            
    flag3=0
    for y in range (4):
        x=2
        if(b[x][y] == True):
            flag3 +=1
            if(flag3==1):
                y3=y            
    flag4=0
    for y in range(4):
        x=3
        if(b[x][y] == True):
            flag4 +=1
            if(flag4==1):
                y4=y               
    if(flag1==1 and flag2==1 and flag3==1 and flag4==1):
        classe += "F"
        if(y1 != y2 and y1 != y3 and y1 != y4 and y2 != y3 and y2 != y4 and y3 != y4):
            classe += "Fb"
            classe += "Fi"
            classe += "Fs"
        else:
            classe += "Fs"         
    return classe

def classifica(r,b):
    classe = ""
    reflexiva=False
    if (r&585==585) :
        classe += "R"
        
    #simetrica
    if (b[0][1]==b[1][0] and b[2][1]==b[1][2] and b[0][2]==b[2][0] and b[0][3]==b[3][0] and b[2][3]==b[3][2] and b[1][3]==b[3][1]):
        classe += "S"
        
    # transitividade
    transitiva = True
    for x in range (4):
        for y in range (4):
            if b[x][y]:
                for z in range (4):
                    if b[y][z]:
                       if not (b[x][z]):
                           transitiva=False
    if(transitiva == True):
        classe += "T"
            
    # irreflexividade
    if reflexiva==False:
        classe += "I"
        

        
    # funcao
    if(r>4095):
        classe += classifica_funcao(r,b)
    return classe

        
def imprime_relacao(relacao,r,b):
        c=relacao[r]
        resp = '{'
        for i in range(4):
            for j in range(4):                
                if b[i][j]:
                    resp += "("+ str(i+1) + "," + str(j+1) +")"
        resp += '}'
        ref_arquivo.write(resp)
        ref_arquivo.write(" "+c)
        ref_arquivo.write("\n")
        
ref_arquivo = open("relacoes.txt","w")
resp = {}
for r in range(65536):
    if resp.get(r) == None:
        b = [["","","",""],["","","",""],["","","",""],["","","",""]]
        b[0][3]= r & 32768 == 32768 #9  0  
        b[2][3]= r & 16384 == 16384 #9  0  
        b[1][3]= r & 8192 == 8192 #9  0     
        b[3][2]= r & 4096 == 4096 #9  0     
        b[3][1]= r & 2048 == 2048 #9  0     
        b[3][0]= r & 1024 == 1024 #9  0    
        b[3][3]= r & 512 == 512 #9  0
        b[2][0]= r & 256 == 256 #9  0
        b[0][2]= r & 128 == 128 #8  0
        b[2][2]= r & 64 == 64   #7  0
        b[1][2] = r & 32 == 32  #6  1
        b[2][1]= r & 16 == 16   #5  0
        b[0][0] = r & 8 == 8    #4  0
        b[0][1] = r & 4 == 4    #3  1
        b[1][0] = r & 2 == 2    #2  0
        b[1][1] = r & 1 == 1    #1  1
        resp[r] = classifica(r,b)    
        imprime_relacao(resp,r,b)
ref_arquivo.close()