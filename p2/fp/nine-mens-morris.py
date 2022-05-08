#97281  Allan Donizette Cravid Fernandes


# Constantes 
LNH = ("1","2","3") # Linhas do tabuleiro
CLN = ("a","b","c") # Colunas do tabuleiro
ID = ("X","O"," ")
NVL = ("facil","normal","dificil") # dificuldade do jogo


#--------------------------------TAD POSICAO----------------------------------                                      
# Representacao interna: dicionario                                          - 
# p.ex {"coluna":a,"linha":1} corresponde a posicao "a1" ---------------------

# Assinatura 

#----------------------------------------
# cria_posicao: str x str -> posicao
# cria_copia_posicao: posicao -> posicao
# obter_pos_c: posicao -> str
# obter_pos_l: posicao -> str
# eh_posicao: universal -> booleano
# posicoes_iguais: posicao x posicao -> booleano
# posicao_para_str: posicao -> str

#----------------------
# Construtores        - 
#----------------------
def cria_posicao(c,l):

    # cria_posicao: str x str -> posicao
    """
    cria_posicao(c,l) recebe duas strings correspondentes a coluna
    c e a linha l de uma posicao e devolve a posicao correspondente.
    """
    if (type(c) is str and type(l) is str and 
     c in ("a","b","c") and l in ("1","2","3")
       ): 
        return {"coluna":c,"linha":l}
    else:
        raise ValueError("cria_posicao: argumentos invalidos")
        
def cria_copia_posicao(p):
    
    # cria_copia_posicao: posicao -> posicao
    """
    cria_copia_posicao(p) recebe uma posicao p e devolve uma copia
    nova da posicao.
    """
    return cria_posicao(p["coluna"],p["linha"])

#----------------------
# Seletores           - 
#----------------------
def obter_pos_c(p):

    # obter_pos_c: posicao -> str
    """
    obter_pos_c(p) devolve a componente coluna c da posicao p.
    """
    return p["coluna"]

def obter_pos_l(p):

    # obter_pos_l: posicao -> str
    """
    obter_pos_l(p) devolve a componente linha l da posicao p.
    """
    return p["linha"]

#----------------------
# Reconhecedor        - 
#----------------------
def eh_posicao(arg):

    # eh_posicao: universal -> booleano
    """
    eh_posicao(arg) devolve True se o argumento corresponde ao TAD
    posicao e False caso contrario.
    """
    return ( isinstance(arg,dict) and len(arg) == 2 and 
        "coluna" in arg and "linha" in arg and 
        isinstance(arg["coluna"],str) and isinstance(arg["linha"],str)
         and arg["coluna"] in CLN and arg["linha"] in LNH 
           )

#----------------------
# Teste               - 
#----------------------
def posicoes_iguais(p1,p2):

    # posicoes_iguais: posicao x posicao -> booleano
    """
    posicoes_iguais(p1,p2) devolve True apenas se p1 e p2 sao posicoes 
    e sao iguais.
    """
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

#----------------------
# Transformador       -
#----------------------            
def posicao_para_str(p):

    # posicao_para_str: posicao -> str
    """
    posicao_para_str(p) devolve a cadeia de carateres "cl" que representa o
    seu argumento,sendo os valores c e l as componentes coluna e linha de p.
    """
    rep_ext = "{}{}".format(obter_pos_c(p),obter_pos_l(p))
    return rep_ext

#-----------------------------------------------------------------------------
# Funcoes de alto nivel TAD POSICAO                                          - 
#-----------------------------------------------------------------------------

#-----------------------
# Funcoes auxiliares   -
#-----------------------
def adjacentes_padrao(p):
    
    # adjacentes_padrao: posicao -> tuplo de posicoes
    """
    adjacentes_padrao(p) devolve um tuplo de posicoes adjacentes padrao
    a posicao p,isto e,todas as posicoes adjacentes nao diagonais a p.
    """
    # adj -> acumulador de posicoes adjacentes 
    # c -> coluna , l -> linha 
    c,l,adj = obter_pos_c(p),obter_pos_l(p),()
    # l_c -> linha cima, l_b linha baixo
    # c_e -> coluna esquerda, c_d -> coluna direita 
    l_c,l_b = chr(ord(l) - 1),chr(ord(l)+1)
    c_e, c_d  = chr(ord(c)-1),chr(ord(c)+1)

    if l_c in LNH: # ordem de leitura,cima
        adj += (cria_posicao(c,l_c),)
    if c_e in CLN:# ordem de leitura esquerda
        adj += (cria_posicao(c_e,l),)
    if c_d in CLN: # ordem de leitura direita
        adj += (cria_posicao(c_d,l),)
    if l_b in LNH: # ordem de leitura baixo
        adj += (cria_posicao(c,l_b),)
    return  adj

