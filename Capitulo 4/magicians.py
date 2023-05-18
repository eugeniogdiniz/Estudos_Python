magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

##O interpretador então repete as linhas 2 e 3, uma vez para cada
#nome da lista. Ler esse código como “para todo mágico na lista de
#mágicos, exiba o nome do mágico” pode ajudar.

#O conceito de laços é importante porque é uma das maneiras mais comuns
#para um computador automatizar tarefas repetitivas. Por exemplo, em um
#laço simples como o que usamos em magicians.py, Python inicialmente lê a
#primeira linha do laço:

#for magician in magicians:

#Essa linha diz a Python para extrair o primeiro valor da lista magicians e
#armazená-lo na variável magician. O primeiro valor é 'alice'. O
#interpretador então lê a próxima linha:

#print(magician)

#Python exibe o valor atual de magician, que ainda é 'alice'. Como a lista
#contém mais valores, o interpretador retorna à primeira linha do laço:

#for magician in magicians:

#Python recupera o próximo nome da lista, que é 'david', e armazena esse
#valor em magician. Então ele executa a linha:

#print(magician)

#Python exibe o valor atual de magician, que agora é 'david', novamente.
#O interpretador repete todo o laço mais uma vez com o último valor da
#lista, que é 'carolina'. Como não há mais valores na lista, Python passa
#para a próxima linha do programa. Nesse caso, não há mais nada depois
#do laço for, portanto o programa simplesmente termina.
