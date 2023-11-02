from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from PIL import Image, ImageFilter
from io import BytesIO
import base64

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

output_folder = "Desafio_RPC-main"

with SimpleXMLRPCServer(('0.0.0.0', 8003), requestHandler=RequestHandler) as server:

    def resize(encoded_image, width, height):
        decoded_image = base64.b64decode(encoded_image)
        image = Image.open(BytesIO(decoded_image))
        decoded_image = base64.b64decode(encoded_image)
        image = Image.open(BytesIO(decoded_image))
        resized_image = image.resize((width, height))
        buffered = BytesIO()
        resized_image.save(buffered, format="PNG")
        encoded_resized_image = base64.b64encode(buffered.getvalue())

        output_filename = "resized_image.png"

        with open(output_filename, "wb") as output_file:
            output_file.write(buffered.getvalue())

        return encoded_resized_image, output_filename

    def desfoc(encoded_image):
        decoded_image = base64.b64decode(encoded_image)
        image = Image.open(BytesIO(decoded_image))

        image = image.convert("RGB")

        blurred_image = image.filter(ImageFilter.GaussianBlur(5))
        buffered = BytesIO()
        blurred_image.save(buffered, format="PNG")
        encoded_blurred_image = base64.b64encode(buffered.getvalue())

        output_filename = "desfoc_image.png"
        with open(output_filename, "wb") as output_file:
            output_file.write(buffered.getvalue())
        return encoded_blurred_image, output_filename
    def convert_to_grayscale(encoded_image):
        decoded_image = base64.b64decode(encoded_image)
        image = Image.open(BytesIO(decoded_image))
        
        grayscale_image = image.convert('L')
        buffered = BytesIO()
        grayscale_image.save(buffered, format="PNG")
        encoded_grayscale_image = base64.b64encode(buffered.getvalue())

        output_filename = "grayscale_image.png"
        with open(output_filename, "wb") as output_file:
            output_file.write(buffered.getvalue())
        return encoded_grayscale_image, output_filename
        

    def rotate_image(encoded_image, angle):
        decoded_image = base64.b64decode(encoded_image)
        image = Image.open(BytesIO(decoded_image))
        decoded_image = base64.b64decode(encoded_image)
        image = Image.open(BytesIO(decoded_image))
        rotated_image = image.rotate(angle)
        buffered = BytesIO()
        rotated_image.save(buffered, format="PNG")
        encoded_rotated_image = base64.b64encode(buffered.getvalue())

        output_filename = "rotate_image.png"
        with open(output_filename, "wb") as output_file:
            output_file.write(buffered.getvalue())
        return encoded_rotated_image, output_filename

    server.register_function(convert_to_grayscale)
    server.register_function(resize)
    server.register_function(rotate_image)
    server.register_function(desfoc)

    print("Servidor RPC em execução...")
    server.serve_forever()
