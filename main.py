from tkinter import *
from tkinter import messagebox
import random


def play_lotto(root):
    def losuj():
        try:
            wynik.config(state="normal")
            wynik.delete(1.0, END)
            losy = int(liczbalosow.get())

            if 0 < losy <= 10:
                for i in range(losy):
                    kupon = set()
                    while len(kupon) < 6:
                        liczba = random.randint(1, 49)
                        kupon.add(str(liczba))

                    end = ", ".join(kupon)
                    wynik.config(state="normal")

                    wynik.insert(END, f"Kupon {i + 1}.    {end} \n")
                    wynik.config(state="disabled")
                    kupon.clear()

            if losy > 10 or losy == 0:
                messagebox.showinfo("Błąd", "Aby wylosować kupony wybierz liczbę od 1 - 10")
        except Exception as e:
            messagebox.showinfo("Błąd", f"Coś poszło nie tak, sprawdź czy wszytko jest poprawnie wpisane i spróbuj "
                                        f"ponownie. Error: {e}")

    root.withdraw()  # Ukryj główne okno

    lotto_window = Toplevel(root)  # Utwórz nowe okno
    lotto_window.title("Lotto")
    lotto_window.iconbitmap("lotto.ico")
    lotto_window.geometry("400x400")
    lotto_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, lotto_window))  # Obsługa zamykania nowego okna

    # Ustawienia kolorów i czcionek
    background_color = "#f0f0f0"
    label_color = "#333"
    button_color = "#4CAF50"
    button_text_color = "#fff"

    lotto_window.configure(background=background_color)

    Label(lotto_window, text="Witaj w generatorze LOTTO!", font=("Arial", 20, "bold"), fg=label_color,
          bg=background_color).pack(pady=(20, 10))
    Label(lotto_window, text="Ile masz kuponów? (max. 10)", font=("Arial", 12), fg=label_color,
          bg=background_color).pack()

    liczbalosow = Entry(lotto_window, font=("Arial", 12))
    liczbalosow.pack(pady=5)

    Button(lotto_window, text="Losuj!", command=losuj, bg=button_color, fg=button_text_color,
           font=("Arial", 12, "bold")).pack(pady=10)

    wynik = Text(lotto_window, width=40, height=10, state="disabled")
    wynik.pack()


def play_euro(root):
    def losuj2():
        try:
            wynik.config(state="normal")
            wynik.delete(1.0, END)
            losy = int(liczbalosow.get())

            if 0 < losy <= 10:
                for i in range(losy):
                    dodatek = set()
                    kupon = set()
                    while len(kupon) < 5:
                        liczba = random.randint(1, 50)
                        kupon.add(str(liczba))
                    while len(dodatek) < 2:
                        liczba2 = random.randint(1, 10)
                        dodatek.add(str(liczba2))

                    end = ", ".join(sorted(kupon))

                    end2 = ", ".join(sorted(dodatek))
                    wynik.config(state="normal")

                    wynik.insert(END, f"Kupon {i + 1}.    {end} | {end2} \n")
                    wynik.config(state="disabled")
                    kupon.clear()

            if losy > 10 or losy == 0:
                messagebox.showinfo("Błąd", "Aby wylosować kupony wybierz liczbę od 1 - 10")
        except Exception as e:
            messagebox.showinfo("Błąd", f"Coś poszło nie tak, sprawdź czy wszytko jest poprawnie wpisane i spróbuj "
                                        f"ponownie. Error: {e}")

    root.withdraw()  # Ukryj główne okno

    euro_window = Toplevel(root)  # Utwórz nowe okno
    euro_window.title("Lotto")
    euro_window.iconbitmap("euro.ico")
    euro_window.geometry("400x400")
    euro_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, euro_window))  # Obsługa zamykania nowego okna

    # Ustawienia kolorów i czcionek
    background_color = "#f0f0f0"
    label_color = "#333"
    button_color = "#4CAF50"
    button_text_color = "#fff"

    euro_window.configure(background=background_color)

    Label(euro_window, text="Witaj w generatorze EUROJACKPOT!", font=("Arial", 15, "bold"), fg=label_color,
          bg=background_color).pack(pady=(20, 10))
    Label(euro_window, text="Ile masz kuponów? (max. 10)", font=("Arial", 12), fg=label_color,
          bg=background_color).pack()

    liczbalosow = Entry(euro_window, font=("Arial", 12))
    liczbalosow.pack(pady=5)

    Button(euro_window, text="Losuj!", command=losuj2, bg=button_color, fg=button_text_color,
           font=("Arial", 12, "bold")).pack(pady=10)

    wynik = Text(euro_window, width=40, height=10, state="disabled")
    wynik.pack()


def on_closing(root, window):
    window.destroy()  # Zniszcz okno podrzędne
    root.deiconify()  # Przywróć główne okno


def main():
    root = Tk()
    root.geometry("700x500")
    root.title("Wybór loterii")

    # Utworzenie ramki dla tytułu
    title_frame = Frame(root, bg="#F0F0F0", pady=20)
    title_frame.pack(fill="both")

    # Tytuł aplikacji
    title_label = Label(title_frame, text="W jakiej loterii grasz?", font=("Arial", 24, "bold"), bg="#F0F0F0")
    title_label.pack()

    # Utworzenie ramki dla przycisków
    buttons_frame = Frame(root, bg="#F0F0F0")
    buttons_frame.pack(fill="both", expand=True)

    # Dodanie przycisku Lotto
    lotto_image = PhotoImage(file="lotto.png")
    lotto_button = Button(buttons_frame, image=lotto_image, bg="#F0F0F0", bd=0, command=lambda: play_lotto(root))
    lotto_button.pack(side=LEFT, padx=20, pady=50)

    # Dodanie przycisku Eurojackpot
    euro_image = PhotoImage(file="eurojackpot-logo (2).png")
    euro_button = Button(buttons_frame, image=euro_image, bg="#F0F0F0", bd=0, command=lambda: play_euro(root))
    euro_button.pack(side=LEFT, padx=20, pady=50)

    root.mainloop()


if __name__ == "__main__":
    main()
