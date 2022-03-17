Esse é um Bot local feito com pyautogui para automação de envio de mensagens via Whatsapp.
Fiz Esse bot de modo que seja feita a leitura de arquivos de texto com as informaçções de contato; o caminho para um arquivo de imagem no computador; e uma mensagem.
O bot procura pela lista o contato a ser buscado, verificando primeiro se o contato se trata de um número de telefone, ou seja, um contato não cadastrado ainda na conta
do usuário, procedendo, nesse caso, para a busca online do contato, para então continuar o processo de envio de mensagem normalmente.
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
    - filepath.txt:
        -Aqui será especificado o caminho em sua maquina onde se encontra a imagem a ser enviada pelo whatsapp.

    - mensagem.txt:
        Escreva aqui a mensagem a ser enviada para seus contatos.    