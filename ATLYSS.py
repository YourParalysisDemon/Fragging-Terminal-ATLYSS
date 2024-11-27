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

Health_offsets = []
Mana_offsets = []
Stamina_offsets = []
Gravity_offsets = []
Max_jumps_offsets = []
Player_speed_offsets = [0XA0, 0X60, 0XDC]
Air_time_offsets = []
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
    new_thread = Thread(target=Health, daemon=True)
    new_thread.start()


def M_Player():
    new_thread = Thread(target=Player_speed, daemon=True)
    new_thread.start()
    
    
def M_Mana():
    new_thread = Thread(target=Mana, daemon=True)
    new_thread.start()
    
    
def M_Stamina():
    new_thread = Thread(target=Stamina, daemon=True)
    new_thread.start()
    
    
def M_Gravity():
    new_thread = Thread(target=Gravity, daemon=True)
    new_thread.start()
    
    
def M_Max_jumps():
    new_thread = Thread(target=Max_jumps, daemon=True)
    new_thread.start()
    
    
def M_Air():
    new_thread = Thread(target=Air_time, daemon=True)
    new_thread.start()
    
    
def M_Day():
    new_thread = Thread(target=Day_cycle, daemon=True)
    new_thread.start()
    
    
def Player_speed():
    addr1 = getpointeraddress(module1 + 0x0, Player_speed_offsets)

    while 1:
        try:
            mem.write_int(addr1, 0x0)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x0)
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
