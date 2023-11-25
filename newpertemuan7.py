import sqlite3
from tkinter import *

# Membuat koneksi ke dalam SQLite
connection = sqlite3.connect('D:\semester 3\PEMOGRAMAN MULTIPLATFORM\PYTHON\Pertemuan7.py\datasiswa.db')
connect = connection.cursor()

# Membuat tabel nilai_siswa
connect.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa
             (nama_siswa TEXT, biologi INTEGER, fisika INTEGER, inggris INTEGER, prediksi_fakultas TEXT)''')

# Membuat objek Tkinter sebagai root window untuk antarmuka grafis.
root = Tk()

# Membuat label
nama_label = Label(root, text="Nama Siswa")
nama_label.pack()
nama_entry = Entry(root)
nama_entry.pack()

biologi_label = Label(root, text="Nilai Biologi")
biologi_label.pack()
biologi_entry = Entry(root)
biologi_entry.pack()

fisika_label = Label(root, text="Nilai Fisika")
fisika_label.pack()
fisika_entry = Entry(root)
fisika_entry.pack()

inggris_label = Label(root, text="Nilai Inggris")
inggris_label.pack()
inggris_entry = Entry(root)
inggris_entry.pack()

# Fungsi untuk submit ke dalam database
def submit():
    nama_siswa = nama_entry.get()
    biologi = int(biologi_entry.get())
    fisika = int(fisika_entry.get())
    inggris = int(inggris_entry.get())

    # Syarat untuk menentukan prediksi fakultas
    if fisika < biologi > inggris:
        prediksi_fakultas = "Kedokteran"
    elif biologi < fisika > inggris:
        prediksi_fakultas = "Teknik"
    elif biologi < inggris > fisika:
        prediksi_fakultas = "Bahasa"
    else:
        prediksi_fakultas = "Tidak dapat diprediksi"

    # Insert data ke dalam database
    connect.execute("INSERT INTO nilai_siswa VALUES (?, ?, ?, ?, ?)",
              (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))
    connection.commit()

    # Membersihkan file setelah submit
    nama_entry.delete(0, END)
    biologi_entry.delete(0, END)
    fisika_entry.delete(0, END)
    inggris_entry.delete(0, END)

# Membuat tombol submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()