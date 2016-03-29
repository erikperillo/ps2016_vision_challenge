int main()
{
	//lendo a imagem de um dispositivo
	Matrix M = read_image();

	//você que dar o valor correto às duas variáveis
	//cone_x e cone_y sao os pontos x e y, respectivamente, do
	//do retangulo que encobre completamente o cone.
	int cone_x, cone_y;

	//bonus: de valor corretamente a variavel abaixo
	float hor_angle = 0.0;

	//----COMPLETE O CODIGO AQUI-----

	Matrix K = threshold(M, 255, 97, 27);

	/* Eu vou assumir aqui que um TAD lista foi implementado e
	Os exemplos estavam em Python, que suporta listas*/

    /*-------------AVALIADOR:--------------
	a lógica do canditato foi entendida, mas só porque essa era uma das 
	soluções pensadas pelos avaliadores. 
	um comentário no código abaixo seria bom.
	---------------/AVALIADOR--------------*/
	List blobs = blob(K);
	List aux = blobs;
	while (aux != NULL)
	{
		if(aux->w > aux->h)
			aux = aux->next;
		else break;
	}

	cone_x = aux->x;
	cone_y = aux->y;

	/*-------------AVALIADOR:--------------
	infelizmente, a lógica do desafio extra está errada.
	no enunciado é dito que o ângulo de visão horizontal é 75 graus.
	com a proposta a seguir, o ângulo pode ir de -90 graus a 90 graus, o 
	que implica um ângulo de visão de 180 graus.
	---------------/AVALIADOR--------------*/
    
	/* Assumindo a linha horizontal como a linha "cosseno" no
	circulo trigonometrico, precisamos normaliza-la de 0~640 para -1~+1.
	*/
	float normalizado = (cone_x/320)-1;

	/* Assumindo que a biblioteca <math.h> pode ser importada para
	usarmos a funcao acos() que se assemelha a funcao arccos na
	matematica.
	Tambem e possivel implementar uma aproximacao cubica rapida
	usando polinomiais de Lagrange que achei no google e da resultados
	extremamente precisos:
	float acos(x) {
		return (-0.69813170079773212 * x * x - 0.87266462599716477) * x + 
		1.5707963267948966;
	}*/
	hor_angle = acos(normalizado);

	/* Angulo positivo para direita do centroe negativo para a
	esquerda. Usei 1.58 como pi/2 porque floats sao literalmente a
	segunda vinda do anticristo e ia arredondar de qualquer jeito. */
	hor_angle = 1.58 - hor_angle;

	listFree(blobs);

	return 0;

	//-------------------------------

	/*-------------AVALIADOR:--------------
	considerações finais:
	código bem comentado, atacou o problema com uma solução boa
	e ao menos tentou fazer o problema extra.

	notas:
	solução do problema básico: 10.0
	clareza do código: 8.0
	problema extra: 1.0
	nota final: 0.7*10 + 0.3*8 + 0.1*1 = 9.5

    para uma sugestão de solução, veja o código solution.py no repositório:
    http://github.com/erikperillo/ps2016_vision_challenge
	---------------/AVALIADOR--------------*/
}
