# <- este simbolo e tido como um comentário.

#lendo a imagem de um dispositivo

M = ler_imagem

#você tem que dar o valor correto às duas variáveis abaixo.

#cone_x e cone_y são os pontos x e y, respectivamente, do centro

#do retângulo que encobre completamente o cone.

cone_x = 0

cone_y = 0

#bônus: de valor corretamente a variável abaixo

hor_angulo = 0.0

MT= threshold(M,255,97,27)

#produz uma matriz onde toda imagem com valor RGB 255,97,27(laranja) é convertida para branco e o
#restante para preto.

points = blob(MT)

cone_p = 0, 0, 0, 0 # ponto vazio.

for point in points: # passa por todos os pontos retornados.
    x, y, w, h = point # pega coordenadas do ponto.
    cx, cy, cw, ch = cone_p # coordenadas do ponto do retângulo do #cone.

    #-------------AVALIADOR:--------------
    #se entendi bem, o propósito era achar o objeto com a menor largura,
    #assumindo que o cone teria sempre largura menor que a dos garis.
    #embora eu considere válido, isso é uma hipótese fraca.
    #o cone pode estar à frente dos garis. 
    #assim, ele seria maior na imagem e sua largura poderia então ser maior
    #que a dos garis.
    #-------------/AVALIADOR--------------
    if w < cw or cw == 0: # testa se tem largura menor q o ponto do retângulo do cone, ou se o
    #ponto do retângulo do cone é vazio.
        cone_p = point

    #-------------AVALIADOR:--------------
    #não entendi o porquê de checar essa condição.
    #um comentário nessa parte era necessário.
    #-------------/AVALIADOR--------------
    if w == cw and h > ch:
        cone_p = point
    end if

    end if

#-------------AVALIADOR:--------------
#pedantismo: variável escrita errado.
#-------------/AVALIADOR--------------
cone_x = cx+(cw/2)#define o centro do retângulo do cone.
Cone_y = cy+(ch/2)


#-------------AVALIADOR:--------------
#considerações finais:
#a solução não foi das melhores, a hipótese é fraca.
#a indentação do código ficou um pouco confusa.
#algumas partes com operações não claras não foram comentadas.

#notas:
#solução do problema básico: 6.0
#clareza do código: 5.0
#problema extra: 0.0
#nota final: 0.7*6 + 0.3*5 + 0.1*0 = 5.7

#para uma sugestão de solução, veja o código solution.py no repositório:
#http://github.com/erikperillo/ps2016_vision_challenge
#-------------/AVALIADOR--------------

