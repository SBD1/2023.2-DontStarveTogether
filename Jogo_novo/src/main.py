import psycopg2
import time
import sys
import os
import random
conn = psycopg2.connect(
    host = "db",
    port = "5432",
    database="dontstarve",
    user="sbd1",
    password="asdfghjkl")
cursor = conn.cursor()

def get_jogadores():
    cursor.execute("SELECT  * FROM jogador")
    return cursor.fetchall()

def get_jogador_id(id):
    cursor.execute(f"SELECT * FROM jogador WHERE id = '{id}'")
    aux = cursor.fetchone()
    jogador = type('', (), {})()
    jogador.id = aux[0]
    jogador.nome = aux[1]
    jogador.vida = aux[2]
    jogador.temp_corporal = aux[3]
    jogador.id_mochila = aux[4]
    jogador.id_posicao = aux[5]
    jogador.id_roupa_equipada = aux[6]
    jogador.id_item_equipado = aux[7]
    return jogador

def del_jogador(id):
    try:
        cursor.execute(f"DELETE FROM jogador WHERE id = {id}")
        conn.commit()
    except:
        return False
    return True

def set_vida_jogador(id_jogador, vida):
    cursor.execute(f"UPDATE jogador SET vida = {vida} WHERE id = {id_jogador};")
    conn.commit()
    return True

def novo_jogador(nome: str):
    cursor.execute(f"INSERT INTO mochila VALUES (DEFAULT);")
    cursor.execute(f"SELECT id FROM mochila ORDER BY  id  DESC LIMIT 1;")
    id_mochila = cursor.fetchone()
    cursor.execute(f"INSERT INTO jogador VALUES (DEFAULT,'{nome}',100,36,{id_mochila[0]}, 134,NULL,NULL);")
    cursor.execute(f"SELECT id FROM jogador ORDER BY  id  DESC LIMIT 1;")
    id = cursor.fetchone()
    cursor.execute(f"SELECT id FROM ferramenta WHERE nome =  'Picareta Detreriorada'")
    id_picareta = cursor.fetchone()[0]
    instancia_item1 = criar_instancia_item(id_picareta,'f')
    cursor.execute(f"SELECT id FROM ferramenta WHERE nome =  'Machado Fraco'")
    id_machado = cursor.fetchone()[0]
    instancia_item2 = criar_instancia_item(id_machado,'f')
    jogador = get_jogador_id(id[0])
    adicionar_item_iventario(jogador,instancia_item1)
    adicionar_item_iventario(jogador,instancia_item2)
    conn.commit()
    return jogador


def get_posicao_jogador(id_jogador):
    cursor.execute(f"SELECT id_posicao FROM jogador WHERE id ='{id_jogador}'")
    id_pos = cursor.fetchone()[0]
    return get_posicao(id_pos)


def set_posicao_jogador (id, posicao):
    cursor.execute(f"UPDATE jogador SET id_posicao = {posicao} WHERE id = '{id}'")
    conn.commit()
    return True


def get_inventario_por_tipo (id, tipo):
    cursor.execute(f"SELECT id_mochila FROM jogador WHERE id = {id}")
    id_mochila = cursor.fetchone()[0]
    cursor.execute(f"SELECT id_instancia_item FROM mochila_guarda_instancia_de_item WHERE id_mochila = {id_mochila}")
    instancias = cursor.fetchall()
    result = []
    for instancia in instancias:
        cursor.execute(f"SELECT * FROM instancia_item WHERE id = {instancia[0]}")
        news = cursor.fetchone()
        if(news[2] == tipo):
            result.append(get_item_por_id_instancia(instancia[0]))
    return result

