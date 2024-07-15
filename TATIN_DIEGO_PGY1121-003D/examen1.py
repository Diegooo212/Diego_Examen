from os import system
system("cls")
import random
empleados=["Juan Perez","Maria Garcia","Carlos Lopez"
           ,"Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez"
           ,"Isabel Gomez","Francisco Diaz","Elena Fernandez"]
sueldos=[(random.randint(300000,2500000)),(random.randint(300000,2500000))
         ,(random.randint(300000,2500000)),(random.randint(300000,2500000))
         ,(random.randint(300000,2500000)),(random.randint(300000,2500000))
         ,(random.randint(300000,2500000)),(random.randint(300000,2500000))
         ,(random.randint(300000,2500000)),(random.randint(300000,2500000))]
total=[]
sueldo_empleados=[]
cantmenos=0
cantentre=0
cantsuperior=0
while True:
    print("""
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadisticas
4. Reporte de sueldos
5. Salir del programa""")
    
    op=input("Ingrese una opcion")
    if op=="1":
        for i in range(10):
            print(f"NOMBRE EMPLEADO: {empleados[0+i]} SUELDO: {sueldos[0+i]}")
            total=(empleados[0+i],sueldos[0+i])
            sueldo_empleados.append(total)

    elif op=="0":
        input("Finalizando programa...")
        print("Desallorado por Diego Tatin")
        print("RUT 21.591.665-0")
        break

    elif op=="2":
            print("   ")
            print(f"Sueldos menores a $800.000 ")
            print("NOMBRE EMPLEADO     SUELDO")
            for total in sueldo_empleados:
                if (total[1])<800000:
                    print(f"""{total[0]}     {total[1]}""")
            print("   ")
            print(f"Sueldos entre $800.000 y $2.000.000 ")
            print("NOMBRE EMPLEADO     SUELDO")
            for total in sueldo_empleados:
                if (total[1])>=800000 and (total[1])<=2000000:
                    print(f"""{total[0]}     {total[1]}""")
            print("   ")
            print(f"Sueldos superiores a $2.000.000")
            print("NOMBRE EMPLEADO     SUELDO")
            for total in sueldo_empleados:
                if (total[1])>2000000:
                    print(f"""{total[0]}     {total[1]}""")
