# módulo 'mostrar'
def mostrar(n):
 """
  Mostra os números de 1 até n.  
 """
 print("{ ", end="")
 for i in range(1, n+1):
  print(f"{i}", end=" ")
 print("} ", end="")

# módulo 'somar'
def somar(n):
 """
  Calcula a soma dos números de 1 até n.  
 """
 soma = 0
 for i in range(1, n+1):
  soma = soma + i
 return(soma)

# módulo 'resultados'
def resultados(n):
 """
   Mostra os números de 1 até n e a soma deles.
 """
 mostrar(n)
 print(f"soma = {somar(n)}")
 print()