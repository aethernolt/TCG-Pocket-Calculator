import ttkbootstrap as ttk
import pywinstyles

from model import *

def setup():
    root = ttk.Window(themename = "darkly")
    root.title("TCG Pocket Calculator")
    root.resizable(0, 0)
    root.minsize(1000, 600)

    # this only works in windows 11 and will probably break in any other verison
    pywinstyles.change_header_color(root, "#1c1c1c")

    n = ttk.Notebook(root)
    n.pack(expand = True, ipadx = 10, ipady = 10)
    pageMain = ttk.Frame(n, width = 1000, height = 600) # main page
    pageMain.pack(fill = "both", expand = True)
    pageStats = ttk.Frame(n, width = 1000, height = 600) # stats page
    pageStats.pack(fill = "both", expand = True)
    pageMissions = ttk.Frame(n, width = 1000, height = 600) # missions page
    pageMissions.pack(fill = "both", expand = True)
    n.add(pageMain, text = "Main")
    n.add(pageStats, text = "Stats")
    n.add(pageMissions, text = "Missions")

    bAddPack = ttk.Button(pageMain,
                          text = "Add Pack",
                          command = set.add,
                          bootstyle = ("success, outline")).grid(column = 1, row = 1, padx = 20, pady = 12)
    bAdd = ttk.Button(pageMain,
                      text = "Add Card",
                      command = card.test,
                      bootstyle = ("success, outline")).grid(column = 1, row = 2, padx = 20, pady = 12)
    bRemove = ttk.Button(pageMain,
                         text = "Remove Card",
                         command = card.test,
                         bootstyle = ("danger, outline")).grid(column = 1, row = 3, padx = 20, pady = 12)
    bExport = ttk.Button(pageMain,
                         text = "Export Data",
                         command = temp,
                         bootstyle = "").grid(column = 1, row = 4, padx = 20, pady = 12)

    root.mainloop()

def temp():
    print("working on it")