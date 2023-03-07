import pyautogui as gui
from time import sleep
import ctypes
import winsound



def MB1_STATE():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x01
    return hllDll.GetKeyState(VK_CAPITAL)

def NUM_STATE():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x90
    return hllDll.GetKeyState(VK_CAPITAL)


def SCROLL_STATE():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x91
    return hllDll.GetKeyState(VK_CAPITAL)

lista_coord = []
lista_coord_execucao = []

while True:
    intervalo = input("Digite o número de segundos entre cliques: ")
    try:
        intervalo = float(intervalo)
    except:
        print("Digite um número inteiro!")
        continue
    break

print("Para salvar coordenadas deixe o NUM LOCK habilitado e clique nos locais desejados. Ao terminar, desative o NUM LOCK e ative o SCROLL LOCK para iniciar.")

while True:
    a = NUM_STATE()
    b = SCROLL_STATE()

    if a:
        c = MB1_STATE()
        print(c)
        
        if c>1:
            pos = gui.position()
            print(pos)
            sleep(0.15)
            lista_coord.append(pos)
        else:
            pass
    elif b:
        print(lista_coord)

        if lista_coord != []:
            lista_coord_execucao = lista_coord
            lista_coord = []
        for coord in lista_coord_execucao:
            if SCROLL_STATE():
                gui.moveTo(coord)
                gui.click()
                sleep(2)
            else:
                break



