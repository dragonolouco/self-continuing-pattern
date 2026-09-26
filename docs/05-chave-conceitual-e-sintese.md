# IA orientada por chaves conceituais

## Intuição

Uma forma de imaginar uma inteligência artificial é como um sistema que recebe uma chave e recupera ou constrói o conjunto de estruturas relacionadas a ela. A chave não precisa apontar para uma resposta pronta; ela pode apontar para conceitos, relações, métodos, restrições e verificações.

```text
chave -> conceitos relacionados -> métodos compatíveis -> execução -> resultado verificado
```

Exemplo:

```text
chave: jogo
  -> definição
  -> propriedades
  -> mecânicas
  -> gêneros
  -> relações com narrativa, regras e objetivo
```

## Recuperar não é apenas buscar texto

Existem três níveis de resposta:

1. **Consulta:** recuperar um fato ou relação já estruturado.
2. **Composição:** combinar conceitos e métodos existentes para uma entrada nova.
3. **Síntese:** criar uma nova sequência de operações, testar e armazenar se funcionar.

```text
se a chave tem método validado:
    executar método
senão se a chave tem componentes compatíveis:
    compor componentes e verificar
senão:
    sintetizar hipótese, testar e versionar
```

## Modelo de dados mínimo

```yaml
chave: jogo
conceitos:
  - atividade
  - regras
  - objetivo
  - mecânicas
relações:
  possui: [regras, objetivo, mecânicas]
  pode_ter: [terror, aventura, estratégia]
métodos:
  - explicar_conceito
  - comparar_generos
  - compor_frase_de_jogo
verificações:
  - conceitos_existentes
  - relações_compatíveis
```

## Gerar estruturas, não apenas respostas

Ao receber “crie um jogo de terror com exploração”, o sistema pode produzir uma especificação intermediária:

```yaml
entidade: jogo
restrições:
  gênero: terror
  mecânica_principal: exploração
saída_esperada:
  - regras
  - objetivo
  - progressão
  - ambientação
verificação:
  - gênero existe
  - mecânica existe
  - componentes são compatíveis
```

Depois disso, outro método pode gerar um documento de design, código ou plano. A saída nasce da composição; não precisa ter sido memorizada como frase exata.

## Evolução autônoma verificável

Um código pode aprender operacionalmente sem uma pessoa indicar cada passo:

```text
1. receber novos dados ou objetivo
2. identificar chaves e conceitos
3. buscar relações e métodos
4. executar uma composição
5. testar o resultado
6. registrar evidências
7. corrigir falhas
8. promover o método validado
9. reutilizar em novas entradas
```

“Autônomo” aqui significa que o ciclo de descoberta, teste e armazenamento pode ser executado pelo próprio sistema. Não significa que ele dispense dados, critérios de sucesso, recursos computacionais ou supervisão de segurança.

## Comparação com modelos generativos

| Aspecto | IA orientada por estruturas | Modelo generativo amplo |
|---|---|---|
| Resposta conhecida | consulta/executa método | gera uma sequência de saída |
| Tarefa determinística | regra e verificação | padrão aprendido ou ferramenta |
| Tarefa nova | compõe ou sintetiza | generaliza e propõe |
| Memória | conceitos, relações e métodos | parâmetros e/ou memória externa |
| Erro | diagnóstico estruturado | pode exigir nova inferência |
| Velocidade | potencialmente muito baixa latência em domínio fechado | depende do tamanho e do caminho de geração |

A comparação real deve ser medida por tarefa. Uma arquitetura estruturada pode ser muito mais rápida em consultas e operações formais, enquanto um modelo generativo pode ser superior em ambiguidade, percepção e descoberta aberta.

## Limite fundamental

Programar todas as variantes de um domínio pode produzir precisão e velocidade excepcionais dentro desse domínio, mas o custo de criar e manter a cobertura também cresce. A arquitetura reduz a necessidade de enumerar respostas; não elimina a necessidade de representar conceitos, dados, exceções e critérios de verificação.
