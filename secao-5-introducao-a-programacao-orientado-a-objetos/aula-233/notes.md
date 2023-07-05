# Na prática: polimorfismo, assinatura de métodos e Liskov Substitution Principle

**OBS**: O Python não suporta _method overload_ (ou sobrecarga de método), _method override_ (ou sobreposição de método).

_Type annotation_ ou _Type hint_ é a tipagem de funções/métodos e variáveis no Python e é muito útil para desenvolvedores uma vez que facilita o entendimento do código e seu fluxo, porém para o Python não faz nenhuma diferença uma vez que é uma linguagem dinamicamente tipada.

Para definir o tipo de retorno de uma função/método, utiliza-se a seguinte sintaxe:

```python
def minhaFunção() -> None:
  ...
```

> **OBS**: por padrão toda função retorna o tipo `None`.