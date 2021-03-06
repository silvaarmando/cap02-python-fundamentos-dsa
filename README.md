<h1
  align='center'
>
  <h3
      align="center"
  >
    <a
      href="https://www.datascienceacademy.com.br/"
    >
      <img
        width="350em"
        src="./screens/logo_dsa.png"
      >
    </a>
  </h3>

  <h2
    align="center"
  >
    Python Fundamentos para Análise de Dados
  </h2>

  <h3
    align="center"
  >
    <img
      alt="Data Types"
      width="450em"
      src="./screens/data_types.svg"
    >
  </h3>

  <h2
    align="center"
  >
    VARIÁVEIS, TIPOS E ESTRUTURAS DE DADOS
  </h2>

</h1>

<br
/>

<h3
  align="center"
>
  <a
    href="#NÚMEROS"
  >
    <img
      alt="Números"
      width="250em"
      src="./screens/summary/NUMEROS.svg"
    >
  </a>
  <br
  />
  <a
    href="#VARIÁVEIS"
  >
    <img
      alt="Variáveis"
      width="250em"
      src="./screens/summary/VARIÁVEIS.svg"
    >
  </a>
  <br
  />
  <a
    href="#STRINGS"
  >
    <img
      alt="Strings"
      width="250em"
      src="./screens/summary/STRINGS.svg"
    >
  </a>
  <br
  />
  <a
    href="#LISTAS"
  >
    <img
      alt="Listas"
      width="250em"
      src="./screens/summary/LISTAS.svg"
    >
  </a>
  <br
  />
  <a
    href="#DICIONÁRIOS"
  >
    <img
      alt="Dicionários"
      width="250em"
      src="./screens/summary/DICIONÁRIOS.svg"
    >
  </a>
  <br
  />
  <a
    href="#TÚPLAS"
  >
    <img
      alt="Túplas"
      width="250em"
      src="./screens/summary/TUPLAS.svg"
    >
  </a>
  <br
  />
  <a
    href="#EXERCÍCIOS"
  >
    <img
      alt="Exercícios"
      width="250em"
      src="./screens/summary/EXERCICIOS.svg"
    >
  </a>
  <br
  />
  <a
    href="#GAME"
  >
    <img
      alt="Game"
      width="250em"
      src="./screens/summary/GAME.svg"
    >
  </a>
</h3>

<br
/>

## NÚMEROS

### TIPOS NÚMERICOS

<p
  align="capitalize"
>
  Existem dois tipos númericos principais em Python:
</p>

<h3
  align="capitalize"
>
  <img
    width="450em"
    alt="Numeric Types"
    src="./screens/numeric_types.svg">
</h3>

### OPERAÇÕES MATEMÁTICAS

<p
  align="capitalize"
>
  O python como todas as linguagens de programação tem todas as operações e funções matemáticas e também podem ser utilizados como uma calculadora avançada.
</p>

<h3
  align="capitalize"
>
  <img
    width="450em"
    alt="Numeric Types"
    src="./screens/arithmetic_operations.svg"
  >
</h3>

<p
  align="capitalize"
>
  Para realizar essas operações com números inteiros com números positivos e negativos é como na matemática convencional, mas dentro das regras da linguagem Python.

  Soma:
</p>

```Python
8 + 12
```

```Python
7 - 7
```

<p
  align="capitalize"
>
  Subtração:
</p>

```Python
5.2 + 1200.8
```

```Python
-3.1 - 7.9999
```

<p
  align="capitalize"
>
  Multiplicação:
</p>

```Python
7.4 ** 2
```

```Python
5 ** 3
```

<p
  align="capitalize"
>
  Divisão:
</p>

```Python
7.4 ** 2
```

```Python
5 ** 3
```

<p
  align="capitalize"
>
  Módulo:
</p>

```Python
49 % 2
```

```Python
25 % 3
```

<p
  align="capitalize"
