#Importar bibliotecas
import pyautogui
import time
import pyperclip #Precisei porque o pyautogui é uma porcaria para escrever caracteres especiais

# Mover o mouse para o canto superior esquerdo para parar o processo
pyautogui.FAILSAFE = True

#Abrir arquivos
#Abrir arquivo de contatos
with open("contatos.txt", "r")as contatos_txt:
    contatos = [i.strip() for i in contatos_txt]

#Caminho para arquivo de imagem
with open("filepath.txt", "r") as filepath_txt:
    filepath = [i for i in filepath_txt]

#Abrir arquivo de mensagem
with open("mensagem.txt", "r", encoding="UTF-8") as mensagem_txt:
    mensagem = [i for i in mensagem_txt]

#Inicio
print("********************************************************************************")
print("**** O programa vai iniciar em 10 segundos... ")
print("**** Por favor não movimentar o mouse nem usar o teclado durante a execução")
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
    pyautogui.moveTo(x=93, y=114) #Mudar a posição dependendo do tamanho da tela
    pyautogui.click()
    pyautogui.write(contato)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(4)

#Mandar imagem
def mandar_mensagem(filepath, mensagem):
    
    pyautogui.moveTo(x=478, y=701) #Mudar a posição dependendo do tamanho da tela
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

for contato in contatos: #Chamando funções

    if contato[:2] == "55":
        try:
            print("Buscando contato online")

            busca_online(contato)
            mandar_mensagem(filepath, mensagem)
        except:
            print(f"Houve um problema. Verifique o contado: {contato}")    
    
    elif contato[:1] == "@":
        try:
            email(useremail, contato, emailMessage, titulo, secret)
        except:
            print(f"Erro ao tentar enviar email. Verifique o contato: {contato}")
    
    else:
        print("Executando Bot")
        try:
            busca_contato(contato)
            mandar_mensagem(filepath, mensagem)
        except:
            print(f"Um erro ocorreu. Verifique o contato: {contato}")

input("Programa terminado. Aperte qualquer tecla para terminar: ")
