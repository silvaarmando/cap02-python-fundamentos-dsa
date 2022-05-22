from math import radians, sin, cos, tan

ângulo = float(input('Qual ângulo que você deseja? '))
seno = sin(radians(ângulo))
print(f'O ângulo {ângulo} ° tem SENO {seno:.2f}')
cosseno = cos(radians(ângulo))
print(f'O ângulo {ângulo} ° tem COSSENO {cosseno:.2f}')
tangente = tan(radians(ângulo))
print(f'O ângulo {ângulo} ° tem TANGENTE {tangente:.2f}')