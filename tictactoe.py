#97281 Allan Donizette Cravid Fernandes

# Definição de Constantes

DIM_TABULEIRO = (3,3) # dimensao do tabuleiro 3 x 3
VALORES_TABULEIRO = (-1,0,1) # valores aceites pelo tabuleiro
POSICOES_TABULEIRO = (1,2,3,4,5,6,7,8,9) # posicoes disponiveis
COLUNAS = (1,2,3) # 3 colunas
COLUNAS_IND = (0,1,2) # indice das colunas
DIAGONAL = (1,2) # duas diagonais 
# posicoes pela sua representacao interna
POSICOES_INTERNAMENTE = ((1,2,3),(4,5,6),(7,8,9)) 
JOGADORES = (1,-1) # os jogadores
GANHADOR_O = (-1,-1,-1)  
GANHADOR_X = (1,1,1)
EMPATE = (0,0,0)
ESTRATEGIA = ('basico','normal','perfeito') # estrategias de jogo
# posicoes de 1 a 9, indexadas pelo seu indice 
POSICOES_INDEXADAS = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
CANTOS = (1,3,7,9) # os cantos do tabuleiro
LATERAIS = (2,4,6,8) # as laterais 
VISUAL = ('X','O','EMPATE') # passagem da estrutura interna para o exterior 
VENCEDOR_X = [(0,1,1),(1,0,1),(1,1,0)] # vitoria para 1 
VENCEDOR_O = [(-1,-1,0),(-1,0,-1),(0,-1,-1)] # vitoria para -1 
VENCEDOR = [3,-3] # valores de soma quando se ganha o jogo 

# bifurcacacao e bloqueio de bifurcacao
BIFURCACAO_X = [(1,0,0),(0,1,0),(0,0,1)] 
BIFURCACAO_O = [(-1,0,0),(0,-1,0),(0,0,-1)]
TIPO_ASSOCIADO = ['BIFURCACAO','BLOQUEIO_BIFURCACAO']

#------------------------------------------------------------------------------

#Funções auxiliares
        

def tuplo_tab(tab):
    # tuplo_tab: tuplo -> booleano
    """ Funcao auxiliar que recebe um tuplo e verifica se os seus elementos 
    sao todos tuplos e de dimensao 3 """
    for el in tab:
        if not isinstance(el,tuple) or len(el) != DIM_TABULEIRO[0]:
            return False
    return True



def tabuleiro_interna(tab):
    # tabuleiro_interna: tuplo -> booleano
    """Funcao auxiliar que recebe um tuplo de tuplos e verifica se os elementos
    dos tuplos mais  internos sao todos inteiros e que possuem unicamente
    valores de -1,0 ou 1"""
    for linha in range(DIM_TABULEIRO[0]):
        for el in tab[linha]:
            if type(el) is not int or el not in VALORES_TABULEIRO:
                return False
    return True
       


def verifica_tabuleiro(tab,inteiro):
    # verifica_tabuleiro: tabuleiro x inteiro -> booleano
    """ Funcao auxiliar que faz a verificacao das linhas e das colunas do 
    tabuleiro """
    # numero de colunas == numero de linhas, 3x3
    # 3 linhas e 3 colunas com valores 1, 2 ou 3
    if not eh_tabuleiro(tab) or type(inteiro) is not int\
        or inteiro > COLUNAS[2] or inteiro not in COLUNAS:   
        return False
    else: 
        return True


def r_visual(inteiro):
    # r_visual: inteiro -> cad. carateres
    """Funcao auxiliar que recebe um inteiro e devolve a sua representacao
    'para os nossos olhos' """
    if inteiro == 1:
        return 'X'
    elif inteiro == -1:
        return 'O'
    else:
        return ' '
#------------------------------------------------------------------------------


def eh_tabuleiro(tab):
    
    # eh_tabuleiro: universal -> booleano    
    """Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu 
    argumento corresponde a um tabuleiro e False caso contrario,sem nunca gerar 
    erros. """
    if not isinstance(tab,tuple): # verifica se e um tuplo 
        return False
    else:
        tamanho = len(tab)
        if tamanho != DIM_TABULEIRO[0]: # verifica se o tabuleiro respeita 
            #o tamanho correto
            return False

    return (tuplo_tab(tab) and tabuleiro_interna(tab))


 
def eh_posicao(pos):
    # eh_posicao: universal ->booleano 
    """ Esta funcao recebe um argumento de qualquer tipo e devolve True se o
    seus
     argumento corresponde a uma posicao e False caso contrario, sem nunca gerar 
     erros."""
    if type(pos) is not int or pos not in POSICOES_TABULEIRO:
        return False
    return True




def obter_coluna(tab,inteiro):
    # obter_coluna: tabuleiro x inteiro -> vector
    """ Esta funcao recebe um tabuleiro e um inteiro com valor de 1 a 3 que
     representa o numero da coluna, e devolve um vector com os valores dessa 
     coluna. Se algum dos argumentos dados forem invalidos , a funcao deve
    gerar um erro com a mensagem 
    'obter coluna: algum dos argumentos e invalido'."""
    if not verifica_tabuleiro(tab,inteiro):
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    else:
        return (tab[0][inteiro-1],tab[1][inteiro-1],tab[2][inteiro-1])




