# Atividade Prática 1
x = int(input())
y = int(input())
print(f"Media = {(x + y) / 2:.1f}")

# Atividade Prática 2
lado = float(input())
print(f"Area.....: {lado**2:.2f}")
print(f"Perimetro: {4*lado:.2f}")
print(f"Diagonal.: {lado*2**(1/2):.2f}")

# Atividade Prática 3
x = int(input())
print(f"antecessor: {x-1}")
print(f"numero....: {x}")
print(f"sucessor..: {x+1}")

# Atividade Prática 4
salario = float(input())
reajuste = float(input())
print(f"Salario atual....: R$ {salario:.2f}")
print(f"Valor do reajuste: R$ {reajuste*salario/100:.2f} ({reajuste:.2f}%)")
print(f"Salario novo.....: R$ {salario*(1+reajuste/100):.2f}")

# Atividade Prática 5
x = int(input())
y = int(input())
print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} X {y} = {x*y}")
print(f"{x} / {y} = {x//y}")
print(f"{x} / {y} = {x/y:.2f}")
