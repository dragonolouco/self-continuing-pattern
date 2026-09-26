# Decomposição e resposta imediata

## A ideia

Esta arquitetura decompõe uma entrada em unidades menores e aplica uma estrutura já conhecida para chegar ao resultado. Quando o conhecimento fundamental, as regras e as verificações estão corretamente organizados, a resposta pode ser produzida com latência muito baixa — em alguns casos, por uma consulta ou uma sequência curta de transições.

```text
entrada grande
    -> decomposição
    -> unidades tipadas
    -> regra/método compatível
    -> cálculo das transições
    -> recomposição
    -> verificação
    -> resposta
```

A ferramenta executora não precisa inventar a solução inteira a cada vez. Ela recebe a estrutura correta, aplica os parâmetros da entrada e repete o procedimento quantas vezes forem necessárias.

## Precisão estrutural

A precisão vem de quatro condições:

1. **Conhecimento correto:** os fatos e primitives usados são válidos.
2. **Estrutura correta:** a decomposição representa o problema sem perder informação.
3. **Regra correta:** cada transição possui contrato e estado bem definidos.
4. **Verificação correta:** invariantes e resultado final são testados.

Quando essas condições são satisfeitas em um domínio fechado, a execução pode ser exata e repetível. A arquitetura não transforma dados errados ou uma regra errada em verdade: ela executa com precisão aquilo que foi formalizado.

## Reutilização em qualquer tamanho

A soma decimal demonstra a generalização:

```text
conhecer dígitos + transporte + ordem das casas
-> somar 10, 100 ou 1 trilhão de dígitos
```

O tamanho da entrada altera a quantidade de passos, não a identidade da regra. Esse padrão aparece em qualquer tarefa que possa ser expressa como uma sequência de estados e transições.

## Domínios aparentemente diferentes

Uma arquitetura pode existir mesmo quando ela ainda não foi explicitada. Exemplos possíveis:

- palavras: letras, posição, prefixos, sufixos e composição;
- significados: entidades, relações, contexto e restrições;
- programação: componentes, tipos, eventos e dependências;
- documentos: seções, referências, regras de validação e transformação;
- dados: registros, filtros, agrupamentos e agregações;
- erros: sintomas, causas, correções e variantes.

A tarefa do projeto é descobrir, formalizar e testar essas arquiteturas — não presumir que toda tarefa já está formalizada.

## Limite importante

“Resposta instantânea” aqui é um objetivo de engenharia, não uma promessa de tempo zero nem uma garantia universal para qualquer pergunta. Em tarefas abertas, o sistema pode precisar interpretar contexto, consultar conhecimento, resolver ambiguidades ou descobrir um método novo. A meta é que, depois de um método ser validado, tarefas semelhantes deixem de exigir reconstrução completa.

```text
descobrir uma vez
    -> estruturar
    -> verificar
    -> armazenar método
    -> reutilizar rapidamente
```
