# Exercícios - Cap 1

## 1.1
__1. Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?__
_R: Não executa_

__2. Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?__
_R: SyntaxError_

__3. Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?__
_R: Operador Unário `2 + (+2)`, soma será `4`_

__4. Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no Python?__
_R: SyntaxError: python interpreta números que iniciam com 0 como base octal (base 8). Para resolver, podemos usar assim:`int('02') + int('03')`__

__5. O que acontece se você tiver dois valores sem nenhum operador entre eles?__
_R: Os valores concatenam, se juntam._

## 1.2
__1. Quantos segundos há em 42 minutos e 42 segundos?__
_R: `(42*60)+42` retorno = 2562_

__2. Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.__
_R: `10/1.161` retorno = 6.21_

