import os

print("Welcome to RoboSpeaker 1.1")

while True:
    x = input("Enter what you want me to speak: ")

    if x.lower() == "q":
        os.system('powershell -Command "Add-Type -AssemblyName System.Speech; '
                  '(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'bye bye\')"')
        break

    os.system(f'powershell -Command "Add-Type -AssemblyName System.Speech; '
              f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"')