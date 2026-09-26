# Ciência e arquiteturas relacionadas

A proposta deste repositório se aproxima de várias linhas de pesquisa, mas não é idêntica a nenhuma delas. O ponto comum é substituir respostas isoladas por representações, regras, relações, procedimentos e verificações reutilizáveis.

## 1. IA simbólica e sistemas especialistas

IA simbólica representa parte do conhecimento explicitamente em símbolos, lógica, regras ou estruturas relacionais e usa algoritmos para manipulá-los. Sistemas especialistas são aplicações orientadas a um domínio que raciocinam sobre conhecimento simbólico e usam inferência heurística; não existe uma única definição que cubra todos os sistemas especialistas [1] [2].

O `self-continuing-pattern` se aproxima dessa tradição ao separar conhecimento fundamental, métodos, estado e executor. A diferença é que este projeto dá ênfase operacional a decompor a entrada, repetir transições locais, verificar invariantes e registrar erros reutilizáveis.

A representação explícita ajuda na inspeção e na explicação, mas não garante que a base esteja correta ou completa. Uma implementação pode ser incompleta ou não-sólida em relação à formalização que pretendia executar [2].

## 2. Grafos de conhecimento e ontologias

RDF representa afirmações como triplas `sujeito–predicado–objeto`; triplas conectadas formam um grafo de relações consultável [3]. OWL 2 acrescenta classes, propriedades, indivíduos e uma semântica formal para ontologias; reasoners podem consultar consequências implícitas de uma ontologia [4]. SHACL valida um grafo contra shapes e produz relatórios de conformidade, mas validação não é o mesmo que inferência [5].

Essa linha é especialmente relevante para a camada de palavras:

```text
palavra -> conceito -> relação -> subcadeia -> contexto
```

Uma integração futura pode usar o grafo para conhecimento declarativo e manter a execução procedural no código:

```text
RDF/OWL -> fatos, tipos e relações
SPARQL  -> consultas e caminhos
SHACL   -> contratos estruturais
motor   -> estado, método, transições e verificação comportamental
```

O grafo não deve carregar sozinho toda a máquina de estados. Ele pode localizar conceitos e métodos compatíveis; o executor continua responsável por aplicar transições e gerar rastros verificáveis.

## 3. Síntese de programas e composição

Síntese de programas procura derivar uma implementação a partir do comportamento desejado. A especificação pode ser lógica, uma coleção de exemplos ou outra forma de restrição. Em programação por exemplos, poucos exemplos podem deixar várias hipóteses compatíveis; por isso, a solução precisa de busca, ranking, interação ou verificação adicional [6] [7].

A síntese guiada por sintaxe restringe o espaço de candidatos por uma gramática e verifica se o candidato satisfaz a especificação. A arquitetura CEGIS alterna geração, verificação e contraexemplos para refinar a busca [6] [8]. Isso corresponde diretamente ao ciclo proposto neste projeto:

```text
gerar/compor método
    -> executar em casos
    -> verificar
    -> coletar falhas
    -> corrigir ou restringir
    -> repetir
```

A composição de componentes pode ser guiada por tipos, assinaturas e pré-condições. Isso transforma o catálogo de primitivas do repositório em um espaço de busca menor e mais seguro.

## 4. Arquiteturas cognitivas

Arquiteturas cognitivas estudam uma infraestrutura relativamente estável de memória, representação, seleção e aprendizagem. ACT-R separa memória declarativa de fatos e memória procedural de produções; buffers representam o estado atual, e um pattern matcher seleciona uma produção compatível [9].

Soar trabalha com memória de trabalho, regras de produção, operadores e subestados. Quando surge um impasse, o sistema pode decompor o problema; seu mecanismo de chunking aprende uma nova produção que resume uma solução de submeta e pode permitir que uma situação semelhante seja resolvida em um passo no futuro [10].

A analogia mais próxima com este projeto é:

```text
produção/chunk -> método reutilizável
memória de trabalho -> estado intermediário
episódio/erro -> experiência estruturada
impasse -> modo de descoberta
```

A analogia não demonstra que este repositório seja uma arquitetura cognitiva validada. O repositório ainda é um protótipo de engenharia e precisa de experimentos próprios.

## 5. IA neuro-simbólica

IA neuro-simbólica combina componentes que aprendem representações com regras, lógica, programas ou relações explícitas. DeepProbLog integra predicados neurais a programação lógica probabilística [11]. Logic Tensor Networks usa lógica de primeira ordem diferenciável para transformar axiomas em objetivos de aprendizagem [12]. Scallop usa uma linguagem declarativa baseada em Datalog com modos discreto, probabilístico e diferenciável e integração com pipelines de aprendizado [13].

