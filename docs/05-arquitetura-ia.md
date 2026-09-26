# Arquitetura de IA baseada em estruturas

## Hipótese

Um sistema voltado a tarefas estruturadas pode ser menor e mais rápido quando não usa um modelo grande para reconstruir toda resposta. Ele pode reservar o modelo aprendido para interpretação ambígua, percepção, priorização ou descoberta.

A afirmação correta é condicional: o ganho depende da tarefa, dos dados, do hardware e da qualidade das implementações. Não existe garantia universal de ser mais rápido que qualquer outro modelo.

## Arquitetura híbrida

```text
entrada do usuário
      |
      v
interpretador semântico leve
      |
      v
classificador/roteador de tarefa
      |
      +--> regra determinística --> motor de métodos
      |
      +--> consulta estruturada --> base/índice
      |
      +--> método conhecido --> executor verificado
      |
      +--> tarefa aberta --> modelo aprendido ou descoberta
                                      |
                                      v
                                  compositor
                                      |
                                      v
                                  execução
                                      |
                                      v
                                  verificação
                                      |
                                      v
                       memória de método ou de erro
```

## O que o modelo aprendido faz

- interpretar linguagem natural;
- identificar intenção, entidades e restrições;
- buscar o método compatível;
- propor decomposições quando nenhuma existe;
- reconhecer padrões de erro e variantes;
- consultar fontes externas;
- pedir informação faltante.

## O que o motor determinístico faz

- calcular;
- manipular estruturas tipadas;
- executar loops e transições;
- aplicar contratos;
- validar invariantes;
- produzir rastreamento auditável;
- repetir métodos sem variação desnecessária.

## Pesos úteis versus pesos inúteis

O objetivo não é simplesmente “ter poucos pesos”. É reduzir parâmetros usados para tarefas que possuem solução explícita. Pesos continuam úteis para generalização, percepção e ambiguidade. A otimização consiste em direcionar cada subproblema para o mecanismo adequado.

## Resposta rápida sem pensamento improdutivo

Uma estrutura de roteamento pode evitar geração longa quando já existe um caminho validado:

```text
se método confiável existe:
    executar diretamente
senão se composição conhecida existe:
    compor e verificar
senão:
    descobrir método, testar e armazenar
```

Isso substitui recomputação por recuperação de procedimento, mas o custo de interpretar, consultar dados e verificar ainda existe.

Para a formulação detalhada de decomposição, precisão estrutural e resposta imediata, consulte [`docs/01-fundamentos/02-decomposicao-resposta-instantanea.md`](01-fundamentos/02-decomposicao-resposta-instantanea.md).

## Segurança epistemológica

Toda resposta deve indicar, internamente:

- origem dos dados;
- método usado;
- pré-condições verificadas;
- invariantes testadas;
- confiança e limitações;
- se houve descoberta ou apenas reutilização.
