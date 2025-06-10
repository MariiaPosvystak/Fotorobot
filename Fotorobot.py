import customtkinter as ctk
from tkinter import simpledialog, Canvas
from PIL import Image, ImageTk
import pygame

pildid = {}
objektid = {}
olemas = {}

pildid1 = {
    "nägu": ["nägu_1.png", "nägu_2.png", "nägu_3.png"],
    "juuksed": ["juuksed_1.png", "juuksed_2.png", "juuksed_3.png", "juuksed_4.png"],
    "silmad": ["silmad_1.png", "silmad_2.png", "silmad_3.png", "silmad_4.png", "silmad_5.png"],
    "nina": ["nina_1.png", "nina_2.png", "nina_3.png", "nina_4.png"],
    "suu": ["suu_1.png", "suu_2.png", "suu_3.png", "suu_4.png"],
    "kulmud": ["kulmud_1.png", "kulmud_2.png", "kulmud_3.png"]
}

indeks_pildid = {
    "nägu": -1,
    "juuksed": -1,
    "silmad": -1,
    "nina": -1,
    "suu": -1,
    "kulmud": -1
}

def toggle_osa(nimi, kategooria, x, y):
    indeks_pildid[kategooria] += 1
    if indeks_pildid[kategooria] >= len(pildid1[kategooria]):
        indeks_pildid[kategooria] = 0
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi] = False
    fail = pildid1[kategooria][indeks_pildid[kategooria]]
    pil_img = Image.open(fail).convert("RGBA").resize((400, 400))
    tk_img = ImageTk.PhotoImage(pil_img)

    pildid[nimi] = tk_img
    objektid[nimi] = canvas.create_image(x, y, image=tk_img)
    olemas[nimi] = True

    if kategooria == "nägu":
        canvas.tag_lower(objektid[nimi])
    else:
        canvas.tag_raise(objektid[nimi])

def salvesta_nägu():
    failnimi = simpledialog.askstring("Salvestapilt", "Sisesta failinimi (ilma laiendita):")
    if not failnimi:
        return
    lopp_pilt = Image.new("RGBA", (400, 400), (255, 255, 255, 255))

    for nimi, kategooria in [("nägu", "nägu"), ("juuksed", "juuksed"), ("silmad", "silmad"), ("nina", "nina"), ("suu", "suu"), ("kulmud","kulmud")]:
        if olemas.get(nimi):
            failitee = pildid1[kategooria][indeks_pildid[kategooria]]
            osa = Image.open(failitee).convert("RGBA").resize((400, 400))
            lopp_pilt.alpha_composite(osa)

    lopp_pilt.save(failnimi + ".png")

# def mangi_muusika():
#     pygame.mixer.music.play(loops=-1)

# def peata_muusika():
#     pygame.mixer.music.stop()

# pygame.mixer.init()
# pygame.mixer.music.load("muusika.mp3")

app = ctk.CTk()
app.geometry("800x800")
app.title("Näo koostaja nuppudega")

frame = ctk.CTkFrame(app)
frame.pack(side="left", padx=10, pady=10)

seaded = {
    "width": 150, "height": 40,
    "font": ("Segoe UI Emoji", 32),
    "fg_color": "blue",
    "text_color": "white",
    "corner_radius": 20
}

canvas = Canvas(app, width=400, height=400, bg="white")
canvas.pack(side="right", padx=10, pady=10)

ctk.CTkLabel(frame, text="Vali näoosad:", **seaded).pack(pady=10)

ctk.CTkButton(frame, text="Nägu", command=lambda: toggle_osa("nägu", "nägu", 200, 200), **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Juuksed", command=lambda: toggle_osa("juuksed", "juuksed", 200, 200), **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Kulmud", command=lambda: toggle_osa("kulmud", "kulmud", 200, 200), **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Silmad", command=lambda: toggle_osa("silmad", "silmad", 200, 200), **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Nina", command=lambda: toggle_osa("nina", "nina", 200, 200), **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Suu", command=lambda: toggle_osa("suu", "suu", 200, 200), **seaded).pack(pady=5)

ctk.CTkButton(frame, text="Salvesta", command=salvesta_nägu, **seaded).pack(side="bottom", pady=5)

frame_mus = ctk.CTkFrame(frame)
frame_mus.pack(padx=10, pady=10)
# ctk.CTkButton(frame_mus, text="Mängi muusikat", command=mangi_muusika, **seaded).pack(pady=5)
# ctk.CTkButton(frame_mus, text="Peata muusika", command=peata_muusika, **seaded).pack(pady=5)

app.mainloop()