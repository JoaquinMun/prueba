import json, csv, unicodedata

datos = [[72642413-6,"Comercial Calcetas Runner",150000000],
[76437473-2,"Reparación Mac",300000000],
[76254356-9,"ProgramaSoftware",27500000],
[76077262-3,"Calzados Roma",15000000],
[76310800-8,"Empresa Arcos",80000000],
[76283690-4,"Casino Coffe",120000000],
[76952985-5,"Cafe Express ltda",50000000],
[76081440-2,"Vino Export SA",20000000],
[76216579-1,"Cepa Merl LTDA",30000000],
[76597875-0,"Comercial Ropa America",60000000],
[76852106-3,"Empresas JP",90000000],
[76887745-8,"Empresas ICata SA",100000000],
[76210124-2,"Buses Peñalolen",150000000],
[76802052-4,"Sandiasaine LTD PA",70000000],
[76575973-1,"Modas Junior P",400000000],
[76869384-2,"Bar del 81",25000000],
[76877803-6,"Empresas LLS",8000000],
[76706124-0,"Empresas luz y vida SA",3000000]   
]

with open("Empresas.csv","w") as listaEmpresa:
    escribircsv=csv.writer(listaEmpresa)
    escribircsv.writerow(("rut","Empresa","Ventas"))
    escribircsv.writerows(datos)
datosccv = []
  
with open("Empresas.csv","r") as listaEmpresa:
    leer= csv.DictReader(listaEmpresa)
    for i in leer:
        ventas2 = int(i["Ventas"])
        calficaciones = (
            "Pequeñas Ventas" if ventas2 < 100000000 else 
            "Medianas Ventas" if ventas2 < 200000000 else 
            "Grndes Ventas" )
        i["calficaciones"] = calficaciones
        datosccv.append(i)
        
        
with open("Orden.json","w") as datosjson:
    json.dump(datosccv,datosjson, indent=4)     





    """ import json
idboleta=0
opcion =0
while opcion!=6:
    print("1 - Mantenedor de Servicios")
    print("2 - Tienda")
    print("3 - Servicios")
    print("6 - Salir")
    opcion=int(input(" "))

    if opcion==1:
        print("1 - Mantenedor de Productos")
        print("2 - Mantenedor de Usuarios")
        print("3 - Mantenedor de Vendedores")
        print("4 - Mantenedor de Boletas")
        opcion=int(input(" "))
        if opcion==1:
            with open ("diccionario/compras.json","r") as archivojsproduc:
                leerproductos=json.load(archivojsproduc)
                productos=[]
                productos.append(leerproductos["productos"])
            with open ("diccionario/comprasproduc.json","w") as archivojsproduc:
             json.dump(productos,archivojsproduc,indent=4)
        if opcion==2:
            with open ("diccionario/compras.json","r") as archivojsusuario:
                leerusuarios=json.load(archivojsusuario)
                usuarios=[]
                usuarios.append(leerproductos["clientes"])
            with open ("diccionario/comprasusuarios.json","w") as archivojsusuario:
             json.dump(usuarios,archivojsusuario,indent=4)
        if opcion==3:
            with open ("diccionario/compras.json","r") as archivojsvendedores:
                leervendedores=json.load(archivojsvendedores)
                vendedores=[]
                vendedores.append(leervendedores["vendedores"])
            with open ("diccionario/comprasVendedores.json","w") as archivojsvendedores:
             json.dump(vendedores,archivojsvendedores,indent=4)
"
"""