from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
if (ano_atual - ano_nasc == 18):
    print(f'Quem nasceu em {ano_nasc} está com 18 anos em {ano_atual}.'
    '\nVocê tem que se alistar IMEDIATAMENTE.')
elif (ano_atual - ano_nasc > 18):
    print(f'Quem nasceu em {ano_nasc} está com {ano_atual - ano_nasc} em {ano_atual}.'
    f'\nVocê já deveria ter se alistado há {(ano_atual - ano_nasc) - 18} anos.')
    f'\n Seu alistamento foi em {ano_nasc + 18}.'
elif (ano_atual - ano_nasc < 18):
    print(f'Quem nasceu em {ano_nasc} está com {ano_atual - ano_nasc} em {ano_atual}.'
    f'\nAinda faltam {(ano_atual - ano_nasc) - 18} anos para o seu alistamento.'
    f'\nSeu alistamento será em {ano_nasc + 18}.')
else:
    print('Erro, por favor execute o código novamente...')