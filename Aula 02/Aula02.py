def cria_lista():
    #variavel 'numeros' vai para a Stack
    # a lista [1,2,3] vai para o Heap
    numeros = [1, 2, 3]
    return numeros

resultado = cria_lista()
# A Função acabou, mas a lista
# Ainda existe no Heap!
print(resultado) # [1, 2, 3]