def get_item_por_id_instancia(id_instancia):
    cursor.execute(f"SELECT * FROM instancia_item WHERE id = {id_instancia}")
    instancia = cursor.fetchone()
    id_item = instancia[1]
    tipo = instancia[2]
    if(tipo == 'a'):
        cursor.execute(f"SELECT * FROM arma WHERE id = {id_item}")
        aux = cursor.fetchone()
        arma = type('', (), {})()
        arma.id = aux[0]
        arma.nome = aux[1]
        arma.dano = aux[2]
        arma.descricao = aux[3]
        arma.instancia = id_instancia
        return (arma)
    elif(tipo == 'f'):
        cursor.execute(f"SELECT * FROM ferramenta WHERE id = {id_item}")
        aux = cursor.fetchone()
        ferramenta = type('', (), {})()
        ferramenta.id = aux[0]
        ferramenta.nome = aux[1]
        ferramenta.funcao = aux[2]
        ferramenta.descricao = aux[3]
        ferramenta.instancia = id_instancia
        return (ferramenta)
    elif(tipo == 'r'):
        cursor.execute(f"SELECT * FROM roupa WHERE id = {id_item}")
        aux = cursor.fetchone()
        roupa = type('', (), {})()
        roupa.id = aux[0]
        roupa.nome = aux[1]
        roupa.protecao_termica = aux[2]
        roupa.protecao_fisica = aux[3]
        roupa.descricao = aux[4]
        roupa.instancia = id_instancia
        return (roupa)
    elif(tipo == 'i'):
        cursor.execute(f"SELECT * FROM ingrediente WHERE id = {id_item}")
        aux = cursor.fetchone()
        ingrediente = type('', (), {})()
        ingrediente.id = aux[0]
        ingrediente.nome = aux[1]
        ingrediente.funcao = aux[2]
        ingrediente.descricao = aux[3]
        ingrediente.instancia = id_instancia
        return (ingrediente)


def get_posicao(id_pos):
    cursor.execute(f"SELECT * FROM posicao WHERE id = {id_pos}")
    aux = cursor.fetchone()
    position = type('', (), {})()
    position.id = aux[0]
    position.bioma = aux[2]
    position.norte = aux[3]
    position.sul = aux[4]
    position.leste = aux[5]
    position.oeste = aux[6]
    position.descricao = aux[7]
    position.pedras =  aux[8]
    position.madeiras = aux[9]
    return position


def set_pedras(id_pos, pedras):
    cursor.execute(f"UPDATE posicao SET pedras = {pedras} WHERE id = {id_pos}")
    conn.commit()
    return True


def get_instancia_item_por_id(id_item):
    cursor.execute(f"SELECT * FROM instancia_item WHERE id = {id_item}")
    return cursor.fetchall()


def set_item_equipado(id_jogador, id_instancia_item):
    cursor.execute(f"UPDATE jogador SET id_item_equipado = {id_instancia_item} WHERE id = {(id_jogador)}")
    conn.commit()
    return True
    


def get_item_equipado(id_jogado):
    cursor.execute(f"SELECT id_item_equipado FROM jogador WHERE id = {(id_jogado)}")
    id_item = cursor.fetchone()
    result = get_item_por_id_instancia(id_item[0]) if id_item[0] != None else None
    return result


def set_roupa_equipada(id_jogador, id_instancia_item):
    cursor.execute(f"UPDATE jogador SET id_roupa_equipada = {id_instancia_item} WHERE id = {(id_jogador)}")
    conn.commit()
    return True


def get_roupa_equipada(id_jogador):
    cursor.execute(f"SELECT id_roupa_equipada FROM jogador WHERE id = {id_jogador}")
    id_item = cursor.fetchone()
    result = get_item_por_id_instancia(id_item[0]) if id_item[0] != None else None
    return result


def add_instancia_item_possicao(id_pos, id_instancia):
    cursor.execute(f"INSERT INTO instancia_item_posicao VALUES ({id_pos},{id_instancia})")
    conn.commit()
    return True


def get_instancia_item_posicao(id_pos):
    cursor.execute(f"SELECT id_instancia_item FROM instancia_item_posicao WHERE id_posicao = {id_pos}")
    aux = cursor.fetchone()
    result = []
    if aux:
        for i in aux:
            result.append(get_instancia_item_por_id(i))
    return result


def del_instancia_item_posicao(id_pos, id_instancia):
    cursor.execute(f"DELETE FROM instancia_item_posicao WHERE id_posicao = {id_pos} AND id_instancia_item = {id_instancia}")
    conn.commit()
    return cursor.fetchone()


