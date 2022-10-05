import socket
import threading

#Clase Server sacada del contenido semana 12-13 2019
class Server:
    def __init__(self, port, host):
        print("Inicializando servidor...")

        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_and_listen()
        self.accept_connections()

    def bind_and_listen(self):
        """
        Enlaza el socket creado con el host y puerto indicado.

        Primero, se enlaza el socket y luego queda esperando
        por conexiones entrantes.
        """
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}...")

    def accept_connections(self):
        """
        Inicia el thread que aceptará clientes.

        Aunque podríamos aceptar clientes en el thread principal de la
        instancia, es útil hacerlo en un thread aparte. Esto nos
        permitirá realizar la lógica en la parte del servidor sin dejar
        de aceptar clientes. Por ejemplo, seguir procesando archivos.
        """
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self):
        """
        Es arrancado como thread para aceptar clientes.

        Cada vez que aceptamos un nuevo cliente, iniciamos un
        thread nuevo encargado de manejar el socket para ese cliente.
        """
        print("Servidor aceptando conexiones...")

        while True:
            client_socket, _ = self.socket_server.accept()
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket, ),
                daemon=True)
            listening_client_thread.start()

    def handle_command(self, value, sock):
        return value

    @staticmethod
    def send(value, sock):
        """
        Envía mensajes hacia algún socket cliente.

        Debemos implementar en este método el protocolo de comunicación
        donde los primeros 4 bytes indicarán el largo del mensaje.
        """
        stringified_value = str(value)
        msg_bytes = stringified_value.encode()
        msg_length = len(msg_bytes).to_bytes(4, byteorder='big')
        sock.send(msg_length + msg_bytes)

    def listen_client_thread(self, client_socket):
        """
        Es ejecutado como thread que escuchará a un cliente en particular.

        Implementa las funcionalidades del protocolo de comunicación
        que permiten recuperar la informacion enviada.
        """
        print("Servidor conectado a un nuevo cliente...")

        while True:
            response_bytes_length = client_socket.recv(4)
            response_length = int.from_bytes(
                response_bytes_length, byteorder='big')
            response = bytearray()

            while len(response) < response_length:
                read_length = min(4096, response_length - len(response))
                response.extend(client_socket.recv(read_length))

            received = response.decode()

            if received != "":
                # El método `self.handle_command()` debe ser definido.
                # Este realizará toda la lógica asociado a los mensajes
                # que llegan al servidor desde un cliente en particular.
                # Se espera que retorne la respuesta que el servidor
                # debe enviar hacia el cliente.
                response = self.handle_command(received, client_socket)
                self.send(response, client_socket)


if __name__ == "__main__":
    port = 8080
    host = '127.0.0.1'

    server = Server(port, host)