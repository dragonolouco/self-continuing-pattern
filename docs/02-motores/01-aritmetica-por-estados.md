# Aritmética por estados

## Soma

A execução percorre as casas da direita para a esquerda. Cada passo lê os dois algarismos e o transporte anterior, produz um algarismo e o novo transporte.

```text
para cada coluna da direita para a esquerda:
    total = a + b + transporte
    escrever total mod 10
    transporte = total // 10
se transporte > 0:
    escrever transporte
```

### Exemplo

```text
  5897
+ 7648
------
 13545
```

Transições locais:

```text
7 + 8 + 0 -> escreve 5, transporte 1
9 + 4 + 1 -> escreve 4, transporte 1
8 + 6 + 1 -> escreve 5, transporte 1
5 + 7 + 1 -> escreve 3, transporte 1
fim       -> escreve 1
```

## Subtração

Quando o algarismo disponível é menor que o algarismo subtraído, a coluna recebe 10 unidades e o estado de empréstimo é propagado para a próxima coluna.

```text
  532
- 178
-----
  354
```

## Multiplicação

Pode ser composta a partir de:

- produtos entre dígitos;
- transporte;
- deslocamento posicional;
- soma de linhas parciais.

## Divisão

Pode ser composta a partir de:

- comparação;
- escolha do quociente local;
- multiplicação;
- subtração;
- transporte do próximo algarismo.

## Escalabilidade

A regra não muda quando o número cresce. O custo cresce com o comprimento da entrada:

| Operação | Custo escolar aproximado |
|---|---:|
| Soma de `n` casas | `O(n)` |
| Subtração de `n` casas | `O(n)` |
| Multiplicação escolar de `n × m` casas | `O(nm)` |
| Consulta de tabela básica | `O(1)` |

“Instantâneo” significa que uma transição pode ser muito barata; não significa custo físico zero.
