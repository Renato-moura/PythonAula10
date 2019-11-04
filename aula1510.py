import random
from collections import Counter
from matplotlib import pyplot as plt
import math
 
def quantidade_de_usuarios_na_rede ():
    return 10
 
def contem (amizade, amizades):
    for e1, e2 in amizades:
        if (amizade[0] == e1 and amizade[1] == e2) or (amizade[0] == e2 and amizade[1] == e1):
            return True
    return False
 
def gera_amizades (numero_conexoes_desejado, qtde_usuarios_na_rede):
    conexoes = []
    for _ in range (numero_conexoes_desejado):
        u1 = None
        u2 = None
        while u1 == u2 or contem ((u1, u2), conexoes):
             u1 = random.randint (0, qtde_usuarios_na_rede - 1)
             u2 = random.randint (0, qtde_usuarios_na_rede - 1)
             #if u1 != u2:
             #    conexoes.append((u1, u2))
        else:
            conexoes.append ((u1, u2))
    return [x for x in set(conexoes)]
 
def test_gera_amizades ():
    print(gera_amizades(6, quantidade_de_usuarios_na_rede()))
 
 
def quantidade_de_amigos(amizades):
    a = Counter (i for i, _ in amizades)
    b = Counter (i for _, i in amizades)
    tudo = a + b
    #print ("a", a, '\n')
    #print ("b", b, '\n')
    #print ("tudo", tudo, '\n')
    #print ("values", tudo.values())
    res = Counter (x for x in tudo.values())
    #print ("res", res)
    return res
 
def test_quantidade_de_amigos ():
    amizades = gera_amizades (8, quantidade_de_usuarios_na_rede())
    quantidade_de_amigos(amizades)
 
def gera_histograma_contagem_amigos (quantidade_de_amigos, qtde_usuarios_na_rede):
    xs = range (qtde_usuarios_na_rede)
    ys = [quantidade_de_amigos[x] for x in xs]
    plt.bar(xs, ys)
    plt.axis ([0, qtde_usuarios_na_rede, 0, qtde_usuarios_na_rede])
    plt.title ("Histograma de contagem de amigos")
    plt.xlabel ("Número de amigos")
    plt.ylabel ("Número de pessoas")
    plt.show()
 
def test_gera_histograma_contagem_amigos ():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades (30, qtde_usuarios)
    qtde_amigos = quantidade_de_amigos (amizades)
    gera_histograma_contagem_amigos (qtde_amigos, qtde_usuarios)
 
def mostra_primeiro_e_segundo_maior (qtde_amigos):
    lista = sorted (qtde_amigos.values())
    print ("Maior: " + str (lista[len(lista) - 1]))
    print ("Segundo maior: " + str (lista[-2]))
 
def test_mostra_primeiro_e_segundo_maior ():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades (30, qtde_usuarios)
    qtde_amigos = quantidade_de_amigos (amizades)
    mostra_primeiro_e_segundo_maior (qtde_amigos)
 
def media_qtde_amigos (qtde_amigos):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    return sum (so_qtdes) / sum (x for x in qtde_amigos.values())
 
def test_media_qtde_amigos ():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades (30, qtde_usuarios)
    qtde_amigos = quantidade_de_amigos (amizades)
    print(media_qtde_amigos (qtde_amigos))
 
 
def mediana_qtde_amigos (qtde_amigos):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    ordenada = sorted (so_qtdes) # O(n lg n)
    print ("ordenada", ordenada)
    meio = len (ordenada) // 2
    return ordenada[meio] if len (ordenada) % 2 == 1 else (ordenada[meio] + ordenada[meio - 1]) / 2
 
def test_mediana_qtde_amigos ():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades (15, qtde_usuarios)
    qtde_amigos = quantidade_de_amigos (amizades)
    #print (qtde_amigos)
    print ("mediana: ", mediana_qtde_amigos(qtde_amigos))
 
def quantile (qtde_amigos, percentual):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    indice = int (percentual * len (so_qtdes))
    l = sorted (so_qtdes)
    print (l)
    return l[indice]
 
 
def test_quantile ():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades (15, qtde_usuarios)
    qtde_amigos = quantidade_de_amigos (amizades)
    print (quantile (qtde_amigos, 0.8))
 
def moda_qtde_amigos (qtde_amigos):
    moda = max (qtde_amigos.values())
    print (qtde_amigos)
    return [x for x, count in qtde_amigos.items() if count == moda]
 
def test_moda_qtde_amigos ():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades (15, qtde_usuarios)
    qtde_amigos = quantidade_de_amigos (amizades)
    print ("moda", moda_qtde_amigos(qtde_amigos))
 
def amplitude_dos_dados (qtde_amigos):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    print (so_qtdes)
    return max (so_qtdes) - min(so_qtdes)
 
def test_amplitude_dos_dados ():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades (15, qtde_usuarios)
    qtde_amigos = quantidade_de_amigos (amizades)
    print ("amplitude", amplitude_dos_dados(qtde_amigos))
 
def diferencas_em_relacao_a_media (qtde_amigos):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    #print ("so_qtdes", so_qtdes)
    media = media_qtde_amigos(qtde_amigos)
    print ("media", media)
    return [x - media for x in so_qtdes]
 
def test_diferencas_em_relacao_a_media ():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades (15, qtde_usuarios)
    qtde_amigos = quantidade_de_amigos (amizades)
    print("diferencas", diferencas_em_relacao_a_media (qtde_amigos))
 
def soma_dos_quadrados (diferencas):
    l = [x ** 2 for x in diferencas]
    print ("diferencas", diferencas)
    print ("quadrados", l)
    return sum (l)
 
def test_soma_dos_quadrados ():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades (15, qtde_usuarios)
    qtde_amigos = quantidade_de_amigos (amizades)
    diferencas = diferencas_em_relacao_a_media (qtde_amigos)
    print ('soma dos quadrados', soma_dos_quadrados(diferencas))
 
 
def variancia (qtde_amigos):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    return (soma_dos_quadrados (diferencas_em_relacao_a_media(qtde_amigos))) / (len (so_qtdes) - 1)
 
def test_variancia ():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades (15, qtde_usuarios)
    qtde_amigos = quantidade_de_amigos (amizades)
    print ('variancia', variancia(qtde_amigos))
 
def desvio_padrao (qtde_amigos):
    return math.sqrt (variancia(qtde_amigos))
 
def test_desvio_padrao ():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades (15, qtde_usuarios)
    qtde_amigos = quantidade_de_amigos (amizades)
    print ("desvio padrão", desvio_padrao(qtde_amigos))
 
def main ():
    test_desvio_padrao()
    #test_variancia()
    #pass
    #test_gera_amizades()
    #test_quantidade_de_amigos()
    #test_gera_histograma_contagem_amigos()
    #test_mostra_primeiro_e_segundo_maior()
    #test_media_qtde_amigos()
    #test_mediana_qtde_amigos()
    #test_quantile()
    #test_moda_qtde_amigos()
    #test_amplitude_dos_dados()
    #test_diferencas_em_relacao_a_media()
    #test_soma_dos_quadrados()
 
 
main()
 