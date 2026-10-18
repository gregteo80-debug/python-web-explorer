import tkinter as tk #Libary for GUI(graphical user interface)
from tkinter import messagebox#From GUI libarary import messagebox for show a box with information
from threading import Thread as th#Libarry what give us an obility  to create a thread for run a function in background
from urllib.parse  import urlparse#This libary give as an obility to parse a  url and get an url's components like scheme, netloc, path, params, query, fragment
import requests#This libary give us an obility to send a request to a server(HTTP request) and get a response from a server(like HTml code and so on)
from bs4 import BeautifulSoup#And this libary give us an obility to parse a Html code from response and get a data from Html code like text, links, titles of website and so on


def show_result(report):
    result_text.delete("1.0",tk.END)
    result_text.insert(tk.END,report)
    button_analyze.config(state="normal")


def analyze_website():
    url = entry_url.get().strip()

    if not url:
        messagebox.showwarning("Warning","Enter a website adress.")
        return
    if not url.startswith(("https://","http://")):
        url = "https://" + url

    button_analyze.config(state="disabled")
    result_text.delete("1.0",tk.END)
    result_text.insert(tk.END,"Loading  webiste...")

    th(target=fetch_website,args=(url,),daemon=True).start()




def fetch_website(url):
    
    try:

        

        response = requests.get(url,timeout=10)
        response.raise_for_status()#Raise an exeption if the response status code indicate an  error(like 404 or 500)
        
        soup = BeautifulSoup(response.text,"html.parser")

        title_tag = soup.find("title")

        

        if title_tag:
            page_title = title_tag.get_text(strip=True)
        else:
            page_title = "No title found"
        headings = [tag.get_text(" ",strip=True) for tag in soup.select("h1, h2, h3")]
        links = []
        for link in soup.select("a[href]"):
            text = link.get_text(" ", strip=True) or "(no text)"
            adress = link.get("href")
            links.append(f"{text} --> {adress}")

        result_text.delete("1.0", tk.END)
        report  = f"Website: {response.url}\n"
        report += f"HTTP status: {response.status_code}\n"
        report += f"Page title: {page_title}\n"

        report += f"Headings ({len(headings)}):\n"
        report += "\n".join(headings[:50]) or "No headings found"

        report +=  "\n\n"
        report += f"Links ({len(links)}):\n"
        report += "\n".join(links[:100]) or "No links found"
        

        if response.text and Ch.get() == True  :
            report +=  "\n\nHtml code: \n"
            report  += f"{response.text}"
        if response.text == None and Ch.get() == True:
            report +=  "\n\nHtml code: \n"
            report += f"No html code found."
        window.after(0,show_result,report)
    except requests.RequestException as error:
        window.after(0,show_result,f"Could not load webiste:\n{error}")



window = tk.Tk()
window.title("Web Explorer")
window.geometry("750x600")
window.minsize(500,400)


Ch = tk.BooleanVar(value=True)

title_label = tk.Label(window,text="Web Explorer",font=("Sans Serif",20,"bold","underline"))
title_label.pack(pady=12)

url_Label = tk.Label(window,text="Enter the URL:",font=("Sans Serif",15))
url_Label.pack(pady=10)

entry_url = tk.Entry(window,width=60,font=("Sans Serif",10))
entry_url.pack(pady=10,fill="x",padx=10)
entry_url.insert(0,"https://example.com")#Insert  a default url in entry for user to see how it works
frame = tk.Frame(window)
frame.pack()

checkbox = tk.Checkbutton(frame,text="Html code:",variable=Ch)
checkbox.pack(pady=10,side="right",padx=15)


button_analyze = tk.Button(frame,text="Analyze website",font=("Sans Serif",10),command=analyze_website)
button_analyze.pack(pady=10,side="left",padx=15)

result_text = tk.Text(window,wrap="word",font=("Consolas",10))
result_text.pack(padx=15,pady=10,fill="both",expand=True)
#wrap="word" - This option allows the text  to wrap at word boundaries, ensuring that words are not split across lines.
#expand=True - This option allows the text widget to expand and fill any avaliable space in the parent window.
window.mainloop()