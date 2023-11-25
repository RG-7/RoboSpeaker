#   Project Speaking Robo 
import os

if __name__ == '__main__':
    print("\n\t\tWelcome to RoboSpeaker 1.1\t\t")
    print("\t\t\t:- Created by RG-7")
    print()
    while True:
        user_input = input("Enter what do you want me to speak : ")
        if user_input.lower() == 'q':
            os.system(f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Thank You for using. See You soon!\');"')
            break

        command = f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{user_input}\');"'
        os.system(command)
print()