def get_crafts(workbench):

    if workbench:
        cursor.execute(f"SELECT * FROM craft")
    else:
        cursor.execute(f"SELECT * FROM craft WHERE necessita_workbench = 'false'")
    aux = cursor.fetchall()
    result = []
    if aux:
        for i in aux:
            item = get_item_por_id(i[0])
            craft = type('', (), {})()
            craft.id = i[0]
            craft.id_item1= i[1]
            craft.quant_item1 = i[2]
            craft.id_item2 = i[3]
            craft.quant_item2 = i[4]
            craft.id_item3 = i[5]
            craft.quant_item3 = i[6]
            craft.needs_workbench = i[7]
            craft.descricao = i[8]
            craft.nome = item.nome if item else None
            result.append(craft)
    return result

def get_item_por_id(id):
    try:
        cursor.execute(f"SELECT * FROM arma WHERE id = {id}")
        aux = cursor.fetchone()
        if aux:
            arma = type('', (), {})()
            arma.id = aux[0]
            arma.nome = aux[1]
            arma.dano = aux[2]
            arma.descricao = aux[3]
            return arma
    except:
        try:
            cursor.execute(f"SELECT * FROM ferramenta WHERE id = {id}")
            aux = cursor.fetchone()
            if aux:
                ferramenta = type('', (), {})()
                ferramenta.id = aux[0]
                ferramenta.nome = aux[1]
                ferramenta.defesa = aux[2]
                ferramenta.descricao = aux[3]
                return ferramenta
        except:
            try:
                cursor.execute(f"SELECT * FROM roupa WHERE id = {id}")
                aux = cursor.fetchone()
                if aux:
                    roupa = type('', (), {})()
                    roupa.id = aux[0]
                    roupa.nome = aux[1]
                    roupa.defesa = aux[2]
                    roupa.descricao = aux[3]
                    return roupa
            except:
                try:
                    cursor.execute(f"SELECT * FROM ingrediente WHERE id = {id}")
                    aux = cursor.fetchone()
                    if aux:
                        ingrediente = type('', (), {})()
                        ingrediente.id = aux[0]
                        ingrediente.nome = aux[1]
                        ingrediente.descricao = aux[2]
                        return ingrediente
                except:
                    return None;


def get_mochila_id(jogador):
    cursor.execute(f"SELECT id_mochila FROM jogador WHERE id = '{jogador.id}'")
    return cursor.fetchone()[0]

def verificar_inventario(id, id_item, quantidade = 1):
    cursor.execute(f"SELECT id_instancia_item FROM instancia_item WHERE id_item = {id_item}")
    aux = cursor.fetchone()
    if(len(aux) > quantidade):
        cursor.execute(f"SELECT id_instancia_item FROM mochila_guarda_instancia_de_item WHERE id_mochila = {get_mochila_id(id)} ")
        aux2 = cursor.fetchone()
        if(aux2 in aux):
            return True
    return False

def criar_instancia_item(id_item,tipo):
    cursor.execute(f"INSERT INTO instancia_item VALUES (DEFAULT,{id_item},'{tipo}')")
    cursor.execute(f"SELECT id FROM instancia_item ORDER BY  id  DESC LIMIT 1;")
    conn.commit()
    return cursor.fetchone()[0]


def remover_item_iventario(id, id_item):

    id_mochila = get_mochila_id(id)
    cursor.execute(f"DELETE FROM mochila_guarda_instancia_de_item WHERE id_mochila = {id_mochila} AND id_instancia_item = {id_item}")
    conn.commit()
    return cursor.fetchall()
    

def adicionar_item_iventario(id, id_instancia_item):
    id_mochila = get_mochila_id(id)
    cursor.execute(f"INSERT INTO mochila_guarda_instancia_de_item VALUES ({id_mochila},{id_instancia_item})")
    conn.commit()
    return True


def get_bioma(id_bioma):
    cursor.execute(f"SELECT * FROM bioma WHERE id = {id_bioma}")
    aux = cursor.fetchone()
    bioma = type('', (), {})()
    bioma.id = aux[0]
    bioma.chance_batalha = aux[1]
    bioma.delta_temp = aux[2]
    bioma.nome = aux[3]
    bioma.nivel = aux[4]
    return bioma

