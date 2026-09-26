# Primitivas, estado e composição

## Primitivas

Uma primitiva é uma operação pequena, testável e com contrato explícito.

| Categoria | Exemplos |
|---|---|
| Símbolo | dígito, letra, byte, token |
| Tipo | número, texto, lista, entidade, booleano |
| Lógica | condição, comparação, repetição |
| Estado | valor atual, transporte, resto, contexto |
| Dados | ler, filtrar, ordenar, agrupar |
| Interface | botão, campo, texto, painel |
| Integração | arquivo, rede, banco, API |

## Estado

O estado impede que a execução perca a sequência. Exemplos:

- soma: transporte;
- subtração: empréstimo;
- divisão: resto e posição atual;
- programa: elementos criados e dependências;
- consulta: entidade, filtros e fonte ativa;
- diagnóstico: padrão reconhecido e correção aplicada.

Um método deve declarar seu estado inicial, as transições permitidas e o estado final esperado.

## Composição

```text
método composto = primitivas + ordem + dados intermediários + verificações
```

Exemplo de contador de interface:

```text
BOTÃO + ESTADO NUMÉRICO + EVENTO CLICK + SOMA + ATUALIZAÇÃO DE TEXTO
```

O sistema não precisa gerar cada linha de cada projeto do zero se esses componentes possuírem contratos compatíveis.

## Contratos

```yaml
metodo: incrementar_contador
entrada:
  - nome: contador
    tipo: inteiro
  - nome: passo
    tipo: inteiro
pre_condicoes:
  - contador existe
  - passo existe
pos_condicoes:
  - resultado = contador + passo
  - nenhum valor original é alterado por acidente
verificacao:
  - resultado - contador == passo
```

## Verificação e invariantes

A execução deve verificar propriedades que sempre precisam ser verdadeiras. Em soma decimal:

```text
0 <= escrito <= 9
novo_transporte ∈ {0, 1}
valor_reconstruído = valor_A + valor_B
```

Uma regra errada pode produzir resultados consistentes, por isso os testes devem verificar tanto exemplos quanto invariantes.
