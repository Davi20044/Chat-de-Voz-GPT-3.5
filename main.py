import openai
from gtts import gTTS
import os
import pygame
import tempfile
from io import BytesIO
import speech_recognition as sr

# Inicializa o mixer do pygame para reprodução de áudio
pygame.mixer.init()

# Define sua chave de API
openai.api_key = 'Chave_API_Openai'

# Função para reconhecimento de fala (speech-to-text)
def ouvir_microfone():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        reconhecedor.adjust_for_ambient_noise(source)
        audio = reconhecedor.listen(source)
    try:
        texto = reconhecedor.recognize_google(audio, language="pt-BR")
        print("Você disse: " + texto)
        return texto
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        return ""
    except sr.RequestError as e:
        print("Erro ao acessar o serviço de reconhecimento de fala; {0}".format(e))
        return ""

# Função para interagir com o modelo GPT e converter a resposta em voz
def conversa_com_gpt(prompt, temperatura=0.7, max_tokens=50):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": "Você: " + prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=temperatura,
        max_tokens=max_tokens
    )
    resposta_texto = resposta.choices[0].message['content']

    # Converter resposta em voz
    tts = gTTS(text=resposta_texto, lang='pt')
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)

    # Reproduzir áudio usando pygame
    pygame.mixer.music.load(audio_bytes)
    pygame.mixer.music.play()

    return resposta_texto

# Função para interação contínua com o usuário
def main():
    print("Bem-vindo! Fale 'Chat' para iniciar a conversa com o GPT.")
    print("Digite ou Fale 'Tchau' para encerrar a conversa.")

    while True:
        # Reconhece o que foi dito pelo usuário
        entrada = ouvir_microfone()

        if "chat" in entrada.lower():
            print("Iniciando conversa com o GPT...")
            conversa_gpt()
        elif entrada.lower() == 'sair':
            print("Até logo!")
            break

# Função para iniciar a conversa com o GPT
def conversa_gpt():
    while True:
        entrada = ouvir_microfone()
        if entrada.lower() == 'tchau':
            print("Encerrando conversa com o GPT.")
            break

        # Conversa com o GPT usando o texto reconhecido
        resposta = conversa_com_gpt(entrada)
        print("GPT: " + resposta)

# Executa o programa
if __name__ == "__main__":
    main()
