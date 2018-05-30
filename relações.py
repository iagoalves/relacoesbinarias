# A = {1,2}  pares: (1,1) (1,2) (2,1) (2,2) mapeados em 4 bits

def classifica(r):
    classe = ""

    
    # reflexividade
    # O 9 = 1001 se olhar na lista de binarios isto é [0,0][1,1] já o 73 = 1001001 = [0,0][1,1][2,2]
    if ((r & 9 == 9) and r < 16) or (r>=16 and r&73==73)  :
        classe += "R"
        
    # simetria
    simetrica = False
    # o 4 = 100 , já o 2 = 10, se os 2 forem true tenho 2 conjuntos simetricos 0110 , [1,0][0,1], caso os 2 forem falsos 1001 = [0,0][1,1] também simetricos
    b01 = r & 4 == 4
    b10 = r & 2 == 2
    b21 = r & 16 == 16
    b12 = r & 32 == 32
    b02 = r & 128 == 128
    b20 = r & 256 == 256
    if (b01 == b10 and b21==b12 and b02==b20):
        classe += "S"
        simetrica = True
    # antisimetrica tá bugado.
    #if ((((r&1 ==1 and (r&2==2 or r&32 == 32)) or (r&8==8 and (r&4==4 or r&128==128)) or (r&64 == 64 and (r&256==256 or r&16 ==16 ))) and simetrica == False) and ((b01 and b10)==False) and ((b02 and b20) == False) and ((b12 and b21) == False) ) :
        #classe += "P"
        
    # transitividade
    b00 = r & 8 == 8
    b11 = r & 1 == 1
    b22 = r & 64 == 64
    if r<16 and (not b01 or not b10 or (b00 and b11)):
        classe += "T"
        
    #essa não sei muito bem se ta certa verifiquei umas parece ok
    if r>=16 and (((not b01 or not b10) and (not b02 or not b20)  and (not b12 or not b21) ) or (b11 and b22 and b00 )):
        classe += "T"
    # irreflexividade
    if not b11 and not b22 and not b00:
        classe += "I"
        

        
    # assimetrica inverso da simetrica
    if simetrica == False:
        classe += "A"
        
    # funcao
    classe += classifica_funcao(r)
    return classe


def imprime_relacoes(relacoes):
    for (r,c) in relacoes.items():
        imprime_relacao(r,c) 
        
def imprime_relacao(r,c):
#aqui é simples de entender, para 9 relações se têm 111111111
# 1 = "têm a relação" 0="não têm a relação"
# quanto aos "==" também é simples, 1<<1 = 2^1 1<<2 = 2^2 ...
# como o ultimo conjunto é 256 = 100000000, a presença de todos conjuntos é 111111111 = 511.
#assim, sem fazer contas de combinações, sabe-se a quantia de conjuntos totais = 511
#com o número de combinações totais dentro de um for pode-se testar bit a bit de todos os conjuntos, dessa forma e retornado todas as funções
#ex: 2=10, 3=11 ... ao se passar o 2 Têm-se que (10 & 10 =2, 10 & 1 =0) assim apenas o conjunto 2 será usado
# para o 3(11&10 =2),(11&11=3),(11&01=1) assim o número 3 irá representar os conjuntos 1,2 e 3
    ref_arquivo = open("relacoes.txt","a")
    
    b = [["","",""],["","",""],["","",""]]
    b[2][0]= r & 256 == 256 #9  0
    b[0][2]= r & 128 == 128 #8  0
    b[2][2]= r & 64 == 64   #7  0
    b[1][2] = r & 32 == 32  #6  1
    b[2][1]= r & 16 == 16   #5  0
    b[0][0] = r & 8 == 8    #4  0
    b[0][1] = r & 4 == 4    #3  1
    b[1][0] = r & 2 == 2    #2  0
    b[1][1] = r & 1 == 1    #1  1

    resp = '{'
    for i in range(3):
        for j in range(3):
            if b[i][j]:
                resp += "("+ str(i) + "," + str(j) +")"
    resp += '}'
    ref_arquivo.write(resp)
    ref_arquivo.write(" "+c)
    ref_arquivo.write("\n")

resp = {}
for r in range(512):
    if resp.get(r) == None:
        resp[r] = classifica(r)
    
imprime_relacoes(resp)