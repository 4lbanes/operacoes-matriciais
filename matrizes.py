def menu():
  print('Bem vindo a matriz dinâmica!')
  while True:
    print('\nEscolha um dos itens abaixo para realizar uma operação desejada por você:')
    print('1 - Cadastrar Matrizes/Vetores')
    print('2 - Multiplicar as matrizes/vetores por um inteiro')
    print('3 - Calcular a transposta de uma matriz/vetor')
    print('4 - Calcular a soma das duas matrizes/vetores cadastradas')
    print('5 - Multiplicar as 2 matrizes/vetores cadastradas')
    print('6 - Escalonar Matriz')
    print('7 - Resolver sistema linear a partir da matriz')
    print('0 - Para sair')

    opcao = int(input("Digite o item desejado: "))

    if opcao == 0:
       print('\nSaindo...\n')
       break

    if opcao == 1:
     A, B = cadastrar_valores()

     for linha in A:
        print(linha)

     for linha in B:
        print(linha)

    if opcao == 2:
      x = int(input('\nInsira o valor inteiro de x que irá multiplicar todos os elementos da matriz A: '))
      y = int(input('\nInsira o valor inteiro de y que irá multiplicar todos os elementos da matriz B: '))

      Ax, By = multiplicar_por_inteiro(A, B, x, y)
      
      for linha in Ax:
         print(linha)
      
      print()

      for linha in By:
         print(linha)

    if opcao == 3:
      C = calcular_transposta(A)
      D = calcular_transposta(B)

      for linha in C:
         print(linha)

      print()

      for linha in D:
         print(linha)

    if opcao == 4:
       matriz_resultante = soma_matrizes(A, B)

       for linha in matriz_resultante:
          print(linha)

    if opcao == 5:
       multiplicar_matrizes(A, B)
       
    if opcao == 6:
       escalonar_matriz(A)
       for linha in A:
          print(linha)

    if opcao == 7:
       resolucao = solve(A)
       print(resolucao)
       
def cadastrar_valores():
    A = []

    la = int(input('\nInsira aqui a quantidade de linhas da sua Matriz A: '))
    ca = int(input('Insira aqui a quantidade de colunas da sua Matriz A: '))

    for j in range(la):
        vetor_a = []
        for i in range(ca):
            a = int(input('Insira aqui os valores que vão compor a sua Matriz/Vetor A: '))
            vetor_a.append(a)
        A.append(vetor_a)

    B = []

    lb = int(input('\nInsira aqui a quantidade de linhas da sua Matriz B: '))
    cb = int(input('Insira aqui a quantidade de colunas da sua Matriz B: '))

    for j in range(lb):
        vetor_b = []
        for i in range(cb):
            b = int(input('Insira aqui os valores que vão compor a sua Matriz/Vetor B: '))
            vetor_b.append(b)
        B.append(vetor_b)

    return A, B

def multiplicar_por_inteiro(A, B, x, y):
    A_multiplicada = []

    for linha in A:
        vetor_multiplicado_a = []
        for numero in linha:
            numero *= x
            vetor_multiplicado_a.append(numero)
        A_multiplicada.append(vetor_multiplicado_a)

    B_multiplicada = []

    for linha in B:
        vetor_multiplicado_b = []
        for numero in linha:
            numero *= y
            vetor_multiplicado_b.append(numero)
        B_multiplicada.append(vetor_multiplicado_b)

    return A_multiplicada, B_multiplicada

def calcular_transposta(M):
    M_transposta = []

    for j in range(len(M[0])):
        nova_linha = []
        for i in range(len(M)):
            nova_linha.append(M[i][j])
        M_transposta.append(nova_linha)

    return M_transposta

def soma_matrizes(A, B):
   if len(A) != len(B) and len(A[0]) != len(B[0]):
      print('\nAs linhas e colunas de A devem ser iguais as linhas e colunas de B!\n')

   matriz_resultante = []

   for j in range(len(A)):
      matriz_resultante.append([])
      for i in range(len(A[0])):
         sum = A[j][i] + B[j][i]
         matriz_resultante[j].append(sum)

   return matriz_resultante

def multiplicar_matrizes(A, B):
   Y = []

   if len(A[0]) == len(B):
      for j in range(len(A)):
         vetor = []
         Y.append(vetor)
         for i in range(len(B[0])):
            Y[j].append(0)

      for j in range(len(A)):
         for i in range(len(B[0])):
            sum = 0
            for l in range(len(A[0])):
               sum += A[j][l] * B[l][i]
            Y[j][i] = sum

      for linha in Y:
         print(linha)

   else:
      print('\nOrdens de matrizes não permite o produto matricial\n')

def escalonar_matriz(A):
    for i in range(len(A)):
        pivo = A[i][i]

        if pivo != 0:
            for j in range(len(A[0])):
                A[i][j] /= pivo

        for k in range(i + 1, len(A)):
            const = A[k][i]
            for j in range(len(A)):
                A[k][j] -= const * A[i][j]

def solve(A): 
    for i in range(len(A)):
        pivot = A[i][i]

        if pivot != 0:
            for j in range(len(A) + 1):
                A[i][j] /= pivot

            for k in range(len(A)):
                if k != i:
                    const = A[k][i]
                    for j in range(len(A) + 1):
                        A[k][j] -= const * A[i][j]

    resolucao = [[A[i][len(A)]] for i in range(len(A))]

    return resolucao

menu()