def get_monstros_by_pos(id_pos):
    cursor.execute(f"SELECT * FROM monstro WHERE id_posicao = {id_pos}")
    aux = cursor.fetchone()
    monstros = []
    try:
        aux = list(aux)[::-1]
        while aux:
            monstro = type('', (), {})()
            monstro.id = aux.pop()
            monstro.nome = aux.pop()
            monstro.dano = aux.pop()
            monstro.descricao = aux.pop()
            monstro.vida = aux.pop()
            monstro.isca = aux.pop()
            monstro.id_posicao = aux.pop()
            monstros.append(monstro)
    finally:
        return monstros


def del_monstro(id_monstro):
    try:
        cursor.execute(f"DELETE FROM monstro WHERE id = {id_monstro}")
        conn.commit()
        return True
    except:
        return False
    
tutorial = """
"""

def jogo_init(jogador: str, first_time: bool):

    clear()

    if first_time:
        print(tutorial)
        input('[i] precione ENTER para continuar')

    while menu_jogador(jogador):
        # clear()
        continue

_txt_init = '''\n
[1] Carregar jogo
[2] Novo Jogo
[0] Sair\n
'''

_txt_menu_jogador = '''\n
[1] Andar
[2] Inventario
[3] Craft
[0] Sair
'''

_txt_otp_invalida = '\n[-] Digite uma opcao valida!'


def clear():
    print(chr(27) + "[2J")


def menu_init():
    while True:
        clear()
        opt_init = -1
        jogador  = -1
        jogador_novo = True
        opt_init = input(_txt_init).strip()

        if opt_init == '1':
            jogador = menu_carregar_jogo()
            jogador_novo = False
            
            if jogador != -1:
                jogo_init(jogador, jogador_novo)
            continue

        if opt_init == '2':
            jogador = menu_novo_jogo()
            jogador_novo = True

            if jogador != -1:
                jogo_init(jogador, jogador_novo)
            continue

        if opt_init == '0':
            exit()
        
        print(_txt_otp_invalida)
        input("[i] precione enter para continuar")


def menu_carregar_jogo():
    jogos_salvos = []
    ids = []
    opt_carregar = -1
    clear()

    try:
        jogos_salvos = get_jogadores()
    except:
        print('\n[-] Nao foi possivel carregar lista de jogos salvos')
        input("[i] precione enter para continuar")
        return -1

    if jogos_salvos:
        for jogador in jogos_salvos:
            ids.append(jogador[0])
            print(f'[{jogador[0]}] {jogador[1]}')
        print(f'\n[0] Cancelar')

    else:
        clear()
        print('\n[i] Voce nao possui jogos salvos!')
        input("[i] precione enter para continuar")
        return -1

    while True:
        opt_carregar = input().strip()

        try:
            opt_carregar = abs(int(opt_carregar))
        except:
            print(_txt_otp_invalida)
            continue

        if opt_carregar == 0:
            return -1 
        
        if  ids.__contains__(opt_carregar):
            clear()
            print('[+] Carregango jogo...')
            input("[i] precione enter para continuar")
            return get_jogador_id(opt_carregar)
        
        print(_txt_otp_invalida)
        

def menu_novo_jogo():
    while True:
        clear()
        nome_jogador = input(
            '[?] Nome do peronagem: ').strip()

        if nome_jogador == '':
            print('[-] Nenhum nome inserido, jogador nao criado')
            input("[i] precione enter para continuar")
            return -1

        jogador = novo_jogador(nome_jogador)
        
        if jogador == -1:
            print('[-] Error ao criar novo peronagem. Tente novamente\n')
            input("[i] precione enter para continuar")
            return -1

        print('[+] Carregango jogo...')
        input("[i] precione enter para continuar")
        return jogador

def menu_jogador(jogador):

    while True:
        clear()
        posicao_jogador = get_posicao_jogador(jogador.id)
        print(posicao_jogador.descricao)
        jogador = get_jogador_id(jogador.id)
        print('\n[i] Vida: ' + str(jogador.vida))

        print(_txt_menu_jogador)
        acao = input('[?] ').strip()

        if acao == '1':
            andar(jogador, posicao_jogador)
            continue

        if acao == '2':
            inventario(jogador)
            continue

        if acao == '3':
            craft(jogador, posicao_jogador)
            continue

        if acao == '0':
            return False
        
