import flet as ft
import random

def main(page: ft.Page):

    def rollDice(e):
        valor = random.randint(1,6)
        rollNumber.value = str(valor)

        if valor == 1:
            diceImage.src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Dice-1.svg/600px-Dice-1.svg.png"
        elif valor == 2:
            diceImage.src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Dice-2.svg/480px-Dice-2.svg.png"
        elif valor == 3:
            diceImage.src="https://upload.wikimedia.org/wikipedia/commons/2/28/Dice-3a.svg"
        elif valor == 4:
            diceImage.src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Dice-4.svg/600px-Dice-4.svg.png"
        elif valor == 5:
            diceImage.src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStdtAlk6Ro_83B_fXPxPlolwgFvgZWFTT5Hsz6iZ-PHrR8RqI86QsZfJlhvaeUAC8g8GI&usqp=CAU"
        elif valor == 6:
            diceImage.src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvXWXP_w1eIJFPiRRYm4TKMAd6uLIxPCA5TSpGKhNEnUP8lBS2nL5CUQmJbzXrX2ujDtI&usqp=CAU"
        rollNumber.update()
        diceImage.update()


    page.horizontal_alignment = "CENTER"
    page.vertical_alignment = "CENTER"


    diceImage = ft.Image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxtrPEtCGL5x2b2eIk2cprcREuqrSGGQFrGQ&usqp=CAU")
    rollNumber = ft.Text(value="No roll yet", size=40)
    rollButton = ft.ElevatedButton(text="Roll Dice", height=40, width=200, on_click=rollDice)
    page.add(diceImage, rollNumber,rollButton)

ft.app(target=main)