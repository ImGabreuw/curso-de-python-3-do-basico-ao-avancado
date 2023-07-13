# Selenium - Selecionando elementos com By, expected_conditions e WebDriverWait

O Selenium é uma ferramenta poderosa para automação de testes em navegadores, e uma das funcionalidades mais importantes é a capacidade de selecionar elementos da página para interagir com eles. O Selenium fornece várias maneiras de selecionar elementos.

### **Classe `By`**

A classe `By` é usada para localizar elementos na página com base em diferentes estratégias, como ID, nome, classe, seletor CSS, XPath, entre outros. Aqui estão alguns exemplos de uso:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Localizando por ID
element = driver.find_element(By.ID, "element_id")

# Localizando por nome
element = driver.find_element(By.NAME, "element_name")

# Localizando por classe
element = driver.find_element(By.CLASS_NAME, "element_class")

# Localizando por seletor CSS
element = driver.find_element(By.CSS_SELECTOR, "css_selector")

# Localizando por XPath
element = driver.find_element(By.XPATH, "xpath_expression")

# Fechar o navegador
driver.quit()
```

### **Classe `expected_conditions`**

A classe `expected_conditions` é usada em conjunto com `WebDriverWait` para aguardar determinadas condições antes de interagir com um elemento. Isso é útil quando você precisa esperar que um elemento esteja visível, clicável, etc. Aqui está um exemplo:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Esperar até que um elemento esteja visível
element = wait.until(EC.visibility_of_element_located((By.ID, "element_id")))

# Esperar até que um elemento esteja clicável
element = wait.until(EC.element_to_be_clickable((By.ID, "element_id")))

# Fechar o navegador
driver.quit()
```

### **Classe `WebDriverWait`**

A classe `WebDriverWait` é usada para definir o tempo máximo de espera para uma determinada condição ser satisfeita. É útil quando você precisa aguardar o carregamento de uma página ou a disponibilidade de um elemento antes de realizar uma ação. Aqui está um exemplo:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Esperar até que a página seja carregada
wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

# Esperar até que um elemento esteja presente na página
element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))

# Fechar o navegador
driver.quit()
```

No exemplo acima, `WebDriverWait` é usado para esperar até que a página esteja completamente carregada e um elemento esteja presente antes de prosseguir.
