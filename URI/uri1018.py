valor = int(input())
print(valor)

cem = int(valor / 100)
valor-=cem*100
cinq = int(valor / 50)
valor-=cinq*50
vinte = int(valor / 20)
valor-=vinte*20
dez = int(valor/10)
valor-=dez*10
cinco = int(valor/5)
valor-=cinco*5
dois = int(valor/2)
valor-=dois*2
um = int(valor/1)

print("""{0} nota(s) de R$ 100,00
{1} nota(s) de R$ 50,00
{2} nota(s) de R$ 20,00
{3} nota(s) de R$ 10,00
{4} nota(s) de R$ 5,00
{5} nota(s) de R$ 2,00
{6} nota(s) de R$ 1,00""".format(cem, cinq, vinte, dez, cinco, dois, um))
