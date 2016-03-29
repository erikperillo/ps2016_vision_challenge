import math # uso do método atan

def main():
    #lendo a imagem de um dispositivo
    M = read_image()

    #você tem que dar o valor correto às duas variáveis abaixo.
    #cone_x e cone_y são os pontos x e y, respectivamente, do centro
    #do retângulo que encobre completamente o cone.
    cone_x, cone_y = 0, 0

    #bônus: dê valor corretamente à variável abaixo
    hor_angle = 0.0

    #----COMPLETE O CÓDIGO AQUI-----

    # Torna branco os pixels originalmente laranja e os outros ficam pretos
    M = threshold(M, 255, 97, 27)

    # atribui os pontos dos retângulos que cercam as manchas brancas da matriz M
    points = blob(M)

    for point in points:
        x, y, w, h = point

        """
        Analisando a imagem, percebemos que o cone logicamente
        tem a altura (h) maior que a base (w). Já os garis, têm a base (w)
        muito maior que a altura (h). Dessa forma, podemos diferenciá-los
        achando qual é o maior lado, a base ou a altura.
        """
        #-------------AVALIADOR:--------------
        #é algo válido de se assumir.
        #um detalhe, porém, é que vocês continuam o loop de forma desnecessária
        #se encontram um cone que satisfaz a condição.
        #como o problema dizia para assumir que havia apenas um cone, podia-se
        #colocar um break na condição abaixo.
        #-------------/AVALIADOR--------------

        if h > w: # altura maior que a base, logo é cone.
            cone_x = x + (w/2) # eixo x é o canto superior esquerdo mais a metade da largura
            cone_y = y + (h/2) # eixo y é o canto superior esquerdo mais a metade da altura

    #---- Parte extra do algoritmo

    # encontrando o centro da imagem
    centro_x = 640/2
    centro_y = 480/2

    """
    Por relações de trigonometria, temos que a tangente do hor_angle é
    (cone_y - centro_y) / (centro_x - cone_x) levando em conta um ângulo
    positivo entre 0 e Pi/2. Dessa forma, temos que hor_angle é o arco tangente
    dessa relação.
    """
    
    #-------------AVALIADOR:--------------
    #isso está incorreto, o objetivo era achar o ângulo HORIZONTAL
    #entre o centro do cone e o centro da imagem.
    #-------------/AVALIADOR--------------
    tan = (cone_y - centro_y) / (cone_x - centro_x)

    if tan < 0: # tangente negativa
        hor_angle = math.atan(-tan)
    else:
        hor_angle = math.atan(tan)

    #-------------------------------

    #-------------AVALIADOR:--------------
    #considerações finais:
    #código bem comentado, atacou o problema com uma solução boa, 
    #ao menos tentou fazer o problema extra.

    #notas:
    #solução do problema básico: 9.0
    #clareza do código: 9.5
    #problema extra: 1.0
    #nota final: 0.7*9 + 0.3*9.5 + 0.1*1 = 9.25

    #para uma sugestão de solução, veja o código solution.py no repositório:
    #http://github.com/erikperillo/ps2016_vision_challenge
    #-------------/AVALIADOR--------------
if __name__ == "__main__":
    main()
