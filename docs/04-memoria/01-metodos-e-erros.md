# Memória de métodos e erros

## Memória útil

A memória deve ser estruturada por valor de reutilização:

```text
memória de certezas: fatos estáveis, transições testadas, componentes válidos
memória de métodos: sequência, pré-condições, pós-condições, custo e limitações
memória de erros: sintoma, contexto, causa, correção e prevenção
```

## Registro de método

```yaml
id: soma_decimal_por_colunas
versão: 1
aplicável_quando:
  - tipo_a: inteiro_decimal
  - tipo_b: inteiro_decimal
passos:
  - alinhar casas
  - percorrer da direita para a esquerda
  - aplicar transição de transporte
verificação:
  - reconstruir valor final
limitações:
  - não cobre números não inteiros nesta versão
```

## Registro de erro

```yaml
id: evento_antes_da_criacao
sintomas:
  - evento não dispara
causa:
  - elemento ainda não existe
correção:
  - registrar após criar elemento ou após carregamento
prevenção:
  - verificar existência antes de conectar
variantes:
  - seletor incorreto
  - ordem de inicialização inválida
```

## Reconhecimento de variantes

O sistema não precisa exigir igualdade literal. Ele pode comparar campos estruturais:

```text
mesmo tipo de falha?
mesmo ponto do ciclo de vida?
mesma pré-condição violada?
mesma correção aplicável?
```

A semelhança deve ser acompanhada de confiança, evidência e possibilidade de desfazer a aplicação. Uma correção parecida não deve ser aplicada cegamente.

## Ciclo de aprendizagem operacional

```text
tentativa -> resultado -> diagnóstico -> correção -> teste
         -> método validado ou erro estruturado
```

Isso evita pensar tudo do zero, mas não elimina a necessidade de testar o método em entradas novas.

Para a visão mais ampla de como chaves conceituais substituem respostas memorizadas e permitem adaptação, consulte [`02-aprendizado-por-metodos.md`](02-aprendizado-por-metodos.md).
