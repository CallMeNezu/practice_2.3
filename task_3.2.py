import psutil
import tkinter as tk


def task_body():
    memory = psutil.virtual_memory()
    dick_usage = psutil.disk_usage("/")
    output_1 = f"""\nНагрузка CPU: {psutil.cpu_percent(interval=1)}% 
    использовано оперативной памяти: {memory.used/(1024**3):.2f} ГБ 
    процентное использование жесткого диска: {dick_usage.percent:.1f}%    
    """
    label = tk.Label(text = output_1)
    label.pack()

root = tk.Tk()
root.title("task_3.2")
root.geometry("500x350")
task_body()

root.mainloop()