def obter_posicoes_adjacentes(p):

    # obter_posicoes_ajdacentes: posicao -> tuplo de posicoes
    """
    obter_posicoes_adjacentes(p) devolve um tuplo com as posicoes adjacentes
    a posicao p de acordo com a ordem de leitura do tabuleiro.
    """
    adjacentes = {("b1","b3","a2","c2"):adjacentes_padrao(p),
                 "b2": tuple([cria_posicao(x,y) for y in ("1","2","3") for x
                 in ("a","b","c") if posicoes_iguais(cria_posicao(x,y),
                 cria_posicao("b","2")) is False 
                  ]),"a1":adjacentes_padrao(p) + (cria_posicao("b","2"),),
                 "c3":(cria_posicao("b","2"),)+adjacentes_padrao(p)
                 }    
    if posicao_para_str(p) in ("b1","b3","a2","c2"):
        return adjacentes[("b1","b3","a2","c2")] # laterais
    elif posicao_para_str(p) in ("b2","c3","a1"): 
        return adjacentes[posicao_para_str(p)] # centro,
    # cantos opostos diagonal \
    else: # cantos opostos diagonal / 
        p_centro = (cria_posicao("b","2"),)
        adj = adjacentes_padrao(p)
        res = adj[:1]+p_centro+adj[1:]
        return res
        
#--------------------------------TAD PECA-------------------------------------   
# Representacao interna: lista                                               -         
# p.ex ["X"]corresponde a peca do jogador X                                  -

# Assinatura 

#----------------------------------------
# cria_peca: str -> peca
# cria_copia_peca: peca -> peca
# eh_peca: universal -> booleano
# pecas_iguais: peca x peca -> booleano
# peca_para_str: peca -> str

#----------------------
# Construtores        - 
#----------------------
def cria_peca(s):

    # cria_peca: str -> peca
    """
    cria_peca(s) recebe uma cadeia de carateres que corresponde ao 
    identificador de um dos jogadores ("X" ou "O") ou uma peca livre (" ") 
    e devolve a peca correspondente.
    """
    if s not in ID:
        raise ValueError("cria_peca: argumento invalido")
    else:
        return [s]

def cria_copia_peca(j):

    # cria_copia_peca: peca -> peca
    """
    cria_copia_peca(j) recebe uma peca e devolve uma copia nova da peca.
    """
    return []+j

#----------------------
# Reconhecedor        - 
#----------------------
def eh_peca(arg):

    # eh_peca: universal -> booleano
    """
    eh_peca(arg) devolve True caso o seu argumento seja um TAD peca e False
    caso contrario.
    """
    return isinstance(arg,list) and len(arg) == 1 and arg[0] in ID

#----------------------
# Teste               - 
#----------------------
def pecas_iguais(j1,j2):

    # pecas_iguais: peca x peca -> booleano
    """
    pecas_iguais(j1, j2) devolve True apenas se j1 e j2 sao pecas e sao iguais.
    """
    return eh_peca(j1) and eh_peca(j2) and j1 == j2

#----------------------
# Transformador       -
#----------------------           
def peca_para_str(j):

    # peca_para_str: peca -> str
    """
    peca_para_str(j) devolve a cadeia de carateres que representa o jogador
    dono da peca,isto e ,"[X]","[O]","[]".
    """
    if j[0] == " ":
        return "[ ]"
    else:
        if j[0] == "X":
            return "[X]"
        else:
            return "[O]"

#-----------------------------------------------------------------------------
# Funcoes de alto nivel __TAD__PECA__                                        - 
#-----------------------------------------------------------------------------
def peca_para_inteiro(j):

    # peca_para_inteiro: peca -> N
    """
    peca_para_inteiro(j) devolve um inteiro valor 1, -1 ou 0, dependendo se a
    peca e do jogador 'X', 'O' ou livre, respetivamente.
    """
    if pecas_iguais(j,cria_peca(" ")):
        return 0
    if pecas_iguais(j,cria_peca("X")):
        return 1
    else: 
        return -1
    
