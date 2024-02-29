import random, string # import random and string library

size = int(input('escreva quantidade de caracteres: ')) # size definition

char = string.ascii_letters + string.digits + '!#@$' # using string library with its ascii method to generate Upper or Lower character

rnd = random.SystemRandom() # calls SystemRadom function to use os.random class library to generate random numbers provided by the operating system

print(''.join(rnd.choice(char) for i in range(size))) # show password with join, chice(char) and scroll by size
