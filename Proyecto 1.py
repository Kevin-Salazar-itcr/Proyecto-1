"Proyecto 1- Kevin Salazar"
import time
print("Aplicacion()")
"Aplicación: función que almacena el menú principal"
def Aplicacion():
    print("Bienvenido(a)")
    time.sleep(1)
    return menu_Principal()
#====================================================================================================================================================
def menu_Principal():    #Funcion que sirve como menú
    print("""
Menú:
1- Opciones administrativas
2- Opciones de usuario normal
3- Salir""")
    time.sleep(0.5)
    return opcion()
#====================================================================================================================================================
def opcion():
    op=str(input("Seleccione una opción: "))
    if(op=="1"):
        return clave()
    if(op=="2"):
        return usuario()
    if(op=="3"):
        print("""
¿Está seguro que desea salir?
    1-si      2-no""")
        op2=str(input("Digite una opción: "))
        if(op2=="1"):
            time.sleep(0.5)
            print("Hasta la próxima")
            print("")
            print("")
            print("")
            time.sleep(2)
            return print("Aplicacion()")
        elif(op2=="2"):
            print(opcion())
        else:
            print("Digite una de las opciones disponibles")
            time.sleep(0.5)
            print(opcion())
    else:
        print("Digite una de las opciones disponibles")
        time.sleep(0.5)
        print(menu_Principal())
#====================================================================================================================================================
def clave():    #Funcion para permitir acceso a determinadas funciones
    clave=input("Digite la contraseña: ")
    f=open("contraseña.txt", "r")
    contraseña=f.read()
    f.close()
    return valid(clave, contraseña, 2) #Inicialmente hay 3 intentos. Al primer error, quedarán 2 (ese 2 se imprime con el mensaje de error)
def valid(clave, contraseña, intentos):
    if(clave==contraseña):
        print("Acceso concedido")
        return administrativo()
    else:
        if(intentos==0):
            print("Contraseña inválida. inténtelo de nuevo en 30 segundos")
            time.sleep(3)
            print("Por favor espere...")
            time.sleep(27)
            intentos=2
            clave=input("Digite la contraseña: ")
            return valid(clave, contraseña, intentos)
        else:
            print("La contraseña es incorrecta. Quedan ", intentos, "intentos.")
            clave=input("Digite la contraseña: ")
            return valid(clave, contraseña, intentos-1)
#====================================================================================================================================================
def administrativo():       
    print("Bienvenido al control administrativo.")
    time.sleep(0.5)
    return Menu()
def Menu():     #Funcion que sirve como menú
    print("""
Menú
    1-  Gestión de empresas
    2-  Gestión de transporte por empresa 
    3-  Gestión de viajes
    4-  Consultar el historial de reservaciones
    5-  Estadísticas de viajes
    6-  Funciones avanzadas
    7-  Volver
    """)
    return admin()
def admin():    
    op=str(input("Seleccione una opción: "))
    if(op=="1"):
        return gestionEmpresa()
    if(op=="2"):
        return gestionTransporte()
    if(op=="3"):
        return gestionViaje()
    if(op=="4"):
        return historial()
    if(op=="5"): 
        return estadisticas()
    if(op=="6"):
        return avanzado()
    if(op=="7"):
        return menu_Principal()
    else:
        print("Digite una de las opciones disponibles")
        return admin()
#====================================================================================================================================================
def usuario():    #Funcion que sirve como menú
    print("""
Menú
    1-  Consulta de viajes 
    2-  Reservación de viaje 
    3-  Cancelación de reservación 
    4-  Salir
    """)
    return entrada()
def entrada():
    op=str(input("Seleccione una opción: "))
    if(op=="1"):
        return consultaViaje()
    if(op=="2"):
        return reserva()
    if(op=="3"):
        return cancelReserva()
    if(op=="4"):
        print("Hasta luego")
        print("")
        print("")
        print("")
        time.sleep(2)
        return print("Aplicacion()")
    else:
        print("Digite una de las opciones disponibles")
        return entrada()
#====================================================================================================================================================
                                                                                     #===================Apartado para funciones auxiliares======================#
#====================================================================================================================================================
#====================================================================================================================================================
                                                                                          #================Funciones dirigidas al administrador"====================#
#====================================================================================================================================================
"Funciones de gestión administrativa"
"""
gestionEmpresa
Esta funcion permite dar mantenimiento a las empresas.
Entradas por empresa:
 Cédula (10 dígitos)
 Nombre  
 Ubicación (dirección del negocio).
Salidas: Permite incluir empresas
             eliminar empresas
             modificar empresas 
             mostrar las empresas
Restricciones: No pueden existir empresas con la misma cédula
                      No pueden eliminarse empresas que hayan sido asociados algún transporte. 
"""
def gestionEmpresa():
    print("""
Menu:
    1- Incluir empresas
    2- Eliminar empresas
    3- Modificar empresas
    4- Mostrar empresas
    5- Volver
    """)
    return Opcion()
def Opcion():
    op=str(input("Seleccione una opción: "))
    if(op=="1"):
        return incluirEmp()
    if(op=="2"):
        return borrarEmp()
    if(op=="3"):
        return modifEmp()
    if(op=="4"):
        return mostrarEmp()
    if(op=="5"):
        return Menu()
    else:
        print("digite una de las opciones disponibles")
        return Opcion()
         #====================Funciones de gestión de empresas====================#
"""
incluirEmp
Esta funcion agrega una nueva empresa
E: Cédula 
    Nombre  
    Ubicación (dirección del negocio)
S: Se debe agregar el contacto al archivo Empresas.txt
R: La cédula debe tener 10 dígitos
    No pueden existir 2 empresas con la misma cédula
"""
def incluirEmp():
        return AgregarCedula()
