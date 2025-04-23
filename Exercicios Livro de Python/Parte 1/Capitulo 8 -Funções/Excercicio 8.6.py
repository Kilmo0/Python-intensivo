
favlinguagem = {
    'Kauã': ['java', 'Python'],
    'Allan': ['php', 'Javascript'],
    'Brian': ['Rust', 'C++'],
}

for nome, linguagem in favlinguagem.items():
    print(f'a linguagem favoritado do {nome} é:')
    for linguagem in linguagem:
        print(linguagem)
