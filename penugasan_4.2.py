import PySimpleGUI as sg

# Konfigurasi Tema
sg.theme('LightGray1')

# Data Dummy untuk Tabel
data_pelanggan = []

# Layout Kolom Kiri (Input)
col_input = [
    [sg.Text("Cari NoPol", size=(12, 1)), sg.Input(key="-CARI-", size=(15, 1)), sg.Button("Cari")],
    [sg.Text("No Plat Polisi", size=(12, 1)), sg.Input(key="-PLAT-", size=(22, 1))],
    [sg.Text("Waktu Masuk", size=(12, 1)), sg.Input(key="-MASUK-", size=(22, 1))],
    [sg.Text("Waktu Keluar", size=(12, 1)), sg.Input(key="-KELUAR-", size=(22, 1))],
    [sg.Text("Biaya", size=(12, 1)), sg.Input("0", key="-BIAYA-", size=(15, 1)), sg.Button("Hitung", key="-HITUNG-")],
]

# Layout Kolom Kanan (Info Biaya)
col_info = [
    [sg.Text("Biaya Per Jam", text_color='red', font=("Comic Sans MS", 15))],
    [sg.Text("Rp. 2.000", text_color='red', font=("Comic Sans MS", 30, "bold"))]
]

# Layout Tabel (Bagian Bawah)
layout_tabel = [
    [
        sg.Column([
            [sg.Text("List Pelanggan Urut Terakhir Keluar", text_color='blue')],
            [sg.Table(values=data_pelanggan, headings=["No Plat Polisi", "Masuk", "Keluar", "Biaya"], 
                      auto_size_columns=False, col_widths=[12, 8, 8, 10], key="-TABEL1-", num_rows=5)]
        ]),
        sg.Column([
            [sg.Text("List Pelanggan Banyak Bayar", text_color='blue')],
            [sg.Table(values=data_pelanggan, headings=["No Plat Polisi", "Masuk", "Keluar", "Biaya"], 
                      auto_size_columns=False, col_widths=[12, 8, 8, 10], key="-TABEL2-", num_rows=5)]
        ])
    ]
]

# Gabungkan Semua Layout
layout = [
    [sg.Text("Aplikasi Parkir Kelompok 6", font=("Comic Sans MS", 16))],
    [sg.Column(col_input), sg.VerticalSeparator(), sg.Column(col_info, element_justification='center')],
    [sg.HSeparator()],
    *layout_tabel
]

window = sg.Window("Program Parkir", layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == "-HITUNG-":
        try:
            # Logika sederhana: Keluar - Masuk (dalam jam)
            masuk = int(values["-MASUK-"])
            keluar = int(values["-KELUAR-"])
            durasi = keluar - masuk
            
            if durasi < 0:
                sg.popup_error("Waktu keluar tidak boleh lebih kecil dari waktu masuk!")
                continue
                
            biaya = durasi * 2000
            window["-BIAYA-"].update(str(biaya))
            
            # Tambah ke tabel
            data_baru = [values["-PLAT-"], values["-MASUK-"], values["-KELUAR-"], f"Rp {biaya}"]
            data_pelanggan.append(data_baru)
            
            # Update kedua tabel
            window["-TABEL1-"].update(values=data_pelanggan)
            window["-TABEL2-"].update(values=sorted(data_pelanggan, key=lambda x: x[3], reverse=True))
            
        except ValueError:
            sg.popup_error("Masukkan jam dalam angka (contoh: Masuk 8, Keluar 10)")

window.close()