nome = str(input('Ola qual seria seu nome todo? ')).strip()
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
nsp = (nome.replace(' ',''))
print(f'O seu nome possui {len(nsp)} letras')
ns = nome.split()
print(f'O seu primeiro nome é {ns[0].capitalize()} e seu nome possui {len(ns[0])} letras.')