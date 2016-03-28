Primeira solução: 
A hipótese é válida, mas fraca. Os garis podem estar com o braço de modo tal que
ele não esteja cercado por laranja.

comentários por linhas:
-linha 5:
Por que criar variáveis com uma só letra e, além do mais, sem comentários
explicando-as?

-linha 41:
O compilador não sabe pra onde seu ponteiro está apontando.
Calcular sizeof dessa maneira vai lhe dar o tamanho do apontador duplo, e não
do vetor. Ou seja, você vai ter um valor constante que provavelmente está
entre 4 e 8 bytes.

-linha 51:
O cálculo está errado. o certo seria:
hor_angle = atan((2*(ximg/2 - cone_x)/ximg)*tan((75/2)*3.1416/180));
(você esqueceu de multiplicar por dois o primeiro termo).

Segunda solução:
Essa hipótese é fraca, pois isso não é dito e basta um pixel para que o 
tamanho seja diferente.

comentários por linhas:
-linha 23:
Novamente, o problema do sizeof em ponteiros. Estou atentando a esses problemas
pois escolher uma linguagem real implica em ter que usá-la corretamente.

-linha 43:
Esse else é desnecessário, pois ele acontece somente se os valores de
wbef e hbef já forem w e h, respectivamente.

-linha 48:
O cálculo está errado. o certo seria:
hor_angle = atan((2*(ximg/2 - cone_x)/ximg)*tan((75/2)*3.1416/180));
(você esqueceu de multiplicar por dois o primeiro termo).

Comentários finais:
As hipóteses são válidas, mas fracas.
A nomeação de variáveis poderia ter sido melhor. O código poderia ter sido 
melhor comentado, também.
Fora o pequeno erro no desafio extra, o pensamento está correto.

Notas:
Solução para o problema básico: 7.0
Clareza do código: 5.5
Problema extra: 9.0
Nota final: 0.7*7.0 + 0.3*5.5 + 0.1*9 = 7.45

Para uma sugestão de solução, veja o código solution.py no repositório: 
http://github.com/erikperillo/ps2016_vision_challenge  