def obter_linha(tab,inteiro):
    # obter_linha: tabuleiro x inteiro -> vector 
    """Esta funcao recebe um tabuleiro e um inteiro com valor de 1 a 3
    que representa o numero da linha, e devolve um vector com os valores 
    dessa linha.Se algum dos argumentos dados forem invalidos, a funcao deve 
    gerar um erro com a mensagem 'obter linha: algum
    dos argumentos e invalido'. """
    if not verifica_tabuleiro(tab,inteiro):
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    else:
        return (tab[inteiro-1][0],tab[inteiro-1][1],tab[inteiro-1][2])



# obter_diagonal: tabuleiro x inteiro -> vector
def obter_diagonal(tab,inteiro):

    """Esta funcao recebe um tabuleiro e um inteiro que representa a direccao 
    da diagonal, 1 para descendente da esquerda para a direita e 2 para
    ascendente da esquerda para a direita, e devolve um vector com os valores
    dessa diagonal.Se algum dos argumentos dados forem invalidos, a funcao 
    deve gerar um erro com a mensagem 'obter diagonal: algum dos argumentos 
    e invalido '."""
    if(type(inteiro) is not int or not eh_tabuleiro(tab)
       or inteiro not in DIAGONAL or inteiro > DIAGONAL[1]
      ): 
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    else:
        if inteiro == DIAGONAL[0]:
            return (tab[0][0],tab[1][1],tab[2][2])
        else:
            return (tab[2][0],tab[1][1],tab[0][2])




def tabuleiro_str(tab):
    #  tabuleiro str: tabuleiro -> cad. carateres
    """Esta funcao recebe um tabuleiro e devolve a cadeia de caracteres que
    o representa (a representacao externa ou representacao "para os nossos 
    olhos"). Se o argumento dado for invalido, a funcao deve gerar um erro com 
    a mensagem 'tabuleiro str: o argumento e invalido'."""
    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_str: o argumento e invalido')
    else:
        # desdobra o tabuleiro nas suas diversas componentes,posicoes
        # o tabuleiro possui 9 posicoes, de 1 a 9, ou seja , p1 a p9
        ((p1,p2,p3),(p4,p5,p6),(p7,p8,p9)) = tab
        # devolve a cadeia de caracteres, tendo em atencao as proporcoes 
        # fornecidas 
        return \
                str(' '+r_visual(p1)+' '+'|'+' '+r_visual(p2)+' '+'|'+' '+\
                    r_visual(p3))+' '+'\n-----------\n'\
               + str(' '+r_visual(p4)+' '+'|'+' '+r_visual(p5)+' '+'|'+' '+\
                     r_visual(p6))+' '+'\n-----------\n'\
               + str(' '+r_visual(p7)+' '+'|'+' '+r_visual(p8)+' '+'|'+' '+\
                     r_visual(p9)+' ')


#------------------------------------------------------------------------------
#Funções de manipulação do tabuleiro   
def obter_posicao(tab):
    """Funcao auxiliar que recebe um tabuleiro e devolve a disposicao das 
    suas posicoes de 1 a 9"""
    # obter_posicao: tabuleiro -> vector
    tab = POSICOES_INTERNAMENTE
    return tab



def manipulacao_interna(tab):
    # manipulacao_interna: tabuleiro -> lista 
    """Funcao auxiliar que recebe um tabuleiro e devolve uma lista que contem 
    todas as suas linhas,colunas e diagonais"""
    res = [obter_linha(tab,COLUNAS[0]),obter_linha(tab,COLUNAS[1]),
           obter_linha(tab,COLUNAS[2]),obter_coluna(tab,COLUNAS[0]),
           obter_coluna(tab,COLUNAS[1]),obter_coluna(tab,COLUNAS[2]),
           obter_diagonal(tab,DIAGONAL[0]),obter_diagonal(tab,DIAGONAL[1])
          ]
    return res 

    


def obter_indice(pos):
    # obter_indice:posicao -> tuplo
    """Funcao auxiliar que recebe uma posicao 
    e devolve um tuplo (linha,coluna) que identifica a posicao
    internamente no tabuleiro"""
    posicao = POSICOES_INDEXADAS
    return posicao[pos-1]




def linhas_mudanca(tab,tuplo,indice):
    # linhas_mudanca: tabuleiro x tuplo x inteiro -> tuplo 
    """Funcao auxiliar que recebe um tabuleiro, um tuplo e um inteiro 
    e devolve um tabuleiro no qual o elemento no indice inteiro e substituido 
    pelo tuplo"""
    
    linhas = [obter_linha(tab,COLUNAS[0]),obter_linha(tab,COLUNAS[1])\
                  ,obter_linha(tab,COLUNAS[2])]
    linhas[indice] = tuplo
    return tuple(linhas)
        


