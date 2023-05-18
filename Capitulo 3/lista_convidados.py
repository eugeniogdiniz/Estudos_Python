list_convid = ['Felipe', 'Ricardo', 'Marx']
print('Boa noite, eu estou convidando você ' + list_convid[0] + ' para o meu jantar de casamento.')
print('Boa noite, eu estou convidando você ' + list_convid[1] + ' para o meu jantar de casamento.')
print('Boa noite, eu estou convidando você ' + list_convid[2] + ' para o meu jantar de casamento.')

print('O ' + list_convid[0] + ' não poderá participar')

list_convid[0] = 'Lucas'
print('Boa noite, eu estou convidando você ' + list_convid[0] + ' para o meu jantar de casamento.')
print('Boa noite, eu estou convidando você ' + list_convid[1] + ' para o meu jantar de casamento.')
print('Boa noite, eu estou convidando você ' + list_convid[2] + ' para o meu jantar de casamento.')

print('Iremos receber novos convidados - Eugenio, Luzia e Antonio')

list_convid.insert(3, 'Eugenio')
list_convid.insert(3, 'Luzia')
list_convid.append('Antonio')
print(list_convid)

print('Boa noite, eu estou convidando você ' + list_convid[0] + ' para o meu jantar de casamento.')
print('Boa noite, eu estou convidando você ' + list_convid[1] + ' para o meu jantar de casamento.')
print('Boa noite, eu estou convidando você ' + list_convid[2] + ' para o meu jantar de casamento.')
print('Boa noite, eu estou convidando você ' + list_convid[3] + ' para o meu jantar de casamento.')
print('Boa noite, eu estou convidando você ' + list_convid[4] + ' para o meu jantar de casamento.')
print('Boa noite, eu estou convidando você ' + list_convid[5] + ' para o meu jantar de casamento.')

list_convid_del = list_convid.pop(0)
list_convid_del = list_convid.pop(0)
list_convid_del = list_convid.pop(0)
list_convid_del = list_convid.pop(0)

del list_convid[0]
del list_convid[0]
print(list_convid)