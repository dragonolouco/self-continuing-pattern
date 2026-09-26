# Aplicações em outros domínios

## Programação por componentes

Pedido: “crie um botão que aumente um número e mostre o resultado”.

```text
interpretar
 -> componente: botão
 -> estado: número
 -> evento: clique
 -> ação: +1
 -> saída: texto

compor
 -> criar elemento
 -> criar estado
 -> registrar evento
 -> executar soma
 -> renderizar estado
 -> verificar ids, tipos e evento
```

O backend pode gerar JavaScript, Python, outra linguagem ou uma representação intermediária. A lógica estrutural permanece.

## Linguagem e consulta estruturada

Pergunta: “qual cidade do Brasil não tem a letra A?”

```text
entidade.tipo == cidade
entidade.país == Brasil
NOT contains(normalize(entidade.nome), "a")
```

A propriedade “não contém A” é derivada. Os fatos “Recife é uma cidade do Brasil” precisam vir de uma base, arquivo ou fonte externa.

### Países e letras como consulta instantânea

O mesmo padrão pode ser usado para uma categoria de países:

```text
categoria = país
campo = nome
operação = não contém
caractere = A
```

O algoritmo percorre a base, normaliza o nome e executa uma comparação de caracteres. Se a base e a regra estiverem corretas, o resultado é determinístico e exato para aquela base. A implementação executável está em [`src/text_engine.py`](../../src/text_engine.py), com testes para categorias, acentos e caracteres inválidos.

Esse mecanismo não precisa ter uma resposta pronta para cada pergunta. Ele reutiliza a mesma estrutura mudando apenas os parâmetros: país, cidade, palavra, documento ou código; contém, não contém, começa com ou termina com.

## Dados

Um pipeline de dados pode ser representado por:

```text
ler -> validar tipo -> filtrar -> transformar -> ordenar -> agregar -> verificar
```

A estrutura é reutilizável; os dados e os parâmetros mudam.

## Validação

```text
entrada -> normalizar -> verificar pré-condições -> executar -> validar pós-condições
```

Exemplos: divisor diferente de zero, campo obrigatório, limite numérico, categoria compatível e dependência disponível.

## Planejamento

Quando o estado do ambiente é observável, o sistema pode escolher uma sequência de ações por pré-condições e efeitos:

```text
objetivo: arquivo publicado
estado atual: arquivo existe, testes passam
método: empacotar -> verificar integridade -> publicar
```

## O que não é derivável apenas por regra local

- qualidade de vida sem métricas e dados;
- ironia e intenção sem contexto;
- fatos que não estão na base;
- percepção visual ou auditiva complexa;
- problemas cuja definição muda durante a execução.

Nesses casos, a arquitetura precisa consultar conhecimento externo, usar um modelo aprendido ou entrar em modo de descoberta.