def eh_posicao_livre(tab,pos):
    # eh_posicao_livre: tabuleiro x posicao -> booleano
    """Esta funcao recebe um tabuleiro e uma posicao, e devolve True se a 
    posicao corresponde a uma posicao livre do tabuleiro e False caso contrario. 
    Se algum dos argumentos dado for invalido, a funcao deve gerar um erro com a 
    mensagem 'eh posicao livre: algum dos argumentos e invalido'."""
    if not eh_tabuleiro(tab) or not eh_posicao(pos) :
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
        
    else:
        # se a posicao dada estiver entre [1,3]  encontra se na primeira linha
        if 1 <= pos <= 3: # pos -1 remove o offset do comeco do indice a 0
            return (tab[0][pos-1] == VALORES_TABULEIRO[1])
        
        elif 4 <= pos <= 6: # entre [4,6] corresponde a segunda linha
            return (tab[1][pos-4] == VALORES_TABULEIRO[1])# pos - 4 remove o 
        # offset do comeco do indice a 0
        else:
            # [7,9] corresponde a terceira e ultima linha
            # pos - 7 remove o offset do comeco do indice a 0
            return (tab[2][pos-7] == VALORES_TABULEIRO[1])




def obter_posicoes_livres(tab):
    # obter_posicoes_livres: tabuleiro -> vector
    """Esta funcao recebe um tabuleiro, e devolve o vector ordenado com todas
    as posicoes livres do tabuleiro. Se o argumento dado for invalido,a funcao 
    deve gerar um erro com a mensagem 'obter posicoes livres: o argumento e 
    invalido'."""
    if not eh_tabuleiro(tab):
        raise ValueError('obter_posicoes_livres: o argumento e invalido')
    else:
        res = ()
        for linha in range(DIM_TABULEIRO[0]):
            for el in range(DIM_TABULEIRO[0]):
                posicoes = obter_posicao(tab)
                if eh_posicao_livre(tab,posicoes[linha][el]):
                    res  += (posicoes[linha][el],)
          
        return res




def jogador_ganhador(tab):
    # jogador_ganhador: tabuleiro -> inteiro
    """Esta funcao recebe um tabuleiro, e devolve um valor inteiro a indicar
    o jogador que ganhou a partida no tabuleiro passado por argumento, sendo o 
    valor igual a 1 se ganhou o jogador que joga com 'X', -1 se ganhou o jogador
    que joga com 'O', ou 0 se nao ganhou nenhum jogador. Se o argumento dado for
    invalido, a funcao deve gerar um erro com a mensagem 'jogador_ganhador: o 
    argumento e invalido'."""
    if not eh_tabuleiro(tab):
        raise ValueError('jogador_ganhador: o argumento e invalido')
    else:
        # obtem todas as linhas,colunas e diagonais que formam o tabuleiro
        linhas_colunas_diagonais = manipulacao_interna(tab)
        if GANHADOR_X in linhas_colunas_diagonais:
            return 1
        if GANHADOR_O in linhas_colunas_diagonais:
            return -1
        if EMPATE in linhas_colunas_diagonais or \
           obter_posicoes_livres(tab) == ():
            return 0




def marcar_posicao(tab,inteiro,pos):
    # marcar_posicao: tabuleiro x inteiro x posicao -> tabuleiro 
    """Esta funcao recebe um tabuleiro, um inteiro identificando um jogador 
(1 para o jogador 'X' ou -1 para o jogador 'O') e uma posicao livre, 
e devolve um novo tabuleiro modificado com uma nova marca do jogador 
nessa posicao. Se algum dos argumentos dados forem invalidos,
a funcao deve gerar um erro com a mensagem 'marcar posicao: algum dos
argumentos e invalido'."""
    try:
        if not eh_posicao_livre(tab,pos):
            raise
    except Exception:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    
    if type(inteiro) is not int or inteiro not in JOGADORES:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    else:
        indice_linha,indice_elemento = obter_indice(pos)      
        if indice_elemento == EMPATE[0]:
            res = ((inteiro,)+tab[indice_linha][indice_elemento+1:])
        if indice_elemento == POSICOES_TABULEIRO[0]:
            res = (tab[indice_linha][:indice_elemento]+(inteiro,)\
                   +tab[indice_linha][indice_elemento+1:])
        if indice_elemento == POSICOES_TABULEIRO[1]:
            res = (tab[indice_linha][:indice_elemento]+(inteiro,))
            
        return linhas_mudanca(tab,res,indice_linha)
    

#------------------------------------------------------------------------------
#Funções de jogo     
def obter_linha_pos(tab,inteiro):
    # obter_linha_pos: tabuleiro de posicoes x inteiro -> vector 
    """ Esta funcao recebe um tabuleiro de posicoes e um inteiro com valor de
    1 a 3 que representa o numero da linha, e devolve um vector com as posicoes
    da linha (esta funcao nao verifica a validade dos argumentos recebidos)"""    
    return (tab[inteiro-1][0],tab[inteiro-1][1],tab[inteiro-1][2])



def obter_coluna_pos(tab,inteiro):
    # obter_coluna_pos: tabuleiro de posicoes x inteiro -> vector
    """ Esta funcao recebe um tabuleiro de posicoes  e um inteiro com valor de
    1 a 3 que representa o numero da coluna, e devolve um vector com as posicoes
    da coluna (esta funcao nao verifica a validade dos argumentos recebidos)"""
    return (tab[0][inteiro-1],tab[1][inteiro-1],tab[2][inteiro-1])