>
  Potência:
</p>

```Python
5 ** 5
```

```Python
7 ** 8
```

<p
  align="capitalize"
>
  Também podemos utilizar números com pontos flutuante(float) para realizar as mesmas operações.
</p>

```Python
# Soma
6.7 + 8.3 + 5
```

```Python
# Subtração
10.2 - 9.1
```

```Python
# Multiplicação
8.7 * 8.7
```

<p
  align="capitalize"
>
  Na divisão ainda podemos utilizar ooperador de <strong>divisão inteira</strong> com <strong>//</strong>
</p>

```Python
15.3 / 3 # Divisão
49.9 // 3 # Divisão Inteira
```

### FUNÇÕES BUILT-IN

<p
  align="capitalize"
>
  <strong
  >
    Funções Built-in
  </strong>
  ou no Português Funções Internas, são funções já incorporadas na própria linguagem sem necessidade de importações ou implementações avançadas.
</p>

<h3
  align="capitalize"
>
  <img
    alt="Built-in Functions em Python"
    width="450em"
    src="./screens/builtin-functions.svg"
  >
</h3>

#### TIPO DE UMA VARIÁVEL

<p
  align="capitalize"
>
  Para sabermos o tipo de um dado em uma variável podemos utilizar o <strong>type()</strong>
</p>

```python
 type(5.8)
```

```python
 type(-8)
```

<p
  align="capitalize"
>
  Também podemos utilizar o <strong>TYPE</strong> para outros tipos de dados.
</p>

```python
 # Variável do tipo String
 name = 'Armando'
 type(name)
```

#### CONVERSÃO

<p
  align="capitalize"
>
  Podemos utilizar funções <strong>built-in</strong> como o <strong>int()</strong> para converter números para um tipo inteiro ou <strong>float()</strong> para converter para um número com ponto flutuante.
</p>

```python
 int(5.4)
```

```python
 int(-8.4)
```

```python
 float(125)
```

#### HEXADECIMAL E BINÁRIO

<p
  align="capitalize"
>
  Com as funções <strong>hex</strong> podemos converter números inteiros para o padrão hexadecimal. <strong>Hexadecimal</strong> é um sistema de numeração posicional que representa os números em base 16, ou seja, utilizando 16 símbolos.
</p>

```python
 hex(3900)
```

```python
 hex(10)
```

<p
  align="capitalize"
>
  Com a função <strong>bin</strong> podemos converter números inteiros em binário. O Sitema de Numeração <strong>Binário</strong> ou de base 2 é um sistema de numeração posicional em que todas as quantidades estão representadas com base em apenas dois números.
</p>

```python
 bin(23)
```

```python
 hex(7090)
```

<br
/>

## VARIÁVEIS

<p
  align="capitalize"
>
  Uma
  <a
    href="https://realpython.com/python-variables/"
  >
    Variável
  </a>
  é como um nome anexado a um objeto específico. No Python, as variáveis não precisam ser declaradas ou definidas com antecedência, como é o caso em muitas outras linguagens de programação. Para criar uma variável, basta atribuir um valor e começar a usá-lo. A atribuição é feita com um único sinal de igual (=).
</p>
<br
/>

```python
 teste = 1
```

<p
  align="capitalize"
>
  O valor pode ser impresso na tela utilizando a função built-in
  <strong
  >
    print()
  </strong>
</p>

```python
 print(teste)
```

<p
  align="capitalize"
>
  Podemos alterar o valor dessa variável, assim como exibilo em uma prompt intérprete em uma sessão REPL(Read–eval–print loop) sem a necessidade de <strong>print()</strong>.
</p>

```python
 teste = 1000
 teste
```

<p
  align="capitalize"
>
  Também é possível fazer declarações multiplas de variáveis, seja esse a um mesmo valor, como a valores diferentes.
</p>

```python
 x, y, z = 153
 x, y, z = 100, 50, 3
```

