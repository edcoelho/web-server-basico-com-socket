# Web Server básico com socket

Um servidor web extremamente básico feito com Python para a disciplina de Redes de Computadores I (CK0249) da UFC.

## Iniciando o servidor

Execute o programa passando o número da porta do socket como argumento (opcional). Segue um exemplo:

```bash
python3 web_server.py 4321
```

## Acessando o servidor

Para testar o servidor, acesse o localhost no teu navegador com a porta selecionada. Exemplo: se a porta selecionada for 4321, então acesse http://127.0.0.1:4321 no teu navegador.

É possível acessar os arquivos que estão no mesmo diretório que o servidor. Por exemplo, para acessar o arquivo teste.html, acesse http://127.0.0.1:4321/teste.html. O servidor acessará o index.html por padrão.

## Encerrando o servidor

Para encerrar o servidor, basta pressionar Ctrl+C no terminal.