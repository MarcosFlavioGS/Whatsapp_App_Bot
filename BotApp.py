#Importar bibliotecas
import pyautogui
import time
import pyperclip #Precisei porque o pyautogui é uma porcaria para escrever caracteres especiais
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


with open("mensagem.txt", "r", encoding="UTF-8") as mensagem_txt:
    mensagem = []
    for i in mensagem_txt:
        mensagem.append(i)  

print("********************************************************************************")
print("**** O programa vai iniciar em 10 segundos... ")
print("**** Por favor não usar movimentar o mouse nem usar o teclado durante a execução")
print("********************************************************************************")
time.sleep(1)

#Abrir whatsapp_app
pyautogui.press('winleft')
pyautogui.write('whatsapp')
pyautogui.press('Enter')
time.sleep(10)


#Procurar contato
def busca_contato(contato):
    print(contato)
    pyautogui.moveTo(x=142, y=114)
    pyautogui.click()
    pyautogui.write(contato)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

    #Mandar imagem
def mandar_mensagem(filepath, mensagem):
    pyautogui.moveTo(x=504, y=830)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(3)
    for i in filepath:
        pyautogui.write(i)
        pyautogui.press('enter')
        time.sleep(1)    
        pyautogui.press('enter')
        time.sleep(2)

        #Mandar mensagem
    for i in mensagem:
        print(i)
        pyperclip.copy(i)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)


def busca_online(contato):
    pyautogui.press('winleft')
    pyautogui.write('Chrome')
    pyautogui.press('enter')
    time.sleep(5)
    #pyautogui.write(f"https://api.whatsapp.com/send?phone=55{contato}") Outra possibilidade
    pyperclip.copy(contato)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('enter')
    time.sleep(5)


for contato in contatos:

    if contato[:4] == "http":
        print("Buscando contato online")

        busca_online(contato)
        mandar_mensagem(filepath, mensagem)
    else:
        print("Executando Bot")
        try:
            busca_contato(contato)
            mandar_mensagem(filepath, mensagem)
        except:
            print(f"Um erro ocorreu. Verifique o contato: {contato}")