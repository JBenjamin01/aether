import speech_recognition as sr
import pyttsx3

# Función para escuchar y reconocer el comando de voz
def listen_to_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="es-ES")
            print("Escuché:", command)
            return command
        except sr.UnknownValueError:
            print("No entendí el audio.")
        except sr.RequestError:
            print("Error con el servicio de reconocimiento.")
        return ""

# Función para convertir texto a voz
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Función principal
def main():
    while True:
        command = listen_to_audio()
        if "salir" in command.lower():
            speak_text("Adiós.")
            break
        elif command:
            speak_text(f"Escuché: {command}")

if __name__ == "__main__":
    main()