import xmlrpc.client
import base64
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def browse_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image_file_path.set(file_path)
        show_selected_image(file_path)  # Exibe a imagem selecionada

def show_selected_image(image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Atualiza o widget de imagem
    image_label.config(image=photo)
    image_label.image = photo

def convert_to_grayscale(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    return grayscale_image

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height))
    return resized_image

def rotate_image(image_path, angle):
    image = Image.open(image_path)
    rotated_image = image.rotate(angle)
    return rotated_image

def process_image(operation):
    image_path = image_file_path.get()
    if not image_path:
        result_label.config(text="Selecione uma imagem primeiro")
        return

    if operation == "convert":
        grayscale_image = convert_to_grayscale(image_path)
        grayscale_image.save('grayscale_image.jpg', format="JPEG")
    if operation == "resize":
        resized_image = resize_image(image_path, 300, 200)
        resized_image.save('resized_image.jpg', format="JPEG")
    if operation == "rotate":
        rotated_image = rotate_image(image_path, 45)
        rotated_image.save('rotated_image.jpg', format="JPEG")

    result_label.config(text="Imagens processadas e salvas com sucesso!")


root = tk.Tk()
root.title("Cliente de Processamento de Imagem")

image_file_path = tk.StringVar()
result_label = tk.Label(root, text="")
result_label.pack()

file_button = tk.Button(root, text="Escolher Imagem", command=browse_image)
file_button.pack()

process_button = tk.Button(root, text="Converter imagem para cinza", command=lambda: process_image("convert"))
process_button.pack()

process_button = tk.Button(root, text="Redimensionar imagem", command=lambda: process_image("resize"))
process_button.pack()

process_button = tk.Button(root, text="Rodar imagem", command=lambda: process_image("rotate"))
process_button.pack()


# Adicione um widget de label para exibir a imagem selecionada
image_label = tk.Label(root)
image_label.pack()

root.mainloop()

