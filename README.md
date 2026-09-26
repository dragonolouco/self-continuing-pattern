# Self-Continuing Pattern

Arquitetura de inteligência baseada em **regras fundamentais, composição, estado, verificação e memória de métodos/erros**.

> **Ideia central:** um sistema não precisa memorizar todas as respostas. Ele precisa conhecer unidades básicas, saber aplicar transformações locais, manter o estado correto e reutilizar estruturas que já foram verificadas.

## O que este repositório investiga

Esta é uma proposta de arquitetura para tarefas que podem ser decompostas em operações menores e repetíveis. O exemplo mais simples é a soma decimal: com apenas os algarismos de `0` a `9`, a regra do transporte e uma execução da direita para a esquerda, o sistema consegue somar números com qualquer quantidade de casas limitada apenas pelo tempo e pela memória disponíveis.

A mesma ideia pode ser aplicada, com diferentes graus de formalização, a:

- matemática e cálculo exato;
- validação, parsing e transformação de dados;
- programação por componentes reutilizáveis;
- consulta estruturada a conhecimento;
- planejamento com estados e pré-condições;
- diagnóstico e correção de erros;
- sistemas híbridos que usam modelos aprendidos somente onde há ambiguidade ou descoberta.

## Estrutura do repositório

| Categoria | Conteúdo |
|---|---|
| [`docs/00-visao-geral.md`](docs/00-visao-geral.md) | Tese, vocabulário e limites da proposta |
| [`docs/01-fundamentos/`](docs/01-fundamentos/) | Primitivas, estado, composição e verificação |
| [`docs/01-fundamentos/02-decomposicao-resposta-instantanea.md`](docs/01-fundamentos/02-decomposicao-resposta-instantanea.md) | Decomposição, precisão estrutural e execução de baixa latência |
| [`docs/01-fundamentos/03-arquitetura-universal-por-camadas.md`](docs/01-fundamentos/03-arquitetura-universal-por-camadas.md) | Camadas universais e exemplo de países/letras |
| [`docs/02-motores/`](docs/02-motores/) | Aritmética e execução passo a passo |
| [`docs/03-aplicacoes/`](docs/03-aplicacoes/) | Programação, linguagem, dados e outros domínios |
| [`docs/03-aplicacoes/02-camada-de-palavras-e-significados.md`](docs/03-aplicacoes/02-camada-de-palavras-e-significados.md) | Palavras, relações, cadeias de conceitos e contexto |
| [`docs/04-memoria/`](docs/04-memoria/) | Memória de métodos, acertos, erros e variantes |
| [`docs/04-memoria/02-aprendizado-por-metodos.md`](docs/04-memoria/02-aprendizado-por-metodos.md) | Chaves conceituais, adaptação e descoberta verificável |
| [`docs/05-arquitetura-ia.md`](docs/05-arquitetura-ia.md) | Proposta de modelo híbrido leve e roteamento |
| [`docs/05-chave-conceitual-e-sintese.md`](docs/05-chave-conceitual-e-sintese.md) | Recuperação, composição e síntese de métodos por chave |
| [`docs/06-limites-e-metricas.md`](docs/06-limites-e-metricas.md) | O que medir, riscos e limites das afirmações |
| [`docs/07-ciencia-e-arquiteturas-relacionadas.md`](docs/07-ciencia-e-arquiteturas-relacionadas.md) | Comparação com IA simbólica, KGs, síntese, Soar/ACT-R e IA neuro-simbólica |
| [`examples/`](examples/) | Exemplos de estruturas, regras e fluxos |
| [`diagrams/`](diagrams/) | Diagramas Mermaid editáveis e PNGs renderizados |
| [`schemas/`](schemas/) | Contratos JSON para chaves, métodos e erros |
| [`src/`](src/) | Protótipos aritmético, textual e de conhecimento de palavras |
| [`tests/`](tests/) | Testes automatizados das invariantes básicas |

## Princípio operacional

```text
entrada
  -> interpretar e tipar
  -> decompor em unidades
  -> selecionar regra ou método
  -> executar uma transição
  -> atualizar o estado
  -> verificar invariantes
  -> repetir
  -> recompor o resultado
    -> registrar sucesso ou falha reutilizável
```

## Decompor para responder rapidamente

Esta arquitetura transforma uma entrada grande em unidades menores, aplica uma estrutura já validada e recompõe o resultado. Quando o conhecimento, as regras e as verificações estão corretos, a resposta pode ser produzida com latência muito baixa e alta precisão no domínio formalizado. O mecanismo não precisa inventar tudo do zero: ele reutiliza métodos, estados e correções estruturadas.

Leia a explicação completa em [`docs/01-fundamentos/02-decomposicao-resposta-instantanea.md`](docs/01-fundamentos/02-decomposicao-resposta-instantanea.md).

## Diagramas

Os desenhos da arquitetura estão em [`diagrams/README.md`](diagrams/README.md). Eles mostram a arquitetura geral, a camada de palavras, o ciclo adaptativo e a soma por estados. Cada desenho possui uma fonte Mermaid editável e uma versão PNG renderizada.

## Protótipo rápido

O protótipo implementa soma e subtração decimal por dígitos, sem converter o número inteiro para uma operação nativa. Ele expõe os estados intermediários e valida o resultado:

```bash
python3 -m unittest discover -s tests -v
python3 -m src.fundamental_engine
```

## Formulação compacta

```text
capacidade
= conhecimento fundamental
+ primitivas
+ estado
+ regras de composição
+ métodos reutilizáveis
+ verificação
+ memória de erros
+ acesso a conhecimento externo
+ adaptação
```

## Posicionamento técnico

A proposta não afirma que regras manuais substituem toda aprendizagem. Tarefas determinísticas podem ser executadas com grande previsibilidade e baixo custo por operação. Já interpretação aberta, percepção, contexto implícito e descoberta de estruturas novas podem exigir modelos aprendidos, bases externas ou ambos.

Também não é correto prometer que será “mais rápido que qualquer modelo” sem especificar tarefa, hardware e métrica. A hipótese testável deste projeto é mais precisa:

> **Para tarefas estruturadas, repetitivas e verificáveis, uma arquitetura especializada pode reduzir latência, memória, custo e variação em comparação com gerar uma resposta do zero.**

## Estado do projeto

Este repositório começa como uma especificação executável: a documentação descreve a arquitetura e o protótipo testa o núcleo mais simples. A evolução deve ser orientada por testes, benchmarks e exemplos reproduzíveis, não apenas por afirmações conceituais.
