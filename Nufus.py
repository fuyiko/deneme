import tkinter as tk
from tkinter import filedialog

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

    kayıt_yolu = r"C:\Users\fuat.kanik\Desktop\Yeni klasör/test.xml"

    tree = ET.parse(filename)
    root = tree.getroot()
    
    dosyalar = root.findall('.//dosya')  # Tüm 'dosya' elemanlarını bul
    
    for dosya in dosyalar:
        taraflar = dosya.findall('taraf')  # Her 'dosya' elemanının altındaki 'taraf' elemanlarını bul
        for taraf in taraflar:
            kisi_kurumlar = taraf.findall('kisiKurumBilgileri')  # 'taraf' elemanının altındaki 'kisiKurumBilgileri' elemanlarını bul
            for kisi_kurum in kisi_kurumlar:
                kisi_adresler = kisi_kurum.findall('adres')  # 'kisiKurumBilgileri' elemanlarının altındaki 'adres' elemanlarını bul
                for kisi_adres in kisi_adresler:
                    kisi_adres.set('adres', 'mernis adreslidir')  # 'adres' elemanlarının 'adres' özniteliğini 'test' olarak değiştir
    
    tree.write(kayıt_yolu, encoding = 'utf-8')
    
    print("İşlem tamamlandı.")

    

root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

root.mainloop()