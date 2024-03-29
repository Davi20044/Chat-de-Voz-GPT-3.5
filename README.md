# Chat de Voz (GPT(

Este projeto consiste em um assistente de conversação que utiliza a tecnologia de Processamento de Linguagem Natural (PLN) e Reconhecimento de Fala para interagir com os usuários.



# Funcionalidades:

- Reconhecimento de Fala (Speech-to-Text): O programa é capaz de ouvir o usuário por meio do microfone e converter a fala em texto. Isso é realizado utilizando a biblioteca speech_recognition, permitindo ao usuário iniciar e interromper a conversa por voz.

- Interação com o Modelo GPT-3.5: O programa utiliza a API da OpenAI para interagir com o modelo GPT-3.5, permitindo uma conversação natural com os usuários. O modelo é alimentado com o texto reconhecido para gerar respostas coerentes.

- Conversão de Texto em Voz: As respostas geradas pelo modelo GPT são convertidas em voz utilizando a biblioteca gTTS. Isso permite que o assistente responda ao usuário tanto por texto quanto por áudio.

- Reprodução de Áudio: A reprodução do áudio é realizada através da biblioteca pygame, que possibilita a reprodução de arquivos de áudio em diversos formatos.


  
# Tecnologias e Bibliotecas:

- OpenAI API: Utilizada para acessar o modelo GPT-3.5 e obter respostas para as consultas dos usuários.

- SpeechRecognition: Biblioteca utilizada para reconhecimento de fala, permitindo que o programa capture e interprete o que o usuário diz.

- gTTS (Google Text-to-Speech): Utilizada para converter texto em voz. Essa biblioteca permite gerar arquivos de áudio a partir do texto fornecido.

- Pygame: Biblioteca utilizada para a reprodução de áudio. Com ela, é possível carregar e reproduzir arquivos de áudio de forma simples e eficiente.

# Fluxo do Programa:

- O usuário inicia o programa e pode optar por interagir com o assistente de conversação.
- Ao iniciar a interação, o usuário pode falar com o assistente, que irá reconhecer a fala e enviar para o modelo GPT-3.5.
- O modelo GPT-3.5 processa a entrada do usuário e gera uma resposta, que é convertida em voz e reproduzida para o usuário.
- O usuário pode continuar interagindo com o assistente até decidir encerrar a conversa.


![image](https://github.com/Davi20044/Chat-de-Voz-GPT-/assets/122330494/c8eabc92-124c-457e-8ac1-bddd37abb96b)
