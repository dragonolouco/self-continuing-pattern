# Arquitetura universal por camadas

## Princípio

A proposta do projeto é investigar se qualquer domínio computável pode ser organizado como uma arquitetura de decomposição. O domínio muda, mas a forma geral permanece:

```text
camada de símbolos
    -> unidades e caracteres
    -> tipos e categorias
    -> entidades e atributos
    -> relações e restrições
    -> regras de transformação
    -> estado intermediário
    -> composição de métodos
    -> verificação
    -> resposta
```

Isso não significa que toda pergunta já possua uma regra pronta. Significa que, quando seus elementos e relações podem ser formalizados, ela pode ser transformada em uma sequência executável e verificável.

## Exemplo: países e letras

Pergunta:

> Qual país não contém a letra `A`?

A arquitetura não precisa armazenar uma resposta pronta para cada variação. Ela recebe:

```text
categoria = país
atributo = nome
operação = não contém
caractere = A
base = lista de países
```

E executa:

```text
para cada entidade na base:
    se entidade.categoria == "país":
        nome = normalizar(entidade.nome)
        se "a" não está em nome:
            adicionar entidade ao resultado
```

A mesma estrutura responde, trocando parâmetros:

- cidade sem a letra `E`;
- país que começa com `B`;
- palavra que termina em `ção`;
- documento que contém uma seção específica;
- código que possui uma chamada de função;
- registro que satisfaz duas condições.

## Por que a resposta pode ser imediata

Depois que a base, a operação e a estrutura estão carregadas, a execução é uma comparação direta por elemento. Não há geração probabilística de uma explicação a cada consulta. A latência depende principalmente do tamanho da base, do índice e da implementação.

Para bases pequenas, isso pode parecer instantâneo. Para bases grandes, índices e pré-processamento podem reduzir a busca. A precisão é exata **em relação à base fornecida, à normalização escolhida e à regra implementada**.

## Camadas para significados

Letras e caracteres são a camada mais simples. Para significados, a arquitetura pode crescer:

```text
letras -> tokens -> palavras -> entidades -> relações -> contexto -> intenção -> ação
```

Cada camada precisa declarar o que conhece e como verifica suas conclusões. “Recife contém a letra R” é uma comparação direta. “Recife é uma cidade” depende de conhecimento estruturado. “Recife é a melhor escolha” depende de critérios, dados e definição de melhor.

Para palavras, uma cadeia pode ser expandida sem abandonar a mesma arquitetura:

```text
palavra -> conceito -> atributos -> relações -> subcadeias -> contexto -> interpretação
```

Exemplo: `jogo -> possui -> mecânicas -> exploração` e `jogo -> pode_ter -> gênero -> terror`. A frase combina essas relações em uma representação intermediária, em vez de depender de uma resposta memorizada para cada frase possível. Consulte [`docs/03-aplicacoes/02-camada-de-palavras-e-significados.md`](../03-aplicacoes/02-camada-de-palavras-e-significados.md).

## Regra geral

```text
se o domínio possui representação,
   operações,
   estado,
   composição e
   critério de verificação,
então ele pode ser transformado em um método executável.
```

Quando algum desses elementos falta, o sistema entra em modo de descoberta, consulta uma fonte externa ou solicita informação adicional.
