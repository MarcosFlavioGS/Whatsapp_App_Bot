import pyautogui
import time
import pyperclip  # Precisei porque o pyautogui é uma porcaria para escrever caracteres especiais

# Mover o mouse para o canto superior esquerdo para parar o processo
pyautogui.FAILSAFE = True

# Abrir arquivos
with open("contatos.txt", "r")as contacts_txt:
    contacts = [i.strip() for i in contacts_txt]

# image
with open("filepath.txt", "r") as filepath_txt:
    filepath = [i for i in filepath_txt]

with open("mensagem.txt", "r", encoding="UTF-8") as msg_txt:
    menssage = [i for i in msg_txt]

print("********************************************************************************")
print("**** O programa vai iniciar em 10 segundos... ")
print("**** Por favor não movimentar o mouse nem usar o teclado durante a execução")
print("********************************************************************************")
time.sleep(10)

# Open whatsapp_app
pyautogui.press('winleft')
time.sleep(3)
pyautogui.write('whatsapp')
time.sleep(1)
pyautogui.press('Enter')
time.sleep(15)


def search_contact(contact):
    pyautogui.moveTo(x=93, y=114) # Mudar a posição dependendo do tamanho da tela
    pyautogui.click()
    pyautogui.write(contact)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(4)


def send_msg(filepath, msg):
    pyautogui.moveTo(x=478, y=701) # Mudar a posição dependendo do tamanho da tela
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

    for i in msg:
        pyperclip.copy(i)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(4)


def search_online(contact):
    pyautogui.press('winleft')
    time.sleep(3)
    pyautogui.write('Chrome')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(6)
    pyperclip.copy("https://api.whatsapp.com/send?phone=")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.write(contact)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(7)


for contact in contacts:
    if contact[:2] == "55":
        try:
            print("Buscando contato online")

            search_online(contact)
            send_msg(filepath, menssage)
        except:
            print(f"Houve um problema. Verifique o contado: {contact}")
    else:
        print("Executando Bot")
        try:
            search_contact(contact)
            send_msg(filepath, menssage)
        except:
            print(f"Um erro ocorreu. Verifique o contato: {contact}")

input("Programa terminado. Aperte qualquer tecla para terminar: ")
