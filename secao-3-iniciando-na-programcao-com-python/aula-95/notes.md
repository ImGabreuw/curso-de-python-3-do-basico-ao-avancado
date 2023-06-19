# Detalhes sobre o interpretador do Python

> ## **Interpretador do Python**

- Executar um módulo Python:

  ```shell
  $ python [arquivo .py]
  ```

  ```shell
  $ python main.py
  ```

- Executar um módulo Python sem a utilizado do _buffer_:

  ```shell
  $ python -u [arquivo .py]
  ```

  ```shell
  $ python -u main.py
  ```

- Executar uma biblioteca como script:

  ```shell
  $ python -m [biblioteca]
  ```

  ```shell
  $ python -m venv env
  ```

  > Executar a biblioteca `venv` como um script

- Executar um comando Python:


  ```shell
  $ python -c "[código Python]"
  ```

  ```shell
  $ python -c "print('Olá');print('Olá')"
  ```

- Executar um módulo Python de forma interativa com o _Python Console_:

  ```shell
  $ python -i [arquivo .py]
  ```

  ```shell
  $ python -i main.py
  ```

  > **OBS**: o código escrito no modo interativo não é salve
