#Importar bibliotecas
import pyautogui
import time
import pyperclip #Precisei porque o pyautogui é uma porcaria para escrever caracteres especiais
import smtplib
import ssl
from email.message import EmailMessage

# Mover o mouse para o canto superior esquerdo para parar o processo
pyautogui.FAILSAFE = True

#Abrir arquivos
#Abrir arquivo de contatos
with open("contatos.txt", "r")as contatos_txt:
    contatos = []
    for i in contatos_txt:
        i = i.strip()
        contatos.append(i)

#Caminho para arquivo de imagem
with open("filepath.txt", "r") as filepath_txt:
    filepath = []
    for i in filepath_txt:
        filepath.append(i)

#Abrir arquivo de mensagem
with open("mensagem.txt", "r", encoding="UTF-8") as mensagem_txt:
    mensagem = []
    for i in mensagem_txt:
        mensagem.append(i)

# Abrir arquivo de mensagem do email
with open("mensagem_email.txt", "r", encoding="UTF-8") as mensagememail_txt:
    emailMessage1 = []
    for i in mensagememail_txt:
        emailMessage1.append(i)
    emailMessage = ''.join(emailMessage1)

#Abrir arquivo de titulo de email
with open("titulo_email.txt", "r", encoding="UTF-8") as titulo_txt:
    titulo1 = []
    for i in titulo_txt:
        titulo1.append(i)
    titulo = ''.join(titulo1)    

# Abrir arquivo de senha
with open("senha_email.txt", "r", encoding="UTF-8") as password_txt:
    secret1 = []
    for i in password_txt:
        secret1.append(i)
    secret = ''.join(secret1)    

# Abrir arquivo de email
with open("email.txt", "r", encoding="UTF-8") as email_txt:
    useremail1 = []
    for i in email_txt:
        useremail1.append(i)
    useremail = ''.join(useremail1)

#Inicio
print("********************************************************************************")
print("**** O programa vai iniciar em 10 segundos... ")
print("**** Por favor não usar movimentar o mouse nem usar o teclado durante a execução")
print("********************************************************************************")
time.sleep(10)

#Abrir whatsapp_app
pyautogui.press('winleft')
time.sleep(3)
pyautogui.write('whatsapp')
time.sleep(1)
pyautogui.press('Enter')
time.sleep(15)


#Procurar contato no whatsapp
def busca_contato(contato):
    pyautogui.moveTo(x=92, y=114)
    pyautogui.click()
    pyautogui.write(contato)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(4)

#Mandar imagem
def mandar_mensagem(filepath, mensagem):
    
    pyautogui.moveTo(x=478, y=701)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    
    for i in filepath:  
        pyautogui.write(i)
        pyautogui.press('enter')
        time.sleep(4)    
        pyautogui.press('enter')
        time.sleep(3)

        #Mandar mensagem
    for i in mensagem:
        pyperclip.copy(i)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(4)

#Função condicional para busca de contato não cadastrado via chrome
def busca_online(contato):
    pyautogui.press('winleft')
    time.sleep(3)
    pyautogui.write('Chrome')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(6)
    pyperclip.copy("https://api.whatsapp.com/send?phone=")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.write(contato)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(7)

#Função para envio de email ao invés de whatsapp caso o contato seja um email
def email(useremail, contato, emailMessage, titulo, secret):
    subject = f"{titulo}"
    body = f"{emailMessage}"
    sender_email = f"{useremail}"
    receiver_email = f"{contato[1:]}"
    password = f"{secret}" #Aqui é o local de senha do email. Porém, é melhor usar algum tipo de arquivo criptografado

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    #Formatação html
    html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
        </body>
    </html>
    """

    message.add_alternative(html, subtype="html")

    context = ssl.create_default_context()

    print("ENVIANDO EMAIL!")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email enviado")

for contato in contatos: #Chamando funções

    if contato[:2] == "55":
        try:
            print("Buscando contato online")

            busca_online(contato)
            mandar_mensagem(filepath, mensagem)
        except:
            print(f"Houve um problema. Verifique o contado: {contato}")    
    
    elif contato[:1] == "@":
        email(useremail, contato, emailMessage, titulo, secret)
    
    else:
        print("Executando Bot")
        try:
            busca_contato(contato)
            mandar_mensagem(filepath, mensagem)
        except:
            print(f"Um erro ocorreu. Verifique o contato: {contato}")

input("Programa terminado. Digite 'Ok' para terminar: ")