def andar(jogador, posicao_jogador):
    clear()

    if posicao_jogador.norte != None:
        print('[1] Norte')
    if posicao_jogador.sul != None:
        print('[2] Sul')
    if posicao_jogador.leste != None:
        print('[3] Leste')
    if posicao_jogador.oeste != None:
        print('[4] Oeste')

    print('[0] Nao andar')

    while True:
        opt_andar = input('[?] ').strip()

        try:
            opt_andar = abs(int(opt_andar))
        except:
            print(_txt_otp_invalida)
            continue

        if opt_andar == 1 and posicao_jogador.norte != None:
            verificar_luta(jogador, posicao_jogador.norte)
            set_posicao_jogador(jogador.id, posicao_jogador.norte)
            return True
        if opt_andar == 2 and posicao_jogador.sul != None:
            verificar_luta(jogador, posicao_jogador.sul)
            set_posicao_jogador(jogador.id, posicao_jogador.sul)
            return True
        if opt_andar == 3 and posicao_jogador.leste != None:
            verificar_luta(jogador, posicao_jogador.leste)
            set_posicao_jogador(jogador.id, posicao_jogador.leste)
            return True
        if opt_andar == 4 and posicao_jogador.oeste != None:
            verificar_luta(jogador, posicao_jogador.oeste)
            set_posicao_jogador(jogador.id, posicao_jogador.oeste)
            return True

        if opt_andar == 0:
            return True

        print(_txt_otp_invalida)
        

def inventario(jogador):
    clear()

    item_equipado = get_item_equipado(jogador.id)
    print(f'equipada: {item_equipado}')
    if item_equipado:
        print(f'[i] Item equipado:  {item_equipado.nome}')

    roupa_equipada = get_roupa_equipada(jogador.id)
    if roupa_equipada:
        print(f'[i] Roupa equipado: {roupa_equipada.nome}')

    print("\n[1] Armas")
    print("[2] Roupas")
    print("[3] Ferramentas")
    print("[4] Ingredientes")
    print("[0] Fechar inventario")

    while True:
        inventario = []
        opt_inventario = input('[?] ').strip()

        try:
            opt_inventario = abs(int(opt_inventario))
        except:
            print(_txt_otp_invalida)
            continue

        if opt_inventario == 1:
            inventario = get_inventario_por_tipo(jogador.id, 'a')
            inventario_armas(jogador, inventario)
            return True

        if opt_inventario == 2:
            inventario = get_inventario_por_tipo(jogador.id, 'r')
            inventario_roupas(jogador, inventario)
            return True
            
        if opt_inventario == 3:
            inventario = get_inventario_por_tipo(jogador.id, 'f')
            inventario_ferramentas(jogador, inventario)
            return True
            
        if opt_inventario == 4:
            inventario = get_inventario_por_tipo(jogador.id, 'i')
            inventario_ingredientes(jogador, inventario)
            return True
            
        if opt_inventario == 0:
            return True

        print(_txt_otp_invalida)
        

def inventario_armas(jogador, inventario):

    while True:
        clear()
        print('[i] Armas\n')

        i = 1
        for item in inventario:
            print(f'[{i}] {item.nome}')
            i+=1
        print('[0] Voltar')
        opt_arma = input('[?] ').strip()

        try:
            opt_arma = abs(int(opt_arma))
        except:
            print(_txt_otp_invalida)
            continue

        if opt_arma > len(inventario):
            print(_txt_otp_invalida)
            input('[i] precione ENTER para continuar')
            continue
            
        if opt_arma == 0:
            return True

        clear()
        print(f"[i] Nome:      {inventario[opt_arma-1].nome}")
        print(f"[i] Descricao: {inventario[opt_arma-1].descricao}")
        print(f"[i] Dano:      {inventario[opt_arma-1].dano}")

        print(f"\n[?] Equipar {inventario[opt_arma-1].nome}? (S/N)")

        if(input('[?]').lower() == 's'):
            set_item_equipado(jogador.id, inventario[opt_arma-1].instancia)
        else:
            continue

        


