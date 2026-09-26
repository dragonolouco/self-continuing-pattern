# Camada de palavras e significados

## Ideia

A camada de letras identifica caracteres. A camada seguinte identifica palavras como unidades com significado, tipo, propriedades e relações. Uma frase é composta por essas unidades, mas o significado final não deve ser obtido apenas somando definições isoladas: a ordem, as relações, os modificadores e o contexto também fazem parte da estrutura.

```text
letras
  -> tokens
  -> palavras/conceitos
  -> atributos e relações
  -> cadeia de conceitos
  -> contexto da frase
  -> intenção ou resposta
```

## O que guardar para cada palavra

Uma entrada mínima pode conter:

```yaml
palavra: jogo
conceito: atividade estruturada
categoria: entretenimento
atributos:
  - possui regras
  - possui objetivo
  - possui mecânicas
relações:
  - possui -> mecânica
  - pode_ter -> gênero
  - pode_ter -> narrativa
```

A palavra não precisa carregar todas as frases possíveis. Ela precisa apontar para um conceito estruturado e para as operações que permitem explorar esse conceito.

## Cadeias e subcadeias de conceitos

Pergunta: “o que é um jogo?”

```text
jogo
  -> é uma atividade
  -> possui regras
  -> possui objetivo
  -> possui mecânicas
       -> interação
       -> progressão
       -> combate
       -> exploração
  -> pode pertencer a gêneros
       -> terror
       -> aventura
       -> estratégia
```

Cada seta é uma relação consultável. Uma subcadeia pode ser explorada sem reconstruir todo o conhecimento:

```text
jogo -> possui -> mecânicas -> exploração
jogo -> pode_ter -> gênero -> terror
```

## Composição de frase

Frase:

> “jogo de terror com exploração”

Decomposição:

```text
jogo        -> conceito principal
 de terror  -> gênero/modificador
 com exploração -> mecânica/atributo
```

Representação intermediária:

```json
{
  "entidade": "jogo",
  "gênero": "terror",
  "mecânica": "exploração"
}
```

A mesma arquitetura pode representar “documento de política com seção de segurança” ou “programa com evento de clique”: o domínio muda, mas a composição de entidade, relação e modificador permanece.

## Contexto além das palavras isoladas

O contexto é uma camada de restrições que seleciona entre significados possíveis. A palavra “banco” pode representar uma instituição financeira ou um assento. A frase, as palavras próximas e o objetivo da consulta restringem a interpretação.

```text
palavra isolada -> candidatos de significado
frase           -> relações e restrições
contexto        -> significado selecionado
verificação     -> coerência com a base e a tarefa
```

## O que é aprendido e o que é calculado

- o léxico e as relações podem ser armazenados como conhecimento estruturado;
- a cadeia pode ser percorrida sob demanda;
- a frase pode ser decomposta por regras e analisadores;
- novos conceitos e relações podem ser descobertos, testados e incorporados;
- ambiguidades exigem contexto, exemplos, fonte externa ou um modelo aprendido.

Assim, o sistema pode saber muito por composição sem memorizar todas as respostas textuais. A precisão depende da cobertura e da correção do conhecimento, da análise da frase e das regras de composição.

## Protótipo

[`src/word_engine.py`](../../src/word_engine.py) implementa uma versão pequena dessa ideia: conceitos, relações, exploração de cadeia e composição determinística de uma frase de jogo. Ele é deliberadamente explícito para que cada conclusão possa ser auditada.
