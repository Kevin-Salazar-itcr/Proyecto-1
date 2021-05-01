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
    4-  Consultar historial de reservaciones o Estadísticas de viaje
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
    f.write((Placa+" | "))
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
    eleccion=str(input("Ingrese la cédula de una empresa: "))
    f = open ("Transportes.txt",'a')
    f.write((eleccion+" | "))
    f.close()
    return asientos()
"============================================="
def asientos():
    print("Cantidad de asientos")
    VIP=str(input("Clase VIP: "))
    NORMAL=str(input("Clase Normal: "))
    ECONOM=str(input("Clase Económica: "))
    f = open ("Transportes.txt",'a')
    f.write((VIP+" - "+NORMAL+" - "+ECONOM+" | \n"))
    f.close()
    f = open ("Asientos.txt",'a')
    f.write((VIP+" - "+NORMAL+" - "+ECONOM+" \n"))
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
    eleccion=str(input("Ingrese la cédula de una empresa: "))
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
    f.write((VIP+" - "+NORMAL+" - "+ECONOM+" \n"))
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
         #====================Funciones de gestión de Transportes====================#
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
    if mensaje==[]:
        print("Esta empresa no tiene ningun transporte. Seleccione uno")
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
    if(eleccion not in mensaje[0]):
        return Aux(eleccion, mensaje[1:])
    else:
        print("Esta empresa tiene vinculado el siguiente transporte: ")
        print(mensaje[0])
        time.sleep(0.5)
        op=str(input("¿Desea agregar este?    1-si   2-no: "))
        if op=="1":
            agreg=op
            return transp(eleccion, agreg)
        else:
            print("Transportes registrados")
            print(" Matrícula  |  Marca  | Modelo | Año | Nombre de la Empresa | Asientos VIP - Normales - Económicos")
            f = open ("Transportes.txt",'r') 
            mensaje = f.read()
            print(mensaje)
            f.close()
            time.sleep(1)
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
    if mensaje==[]:
        print("Esta empresa no tiene ningun transporte. Seleccione uno")
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
    if(eleccion not in mensaje[0]):
        return NuevoAux(eleccion, mensaje[1:])
    else:
        print("Esta empresa tiene vinculado el siguiente transporte: ")
        print(mensaje[0])
        time.sleep(0.5)
        op=str(input("¿Desea agregar este?    1-si   2-no: "))
        if op=="1":
            agreg=op
            return Nuevotransp(eleccion, agreg)
        else:
            print("Transportes registrados")
            print(" Matrícula  |  Marca  | Modelo | Año | Nombre de la Empresa | Asientos VIP - Normales - Económicos")
            f = open ("Transportes.txt",'r') 
            mensaje = f.read()
            print(mensaje)
            f.close()
            time.sleep(1)
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
        return RangoSalida()
    if op==2:
        return RangoLlegada()
    if op==3:
        return RangoReserva()
    if op==4:
        salida=str(input("Escriba el lugar de salida: "))
        Llegada=str(input("Escriba el lugar de llegada: "))
        return FiltroLlegada(salida, Llegada)
    if op==5:
        return Menu()
    else:
        print("Digite una de las opciones disponibles")
        return opcionesFiltro()
#====================================================================================================================================================
"""
estadisticas
Entrada: Se debe seleccionar un viaje (se muestran al usuario los existentes)
Salidas: mostrar el siguiente detalle: 
 Número de viaje, 
 Empresa, transporte, 
 Lugar, fecha y hora salida, 
 Lugar, fecha y hora llegada, 
 Cantidad de asientos clase vip reservados y asientos clase vip disponibles, 
 Cantidad de asientos normal reservados y asientos normal disponibles, 
 Cantidad de asientos económico reservados y asientos económico disponibles, 
 Costo por boleto vip, normal y económico, 
 Monto recaudado por el viaje. "
"""
def estadisticas():
    print("Funcion no disponible")
    return Menu()
#====================================================================================================================================================
def avanzado(): #Función que sirve como menú
    print("""
1-  Cambio de contraseña
2-  Acerca de
3-  Volver
""")
    return op2()
def op2():
    op=str(input("Seleccione una opción: "))
    if op=="1":
        return cambio()
    elif op=="2":
        return info()
    elif op=="3":
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
        return FiltroEmpresa()
    if(op=="2"):
        return FiltroSalida()
    if(op=="3"):
        return FiltroLlegada()
    if(op=="4"):
        return FiltroFechaSalida()
    if(op=="5"):
        return FiltroFechaLlegada()
    if(op=="6"):
        return usuario()
    else:
        print("Digite una de las opciones disponibles")
        return OPCIONES()
    #Apartado para los filtros
def FiltroEmpresa():
    print("Funcion no disponible")
    return consultaViaje()
def FiltroSalida():
    print("Funcion no disponible")
    return consultaViaje()
def FiltroLlegada():
    print("Funcion no disponible")
    return consultaViaje()
def FiltroFechaSalida():
    print("Funcion no disponible")
    return consultaViaje()
def FiltroFechaLlegada():
    print("Funcion no disponible")
    return consultaViaje()
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
        dato=list((str(mensaje[0]))[5:])
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
    print("Empresa y transporte: ", datos[4:6])
    print("Lugar, fecha y hora salida | lugar, fecha y hora llegada")
    print(datos[0], ", ",datos[1], " | ",datos[2], ", ",datos[3])
    print("Cantidad de asientos reservados: " )
    print("Clase VIP:            ", VIP)
    print("Clase normal:        ", NORMAL)
    print("Clase económica:  ", ECONOM)
    print("Montos por asientos: " )
    print("Clase VIP:            ", VIP*int(datos[6]))
    print("Clase normal:        ", NORMAL*int(datos[7]))
    print("Clase económica:  ", ECONOM*int(datos[8]))
    total=(VIP*int(datos[6])+NORMAL*int(datos[7])+ECONOM*int(datos[8]))
    print("      Monto total: ", total)
    f=open("Reservas.txt", "a")         
    f.write(str(identif)+"|"+nombre+"|"+str(ya)+"|"+str(datos[4])+", "+str(datos[5])+"|"+str(datos[0])+ ", "+str(datos[1])+ "|"+str(datos[2])+ ", "+str(datos[3])+"|"+str(VIP)+"|"+str(NORMAL)+"|"+str(ECONOM)+"|"+str(total))
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
