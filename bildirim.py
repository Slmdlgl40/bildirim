from plyer import notification

def bildirim_goster(baslık,mesaj):
    notification.notify(title = baslık,message = mesaj,timeout = 10)

baslık_input = input("Başlığı girin: ")
mesaj_input = input("Mesajı girin: ")
bildirim_goster(baslık_input,mesaj_input)