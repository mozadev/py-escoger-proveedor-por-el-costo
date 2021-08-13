print("           ****************************")
print("           *    PEREIRA Y ASOCIADOS   *")
print("           ****************************")

total1=0
total2=0
total3=0
men = 999999999999999999

Ortega=[8.55,9.15,12.00,12.10, 20.00, 0.22]
DISENSA=[07.85,08.95,14.50,12.60,21.20,0.21]
Fernandez=[08.00,09.50,10.50,11.50,23.50,0.25]
materiales=["Cemento         ", "Empaste Interior","Empaste Exterior", "ceramica        ", "Pintura         ", "Ladrillo        "]
empresas=["Ortega","DISESA", "Fernandez"]
print("Tipo de material", "    Ortega", "     DISENSA", "    Fernandez")
for tabla in range (0,6):
    print(materiales[tabla], "    $", Ortega[tabla], "     $",DISENSA[tabla], "       $",Fernandez[tabla])
print("******************************************************")


cantidades1=[]
for i in range(6):
    cantidades1.append([0]*1)
for cantidad in range (0,6):
    x=float(input("Ingrese la cantidad del material de la primera obra: "))
    cantidades1[cantidad]=x
for i in range (6):
    subtotal=cantidades1[i]*Ortega[i]
    subtotal1=cantidades1[i]*DISENSA[i]
    subtotal2=cantidades1[i]*Fernandez[i]
    total1=total1+subtotal
    total2=total2+subtotal1
    total3=total3+subtotal2
total=[total1,total2,total3]
i=1
while(i<=3):
    if (total[i-1]<men):
        men=total[i-1]
        nombre1=empresas[i-1]
    i=i+1
print(" ")
print("Para la primera obra es más económico adquirir los materiales del proveedor ",nombre1, "al precio de: $",men)
print(" ")


total1=0
total2=0
total3=0
subtotal=0
subtotal1=0
subtotal2=0
men=9999999999
cantidades2=[]
for i in range(6):
    cantidades2.append([0]*1)
for cantidad in range (0,6):
    x=float(input("Ingrese la cantidad del material de la segunda obra: "))
    cantidades2[cantidad]=x
for i in range (6):
    subtotal=cantidades2[i]*Ortega[i]
    subtotal1=cantidades2[i]*DISENSA[i]
    subtotal2=cantidades2[i]*Fernandez[i]
    total1=total1+subtotal
    total2=total2+subtotal1
    total3=total3+subtotal2
total=[total1,total2,total3]
i=1
while(i<=3):
    if (total[i-1]<men):
        men=total[i-1]
        nombre1=empresas[i-1]
    i=i+1
print(" ")
print("Para la segunda obra es más económico adquirir los materiales del proveedor ",nombre1, "al precio de: $",men)
print(" ")


total1=0
total2=0
total3=0
subtotal=0
subtotal1=0
subtotal2=0
men=9999999999
cantidades3=[]
for i in range(6):
    cantidades3.append([0]*1)
for cantidad in range (0,6):
    x=float(input("Ingrese la cantidad del material de la tercera obra: "))
    cantidades3[cantidad]=x
for i in range (6):
    subtotal=cantidades3[i]*Ortega[i]
    subtotal1=cantidades3[i]*DISENSA[i]
    subtotal2=cantidades3[i]*Fernandez[i]
    total1=total1+subtotal
    total2=total2+subtotal1
    total3=total3+subtotal2
total=[total1,total2,total3]
i=1
while(i<=3):
    if (total[i-1]<men):
        men=total[i-1]
        nombre1=empresas[i-1]
    i=i+1
print(" ")
print("Para la tercera obra es más económico adquirir los materiales del proveedor ",nombre1, "al precio de: $",men)
print(" ")
print("Presione <ENTER> para continuar...")
input()