favlinguagem = {
    'Kauã': 'java',
    'Allan': 'php',
    'Brian': 'Rust',
    'Brian': 'Rust'
}
print('as linguagens mensionadas foram:')
for linguagem in set(sorted(favlinguagem.values())):
    print(linguagem.title())