<p
  align="capitalize"
>
  Em muitas linguagens de programação, as variáveis são digitadas estaticamente, como tendo inicialmente um tipo de dados específico, e qualquer valor atribuído a ela durante sua vida útil tem sempre esse tipo de valor. No Python as variáveis não estão sujeitas a esta restrição. Aqui uma variável pode receber um valor de um tipo e, posteriormente, reatribuir um valor de um tipo diferente.
</p>

```python
  example = 22.37
  print(example)
  # 22.37

  example = 'Eu sou groot!'
  print(example)
  # Eu sou groot!
```

<p
  align="capitalize"
>
  As variáveis em Python podem ser escritas com letras, números e underline, mas não podem começar com números.
</p>

```python
 name01 = 'Coffee'
 numbers = 12321
```

<p
  align="capitalize"
>
  O python é <a href="https://pt.wikipedia.org/wiki/Case-sensitive">case-sensitive</a> o que significa que as palavras depois da primeira são capitalizadas. Não se limitando a isso, assim como na maioria das linguagens de programação, podemos utilizar <strong>Snake Case</strong> ou <strong>Pascal Case</strong> na hora de escrever suas variáveis.
</p>

```python
 MyName = 'Armando Silva'
 myName = 'Armando Silva'
 my_name = 'Armando Silva'
```

<p
  align="capitalize"
>
  As palavras reservadas em Python, nomes de funções especias no idioma. Até o Python 3.6 eram 33 palavras reservadas.
</p>

<h3
  align="capitalize"
>
  <img
    src="./screens/reserved_words.svg"
  />
</h3>

<p
  align="capitalize"
>
  Essas palavras não podem ser usadas como nome de variáveis.
</p>

```python
 and = 'Let is go'
 # SyntaxError: sintaxe inválida
```

## STRINGS

<p
  align="capitalize"
>
  <a
    href=""
  >
    Strings
  </a> não apenas em <strong>Python</strong>, como na maioria das linguagens de programação, são conjuntos de caracteres de texto que podem ser compreendidos como representações de informações escritas dentro de um código
</p>

```python
 'Isso é uma String!'
```

<p
  align="capitalize"
>
  Podemos criar uma string em Python usando aspas simples ou duplas e podemos imprimir uma variável com um valor tipo <strong>String</strong> usando a função built-in <strong>print()</strong>
</p>

```python
 'String com aspas simples'
```

```python
 "String com aspas duplas"
```

```python
 print("Imprimindo uma String em uma variável com aspas duplas e 'Simples'")
```

```python
 # É possível utilizar o \n para quebra de linha em uma STRING
 print('A primeira quebra de linha.\n Segunda quebra de linha! \n')
```

### INDEXAÇÃO DE STRINGS

<p
  align="capitalize"
>
  Para fazer a indexação de uma String é necessário usar colchetes <strong>[ ]</strong> para manipular o texto de diversas formas.
</p>

```python
 index = 'Estou estudando na Data Science Academy'

 print(index)
```

<p
  align="capitalize"
>
  Ao indexar uma String podemos retornar o primeiro caractere <code>index[0]</code> e podemos retornar qualquer caractere apartir daí.
</p>

```python
 index[0]
 # 'E'
```

```python
 index[6]
 # 'e'
```

<p
  align="capitalize"
>
  Podemos usar um <strong>:</strong> para executar um <strong>slicing</strong> que faz a leitura de tudo até um ponto designado, lembrando que a indexação em Python começa pela posição 0.
</p>

```python
 # Retorna todos os elementos da string, começando pela posição até o fim da string.
 index[1:]
```

```python
 # A String original permanece a mesma.
 print(index)
```

```python
 # Retorna tudo até a posição 5
 index[:5]
```

```python
 # Retorna a string inteira
 index[:]
```

```python
 # Podemos usar indexação negativa e retorna a string de trás para frente
 index[-1]
```

