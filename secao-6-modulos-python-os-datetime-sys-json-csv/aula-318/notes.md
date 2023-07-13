# Selenium - Enviando teclas com a classe Keys

Ao usar o Selenium para automação de testes, muitas vezes é necessário interagir com elementos de entrada, como campos de texto, pressionando teclas específicas, como Enter, Tab, Ctrl, etc. A classe `Keys` do Selenium fornece métodos para enviar teclas especiais e combinações de teclas.

Aqui está como você pode usar a classe `Keys` para enviar teclas usando o Selenium:

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Localize o campo de texto
campo_texto = driver.find_element_by_id("campo_texto_id")

# Enviar teclas simples
campo_texto.send_keys("Texto de exemplo")

# Enviar teclas especiais
campo_texto.send_keys(Keys.ENTER)  # Pressionar Enter
campo_texto.send_keys(Keys.TAB)  # Pressionar Tab

# Enviar combinação de teclas
campo_texto.send_keys(Keys.CONTROL + "a")  # Pressionar Ctrl+A para selecionar tudo
campo_texto.send_keys(Keys.CONTROL + "c")  # Pressionar Ctrl+C para copiar
campo_texto.send_keys(Keys.CONTROL + "v")  # Pressionar Ctrl+V para colar

# Fechar o navegador
driver.quit()
```

No exemplo acima, usamos o método `send_keys()` para enviar texto para o campo de texto identificado por "campo_texto_id". Em seguida, usamos `send_keys()` novamente para enviar teclas especiais ou combinações de teclas.

Algumas teclas especiais disponíveis na classe `Keys` incluem `ENTER`, `TAB`, `ESCAPE`, `SPACE`, `BACKSPACE`, `DELETE`, entre outras. Para enviar teclas modificadoras como `CTRL`, `ALT` ou `SHIFT`, você pode combiná-las com outras teclas. No exemplo acima, usamos `Keys.CONTROL + "a"` para enviar a combinação Ctrl+A, `Keys.CONTROL + "c"` para enviar Ctrl+C e `Keys.CONTROL + "v"` para enviar Ctrl+V.

Essa é uma maneira conveniente de simular ações do teclado durante a automação de testes usando o Selenium. A classe `Keys` fornece uma ampla gama de opções para enviar teclas especiais e combinações de teclas de forma programática.
