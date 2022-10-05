import socket
import json
import pickle


class Cliente:

    def __init__(self):
        '''Inicializador de cliente.

        Crea su socket, e intente conectarse a servidor.
        '''
        # --------------------
        # Completar desde aquí

        self.host = '127.0.0.1'
        self.port = 9999
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Aqui deberas intentar conectar al servidor.

            # Completar hasta aquí
            self.socket_cliente.connect((self.host, self.port))
            # --------------------
            print("Cliente conectado exitosamente al servidor.")
            self.interactuar_con_servidor()
        except ConnectionRefusedError:
            self.cerrar_conexion()

    def interactuar_con_servidor(self):
        '''Comienza ciclo de interacción con servidor.

        Recibe estado y envia accion.
        '''
        while True:
            mensaje, continuar = self.recibir_estado()
            print(mensaje)
            if not continuar:
                break
            accion = self.procesar_comando_input()
            while accion is None:
                print('Input invalido.')
                accion = self.procesar_comando_input()
            self.enviar_accion(accion)
        self.cerrar_conexion()

    def recibir_estado(self):
        '''Recibe actualización de estado desde servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje
        largo_archivo = int.from_bytes(self.socket_cliente.recv(4), byteorder='big')
        datos = bytearray()

        # Ahora leemos el archivo por chunks, de máximo 4096 bytes.
        while len(datos) < largo_archivo:
            # El último recv será probablemente más chico que 4096
            bytes_leer = min(4096, largo_archivo - len(datos))
            bytes_recibidos = self.socket_cliente.recv(bytes_leer)
            datos.extend(bytes_recibidos)
        data = pickle.loads(datos)
        # Debe haber un string para imprimirse
        mensaje = data["mensaje"]
        # Debe haber un boolean para saber si continuar funcionando
        continuar = data["continuar"]

        # Completar hasta aquí
        # --------------------
        return mensaje, continuar

    def procesar_comando_input(self):
        '''Procesa y revisa que el input del usuario sea valido'''
        input_usuario = input('-> ')
        # ---------
        # Completar
        if input_usuario == '\juego_nuevo':
            return '\\juego_nuevo'
        elif input_usuario[0:15] == '\jugada columna' and input_usuario[16:].isnumeric():
            return {'1': '\\jugada', '2': int(input_usuario[16:])}
        elif input_usuario == '\salir':
            return '\\salir'
        return None

        # Completar hasta aquí
        # --------------------

    def enviar_accion(self, accion):
        '''Envia accion asociada a comando ya procesado al servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje
        mensaje_accion = json.dumps(accion)
        mensaje_accion_cod = mensaje_accion.encode('utf-8')
        mss_accion_len = len(mensaje_accion_cod)
        mensaje_con_len_accion = mss_accion_len.to_bytes(4, byteorder='big') + mensaje_accion_cod
        self.socket_cliente.sendall(mensaje_con_len_accion)


        # Completar hasta aquí
        # --------------------

    def cerrar_conexion(self):
        '''Cierra socket de conexión.'''
        self.socket_cliente.close()
        print("Conexión terminada.")


if __name__ == "__main__":
    Cliente()
