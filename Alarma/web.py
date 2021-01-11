
def mail():
        
    # Importamos librerías
    import smtplib
    import mimetypes
    from PIL import Image
    import requests
    from io import BytesIO
    import os, sys
    import datetime
    import time 

    # Importamos los módulos necesarios
    from email.mime.multipart import MIMEMultipart
    from email.mime.image import MIMEImage
    from email.mime.text import MIMEText
    # Capturamos Imagen
    imagenes = []
    for x in range (5):
        datetime_object = datetime.datetime.now()
        print(datetime_object)
        d1 = str(datetime_object)
        output = d1.replace(":","")
        output = output.replace(" ","_")
        output = output[0:17]+".jpg"

        #Cambiar la direccion IP segun su configuracion
        url = "http://192.168.1.186/cam-hi.jpg"

        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        try:
            img.save(output)
        except IOError:
            print("cannot convert", infile)
        print(output)
        imagenes.append(output)
        datetime_object = datetime.datetime.now()
        print(datetime_object)
        
        
    # Creamos objeto Multipart, quien será el recipiente que enviaremos
    msg = MIMEMultipart()
    msg['From']="seguridadqajo@gmail.com"
    msg['To']="manuelcastillourquijo@gmail.com"
    msg['Subject']="Alarma Activada"
    msg.attach(MIMEText("La alarma de movimiento ha sido activada, verifique la integridad de su vivienda."))

    # Adjuntamos Imagen

    for x in imagenes:
        file = open(x, "rb")
        attach_image = MIMEImage(file.read())
        attach_image.add_header('Content-Disposition', 'attachment; filename = "{0}"'.format(x))
        msg.attach(attach_image)    

    # Autenticamos
    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login("seguridadqajo@gmail.com","Urquijo8")

    # Enviamos
    mailServer.sendmail("manuelcastillourquijo@gmail.com", "manuelcastillourquijo@gmail.com", msg.as_string())

    # Cerramos conexión
    mailServer.close()
