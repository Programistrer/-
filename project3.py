from tkinter import *

window = Tk()
window.title("Калькулятор ИМТ")
window.geometry("600x400")
window.configure(bg = "green")

def rachet():
    ves = float(entry1.get())
    rost = float(entry2.get())

    preresult = rost / 100
    result = round(ves / (preresult * 2), 2)
    final_label["text"] = f"Ваш ИМТ: {result}"


main_label = Label(window, text = "Калькулятор индекса массы тела", bg = "green", fg = "white")
main_label.grid(row = 1, column = 2)

label1 = Label(window, text = "Вес(кг): ", bg = "green", fg = "white")
label1.grid(row = 2, column = 1)

entry1 = Entry(window)
entry1.grid(row = 2, column = 2)

label2 = Label(window, text = "Рост(см): ", bg = "green", fg = "white")
label2.grid(row = 3, column = 1)

entry2 = Entry(window)
entry2.grid(row = 3, column = 2)

knopka = Button(window, text = "Рассчитать", command = rachet)
knopka.grid(row = 5, column = 2)

final_label = Label(window, text = "Результат:", bg = "green", fg = "white")
final_label.grid(row = 4, column = 1)

window.mainloop()