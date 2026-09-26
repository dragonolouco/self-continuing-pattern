# Aprendizado por métodos e adaptação

## Ideia central

Aprender uma resposta específica pode ser desnecessário quando existe uma regra capaz de calculá-la. Saber todos os números de 1 a 1 milhão, por exemplo, ocupa espaço de memória sem necessidade se a arquitetura já sabe representar inteiros, comparar valores, somar, subtrair e calcular qualquer número pedido.

```text
resposta memorizada: número X -> texto X
método reutilizável: representação + operações -> qualquer X válido
```

O mesmo princípio vale para outras famílias de problemas: a memória guarda a chave conceitual e o procedimento, enquanto os dados concretos são fornecidos e processados quando necessário.

## Chaves conceituais

Uma chave é uma representação compacta que permite localizar ou construir um método:

```yaml
chave:
  domínio: aritmética
  tipos: [inteiro, inteiro]
  objetivo: soma
  estado: transporte
  restrições: [base_decimal]
método: soma_por_colunas
verificação: reconstruir_resultado
```

Em linguagem, uma chave pode conter entidade, intenção, relação, modificador e contexto. Em programação, pode conter componente, evento, estado e ação.

## Ciclo adaptativo

```text
receber informação
    -> estruturar conceitos
    -> comparar com métodos conhecidos
    -> selecionar hipótese
    -> executar
    -> verificar resultado
    -> se correto: armazenar método
    -> se incorreto: diagnosticar erro
    -> corrigir, testar e versionar
    -> reutilizar em variantes futuras
```

O sistema não precisa pensar longamente quando já existe uma chave compatível. Ele recupera o método, aplica os dados e verifica. O esforço maior acontece quando não há método adequado; nesse caso, entra em descoberta.

Uma chave pode resultar em três operações diferentes: consultar uma relação pronta, compor métodos existentes ou sintetizar uma sequência nova e testá-la. A diferença entre esses níveis é importante para medir velocidade, custo e risco.

## Evolução sem ajuda passo a passo

Uma arquitetura pode evoluir automaticamente no sentido operacional de:

- organizar informações novas em categorias;
- associar conceitos a relações;
- testar composições;
- registrar métodos bem-sucedidos;
- reconhecer padrões de falha;
- propor correções;
- validar a correção em casos de teste;
- promover o método para reutilização.

Isso não significa aprendizagem irrestrita ou infalível. Para evitar que uma conclusão errada vire regra, a promoção deve exigir evidência, testes, versionamento, confiança e possibilidade de reversão.

## Exemplo numérico

Pedido: calcular um número com muitas casas.

```text
chave: inteiro decimal
método: operar casa por casa
estado: transporte/emprestimo
verificação: operação inversa ou invariantes
```

A quantidade de casas muda o número de transições, não a estrutura. O sistema pode calcular uma entrada de 10, 100 ou 1 milhão de dígitos sem memorizar cada inteiro possível.

## Exemplo semântico

Pedido: interpretar “jogo de terror com exploração”.

```text
chave: entidade + gênero + mecânica
método: buscar relações e compor atributos
verificação: todos os conceitos existem e as relações são compatíveis
```

Se aparecer “jogo de ficção científica”, o sistema pode consultar uma fonte, solicitar o conceito ou iniciar descoberta. Ele não deve inventar silenciosamente uma definição ausente.

## O que significa “infinitamente”

A arquitetura pode ser aplicada indefinidamente enquanto houver representação, recursos físicos, regras e dados suficientes. “Infinito” descreve a generalidade do procedimento, não memória ou tempo físicos infinitos.
