# Contribuindo

## Princípios

1. Descrever a estrutura antes de adicionar uma implementação.
2. Separar regras determinísticas de interpretação e descoberta.
3. Dar nomes explícitos ao estado, às pré-condições e às pós-condições.
4. Adicionar testes de exemplos e invariantes.
5. Registrar limitações e não prometer desempenho sem benchmark.
6. Preferir métodos pequenos, compostos e reutilizáveis.

## Executar os testes

```bash
python3 -m unittest discover -s tests -v
```

## Adicionar um método

Documente:

- identificador e versão;
- quando pode ser usado;
- entradas e tipos;
- pré-condições;
- passos e estado intermediário;
- pós-condições;
- verificação;
- limitações;
- erros conhecidos e prevenção.

## Adicionar um erro

Registre sintoma, contexto, causa, correção, evidência, confiança e variantes. Uma ocorrência isolada não deve virar regra geral sem teste.
