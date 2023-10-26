import xmlrpc.client
import base64
import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk

def browse_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image_file_path.set(file_path)
        show_selected_image(file_path)

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
        result_label.config(text="Imagem em tons de cinza salva com sucesso!")
    elif operation == "resize":
        # Solicitar largura e altura ao usuário
        width = simpledialog.askinteger("Redimensionar imagem", "Insira a largura desejada:")
        height = simpledialog.askinteger("Redimensionar imagem", "Insira a altura desejada:")

        if width is not None and height is not None:
            resized_image = resize_image(image_path, width, height)
            resized_image.save('resized_image.jpg', format="JPEG")
            result_label.config(text="Imagem redimensionada e salva com sucesso!")
        else:
            result_label.config(text="Largura e altura inválidas.")
    elif operation == "rotate":
        # Solicitar o ângulo de rotação ao usuário
        angle = simpledialog.askinteger("Rodar imagem", "Insira o ângulo de rotação desejado (em graus):")

        if angle is not None:
            rotated_image = rotate_image(image_path, angle)
            rotated_image.save('rotated_image.jpg', format="JPEG")
            result_label.config(text="Imagem rotacionada e salva com sucesso!")
        else:
            result_label.config(text="Ângulo de rotação inválido.")

root = tk.Tk()
root.title("Cliente de Processamento de Imagem")

image_file_path = tk.StringVar()
result_label = tk.Label(root, text="")
result_label.pack()

file_button = tk.Button(root, text="Escolher Imagem", command=browse_image)
file_button.pack()

process_button_convert = tk.Button(root, text="Converter imagem para cinza", command=lambda: process_image("convert"))
process_button_convert.pack()

process_button_resize = tk.Button(root, text="Redimensionar imagem", command=lambda: process_image("resize"))
process_button_resize.pack()

process_button_rotate = tk.Button(root, text="Rodar imagem", command=lambda: process_image("rotate"))
process_button_rotate.pack()

# Adicione um widget de label para exibir a imagem selecionada
image_label = tk.Label(root)
image_label.pack()

root.mainloop()
