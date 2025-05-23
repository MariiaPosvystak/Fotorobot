from tkinter.messagebox import showinfo
import customtkinter as ctk
from tkinter import PhotoImage, simpledialog,Canvas
from PIL import Image, ImageTk
import pygame

pildid={}
objektid={}
olemas={}

def salvesta_nägu():
    failinimi = simpledialog.askstring("Salvesta pilt", "Sisesta faili nimi (ilma laiendita):")
    if not failinimi:
        return
    lõpp_pilt = Image.new("RGBA", (400, 400), (255, 255, 255, 255))
    for nimi in ["nägu","otsmik", "silmad", "nina", "suu"]:
        if olemas.get(nimi):
            failitee={
                "nägu":"Nägu.png",
                "otsmik": "LOtsmik.png",
                "silmad":"LSilmad.png",
                "nina":"LNina.png",
                "suu":"LSuu.png"}.get(nimi)
            if failitee:
                osa=Image.open(failitee).convert("RGBA").resize((400, 400))
                lõpp_pilt.alpha_composite(osa)
    lõpp_pilt.save(f"{failinimi}"".png")
    showinfo("Pilt salvestatud:", f"Fail nimi on {failinimi}.png")
            

# def toggle_osa(nimi, fail, x, y):
#     if olemas.get(nimi):
#         canvas.delete(objektid[nimi])
#         olemas[nimi]=False
#     else:
#         pil_img= Image.open("cat.png").convert("RGBA").resize((400,400))
#         tk_img=ImageTk.PhotoImage(pil_img)
#         pildid[nimi]=tk_img
#         objektid[nimi]=canvas.create_image(x, y, image=tk_img)
#         olemas[nimi]=True


# fail={"LHair.png","LNina.png","LOtsmik.png","LSilmad.png","LSuu.png"}

def toggle_osa(nimi, fail, x, y):
    if olemas.get(nimi):
        canvas.delete(objektid[nimi])
        olemas[nimi] = False
    else:
        pil_img = Image.open(fail).convert("RGBA").resize((400, 400))
        tk_img = ImageTk.PhotoImage(pil_img)
        pildid[nimi] = tk_img
        objektid[nimi] = canvas.create_image(x, y, image=tk_img)
        olemas[nimi] = True


# def mängi_muusika():
#     pygame.mixer.music.play(loops=-1)
# def peata_muusika():
#     pygame.mixer.music.stop()
# pygame.mixer.init()
# pygame.mixer.music.load("taustamuusika.mp3")

app=ctk.CTk()
app.geometry("800x500")
app.title("Näo koostaja nuppudega")

#Canvas paremal
canvas=Canvas(app,width=400,height=400,bg="white")
canvas.pack(side="right", padx=10, pady=10)

toggle_osa("nägu", "alus.png", 200, 200)
olemas["nägu"]=True

frame = ctk.CTkFrame(app)
frame.pack(side="left",padx=0,pady=10)
seaded={
    "width": 150, "height":40,
    "font": ("Segoe UI Emoji",32),
    "fg_color":"#4CAF50",
    "text_color":"white",
    "corner_radius":20}
ctk.CTkLabel(frame, text="Vali näoosad:", **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Otsmik", command=lambda: toggle_osa("otsmik", "LOtsmik.png", 200, 200), **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Silmad", command=lambda: toggle_osa("silmad", "LSilmad.png", 200, 200), **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Nina", command=lambda: toggle_osa("nina", "LNina.png", 200, 200), **seaded).pack(pady=5)
ctk.CTkButton(frame, text="Suu", command=lambda: toggle_osa("suu", "LSuu.png", 200, 200), **seaded).pack(pady=5)
# ctk.CTkButton(frame, text="Otsmik", command=lambda: toggle_osa("otmik, LOtsmik.png",200,200) ,**seaded).pack(pady=5)
# ctk.CTkButton(frame, text="Silmad", command=lambda: toggle_osa("silmad, LSilmad.png",200,200) ,**seaded).pack(pady=5)
# ctk.CTkButton(frame, text="Nina", command=lambda: toggle_osa("nina, LNina.png",200,200) ,**seaded).pack(pady=5)
# ctk.CTkButton(frame, text="Suu", command=lambda: toggle_osa("suu, LSuu.png",200,200) ,**seaded).pack(pady=5)
nupp=ctk.CTkButton(frame, text="Salvesta nägu", command=salvesta_nägu, **seaded)
nupp.pack(pady=10)

frame_mus=ctk.CTkFrame(frame)
frame_mus.pack(pady=10,padx=10)

# ctk.CTkButton(frame_mus, text="Mängi muusikat", fg_color="#4CAF550", command=mängi_muusika).pack(side="left",pady=10)
# ctk.CTkButton(frame_mus, text="Peata muusika", fg_color="#4CAF550", command=peata_muusika).pack(side="left",pady=10)

app.mainloop()