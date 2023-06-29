# Encapsulamento (modificadores de acesso: public, \_protected, \_\_private)

O encapsulamento e os modificadores de acesso são conceitos importantes em programação orientada a objetos que permitem controlar o acesso aos atributos e métodos de uma classe, determinando quais são visíveis e modificáveis a partir do código externo à classe.

Em Python, não existem modificadores de acesso tradicionais, como "public", "private" e "protected" encontrados em algumas linguagens. No entanto, existem convenções para indicar a intenção de acesso de um atributo ou método. A seguir, estão as convenções comuns usadas em Python:

1. Atributos e métodos públicos: não há convenção especial. Eles podem ser acessados diretamente de fora da classe.

2. Atributos e métodos protegidos: por convenção, o nome começa com um sublinhado (`_`). Embora eles ainda possam ser acessados de fora da super classe e sub classes, o sublinhado indica que não devem ser acessados diretamente.

3. Atributos e métodos privados: por convenção, o nome começa com dois sublinhados (`__`). Isso indica que eles devem ser considerados como privados e não devem ser acessados de fora da classe. No entanto, eles podem ser acessados indiretamente usando a técnica de "_name mangling_" (desfiguração de nomes), ou seja, o Python muda o nome de atributos e métodos privados (com 2 underline) ao serem chamados fora da classe.

Aqui está um exemplo que ilustra essas convenções de encapsulamento e acesso em Python:

```python
class MinhaClasse:
    def __init__(self):
        self.publico = 1
        self._protegido = 2
        self.__privado = 3

    def metodo_publico(self):
        print("Método público")

    def _metodo_protegido(self):
        print("Método protegido")

    def __metodo_privado(self):
        print("Método privado")


objeto = MinhaClasse()

print(objeto.publico)          # Saída: 1
print(objeto._protegido)       # Saída: 2
print(objeto._MinhaClasse__privado)  # Saída: 3 (acesso "name mangling")

objeto.metodo_publico()       # Saída: Método público
objeto._metodo_protegido()    # Saída: Método protegido
objeto._MinhaClasse__metodo_privado()  # Saída: Método privado (acesso "name mangling")
```

Observe que, embora o acesso aos atributos e métodos protegidos e privados seja possível, por convenção, é recomendado que você evite acessá-los diretamente de fora da classe. Em vez disso, use os métodos públicos para interagir com esses atributos ou métodos, pois isso promove o encapsulamento e a manutenção do controle sobre a lógica interna da classe.

Lembre-se de que essas convenções são apenas acordos entre os desenvolvedores e não são impostas pelo interpretador Python. É possível acessar e modificar atributos e métodos em qualquer circunstância, mas seguir as convenções ajuda a criar um código mais legível e a evitar problemas de acesso indevido ou modificações acidentais.
