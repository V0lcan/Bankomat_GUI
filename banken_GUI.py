from tkinter import *
from tkinter import messagebox
from bankomat_functions import *

# Funktioner


def validate_deposit():
    """
    Kollar det inmatade värdet för insättning och skriver ut en message box om det är godkänt eller inte
    :return: None
    """
    deposit = int(deposit_entry.get())

    if deposit >= 0:
        transaktioner.append(deposit)
        write_transaction_to_file(deposit)
        messagebox.showinfo(title="Information", message="Värdet har registerats. Du kan nu stänga detta fönster")
    else:
        messagebox.showwarning(title="Ett fel uppstod", message="Du har matat in fel värde. Var vänlig försök igen.")

    deposit_entry.delete(0, END)


def validate_withdraw():
    """
    Kollar det inmatade värdet för uttag och skriver ut en message box om det är godkänt eller inte
    :return: None
    """
    withdraw = int(withdraw_entry.get())
    if withdraw >= 0:
        transaktioner.append(-withdraw)
        write_transaction_to_file(-withdraw)
        messagebox.showinfo(title="Information", message="Värdet har registerats. Du kan nu stänga detta fönster")
    else:
        messagebox.showwarning(title="Ett fel uppstod", message="Du har matat in fel värde. Var vänlig försök igen.")

    withdraw_entry.delete(0, END)


def uttag_open():
    """
    Fönster för uttag
    :return: None
    """
    global button1, withdraw_entry
    # Uttagsfönster
    uttag = Toplevel()
    uttag.geometry("1440x1080")
    uttag.configure(background="#00b2e9")
    uttag.title("Uttag")
    withdraw_label = Label(uttag, text="Uttag")  # Text för uttag fönstret
    withdraw_label.config(font=("timesnewroman", 50))  # Ställer in textformat och storlek
    withdraw_label.grid(row=2, padx=600, pady=40)  # Placerar texten
    info = Label(uttag, text="Ange hur mycket du vill ta ut")  # Text för att informera vad man gör på inmatningsrutan
    info.config(font=("timesnewroman", 35))  # Ställer in infotexten
    info.grid()  # Placerar texten

    # Inmatningsruta uttag
    withdraw_entry = Entry(uttag)  # Inmatningsruta för att ta ut pengar
    # int(withdraw_entry.get())
    withdraw_entry.config(font=("timesnewroman", 50))  # Ställer in textformat och storlek när man skriver in
    withdraw_entry.grid(row=6, padx=400)  # Placerar inmatnigsrutan
    button1 = Button(uttag, text="Ok", command=validate_withdraw)  # När man klickar på ok valideras det inmatade värdet,
    # om värdet är ok skrivs värdet till transaktionerna.
    # Om värdet är inte godkänt visas en text att man får försöka igen.
    button1.config(font=("timesnewroman", 45))
    button1.grid()


def insattning_open():
    """
    Fönster för insättning
    :return: None
    """
    global button2, deposit_entry
    # Insättningsfönster
    insattning = Toplevel()
    insattning.geometry("1440x1080")
    insattning.configure(background="#00b2e9")
    insattning.title("Insättning")
    deposit_label = Label(insattning, text="Insättning")  # Text för insättningsfönstret
    deposit_label.config(font=("timesnewroman", 50))  # Ställer in textformat och storlek
    deposit_label.grid(row=2, padx=600, pady=40)  # Placerar texten
    info2 = Label(insattning,
                  text="Ange hur mycket du vill sätta in")  # Text för att informera vad man gör på insättningssidan
    info2.config(font=("timesnewroman", 35))  # Ställer in infotexten
    info2.grid()  # Placerar texten

    # Inmatningsruta insättning
    deposit_entry = Entry(insattning)  # Inmatningsruta för att sätta in pengar
    deposit_entry.config(font=("timesnewroman", 50))  # Ställer in textformat och storlek när man skriver in
    deposit_entry.grid(row=6, padx=400)  # Placerar inmatningsrutan
    button2 = Button(insattning, text="Ok", command=validate_deposit)  # När man klickar på ok så valideras det inmatade värdet,
    # om värdet är ok skrivs värdet till transaktionerna.
    # Om värdet är inte godkänt visas en text att man får försöka igen.
    button2.config(font=("timesnewroman", 45))
    button2.grid()


def transactions_open():
    """
    Öppnar ett fönster och visar sparade transaktioner
    :return: None
    """
    transactions = Toplevel()
    transactions.geometry("1440x1080")
    transactions.configure(background="#00b2e9")
    transactions.title("Transaktioner")
    transactions_label = Label(transactions, text="Transaktioner")
    transactions_label.config(font=("timesnewroman", 50))
    transactions_label.grid(row=2, padx=600, pady=40)


root = Tk()

check_file_exists()
print(transaktioner)

# Sätter storleken på fönstret
root.geometry("1440x1080")

# Sätter bakrund till fönstret
root.configure(background="#00b2e9")

# Ger fönstret en titel
root.title("Banken")

# Skapar en text där det står banken och en annan text där det står välkommen med lite konfigureringar
logo = Label(root, text="Banken")
logo.config(font=("timesnewroman", 55))
logo.grid(row=0, padx=650)
logo2 = Label(root, text="Välkommen")
logo2.config(font=("timesnewroman", 45))
logo2.grid()
balance = Label(root, text=balance())  # Denna variabel ska visa saldot man har kvar på kontot (tekniskt fel)
balance.config(font=("timesnewroman", 55))
balance.grid(row=6, pady=80)

# Knappar med text
knapp = Button(root, text="Transaktioner", command=transactions_open)
# Knapp1 visar de senaste gjorda transaktionerna på kontot
knapp2 = Button(root, text="Insättning", command=insattning_open)
# Knapp2 ska göra att man kan sätta in pengar på kontot
knapp3 = Button(root, text="Uttag", command=uttag_open)
# Knapp3 ska göra så att man kan ta ut pengar från kontot
knapp4 = Button(root, text="Avsluta", command=exit)  # Denna knapp avslutar applikationen med kommandot "exit"

# Konfigurering av text och storlek på knapparna
knapp.config(font=("timesnewroman", 40))
knapp2.config(font=("timesnewroman", 40))
knapp3.config(font=("timesnewroman", 40))
knapp4.config(font=("timesnewroman", 40,))

# Placering av knaparna
knapp.grid(row=2, pady=20)
knapp2.grid(row=3, pady=20)
knapp3.grid(row=4, pady=20)
knapp4.grid(row=5, pady=20)


# Mainloop för fönsteret
root.mainloop()
