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