def obter_diagonal_pos(tab,inteiro): 
    # obter_coluna_pos: tabuleiro de posicoes x inteiro -> vector
    """Esta funcao recebe um tabuleiro de posicoes e um inteiro que representa 
    a diagonal e devolve um tuplo de posicoes da diagonal
    (esta funcao nao verifica a validade dos argumentos recebidos)"""
    if inteiro == DIAGONAL[0]:
        return (tab[0][0],tab[1][1],tab[2][2])
    else:
        return (tab[2][0],tab[1][1],tab[0][2])

    

def posicao_correta(tab,tuplo):
    # posicao_correta: tabuleiro x linha,coluna ou diagonal -> posicao livre
    """Esta funcao recebe um tabuleiro e uma linha, coluna ou diagonal 
    e devolve a primeira posicao livre que encontrar"""
    for pos in tuplo:
        if eh_posicao_livre(tab,pos):
            return pos     
               


def vencedor(lista_interna):
    # vencedor: lista -> cad. carateres  
    """Funcao auxiliar que recebe um tabuleiro e devolve a representacao visual 
    do jogador vencedor"""
    # lista interna corresponde a uma lista de todas as filas de um tabuleiro
    for el in range(len(lista_interna)):
        if sum(list(lista_interna[el])) == VENCEDOR[0]:
            return 'X'
        if sum(list(lista_interna[el])) == VENCEDOR[1]:
                return 'O'


          
def vitoria_jogador_bloqueio(tab,inteiro,estado_jogo,soma):
    # vitoria_jogador_bloqueio: tabuleiro x inteiro x lista x inteiro -> posicao 
    """Funcao auxiliar que recebe um tabuleiro,um inteiro,uma lista, e um 
    inteiro e devolve uma posicao"""
    for el in range(len(estado_jogo)):
            if sum(list(estado_jogo[el])) == soma:
                posicoes = obter_posicao(tab)
                if el in range(0,3): # linhas 1,2,3
                    # tuplo de posicoes dos elementos da linha 
                    linha = posicoes[el]
                    return posicao_correta(tab,linha)
                if el in range(3,6): # colunas 1,2,3
                    ind_coluna = el - 2 # indice das colunas 
                    pos = \
                        obter_coluna_pos(obter_posicao(tab),ind_coluna)
                    return posicao_correta(tab,pos)
                
                if el in range(6,8): # diagonais 1,2
                    ind_diagonal = el - 5 # obtem se o numero da diagonal 
                    diagonal = \
                         obter_diagonal_pos(obter_posicao(tab),ind_diagonal)
                    return posicao_correta(tab,diagonal)   
                

#------------------------------------------------------------------------------
#Funções auxiliares associadas a bifurcação e ao seu bloqueio                
def agrupa_por_chaves(lista):
    # agrupa_por_chaves: lista -> dicionario
    """Funcao auxiliar  que recebe uma lista de pares, contendo uma chave e um
    valor, (k, v), representados por tuplos de dois elementos, devolve um 
    dicionario que a cada chave k associa a lista com os
     valores v para essa chave encontrados na lista que e seu argumento."""
    res = {}
    for el in lista:
        if el[0] not in res:
            res[el[0]] = [el[1]]
        else:
            res[el[0]] = res[el[0]] + [el[1]]
    return res



def bifurcacao_filas(tab,estado_jogo,inteiro):
    #bifurcacao_filas: tabuleiro x lista x inteiro -> dicionario
    """Esta funcao recebe um tabuleiro, uma lista, um inteiro e
    devolve um dicionario que contem as linhas,colunas e diagonais que se 
    encontram em possivel situacao de bifurcacao"""
    
    if inteiro == JOGADORES[0]: # peca 1
        res = []
        res_linha = [('linha',el+1)  for el in range(0,3) if sum(estado_jogo[el]) == 1 \
         and(estado_jogo[el][0]*estado_jogo[el][1]) == 0]

        res_coluna =  [ ('coluna',el-2)  for el in range(3,6) if sum(estado_jogo[el]) == 1\ 
        and(estado_jogo[el][0]*estado_jogo[el][1]) == 0]

        res_diagonal = [ ('diagonal',el-5)  for el in range(6,8) if sum(estado_jogo[el]) == 1\
        and(estado_jogo[el][0]*estado_jogo[el][1]) == 0]

        res += res_linha + res_coluna + res_diagonal
        
    if inteiro == JOGADORES[1]: # peca -1
        res = []
        res_linha = [ ('linha',el+1)  for el in range(0,3) if sum(estado_jogo[el]) == -1\
        and (estado_jogo[el][0]*estado_jogo[el][1]) == 0]

        res_coluna =  [ ('coluna',el-2)  for el in range(3,6) if sum(estado_jogo[el]) == -1\
        and (estado_jogo[el][0]*estado_jogo[el][1]) == 0]

        res_diagonal = [ ('diagonal',el-5)  for el in range(6,8)if sum(estado_jogo[el]) == -1\ 
        and (estado_jogo[el][0]*estado_jogo[el][1])== 0]

        res += res_linha + res_coluna + res_diagonal        
        
    return agrupa_por_chaves(res) 



