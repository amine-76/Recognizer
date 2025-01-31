import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia

# Initialisation du moteur de voix
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Vitesse de la voix
engine.setProperty("volume", 1.0)  # Volume à 100%

# Fonction pour faire parler l'assistant
def parler(texte):
    engine.say(texte)
    engine.runAndWait()

# Fonction pour écouter la voix de l'utilisateur
def ecouter():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Dites quelque chose...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        texte = recognizer.recognize_google(audio, language="fr-FR")  # Détection en français
        print("Vous avez dit :", texte)
        return texte.lower()
    except sr.UnknownValueError:
        print("Je n'ai pas compris...")
        return ""
    except sr.RequestError:
        print("Problème avec l'API de reconnaissance vocale.")
        return ""

# Fonction principale de l'assistant
def assistant():
    parler("Bonjour ! Comment puis-je vous aider ?")
    
    while True:
        commande = ecouter()

        if "heure" in commande:
            heure = datetime.datetime.now().strftime("%H:%M")
            parler(f"Il est {heure}")
        
        elif "wikipedia" in commande:
            parler("Que voulez-vous chercher sur Wikipedia ?")
            sujet = ecouter()
            if sujet:
                try:
                    result = wikipedia.summary(sujet, sentences=2, auto_suggest=False)
                    parler("Voici ce que j'ai trouvé :")
                    parler(result)
                except wikipedia.exceptions.PageError:
                    parler("Désolé, je n'ai pas trouvé d'information sur ce sujet.")
        
        elif "ouvre google" in commande:
            parler("J'ouvre Google")
            webbrowser.open("https://www.google.com")
        
        elif "stop" in commande or "au revoir" in commande:
            parler("D'accord, à bientôt !")
            break
        
        else:
            parler("Je ne comprends pas cette commande.")

# Lancer l'assistant
assistant()
