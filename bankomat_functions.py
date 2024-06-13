from config import *

# Funktioner
def balance():
    """ Beräknar saldot på kontot

    :return: Saldot
    """
    balance = 0
    for t in transaktioner:
        balance += t
    return balance


def validate_int(output, error_mess):
    """Validerar inmatat värde

    :param output: Text som skrivs till användaren
    :param error_mess: Text som skrivs om inmatningen blir felaktig
    :return: Validerat värde
    """
    while True:
         try:
            value = int(input(output))
            break
         except:
             print(error_mess)
    return value


def validate_float(output_float, error_mess_float):
    """Validerar inmatat float-värde

    :param output_float: Text som skrivs till användaren
    :param error_mess_float: Text som skrivs om inmatningen blir felaktig
    :return: Validerat värde
    """
    while True:
        try:
            value_float = float(input(output_float))
            break
        except:
            print(error_mess_float)
    return value_float


def print_transactions():
    """ Skapar utskrift av transkationer

    :return: Sträng med hela utskriften
    """
    rad = 0
    balance = 0
    output = ("\nAlla transaktioner:"
             "\n{:>3}| {:>12} |{:>12}"
             "\n--------------------------------".format("Nr", "Händelse", "Saldo"))
    for t in transaktioner:
        rad += 1
        balance += t
        output += ("\n{:>2}.| {:>9} kr |{:>9} kr".format(rad, t, balance))

    return output


def check_file_exists():
    """ Om filen inte finns så skapas den och sedan så läggs en transaktion till filen.
        Eftersom "x" returnerar ett error om filen finns kan vi utnyttja detta

    :return: None
    """

    try:
        with open(filnamn, "x"):
            print("Filen skapades")

        with open(filnamn, "a") as f:
            f.write("{}\n".format(1000))
    except:
        return


def read_file():
    """ Läser in filets innehåll till transaktionslistan

    :return: None
    """
    check_file_exists()         # Kollar om filen finns, annars så skapas ett nytt

    with open(filnamn) as f:
        for rad in f:
            if len(rad) > 0:
                add_transaction(int(rad))


def add_transaction(transaction, toFile = False):
    """ Lagrar transaktion i transaktionslistan och till filen

    :param transaction: Transaktionen
    :param toFile: True - lagra också till filen, false är förvalt
    :return: None
    """
    transaktioner.append(transaction)
    if toFile:
        write_transaction_to_file(transaction)


def write_transaction_to_file(transaction):
    """ Skriver en transaktion till filen

    :param transaction: Transaktionen
    :return: None
    """
    with open(filnamn, "a") as f:
        f.write("{}\n".format(transaction))
