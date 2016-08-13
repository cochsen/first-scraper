from tkinter import *
from tkinter import ttk, filedialog, messagebox
import base64
import json
import os
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    tk_root = Tk()
    tk_root.title('First Scraper')

    tk_mainframe = ttk.Frame(tk_root, padding = '5 5 5 5')
    tk_mainframe.grid(row = 0, column = 0, sticky = (E, W, N, S))

    tk_url_frame = ttk.LabelFrame(tk_mainframe, text = 'URL', padding = '5 5 5 5')
    tk_url_frame.grid(row = 0, column = 0, sticky = (E, W))
    tk_url_frame.columnconfigure(0, weight = 1)
    tk_url_frame.rowconfigure(0, weight = 1)

    url = StringVar()
    url.set('http://localhost:8080')
    tk_url_entry = ttk.Entry(tk_url_frame, width = 40, textvariable = url)
    tk_url_entry.grid(row = 0, column = 0, sticky = (E, W, S, N), padx = 5)
    tk_fetch_btn = ttk.Button(tk_url_frame, text = 'Fetch info', command = fetch_url)
    tk_fetch_btn.grid(row = 0, column = 1, sticky = W, padx = 5)

    tk_img_frame = ttk.LabelFrame(tk_mainframe, text = 'Content', padding = '9 0 0 0')
    tk_img_frame.grid(row = 1, column = 0, sticky = (N, S, E, W))

    images = StringVar()
    tk_img_listbox = ListBox(tk_img_frame, listvariable = images, height = 6, width = 25)
    tk_img_listbox.grid(row = 0, column = 0, sticky = (E, W), pady = 5)
    tk_scrollbar = ttk.Scrollbar(tk_img_frame, orient = VERTICAL, command = tk_img_listbox.yview)
    tk_scrollbar.grid(row = 0, column = 1, sticky = (S, N), pady = 6)
    tk_img_listbox.configure(yscrollcommand = tk_scrollbar.set)

    tk_radio_frame = ttk.Frame(tk_img_frame)
    tk_radio_frame.grid(row = 0, column = 2, sticky = (N, S, W, E))
    tk_choice_lbl = ttk.Label(tk_radio_frame, text = 'Choose how to save images')
    tk_choice_lbl.grid(row = 0, column = 0, padx = 5, pady = 5)

    save_method = StringVar()
    save_method.set('img')
    tk_img_only_radio = ttk.Radiobutton(tk_radio_frame, text = 'As Images', variable = save_method, value = 'img')
    tk_img_only_radio.grid(row = 1, column = 0, padx = 5, pady = 2, sticky = W)
    tk_img_only_radio.configure(state = 'normal')
    tk_json_radio = ttk.Radiobutton(tk_radio_frame, text = 'As JSON', variable = save_method, value = 'json')
    tk_json_radio.grid(row = 2, column = 0, padx = 5, pady = 2, sticky = W)

    tk_scrape_btn = ttk.Button(tk_mainframe, text = 'Scrape', command = save)
    tk_scrape_btn.grid(row = 2, column = 0, sticky = E, pady = 5)

    tk_status_frame = ttk.Frame(tk_root, relief = 'sunken', padding = '2 2 2 2')
    tk_status_frame.grid(row = 1, column = 0, sticky = (E, W, S))
    
    status_msg = StringVar()
    status_msg.set('Type a URL to start scraping ...')
    tk_status = ttk.Label(tk_status_frame, textvariable = status_msg, anchor = W)
    tk_status.grid(row = 0, column = 0, sticky = (E, W))

    tk_root.mainloop()  # run application