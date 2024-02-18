import random, string # import biblioteca random and string

tamanho = int(input('escreva quantidade de caracteres: ')) # definição de tamanho

char = string.ascii_letters + string.digits + '!#@$' # utilizando biblioteca string com seu metodh  ascii para gerar caracter Upper or Lower

rnd = random.SystemRandom() # chama function SystemRadom para utilizar biblioteca class os.random para gerar numeros aleatorio fornecido pelo sistema operacional

print(''.join(rnd.choice(char) for i in range(tamanho))) # mostrar senha com join, chice(char) e percorrer pelo tamanho