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
module1 = module_from_name(mem.process_handle, "UnityPlayer.dll").lpBaseOfDll

Health = []
Mana = []
Stamina = []
Gravity = []
Max_jumps = []
Player_speed = [0XA0, 0X60, 0XDC]
Air_time = []
Day_cycle = []


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


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
root.geometry("270x230")


def callback(url):
    webbrowser.open_new(url)


def show():
    root.deiconify()


def hide():
    root.withdraw()


# Links
link1 = tk.Label(root, text="Your Sleep Paralysis Demon", bg="black", fg="red", cursor="hand2")
link1.grid(row=8, column=0)
link1.bind("<Button-1>", lambda e: callback("https://steamcommunity.com/profiles/76561198259829950/"))

# Hot keys
keyboard.add_hotkey("-", show)
keyboard.add_hotkey("+", hide)
keyboard.add_hotkey("", )
keyboard.add_hotkey("", )
keyboard.add_hotkey("", )
keyboard.add_hotkey("", )
keyboard.add_hotkey("K", root.destroy)
root.mainloop()
