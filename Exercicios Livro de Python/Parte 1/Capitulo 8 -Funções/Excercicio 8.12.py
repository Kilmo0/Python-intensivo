def sandwich_maker(*ingredientes):
    print('Seu sandwich terá:')
    for igrediente in ingredientes:
        print(f"- {igrediente}")

sandwich_maker('tomate', 'Alface', 'Queijo')