#--------------------------------TAD TABULEIRO--------------------------------
# Representacao interna: dicionario de 3 chaves, "a","b","c" sendo estas as  -
# colunas do tabuleiro,o valor associado a cada chave eh uma lista de 3      -
# elementos                                                                  -           
# p.ex ---- {"a":["X"," "," "],"b":[" ","O"," "],"c":[" "," "," "]}          -
# corresponde a um tabuleiro do jogo do moinho com pecas diferentes          -
# nas posicoes 'a1' e 'b2'                                                   - 

# Assinatura 

#----------------------------------------
# cria_tabuleiro: {} -> tabuleiro
# cria_copia_tabuleiro: tabuleiro -> tabuleiro
# obter_peca: tabuleiro x posicao -> peca
# obter_vetor: tabuleiro x  str -> tuplo de pecas 
# coloca_peca: tabuleiro x peca x posicao -> tabuleiro
# remove: tabuleiro x posicao: -> tabuleiro 
# move_peca: tabuleiro x posicao x posicao -> tabuleiro
# eh_tabuleiro: universal -> booleano
# eh_posicao_livre: tabuleiro x posicoes -> booleano
# tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
# tabuleiro_para_str: tabuleiro -> str
# tuplo_para_tabuleiro: tuplo -> tabuleiro

#----------------------
# Construtores        - 
#----------------------
def cria_tabuleiro():

    #cria_tabuleiro: {} -> tabuleiro
    """
    cria_tabuleiro() devolve um tabuleiro de jogo do moinho de 3x3 sem posicoes 
    ocupadas por pecas de jogador.
    """
    p = cria_peca(" ")
    return {"a":[p]*3,"b":[p]*3,"c":[p]*3}

def cria_copia_tabuleiro(t):

    # cria_copia_tabuleiro: tabuleiro -> tabuleiro
    """
    cria_copia_tabuleiro(t) recebe um tabuleiro e devolve uma copia nova do
    tabuleiro.
    """
    # obtem as colunas "a","b" e "c" do tabuleiro
    c_a,c_b,c_c = [x for x in t["a"]],[x for x in t["b"]],[x for x in t["c"]]
    
    return {"a":c_a,"b":c_b ,"c":c_c}

#----------------------
# Seletores           - 
#----------------------
def obter_peca(t,p):

    # obter_peca: tabuleiro x posicao -> peca
    """
    obter_peca(t,p) devolve a peca na posicao tabuleiro.Se a posicao nao 
    estiver ocupada,devolve uma peca livre.
    """
    c = obter_pos_c(p) # obtem a coluna
    l = int(obter_pos_l(p)) - 1 # obtem a linha,remove o offset de + 1,
    # as linhas comecam em 1

    return t[c][l]

def obter_vetor(t,s):

    # obter_vetor: tabuleiro x  str -> tuplo de pecas 
    """
    obtervetor(t,s) devolve todas as pecas da linha ou coluna 
    especificada pelo seu argumento.
    """
    if s in CLN:
        return tuple(t[s])
    else: # obtem linhas
        res = ()
        l = int(s) - 1
        for c in CLN:
            res += (t[c][l],)
        return res 
    
#----------------------
# Modificadores       - 
#----------------------
def coloca_peca(t,j,p):

    # coloca_peca: tabuleiro x peca x posicao -> tabuleiro
    """
    coloca_peca(t,j,p) modifica destrutivamente o tabuleiro t colocando 
    a peca j na posicao p, e devolve o proprio tabuleiro.
    """
    c = obter_pos_c(p) 
    l = int(obter_pos_l(p)) - 1 
    t[c][l] = j # altera a peca na posicao dada
    return t
    
def remove_peca(t,p):

    # remove: tabuleiro x posicao: -> tabuleiro 
    """
    remove_peca(t,p) modifica destrutivamente o tabuleiro t removendo a peca 
    da posicao p, e devolve o proprio tabuleiro.
    """
    # remover uma peca da posicao p eh o mesmo que colocar na posicao p 
    # uma peca livre -> p_l
    p_l = cria_peca(" ")
    return coloca_peca(t,p_l,p)