def bifurcacao_dois_em_linha(inteiro,tab,posicoes_intersecao):
    # bifurcacao_dois_em_linha: inteiro x tabuleiro x tuplo de posicoes -> posicao
    """Funcao auxiliar que recebe um inteiro,um tabuleiro e um conjunto de 
    posicoes de intersecao e devolve uma posicao,responsavel pelo dois em  linha 
    do bloqueio de bifurcacao"""
    # dois em linha, no qual o oponente nao tem possibilidades de
    # criar bifurcacao
    if inteiro ==  JOGADORES[0]:
        marcar = JOGADORES[1]
    else:
        marcar = JOGADORES[0]
    estado_jogo = manipulacao_interna(tab)
    posicoes_livres = obter_posicoes_livres(tab)
    res = ()
    for pos in range(len(posicoes_livres)):
        if posicoes_livres[pos] not in posicoes_intersecao:
            res += (posicoes_livres[pos],)
    tabu = ()
    tabu += tab
    tabu = marcar_posicao(tabu,marcar,min(res))
    # verifica se ha mais do que uma bifurcacao
    if  len(bifurcacao_filas(tabu,estado_jogo,inteiro)) == 2:
        res = []
        for pos in range(len(posicoes_livres)):
            if posicoes_livres[pos] not in posicoes_intersecao:
                res += [posicoes_livres[pos],]
        return min(res,default='EMPTY')                        
       
    else:
        res = {}
        for el in res:
            if res[el] > 1 and eh_posicao_livre(tab,el):
                posicoes_intersecao += (el,)
        return(min(posicoes_intersecao))            
        
    

# -> posicao livre
def bifurcacao_intersecao(filas,tab,inteiro,tipo_associado):
    #bifurcacao_intersecao: filas x tabuleiro x inteiro x cad. carateres 
    # -> posicao livre
    """Esta funcao recebe uma fila(dicionario), um tabuleiro,um inteiro 
    e uma cadeira de carateres e devolve a menor posicao livre(bifurcacao) 
    que resulta das diversas intersecoes entre linhas,colunas e diagonais
    ,no caso da bloqueio e devolvido a menor posicao livre ou a menor posicao 
    que respeita o principio de dois em linha e que evita a criacao de 
    bifurcacoes por parte do adversario
        """
    # tipo associado, ou seja, bifurcacao ou o seu bloqueio
    if tipo_associado in TIPO_ASSOCIADO:
        
        posicoes = obter_posicao(tab)
        interseta = ()
        for el in filas:
            if el == 'linha':
                linha = filas[el]
                # linha de posicoes
                for pos in linha:
                    posicoes_linhas = obter_linha_pos(posicoes,pos)
                    interseta += (posicoes_linhas,)

            if el == 'coluna':
                coluna = filas[el]
                # coluna de posicoes
                for pos in coluna:
                    posicoes_coluna = obter_coluna_pos(posicoes,pos) 
                    interseta += (posicoes_coluna,)
                    
            if el == 'diagonal':
                diagonal = filas[el]
                # diagonal de posicoes
                for pos in diagonal:
                    posicoes_diagonal = obter_diagonal_pos(posicoes,pos)
                    interseta += (posicoes_diagonal,)                    
         
        # Permite saber a incidencia das diversas posicoes  
        res = {}
        for pos in range(len(interseta)):
            for el in interseta[pos]:
                if el not in res:
                    res[el] = 1
                else:
                    res[el] += 1
        
        #  Permite obter a intersecoes livres 
        posicoes_intersecao = ()
        for el in res:
            if res[el] > 1 and eh_posicao_livre(tab,el):
                posicoes_intersecao += (el,)
    
    
        if posicoes_intersecao == ():
            return 'EMPTY'
        if tipo_associado == TIPO_ASSOCIADO[0]: # bifurcacao
            return min(posicoes_intersecao,default='EMPTY')
        
        else: # trata se de bloqueio de bifurcacao
            if len(posicoes_intersecao) == POSICOES_TABULEIRO[0]: # 1
                return min(posicoes_intersecao,default='EMPTY')
            else:
                return bifurcacao_dois_em_linha(inteiro,tab,posicoes_intersecao)
               
                 
                
def jogo_galo_empate(tab,posicoes_livres):
    # jogo_galo_empate:  tabuleiro x inteiro(numero de posicoes livres) -> 
    # cad. carateres   
    if obter_posicoes_livres(tab) == () and jogador_ganhador(tab) == 0 and\
    (posicoes_livres == 1 or posicoes_livres == 0):
        return 'EMPATE'      


#------------------------------------------------------------------------------
#Funções principais 
def vitoria(tab,inteiro):
    # vitoria: tabuleiro x jogador(inteiro) -> posicao
    """Esta funcao recebe um tabuleiro e um jogador (inteiro) e verifica se 
    o jogador possui duas das suas pecas em linha e uma posicao livre e 
    devolve a posicao a ser marcada(ganhando o jogo)"""
    # linhas,colunas e diagonais do tabuleiro por ordem de aparecimento
    estado_jogo = manipulacao_interna(tab)  
    if inteiro == JOGADORES[0]:  # peca 1
        soma = sum(VENCEDOR_X[0]) 
        return vitoria_jogador_bloqueio(tab,inteiro,estado_jogo,soma)
    else: # peca -1
        soma = sum(VENCEDOR_O[0])
        return vitoria_jogador_bloqueio(tab,inteiro,estado_jogo,soma)
 


