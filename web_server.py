import socket as soc    

# Configuração do socket do servidor
server_port = 3570
server_addr = ("127.0.0.1", server_port)

# Cria o socket do servidor
# AF_INET indica que estamos usando IPv4
# SOCK_STREAM indica que estamos usando TCP
server_socket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
server_socket.bind(server_addr)

# O socket está ouvindo apenas 1 conexão por vez.
server_socket.listen(1)

while True:
    print("Esperando uma requisição na porta %d..." %server_port)

    # Cria o socket da conexão e o endereço do cliente.
    conn_socket, client_addr = server_socket.accept()

    data_received = conn_socket.recv(4096)
    print("Recebido de %s: %s" %(client_addr[0], data_received))

    # Decodifica a mensagem recebida e pega o nome do arquivo requisitado no cabeçalho da requisição.
    file_requested = data_received.split()[1].decode()
    # Retira o '/' do começo do nome do arquivo.
    file_requested = file_requested[1:]

    # Se nenhum arquivo for solicitado, retorna o index.html
    if file_requested == "":
        file_requested = "index.html"

    response_headers = ""
    response_body = ""

    try:
        with open(file_requested, "r") as file:
            response_body = file.read()
        
        response_headers += "HTTP/1.1 200 OK\r\n"
    except IOError:
        response_headers += "HTTP/1.1 404 Not Found\r\n"
        response_body = "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n"

    # Codifica o conteúdo do arquivo em bytes para poder enviar.
    response_body = response_body.encode("utf-8")

    # Prepara os cabeçalhos da resposta.
    response_headers += "Content-Type: text/html; charset=utf-8\r\n"
    response_headers += "Content-Length: " + str(len(response_body)) + "\r\n\r\n"
    response_headers = response_headers.encode()

    # Envia a resposta para o cliente.
    conn_socket.send(response_headers)
    conn_socket.send(response_body)

    conn_socket.close()

server_socket.close()