def move_peca(t,p1,p2):

    # move_peca: tabuleiro x posicao x posicao -> tabuleiro
    """
    move_peca(t,p1,p2) modifica destrutivamente o tabuleiro t movendo 
    a peca que se encontra na posicao p1 para a posicao p2, e devolve 
    o proprio tabuleiro.
    
    """
    
    # mover uma peca da posicao p1 para a posicao p2 e o mesmo que 
    # colocar a peca da posicao p1 na posicao p2 e remover a peca
    # na posicao p1
    
    j_p1 = obter_peca(t,p1)  
    t_mod = remove_peca(t,p1)
    t = coloca_peca(t_mod,j_p1,p2)
    return t
    
#----------------------
# Reconhecedor        - 
#----------------------

#-----------------------
# Funcoes auxiliares   -
#-----------------------
def transforma(tr, lst):
    
    # transforma: transformacao x lista -> lista 
    """
     transforma(tr,lst), aplica a transformacao tr a todos os elementos
     da lista lst.
     
    """
    res = list()
    for e in lst:
        res = res + [tr(e)]
    return res 

def alisas(t):
    
    # alisas: tuplo -> tuplo
    """
    alisas(t), recebe um tuplo que pode conter outros tuplos e "alisa" os
    tuplos interiores caso existam e devolve unicamente o tuplo exterior 
    com elementos de outros tipos caso estes existam.
    
    """
    i = 0
    while i < len(t):
        if isinstance(t[i],tuple):
            t = t[:i] + t[i] + t[i+1:]
        else:
            i+= 1
    return t

def tabuleiro_valido(arg):
    
    # tabuleiro_valido: tabuleiro(cuja validade e dubia) -> booleano
    """
    tabuleiro_valido(arg), devolve True caso o tabuleiro seja valido,isto e
    pode ter um maximo de 3 pecas de cada jogador, nao pode conter mais de 1
    peca mais de um jogador que do contrario, e apenas pode haver um ganhador
    em simultaneo.
    
    """
    c_1,c_2,c_3  = CLN[0],CLN[1],CLN[2]   
    # todas as CLN do  tabuleiro 
    res = alisas((obter_vetor(arg,c_1),obter_vetor(arg,c_2),
                obter_vetor(arg,c_3),
                ))
    
    # obtem a representacao em inteiros das pecas
    i_pecas = transforma(lambda x: peca_para_inteiro(x),list(res))
    # obtem o numero de vezes que a peca "X" e "O" aparece no tabuleiro
    jg_X,jg_O = i_pecas.count(1),i_pecas.count(-1)
    i_pecas_mod = [abs(el) for el in i_pecas ] # transforma para positivo 
    # cada inteiro das pecas
    # so se pode ter no maximo 3 pecas de cada jogador
    if ((jg_X == jg_O and jg_X != 3) or (jg_X == jg_O and
        pecas_iguais(obter_ganhador(arg),cria_peca(" ")))
       ): # o jogo possui apenas um vencedor,caso este exista
        return True 
    elif (((jg_X == jg_O +1) or (jg_O == jg_X +1)) and
     sum(i_pecas_mod) <= 6 and jg_X <= 3 and jg_O <= 3
         ):
        return True
    else:
        return False 
    
def posicoes_ord_leitura():
    # posicoes_ord_leitura: {} -> lista
    """
    posicoes_ord_leitura() devolve a lista de posicoes do tabuleiro
    por ordem de leitura.
    
    """
    return [cria_posicao(c,l) for l in LNH for c in CLN ]

#-----------------------      
def eh_tabuleiro(arg):

    # eh_tabuleiro: universal -> booleano
    """
    eh_tabuleiro(arg), devolve True caso o seu argumento seja um TAD tabuleiro 
    e False caso contrario. 
    """
    # verifica se as pecas sao validas 
    def pecas_validas(arg):
        
        # peca_validas: universal -> booleano
        """
        pecas_validas(arg) devolve true caso o argumento fornecido
        e constituido por pecas validas.
        
        """
        
        for col in CLN:
            for el in range(3):    
                if not eh_peca(arg[col][el]):
                    return False
        return True
    
    # verifica se corresponde a representacao interna do TAD tabuleiro
    validacoes = (isinstance(arg,dict) and len(arg)== 3 and "a" in arg 
                  and "b" in arg and
                  "c" in arg and isinstance(arg["a"],list) 
                  and isinstance(arg["b"],list) and isinstance(arg["c"],list) 
                  and all(len(i) == 3 for i in [arg["a"],
                  arg["b"],arg["c"]]) and pecas_validas(arg) 
                 )    
    return validacoes and tabuleiro_valido(arg)