```python
 # Retornando tudo exceto o último caractere
 index[:-1]
```

<p
  align="capitalize"
>
 É possível utilizar a notação de índice e fatiar a <strong>string</strong> em pedaços específicos (o padrão é 1). Podemos usar dois pontos duas vezes em uma linha e, em seguida, um número que especifica a frequência para retornar elementos.
</p>

```python
 index[::1]
 # 'Estou estudando na Data Science Academy'
```

```python
 index[::2]
 # 'Etuetdnon aaSineAaey'
```

```python
 index[::-1]
 # 'ymedacA ecneicS ataD an odnadutse uotsE'
```

### PROPRIEDADES DE STRINGS

```python
 course = 'Python Fundamentos para Análise de Dados'
```

<p
  align="capitalize"
>
 Não é possível alterar uma String em Python, mas é possível concatenar uma String, mas uma String é um objeto imutável.
</p>

```python
 # Alterando um caractere
 course[0] = 'J'
```

```python
 # Concatenando uma string
 course + 'é o melhor curso de fundamentos python.'
```

```python
 course = course + 'é o melhor curso de fundamentos python.'
```

```python
 print(course)
```

```python
 # Podemos utilizar o símbolo de multiplicação para fazer repetição de caracteres.
 letra = 'AV'
 letra * 5
```

### FUNÇÕES BUILTIN-IN DE STRINGS

```python
 name = 'Data Science Academy'
```

<p
  align="capitalize"
>
  Para converter uma
  <code
  >
    string</code>
  para converter um texto para caixa alta ou maiusculas podemos utilizar o método <code
  >
    upper()</code>.
</p>

```python
 # Upper Case
 name.upper()
```

<p
  align="capitalize"
>
  Para converter para <strong
  >lower case</strong> é utilizado o método <code
  >lower()</code>.
</p>

```python
 # Lower Case
 name.lower()
```

<p
  align="capitalize"
>
  Para dividir uma string por espaços é utilizado o método <code
  >split()</code>
</p>

```python
 name.split()
 # ['Data', 'Science', 'Academy']
```

<p
  align="capitalize"
>
  O método
  <code
  >join()</code> retorna uma string na qual os elementos da sequência foram unidos por um separador <strong>str</strong>.
</p>

```python
 join_name = ''
 join_name = join_name.join(name)
 # 'Data Science Academy'
```

<p
  align="capitalize"
>
  O método
  <code
  >strip()</code> remove os espaços em branco no começo e no final de uma
  <strong
  >
    string
  </strong>.
</p>

```python
 name = '  Python para Análise de Dados   '
 name.strip()
 # 'Python para Análise de Dados'
```

<p
  align="capitalize"
>
  O método
  <code
  >len()</code> mostra a quantidade de caracteres de uma
  <strong
  >
    string
  </strong>.
</p>

```python
 x = 'Python para Análise de Dados'
 len(x)
 # 28
```

<p
  align="capitalize"
>
  O método
  <code
  >find()</code> localiza dentro uma
  <strong
  >
    string
  </strong> um conjunto de caracteres.
</p>

```python
 x = 'Python para Análise de Dados'
 x.find('Dados')
 # 23
```

<br
/>

### FUNÇÕES STRING

<br
/>

<p
  align="capitalize"
>
  Funções String são funções especificas para strings.
</p>

```python
  x = 'Seja bem-vindo ao Universo🌎 de Python'
```

<p
  align="capitalize"
>
  A funçao
  <strong
  >
  Capitalize
  </strong>
  é utilizada para deixar o primeiro caractere como maiúscula.
</p>

```python
  x.capitalize()
  # SEJA BEM-VINDO AO UNIVERSO DE PYTHON
```

<p
  align="capitalize"
>
  A funçao
  <strong
  >
  Count
  </strong>
  retorna a primeira ocorrência do caractere dentro do primeiro conjunto caracteres em que ele está presente.
