import PySimpleGUI as sg

# Konfigurasi Tema
sg.theme('LightBlue')

# Layout bagian judul dengan background biru muda
layout_judul = [
    [sg.Text("DATA SISWA BARU", font=("Arial", 20, "bold"), justification='center', expand_x=True, pad=(0, 20))]
]

# Layout form input
layout_form = [
    [sg.Text("Nama Lengkap", size=(15, 1))],
    [sg.Input(key="-NAMA-", expand_x=True)],
    
    [sg.Text("Tanggal Lahir", size=(15, 1))],
    [sg.Input(key="-TGL-", expand_x=True)],
    
    [sg.Text("Asal Sekolah", size=(15, 1))],
    [sg.Input(key="-ASAL-", expand_x=True)],
    
    [sg.Text("NISN", size=(15, 1))],
    [sg.Input(key="-NISN-", expand_x=True)],
    
    [sg.Text("Nama Ayah", size=(15, 1))],
    [sg.Input(key="-AYAH-", expand_x=True)],
    
    [sg.Text("Nama Ibu", size=(15, 1))],
    [sg.Input(key="-IBU-", expand_x=True)],
    
    [sg.Text("Nomor Telepon / HP", size=(15, 1))],
    [sg.Input(key="-TELP-", expand_x=True)],
    
    [sg.Text("Alamat", size=(15, 1))],
    [sg.Multiline(key="-ALAMAT-", expand_x=True, size=(45, 5))],
]

# Layout bagian tombol di bawah
layout_tombol = [
    [sg.Push(), sg.Button("Hapus", button_color=('white', '#d35400'), size=(10, 1)), 
     sg.Button("Simpan", button_color=('white', '#d35400'), size=(10, 1)), sg.Push()]
]

# Gabungkan semua bagian layout
layout = [
    [sg.Column(layout_judul, background_color='#9dedf7', pad=(0,0), expand_x=True)],
    [sg.Column(layout_form, pad=(50, 20))],
    [sg.Column(layout_tombol, background_color='#9dedf7', expand_x=True, pad=(0,0))]
]

# Membuat Jendela
window = sg.Window("MainWindow", layout, size=(600, 750), finalize=True, element_padding=(0, 5))

# Event Loop
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
        
    if event == "Simpan":
        # Logika sederhana menampilkan data yang disimpan
        nama = values["-NAMA-"]
        if nama:
            sg.popup(f"Data Siswa: {nama} berhasil disimpan!", title="Sukses")
        else:
            sg.popup_error("Nama Lengkap tidak boleh kosong!")

    if event == "Hapus":
        # Mengosongkan semua input
        for key in ["-NAMA-", "-TGL-", "-ASAL-", "-NISN-", "-AYAH-", "-IBU-", "-TELP-", "-ALAMAT-"]:
            window[key].update("")

window.close()