# Import necessary libraries for web scraping
from selenium import webdriver
from selenium.webdriver.common.by import By  # Updated for modern Selenium
from time import sleep

# Initialize Chrome WebDriver (ensure chromedriver is in the specified path or add to PATH)
site = webdriver.Chrome('C:/Users/M/Desktop/AL Tools/Web Scraping/chromedriver.exe')

# Navigate to the starting page for Quran chapter 1
site.get('https://www.clearquran.com/001.html')

# Initialize lists to store scraped data
AYAT = []  # List to store cleaned verse texts
NUM = []   # List to store verse numbers with chapter names (e.g., '1 al-Fatihah')
MAX = []   # List to store maximum verse count per chapter

# Loop through all 114 chapters of the Quran
for i in range(114):
    # Locate the element containing the Quran text
    ayat = site.find_element(By.XPATH, '//*[@id="quran-text"]')
    
    # Handle the first chapter (Al-Fatihah) separately
    if i == 0:
        # Clean verse texts by removing numbers
        sents = [' '.join(i.split()[1:]) for i in ayat.text.split('\n')]
        # Extract verse numbers and chapter names
        for x in range(300):
            try:
                r = site.find_element(By.XPATH, f'/html/body/div[1]/div[4]/div[2]/p[{x+1}]/span')
                e = site.find_element(By.XPATH, '//*[@id="chNameAr"]')
                NUM.append(f'{str(x+1)} {e.text}')
            except:
                # Append max verse count for this chapter and break
                MAX.append(7)
                break
    else:
        # Clean verse texts for other chapters, skipping the first line
        sents = [' '.join(i.split()[1:]) for i in ayat.text.split('\n')][1:]
        # Extract verse numbers and chapter names
        for x in range(300):
            try:
                r = site.find_element(By.XPATH, f'/html/body/div[1]/div[4]/div[2]/p[{x+3}]/span')
                e = site.find_element(By.XPATH, '//*[@id="chNameAr"]')
                NUM.append(f'{str(x+1)} {e.text}')
            except:
                # Append max verse count for this chapter and break
                MAX.append(x)
                break
    
    # Append cleaned verses to AYAT list
    AYAT += sents
    
    # Get current chapter number for load verification
    t = site.find_element(By.XPATH, '//*[@id="chNumber"]').text
    
    # Click the next chapter arrow
    site.find_element(By.XPATH, '//*[@id="arrow-right"]').click()
    
    # Wait loop to ensure the next chapter has loaded
    while True:
        try:
            ell = site.find_element(By.XPATH, '//*[@id="chNumber"]')
            if t == ell.text:
                sleep(0.1)  # Short delay if page hasn't loaded yet
            else:
                break
        except:
            sleep(0.1)  # Handle exceptions during loading

# Print the NUM list (verse numbers with chapter names)
print(NUM)

# Import pandas for data export (assuming ALL is a dictionary or data structure; if undefined, replace with appropriate variable)
import pandas as pd
# Export data to CSV (note: ALL is not defined in previous cells; assuming it's AYAT or a derived structure)
pd.DataFrame(ALL).to_csv('E:/Other abbas/other-python/ayeh.csv')  # Replace ALL with correct variable if needed

# GUI code for displaying results (requires tkinter and webbrowser)
from tkinter import *
from tkinter import ttk
import webbrowser

# Derive unique surah names from NUM
surah_values = []
for i in [x.split()[1] for x in NUM]:
    if i not in surah_values:
        surah_values.append(i)

# Assume ALL is predefined or loaded; here it's set to ALl (possible typo in original)
ALl = ALL  # Note: ALL needs definition; this may cause NameError if not set

# Initialize Tkinter window
win = Tk()
win.resizable(0, 0)
win.configure(bg='yellow')
win.geometry('800x600')

# Load background image (ensure the file exists to avoid TclError)
bg = PhotoImage(file="E:/Other abbas/other-python/qq.png")  # If file missing, comment out or replace

# Create background label (may cause TclError if image not found or Tkinter issue)
l1 = Label(win, width=800, height=600, image=bg)
l1.place(x=0, y=0)

# Instruction label
l2 = Label(win, text='Please select the desired verse:', font=('b', 25, 'bold'))
l2.place(x=140, y=10)

# Combobox for surah selection
surah = ttk.Combobox(win, width=15, font=("b", 25), values=surah_values)
surah.current(0)
surah.place(x=440, y=100)

# Combobox for ayah selection (initially limited)
ayeh = ttk.Combobox(win, width=15, font=("b", 25), values=[1, 2, 3, 4, 5, 6, 7])
ayeh.current(0)
ayeh.place(x=110, y=100)

# Function to update ayah options based on selected surah
def changed(event):
    ayeh['values'] = [n for n in range(1, MAX[surah_values.index(surah.get())] + 1)]

surah.bind('<<ComboboxSelected>>', changed)

# Entry widgets for displaying results
e1 = Entry(font=('b', 17), width=17, fg='cyan', bg='blue')
e1.place(x=30, y=540)

e2 = Entry(font=('b', 17), width=17, fg='cyan', bg='blue')
e2.place(x=150, y=500)

e3 = Entry(font=('b', 17), width=17, fg='cyan', bg='blue')
e3.place(x=270, y=460)

e4 = Entry(font=('b', 17), width=17, fg='cyan', bg='blue')
e4.place(x=390, y=420)

e5 = Entry(font=('b', 17), width=17, fg='cyan', bg='blue')
e5.place(x=520, y=380)

# Function to open URL in browser
def open_url(url):
    webbrowser.open_new_tab(url)

# Function to display similar verses (assumes ALL/ALl structure)
def showw():
    global ALL  # Global reference (may need definition)
    for i in ALl:
        if i == ayeh.get() + ' ' + surah.get():
            vals = ALl[i]
            # Generate URL and insert result for e5
            url = f'https://quran.com/{surah_values.index(vals[0][0].split()[1]) + 1}/{vals[0][0].split()[0]}'
            e5.insert(0, vals[0][0] + ': ' + str(vals[0][1]) + '%')
            e5.bind("<Button-1>", lambda e: open_url(url))
            
            # Similar for e4
            url = f'https://quran.com/{surah_values.index(vals[1][0].split()[1]) + 1}/{vals[1][0].split()[0]}'
            e4.insert(0, vals[1][0] + ': ' + str(vals[1][1]) + '%')
            e4.bind("<Button-1>", lambda e: open_url(url))
            
            # Similar for e3
            url = f'https://quran.com/{surah_values.index(vals[2][0].split()[1]) + 1}/{vals[2][0].split()[0]}'
            e3.insert(0, vals[2][0] + ': ' + str(vals[2][1]) + '%')
            e3.bind("<Button-1>", lambda e: open_url(url))
            
            # Similar for e2
            url = f'https://quran.com/{surah_values.index(vals[3][0].split()[1]) + 1}/{vals[3][0].split()[0]}'
            e2.insert(0, vals[3][0] + ': ' + str(vals[3][1]) + '%')
            e2.bind("<Button-1>", lambda e: open_url(url))
            
            # Similar for e1
            url = f'https://quran.com/{surah_values.index(vals[4][0].split()[1]) + 1}/{vals[4][0].split()[0]}'
            e1.insert(0, vals[4][0] + ': ' + str(vals[4][1]) + '%')
            e1.bind("<Button-1>", lambda e: open_url(url))

# Button to trigger showw function
b = Button(text='find', bg='purple', fg='white', width=10, font=('b', 20), command=showw)
b.place(x=340, y=300)

# Start the Tkinter main loop
win.mainloop()
