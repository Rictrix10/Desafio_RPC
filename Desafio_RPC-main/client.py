import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk
import pygame 
import xmlrpc.client
import base64

pygame.mixer.init()

server_url = "http://localhost:8003" 

server_proxy = xmlrpc.client.ServerProxy(server_url, allow_none=True)

def browse_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image_file_path.set(file_path)
        show_selected_image(file_path)

def convert_image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        image_base64 = base64.b64encode(image_data).decode('utf-8')
    return image_base64

def show_selected_image(image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

def process_image(operation):
    image_path = image_file_path.get()
    if not image_path:
        result_label.config(text="Selecione uma imagem primeiro")
        return

    if operation == "convert":
        image_base64 = convert_image_to_base64(image_path)
        server_proxy.convert_to_grayscale(image_base64)
        
    elif operation == "resize":
        width = simpledialog.askinteger("Redimensionar imagem", "Insira a largura desejada:")
        height = simpledialog.askinteger("Redimensionar imagem", "Insira a altura desejada:")

        if width is not None and height is not None:
            image_base64 = convert_image_to_base64(image_path)
            server_proxy.resize(image_base64, width, height)
            
        else:
            result_label.config(text="Largura e altura inválidas.")

    elif operation == "rotate":
        angle = simpledialog.askinteger("Rodar imagem", "Insira o ângulo de rotação desejado (em graus):")  

        if angle is not None:
            image_base64 = convert_image_to_base64(image_path)
            server_proxy.rotate_image(image_base64, angle)

    elif operation == "desfocar":
            image_base64 = convert_image_to_base64(image_path)
            server_proxy.desfoc(image_base64)
            

def on_button_hover(event):
    event.widget.config(bg="gray")
    pygame.mixer.Sound("buttonSong.wav").play()
def on_button_leave(event):
    event.widget.config(bg="SystemButtonFace")


root = tk.Tk()
root.title("Cliente de Processamento de Imagem")

window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

image_file_path = tk.StringVar()
result_label = tk.Label(root, text="")
result_label.pack()

file_button = tk.Button(root, text="Escolher Imagem", command=browse_image, width=30)
file_button.pack(pady=3)
file_button.bind("<Enter>", on_button_hover)
file_button.bind("<Leave>", on_button_leave)

process_button_convert = tk.Button(root, text="Converter imagem para cinza", command=lambda: process_image("convert"), width=30)
process_button_convert.pack(pady=3)
process_button_convert.bind("<Enter>", on_button_hover)
process_button_convert.bind("<Leave>", on_button_leave)

process_button_resize = tk.Button(root, text="Redimensionar imagem", command=lambda: process_image("resize"), width=30)
process_button_resize.pack(pady=3)
process_button_resize.bind("<Enter>", on_button_hover)
process_button_resize.bind("<Leave>", on_button_leave)

process_button_rotate = tk.Button(root, text="Rodar imagem", command=lambda: process_image("rotate"), width=30)
process_button_rotate.pack(pady=3)
process_button_rotate.bind("<Enter>", on_button_hover)
process_button_rotate.bind("<Leave>", on_button_leave)

process_button_rotate = tk.Button(root, text="Desfocar", command=lambda: process_image("desfocar"), width=30)
process_button_rotate.pack(pady=3)
process_button_rotate.bind("<Enter>", on_button_hover)
process_button_rotate.bind("<Leave>", on_button_leave)


image_label = tk.Label(root)
image_label.pack()

root.mainloop()
