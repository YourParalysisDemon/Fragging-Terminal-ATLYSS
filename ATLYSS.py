import keyboard
import tkinter as tk
import pygame
import pymem.exception
import webbrowser
from threading import Thread
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer

# Game were hacking
mem = Pymem("ATLYSS")

# DLL of said game
module1 = module_from_name(mem.process_handle, "mono-2.0-bdwgc.dll").lpBaseOfDll

Health_offsets = [0X150, 0XB28, 0XAC]
Mana_offsets = [0X150, 0XB28, 0XB0]
Stamina_offsets = []
Gravity_offsets = []
Max_jumps_offsets = []
Player_speed_offsets = [0X350, 0XB5C]
Air_time_offsets = [0X150, 0XBA8]
Day_cycle_offsets = []


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


# Threads
def M_Health():
    new_thread = Thread(target=Player_health, daemon=True)
    new_thread.start()


def M_Player():
    new_thread = Thread(target=Player_speed, daemon=True)
    new_thread.start()


def M_Mana():
    new_thread = Thread(target=Player_mana, daemon=True)
    new_thread.start()


def M_Speed():
    new_thread = Thread(target=Player_speed, daemon=True)
    new_thread.start()


def M_Air():
    new_thread = Thread(target=Player_air, daemon=True)
    new_thread.start()


def Player_speed():
    addr1 = getpointeraddress(module1 + 0x00752200, Player_speed_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x42c80000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x420c0000)
            break


def Player_health():
    addr1 = getpointeraddress(module1 + 0x007280F8, Health_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x00000013)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x00000013)
            break


def Player_mana():
    addr1 = getpointeraddress(module1 + 0x007280F8, Mana_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x00000013)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x00000013)
            break


def Player_air():
    addr1 = getpointeraddress(module1 + 0x007280F8, Air_time_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x3f800000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F"):
            mem.write_int(addr1, 0x00000000)
            break


# Are GUI
pygame.init()
pygame.mixer_music.load("music/mod.mp3")
pygame.mixer_music.play(1)

root = tk.Tk()
photo = tk.PhotoImage(file="back/155.png")
root.wm_iconphoto(False, photo)
root.attributes("-topmost", True)
root.title("Fragging Terminal")
root.configure(background='dark red')
root.geometry("270x170")


def callback(url):
    webbrowser.open_new(url)


def show():
    root.deiconify()


def hide():
    root.withdraw()


# buttons
button1 = tk.Button(root, text="Health", bg='black', fg='white', command=M_Health)
button1.grid(row=1, column=0)
button2 = tk.Button(root, text="Mana", bg='black', fg='white', command=M_Mana)
button2.grid(row=2, column=0)
button3 = tk.Button(root, text="Fly", bg='black', fg='white', command=M_Air)
button3.grid(row=3, column=0)
button4 = tk.Button(root, text="Speed", bg='black', fg='white', command=M_Speed)
button4.grid(row=4, column=0)
button5 = tk.Button(root, text="Exit", bg='white', fg='black', command=root.destroy)
button5.grid(row=5, column=0)

# text
label0 = tk.Label(master=root, text="Main Loops", bg='red', fg='black')
label0.grid(row=0, column=0)
label1 = tk.Label(master=root, text='/ Show GUI', bg='red', fg='black')
label1.grid(row=0, column=3)
label2 = tk.Label(master=root, text='* Hide GUI', bg='red', fg='black')
label2.grid(row=1, column=3)
label3 = tk.Label(master=root, text='F1 KILL LOOPS', bg='red', fg='black')
label3.grid(row=2, column=3)
label4 = tk.Label(master=root, text='R Fly on', bg='red', fg='black')
label4.grid(row=3, column=3)
label5 = tk.Label(master=root, text='F Fly off', bg='red', fg='black')
label5.grid(row=4, column=3)
label6 = tk.Label(master=root, text='K KILL EXE', bg='red', fg='black')
label6.grid(row=5, column=3)

# Links
link1 = tk.Label(root, text="Your Sleep Paralysis Demon", bg="black", fg="red", cursor="hand2")
link1.grid(row=7, column=0)
link1.bind("<Button-1>", lambda e: callback("https://steamcommunity.com/profiles/76561198259829950/"))

# Hot keys
keyboard.add_hotkey("-", show)
keyboard.add_hotkey("+", hide)
keyboard.add_hotkey("R", M_Air)
keyboard.add_hotkey("K", root.destroy)
root.mainloop()
