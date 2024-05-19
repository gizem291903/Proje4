import tkinter as tk
from tkinter import ttk
import sqlite3


def etkinlik_penceresi():
    etkinlik_pencere = tk.Toplevel(main_window)
    etkinlik_pencere.title("Etkinlik Yönetim Sistemi")

    def etkinlikleri_listele():
        etkinlik_listbox.delete(0, tk.END)
        conn = sqlite3.connect('etkinlik_yonetimi.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Etkinlik")
        etkinlikler = c.fetchall()
        for etkinlik in etkinlikler:
            etkinlik_listbox.insert(tk.END, etkinlik)
        conn.close()

    def etkinlik_ekle():
        adi = etkinlik_adi_entry.get()
        tarih = etkinlik_tarih_entry.get()
        yer = etkinlik_yer_entry.get()
        conn = sqlite3.connect('etkinlik_yonetimi.db')
        c = conn.cursor()
        c.execute("INSERT INTO Etkinlik (etkinlik_adi, tarih, yer) VALUES (?, ?, ?)", (adi, tarih, yer))
        conn.commit()
        conn.close()
        etkinlikleri_listele()

    etkinlik_ekle_frame = ttk.LabelFrame(etkinlik_pencere, text="Etkinlik Ekle")
    etkinlik_ekle_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    etkinlik_adi_label = ttk.Label(etkinlik_ekle_frame, text="Etkinlik Adı:")
    etkinlik_adi_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    etkinlik_adi_entry = ttk.Entry(etkinlik_ekle_frame)
    etkinlik_adi_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    etkinlik_tarih_label = ttk.Label(etkinlik_ekle_frame, text="Tarih:")
    etkinlik_tarih_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    etkinlik_tarih_entry = ttk.Entry(etkinlik_ekle_frame)
    etkinlik_tarih_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    etkinlik_yer_label = ttk.Label(etkinlik_ekle_frame, text="Yer:")
    etkinlik_yer_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    etkinlik_yer_entry = ttk.Entry(etkinlik_ekle_frame)
    etkinlik_yer_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    etkinlik_ekle_button = ttk.Button(etkinlik_ekle_frame, text="Etkinlik Ekle", command=etkinlik_ekle)
    etkinlik_ekle_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    etkinlik_listele_frame = ttk.LabelFrame(etkinlik_pencere, text="Etkinlik Listesi")
    etkinlik_listele_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    etkinlik_listbox = tk.Listbox(etkinlik_listele_frame, width=50, height=10)
    etkinlik_listbox.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    scrollbar = ttk.Scrollbar(etkinlik_listele_frame, orient="vertical", command=etkinlik_listbox.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    etkinlik_listbox.config(yscrollcommand=scrollbar.set)

    etkinlikleri_listele()


# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('etkinlik_yonetimi.db')
c = conn.cursor()

# Tabloları oluştur
c.execute('''CREATE TABLE IF NOT EXISTS Etkinlik (
                etkinlik_id INTEGER PRIMARY KEY,
                etkinlik_adi TEXT,
                tarih TEXT,
                yer TEXT
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS Katilimci (
                katilimci_id INTEGER PRIMARY KEY,
                ad TEXT,
                soyad TEXT,
                email TEXT
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS Bilet (
                bilet_id INTEGER PRIMARY KEY,
                etkinlik_id INTEGER,
                katilimci_id INTEGER,
                FOREIGN KEY(etkinlik_id) REFERENCES Etkinlik(etkinlik_id),
                FOREIGN KEY(katilimci_id) REFERENCES Katilimci(katilimci_id)
            )''')

# Veritabanına değişiklikleri kaydet
conn.commit()

# Veritabanı bağlantısını kapat
conn.close()


def katilimci_penceresi():
    katilimci_pencere = tk.Toplevel(main_window)
    katilimci_pencere.title("Katılımcı Yönetim Sistemi")

    def katilimcilari_listele():
        katilimci_listbox.delete(0, tk.END)
        conn = sqlite3.connect('etkinlik_yonetimi.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Katilimci")
        katilimciler = c.fetchall()
        for katilimci in katilimciler:
            katilimci_listbox.insert(tk.END, katilimci)
        conn.close()

    def katilimci_ekle():
        ad = katilimci_ad_entry.get()
        soyad = katilimci_soyad_entry.get()
        email = katilimci_email_entry.get()
        conn = sqlite3.connect('etkinlik_yonetimi.db')
        c = conn.cursor()
        c.execute("INSERT INTO Katilimci (ad, soyad, email) VALUES (?, ?, ?)", (ad, soyad, email))
        conn.commit()
        conn.close()
        katilimcilari_listele()

    katilimci_ekle_frame = ttk.LabelFrame(katilimci_pencere, text="Katılımcı Ekle")
    katilimci_ekle_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    katilimci_ad_label = ttk.Label(katilimci_ekle_frame, text="Ad:")
    katilimci_ad_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    katilimci_ad_entry = ttk.Entry(katilimci_ekle_frame)
    katilimci_ad_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    katilimci_soyad_label = ttk.Label(katilimci_ekle_frame, text="Soyad:")
    katilimci_soyad_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    katilimci_soyad_entry = ttk.Entry(katilimci_ekle_frame)
    katilimci_soyad_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    katilimci_email_label = ttk.Label(katilimci_ekle_frame, text="Email:")
    katilimci_email_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    katilimci_email_entry = ttk.Entry(katilimci_ekle_frame)
    katilimci_email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    katilimci_ekle_button = ttk.Button(katilimci_ekle_frame, text="Katılımcı Ekle", command=katilimci_ekle)
    katilimci_ekle_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    katilimci_listele_frame = ttk.LabelFrame(katilimci_pencere, text="Katılımcı Listesi")
    katilimci_listele_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    katilimci_listbox = tk.Listbox(katilimci_listele_frame, width=50, height=10)
    katilimci_listbox.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    scrollbar = ttk.Scrollbar(katilimci_listele_frame, orient="vertical", command=katilimci_listbox.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    katilimci_listbox.config(yscrollcommand=scrollbar.set)

    katilimcilari_listele()


def bilet_penceresi():
    bilet_pencere = tk.Toplevel(main_window)
    bilet_pencere.title("Bilet Yönetim Sistemi")

    def biletleri_listele():
        bilet_listbox.delete(0, tk.END)
        conn = sqlite3.connect('etkinlik_yonetimi.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Bilet")
        biletler = c.fetchall()
        for bilet in biletler:
            bilet_listbox.insert(tk.END, bilet)
        conn.close()

    def bilet_ekle():
        etkinlik_id = etkinlik_id_entry.get()
        katilimci_id = katilimci_id_entry.get()
        conn = sqlite3.connect('etkinlik_yonetimi.db')
        c = conn.cursor()
        c.execute("INSERT INTO Bilet (etkinlik_id, katilimci_id) VALUES (?, ?)", (etkinlik_id, katilimci_id))
        conn.commit()
        conn.close()
        biletleri_listele()

    bilet_ekle_frame = ttk.LabelFrame(bilet_pencere, text="Bilet Ekle")
    bilet_ekle_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    etkinlik_id_label = ttk.Label(bilet_ekle_frame, text="Etkinlik ID:")
    etkinlik_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    etkinlik_id_entry = ttk.Entry(bilet_ekle_frame)
    etkinlik_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    katilimci_id_label = ttk.Label(bilet_ekle_frame, text="Katılımcı ID:")
    katilimci_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    katilimci_id_entry = ttk.Entry(bilet_ekle_frame)
    katilimci_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    bilet_ekle_button = ttk.Button(bilet_ekle_frame, text="Bilet Ekle", command=bilet_ekle)
    bilet_ekle_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    bilet_listele_frame = ttk.LabelFrame(bilet_pencere, text="Bilet Listesi")
    bilet_listele_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    bilet_listbox = tk.Listbox(bilet_listele_frame, width=50, height=10)
    bilet_listbox.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    scrollbar = ttk.Scrollbar(bilet_listele_frame, orient="vertical", command=bilet_listbox.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    bilet_listbox.config(yscrollcommand=scrollbar.set)

    biletleri_listele()


def kullanım_kılavuzu():
    kullanım_kılavuzu_pencere = tk.Toplevel(main_window)
    kullanım_kılavuzu_pencere.title("Kullanım Kılavuzu")

    metin = """Etkinlik Yönetimi:
    - Etkinlik eklemek için "Etkinlik Adı", "Tarih" ve "Yer" bilgilerini girin ve "Etkinlik Ekle" butonuna tıklayın.
    - Eklenen etkinlikler etkinlik listesinde görüntülenecektir.

Katılımcı Yönetimi:
    - Katılımcı eklemek için "Ad", "Soyad" ve "Email" bilgilerini girin ve "Katılımcı Ekle" butonuna tıklayın.
    - Eklenen katılımcılar katılımcı listesinde görüntülenecektir.

Bilet Yönetimi:
    - Bilet eklemek için ilgili etkinliğin ID'sini ve katılımcının ID'sini girin ve "Bilet Ekle" butonuna tıklayın.
    - Eklenen biletler bilet listesinde görüntülenecektir."""

    metin_etiket = tk.Label(kullanım_kılavuzu_pencere, text=metin, justify="left")
    metin_etiket.pack(padx=10, pady=10)


main_window = tk.Tk()
main_window.title("Ana Sayfa")
main_window.geometry("400x300")

# Hoşgeldiniz metni
hoşgeldiniz_label = ttk.Label(main_window, text="Hoşgeldiniz!", font=("Helvetica", 16))
hoşgeldiniz_label.pack(pady=10)

# Butonlar
etkinlik_button = ttk.Button(main_window, text="Etkinlik Yönetimi", command=etkinlik_penceresi)
etkinlik_button.pack(fill="x", pady=5)

katilimci_button = ttk.Button(main_window, text="Katılımcı Yönetimi", command=katilimci_penceresi)
katilimci_button.pack(fill="x", pady=5)

bilet_button = ttk.Button(main_window, text="Bilet Yönetimi", command=bilet_penceresi)
bilet_button.pack(fill="x", pady=5)

kullanım_kılavuzu_button = ttk.Button(main_window, text="Kullanım Kılavuzu", command=kullanım_kılavuzu)
kullanım_kılavuzu_button.pack(fill="x", pady=5)


# Çıkış butonu
def cikis_yap():
    main_window.destroy()


cikis_button = ttk.Button(main_window, text="Çıkış", command=cikis_yap)
cikis_button.place(relx=1, rely=1, anchor="se")

main_window.mainloop()
