from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from PIL import Image
from io import BytesIO
import base64

# Classe que controla o acesso ao servidor
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Crie o servidor RPC
with SimpleXMLRPCServer(('localhost', 8001), requestHandler=RequestHandler) as server:

    def convert_to_grayscale(encoded_image):
        decoded_image = base64.b64decode(encoded_image)
        image = Image.open(BytesIO(decoded_image))
        grayscale_image = image.convert('L')
        buffered = BytesIO()
        grayscale_image.save(buffered, format="JPEG")
        encoded_grayscale_image = base64.b64encode(buffered.getvalue())
        return encoded_grayscale_image

    def resize_image(encoded_image, width, height):
        decoded_image = base64.b64decode(encoded_image)
        image = Image.open(BytesIO(decoded_image))
        resized_image = image.resize((width, height))
        buffered = BytesIO()
        resized_image.save(buffered, format="JPEG")
        encoded_resized_image = base64.b64encode(buffered.getvalue())
        return encoded_resized_image

    def rotate_image(encoded_image, angle):
        decoded_image = base64.b64decode(encoded_image)
        image = Image.open(BytesIO(decoded_image))
        rotated_image = image.rotate(angle)
        buffered = BytesIO()
        rotated_image.save(buffered, format="JPEG")
        encoded_rotated_image = base64.b64encode(buffered.getvalue())
        return encoded_rotated_image

    server.register_function(convert_to_grayscale)
    server.register_function(resize_image)
    server.register_function(rotate_image)

    print("Servidor RPC em execução...")
    server.serve_forever()
