import PySimpleGUI as sg

# Tema agar tampilan bersih
sg.theme('LightGray1')

# Definisi layout berdasarkan gambar
layout = [
    [sg.Text("Harga:", font=("Arial", 12))],
    [sg.Input(key="-HARGA-", size=(30, 1), justification='center')],
    [sg.Text("Kuantitas:", font=("Arial", 12))],
    [sg.Input(key="-QTY-", size=(30, 1), justification='center')],
    [sg.Button("Hitung Total", size=(15, 1))],
    [sg.Text("Total: Rp 0.00", key="-TOTAL-", font=("Arial", 14, "bold"))]
]

# Membuat Jendela
window = sg.Window("Program Kasir", layout, element_justification='center', size=(300, 250))

# Event Loop
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
        
    if event == "Hitung Total":
        try:
            # Mengambil data dari input dan konversi ke angka
            harga = float(values["-HARGA-"])
            qty = float(values["-QTY-"])
            
            # Perhitungan
            total = harga * qty
            
            # Update teks total dengan format ribuan
            window["-TOTAL-"].update(f"Total: Rp{total:,.2f}")
            
        except ValueError:
            # Jika input bukan angka, tampilkan pesan error
            sg.popup_error("Harap masukkan angka yang valid!", title="Error Input")

window.close()