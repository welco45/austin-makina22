import socket
import threading


# Server function
def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the server to a host and port
    host = 'localhost'
    port = 12345
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server is listening on {host}:{port}...")

        # Accept a connection from the client
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Send a message to the client
        message = "Hello from server!"
        client_socket.send(message.encode())

        # Close the client connection
        client_socket.close()
    except socket.error as e:
        print(f"Error in server: {e}")
    finally:
        # Ensure the server socket is closed properly
        server_socket.close()


# Client function
def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    host = 'localhost'
    port = 12345
    try:
        client_socket.connect((host, port))

        # Receive a message from the server
        message = client_socket.recv(1024).decode()
        print("Received message:", message)
    except socket.error as e:
        print(f"Error in client: {e}")
    finally:
        # Close the connection
        client_socket.close()


# Run the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Run the client
start_client()

# Wait for the server to finish
server_thread.join()

