#2.7 – Removendo caracteres em branco de nomes: Armazene o nome de uma
#pessoa e inclua alguns caracteres em branco no início e no final do nome. Lembre-
#se de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.

name = '\tKauã \nLorenzi\t'

#solução proposta pelo chatgpt para remover o \n
fixed_name = name.strip().replace('\n', "")
print(fixed_name)

