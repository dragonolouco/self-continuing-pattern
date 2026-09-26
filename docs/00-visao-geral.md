# Visão geral

## Tese

Muitos problemas grandes são sequências de microproblemas pertencentes a um conjunto pequeno de tipos. Se o sistema conhece as primitivas, as regras de transição e a forma de atualizar o estado, ele pode resolver entradas novas sem armazenar cada resposta.

## Exemplo mínimo: soma decimal

Para cada coluna, a máquina recebe três valores:

```text
algarismo A ∈ {0..9}
algarismo B ∈ {0..9}
transporte ∈ {0, 1}
```

A transição é:

```text
total = A + B + transporte
escrito = total mod 10
novo_transporte = floor(total / 10)
```

Há `10 × 10 × 2 = 200` combinações locais. A soma de números com 100, 11 milhões ou 1 trilhão de dígitos não cria novas regras: repete a mesma transição em mais colunas.

## Conhecimento não é uma coisa única

1. **Fundamental:** símbolos, tipos, fatos e operações primitivas.
2. **Procedural:** ordem das etapas, pré-condições e pós-condições.
3. **Derivado:** propriedades calculadas quando necessárias.
4. **Experiencial:** métodos que funcionaram e padrões de erro corrigidos.
5. **Externo:** dados que o sistema ainda não possui e precisa consultar.

## Estrutura versus resposta

Uma resposta memorizada associa diretamente um problema a uma saída. Uma estrutura memorizada descreve como transformar uma família de entradas:

```text
resposta isolada:       entrada X -> saída Y
estrutura reutilizável: tipo + estado + regra + composição -> muitas saídas
```

## Aprender sem guardar tudo

Neste projeto, aprender pode significar:

- descobrir uma decomposição;
- testar uma sequência de regras;
- verificar o resultado;
- transformar a sequência em método parametrizado;
- registrar a causa de falhas e a condição preventiva;
- reconhecer variantes do mesmo padrão em futuras entradas.

A memória deve guardar o que aumenta a capacidade futura, não todo o histórico bruto.

## Ciclo de execução

```text
observar -> interpretar -> decompor -> executar -> verificar
    ^                                             |
    |----------- registrar método/erro -----------|
```

## Princípio de escopo

A abordagem é mais forte quando há regras estáveis, tipos claros, estados observáveis e resultados verificáveis. Ela é menos suficiente quando a tarefa depende de contexto implícito, percepção, preferências subjetivas ou conhecimento externo incompleto.
