# Esquemas

Os esquemas definem contratos mínimos para os artefatos que o sistema recupera, compõe e aprende.

- [`concept-key.schema.json`](concept-key.schema.json): roteamento por domínio, objetivo, tipos, estado e restrições.
- [`method.schema.json`](method.schema.json): método com pré-condições, passos, pós-condições, verificação e evidência.
- [`error-pattern.schema.json`](error-pattern.schema.json): sintoma, contexto, causa, correção, prevenção, variantes e evidência.

A validação do esquema garante forma. Ela não garante que os fatos sejam verdadeiros, que o método esteja correto ou que a correção funcione em todos os casos; essas propriedades exigem testes comportamentais, fontes e verificação apropriada.