</p>

```python
  x.count('b')
  # 0
```

<p
  align="capitalize"
>
  A funçao
  <strong
  >
  Find
  </strong>
  retorna a primeira ocorrência do caractere dentro da string comleta.
</p>

```python
  x.find('b')
  # 6
```

### OPERADORES RELACIONAIS

<p
  align="capitalize"
>
  <strong
  >
    Operadores Relacionais
  </strong>
   são normalmente usados ​​em contextos booleanos como instruções condicionais e de loop para direcionar o fluxo do programa, podendo ser usado com strings e vários outros tipos de dados e em contextos diferentes.
</p>

<h3
  align="center"
>
  <img
    src="./screens/relational-operator-in-python.png"
  />
</h3>

<br
/>

## LISTAS

<p
  align="capitalize"
>
  Uma lista (list) em Python é uma estrutura de dados utilizada para criar sequências ou coleções ordenadas de valores. Cada valor na lista é identificado por um índice. O valores que formam uma lista são chamados elementos ou itens.

  Para criar uma lista de dados é necessário inserir os dados entre colchetes <strong>[ ]</strong>.
</p>

```python
  lista_da_feira = [ 'laranjas', 'maçãs', 'farinha', 'queijo' ]
```

```python
  # Imprimindo uma lista em python

  print(lista_da_feira)
  # ['laranjas', 'maçãs', 'farinha', 'queijo']
```

<p
  align="capitalize"
>
  Para imprimir um item da lista pelo indice, é utilizado a mesma marcação que em variáveis do tipo String, utilizando colchetes com o número da posição em que o item se encontra.
</p>

```python
  lista_da_feira[2]
```

### USANDO DADOS DIFERENTES EM UMA LISTA
<p
  align="capitalize"
>
  Também é possível criar listas com vários tipos de dados diferentes já que as listas em python não possuem restrição de tipo. 
</p>

```python
  # Lista com valores de tipos diferentes
  lista_variada = [300, 8.2, "Análise de Dados", true]
```

```python
  # Definindo cada da lista a uma variável
  valor_number = lista_variada[0]
  valor_float = lista_variada[1]
  valor_string = lista_variada[2]
  valor_boolean = lista_variada[3]
```

<br
/>

### ATUALIZANDO ITEMS NA LISTA

<br/>

<p
  align="capitalize"
>
  Para atualizar um item em uma lista é preciso definir pelo indice qual item queremos atualizar.
</p>

```python
  lista_variada[1]
```

<p
  align="capitalize"
>
  Depois é possível definir por qual item ele deve ser alterado utilizando o operador de igual <strong>=</strong>.
</p>

```python
  lista_variada[1] = 'banana'
```

```python
  print(lista_variada)
  # [300, 8.2, 'banana', true]
```


### DELETANDO UM ITEM EM UMA LISTA

<p
  align="capitalize"
>
  Para se deletar um item especifico em uma lista é utilizada a mesma notação de indice, mas dessa vez é utilizado a função <strong>del</strong> na frente da expressão.
</p>

```python
  # Deletando um item da lista
  del lista_variada[2]
```

```python
  # Imprimindo a lista com os dados alterados
  print(lista_variada)
```

<br/>

### LISTAS ANINHADAS

<p
  align="capitalize"
>
  Como as listas em Python não tem restrição de tipo fixo, é possível fazer aninhamento de listas, ou seja, colocar listas dentro de outras listas, e até mesmo fazer o agrupamento de um conjunto de listas.
</p>

```python
  lista_de_listas = [[1, 9, 4], [23, 8, 12], [21, 22, 7.8]]
```

```python
  print(lista_de_listas)
  # [[1, 9, 4], [23, 8, 12], [21, 22, 7.8]]
```

<p
  align="capitalize"
>
  Também é possível fazer o fatiamento de listas aninhadas.
</p>

