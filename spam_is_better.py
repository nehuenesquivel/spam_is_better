import getpass
import os.path
import re
import smtplib
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def read_attachments_paths():
    global attachments_paths
    attachments_paths = []
    with open(
        "archivos_adjuntos.txt", mode="r", encoding="utf-8"
    ) as attachments_paths_file:
        for attachment_path in attachments_paths_file:
            attachments_paths.append(attachment_path.strip())
    print("(1) Las rutas de los archivos adjuntos han sido leídas.")

def read_recipients_addresses():
    global recipients_addresses
    recipients_addresses = []
    with open(
        "destinatarixs.txt", mode="r", encoding="utf-8"
    ) as recipients_addresses_file:
        for recipient_address in recipients_addresses_file:
            recipients_addresses.append(recipient_address.strip())
    print("(2) Las direcciones de lxs destinatarixs han sido leídas.")

def generic_validation(option, message):
    if option > 3:
        if option == 4:
            key = getpass.getpass(message)
        elif option == 5:
            key = input(message)
        if key == "3":
           print("Sólo faltaba poquito para cumplir mi propósito en esta vida :'(")
           sys.exit()
    else:
        key = input(message)
        if option == 1:
            while key != "1":
                if key == "3":
                    print("¡Hasta luego! :)")
                    sys.exit()
                key = input()
        elif option == 2:
            while key != "1" and key != "2":
                if key == "3":
                    print("¡Nos vemos! :)")
                    sys.exit()
                key = input()
        elif option == 3:
            while invalid_address(key):
                if key == "3":
                    print("¡Un gusto conocerte! :)")
                    sys.exit()
                key = input()
    return key

def invalid_attachments_paths():
    if not attachments_paths:
        key = generic_validation(2, "(1*1) No fue definido ningún archivo adjunto, ¿sólo querés enviar un mensaje? Si es así, presioná 2, en caso contrario, luego de definirlos, presioná 1: ")
        if key == "1":
            return True
    else:
        for attachments_path in attachments_paths:
            if not os.path.exists(attachments_path):
                generic_validation(1, "(1*2) La ruta " + attachments_path + " es inválida, ¿podrías revisarla? Cuando la corrijas, presioná 1: ")
                return True
    return False

def invalid_recipients_addresses():
    if not recipients_addresses:
        generic_validation(1, "(2*1) No se definieron direcciones de destinatarixs, ¿te fijas qué onda? Cuando las definas, presioná 1: ")
        return True
    else:
        for recipient_address in recipients_addresses:
            if not address_regex.match(recipient_address):
                generic_validation(1, "(2*2) La dirección " + recipient_address + " es inválida, ¿podrías revisarla? Cuando la corrijas, presioná 1: ")
                return True
    return False

def read_email_information():
    global subject
    global body
    print("")
    subject = input("asunto:")
    body = input("cuerpo:")

def read_sender_information():
    global sender_address
    global sender_password
    print("Necesito una cuenta desde donde enviar los mensajes, cualquiera, ¡la tuya!")
    print("Atentx ingresando la contraseña que no tengo forma de validar que sea correcta, en otras palabras, probablemente rompa todo. (?")
    #se podría refactorizar hermosamente esta parte, lo sé, pero sigo cansado. el sistema capitalista me lastima. :(
    sender_address = generic_validation(3, "La (tu) cuenta: ")
    sender_password = generic_validation(4, "La (tu) contraseña: ")
    key1 = generic_validation(5, "¿Está todo bien?, ¿seguimos adelante o querés volver a ingresar los datos? s(mandamos mecha)/n(ingresar datos): ")
    while key1 != "s":        
        sender_address = generic_validation(3, "La (tu) cuenta: ")
        sender_password = generic_validation(4, "La (tu) contraseña: ")
        key1 = generic_validation(5, "¿Está todo bien?, ¿seguimos adelante o querés volver a ingresar los datos? s(mandamos mecha)/n(ingresar datos): ")
    print("(3) La información de lx remitente está definida. No te preocupes por la seguridad de los datos, esto es transparente.")

