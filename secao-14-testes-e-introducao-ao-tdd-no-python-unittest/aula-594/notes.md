# Unittest #2 - Com TDD

O Desenvolvimento Orientado a Testes (_Test Driven Development_ ou TDD) é uma prática de desenvolvimento de software que coloca o foco na criação de testes antes da implementação do código. Essa abordagem segue um ciclo iterativo e incremental, no qual os testes são escritos antes do código real. O processo TDD geralmente envolve três etapas principais: **Red**, **Green**, e **Refactor** (também conhecidas como Ciclo TDD).

![](./assets/test-driven-development-TDD.webp)

1. **Red (Vermelho):** Nesta fase, o desenvolvedor escreve um teste automatizado que descreve a funcionalidade desejada, mas a implementação ainda não existe ou falha.

   ```python
   # Exemplo de teste em Python usando a biblioteca de testes unittest
   def test_soma():
       assert soma(2, 3) == 5
   ```

2. **Green (Verde):** Nesta etapa, o desenvolvedor implementa o código mínimo para fazer o teste passar.

   ```python
   # Exemplo de implementação da função soma para que o teste passe
   def soma(a, b):
       return a + b
   ```

3. **Refactor (Refatoração):** Aqui, o código é aprimorado e otimizado sem alterar o comportamento do mesmo, garantindo que ele atenda aos requisitos.

O TDD promove diversas vantagens, como:

- **Maior confiança no código:** Como o código é testado automaticamente, há menos probabilidade de bugs e regressões.

- **Maior clareza e simplicidade:** O desenvolvedor se concentra em escrever apenas o código necessário para passar nos testes, resultando em um código mais enxuto e objetivo.

- **Facilita a manutenção:** Testes automatizados facilitam a identificação de problemas após as modificações no código.

- **Fomenta o design orientado a interfaces:** TDD incentiva o pensamento sobre as interfaces e como o código será usado por outras partes do sistema.

Além disso, é importante observar que o TDD não é uma técnica restrita a uma linguagem específica de programação, podendo ser aplicado em diversas plataformas e linguagens.

Se você está começando a aprender TDD, considere usar uma estrutura de testes adequada para a linguagem que você está utilizando, como **JUnit** para Java, **Jest** para JavaScript, **unittest** para Python, entre outros. O TDD pode ser uma prática desafiadora no início, mas com a prática, torna-se uma ferramenta valiosa para o desenvolvimento de software de qualidade.
