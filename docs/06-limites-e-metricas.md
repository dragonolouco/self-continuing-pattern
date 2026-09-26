# Limites, métricas e evolução

## Limites

- regras manuais não cobrem automaticamente todas as exceções do mundo;
- dados externos podem estar incompletos, desatualizados ou errados;
- uma regra errada pode produzir respostas consistentemente erradas;
- memórias de erro podem acumular falsos positivos;
- composição exige compatibilidade entre tipos e dependências;
- descoberta continua sendo mais cara que execução de método conhecido;
- “menor”, “mais rápido” e “mais eficiente” só têm significado com um benchmark definido.

## Métricas

| Métrica | Pergunta |
|---|---|
| Latência por tarefa | Quanto tempo leva para responder? |
| CPU/GPU por tarefa | Quanto cálculo foi necessário? |
| Memória residente | Quanto precisa ficar carregado? |
| Taxa de reutilização | Quantas tarefas usaram método existente? |
| Taxa de descoberta | Quantas exigiram método novo? |
| Erros repetidos | A memória evita reincidência? |
| Cobertura de primitivas | Quantos problemas são expressáveis? |
| Correção determinística | O método continua correto em novos tamanhos? |

## Comparação justa

Comparar com um modelo neural exige fixar:

- mesma tarefa e distribuição de entradas;
- qualidade mínima aceitável;
- latência de aquecimento e de execução;
- custo de consulta a dados e ferramentas;
- memória do processo;
- taxa de erro e taxa de verificação;
- hardware e paralelismo.

## Roteiro

1. ampliar os testes aritméticos e os rastros de estado;
2. adicionar multiplicação e divisão com contratos;
3. criar catálogo de primitivas e métodos em JSON/YAML;
4. adicionar memória de erros com busca por campos estruturais;
5. implementar um roteador de tarefas;
6. criar exemplos de programação, dados e consultas;
7. medir contra implementações de referência;
8. integrar um modelo leve apenas para interpretação e descoberta;
9. testar generalização, regressões e falsos reconhecimentos.

## Referências comparativas

O projeto foi comparado com IA simbólica, grafos de conhecimento e ontologias, síntese de programas, arquiteturas cognitivas, aprendizagem contínua e IA neuro-simbólica. A comparação completa, com fontes externas e recomendações de implementação, está em [`docs/07-ciencia-e-arquiteturas-relacionadas.md`](07-ciencia-e-arquiteturas-relacionadas.md).