def invalid_address(address):
    if not address_regex.match(address):
        if address != "3": #lo sé, feíta solución, pero estoy medio cansado. espero que vos estés bien. :)
            print("(3*1) Aparentemente la dirección no es válida, ¿podrías volver a ingresarla?")
        return True
    return False

def confirm():
    print("Se enviaran los archivos adjuntos ("+ str(len(attachments_paths)) +"):")
    for attachments_path in attachments_paths:
        print(attachments_path)
    print("A las direcciones ("+ str(len(recipients_addresses)) +"):")
    for recipient_address in recipients_addresses:
        print(recipient_address)
    print("Con el asunto:")

    print("Y el mensaje:")

    print("Desde la cuenta: " + sender_address)
    confirm = input("¿Todo listo?, ¿cambiamos el mundo? (siempre para mejor, más vale) s/n: ")
    if confirm != "s":
        print("Confío en tus razones...")
        sys.exit()


address_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
print("¡Bievenidx! Si vas a hacer spam, que sea por una causa justa. ;)")
print("Por las dudas, te aviso que es posible abortar el programa en cualquier momento presionando 3, don't worry.")
read_attachments_paths()
while invalid_attachments_paths():
    read_attachments_paths()
read_recipients_addresses()
#read_email_information()
while invalid_recipients_addresses():
    read_recipients_addresses()
read_sender_information()
confirm()
#send()
print("¡Listo el spam! Digo, los mensajes. Por si te deja tranquilx, se enviaron "+ number_of_messages +" correos electrónicos. ¡Que estés bien!")


"""
def send():

    message = MIMEMultipart()
    message["From"] = sender_address
    message["Subject"] = "subject"
    payload = MIMEBase('application', 'octate-stream')

    for attachment_file_name in attachments:
        payload.set_payload(open(attachment_file_name, 'rb').read())

    encoders.encode_base64(payload)


        message.attach(MIMEText(mail_content, 'plain'))






def validate():
    if attachments or receivers:

    else:
        print("datos inconsistentes")
        exit


  if attachment_path_list is not None:
        for each_file_path in attachment_path_list:
            try:
                file_name=each_file_path.split("/")[-1]
                part = MIMEBase('application', "octet-stream")
                part.set_payload(open(each_file_path, "rb").read())

                Encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment' ,filename=file_name)
                msg.attach(part)
            except:
                print "could not attache file"
    msg.attach(MIMEText(msg_text,'html'))
    s.sendmail(sender, recipients, msg.as_string())




payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
print('Mail Sent')





    session = smtplib.SMTP(
        host="smtp-mail.outlook.com", port="587"
    )  #smtp.gmail.com
    session.starttls()
    session.login(sender_address, sender_password)
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

# text = message.as_string()
# 
# session.quit()

# contenido del mail
# revisar si estan los archivos que se envian!
# definir nombre repo
# validacion vacia archivos, validacion mails que sirvne y archivos existentes


   

    for receiver in receivers:
        message["To"] = receiver
        simple_mail_transfer_protocol.send_message(message)






"""


# msg.attach(MIMEText(message, 'plain'))


# mail_content = """Hello,
# This is a test mail.
# In this mail we are sending some attachments.
# The mail is sent using Python SMTP library.
# Thank You
# """

# # The subject line
# # The body and the attachments for the mail
# message.attach(MIMEText(mail_content, "plain"))
# attach_file_name = "TP_python_prev.pdf"
# attach_file = open(attach_file_name, "rb")  # Open the file as binary mode
# payload = MIMEBase("application", "octate-stream")
# payload.set_payload((attach_file).read())
# encoders.encode_base64(payload)  # encode the attachment
# # add payload header with filename
# payload.add_header("Content-Decomposition", "attachment", filename=attach_file_name)
# message.attach(payload)
