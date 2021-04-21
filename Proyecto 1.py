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
        return print("Hasta luego")
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
 Cédula (10 dígitos), 
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
    Cedula=int(input("Ingrese la cédula: "))
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
def modifEmp():
    pass
"========================================================================"
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
    print(" Cedula  |  Empresa  |        Ubicación de la empresa        |   Transportes")
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
    time.sleep(0.5)
    print("El transporte ha sido agregado con éxito")
    time.sleep(0.5)
    return gestionTransporte()
"============================================="
def borrarTransport():
    return gestionTransporte()
def modifTransport():
    return gestionTransporte()
def mostrarTransport():
    time.sleep(0.5)
    print("Transportes registrados")
    print(" Matrícula  |  Marca  | Modelo | Año | Cédula de la Empresa | Asientos VIP - Normales - Económicos")
    f = open ("Transportes.txt",'r') 
    mensaje = f.read()
    print(mensaje)
    f.close()
    time.sleep(2)
    return gestionTransporte()
    
#====================================================================================================================================================
"""
gestionViaje
Esta funcion permite registrar viajes
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
    return Menu()
#====================================================================================================================================================
"""
historial
Esta funcion muestra una lista de las reservaciones generadas en el sistema.
Entradas: un menú con los siguientes filtros:
 Rango de fecha de salida, 
 Rango de fecha de llegada, 
 Rango de fecha de la reservación, 
 Lugar de salida y llegada. 
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
    pass
    return Menu()
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
    pass
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
Restricciones: La contraseña nueva no puede se r igual a la actual
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
 Empresa, 
 Lugar de salida, 
 Lugar de llegada, 
 Rango de fecha de salida y 
 Rango de fecha de llegada.
Salida: Por cada viaje debe mostrar:
         Número de viaje, 
         Ciudad salida, 
         Fecha y hora salida, 
         Ciudad de llegada, 
         Fecha y hora llegada, 
         Empresa y transporte, 
         Monto clase vip, monto clase normal y monto clase económica. 
"""
def consultaViaje():
    pass
    return usuario()
#====================================================================================================================================================
"""
reserva
Cuando se hace la reservación debe seleccionarse el viaje (mostrar al usuario información de 
número de viaje, empresa, lugar de salida y llegada, y fechas), el usuario selecciona uno.
Entradas: 
 El nombre
 La cantidad de espacios a reservar en clase vip, normal y económica. 
Salidas: Se le entregará un comprobante (se mostrará en pantalla, no debe exportarse ni imprimir) al cliente con:
         Identificador de la reserva (generado automáticamente), 
         Nombre de la persona que reserva, 
         Fecha y hora de la reservación (capturadas del sistema), 
         Empresa, 
         Transporte,
         Lugar, fecha y hora salida, lugar, fecha y hora llegada, 
         Cantidad de asientos reservados en clase vip, clase normal y clase económica, 
         Monto de reservación (calcular según cantidad, tipos y montos de asientos). 
Restricciones: para la cantidad de asientos reservados en cada categoría debe haber espacios disponibles.
                      Se deberá reservar al menos un asiento en total.
"""
def reserva():
    pass
    return usuario()
#====================================================================================================================================================
"""
cancelReserva
La función cancela una reserva de viaje
Entrada: el identificador de la reserva
Salida: debe borrar la reservación y liberar los asientos reservados
"""
def cancelReserva():
    pass
    return usuario()
