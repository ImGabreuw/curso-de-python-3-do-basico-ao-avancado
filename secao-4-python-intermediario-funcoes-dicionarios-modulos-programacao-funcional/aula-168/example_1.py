def decorador1(funcao):
    def funcao_decorada():
        print("Executando decorador 1")
        funcao()
    return funcao_decorada

def decorador2(funcao):
    def funcao_decorada():
        print("Executando decorador 2")
        funcao()
    return funcao_decorada

@decorador1
@decorador2
def minha_funcao():
    print("Executando minha_funcao.")

minha_funcao()