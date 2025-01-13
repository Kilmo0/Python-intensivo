#sistema de login

users = ['Amanda', 'Kauã', 'Allan']
newusers = ['Amanda', 'Brian', 'Ana']

lowusers = (lowusersa.lower() for lowusersa in users)
newlowusers = (newlowusersa.lower() for newlowusersa in newusers)

for newuser in newlowusers:
    if not newuser in lowusers:
        print('Seja bem vindo {}'.format(newuser))
    else:
        print('você já está cadastrado {}'.format(newuser))