"============================================="
def contarDigitos(num):
    if (num<=9):
        return 1
    else:
        return 1+contarDigitos(num//10)
def AgregarCedula():
    Cedula=int(input("Ingrese la cédula jurídica: "))
    if(contarDigitos(Cedula)!=10):
        print("La cédula debe tener 10 dígitos")
        return AgregarCedula()
    else:
        f=open("Empresas.txt",'r')
        mensaje = f.readlines()
        f.close()
        Cedula=str(Cedula)
        return verificar(Cedula, mensaje)
"============================================="
def verificar(Cedula, mensaje):
    Cedula=str(Cedula)
    if mensaje==[]:
        return agregar(Cedula)
    if(Cedula not in mensaje[0]):
        return verificar(Cedula, mensaje[1:])
    else:
        print("Error: la cédula ya está relacionada a una empresa")
        return AgregarCedula()
"============================================="
def agregar(Cedula):
    f = open ("Empresas.txt",'a')
    f.write((Cedula+" | "))
    f.close()
    return nombreEmpresa()
"============================================="
def nombreEmpresa():
    Nombre=str(input("Nombre de la entidad: "))
    f = open ("Empresas.txt",'a')
    f.write((Nombre+" | "))
    f.close()
    return ubicacion()
"============================================="
def ubicacion():
    ubic=str(input("Dirección de la empresa: "))
    f = open ("Empresas.txt",'a')
    f.write((ubic+" | \n"))
    f.close()
    time.sleep(0.5)
    print("La empresa ha sido agregada con éxito")
    time.sleep(0.5)
    return gestionEmpresa()
"========================================================================"
"""
borrarEmp
Esta función sirve para borrar una empresa del registro
E: numero de cedula de la empresa
S: Debe borrar la empresa identificada con la cédula
R: No se puede borrar a empresas relacionadas con un transporte
"""
def borrarEmp():
    ClaveBorrar=(input("Digite el número de cédula: "))
    return revisarTransporte(ClaveBorrar)
def revisarTransporte(ClaveBorrar):
    archivo=open("Transportes.txt", "r")
    mensaje= archivo.readlines()
    archivo.close()
    return revisarAux(ClaveBorrar, mensaje)
def revisarAux(ClaveBorrar, mensaje):
    if mensaje==[]:
        return borrarEmpAux(ClaveBorrar)
    if(ClaveBorrar not in mensaje[0]):
        return revisarAux(ClaveBorrar, mensaje[1:])
    else:
        print("Error: No se pudo borrar la empresa porque está vinculada a un transporte")
        return borrarEmp()
def borrarEmpAux(ClaveBorrar):
    f = open("Empresas.txt","r")
    lineas = f.readlines()
    f.close()
    f = open("Empresas.txt","w")
    for linea in lineas:
        if ClaveBorrar not in linea:
            f.write(linea)
    f.close()
    print("La empresa ha sido eliminada")
    time.sleep(0.5)
    return gestionEmpresa()
"========================================================================"
"""
modifEmp
Esta función es capaz de modificar los campos de una empresa.
E: La cédula jurídica de la empresa
S: Podrá modificarse el nombre de la empresa y su ubicación
"""
def modifEmp():
    f=open("Empresas.txt", "r")
    texto= f.read()
    n = 0
    for i in texto:
        if i == "\n":
            n+=1
    f.close
    
    if (n==0):
        print("Actualmente no hay empresas para modificar")
        time.sleep(0.5)
        return gestionEmpresa()
    else:
        return modEmp()
"============================================="  
def modEmp():
    cedula=(input("Digite la cédula de la empresa a modificar: "))
    f=open("Empresas.txt",'r')
    mensaje = f.readlines()
    f.close()
    cedula=str(cedula)
    return modAux(cedula, mensaje)
def modAux(cedula, mensaje):
    if mensaje==[]:
        print("Esta empresa no existe en los registros")
        return gestionEmpresa() 
    if(cedula not in mensaje[0]):
        return modAux(cedula, mensaje[1:])
    else:
        print("    Cedula     |    Empresa    |   Ubicación de la empresa   ")
        print(mensaje[0])
        time.sleep(1)
        return modAux2(cedula)
def modAux2(cedula):
    f = open("Empresas.txt","r")
    lineas = f.readlines()
    f.close()
    f = open("Empresas.txt","w")
    for linea in lineas:
        if cedula not in linea:
            f.write(linea)
    f.close()
    f = open ("Empresas.txt",'a')
    f.write((cedula+" | "))
    f.close()
    return nuevoEmpresa()
"============================================="
def nuevoEmpresa():
    Nombre=str(input("Nuevo nombre de empresa: "))
    f = open ("Empresas.txt",'a')
    f.write((Nombre+" | "))
    f.close()
    return nuevoUbicacion()
"============================================="
def nuevoUbicacion():
    ubicac=str(input("Dirección de la empresa: "))
    f = open ("Empresas.txt",'a')
    f.write((ubicac+" | "))
    f.close()
    time.sleep(0.5)
    print("La empresa ha sido actualizada") 
    time.sleep(0.5)
    return gestionEmpresa() 
"========================================================================"
"""
mostrarEmp
Muestra una lista con todas las empresas
"""
def mostrarEmp():
    time.sleep(0.5)
    print("Empresas registradas")
    print("    Cedula     |    Empresa    |   Ubicación de la empresa   ")
    f = open ("Empresas.txt",'r') 
    mensaje = f.read()
    print(mensaje)
    f.close()
    time.sleep(2)
    return gestionEmpresa()
#====================================================================================================================================================
"""
gestionTransporte
Esta funcion permite dar mantenimiento a los transportes
(buseta, limosina, avión, jet privado...)
Entradas por transporte:
 placa
 Marca  
 Modelo
 Año
 Empresa (una de la lista de empresas)
 Cantidad de asientos
        clase VIP
        clase normal
        clase económica
Salidas: Permite incluir transportes
             eliminar transportes
             modificar transportes
             mostrar los transportes
 Restricciones: No pueden existir 2 transportes con la misma placa
                      No pueden eliminarse transportes que estén registrados en un viaje 
"""
def gestionTransporte():
    print("""
Menu:
    1- Incluir transportes
    2- Eliminar transportes
    3- Modificar transportes
    4- Mostrar transportes
    5- Volver
    """)
    return OPC()
def OPC():
    op=str(input("Seleccione una opción: "))
    if(op=="1"):
        return incluirTransport()
    if(op=="2"):
        return borrarTransport()
    if(op=="3"):
        return modifTransport()
    if(op=="4"):
        return mostrarTransport()
    if(op=="5"):
        return Menu()
    else:
        print("digite una de las opciones disponibles")
        return OPC()
         #====================Funciones de gestión de Transportes====================#
"""
incluirTransport
Esta funcion permite incluir transportes
Entradas
 placa (6 digitos)
 Marca  
 Modelo
 Año
 Empresa (una de la lista de empresas) 'Se usa como entrada la cedula de la empresa'
 Cantidad de asientos
        clase VIP
        clase normal
        clase económica
Salidas: Agrega el transporte en el archivo 'Transportes.txt'
 Restricciones: No pueden existir 2 transportes con la misma placa
                      No pueden eliminarse transportes que estén registrados en un viaje 
"""
def incluirTransport():
    return AgregarPlaca()
"============================================="
def AgregarPlaca():
    Placa=int(input("Ingrese el número de matrícula: "))
    if(contarDigitos(Placa)!=6):
        print("La placa debe tener 6 dígitos")
        return AgregarPlaca()
    else:
        f=open("Transportes.txt",'r')
        mensaje = f.readlines()
        f.close()
        Placa=str(Placa)
        return Matricula(Placa, mensaje)
"============================================="
def Matricula(Placa, mensaje):
    if mensaje==[]:
        return AddMatricula(Placa)
    if(Placa not in mensaje[0]):
        return Matricula(Placa, mensaje[1:])
    else:
        print("Error: El número de matrícula pertenece a otro transporte")
        return AgregarPlaca()
"============================================="
def AddMatricula(Placa):
    f = open ("Transportes.txt",'a')
    f.write((Placa+" | "))
    f.close()
    f = open ("Asientos.txt",'a')
    f.write((Placa+"|"))
    f.close()
    return Marca()
"============================================="
def Marca():
    marca=str(input("Marca del transporte: "))
    f = open ("Transportes.txt",'a')
    f.write((marca+" | "))
    f.close()
    return Modelo()
"============================================="
def Modelo():
    modelo=str(input("Modelo: "))
    f = open ("Transportes.txt",'a')
    f.write((modelo+" | "))
    f.close()
    return Year()
"============================================="
def Year():
    year=str(input("Año: "))
    f = open ("Transportes.txt",'a')
    f.write((year+" | "))
    f.close()
    return Empresa()
"============================================="
def Empresa():
    time.sleep(0.5)
    print("Empresas registradas")
    print(" Cedula  |  Empresa  |        Ubicación de la empresa        ")
    f = open ("Empresas.txt",'r') 
    mensaje = f.read()
    print(mensaje)
    f.close()
    time.sleep(2)
    eleccion=str(input("Ingrese el nombre de una empresa: "))
    f = open ("Transportes.txt",'a')
    f.write(eleccion+" | ")
    f.close()
    return asientos()
"============================================="
def asientos():
    print("Cantidad de asientos")
    VIP=str(input("Clase VIP: "))
    NORMAL=str(input("Clase Normal: "))
    ECONOM=str(input("Clase Económica: "))
    f = open ("Transportes.txt",'a')
    f.write(VIP+" - "+NORMAL+" - "+ECONOM+" | \n")
    f.close()
    f = open ("Asientos.txt",'a')
    f.write(VIP+"|"+NORMAL+"|"+ECONOM+" \n")
    f.close()
    time.sleep(0.5)
    print("El transporte ha sido agregado con éxito")
    time.sleep(0.5)
    return gestionTransporte()
"============================================="
def borrarTransport():
    Borrar=(input("Digite el número de matrícula: "))
    return verificacionTransp(Borrar)
def verificacionTransp(Borrar):
    archivo=open("Viajes.txt", "r")
    mensaje= archivo.readlines()
    archivo.close()
    return VerifTransAux(Borrar, mensaje)
def VerifTransAux(Borrar, mensaje):
    if mensaje==[]:
        return borrarTranspAux(Borrar)
    if(Borrar not in mensaje[0]):
        return VerifTransAux(Borrar, mensaje[1:])
    else:
        print("Error: No se pudo borrar. El transporte está registrado en un viaje")
        return borrarTransport()
def borrarTranspAux(Borrar):
    f = open("Transportes.txt","r")
    lineas = f.readlines()
    f.close()
    f = open("Transportes.txt","w")
    for linea in lineas:
        if Borrar not in linea:
            f.write(linea)
    f.close()
    f = open("Asientos.txt","r")
    lineas = f.readlines()
    f.close()
    f = open("Asientos.txt","w")
    for linea in lineas:
        if Borrar not in linea:
            f.write(linea)
    f.close()
    time.sleep(0.5)
    print("El transporte ha sido eliminado")
    time.sleep(0.5)
    return gestionTransporte()
"============================================="
"""
modifTransport
Esta función es capaz de modificar los campos de un transporte.
E: El numero de matrícula del transporte
S: Podrá modificarse cada uno de los campos del transporte
"""
def modifTransport():
    f=open("Transportes.txt", "r")
    texto= f.read()
    n = 0
    for i in texto:
        if i == "\n":
            n+=1
    f.close
    
    if (n==0):
        print("Actualmente no hay Transportes para modificar")
        time.sleep(0.5)
        return gestionTransporte()
    else:
        return modTrp()
"============================================="  
def modTrp():
    placa=(input("Digite la matrícula del transporte a modificar: "))
    f=open("Transportes.txt",'r')
    mensaje = f.readlines()
    f.close()
    placa=str(placa)
    return modTrpAux(placa, mensaje)
def modTrpAux(placa, mensaje):
    if mensaje==[]:
        print("El vehículo no aparece en los registros")
        return gestionTransporte() 
    if(placa not in mensaje[0]):
        return modTrpAux(placa, mensaje[1:])
    else:
        print(" Matrícula  |  Marca  | Modelo | Año |  Empresa  | Asientos VIP - Normales - Económicos")
        print(mensaje[0])
        time.sleep(1)
        return modTrpAux2(placa)
def modTrpAux2(placa):
    f = open("Transportes.txt","r")
    lineas = f.readlines()
    f.close()
    f = open("Transportes.txt","w")
    for linea in lineas:
        if placa not in linea:
            f.write(linea)
    f.close()
    f = open ("Transportes.txt",'a')
    f.write((placa+" | "))
    f.close()
    f = open("Asientos.txt","r")
    lineas = f.readlines()
    f.close()
    f = open("Asientos.txt","w")
    for linea in lineas:
        if placa not in linea:
            f.write(linea)
    f.close()
    f = open ("Asientos.txt",'a')
    f.write((placa+"|"))
    f.close()
    return nuevoMarca()
"============================================="
def nuevoMarca():
    marca=str(input("Marca del transporte: "))
    f = open ("Transportes.txt",'a')
    f.write((marca+" | "))
    f.close()
    return nuevoModelo()
"============================================="
def nuevoModelo():
    modelo=str(input("Modelo: "))
    f = open ("Transportes.txt",'a')
    f.write((modelo+" | "))
    f.close()
    return nuevoAño()
"============================================="
def nuevoAño():
    year=str(input("Año: "))
    f = open ("Transportes.txt",'a')
    f.write((year+" | "))
    f.close()
    return nuevoEmpresaTrp()
"============================================="
def nuevoEmpresaTrp():
    time.sleep(0.5)
    print("Empresas registradas")
    print(" Cedula  |  Empresa  |        Ubicación de la empresa        ")
    f = open ("Empresas.txt",'r') 
    mensaje = f.read()
    print(mensaje)
    f.close()
    time.sleep(2)
    eleccion=str(input("Ingrese el nombre de una empresa: "))
    f = open ("Transportes.txt",'a')
    f.write((eleccion+" | "))
    f.close()
    return nuevoAsientos()
"============================================="
def nuevoAsientos():
    print("Cantidad de asientos")
    VIP=str(input("Clase VIP: "))
    NORMAL=str(input("Clase Normal: "))
    ECONOM=str(input("Clase Económica: "))
    f = open ("Transportes.txt",'a')
    f.write((VIP+" - "+NORMAL+" - "+ECONOM+" | \n"))
    f.close()
    f = open ("Asientos.txt",'a')
    f.write((VIP+"|"+NORMAL+"|"+ECONOM+" \n"))
    f.close()
    time.sleep(0.5)
    print("El transporte ha sido actualizado") 
    time.sleep(0.5)
    return gestionTransporte()
"============================================="
def mostrarTransport():
    time.sleep(0.5)
    print("Transportes registrados")
    print(" Matrícula  |  Marca  | Modelo | Año |  Empresa  | Asientos VIP - Normales - Económicos")
    f = open ("Transportes.txt",'r') 
    mensaje = f.read()
    print(mensaje)
    f.close()
    time.sleep(2)
    return gestionTransporte()
"==========================================================="
"""
gestionViaje
Esta funcion permite incluir, eliminar, modificar y mostrar viajes
Entradas por viaje
 Número de viaje (autogenerado)
 Ciudad de salida
 Fecha y hora de salida
 Ciudad de llegada
 Fecha y hora de llegada
 Empresa y transporte
 Monto de asiento
        clase VIP
        clase normal
        clase económica
Salidas: Registra la información del viaje
Restricciones: Ninguna
"""
def gestionViaje():
    print("""
Menu:
    1- Incluir viajes
    2- Eliminar viajes
    3- Modificar viajes
    4- Mostrar viajes
    5- Volver
    """)
    return OPCION()
def OPCION():
    op=str(input("Seleccione una opción: "))
    if(op=="1"):
        return incluirViaje()
    if(op=="2"):
        return borrarViaje()
    if(op=="3"):
        return modifViaje()
    if(op=="4"):
        return mostrarViaje()
    if(op=="5"):
        return Menu()
    else:
        print("digite una de las opciones disponibles")
        return OPCION()
         #====================Funciones de gestión de viajes====================#
def incluirViaje():
    return NumViaje()
"============================================="
import random
def NumViaje():
    NumViaje=random.randint(1000, 9999)
    f=open("Viajes.txt",'r')
    mensaje = f.readlines()
    f.close()
    NumViaje=str(NumViaje)
    return Revision(NumViaje, mensaje)
"============================================="
def Revision(NumViaje, mensaje):  #Funcion para que no se repitan numeros de viaje
    if mensaje==[]:
        return ViajeNum(NumViaje)
    if(NumViaje not in mensaje[0]):
        return Revision(NumViaje, mensaje[1:])
    else:
        return NumViaje()  
"============================================="
def ViajeNum(NumViaje):
    print("Número de viaje: "+NumViaje)
    f = open ("Viajes.txt",'a')
    f.write((NumViaje+"|"))
    f.close()
    f = open ("Precios.txt",'a')
    f.write((NumViaje+"|"))
    f.close()
    return Salida()
"============================================="
def Salida():
    Salida=str(input("Ciudad de salida: "))
    FechaSalida=(input("Ingrese la fecha de salida en formato dd/mm/aaaa: "))
    HoraSalida=(input("Ingrese la hora de salida en formato '00-24' h: "))
    Llegada=str(input("Ciudad de llegada: "))
    FechaLlegada=(input("Ingrese la fecha de llegada en formato dd/mm/aaaa: "))
    HoraLlegada=(input("Ingrese la hora de llegada en formato '00-24' h: "))
    f=open("Viajes.txt", "a")
    f.write(Salida+"|"+FechaSalida+" "+HoraSalida+"|"+Llegada+"|"+FechaLlegada+" "+HoraLlegada+"|")
    f.close()     #Esta es la unica manera en que funciona. Si separaba y validaba cada input, el archivo no compilaba...
    return EmpresaViaje()
"============================================="
def EmpresaViaje():
    time.sleep(0.5)
    print("Empresas registradas")
    print(" Cedula  |  Empresa  |        Ubicación de la empresa        |   Transportes")
    f = open ("Empresas.txt",'r') 
    mensaje = f.read()
    print(mensaje)
    f.close()
    time.sleep(2)
    eleccion=str(input("Ingrese el nombre de una empresa: "))
    return Transporte(eleccion) 
"============================================="
def Transporte(eleccion):
    f=open("Transportes.txt", "r")
    mensaje=f.readlines()
    f.close()
    return Aux(eleccion, mensaje)
def Aux(eleccion, mensaje):
    time.sleep(0.5)
    print("Transportes registrados")
    print(" Matrícula  |  Marca  | Modelo | Año | Nombre de la Empresa | Asientos VIP - Normales - Económicos")
    f = open ("Transportes.txt",'r') 
    mensaje = f.read()
    print(mensaje)
    f.close()
    time.sleep(2)
    agreg=str(input("Ingrese el número de matrícula del transporte: "))
    return transp(eleccion, agreg)
def transp(eleccion, agreg):
    f = open ("Viajes.txt",'a')
    f.write((eleccion+"|"+agreg+"|"))
    f.close()
    time.sleep(0.5)
    return Montos()
"============================================="
def Montos():
    print("Monto por asientos")
    VIP=str(input("Clase VIP: "))
    NORMAL=str(input("Clase Normal: "))
    ECONOM=str(input("Clase Económica: "))
    f = open ("Viajes.txt",'a')
    f.write((VIP+"|"+NORMAL+"|"+ECONOM+"\n"))
    f.close()
    f = open ("Precios.txt",'a')
    f.write((VIP+"|"+NORMAL+"|"+ECONOM+"\n"))
    f.close()
    time.sleep(0.5)
    print("El viaje ha sido agregado con éxito")
    time.sleep(0.5)
    return gestionViaje()
"============================================="
"""
borrarViaje
Esta función sirve para borrar un viaje del registro
E: numero de viaje
S: Debe borrar el viaje
R: Ninguna
"""
def borrarViaje():
    viaje=(input("Digite el número de viaje: "))
    f = open("Viajes.txt","r")
    lineas = f.readlines()
    f.close()
    f = open("Viajes.txt","w")
    for linea in lineas:
        if viaje not in linea:
            f.write(linea)
    f.close()
    f = open("Precios.txt","r")
    lineas = f.readlines()
    f.close()
    f = open("Precios.txt","w")
    for linea in lineas:
        if viaje not in linea:
            f.write(linea)
    f.close()
    print("Se ha eliminado el viaje")
    time.sleep(0.5)
    return gestionViaje()
"=============================================="
"""
modifViaje
Esta función es capaz de modificar los campos de un viaje.
E: El numero de viaje
S: Podrá modificarse cada uno de los campos del viaje
"""
def modifViaje():
    f=open("Viajes.txt", "r")
    texto= f.read()
    n = 0
    for i in texto:
        if i == "\n":
            n+=1
    f.close
    if (n==0):
        print("Actualmente no hay viajes para modificar")
        time.sleep(0.5)
        return gestionViaje()
    else:
        return modVj()
"============================================="  
def modVj():
    viaje=(input("Digite la matrícula del transporte a modificar: "))
    f=open("Viajes.txt",'r')
    mensaje = f.readlines()
    f.close()
    viaje=str(viaje)
    return modVjAux(viaje, mensaje)
def modVjAux(viaje, mensaje):
    if mensaje==[]:
        print("El viaje no se encuentra registrado")
        return gestionViaje() 
    if(viaje not in mensaje[0]):
        return modVjAux(viaje, mensaje[1:])
    else:
        print("N° viaje | Ciudad salida | Fecha/hora salida | Ciudad llegada | Fecha/hora llegada | Empresa | Transporte | Montos VIP - Normales - Económicos")
        print(mensaje[0])
        time.sleep(1)
        return modVjAux2(viaje)
def modVjAux2(viaje):
    f = open("Viajes.txt","r")
    lineas = f.readlines()
    f.close()
    f = open("Viajes.txt","w")
    for linea in lineas:
        if viaje not in linea:
            f.write(linea)
    f.close()
    f = open ("Viajes.txt",'a')
    f.write((viaje+"|"))
    f.close()
    f = open("Precios.txt","r")
    lineas = f.readlines()
    f.close()
    f = open("Precios.txt","w")
    for linea in lineas:
        if viaje not in linea:
            f.write(linea)
    f.close()
    f = open ("Precios.txt",'a')
    f.write((viaje+"|"))
    f.close()
    return nuevoSalida()
"=============================================="
def nuevoSalida():
    Salida=str(input("Ciudad de salida: "))
    FechaSalida=(input("Ingrese la fecha de salida en formato dd/mm/aaaa: "))
    HoraSalida=(input("Ingrese la hora de salida en formato '00-24' h: "))
    Llegada=str(input("Ciudad de llegada: "))
    FechaLlegada=(input("Ingrese la fecha de llegada en formato dd/mm/aaaa: "))
    HoraLlegada=(input("Ingrese la hora de llegada en formato '00-24' h: "))
    f=open("Viajes.txt", "a")
    f.write(Salida+"|"+FechaSalida+" "+HoraSalida+"|"+Llegada+"|"+FechaLlegada+" "+HoraLlegada+"|")
    f.close()
    return NuevoEmpresaViaje()
"============================================="
def NuevoEmpresaViaje():
    time.sleep(0.5)
    print("Empresas registradas")
    print(" Cedula  |  Empresa  |        Ubicación de la empresa        |   Transportes")
    f = open ("Empresas.txt",'r') 
    mensaje = f.read()
    print(mensaje)
    f.close()
    time.sleep(2)
    eleccion=str(input("Ingrese el nombre de una empresa: "))
    return NuevoTransporte(eleccion) 
"============================================="
def NuevoTransporte(eleccion):
    f=open("Transportes.txt", "r")
    mensaje=f.readlines()
    f.close()
    return NuevoAux(eleccion, mensaje)
def NuevoAux(eleccion, mensaje):
    time.sleep(0.5)
    print("Transportes registrados")
    print(" Matrícula  |  Marca  | Modelo | Año | Nombre de la Empresa | Asientos VIP - Normales - Económicos")
    f = open ("Transportes.txt",'r') 
    mensaje = f.read()
    print(mensaje)
    f.close()
    time.sleep(2)
    agreg=str(input("Ingrese el número de matrícula del transporte: "))
    return Nuevotransp(eleccion, agreg)

def Nuevotransp(eleccion, agreg):
    f = open ("Viajes.txt",'a')
    f.write((eleccion+"|"+agreg+"|"))
    f.close()
    time.sleep(0.5)
    return NuevoMontos()
"============================================="
def NuevoMontos():
    print("Monto por asientos")
    VIP=str(input("Clase VIP: "))
    NORMAL=str(input("Clase Normal: "))
    ECONOM=str(input("Clase Económica: "))
    f = open ("Viajes.txt",'a')
    f.write((VIP+"|"+NORMAL+"|"+ECONOM+"\n"))
    f.close()
    f = open ("Precios.txt",'a')
    f.write((VIP+"|"+NORMAL+"|"+ECONOM+"\n"))
    f.close()
    time.sleep(0.5)
    print("El viaje ha sido actualizado")
    time.sleep(0.5)
    return gestionViaje()
"=============================================="
"""
mostrarViaje
Esta funcion muestra una lista con todos los viajes registrados en el sistema
"""
def mostrarViaje():
    time.sleep(0.5)
    print("Viajes registrados")
    print("N° viaje | Ciudad salida | Fecha/hora salida | Ciudad llegada | Fecha/hora llegada | Empresa | Transporte | Montos VIP - Normales - Económicos")
    f = open ("Viajes.txt",'r') 
    mensaje = f.read()
    print(mensaje)
    f.close()
    time.sleep(2)
    return gestionViaje()
#====================================================================================================================================================
"""
historial
Esta funcion muestra una lista de las reservaciones generadas en el sistema.
Entradas: un menú con los siguientes filtros:
 Rango de fecha de salida
 Rango de fecha de llegada 
 Rango de fecha de la reservación
 Lugar de salida y llegada
Salidas: Por cada reservación, debe mostrar
         Identificador
         Nombre de la persona que reserva
         Número de viaje
         Fecha y hora de la reservación
         Empresa, transporte
         Lugar, fecha y hora salida
         Lugar, fecha y hora llegada
         Cantidad de asientos reservados en clase vip, clase normal y clase económica
         Monto de reservación. 
Restricciones: Ninguna
"""
def historial():
    print("""
Menú de filtros:
 1- Rango de fecha de salida
 2- Rango de fecha de llegada
 3- Rango de fecha de reservación
 4- Lugar de salida y llegada
 5- Volver
""")
    return opcionesFiltro()
def opcionesFiltro():
    op=int(input("Seleccione una opción: "))
    if op==1:
        salida=str(input("Escriba una fecha:"))
        return RangoSalida(salida)
    if op==2:
        llegada=str(input("Escriba una fecha:"))
        return RangoLlegada(llegada)
    if op==3:
        reserva=str(input("Escriba una fecha:"))
        return RangoReserva(reserva)
    if op==4:
        salida=str(input("Escriba el lugar de salida: "))
        Llegada=str(input("Escriba el lugar de llegada: "))
        return FiltroLlegada(salida, Llegada)
    if op==5:
        return Menu()
    else:
        print("Digite una de las opciones disponibles")
        return opcionesFiltro()
"========================================================================="
         #====================Funciones del historial de reservas====================#
def RangoSalida(salida):
    f=open("Reservas.txt",'r')
    mensaje = f.readlines()
    f.close()
    return buscar1(salida, mensaje, 0)
def buscar1(salida, mensaje, cont):
    if mensaje==[]:
        if cont==0:
            print("No se encontraron coincidencias")
            time.sleep(0.5)
            return historial()
        else:
            print("Total de coincidencias: ", cont)
            time.sleep(1)
            return historial()
    if(salida not in mensaje[0]):
        return buscar1(salida, mensaje[1:], cont)
    else:
        print("Id reserva |   cliente  | N° viaje | Fecha/hora de reserva | Empresa, transporte | Lugar, fecha y hora salida | Lugar, fecha y hora llegada |asientos VIP| normal | económico | Monto de reserva")
        print(mensaje[0])
        time.sleep(1)
        return buscar1(salida, mensaje[1:], cont+1)

"=============================================================="
def RangoLlegada(llegada):
    f=open("Reservas.txt",'r')
    mensaje = f.readlines()
    f.close()
    return buscar2(llegada, mensaje, 0)
def buscar2(llegada, mensaje, cont):
    if mensaje==[]:
        if cont==0:
            print("No se encontraron coincidencias")
            time.sleep(0.5)
            return historial()
        else:
            print("Total de coincidencias: ", cont)
            time.sleep(1)
            return historial()
    if(llegada not in mensaje[0]):
        return buscar2(llegada, mensaje[1:], cont)
    else:
        print("Id reserva |   cliente  | N° viaje | Fecha/hora de reserva | Empresa, transporte | Lugar, fecha y hora salida | Lugar, fecha y hora llegada |asientos VIP| normal | económico | Monto de reserva")
        print(mensaje[0])
        time.sleep(1)
        return buscar2(llegada, mensaje[1:], cont+1)

"=============================================================="
def RangoReserva(reserva):
    f=open("Reservas.txt",'r')
    mensaje = f.readlines()
    f.close()
    return buscar3(reserva, mensaje, 0)
def buscar3(reserva, mensaje, cont):
    if mensaje==[]:
        if cont==0:
            print("No se encontraron coincidencias")
            time.sleep(0.5)
            return historial()
        else:
            print("Total de coincidencias: ", cont)
            time.sleep(1)
            return historial()
    if(reserva not in mensaje[0]):
        return buscar3(reserva, mensaje[1:], cont)
    else:
        print("Id reserva |   cliente  | N° viaje | Fecha/hora de reserva | Empresa, transporte | Lugar, fecha y hora salida | Lugar, fecha y hora llegada |asientos VIP| normal | económico | Monto de reserva")
        print(mensaje[0])
        time.sleep(1)
        return buscar3(reserva, mensaje[1:], cont+1)

"=============================================================="
def FiltroLlegada(salida, Llegada):
    f=open("Reservas.txt",'r')
    mensaje = f.readlines()
    f.close()
    return buscar4(salida, Llegada, mensaje, 0)
def buscar4(salida, Llegada, mensaje, cont):
    if mensaje==[]:
        if cont==0:
            print("No se encontraron coincidencias")
            time.sleep(0.5)
            return historial()
        else:
            print("Total de coincidencias: ", cont)
            time.sleep(1)
            return historial()
    if(salida not in mensaje[0]) and (Llegada not in mensaje[0]):
        return buscar4(salida, Llegada, mensaje[1:], cont)
    else:
        print("Id reserva |   cliente  | N° viaje | Fecha/hora de reserva | Empresa, transporte | Lugar, fecha y hora salida | Lugar, fecha y hora llegada |asientos VIP| normal | económico | Monto de reserva")
        print(mensaje[0])
        time.sleep(1)
        return buscar4(salida, Llegada, mensaje[1:], cont+1)

#====================================================================================================================================================
"""
estadisticas
Entrada: Se debe seleccionar un viaje (se muestran al usuario los existentes)
Salidas: mostrar el siguiente detalle: 
 Número de viaje
 Empresa, transporte
 Lugar, fecha y hora salida
 Lugar, fecha y hora llegada 
 Cantidad de asientos clase vip reservados y asientos clase vip disponibles
 Cantidad de asientos normal reservados y asientos normal disponibles
 Cantidad de asientos económico reservados y asientos económico disponibles
 Costo por boleto vip, normal y económico
 Monto recaudado por el viaje
"""
def estadisticas():
    print("A continuación, se le mostrará una lista de viajes guardados en el sistema")
    f=open("Viajes.txt", "r")
    mensaje=f.read()
    time.sleep(1)
    print("N° viaje | Ciudad salida | Fecha/hora salida | Ciudad llegada | Fecha/hora llegada | Empresa | Transporte | Montos VIP - Normales - Económicos")
    print(mensaje)
    seleccion=str(input("Seleccione uno (por número de viaje): "))
    return buscarInfo(seleccion)
def buscarInfo(seleccion):
    f=open("Viajes.txt",'r')
    mensaje = f.readlines()
    f.close()
    return EstadistViaje(seleccion, mensaje)
def EstadistViaje(seleccion, mensaje):
    if mensaje==[]:
        print("Hubo un error. No se encontraron coincidencias")
        time.sleep(0.5)
        return Menu()
    if(seleccion not in mensaje[0]):
        return EstadistViaje(seleccion, mensaje[1:])
    else:
        dato=list(str(mensaje[0]))
        return DatosViaje(seleccion, dato, [" "], [])
def DatosViaje(seleccion, dato, sub, res):
    if dato==[]:
        datos=res+[sub]
        datos=unirLista(datos)
        return seleccionar(seleccion, datos)
    if dato[0]!="|":
        return DatosViaje(seleccion, dato[1:],sub+[dato[0]], res)
    else:
        return DatosViaje(seleccion, dato[1:], [], res +[sub])
def seleccionar(seleccion, datos):
    Lug_Salida=datos[1]
    FH_Salida=datos[2]
    Lug_Llegada=datos[3]
    FH_Llegada=datos[4]
    Emp=datos[5]
    Trp=datos[6]
    MontoVIP=datos[7]
    MontoNml=datos[8]
    MontoEcm=datos[9]
    f=open("Asientos.txt", "r")
    asientos=f.readlines()
    f.close()
    return Select_Asientos(asientos, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm)
def Select_Asientos(asientos, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm):
    if asientos==[]:
        print("Hubo un error inesperado.")
        return Menu()
    if(Trp not in asientos[0]):  
        return (asientos[1:], seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm)
    else:
        asiento=(list(str(asientos[0])))
        return Select_Aux(asiento, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, [" "], [])
def Select_Aux(asiento, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, sub, res):
    if asiento==[]:
        asientos=res+[sub]
        asientos=unirLista(asientos)
        vipDisp=(asientos[1])
        normalDisp=(asientos[2])
        economDisp=(asientos[3])
        return MasDatos(asientos, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, vipDisp, normalDisp, economDisp)
    if asiento[0]!="|":
        return Select_Aux(asiento[1:], seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, sub+[asiento[0]], res)
    else:
        return Select_Aux(asiento[1:], seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, [], res +[sub])
"==============================================="
def MasDatos(asientos, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, vipDisp, normalDisp, economDisp):
    f=open("Reservas.txt", "r")
    mensaje=f.readlines()
    f.close()
    return buscarCoincidencias(mensaje, asientos, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, vipDisp, normalDisp, economDisp)
def buscarCoincidencias(mensaje, asientos, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, vipDisp, normalDisp, economDisp):
    return Coincidencias(mensaje, 0, [], asientos, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, vipDisp, normalDisp, economDisp)
def Coincidencias(mensaje, i, res, asientos, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, vipDisp, normalDisp, economDisp):
    if mensaje==[]:
        if i==0:
            return print("No se encontraron coincidencias")
        else:
            DatosReserva=res
            return seguir(DatosReserva, asientos, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, vipDisp, normalDisp, economDisp)
    if(Trp not in mensaje[0]):
        return Coincidencias(mensaje[1:], i, res, asientos, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, vipDisp, normalDisp, economDisp)
    else:
        return Coincidencias(mensaje[1:], i+1, res+[mensaje[0]], asientos, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, vipDisp, normalDisp, economDisp)
def seguir(DatosReserva, asientos, seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, vipDisp, normalDisp, economDisp):
    Datos=comprimirLista(DatosReserva)
    datos1= Datos
    datos2= Datos
    datos3= Datos
    datos4= Datos
    vipRes=relacionarAsientVIP(datos1)
    normalRes=relacionarAsientNormal(datos2)
    economRes=relacionarAsientEconom(datos3)
    Total=relacionarMontos(datos4)
    return Estadist_Final(seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, vipDisp, normalDisp, economDisp, vipRes, normalRes, economRes, Total)
def Estadist_Final(seleccion, Lug_Salida, FH_Salida, Lug_Llegada, FH_Llegada, Emp, Trp, MontoVIP, MontoNml, MontoEcm, vipDisp, normalDisp, economDisp, vipRes, normalRes, economRes, Total):
    print("Número de viaje: "+seleccion)
    print("Empresa, transporte: "+Emp+", "+Trp)
    print("Lugar, fecha y hora salida: "+Lug_Salida+", "+FH_Salida)
    print("Lugar, fecha y hora llegada: "+Lug_Llegada+", "+FH_Llegada)
    print("Asientos VIP reservados | Asientos VIP disponibles: "+vipRes+" | "+vipDisp)
    print("Asientos Normales reservados | Asientos Normales disponibles: "+normalRes+" | "+normalDisp)
    print("Asientos Económicos reservados | Asientos Económicos disponibles: "+economRes+" | "+economDisp)
    print("Costo por boleto: ")
    print("VIP: "+MontoVIP)
    print("Normal: "+MontoNml)
    print("Económico: "+MontoEcm)
    print("Monto recaudado por el viaje: "+Total)
    time.sleep(2)
    return Menu()
"==============================================="
"""
comprimirLista
Dada una lista con sublistas que contienen un texto, se descompone cada texto de sublista en palabras
(esto para seleccionar datos específicos)
"""
def comprimirLista(lista):
    if lista==[]:
        return "La lista está vacía"
    else:
        return comprimir1(lista, [])
def comprimir1(lista, RES):
    if lista==[]:
        return RES
    else:
        obj=(list(str(lista[0])))
        return comprimirObjeto(lista, obj, [" "], [], RES)
def comprimirObjeto(lista, obj, sub, res, RES):
    if obj==[]:
        datos=res+[sub]
        datos=unirLista(datos) 
        return comprimir1(lista[1:], RES+[datos])
    if obj[0]!="|":
        return comprimirObjeto(lista, obj[1:],sub+[obj[0]], res, RES)
    else:
        return comprimirObjeto(lista, obj[1:], [], res +[sub], RES)
"=================================="
def relacionarAsientVIP(datos):
    return relacionarVIP(datos, 0)
def relacionarVIP(datos, info):
    if datos==[]:
        return str(info)
    else:
        return relacVIP(datos, datos[0], 0, info)
def relacVIP(datos, dato, res1, info):
    res1+=int(dato[7])
    return relacionarVIP(datos[1:], info+res1)
"=================================="    
def relacionarAsientNormal(datos):
    return relacionarNormal(datos, 0)
def relacionarNormal(datos, info2):
    if datos==[]:
        return str(info2)
    else:
        return relacNormal(datos, datos[0], 0, info2)
def relacNormal(datos, dato, res2, info2):
    res2+=int(dato[8])
    return relacionarNormal(datos[1:], info2+res2)
"=================================="
def relacionarAsientEconom(datos):
    return relacionarEconom(datos, 0)
def relacionarEconom(datos, info3):
    if datos==[]:
        return str(info3)
    else:
        return relacEconom(datos, datos[0], 0, info3)
def relacEconom(datos, dato, res3, info3):
    res3+=int(dato[9])
    return relacionarEconom(datos[1:], info3+res3)
"=================================="
def relacionarMontos(datos):
    return MontoFinal(datos, 0)
def MontoFinal(datos, info4):
    if datos==[]:
        return str(info4)
    else:
        return MontoFinalAux(datos, datos[0], 0, info4)
def MontoFinalAux(datos, dato, res4, info4):
    res4+=int(dato[10])
    return MontoFinal(datos[1:], info4+res4)
#====================================================================================================================================================
def avanzado(): #Función que sirve como menú
    print("""
1-  Cambio de contraseña
2-  Acerca de
3-  Formatear
4-  Volver
""")
    return op2()
def op2():
    op=str(input("Seleccione una opción: "))
    if op=="1":
        return cambio()
    elif op=="2":
        return info()
    elif op=="3":
        return Formatear()
    elif op=="4":
        return Menu()
    else:
        print("Digite una de las opciones disponibles")
        return op2()
#====================================================================================================================================================
"""
cambio
Una función extra que permite al administrador cambiar la contraseña del servidor administrativo
Entrada: la contraseña actual
              la nueva contraseña
Salida: el cambio de la contraseña
Restricciones: La contraseña nueva no puede ser igual a la actual
                      La contraseña debe tener mínimo 8 caracteres
"""
def cambio():
    clave=input("Digite la contraseña: ")
    f=open("contraseña.txt", "r")
    contraseña=f.read()
    f.close()
    return valid2(clave, contraseña, 2)
def valid2(clave, contraseña, intentos):
    if(clave==contraseña):
        return cambiar(clave)
    else:
        if(intentos==0):
            print("Contraseña inválida. inténtelo de nuevo en 30 segundos")
            time.sleep(3)
            print("Por favor espere...")
            time.sleep(27)
            intentos=2
            clave=input("Digite la contraseña: ")
            return valid2(clave, contraseña, intentos)
        else:
            print("La contraseña es incorrecta. Quedan ", intentos, "intetos.")
            clave=input("Digite la contraseña: ")
            return valid2(clave, contraseña, intentos-1)
def contarString(palabra):
    if palabra=="":
        return 0
    else:
        return 1+contarString(palabra[1:])
def cambiar(clave):
    nuevo=str(input("Nueva contraseña: "))
    if(nuevo==clave):
        print("Error: la nueva contraseña no puede ser igual a la anterior.")
        return cambiar(clave)
    if(contarString(nuevo)<8):
        print("Error: la contraseña debe tener un mínimo de 8 caracteres")
        return cambiar(clave)
    else:
        f=open("contraseña.txt", "w")
        f.write(nuevo)
        f.close()
        print("La contraseña ha sido cambiada exitosamente")
        return restart()
def restart():
    print("""
¿Desea reiniciar el programa?
    1-si      2-no""")
    operac=str(input("Digite una opción: "))
    if(operac=="1"):
        print("Reiniciando")
        time.sleep(1)
        return print(menu_Principal())
    if(operac=="2"):
        return print(avanzado())
    else:
        print("Digite una de las opciones disponibles")
        time.sleep(0.5)
        return print(restart)
        
#====================================================================================================================================================
"""
info
Muestra una pequeña informacione del programa
"""
def info():
    time.sleep(1)
# 'Kuzu productions' es el nombre de un proyecto de negocios, que fue desarrollado por mí (Kevin Salazar) a finales del 2019
    print("""
         BestTraveller-Gestor de Viajes
                      Versión 1.0
             @2020-2021 Kuzu Prod.

                       Creador:
          KEVIN SALAZAR VALLES
""")
    time.sleep(0.5)
    return op2()
#====================================================================================================================================================
"""
Formatear
Elimina toda la base de datos
"""
def Formatear():
    print("Esta opción no se puede deshacer")
    return Format()
def Format():
    print("¿Está seguro que desea proceder?")
    op=int(input("1- si   2-no: "))
    if(op==1):
        return permiso()
    if(op==2):
        return avanzado()
    else:
        print("Digite una de las opciones disponibles")
        return Format()
def permiso():
    clave=input("Digite la contraseña: ")
    f=open("contraseña.txt", "r")
    contraseña=f.read()
    f.close()
    return permisoAux(clave, contraseña, 2)
def permisoAux(clave, contraseña, intentos):
    if(clave==contraseña):
        print("Formateando")
        f = open ("Asientos.txt",'w')
        f.write("")
        f.close()
        f = open ("Empresas.txt",'w')
        f.write("")
        f.close()
        f = open ("Precios.txt",'w')
        f.write("")
        f.close()
        f = open ("Reservas.txt",'w')
        f.write("")
        f.close()
        f = open ("TRansportes.txt",'w')
        f.write("")
        f.close()
        f = open ("Viajess.txt",'w')
        f.write("")
        f.close()
        time.sleep(3)
        print("Se ha eliminado toda la base de datos del programa")
        return avanzado()
    else:
        if(intentos==0):
            print("Contraseña inválida. inténtelo de nuevo en 30 segundos")
            time.sleep(3)
            print("Por favor espere...")
            time.sleep(27)
            intentos=2
            clave=input("Digite la contraseña: ")
            return permisoAux(clave, contraseña, intentos)
        else:
            print("La contraseña es incorrecta. Quedan ", intentos, "intetos.")
            clave=input("Digite la contraseña: ")
            return permisoAux(clave, contraseña, intentos-1)
#====================================================================================================================================================
                                                                                        #================Funciones dirigidas al usuario normal"====================#
#====================================================================================================================================================
"""
consultaViaje
Muestra una lista de los viajes.
Entrada: un menú con los siguientes filtros: 
 Empresa
 Lugar de salida
 Lugar de llegada
 Rango de fecha de salida
 Rango de fecha de llegada.
Salida: Por cada viaje debe mostrar:
         Número de viaje
         Ciudad salida
         Fecha y hora salida
         Ciudad de llegada
         Fecha y hora llegada
         Empresa y transporte
         Monto clase vip, monto clase normal y monto clase económica
"""
def consultaViaje():
    print("""
Menú de filtros:
    1- Empresa
    2- Lugar de salida
    3- Lugar de llegada
    4- Rango de fecha de salida
    5- Rango de fecha de llegada.
    6- Volver
""")
    return OPCIONES()
def OPCIONES():
    op=str(input("Seleccione una opción: "))
    if(op=="1"):
        Dato=str(input("Nombre de la empresa: "))
        return FiltroEmpresaViaje(Dato)
    if(op=="2"):
        Dato=str(input("Lugar de salida: "))
        return FiltroSalidaViaje(Dato)
    if(op=="3"):
        Dato=str(input("Lugar de llegada: "))
        return FiltroLlegadaViaje(Dato)
    if(op=="4"):
        Dato=str(input("Fecha de salida: "))
        return FiltroFechaSalidaViaje(Dato)
    if(op=="5"):
        Dato=str(input("Fecha de Llegada: "))
        return FiltroFechaLlegadaViaje(Dato)
    if(op=="6"):
        return usuario()
    else:
        print("Digite una de las opciones disponibles")
        return OPCIONES()
    #Apartado para los filtros
def FiltroEmpresaViaje(Dato):
    f=open("Viajes.txt",'r')
    mensaje = f.readlines()
    f.close()
    return FiltroEmpresaViajeAux(Dato, mensaje, 0)
def FiltroEmpresaViajeAux(Dato, mensaje, i):
    if mensaje==[]:
        if i==0:
            print("No se encontraron coincidencias")
            time.sleep(0.5)
            return consultaViaje()
        else:
            print("Total de coincidencias: ", i)
            time.sleep(1)
            return consultaViaje()
    if(Dato not in mensaje[0]):
        return FiltroEmpresaViajeAux(Dato, mensaje[1:], i)
    else:
        print("N° viaje | Ciudad salida | Fecha/hora salida | Ciudad llegada | Fecha/hora llegada | Empresa | Transporte | Montos VIP - Normales - Económicos")
        print(mensaje[0])
        time.sleep(1)
        return FiltroEmpresaViajeAux(Dato, mensaje[1:], i+1)
"========================================"
def FiltroSalidaViaje(Dato):
    f=open("Viajes.txt",'r')
    mensaje = f.readlines()
    f.close()
    return FiltroSalidaViajeAux(Dato, mensaje, 0)
def FiltroSalidaViajeAux(Dato, mensaje, i):
    if mensaje==[]:
        if i==0:
            print("No se encontraron coincidencias")
            time.sleep(0.5)
            return consultaViaje()
        else:
            print("Total de coincidencias: ", i)
            time.sleep(1)
            return consultaViaje()
    if(Dato not in mensaje[0]):
        return FiltroSalidaViajeAux(Dato, mensaje[1:], i)
    else:
        print("N° viaje | Ciudad salida | Fecha/hora salida | Ciudad llegada | Fecha/hora llegada | Empresa | Transporte | Montos VIP - Normales - Económicos")
        print(mensaje[0])
        time.sleep(1)
        return FiltroSalidaViajeAux(Dato, mensaje[1:], i+1)
"========================================"
def FiltroLlegadaViaje(Dato):
    f=open("Viajes.txt",'r')
    mensaje = f.readlines()
    f.close()
    return FiltroLlegadaViajeAux(Dato, mensaje, 0)
def FiltroLlegadaViajeAux(Dato, mensaje, i):
    if mensaje==[]:
        if i==0:
            print("No se encontraron coincidencias")
            time.sleep(0.5)
            return consultaViaje()
        else:
            print("Total de coincidencias: ", i)
            time.sleep(1)
            return consultaViaje()
    if(Dato not in mensaje[0]):
        return FiltroLlegadaViajeAux(Dato, mensaje[1:], i)
    else:
        print("N° viaje | Ciudad salida | Fecha/hora salida | Ciudad llegada | Fecha/hora llegada | Empresa | Transporte | Montos VIP - Normales - Económicos")
        print(mensaje[0])
        time.sleep(1)
        return FiltroLlegadaViajeAux(Dato, mensaje[1:], i+1)
"========================================"
def FiltroFechaSalidaViaje(Dato):
    f=open("Viajes.txt",'r')
    mensaje = f.readlines()
    f.close()
    return FiltroFechaSalidaViajeAux(Dato, mensaje, 0)
def FiltroFechaSalidaViajeAux(Dato, mensaje, i):
    if mensaje==[]:
        if i==0:
            print("No se encontraron coincidencias")
            time.sleep(0.5)
            return consultaViaje()
        else:
            print("Total de coincidencias: ", i)
            time.sleep(1)
            return consultaViaje()
    if(Dato not in mensaje[0]):
        return FiltroFechaSalidaViajeAux(Dato, mensaje[1:], i)
    else:
        print("N° viaje | Ciudad salida | Fecha/hora salida | Ciudad llegada | Fecha/hora llegada | Empresa | Transporte | Montos VIP - Normales - Económicos")
        print(mensaje[0])
        time.sleep(1)
        return FiltroFechaSalidaViajeAux(Dato, mensaje[1:], i+1)
"========================================"
def FiltroFechaLlegadaViaje(Dato):
    f=open("Viajes.txt",'r')
    mensaje = f.readlines()
    f.close()
    return FiltroFechaLlegadaViajeAux(Dato, mensaje, 0)
def FiltroFechaLlegadaViajeAux(Dato, mensaje, i):
    if mensaje==[]:
        if i==0:
            print("No se encontraron coincidencias")
            time.sleep(0.5)
            return consultaViaje()
        else:
            print("Total de coincidencias: ", i)
            time.sleep(1)
            return consultaViaje()
    if(Dato not in mensaje[0]):
        return FiltroFechaLlegadaViajeAux(Dato, mensaje[1:], i)
    else:
        print("N° viaje | Ciudad salida | Fecha/hora salida | Ciudad llegada | Fecha/hora llegada | Empresa | Transporte | Montos VIP - Normales - Económicos")
        print(mensaje[0])
        time.sleep(1)
        return FiltroFechaLlegadaViajeAux(Dato, mensaje[1:], i+1)
#====================================================================================================================================================
"""
reserva
Cuando se hace la reservación debe seleccionarse el viaje (mostrar al usuario información de 
número de viaje, empresa, lugar de salida y llegada, y fechas), el usuario selecciona uno.
Entradas: 
 El nombre
 La cantidad de espacios a reservar en clase vip, normal y económica. 
Salidas: Se le entregará un comprobante (se mostrará en pantalla, no debe exportarse ni imprimir) al cliente con:
         Identificador de la reserva (generado automáticamente)
         Nombre de la persona que reserva
         Fecha y hora de la reservación (capturadas del sistema)
         Empresa 
         Transporte
         Lugar, fecha y hora salida, lugar, fecha y hora llegada
         Cantidad de asientos reservados en clase vip, clase normal y clase económica
         Monto de reservación (calcular según cantidad, tipos y montos de asientos)
Restricciones: para la cantidad de asientos reservados en cada categoría debe haber espacios disponibles
                      Se deberá reservar al menos un asiento en total
"""
def reserva():
    print("Bienvenido(a) al sistema de reservas de BestTraveller")
    time.sleep(0.5)
    print("Esta es una lista de los viajes que dispone la aplicación")
    time.sleep(0.5)
    print("N° viaje | Ciudad salida | Fecha/hora salida | Ciudad llegada | Fecha/hora llegada | Empresa | Transporte | Montos VIP - Normales - Económicos")
    f=open("Viajes.txt", "r")
    mensaje=f.read()
    print(mensaje)
    f.close()
    select=str(input("Seleccione uno de los viajes (por número de viaje): "))
    return buscarViaje(select)
def buscarViaje(select):
    f=open("Viajes.txt", "r")
    mensaje=f.readlines()
    f.close()
    return buscarviaje(select, mensaje)
def buscarviaje(select, mensaje):
    if mensaje==[]:
        print("Error: El número de viaje no existe en los registros.")
        return usuario()
    if(select not in mensaje[0]):
        return buscarviaje(select, mensaje[1:])
    else:
        dato=(list(str(mensaje[0]))[0:])
        return sacarDato(select, dato,[" "], [])
def sacarDato(select, dato, sub, res):
    if dato==[]:
        datos=res+[sub]
        datos=unirLista(datos)
        return continuar(select, datos)
    if dato[0]!="|":
        return sacarDato(select, dato[1:],sub+[dato[0]], res)
    else:
        return sacarDato(select, dato[1:], [], res +[sub])
def unirLista(lista):
    return unirobj(lista, [])
def unirobj(lista, result):
    if lista==[]:
        return result
    else:
        obj=lista[0]
        result+=[unir(obj)]
        return unirobj(lista[1:], result)
def unir(lista):
    return unirAux(lista,"")
def unirAux(lista, res):
    if lista==[]:
        return res
    else:
        return unirAux(lista[1:], res+lista[0])
def continuar(select, datos):
    nombre=str(input("Escriba su nombre: "))
    return cantAsientos(select, nombre, datos)
def cantAsientos(select, nombre, datos):
    VIP=int(input("Cantidad de asientos VIP a reservar (Digite 0 si no desea reservar): "))
    NORMAL=int(input("Cantidad de asientos normales a reservar (Digite 0 si no desea reservar): "))
    ECONOM=int(input("Cantidad de asientos económicos a reservar (Digite 0 si no desea reservar): "))
    if((VIP+NORMAL+ECONOM)==0):
        print("Error: debe de reservar al menos un asiento")
        return cantAsientos(select, nombre, datos)
    else:
        return revisarAsientos(select, nombre,datos, datos[6], VIP, NORMAL, ECONOM)
def revisarAsientos(select, nombre,datos, Transporte, VIP, NORMAL, ECONOM):
    f=open("Asientos.txt", "r")
    asientos=f.readlines()
    f.close()
    return revisarAux(select, nombre,datos, Transporte, asientos, VIP, NORMAL, ECONOM)
def revisarAux(select, nombre,datos, Transporte, asientos, VIP, NORMAL, ECONOM):
    if asientos==[]:
        print("Hubo un error inesperado.")
        return usuario()
    if(Transporte not in asientos[0]):
        return revisarAux(select, nombre,datos, Transporte, asientos[1:], VIP, NORMAL, ECONOM)
    else:
        asiento=(list(str(asientos[0])))[0:-2]
        return acomodar(select, nombre,datos, asiento, VIP, NORMAL, ECONOM, [" "], [])
def acomodar(select, nombre,datos, asiento, VIP, NORMAL, ECONOM, sub, res):
    if asiento==[]:
        asientos=res+[sub]
        asientos=unirLista(asientos)
        print(asientos)
        return confirmarAsientos(select, nombre,datos, asientos, VIP, NORMAL, ECONOM)
    if asiento[0]!="|":
        return acomodar(select, nombre,datos, asiento[1:], VIP, NORMAL, ECONOM, sub+[asiento[0]], res)
    else:
        return acomodar(select, nombre,datos, asiento[1:], VIP, NORMAL, ECONOM, [], res +[sub])
def confirmarAsientos(select, nombre,datos, asientos, VIP, NORMAL, ECONOM):
    vip=int(asientos[1])
    normal=int(asientos[2])
    econom=int(asientos[3])
    if(VIP>=vip):
        print("Error: sólo hay"+" "+asientos[1]+" asientos disponible(s) en clase VIP")
        return usuario()
    if(NORMAL>=normal):
        print("Error: sólo hay"+" "+asientos[2]+" asientos disponible(s) en clase Normal")
        return usuario()
    if int(ECONOM>=econom):
        print("Error: sólo hay"+" "+asientos[3]+" asientos disponible(s) en clase Económica")
        return usuario()
    else:
        return reservarAsientos(select, nombre,datos, asientos, VIP, NORMAL, ECONOM)
def reservarAsientos(select, nombre,datos, asientos, VIP, NORMAL, ECONOM):
    f=open("Asientos.txt", "r")
    lineas=f.readlines()
    f.close()
    Trp=str(asientos[0])
    Trp=Trp[1:]
    f=open("Asientos.txt", "w")
    for linea in lineas:
        if Trp not in linea:
            f.write(linea)
        f.close()
    VIPdisp= int(asientos[1])-int(VIP)
    NMLdisp= int(asientos[2])-int(NORMAL)
    ECNdisp= int(asientos[3])-int(ECONOM)
    f=open("Asientos.txt", "a")
    f.write(str(asientos[0])+"|"+str(VIPdisp)+"|"+str(NMLdisp)+"|"+str(ECNdisp))
    f.close()
    return factura(select, nombre,datos, VIP, NORMAL, ECONOM)

from datetime import datetime
def factura(select, nombre,datos, VIP, NORMAL, ECONOM):
    print("Generando factura")
    time.sleep(1)
    identif=random.randint(1000, 9999)
    print("Comprobante de reservación ")
    print("Reservación Nº ", identif)
    print("Nombre del reservante: ", nombre)
    ya=datetime.now()
    print("Fecha y hora de reservación: ", ya)
    print("Empresa y transporte: ", datos[5:7])
    print("Lugar, fecha y hora salida | lugar, fecha y hora llegada")
    print(datos[1], ", ",datos[2], " | ",datos[3], ", ",datos[4])
    print("Cantidad de asientos reservados: " )
    print("Clase VIP:            ", VIP)
    print("Clase normal:        ", NORMAL)
    print("Clase económica:  ", ECONOM)
    print("Montos por asientos: " )
    print("Clase VIP:            ", VIP*int(datos[7]))
    print("Clase normal:        ", NORMAL*int(datos[8]))
    print("Clase económica:  ", ECONOM*int(datos[9]))
    total=(VIP*int(datos[7])+NORMAL*int(datos[8])+ECONOM*int(datos[9]))
    print("      Monto total: ", total)
    f=open("Reservas.txt", "a")         
    f.write(str(identif)+"|"+nombre+"|"+str(datos[0])+"|"+str(ya)+"|"+str(datos[5])+", "+str(datos[6])+"|"+str(datos[1])+ ", "+str(datos[2])+ "|"+str(datos[3])+ ", "+str(datos[4])+"|"+str(VIP)+"|"+str(NORMAL)+"|"+str(ECONOM)+"|"+str(total)+"\n")
    time.sleep(1)
    print("Disfrute su viaje")
    return usuario()
#====================================================================================================================================================
"""
cancelReserva
La función cancela una reserva de viaje
Entrada: el identificador de la reserva
Salida: debe borrar la reservación y liberar los asientos reservados
"""
def cancelReserva():
    cancel=str(input("Escriba el identificador de su reserva: "))
##    f=open("reservas.txt", "r")
##    mensaje = f.readlines()
##    f.close()
##    return cancelar(cancel, mensaje)
##def cancelar(cancel, mensaje):
##    if mensaje==[]:
##        print("El viaje no se encuentra registrado")
##        return usuario() 
##    if(cancel not in mensaje[0]):
##        return cancelar(cancel, mensaje[1:])
##    else:
    print("funcion no disponible")
    return usuario()
