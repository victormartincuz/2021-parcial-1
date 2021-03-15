def ejercicio2():
    marcas=[]
    codigos=[]
    for x in range(10):
        nom=input("Ingrese la marca del producto:")
        marcas.append(nom)
        no1=input("Ingrese Nombre del producto:")
        no2=input("Ingrese codigo de un producto:")
        codigos.append([no1,no2])
    for x in range(10):
        print(marcas[x],codigos[x][0],codigos[x][1])
ejercicio2()