Essa linha sugere uma divisão de trabalho para o projeto:

```text
modelo aprendido -> percepção, linguagem ambígua, entidades e hipóteses
conversor tipado -> origem, confiança, evidência e versão
motor estruturado -> regras, estado, composição e execução
verificador -> invariantes, contratos, testes e proveniência
memória -> métodos, erros, variantes e rollback
```

Probabilidade alta não deve ser tratada como prova. Uma hipótese produzida por um modelo precisa ser marcada como hipótese e passar por validação antes de alterar a memória confiável.

## 6. Aprendizagem contínua e adaptação

Aprendizagem contínua estuda como aprender novas tarefas sem perder excessivamente o conhecimento anterior. Em redes neurais, o esquecimento catastrófico é uma dificuldade conhecida; Elastic Weight Consolidation é uma técnica que restringe alterações em parâmetros importantes para tarefas anteriores [14].

Neste projeto, o equivalente estrutural é controlar a evolução da memória de métodos:

```text
novo método -> testes novos -> regressão antiga -> promoção versionada
falha       -> diagnóstico -> correção isolada -> rollback se necessário
```

O projeto não precisa assumir que toda adaptação deve ocorrer em pesos. Ela pode ocorrer em métodos, relações, chaves, regras e políticas de seleção. Porém, esses artefatos também podem regredir e precisam de versionamento, validade, evidência e reversão.

## Arquitetura recomendada para o próximo estágio

```text
1. Memória de trabalho
   estado tipado da tarefa atual

2. Base declarativa
   fatos, conceitos, relações, fontes e versões

3. Catálogo procedural
   primitivas, métodos, contratos e custos

4. Roteador por chave
   domínio, tipos, objetivo, contexto e restrições

5. Compositor/sintetizador
   consulta, composição ou descoberta

6. Executor
   transições, efeitos e rastreamento

7. Verificador
   invariantes, testes, shapes e propriedades

8. Memória experiencial
   acertos, erros, contraexemplos, correções e variantes

9. Governança da adaptação
   evidência, confiança, versionamento, quarentena e rollback
```

## Conclusão técnica

A pesquisa apoia a ideia de que existe uma família ampla de técnicas para representar conhecimento, decompor objetivos, compor procedimentos e verificar resultados. Ela não apoia uma afirmação universal de que uma arquitetura estruturada será sempre mais rápida, menor ou mais precisa que qualquer modelo neural.

A hipótese mais forte e testável do projeto é:

> **Em tarefas fechadas, tipadas, repetitivas e verificáveis, separar conhecimento, método, estado, execução e verificação pode reduzir recomputação e tornar o comportamento mais previsível e auditável.**

A hipótese deve ser avaliada por benchmarks com tarefa, distribuição de entradas, hardware, aquecimento, memória, latência, custo de consulta, taxa de erro, taxa de reutilização e taxa de descoberta claramente definidos.

## Referências

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9166567/ "Hitzler et al., Neuro-symbolic approaches in artificial intelligence"
[2]: https://plato.stanford.edu/entries/logic-ai/ "Stanford Encyclopedia of Philosophy, Logic-Based Artificial Intelligence"
[3]: https://www.w3.org/TR/rdf11-primer/ "W3C, RDF 1.1 Primer"
[4]: https://www.w3.org/TR/owl2-primer/ "W3C, OWL 2 Web Ontology Language Primer"
[5]: https://www.w3.org/TR/shacl/ "W3C, Shapes Constraint Language"
[6]: https://cacm.acm.org/research/search-based-program-synthesis/ "Alur et al., Search-based Program Synthesis"
[7]: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/pbe16.pdf "Gulwani, Programming by Examples"
[8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5597726/ "David and Kroening, Program synthesis: challenges and opportunities"
[9]: https://act-r.psy.cmu.edu/about/ "ACT-R About, Carnegie Mellon University"
[10]: https://soar.eecs.umich.edu/soar_manual/04_ProceduralKnowledgeLearning/ "Soar Manual, Procedural Knowledge Learning"
[11]: https://proceedings.neurips.cc/paper/2018/hash/dc5d637ed5e62c36ecb73b654b05ba2a-Abstract.html "Manhaeve et al., DeepProbLog"
[12]: https://arxiv.org/abs/2012.13635 "Logic Tensor Networks"
[13]: https://www.scallop-lang.org/ "Scallop project"
[14]: https://www.pnas.org/doi/10.1073/pnas.1611835114 "Kirkpatrick et al., Overcoming catastrophic forgetting in neural networks"
