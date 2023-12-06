# This is a sample Python script.
import pyautogui
import serial


import time
# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    screenWidth ,  screenHeight  =  pyautogui.size ()  # Restituisce due numeri interi, la larghezza e l'altezza dello schermo. (Il monitor principale, nelle configurazioni multi-monitor.)
    currentMouseX ,  currentMouseY  =  pyautogui.position ()
    pyautogui.moveTo(40, 190)
    pyautogui.click () # Fare clic con il mouse nella posizione corrente.
    pyautogui.click (200 ,  220)  # Fare clic con il mouse sulle coordinate x, y 200, 220.
    #pyautogui.move (None, 100)# Sposta il mouse di 10 pixel verso il basso, ovvero sposta il mouse rispetto alla sua posizione corrente.


    print(currentMouseX,currentMouseY)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.return rightMin + (valueScaled * rightSpan)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ser = serial.Serial('COM3')
    print("camilla ti puoi muovere!!")
    while(1):
        velocity = 7
        x = ser.readline()
        try:
            stringa = str(x).split('\\')[1][1:].split(" ")
            currentMouseX ,  currentMouseY  =  pyautogui.position ()
            if len(stringa) > 1:
                direction1 = stringa[0]
                value1 = int(float(stringa[1]))
                direction2 = "no"
                value2=0
                if len(stringa) == 5:
                    direction2 = stringa[2]
                    value2 = int(float(stringa[3]))
                if direction1 == "click":
                    print("click")
                    pyautogui.click()
                else:
                    if (direction1 == "destra" or direction1 == "sinistra"):
                        #print(translate(value,-10,-10,1,10))
                        pyautogui.moveTo(currentMouseX-value1*velocity, currentMouseY-value2*velocity,0.01)
                        print("sto andando denstra sinistra forse obliguo: ", value1, value2)
                    else:
                        pyautogui.moveTo(currentMouseX, currentMouseY-value1*velocity,0.01)
                        print("sto andando sotto o sopra ")
        except:
            pass



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
