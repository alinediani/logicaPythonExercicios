vendedor = str(input())
salarioFixo = "%0.2f" %float(input())
totalVendas = "%0.2f" %float(input())
totalReceber = ((float(totalVendas)/100)*15)+float(salarioFixo)
totalReceberC = "%0.2f" %totalReceber
print("TOTAL = R$ "+totalReceberC)