def bloqueio(tab,inteiro):
    # bloqueio: tabuleiro x inteiro ->  posicao 
    """Esta funcao recebe um tabuleiro e um jogaodor(inteiro) e verifica se o 
    jogador adversario possui duas das suas pecas em linha e uma posicao livre 
    e devolve a posicao a ser marcada(ganhando o jogo)"""    
    estado_jogo = manipulacao_interna(tab)  
    if inteiro == JOGADORES[0]:  # peca 1
        adversario = JOGADORES[1]
        soma = sum(VENCEDOR_O[0]) 
        return vitoria_jogador_bloqueio(tab,adversario,estado_jogo,soma)
    else: # peca -1
        adversario = JOGADORES[0]
        soma = sum(VENCEDOR_X[0])
        return vitoria_jogador_bloqueio(tab,adversario,estado_jogo,soma)   


                       
 
def bifurcacao(tab,inteiro):
    # bifurcacao: tabuleiro x jogador (inteiro) -> posicao  
    """Esta funcao recebe um tabuleiro e um jogador(inteiro) e verifica se o 
    jogador tem duas filas que se intersetam, onde cada uma contem as suas pecas
     ,caso a posicao de intersecao esteja livre, ela e devolvida,posteriormente
     marcada de forma a criar duas formas de vencer na jogada seguinte"""     
    
    # todas as filas do tabuleiro
    estado_jogo = manipulacao_interna(tab)
    # atribuicao de uma categoria a funcao 
    # trata-se de uma 'BIFURCACAO'
    tipo_associado = TIPO_ASSOCIADO[0] 
    if inteiro == JOGADORES[0]: # peca 1
            return (bifurcacao_intersecao(bifurcacao_filas(tab,estado_jogo,inteiro),
                    tab,inteiro,tipo_associado)
                    )             
    else: # peca -1 
        return (bifurcacao_intersecao(bifurcacao_filas(tab,estado_jogo,inteiro)
                ,tab,inteiro,tipo_associado)
                )               



  
def bloqueio_de_bifurcacao(tab,inteiro):
    # bloqueio_de_bifurcacao: tabuleiro x jogador (inteiro) -> posicao 
    """Esta funcao recebe um tabuleiro e um jogador(inteiro) e devolve uma 
    posicao, esta resulta de verificar que jogador adversario possui apenas 
    uma bifurcacao,o jogador deve bloquear a bifurcacao(escolher a posicao 
    livre da intersecao) senao o jogador deve criar um dois em linha para forcar 
    o oponente a defender)"""     
    
    estado_jogo = manipulacao_interna(tab)
    # atribuicao de uma categoria a funcao 
    # trata-se de um 'BLOQUEIO_DE_BIFURCACAO'
    tipo_associado = TIPO_ASSOCIADO[1]
    if inteiro == JOGADORES[0]:  # peca 1
        adversario = JOGADORES[1]
        return (bifurcacao_intersecao(bifurcacao_filas(tab,estado_jogo,adversario,)
                ,tab,adversario,tipo_associado)
                )         
    else: # peca -1
        adversario = JOGADORES[0] 
        return (bifurcacao_intersecao(bifurcacao_filas(tab,estado_jogo,adversario),
                tab,adversario,tipo_associado)
                )    
       


def vazio(tab,conj_pos):
    # vazio: tabuleiro x conjunto de posicoes -> inteiro
    """Funcao que recebe um tabuleiro e um conjunto de posicoes
    e devolve a posicao do primeiro elemento do conjunto de posicoes que seja 
    0 caso esta exista"""    
    for el in conj_pos:
        linha,coluna = obter_indice(el)
        if tab[linha][coluna] == VALORES_TABULEIRO[1]:
            return el  # devolve o canto vazio
    


def canto_vazio(tab):
    # canto_vazio: tabuleiro -> inteiro
    """Funcao que recebe um tabuleiro e devolve a posicao do primeiro
    canto vazio caso este exista"""
    return vazio(tab,CANTOS)




def lateral_vazio(tab):
    # lateral_vazio: tabuleiro -> inteiro
    """Funcao que recebe um tabuleiro e devolve a posicao do primeiro
    lateral vazio caso este exista"""
    return vazio(tab,LATERAIS)

    

def oposto_posicao(tab,adversario):
    # oposto_posicao: tabuleiro x adversario(inteiro) -> posicao
    """Funcao auxiliar que recebe um tabuleiro e um inteiro 
    e devolve uma posicao,sendo esta uma posicao oposta"""
    linha,coluna = obter_indice(POSICOES_TABULEIRO[0])
    if tab[linha][coluna] == adversario and eh_posicao_livre(tab,\
        POSICOES_TABULEIRO[8]):
        return POSICOES_TABULEIRO[8]
    linha,coluna = obter_indice(POSICOES_TABULEIRO[2])
    if tab[linha][coluna] == adversario and eh_posicao_livre(tab,\
        POSICOES_TABULEIRO[6]):
        return POSICOES_TABULEIRO[6]
    linha,coluna = obter_indice(POSICOES_TABULEIRO[6])
    if tab[linha][coluna] == adversario and eh_posicao_livre(tab,\
            POSICOES_TABULEIRO[2]):
        return POSICOES_TABULEIRO[2]
    linha,coluna = obter_indice(POSICOES_TABULEIRO[8])
    if tab[linha][coluna] == adversario and eh_posicao_livre(tab,\
            POSICOES_TABULEIRO[0]):
        return POSICOES_TABULEIRO[0]                  



