# Pillow: redimensionando imagens com Python

O Pillow é uma biblioteca popular de processamento de imagens em Python. Ela fornece várias funcionalidades, incluindo a capacidade de redimensionar imagens de forma fácil e eficiente. 

Para redimensionar uma imagem usando o Pillow, você precisa primeiro instalar a biblioteca. Você pode fazer isso usando o pip, o gerenciador de pacotes do Python, com o seguinte comando:

```
pip install pillow
```

Aqui está um exemplo de código que demonstra como redimensionar uma imagem usando o Pillow:

```python
from PIL import Image

# Abrir a imagem
imagem_original = Image.open('imagem_original.jpg')

# Definir o tamanho desejado
novo_tamanho = (800, 600)

# Redimensionar a imagem
imagem_redimensionada = imagem_original.resize(novo_tamanho)

# Salvar a imagem redimensionada
imagem_redimensionada.save('imagem_redimensionada.jpg')
```

Neste exemplo, a imagem original é aberta usando a função `Image.open()` do Pillow. Em seguida, o tamanho desejado para a imagem redimensionada é definido na variável `novo_tamanho`. A função `resize()` é usada para redimensionar a imagem original para o novo tamanho especificado.

Por fim, a imagem redimensionada é salva no disco usando a função `save()`, especificando o nome do arquivo de destino.

Após executar o código acima, você terá uma nova imagem chamada "imagem_redimensionada.jpg" no mesmo diretório do script, com as dimensões especificadas.

É importante notar que o redimensionamento de imagens pode afetar a proporção original da imagem, tornando-a mais larga ou mais estreita. Se você deseja manter a proporção original, pode usar a função `thumbnail()` em vez da função `resize()`. A função `thumbnail()` redimensiona a imagem para se ajustar dentro de um retângulo especificado, mantendo a proporção original.