def inventario_roupas(jogador, inventario):
    while True:
        clear()
        print('[i] Roupas\n')

        i = 1
        for item in inventario:
            print(f'[{i}] {item.nome}')
            i+=1
        print('[0] Voltar')
        opt_roupa = input('[?] ').strip()

        try:
            opt_roupa = abs(int(opt_roupa))
        except:
            print(_txt_otp_invalida)
            continue

        if opt_roupa > len(inventario):
            print(_txt_otp_invalida)
            input('[i] precione ENTER para continuar')
            continue
            
        if opt_roupa == 0:
            return True

        clear()
        print(f"[i] Nome:             {inventario[opt_roupa-1].nome}")
        print(f"[i] Descricao:        {inventario[opt_roupa-1].descricao}")
        print(f"[i] Protecao Termica: {inventario[opt_roupa-1].protecao_termica}")
        print(f"[i] Protecao Fisica:  {inventario[opt_roupa-1].protecao_termica}")

        print(f"\n[?] Equipar {inventario[opt_roupa-1].nome}? (S/N)")

        if(input('[?] ').lower() == 's'):
            set_roupa_equipada(jogador.id, inventario[opt_roupa-1].instancia)
        else:
            continue

def inventario_ferramentas(jogador, inventario):
    while True:
        clear()
        print('[i] Ferramentas\n')

        i = 1
        for item in inventario:
            print(f'[{i}] {item.nome}')
            i+=1
        print('[0] Voltar')
        opt_ferramenta = input('[?] ').strip()

        try:
            opt_ferramenta = abs(int(opt_ferramenta))
        except:
            print(_txt_otp_invalida)
            continue

        if opt_ferramenta > len(inventario):
            print(_txt_otp_invalida)
            input('[i] precione ENTER para continuar')
            continue
            
        if opt_ferramenta == 0:
            return True

        clear()
        print(f"[i] Nome:             {inventario[opt_ferramenta-1].nome}")
        print(f"[i] Descricao:        {inventario[opt_ferramenta-1].descricao}")

        print(f"\n[?] Usar {inventario[opt_ferramenta-1].nome}? (S/N)")

        if(input('[?] ').lower() == 's'):
            funcao = inventario[opt_ferramenta-1].funcao
            try:
                eval('world.'+ funcao)
                return
            except:
                print('[-] Nao foi possivel utilizar a ferramenta')
                input("[i] precione enter para continuar")
        else:
            continue

def inventario_ingredientes(jogador, inventario):
    while True:
        clear()
        print('[i] Ingredientes\n')

        i = 1
        for item in inventario:
            print(f'[{i}] {item.nome}')
            i+=1
        print('[0] Voltar')
        opt_ingrediente = input('[?] ').strip()

        try:
            opt_ingrediente = abs(int(opt_ingrediente))
        except:
            print(_txt_otp_invalida)
            continue

        if opt_ingrediente > len(inventario):
            print(_txt_otp_invalida)
            input('[i] precione ENTER para continuar')
            continue
            
        if opt_ingrediente == 0:
            return True
        
        clear()
        print(f"[i] Nome:             {inventario[opt_ingrediente-1].nome}")
        print(f"[i] Descricao:        {inventario[opt_ingrediente-1].descricao}")

        print(f"\n[?] Usar {inventario[opt_ingrediente-1].nome}? (S/N)")

        if(input('[?] ').lower() == 's'):
            funcao = inventario[opt_ingrediente-1][1].funcao
            try:
                print('world.'+ funcao)
                eval('world.'+ funcao)
            except:
                print('[-] Nao foi possivel utilizar o ingrediente')
                input("[i] precione enter para continuar")
        else:
            continue

def craft(jogador, posicao):
    while True:
        clear()
        print('[i] Craft\n')

        itens_na_pos = get_instancia_item_posicao(posicao.id)

        if itens_na_pos:
            for item_na_pos in itens_na_pos:
                if item_na_pos == 11: 
                    lista_crafts = get_crafts(True)
                    break
        else:
            lista_crafts = get_crafts(False)

        i = 1
        for craft in lista_crafts:
            print(f'[{i}] {craft.nome}')
            i+=1
        print('[0] Voltar')
        opt_craft = input('[?] ').strip()

        try:
            opt_craft = abs(int(opt_craft))
        except:
            print(_txt_otp_invalida)
            continue

        if opt_craft > len(lista_crafts):
            print(_txt_otp_invalida)
            input('[i] precione ENTER para continuar')
            continue
            
        if opt_craft == 0:
            return True

        clear()
        print(f"[i] Nome:             {lista_crafts[opt_craft-1].nome}")
        print(f"[i] Materiais:        {lista_crafts[opt_craft-1].descricao}")

        print(f"\n[?] Construis {lista_crafts[opt_craft-1].nome}? (S/N)")

        if(input('[?] ').lower() == 's'):
            crafitar(jogador, lista_crafts[opt_craft-1])
        else:
            continue