def canto_oposto(tab,inteiro):
    # canto_oposto: tbauleiro x inteiro -> posicao
    """Funcao que recebe um tabuleiro e um inteiro correspondente a
    peca do jogador e verifica se o adversario encontra se num canto 
    e se o canto oposto a peca inimiga encontra se vazia e devolve a posicao 
    oposta vazia,caso esta exista"""
    if inteiro == JOGADORES[0]:  # peca for 1
        adversario = JOGADORES[1] # inimigo -1
        return oposto_posicao(tab,adversario)
    else:
        adversario = JOGADORES[0] # inimigo 1
        return oposto_posicao(tab,adversario)

        

def basico(tab,inteiro):
    # basico: tabuleiro x inteiro -> posicao
    """Funcao que recebe um tabuleiro e um inteiro correspondente a peca do 
    jogador e devolve uma posicao resultante da estrategia 'basico' """
    if eh_posicao_livre(tab,POSICOES_TABULEIRO[4]): # 5
        tab = marcar_posicao(tab,inteiro,POSICOES_TABULEIRO[4])
        return POSICOES_TABULEIRO[4]
    if canto_vazio(tab) in CANTOS: # 7
        posicao = canto_vazio(tab)
        tab = marcar_posicao(tab,inteiro,canto_vazio(tab))
        return posicao
    if lateral_vazio(tab) in LATERAIS: # 8
        posicao = lateral_vazio(tab)
        tab = marcar_posicao(tab,inteiro,lateral_vazio(tab))
        return posicao    



def normal(tab,inteiro):
    # normal: tabuleiro x inteiro -> posicao 
    """Funcao que recebe um tabuleiro e um inteiro correspondente a peca do 
    jogador e devolve uma posicao resultante da estrategia 'normal' """""
    if vitoria(tab,inteiro) in POSICOES_TABULEIRO: # 1
        posicao = vitoria(tab,inteiro)
        tab = marcar_posicao(tab,inteiro,posicao)
        return posicao
    if bloqueio(tab,inteiro) in POSICOES_TABULEIRO: # 2
        posicao = bloqueio(tab,inteiro)
        tab = marcar_posicao(tab,inteiro,posicao)
        return posicao
    if eh_posicao_livre(tab,POSICOES_TABULEIRO[4]): # 5
        tab = marcar_posicao(tab,inteiro,POSICOES_TABULEIRO[4])
        return POSICOES_TABULEIRO[4]
    if canto_oposto(tab,inteiro) in CANTOS: # 6
        posicao = canto_oposto(tab,inteiro)
        tab = marcar_posicao(tab,inteiro,posicao)
        return posicao
    if canto_vazio(tab) in CANTOS: # 7
        posicao = canto_vazio(tab)
        tab = marcar_posicao(tab,inteiro,canto_vazio(tab))
        return posicao
    if lateral_vazio(tab) in LATERAIS: # 8
        posicao = lateral_vazio(tab)
        tab = marcar_posicao(tab,inteiro,lateral_vazio(tab))
        return posicao



def perfeito(tab,inteiro):
    # perfeito: tabuleiro x inteiro -> posicao 
    """Funcao que recebe um tabuleiro e um inteiro correspondente a peca do 
    jogador e devolve uma posicao resultante da estrategia 'perfeito' """""    
    if vitoria(tab,inteiro) in POSICOES_TABULEIRO: # 1
        posicao = vitoria(tab,inteiro)
        tab = marcar_posicao(tab,inteiro,posicao)
        return posicao
    if bloqueio(tab,inteiro) in POSICOES_TABULEIRO: # 2
        posicao = bloqueio(tab,inteiro)
        tab = marcar_posicao(tab,inteiro,posicao)
        return posicao
    if bifurcacao(tab,inteiro) in POSICOES_TABULEIRO: # 3
        posicao = bifurcacao(tab,inteiro)
        tab = marcar_posicao(tab,inteiro,posicao)
        return posicao
    if bloqueio_de_bifurcacao(tab,inteiro) in POSICOES_TABULEIRO: # 4
        posicao = bloqueio_de_bifurcacao(tab,inteiro)
        tab = marcar_posicao(tab,inteiro,posicao)
        return posicao        
    if eh_posicao_livre(tab,POSICOES_TABULEIRO[4]): # 5
        tab = marcar_posicao(tab,inteiro,POSICOES_TABULEIRO[4])
        return POSICOES_TABULEIRO[4]           
    if canto_oposto(tab,inteiro) in CANTOS: # 6
        posicao = canto_oposto(tab,inteiro)
        tab = marcar_posicao(tab,inteiro,posicao)
        return posicao
    if canto_vazio(tab) in CANTOS: # 7
        posicao = canto_vazio(tab)
        tab = marcar_posicao(tab,inteiro,canto_vazio(tab))
        return posicao
    if lateral_vazio(tab) in LATERAIS: # 8
        posicao = lateral_vazio(tab)
        tab = marcar_posicao(tab,inteiro,lateral_vazio(tab))
        return posicao         
