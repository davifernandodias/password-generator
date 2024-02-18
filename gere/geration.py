import random, string

tamanho = int(input('escreva quantidade de caracteres: '))

char = string.ascii_letters + string.digits + '!#@$'

rnd = random.SystemRandom()

print(''.join(rnd.choice(char) for i in range(tamanho)))