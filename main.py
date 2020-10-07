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
                    referencias=input("Desea consultar referencia? [S/N]").upper()
                    if referencias=="S":
                        idp=int(input("Ingrese ID de la consulta: "))
                        mycursor.execute("SELECT * FROM CasaAngel.ReferenciaFamiliar WHERE (`idasilado` = '"+str(idp)+"');")
                        referencia=mycursor.fetchall()
                        print(referencia[0])
                    Estudio=input("Desea consultar estudio socio-economico?[S/N]").upper()
                    if Estudio=="S":
                        edp=int(input("Ingrese ID de consulta: "))
                        mycursor.execute("SELECT * FROM CasaAngel.estudioSocio WHERE (`idasilado` = '"+str(edp)+"');")
                        estudios=mycursor.fetchall()
                        print(estudios[0])

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
                    sqlstr("INSERT INTO `CasaAngel`.`HistorialClinico` (`idHistorialClinico`, `idasilado`) VALUES ('"+idasilado+"', '"+idasilado+"');")   
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
                        print("Referencia Agregada")
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
                            opcmod=int(input("1.-Modificar Asilado\n2.-Modificar Referencias del asilado\n3.-Modificar Estudio Socio-Economico\n"))
                            if opcmod==1:
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
                                        updsql="EstadoCivil"

                                        opcivil = int(input("1.-Soltero\n2.-Casado\n3.-Viudo\n"))
                                        if opcivil == 1:
                                            modificacion="Soltero"
                                        if opcivil == 2:
                                            modificacion="Casado"
                                        if opcivil == 3:
                                            modificacion="Viudo"
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
                            if opcmod == 2:

                                split=(input("Desea modificar todos los campos?[S/N]")).upper()
                                if split =="S":
                                    #fecha=input("Ingrese fecha de nacimiento: [DD-MM-AAAA]  ")
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
                                    sqlstr = ("UPDATE `CasaAngel`.`ReferenciaFamiliar` SET  `Nombre` = '"+nombre+"', `Edad` = '"+edad+"', `Sexo` = '"+sexo+"', `EstadoCivil` = '"+estadocivil+"', `Estudios` = '"+estudios+"', `CURP` = '"+curp+"', `SeguroSocial` = '"+nss+"', `INE` = '"+ine+"', `CalleNumero` = '"+calle+"', `Colonia` = '"+colonia+"', `Ciudad` = '"+ciudad+"' WHERE (`idasilado` = '"+str(choice)+"');")
                                    mycursor.execute(sqlstr)
                                    mydb.commit()    
                                    print("Datos Actualizados!!")

                                else:
                                    campo=int(input("Ingrese campo a modificar:\n1.-Nombre\n2.-Edad\n3.-Sexo\n4.-Estado Civil\n5.-Estudios\n6.-CURP\n7.-NSS\n8.-INE\n9.-Calle\n10.-Colonia\n11.-Ciudad\n12.-Estado\n"))
                                    if campo == 1:
                                        updsql="Nombre"
                                        modificacion=input("Ingrese Nombre: ")
                                    if campo == 2:
                                        updsql="Edad"
                                        modificacion=input("Ingrese Edad: ")                
                                    if campo == 3:
                                        updsql="Sexo"
                                        modificacion=input("Ingrese Sexo: ")                
                                    if campo == 4:
                                        updsql="EstadoCivil"
                                        opcivil = int(input("1.-Soltero\n2.-Casado\n3.-Viudo\n"))
                                        if opcivil == 1:
                                            modificacion="Soltero"
                                        if opcivil == 2:
                                            modificacion="Casado"
                                        if opcivil == 3:
                                            modificacion="Viudo"
                                    if campo == 5:
                                        updsql="Estudios"
                                        modificacion=input("Ingrese Estudios: ")
                                    if campo == 6:
                                        updsql="CURP"
                                        modificacion=input("Ingrese CURP: ")
                                    if campo == 7:
                                        updsql="SeguroSocial"
                                        modificacion=input("Ingrese Seguro Social: ")
                                    if campo == 8:
                                        updsql="INE"
                                        modificacion=input("Ingrese INE: ")
                                    if campo == 9:
                                        updsql="CalleNumero"
                                        modificacion=input("Ingrese Calle: ")
                                    if campo == 10:
                                        updsql="Colonia"
                                        modificacion=input("Ingrese Colonia: ")
                                    if campo == 11:
                                        updsql="Ciudad"
                                        modificacion=input("Ingrese Ciudad: ")
                                    if campo == 12:
                                        updsql="Estado"
                                        modificacion=input("Ingrese Estado: ")
                                    sqlstr=("UPDATE `CasaAngel`.`ReferenciaFamiliar` SET `"+updsql+"` = '"+modificacion+"' WHERE (`idasilado` = '"+str(choice)+"');")
                                    mycursor.execute(sqlstr)
                                    mydb.commit()
                                    print("Datos Actualizados!!")

                if opc == 4:
                    mycursor.execute("SELECT * FROM CasaAngel.asilado;")
                    resultado = mycursor.fetchall()
                    for x in resultado:
                        print (x)
                    deleteopc = int(input("Ingrese ID de registro que desea borrar: "))
                    for x in range(len(resultado)):
                        if deleteopc == resultado[x-1][0]:
                            print("Elemento a Eliminar: ")
                            print(resultado[x-1])
                            sure=input("Seguro que desea eliminar registro?: [S/N]").upper()
                            if sure=="S":
                                mycursor.execute("SELECT * FROM CasaAngel.asilado;")
                                resultado = mycursor.fetchall()
                                idupd=len(resultado)
                                sqlstr=("DELETE FROM `CasaAngel`.`asilado` WHERE (`idasilado` = '"+str(deleteopc)+"');")
                                mycursor.execute(sqlstr)
                                mydb.commit()
                                sqlstr=("DELETE FROM `CasaAngel`.`estudioSocio` WHERE (`idasilado` = '"+str(deleteopc)+"');")
                                mycursor.execute(sqlstr)
                                mydb.commit()
                                sqlstr=("DELETE FROM `CasaAngel`.`ReferenciaFamiliar` WHERE (`idasilado` = '"+str(deleteopc)+"');")
                                mycursor.execute(sqlstr)
                                mydb.commit()
                                sqlstr=("DELETE FROM `CasaAngel`.`notas` WHERE (`idasilado` = '"+str(deleteopc)+"');")
                                mycursor.execute(sqlstr)
                                mydb.commit()
                                sqlstr=("DELETE FROM `CasaAngel`.`HistorialClinico` WHERE (`idasilado` = '"+str(deleteopc)+"');")
                                mycursor.execute(sqlstr)
                                mydb.commit()
                                print("Registros eliminados")
                                #mycursor.execute("SELECT * FROM CasaAngel.asilado;")

                                for x in range(deleteopc,idupd):
                                    sqlstr=("UPDATE `CasaAngel`.`asilado` SET `idasilado` = '"+str(x)+"' WHERE (`idasilado` = '"+str(x+1)+"');")
                                    mycursor.execute(sqlstr)
                                    mydb.commit()
                                    sqlstr=("UPDATE `CasaAngel`.`ReferenciaFamiliar` SET `idReferenciaFamiliar` = '"+str(x)+"', `idasilado` = '"+str(x)+"' WHERE (`idReferenciaFamiliar` = '"+str(x+1)+"');")
                                    mycursor.execute(sqlstr)
                                    mydb.commit()
                                    sqlstr=("UPDATE `CasaAngel`.`estudioSocio` SET `idestudioSocio` = '"+str(x)+"', `idasilado` = '"+str(x)+"' WHERE (`idestudioSocio` = '"+str(x+1)+"');")
                                    mycursor.execute(sqlstr)
                                    mydb.commit()
                                    sqlstr=("UPDATE `CasaAngel`.`notas` SET `idasilado` = '"+str(x)+"' WHERE (`idasilado` = '"+str(x+1)+"');")
                                    mycursor.execute(sqlstr)
                                    mydb.commit()
                                    sqlstr=("UPDATE `CasaAngel`.`HistorialClinico` SET `idHistorialClinico` = '"+str(x)+"', `idasilado` = '"+str(x)+"' WHERE (`idasilado` = '"+str(x+1)+"');")
                                    mycursor.execute(sqlstr)
                                    mydb.commit()
                if opc == 5:
                    ex=1
            if usuario[3] == 1:
                print("Area Medica")
                opc=int(input("1.-Consulta Historial \n2.-Modificar Historial de asilado\n3.-Notas Medicas\n5.-Salir\n"))
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
                    idp=int(input("Ingrese ID del asilado: "))
                    mycursor.execute("SELECT * FROM CasaAngel.HistorialClinico WHERE (`idasilado` = '"+str(idp)+"');")
                    historial = mycursor.fetchall()
                    if historial:
                        print("Historial del asildado:")
                        print(historial[0])
                    else:
                        print("No existe registro")
                
                if opc==2:
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
                    idp=int(input("Ingrese ID del asilado: "))
                    mycursor.execute("SELECT * FROM CasaAngel.HistorialClinico WHERE (`idasilado` = '"+str(idp)+"');")
                    historial = mycursor.fetchall()
                    if historial:
                        print("Historial del asildado:")
                        print(historial[0])
                        habitacion=input("Ingrese numero de habitacion: ")
                        fecha=input("Ingrese fecha DD-MM-AAAA: ")
                        ocupacion=input("Ingrese ocupacion:  ")
                        religion=input("Ingrese Religion: ")
                        motivo=input("Ingrese motivo del consulta: ")
                        enfermedad=input("Ingrese enfermedad: ")
                        antPatologicos=input("Ingrese Antecedentes patologicos: ")
                        antNoPatologicos=input("Ingrese Antecedentes NO patologicos: ")
                        historialClinico=input("Ingrese Historial Clinico: ")
                        herencia=input("Heredo de familiares?: ")
                        habitos=input("Ingrese Habitos toxicos:" )
                        vacuna=input("Ingrese Vacuna: ")
                        sistemaNeuro=input("Ingrese estado del sistema neurologico: ")
                        sistemaCardio=input("Ingrese estado del sistema cardiologico: ")
                        sistemaRespi=input("Ingrese estado del sistema Respiratorio: ")
                        sistemaGastro=input("Ingrese estado del sistema Gastrointestinal: ")
                        sistemaEndo=input("Ingrese estado del sistema Endocrino: ")
                        musculo=input("Ingrese estado del musculo esqueletico: ")
                        fragmentos=input("Ingrese estado fragmentos: ")
                        examen=input("Ingrese resultado examen fisico: ")
                        diag=input("Ingrese diagnostico preventivo: ")
                        trat=input("Ingrese tratamiento: ")
                        sqlstr=("UPDATE `CasaAngel`.`HistorialClinico` SET `Habitacion` = '"+habitacion+"', `Fecha` = '"+fecha+"', `Ocupacion` = '"+ocupacion+"', `Religion` = '"+religion+"', `Motivo` = '"+motivo+"', `Enfermedad` = '"+enfermedad+"', `AntecedentesPatologicos` = '"+antPatologicos+"', `AntecedentesNoPatologicos` = '"+antNoPatologicos+"', `HistorialClinicocol` = '"+historialClinico+"', `HerodoFamiliares` = '"+herencia+"', `HabitosToxicos` = '"+habitos+"', `VacunaRecibida` = '"+vacuna+"', `SistemaNeurologico` = '"+sistemaNeuro+"', `SistemaCardiovascular` = '"+sistemaCardio+"', `SistemaRespiratorio` = '"+sistemaRespi+"', `SistemaGastroinstestinal` = '"+sistemaGastro+"', `SistemaEndocrino` = '"+sistemaEndo+"', `MusculoEsqueletico` = '"+musculo+"', `Fragmentos` = '"+fragmentos+"', `ExamenFisico` = '"+examen+"', `DiagnosticoPreventivo` = '"+diag+"', `Tratatamiento` = '"+trat+"' WHERE (`idHistorialClinico` = '"+str(idp)+"');")
                        mycursor.execute(sqlstr)
                        mydb.commit()
                        for x in range(len(resultado)):
                            if idp == resultado[x][0]:

                                print("Datos de {0} actualizados!!".format(resultado[x][4]))
                if opc==3:
                    notasopc=int(input("1.-Ver Notas\n2.-Agregar Notas\n"))
                    if notasopc==1:
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
                        idp=int(input("Ingrese ID del asilado: "))
                        mycursor.execute("SELECT * FROM CasaAngel.notas WHERE (`idasilado` = '"+str(idp)+"');")
                        resultado = mycursor.fetchall()
                        if resultado:
                            for x in resultado:
                                print(resultado)
                        else:
                            print("No existen notas medicas.")
                
                    if notasopc==2:
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
                        idp=int(input("Ingrese ID del asilado: "))
                        fecha=input("Ingrese Fecha: ")
                        subj=input("Ingrese caso: ")
                        obj=input("Ingrese objetivo: ")
                        analisis=input("Ingrese analisis: ")
                        plan=input("Ingrese plan: ")
                        mycursor.execute("SELECT * FROM CasaAngel.notas;")
                        resultado = mycursor.fetchall()
                        idnotas=len(resultado)+1
                        sqlstr=("INSERT INTO `CasaAngel`.`notas` (`idnotas`, `fecha`, `subjetivocaso`, `objetivo`, `analisis`, `plan`, `idasilado`) VALUES ('"+str(idnotas)+"', '"+fecha+"', '"+subj+"', '"+obj+"', '"+analisis+"', '"+plan+"', '"+str(idp)+"');")
                        mycursor.execute(sqlstr)
                        mydb.commit()
                        print("Nota agregada")                        
    else:
        print("Datos Invalidos")
# Victor -- Codigo
# Lalo -- Cronograma
# Jorge -- UML / Base de datos
# Mota -- Documentacion 
# Saul -- Investigacion Redes / Diagrama packet tracer.
# Carlos -- Power Point 
#UPDATE `CasaAngel`.`asilado` SET `EstadoCivil` = 'ass' WHERE (`idasilado` = '1');

