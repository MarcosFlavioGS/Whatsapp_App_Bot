Esse é um Bot local feito com pyautogui para automação de envio de mensagens via Whatsapp, assim como um envio secundário para emails.
Fiz Esse bot de modo que seja feita a leitura de arquivos de texto com as informaçções de contato; o caminho para um arquivo de imagem no computador; e uma mensagem.
O bot procura pela lista o contato a ser buscado, verificando primeiro se o contato se trata de um número de telefone, ou seja, um contato não cadastrado ainda na conta do usuário, procedendo, nesse caso, para a busca online do contato, para então continuar o processo de envio de mensagem normalmente. O bot também conta com um envio de email em segundo plano para contatos de email cadastrados na lista(ver abaixo como identificar o contato para o bot)
O programa também possui uma checagem de exceções para que não pare de funcionar por causa de um erro, fornecendo no console o contato onde houve o travamento para que o
usuário possa verificar, posteriormente, algum possível erro de digitação.

Esse Bot ainda está em processo de aprimoramento e será atualizado no futuro.

-- Utilização dos arquivos .txt de consulta:

    - contatos.txt:
        -Aqui deve-se colocar por escrito os contatos um por linha, identificando o tipo de contato com as "tags" apropriadas: 
            - Contatos já cadastrados nos contatos de whatsapp do usuário devem ser escritos EXATAMENTE como estão escritos na sua lista de contatos no whatsapp, porém, sem a acentuação.

            - Contatos não cadastrados em sua lista de contatos do whatsapp poderam ser passados apenas com seus números de celular, basta que seja passado na frente do contato o número '55' seguidos pelo restante do número: 55XXXXXXXXXXX.

            -   Contatos cuja única informação para contato seja um email também poderão ser acessados, basta escrever o email antecedido por um '@', ficando dessa forma: @esteeumexemplo@gmail.com. 
             * É importante ficar claro que o email DESTINATÁRIO poderá ser de qualquer servidor de email sem nenhuma restrição, porém, o usuário deste programa só poderá enviar emails a partir de um @GMAIL.*
             *IMPORTANTE: Para que o envio de email possa ser feito, é necessário configurar sua conta google para tal. Para isso, entre nas configurações da sua conta google, na aba de segurança, e ative a opção de acesse à aplicativos menos seguros. Note que, como é uma configuração de segurança, é importante não deixar essa opção ativada por indefinidamente, então procure, sempre que possível deixar desativado, ativando somente quando for utilizar o envio de email automatizado.
    - filepath.txt:
        -Aqui será especificado o caminho em sua maquina onde se encontra a imagem a ser enviada pelo whatsapp, ex: "C://User/images/minhaFoto.jpg"

    - mensagem.txt:
        Escreva aqui a mensagem a ser enviada para seus contatos. Note que existe também o arquivo "mensagem_email.txt" aqui é onde será colocada a mensagem para envio no email

-- Envio de email:
    - Para o envio de email serão utilizados 4 arquivos de consulta .txt. O arquivo email.txt será utilizado para informar o email(@gmail) do usuário; O arquivo mensagem_email.txt, que já foi referido anteriormente, será utilizado para informar a mensagem que será enviada no corpo do email; O arquivo titulo_email.txt será utilizado para informar um cabeçalho para a mensagem de email; E por fim, no arquivo senha_email.txt deverá ser informada a senha para acesso ao email(formas mais seguras de criptografia serão implementadas no futuro)