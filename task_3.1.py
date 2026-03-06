import requests
import tkinter as tk

root = tk.Tk()
root.title("task_3.1")
root.geometry("500x300+400+225")

urls= ['https://github.com/', 'https://www.binance.com/en',
       'https://tomtit.tomsk.ru/', 'https://jsonplaceholder.typicode.com/',
       'https://moodle.tomtit-tomsk.ru/']

for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            url_true = tk.Label(text = f"{url} доступен")
            url_true.pack(anchor = "nw")
            print(f"{url} доступен")
        else:
            url_false = tk.Label(text = f"{url} не доступен. Код: {response.status_code}")
            url_false.pack(anchor = "nw")
            print(f"{url} не доступен. Код: {response.status_code}")
    except requests.exceptions.RequestException as e:
        url_error = tk.Label(text = f"ошибка {url}: {e}")
        url_error.pack(anchor = "nw")
        print(f"ошибка {url}: {e}")

root.mainloop()