def eh_posicao_livre(t,p):
    
        # eh_posicao_livre: tabuleiro x posicoes -> booleano
        """
        eh_posicao_livre(t,p) devolve True apenas no caso da posicao p do
        tabuleiro corresponde a uma posicao livre.
    
        """
        return  pecas_iguais(obter_peca(t,p),cria_peca(" "))

#----------------------
# Teste               - 
#----------------------
def tabuleiros_iguais(t1,t2):

    # tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    """
    tabuleiros_iguais(t1,t2) devolve True apenas se t1 e t2 sao tabuleiros e 
    sao iguais
    """
    return eh_tabuleiro(t1) and eh_tabuleiro(t1) and t1 == t2

#----------------------
# Transformador       -
#---------------------- 
def tabuleiro_para_str(t):

    # tabuleiro_para_str: tabuleiro -> str
    """
    tabuleiro_para_str(t) devolve a cadeia de caracteres que representa o
    tabuleiro.
    """
    # l_1,l_2,l_3 -> linha 1,2,3 respetivamente

    l_1,l_2,l_3 = (obter_vetor(t,"1"),
                  obter_vetor(t,"2"),
                  obter_vetor(t,"3")
                  )
    # obtem a representacao para str das pecas na linha 1
    l_1 = [peca_para_str(peca) for peca in l_1]
    # idem para as restantes
    l_2 = [peca_para_str(peca) for peca in l_2]
    l_3 = [peca_para_str(peca) for peca in l_3]
    
    # separador horizontal,vertical,diagonal 1,diagonal 2,espaco
    sep_h,sep_v,sep_d1,sep_d2,esp = "-","|","\\","/"," "
    # espaco extra, nova linha
    esp_,n_l = esp*3,"\n"
    n_1,n_2,n_3 = "\n1","\n2","\n3"
  
    # obtem os marcadores de posicao
    m_posicao = "{}"*49
    return m_posicao.format(esp_,CLN[0],esp_,CLN[1],esp_,CLN[2],n_1,esp,l_1[0],
          sep_h,l_1[1],sep_h,l_1[2],n_l,esp_,sep_v,esp,sep_d1,esp,sep_v,esp,
          sep_d2,esp,sep_v,n_2,esp,l_2[0],sep_h,l_2[1],sep_h,l_2[2],n_l,esp_,
          sep_v,esp,sep_d2,esp,sep_v,esp,sep_d1,esp,sep_v,n_3,esp,l_3[0],sep_h,
          l_3[1],sep_h,l_3[2])
         
def inteiro_para_peca(n):
    
    # inteiro_para_peca: inteiro -> peca
    """
    inteiro_para_peca(n) devolve a peca correspondente ao inteiro n.
    
    """
    inteiro_peca = {1: cria_peca("X"),-1: cria_peca("O"),0:cria_peca(" ")}
    return inteiro_peca[n]

def tuplo_para_tabuleiro(t):

    # tuplo_para_tabuleiro: tuplo -> tabuleiro
    """
    tuplo_para_tabuleiro(t) devolve o tabuleiro que e representado pelo tuplo t
    com 3 tuplos,cada um deles cada um deles contendo 3 valores inteiros iguais
     a 1, -1 ou 0.
    """
    # obtem as colunas do tuplo
    c_a = [t[x][0] for x in range(3)]
    c_b = [t[x][1] for x in range(3)]
    c_c = [t[x][2] for x in range(3)]

    # converte as colunas do tuplo em colunas de pecas
    CLN = {"a": [inteiro_para_peca(n) for n in c_a],
               "b":[inteiro_para_peca(n) for n in c_b],
               "c":[inteiro_para_peca(n) for n in c_c]
           }
    t = cria_tabuleiro # cria um tabuleiro com pecas livres
    # modifica as colunas do tabuleiro t
    t  = {i:CLN[i] for i in CLN}
    return t
             
#-----------------------------------------------------------------------------
#                  Funcoes de alto nivel __TAD__TABULEIRO__                  - 
#-----------------------------------------------------------------------------
def linha_coluna_inteiro(t):
    
    # linha_coluna_inteiro: tabuleiro -> lista 
    """
    linha_coluna_inteiro() devolve uma lista de todas as colunas e 
    linhas do tabuleiro.
    """
    # obtem todas as colunas e linhas do tabuleiro   
    c_l_tab = [obter_vetor(t,x) for x in CLN]+[obter_vetor(t,y) for y in LNH]
  
    # obtem c_l_tab na sua representacao de inteiros
    c_l = [[peca_para_inteiro(j) for j in c_l_tab[el]] for el in range(6)]
    return c_l

def obter_ganhador(t):
    
        # obter_ganhador: tabuleiro -> peca
        """
        obter_ganhador(t) devolve uma peca do jogador que tenha as suas 3 pecas 
        em linha na vertical ou na horizontal no tabuleiro.Se nao existir 
        nenhum ganhador, devolve uma peca livre.
    
        """
        # obtem as colunas e linhas do tabuleiro em inteiros
        c_l = linha_coluna_inteiro(t)
        
        for el in range(6):
            if sum(c_l[el]) == 3:
                return cria_peca("X")
            if sum(c_l[el]) == -3:
                return cria_peca("O")
        return cria_peca(" ") # caso nao se verifique as condicoes acima,
        #devolve a peca livre        
        
def obter_posicoes_livres(t):
    # obter_posicoes_livres: tabuleiro -> tuplo de posicoes 
    """
    obter_posicoes_livres(t) devolve um tuplo com as posicoes nao ocupadas 
    pelas pecas de qualquer um dos dois jogadores na ordem de leitura do
    tabuleiro.
    
    """
    # obtem as posicoes por ordem de leitura do tabuleiro
    res  = posicoes_ord_leitura()
    # devolve as posicoes livres
    return tuple([p for p in res if eh_posicao_livre(t,p)])
       
def obter_posicoes_jogador(t,j):
    # obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes
    """
    obter_posicoes_jogador(t,j) devolve um tuplo com as posicoes ocupadas 
    pelas pecas j de um dos dois jogadores na ordem de leitura do tabuleiro .
    """
    # obtem as posicoes por ordem de leitura do tabuleiro
    res  =  posicoes_ord_leitura()
    # devolve as posicoes do jogador
    return tuple([p for p in res if pecas_iguais(obter_peca(t,p),j)])   
    
#-----------------------------------------------------------------------------
#                          Funcoes Adicionais                                - 
#-----------------------------------------------------------------------------

#-----------------------
# Funcoes auxiliares   -
#-----------------------
#--------------------------
#  fases de colocacao -
#--------------------------

# 1 
def eh_vitoria(t,j):
    
    # eh_vitoria_bloqueio: tabuleiro x peca -> posicao
    """
    eh_vitoria(t,j) verifica se ha duas pecas em linha e uma posicao
    livre,caso sim retorna a posicao correspondente.
    
    """
    # obtem todas as posicoes livres
    pos_livres = obter_posicoes_livres(t)
    # guarda a posicao caso (linha/ coluna) esteja em dois em linha
    res = tuple([pos for pos in pos_livres if obter_vetor(t,
            obter_pos_l(pos)).count(j)== 2 or obter_vetor(t,
             obter_pos_c(pos)).count(j)==2]
               )
    return "None" if res == () else res[0]

# 2
def bloqueio(t,j):
    
    # bloqueio: tabuleiro x peca -> posicao
    """
    bloqueio(t,j) verifica se a peca oponente possui um dois em linha
    e uma posicao livre,caso sim retorna a posicao correspondente.
    """
    p = peca_para_inteiro(j) # obtem a representacao em inteiro da peca
    # obtem a peca adversaria
    j = inteiro_para_peca(-p)
    return eh_vitoria(t,j)
      
# 3
def centro(t,_1):
    
    # centro: tabuleiro -> posicao
    """
    centro_t(t) verifica se o centro e posicao livre,
    caso sim retorna a posicao correspondente.
    """
    pos = posicoes_ord_leitura()
    c = pos[4]
    return tuple([c if eh_posicao_livre(t,c) else "None"])[0]    

# 4
def canto_vazio(t,_1):
    
    # canto_vazio: tabuleiro -> posicao
    """
    canto_vazio(t) verifica se um canto e posicao livre,
    caso sim retorna a posicao correspondente.
    
    """
    pos = posicoes_ord_leitura()
    # obtem tuplo com os cantos vazios livres 
    canto_v = tuple([ pos[p] for p in (0,2,6,8) if eh_posicao_livre(t,pos[p])])
    return "None" if canto_v == () else canto_v[0]

# 5 
def lateral_vazio(t,_1):
    
    # lateral_vazio: tabuleiro -> tuplo de uma posicao
    """
    lateral_vazio(t) verifica se uma lateral e posicao livre,
    caso sim retorna a posicao correspondente.
    """
    pos = posicoes_ord_leitura()
    lateral_v = tuple([pos[p] if eh_posicao_livre(t,pos[p]) else None
                       for p in (1,3,5,7)])
    return (lateral_v[0],)
    
def coloca_ou_move(t,j):
    
    # coloca_ou_move: tabuleiro x peca -> booleano
    """
    coloca_ou_move(t,j) devolve True se o tabuleiro esta na fase de movimento e 
    False caso esteja na fase de colocao .
    
    """
    res =  posicoes_ord_leitura()  
    p_total = [obter_peca(t,p) for p in res] 
    j_num = p_total.count(j)
    cond = (j_num == 3 and pecas_iguais(obter_ganhador(t),cria_peca(" ")))
    return cond
  
def facil(t,j):
    
    # facil: tabuleiro x peca -> posicao
    """
    facil(t,j) devolve a primeira posicao que satisfaz 
    as acoes/fases do modo facil.
    
    """
    fases = (eh_vitoria,bloqueio,
             centro,canto_vazio,lateral_vazio
            )    
    posicao = ()
    for fase in range(len(fases)):
        if eh_posicao(fases[fase](t,j)):
            posicao += (fases[fase](t,j),)
    return posicao[0]

def movimento_auto_facil(t,j):
    
    # movimento_auto_facil(t,j): tabuleiro x peca ->  tuplo de posicoes
    """
    movimento_auto_facil(t,j) devolve um tuplo de duas posicoes,sendo a
    primeira a origem e a segunda o destino do movimento.
     
    """
    j_pos = obter_posicoes_jogador(t,j)
    res = tuple([tuple([(x,obter_posicoes_adjacentes(x)[y]) for x in j_pos if
            eh_posicao_livre(t,obter_posicoes_adjacentes(x)[y])]) for y in 
           range(3)
              ])
    return (j_pos[0],)*2 if res == ((), (), ()) else (alisas(res)[0],
                                                      alisas(res)[1])
    
def minimax(t,j,depth,tpl):
    
    # minimax: tabuleiro x peca x inteiro x sequencia de movimentos
    #-> tuplo de posicoes
    """
    minimax(t,j,depth,tpl),implementacao do algoritmo minimax que 
    minimiza a possivel perda maxima,devolve um tuplo de posicoes.
    
    """
    if (pecas_iguais(obter_ganhador(t),cria_peca(" ")) is False) or depth == 0: 
        return (peca_para_inteiro(obter_ganhador(t)),tpl)
    else:
        melhor_resultado,melhor_seq_movimentos  = -peca_para_inteiro(j), ()
        for pos in obter_posicoes_jogador(t,j):
            for adj in obter_posicoes_adjacentes(pos):
                if eh_posicao_livre(t,adj): 
                    tab = move_peca(cria_copia_tabuleiro(t),pos,adj)
                    novo_resultado,nova_seq_movimentos = minimax(tab,
                    inteiro_para_peca(melhor_resultado),depth-1,
                     tpl + (pos,adj)
                                                                )
                    if ((melhor_seq_movimentos == ()) 
                        or  (peca_para_inteiro(j) == 1 and 
                        novo_resultado > melhor_resultado) or (
                        peca_para_inteiro(j) == -1 and novo_resultado <
                        melhor_resultado 
                        )):
                        melhor_resultado,melhor_seq_movimentos = ( 
                            novo_resultado,nova_seq_movimentos
                                                                 )                    
        return (melhor_resultado,melhor_seq_movimentos)
    
def obter_movimento_manual(t,j):
    
    # obter_movimento_manual: tabuleiro x peca -> tuplo de posicoes
    """
    obter_movimento_manual(t,j) funcao auxiliar que recebe um tabuleiro e
    uma peca de um jogador,e devolve um tuplo com uma ou duas posicoes que
    representam uma posicao ou um movimento introduzido manualmente pelo 
    jogador.   
    
    """
    res,erro = posicoes_ord_leitura(),"obter_movimento_manual: escolha invalida"
    pos_str,p_ext = [posicao_para_str(p) for p in res],{
        posicao_para_str(res[el]):res[el] for el in range(9)
                                                       }
    men,sa,gem =( "Turno do jogador."," Escolha um movimento: ",
                  " Escolha uma posicao: ")
    if coloca_ou_move(t,j): # fase de movimento
        m = input("{}{}".format(men,sa))
        if len(m) == 4 and m[:2] in pos_str and m[2:] in pos_str:
            orig,dest = m[:2],m[2:]
            peca = obter_peca(t,p_ext[orig])
                            # verificao se o movimento eh valido
            if (p_ext[dest] in obter_posicoes_adjacentes(p_ext[orig]) and 
                eh_posicao_livre(t,p_ext[dest]) and pecas_iguais(peca,j)):
                return (p_ext[orig],p_ext[dest])
            
            if (not eh_posicao_livre(t,p_ext[dest]) and pecas_iguais(peca,j)):
                for pos in obter_posicoes_adjacentes(p_ext[orig]):
                    if eh_posicao_livre(t,pos):
                        raise ValueError("{}".format(erro))
                return (p_ext[orig],)*2
                 
        raise ValueError("{}".format(erro))
    else:                   # fase de colocao,ainda se pode colocar 
                            #mais pecas do jogador 
        m = input("{}{}".format(men,gem)) # e nao ha vencedor
        if m in pos_str and p_ext[m] in obter_posicoes_livres(t):
            return (p_ext[m],)
        raise ValueError("obter_movimento_manual: escolha invalida")
        
def obter_movimento_auto(t,j,nivel):
    
    # obter_movimento_auto: tabuleiro x peca x str -> tuplo de posicoes
    """
    obter_movimento_auto(t,j,nivel) funcao auxiliar que recebe um tabuleiro e
    uma peca de um jogador e uma cadeia de carateres que representa o nivel de
    dificuldade do jogo e devolve um tuplo com uma ou duas posicoes que
    representam uma posicao ou um movimento escolhido automaticamente.
    
    """
    if coloca_ou_move(t,j): # Fase de movimento
                            # associa a dificuldade de jogo 
                            # com funcoes de tratamento
        fases = {"facil":movimento_auto_facil(t,j),
                 "normal": minimax(t,j,1,())[1],"dificil":minimax(t,j,5,())[1]
                 }      
        for jogo in NVL:    # diferentes dificuldades de jogo
            if nivel == jogo:
                return (fases[nivel][0],fases[nivel][1])
        
    return (facil(t,j),)    #a fase de colocacao e a mesma 
                            #para diferentes dificuldades
    
def tabuleiro_mod(t,turno,modo,pc):
    
    # tabuleiro_mod: tabuleiro x inteiro x str x tuplo x inteiro -> tabuleiro 
    """
    tabuleiro_mod(t,turno,modo,pc) devolve o tabuleiro depois de se ter 
    aplicado as operacoes de colocacao ou movimento de peca.
    
    """
    if turno == 1: # humano
        if pc == 1:
            turno = -1
        estrategia = obter_movimento_manual(t,inteiro_para_peca(turno))
        if len(estrategia) == 1: 
            t = coloca_peca(t,inteiro_para_peca(turno),estrategia[0])
        else:
            t = move_peca(t,estrategia[0],estrategia[1])  
    else:
        mensagem = "Turno do computador ({}):"
        print(mensagem.format(modo))
        estrategia = obter_movimento_auto(t,inteiro_para_peca(pc),modo)
        if len(estrategia) == 1:
            t = coloca_peca(t,inteiro_para_peca(pc),estrategia[0])
        else:
            t = move_peca(t,estrategia[0],estrategia[1])  
    return t
        
def moinho(jogador,modo):
    
    # moinho: str x str -> str
    """
    moinho(jogador,modo),funcao principal do jogo que permite jogar um 
    jogo do moinho completo entre um jogador humano e o computador.
    
    """
    if jogador not in ("[O]","[X]") or modo not in NVL:
        raise ValueError("moinho: argumentos invalidos")
    else:
        print("Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {}.".format(
        modo))
        if jogador == '[X]':
            turno = 1
            pc = -turno
        else:
            turno = -1
            pc = -turno 
        t = cria_tabuleiro()
        print(tabuleiro_para_str(t))
        while pecas_iguais(obter_ganhador(t),cria_peca(" ")):
          
            t = tabuleiro_mod(t,turno,modo,pc)
            print(tabuleiro_para_str(t))
            turno = -turno # alterna o jogador
        
        return peca_para_str(obter_ganhador(t))
