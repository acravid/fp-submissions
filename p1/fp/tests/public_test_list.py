def teste211():
    total_score = 0
    fun_name = eh_tabuleiro_public

    tab = ((1,0,0),(-1,1,0),(1,-1,-1))
    eh_tabuleiro(tab)
    # True

    tab = ((1,0,0),('O',1,0),(1,-1,-1))
    eh_tabuleiro(tab)
    # False

    tab = ((1,0,0),(-1,1,0),(1,-1))
    eh_tabuleiro(tab)
    # False

    return


def teste212():
    total_score = 0
    fun_name = eh_posicao_public

    eh_posicao(9)
    # True
    eh_posicao(-2)
    # False
    eh_posicao((1,))
    # False

    return



def teste213():
    total_score = 0
    fun_name = obter_coluna_public

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    obter_coluna(tab, 2)
    # (-1, 0, -1)

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    obter_coluna(tab, 1)
    # (1, 1, 1)

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    obter_coluna(tab, 4)
    # obter_coluna: algum dos argumentos e invalido


    return


def teste214():
    total_score = 0
    fun_name = obter_linha_public

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    obter_linha(tab, 2)
    # (1, 0, -1)

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    obter_linha(tab, 1)
    # (1, -1, 0)
    
    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    obter_linha(tab, 4)
    # obter_linha: algum dos argumentos e invalido


    return



def teste215():
    total_score = 0
    fun_name = obter_diagonal_public

    
    tab = ((1,-1,-1),(1,0,-1),(1,-1,0))
    obter_diagonal(tab, 1)
    # (1, 0, 0)

    tab = ((1,-1,-1),(1,0,-1),(1,-1,0))
    obter_diagonal(tab, 2)
    # (1, 0, -1)

    tab = ((1,-1,-1),(1,0,-1),(1,-1,0))
    obter_diagonal(tab, 3)
    # obter_diagonal: algum dos argumentos e invalido

    return



def teste216():
    total_score = 0
    fun_name = tabuleiro_str_public

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    tabuleiro_str(tab)
    #  X | O |   \\n-----------\\n X |   | O \\n-----------\\n X | O |   
    
    tabuleiro_str(((1,-1,0),(1,0,-1)))
    # tabuleiro_str: o argumento e invalido

    return



def teste221():
    total_score = 0
    fun_name = eh_posicao_livre_public

    tab = ((1,-1,0),(1,-1,0),(1,-1,0))
    eh_posicao_livre(tab, 9)
    # True

    tab = ((1,-1,0),(1,-1,0),(1,-1,0))
    eh_posicao_livre(tab, 7)
    # False


    tab = ((1,-1,0),(1,-1,0),(1,-1,0))
    eh_posicao_livre(tab, (-1,))
    # eh_posicao_livre: algum dos argumentos e invalido


    return



def teste222():
    total_score = 0
    fun_name = obter_posicoes_livres_public

    tab = ((1,-1,0),(1,-1,0),(1,-1,0))
    obter_posicoes_livres(tab)
    # (3, 6, 9)
    
    tab = ((1,-1,0),(1,-1,0),(1,-1))
    obter_posicoes_livres(tab)
    # obter_posicoes_livres: o argumento e invalido

    return



def teste223():
    total_score = 0
    fun_name = jogador_ganhador_public

    tab = ((1,-1,0),(1,0,-1),(0,-1,0))
    jogador_ganhador(tab)
    # 0
    
    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    jogador_ganhador(tab)
    # 1
    
    tab = ((1,1,-1),(-1,-1,1),(-1,-1,1))
    jogador_ganhador(tab)
    # -1

    tab = ((1,1,-1),(-1,-1,1),(1,-1))
    jogador_ganhador(tab)
    # jogador_ganhador: o argumento e invalido

    return


def teste224():
    total_score = 0
    fun_name = marcar_posicao_public

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    marcar_posicao(tab, -1, 5)
    # ((1, -1, 0), (1, -1, -1), (1, -1, 0))

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    marcar_posicao(tab, 1, 3)
    # ((1, -1, 1), (1, 0, -1), (1, -1, 0))

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    marcar_posicao(tab, 1, 1)
    # marcar_posicao: algum dos argumentos e invalido

    return


def teste231():
    total_score = 0
    fun_name = escolher_posicao_manual_public


    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    escolher_posicao_manual_mooshak(tab,'3')
    # Turno do jogador. Escolha uma posicao livre: 3

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    escolher_posicao_manual_mooshak(tab,'12')
    # Turno do jogador. Escolha uma posicao livre: escolher_posicao_manual: a posicao introduzida e invalida

    return


def teste232():
    total_score = 0
    fun_name = escolher_posicao_auto_public

    tab = ((0,0,0),(0,1,0),(-1,0,0))
    escolher_posicao_auto(tab, 1, 'basico')
    # 1

    tab = ((0,0,0),(0,1,0),(-1,0,0))
    escolher_posicao_auto(tab, 1, 'normal')
    # 3

    tab = ((0,0,-1),(-1,1,0),(1,0,0))
    escolher_posicao_auto(tab, 1, 'normal')
    # 1

    tab = ((0,0,-1),(-1,1,0),(1,0,0))
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 8

    tab = ((0,0,-1),(-1,1,0),(1,0,0))
    escolher_posicao_auto(tab, 'X', 'basico')
    # escolher_posicao_auto: algum dos argumentos e invalido


def teste233():
    total_score = 0
    fun_name = jogo_do_galo_public

    jogo_do_galo_mooshak('O', 'basico', '1\\n7\\n4')
    # Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'O'.\nTurno do computador (basico):\n   |   |   \n-----------\n   | X |   \n-----------\n   |   |   \nTurno do jogador. Escolha uma posicao livre:  O |   |   \n-----------\n   | X |   \n-----------\n   |   |   \nTurno do computador (basico):\n O |   | X \n-----------\n   | X |   \n-----------\n   |   |   \nTurno do jogador. Escolha uma posicao livre:  O |   | X \n-----------\n   | X |   \n-----------\n O |   |   \nTurno do computador (basico):\n O |   | X \n-----------\n   | X |   \n-----------\n O |   | X \nTurno do jogador. Escolha uma posicao livre:  O |   | X \n-----------\n O | X |   \n-----------\n O |   | X \nO

    jogo_do_galo_mooshak('X', 'perfeito', '1\\n9\\n8\\n3\\n4')
    # Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'X'.\nTurno do jogador. Escolha uma posicao livre:  X |   |   \n-----------\n   |   |   \n-----------\n   |   |   \nTurno do computador (perfeito):\n X |   |   \n-----------\n   | O |   \n-----------\n   |   |   \nTurno do jogador. Escolha uma posicao livre:  X |   |   \n-----------\n   | O |   \n-----------\n   |   | X \nTurno do computador (perfeito):\n X | O |   \n-----------\n   | O |   \n-----------\n   |   | X \nTurno do jogador. Escolha uma posicao livre:  X | O |   \n-----------\n   | O |   \n-----------\n   | X | X \nTurno do computador (perfeito):\n X | O |   \n-----------\n   | O |   \n-----------\n O | X | X \nTurno do jogador. Escolha uma posicao livre:  X | O | X \n-----------\n   | O |   \n-----------\n O | X | X \nTurno do computador (perfeito):\n X | O | X \n-----------\n   | O | O \n-----------\n O | X | X \nTurno do jogador. Escolha uma posicao livre:  X | O | X \n-----------\n X | O | O \n-----------\n O | X | X \nEMPATE

    return
