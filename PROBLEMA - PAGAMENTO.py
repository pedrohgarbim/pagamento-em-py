nome = str(input("Nome: "))
valor = float(input("Valor por hora: "))
horas = int(input("Horas trabalhadas: "))

pagamento = valor * horas
mes = pagamento * 20

print(f"O pagamento para {nome} deve ser {pagamento:.2f}")
print(f"Ao mes, o pagamento de {nome} caso seu trabalho se mantenha constante"
      f"sera de {mes}")