def crafitar(jogador, craft):

    if craft.id_item1:
        if not verificar_inventario(jogador.id, craft.id_item1, craft.quant_item1):
            print('[-] Voce nao possui todos os ingredientes necessarios')
            input('[i] precione ENTER para continuar')
            return False

    if craft.id_item2:
        if not verificar_inventario(jogador.id, craft.id_item2, craft.quant_item2):
            print('[-] Voce nao possui todos os ingredientes necessarios')
            input('[i] precione ENTER para continuar')
            return False
    
    if craft.id_item3:
        if not verificar_inventario(jogador.id, craft.id_item3, craft.quant_item3):
            print('[-] Voce nao possui todos os ingredientes necessarios')
            input('[i] precione ENTER para continuar')
            return False

    if craft.id_item1:
        for i in range(craft.quant_item1):
            remover_item_iventario(jogador.id, craft.id_item1)

    if craft.id_item2:
        for i in range(craft.quant_item2):
            remover_item_iventario(jogador.id, craft.id_item2)

    if craft.id_item3:
        for i in range(craft.quant_item3):
            remover_item_iventario(jogador.id, craft.id_item3)
    
    instancia_criada = criar_instancia_item(craft.id_item_resultado)

    adicionar_item_iventario(jogador.id, instancia_criada)
    return True


def morte(id_jogador):
    clear()
    input(f'[i] sua vida chegou a 0')
    input(f'[i] voce morreu')
    input(f'[i] clice ENTER para continuar')

    del_jogador(id_jogador)
    os.execl(sys.executable, sys.executable, *sys.argv)

def pegar_pedra(jogador, nivel):
    posicao = get_posicao_jogador(jogador)
    sorte = random.uniform(.5, 1.5)

    quant_pedras_pegas = round(sorte * nivel * 10)
    quant_pedras_pegas = min(quant_pedras_pegas, posicao.pedras)

    clear()

    if quant_pedras_pegas > 0:
        set_pedras(posicao.id, posicao.pedras - quant_pedras_pegas)
        print(f'[i] {jogador} pegou {quant_pedras_pegas} pedras')
    else:
        print(f'[i] Nao ha pedras por aqui')

    input("\n[i] precione enter para continuar")
    return 

def colocar_na_pos(jogador, id_item):
    instancia_item = verificar_inventario(jogador.id, id_item)
    add_instancia_item_possicao(jogador.pos, instancia_item)
    remover_item_iventario(jogador.id, instancia_item.id_item)


def verificar_luta(jogador, id_pos):
    pos = get_posicao(id_pos)
    bioma = get_bioma(pos.bioma)

    sorte = random.uniform(0, 1)
    if sorte <= bioma.chance_batalha:
        monstros = get_monstros_by_pos(id_pos)

        if len(monstros) == 0:
            return

        foo = random.randint(0,len(monstros)-1)
        monstro = monstros[foo]
        luta(jogador, monstro)



def luta(jogador, monstro):
    clear()
    print(f'[i] um {monstro.nome} selvagem apareceu!')
    print(f'[i] {monstro.descricao}')
    input("[i] precione ENTER para continuar")

    vida_jogador = jogador.vida - (monstro.dano*2)

    if(vida_jogador <= 0):
        morte(jogador.id)

    clear()
    print(f'[i] voce levou {monstro.dano*2} de dano, mas matou o monstro')
    input("[i] precione ENTER para continuar")
    set_vida_jogador(jogador.id, vida_jogador)
    del_monstro(monstro.id)

def main():
    menu_init()

if __name__ == '__main__':
    print('\n[+] Bem vindo ao Dont Starve MUD')
    while True:
        main()