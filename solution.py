# -*- coding: utf-8 -*-
#abaixo segue uma possível solução para o case da visão.

PI = 3.1415926536

"""converte de graus para radianos."""
def deg_to_rad(deg):
    return (deg/180.)*PI 

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

    #definição da cor laranja rgb
    orange_rgb = (255, 97, 27)

    #dimensões da imagem
    width, height = 640, 480

    #ângulo de visão
    hor_vision_angle = deg_to_rad(75.)

    #constante que converte pixels para radianos
    hor_pix_to_rad = hor_vision_angle/width

    #adquirindo imagem binária
    M_thr = threshold(orange_rgb)

    #adquirindo coordenadas das manchas laranjas
    points = blob(M_thr)
    #iterando sobre os pontos.
    #se o retângulo tem a altura maior que a largura, então é um cone,
    #pois os garis só deitam na horizontal.
    for point in points:
        x, y, w, h = point
        if h > w:
            cone_x = x + w/2
            cone_y = y + h/2 
            break

    #bônus: obtendo o ângulo do objeto com o centro da imagem
    hor_angle = (cone_x - width/2)*hor_pix_to_rad

    return cone_x, cone_y, hor_angle

    #-------------------------------
    
if __name__ == "__main__":
    main()