```python
  listas_tipos = [[23, 22, 15], ['Uva', 'Maçã', 'Maracujá'], [31.34, 11.97, 8.12]]
```

```python
  lista_de_inteiros = listas_tipos[0]
  lista_de_strings = listas_tipos[1]
  lista_de_floats = listas_tipos[2]
  print(lista_de_inteiros, lista_de_strings, lista_de_floats)
```

```python
  primeiro_inteiro = lista_de_inteiros[0]
  segunda_string = lista_de_strings[1]
  terceiro_float = lista_de_floats[2]

  print(primeiro_inteiro, segunda_string, terceiro_float)
```



## DICIONÁRIOS

<p
  align="capitalize"
>
  Dicionários em Python é uma estrutura de dados formada apartir de uma coleção de items armazenada de formas não ordenada, seus elementos contém uma chave e um valor. A chave serve para indexar o elemento dentro do dicionário e o valor pode ser definido como qualquer valor aceitável ou estrutura de dados dentro do Python.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sua sintáxe básica é formada por <strong>chaves { }</strong>, e os valores chave e valor são separados por <strong>dois pontos :</strong> dentro da sintáxe do python, ou seja dicionários são mapeamentos de chaves e valores
</p>

<h6
  align="center"
>
  <img
    src="./screens/dicinonarios-python.png"
    alt="Imagem de direito autoral da TreinaWeb, essa imagem apresenta o nome dicionários com a logo do Python e um exemplo da estrutura de dados dicionário"
    width="650em"
  />
</h6>

### CRIANDO DICIONÁRIOS

<p
  align="capitalize"
>
  Existem basicamente 6 maneiras de se criar um dicionário em Python.
</p>

<p
  align="capitalize"
>
  1ª Podemos criar um dicionário da forma mais tradicional, atribuindo dentro de uma variável a abertura de uma chave, e inserindo pares chaves e valor, separando os valores com <strong>dois pontos <code>:</code></strong>, e depois fechado chaves.
</p>

```python
>>> feira = { 'morangos': 24, 'bananas': 18, 'laranjas': 12, 'melancias': 3 }
```

<p
  align="capitalize"
>
  2ª Também é possível utilizar a função built-in <code>dict</code> passando as chaves e valores como parâmetros.
</p>

```python
>>> feira = dict(morangos=24, bananas=18, laranjas=12, melancias=3)
```

<p
  align="capitalize"
>
  3ª Utilizando a função <code>zip</code> para concatenar listas para <code>chave:valor</code> dentro de um objeto <code>dict</code>.
</p>

```python
>>> feira = dict(zip(['moragos', 'laranjas', 'melancias'], [24, 18, 3]))
```

<p
  align="capitalize"
>
  4ª Utilizando uma lista de tuplas com items simbolizando <code>chave</code> e <code>valor</code> em um objeto <code>dict</code>.
</p>

```python
>>> feira = dict([('laranjas', 24), ('melancias', 3), ('morangos', 36)])
```

<p
  align="capitalize"
>
  5ª Utilizando um Dict Comprehensions
</p>

```python
>>> feira = {name: idx + 1 for idx, name in enumerate(('morangos', 'laranjas', 'melancias'))}
```

<p
  align="capitalize"
>
  6ª A forma mais estranha de se criar um dicionário é transformar um dicionário em dicionário.
</p>

```python
>>> feira = dict({ 'morangos': 24, 'bananas': 18, 'laranjas': 12, 'melancias': 3 })
```

### Acessando Items e obtendo chave e valor

<p
  align="capitalize"
>
  Para acessar um item dentro de um dicionário em python, podemos utilizar a chave dentro da indexação.
</p>

```python
>>> profile = { name: 'Armando Silva', age: 50, height: 1.70 }
>>> profile[name]
```

<br
/>


## TÚPLAS

<br
/>

## EXERCÍCIOS

<br
/>

## GAME

<br
/>
