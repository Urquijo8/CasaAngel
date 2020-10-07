import mysql.connector
import random


if __name__ == "__main__":
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    )
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM CasaAngel.users;")
    resultado = mycursor.fetchall()
    access=False
    username = (input("Ingrese usuario: "))
    password = (input("Ingrese contraseña: "))
    for x in range(len(resultado)):
        if username in resultado[x]:
            if password == resultado[x][2]:
                access=True
                print("Bienvenido {0}".format(username))
                usuario=resultado[x]
            else:
                access=False
                print("Contraseña Incorrecta")
    if access:
        ex=0
        while(ex==0):
            if 0 == usuario[3]:
                opc=int(input("1.-Consulta\n2.-Agregar Nuevo Asilado\n3.-Modificar Asildado\n4.-Borrar Asilado\n5.-Salir\n"))
                if opc==1:
                    mycursor.execute("SELECT * FROM CasaAngel.asilado;")
                    resultado = mycursor.fetchall()
                    for x in resultado:
                        print (x)
                    busqueda=(input("Desea realizar una busqueda por nombre? [S/N]")).upper()
                    if busqueda=="S":
                        nombreBusqueda=input("Ingrese nombre a buscar: ")
                        for x in range(len(resultado)):
                            if nombreBusqueda in resultado[x]:
                                print(resultado[x])

                if opc==2:
                    mycursor.execute("SELECT * FROM CasaAngel.asilado;")
                    resultado = mycursor.fetchall()
                    idasilado=len(resultado)+1
                    print(idasilado)
                    idasilado=str(idasilado)
                    fecha=input("Ingrese fecha de nacimiento: [DD-MM-AAAA]  ")
                    expediente = random.randrange(1000,9000)
                    expediente = str(expediente)
                    huellas = random.randrange(100000,900000)
                    huellas = str(huellas)
                    nombre = input("Ingrese nombre completo: ")
                    edad = input("Ingrese Edad: ")
                    sexo = input("Ingrese sexo [M/F]: ")
                    opcivil = int(input("1.-Soltero\n2.-Casado\n3.-Viudo\n"))
                    if opcivil == 1:
                        estadocivil="Soltero"
                    if opcivil == 2:
                        estadocivil="Casado"
                    if opcivil == 3:
                        estadocivil="Viudo"
                    estudios=input("Ingrese nivel de estudios: ")
                    curp=input("Ingrese CURP: ")
                    nss=input("Ingrese Numero de seguro social: ")
                    ine=input("Ingrese numero de INE: ")
                    calle=input("Ingrese calle y numero de domicilio: ")
                    colonia=input("Ingrese Colonia: ")
                    ciudad=input("Ingrese Ciudad: ")
                    estado=input("Ingrese Estado: ")
                    sqlstr=("INSERT INTO `CasaAngel`.`asilado` (`idasilado`, `Fecha`, `Expediente`, `Huellas`, `Nombre`, `Edad`, `Sexo`, `EstadoCivil`, `Estudios`, `CURP`, `SeguroSocial`, `INE`, `CalleNumero`, `Colonia`, `Ciudad`, `Estado`) VALUES ('"+idasilado+"', '"+fecha+"', '"+expediente+"', '"+huellas+"', '"+nombre+"', '"+edad+"', '"+sexo+"', '"+estadocivil+"', '"+estudios+"', '"+curp+"', '"+nss+"', '"+ine+"', '"+calle+"', '"+colonia+"', '"+ciudad+"', '"+estado+"');")
                    mycursor.execute(sqlstr)
                    mydb.commit()
                    print("Datos agregados")
                    socioeconomico = input("Desea ingresar estudio socio-economico? [S/N]").upper() #Datos socioeconomicos 
                    if socioeconomico == "S":
                        mycursor.execute("SELECT * FROM CasaAngel.estudioSocio;")
                        resultado = mycursor.fetchall()
                        idSocio = len(resultado)+1
                        idSocio = str(idSocio)
                        leer=input("Sabe leer y escribir? [S/N]: ")
                        profesion = input("Cual es su profesion?: ")
                        hobbies = input("Cuales son sus Hobbies?: ")
                        vivienda = input("Con quien vive?: ")
                        hijos = input("Cuantos hijos tiene?: ")
                        relacion = input("Que relacion familiar tiene?: ")
                        tutor = input("Quien es el tutor?: ")
                        participacion = input("Participa en asilos? [S/N]: ")
                        hogar = input ("Que actividad tiene en el hogar?: ")
                        economia = input("Si cuenta con un apoyo economico de cuanto es?: ")
                        apoyoEc = input(" De donde procede el apoyo?: ")
                        depende = input("Depende de alguna persona? ")
                        ownHogar = input("A quien le pertenece su hogar? ")
                        sqlstr = ("INSERT INTO `CasaAngel`.`estudioSocio` (`idestudioSocio`, `lee`, `estudios`, `profesion`, `hobbies`, `conquienvive`, `hijos`, `relacionFamiliar`, `tutor`, `participaAsilos`, `actividadesHogar`, `apoyoEconomico`, `OrigenApoyo`, `dependiente`, `ownHogar`, `idasilado`) VALUES ('"+idSocio+"', '"+leer+"', '"+estudios+"', '"+profesion+"', '"+hobbies+"', '"+vivienda+"', '"+hijos+"', '"+relacion+"', '"+tutor+"', '"+participacion+"', '"+hogar+"', '"+economia+"', '"+apoyoEc+"', '"+depende+"', '"+ownHogar+"', '"+idasilado+"');")
                        mycursor.execute(sqlstr)
                        mydb.commit()
                        print("Estudio agregado")
                    else:
                        mycursor.execute("SELECT * FROM CasaAngel.estudioSocio;")
                        resultado = mycursor.fetchall()    
                        idSocio = len(resultado)+1
                        idSocio = str(idSocio)
                        sqlstr = ("INSERT INTO `CasaAngel`.`estudioSocio` (`idestudioSocio`, `idasilado`) VALUES ('"+idSocio+"', '"+idasilado+"');")
                        mycursor.execute(sqlstr)
                        mydb.commit()      
                    referenciaopc = input("Desea agregar referencias familiares?[S/N]: ")
                    if "S" == referenciaopc:
                        mycursor.execute("SELECT * FROM CasaAngel.ReferenciaFamiliar;")
                        resultado = mycursor.fetchall()
                        idReferencia = len(resultado)+1
                        idReferencia = str(idReferencia)
                        nombre = input("Ingrese nombre completo: ")
                        edad = input("Ingrese Edad: ")
                        sexo = input("Ingrese sexo [M/F]: ")
                        opcivil = int(input("1.-Soltero\n2.-Casado\n3.-Viudo\n"))
                        if opcivil == 1:
                            estadocivil="Soltero"
                        if opcivil == 2:
                            estadocivil="Casado"
                        if opcivil == 3:
                            estadocivil="Viudo"
                        estudios=input("Ingrese nivel de estudios: ")
                        curp=input("Ingrese CURP: ")
                        nss=input("Ingrese Numero de seguro social: ")
                        ine=input("Ingrese numero de INE: ")
                        calle=input("Ingrese calle y numero de domicilio: ")
                        colonia=input("Ingrese Colonia: ")
                        ciudad=input("Ingrese Ciudad: ")
                        estado=input("Ingrese Estado: ")
                        sqlstr = ("INSERT INTO `CasaAngel`.`ReferenciaFamiliar` (`idReferenciaFamiliar`, `Nombre`, `Edad`, `Sexo`, `EstadoCivil`, `Estudios`, `CURP`, `SeguroSocial`, `INE`, `Calle`, `Colonia`, `Ciudad`, `Estado`, `idasilado`) VALUES ('"+idReferencia+"', '"+nombre+"', '"+edad+"', '"+sexo+"', '"+estadocivil+"', '"+estudios+"', '"+curp+"', '"+nss+"', '"+ine+"', '"+calle+"', '"+colonia+"', '"+ciudad+"', '"+estado+"','"+idasilado+"');")
                        mycursor.execute(sqlstr)
                        mydb.commit()    
                        print("Referncia Agregada")
                    else:
                        mycursor.execute("SELECT * FROM CasaAngel.ReferenciaFamiliar;")
                        resultado = mycursor.fetchall()
                        idReferencia = len(resultado)+1
                        idReferencia = str(idReferencia)
                        sqlstr = ("INSERT INTO `CasaAngel`.`ReferenciaFamiliar` (`idReferenciaFamiliar`, `idasilado`) VALUES ('"+idReferencia+"', '"+idasilado+"');")
                        mycursor.execute(sqlstr)
                        mydb.commit()    
                if opc == 3:
                    mycursor.execute("SELECT * FROM CasaAngel.asilado;")
                    resultado = mycursor.fetchall()
                    for x in resultado:
                        print (x)
                    choice=int(input("Ingrese ID a modificar: "))
                    for x in range(len(resultado)):
                        if choice == resultado[x][0]:
                            print("Elemento a modificar: ")
                            print(resultado[x])
                            split=(input("Desea modificar todos los campos?[S/N]")).upper()
                            if split =="S":
                                fecha=input("Ingrese fecha de nacimiento: [DD-MM-AAAA]  ")
                                #expediente = random.randrange(1000,9000)
                                #expediente = str(expediente)
                                #huellas = random.randrange(100000,900000)
                                #huellas = str(huellas)
                                nombre = input("Ingrese nombre completo: ")
                                edad = input("Ingrese Edad: ")
                                sexo = input("Ingrese sexo [M/F]: ")
                                opcivil = int(input("1.-Soltero\n2.-Casado\n3.-Viudo\n"))
                                if opcivil == 1:
                                    estadocivil="Soltero"
                                if opcivil == 2:
                                    estadocivil="Casado"
                                if opcivil == 3:
                                    estadocivil="Viudo"
                                estudios=input("Ingrese nivel de estudios: ")
                                curp=input("Ingrese CURP: ")
                                nss=input("Ingrese Numero de seguro social: ")
                                ine=input("Ingrese numero de INE: ")
                                calle=input("Ingrese calle y numero de domicilio: ")
                                colonia=input("Ingrese Colonia: ")
                                ciudad=input("Ingrese Ciudad: ")
                                estado=input("Ingrese Estado: ")
                                sqlstr = ("UPDATE `CasaAngel`.`asilado` SET `Fecha` = '"+fecha+"', `Nombre` = '"+nombre+"', `Edad` = '"+edad+"', `Sexo` = '"+sexo+"', `EstadoCivil` = '"+estadocivil+"', `Estudios` = '"+estudios+"', `CURP` = '"+curp+"', `SeguroSocial` = '"+nss+"', `INE` = '"+ine+"', `CalleNumero` = '"+calle+"', `Colonia` = '"+colonia+"', `Ciudad` = '"+ciudad+"' WHERE (`idasilado` = '"+str(choice)+"');")
                                mycursor.execute(sqlstr)
                                mydb.commit()    
                                print("Datos Actualizados!!")

                            else:
                                campo=int(input("Ingrese campo a modificar: \n1.-Fecha\n2.-Nombre\n3.-Edad\n4.-Sexo\n5.-Estado Civil\n6.-Estudios\n7.-CURP\n8.-NSS\n9.-INE\n10.-Calle\n11.-Colonia\n12.-Ciudad\n13.-Estado\n"))
                                if campo == 1:
                                    updsql="Fecha"
                                    modificacion=input("Ingrese Fecha: ")
                                if campo == 2:
                                    updsql="Nombre"
                                    modificacion=input("Ingrese Nombre: ")
                                if campo == 3:
                                    updsql="Edad"
                                    modificacion=input("Ingrese Edad: ")                
                                if campo == 4:
                                    updsql="Sexo"
                                    modificacion=input("Ingrese Sexo: ")                
                                if campo == 5:
                                    opcivil = int(input("1.-Soltero\n2.-Casado\n3.-Viudo\n"))
                                    if opcivil == 1:
                                        modificacion="Soltero"
                                    if opcivil == 2:
                                        modificacion="Casado"
                                    if opcivil == 3:
                                        modificacion="Viudo"
                                        updsql="Fecha"
                                if campo == 6:
                                    updsql="Estudios"
                                    modificacion=input("Ingrese Estudios: ")
                                if campo == 7:
                                    updsql="CURP"
                                    modificacion=input("Ingrese CURP: ")
                                if campo == 8:
                                    updsql="SeguroSocial"
                                    modificacion=input("Ingrese Seguro Social: ")
                                if campo == 9:
                                    updsql="INE"
                                    modificacion=input("Ingrese INE: ")
                                if campo == 10:
                                    updsql="CalleNumero"
                                    modificacion=input("Ingrese Calle: ")
                                if campo == 11:
                                    updsql="Colonia"
                                    modificacion=input("Ingrese Colonia: ")
                                if campo == 12:
                                    updsql="Ciudad"
                                    modificacion=input("Ingrese Ciudad: ")
                                if campo == 13:
                                    updsql="Estado"
                                    modificacion=input("Ingrese Estado: ")
                                sqlstr=("UPDATE `CasaAngel`.`asilado` SET `"+updsql+"` = '"+modificacion+"' WHERE (`idasilado` = '"+str(choice)+"');")
                                mycursor.execute(sqlstr)
                                mydb.commit()
                                print("Datos Actualizados!!")
        
                if opc == 5:
                    ex=1

# Victor -- Codigo
# Lalo -- Cronograma
# Jorge -- UML / Base de datos
# Mota -- Documentacion 
# Saul -- Investigacion Redes / Diagrama packet tracer.
# Carlos -- Power Point 
#UPDATE `CasaAngel`.`asilado` SET `EstadoCivil` = 'ass' WHERE (`idasilado` = '1');
#UPDATE `CasaAngel`.`asilado` SET `Fecha` = 'y', `Nombre` = 'y', `Edad` = 'y', `Sexo` = 'y', `EstadoCivil` = 'y', `Estudios` = 'y', `CURP` = 'y', `SeguroSocial` = 'y', `INE` = 'y', `CalleNumero` = 'y', `Colonia` = 'y', `Ciudad` = 'y' WHERE (`idasilado` = '1');

