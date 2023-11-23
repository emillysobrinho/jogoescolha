import random
pontos_seus = 0
pontos_deles = 0
while(True):
 cor_secreta = random.choice(['R','G','B'])
 palpite = input("adivinhe a cor(R, G, B): ").upper()
 if palpite not in ['R', 'G', 'B']:
  print("Entrada invalida, Escolha R, G, B.")
 elif palpite == cor_secreta:
  print("Parabéns! Você Acertou!")
  pontos_seus = pontos_seus +1
 elif palpite != cor_secreta:
  print("Você Errou!")
  pontos_deles = pontos_deles +1
 print('A cor era', cor_secreta)
 print(f'VOCÊ {pontos_seus} X PC {pontos_deles}')