#------------------------------------------------------------------------------

def escolher_posicao_manual(tab):
    #  escolher_posicao_manual: tabuleiro -> posicao 
    """Esta funcao realiza a leitura de uma posicao introduzida manualmente
    por um jogador e devolve esta posicao escolhida."""
    if not eh_tabuleiro(tab):
        raise ValueError('escolher_posicao_manual: o argumento e invalido')  
    posicao = eval(input('Turno do jogador. Escolha uma posicao livre: ')) 
    try:
        if not eh_posicao_livre(tab,posicao):
            raise 
    except Exception:
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    return posicao
        


def escolher_posicao_auto(tab,inteiro,cad_carateres):
    # escolher_posicao_auto: tabuleiro x inteiro x cad. carateres -> posicao
    """Esta fundao recebe um tabuleiro, um inteiro identificando um jogador
    (1 para o jogador 'X' ou -1 para o jogador 'O') e uma cadeia de carateres 
    correspondente a estrategia, e devolve a posicao escolhida automaticamente 
    de acordo com a estrategia selecionada"""
    if(not eh_tabuleiro(tab) or type(inteiro) is not int or inteiro not in \
       JOGADORES or cad_carateres not in ESTRATEGIA
       ):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    else:
        # basico
        if cad_carateres == ESTRATEGIA[0]: 
            return basico(tab,inteiro)    
        # normal
        elif cad_carateres == ESTRATEGIA[1]:
            return normal(tab,inteiro)
        # perfeito    
        else: 
            return perfeito(tab,inteiro)
                       


def jogo_do_galo(cad_carateres,cad_caraters):
    # jogo_do_galo: cad. carateres x cad. carateres  -> cad. carateres 
    """Funcao principal que permite jogar um jogo completo de Jogo
do Galo de um jogador contra o computador. O jogo comeca sempre com o jogador
'X' a marcar uma posicao livre e termina quando um dos jogadores vence ou, se 
nao existem posicoes livres no tabuleiro. A funcao recebe duas cadeias de 
caracteres e devolve o identificador do jogador ganhador ('X' ou 'O'). Em caso 
de empate, a funcao deve devolver a cadeia de caracteres 'EMPATE'. O primeiro 
argumento corresponde a marca ('X' ou 'O') que deseja utilizar o jogador humano,
e o segundo argumento selecciona a estrategia de jogo utilizada pela maquina.
"""
    if not cad_carateres in VISUAL or cad_caraters not in ESTRATEGIA:
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    print('Bem-vindo ao JOGO DO GALO.')
    print("O jogador joga com \'{}\'.".format(cad_carateres))
    tab = ((0,0,0),(0,0,0),(0,0,0))
    if cad_carateres == VISUAL[0]:
        posicoes_livres = 9
        while posicoes_livres >= 0:       
            inteiro = JOGADORES[0]
            pos = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab,inteiro,pos)
            print(tabuleiro_str(tab))
            posicoes_livres -= 1               
            if vencedor(manipulacao_interna(tab)) in VISUAL:  
                return vencedor(manipulacao_interna(tab))
            if jogo_galo_empate(tab,posicoes_livres) in VISUAL:
                return jogo_galo_empate(tab,posicoes_livres)            
            print('Turno do computador '+'('+cad_caraters+'):')
            adversario = JOGADORES[-1]
            posicao = escolher_posicao_auto(tab,adversario,cad_caraters)
            tab = marcar_posicao(tab,adversario,posicao)
            print(tabuleiro_str(tab))
            posicoes_livres -= 1 
            if vencedor(manipulacao_interna(tab)) in VISUAL:
                return vencedor(manipulacao_interna(tab))
            if jogo_galo_empate(tab,posicoes_livres) in VISUAL:
                return jogo_galo_empate(tab,posicoes_livres)                              
    else:
        posicoes_livres = 9
        while posicoes_livres >= 0:          
            inteiro = JOGADORES[1]       
            print('Turno do computador '+'('+cad_caraters+'):')
            adversario = JOGADORES[0]
            posicao = escolher_posicao_auto(tab,adversario,cad_caraters)
            tab = marcar_posicao(tab,adversario,posicao)
            print(tabuleiro_str(tab))
            posicoes_livres -= 1 
            if vencedor(manipulacao_interna(tab)) in VISUAL:
                return vencedor(manipulacao_interna(tab))
            if jogo_galo_empate(tab,posicoes_livres) in VISUAL:
                return jogo_galo_empate(tab,posicoes_livres) 
            pos = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab,inteiro,pos)
            print(tabuleiro_str(tab))
            posicoes_livres -= 1               
            if vencedor(manipulacao_interna(tab)) in VISUAL:  
                return vencedor(manipulacao_interna(tab))
            if jogo_galo_empate(tab,posicoes_livres) in VISUAL:
                return jogo_galo_empate(tab,posicoes_livres) 
