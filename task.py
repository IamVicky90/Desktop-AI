import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os, os.path
import smtplib
import random
try:
    
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    print(voices[0].id)
    engine.setProperty('voice',voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    def chrome_webbrowser(chrome_path, url):
        webbrowser.get(chrome_path).open(url)

    def wishme():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak('Good Morning Vicky')
        elif hour>=12 and hour>=17:
            speak('Good Afternoon Vicky')
        else:
            speak('Good Evening')
        print('Hellow I am Computer, How can I help you!')
        speak('Hellow I am Computer, How can I help you!')
    def takecommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening....')
            r.pause_threshold=1
            
            audio=r.listen(source,timeout=1,phrase_time_limit=3)
        try:
            print('Recognizing....')
            querry=r.recognize_google(audio,language='en-in')
            print(f'You said {querry}')
        except Exception:
            print('Say That Again Please!')
            return 'None'
        return querry


    if __name__ == "__main__":
        chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path)
        while True:
            querry=takecommand().lower()
            # Strt
            if "poweroff computer" in querry:
                speak("Computer has been closed")
                os.system("shutdown /s /t 1")
            elif "power off computer" in querry:
                speak("Computer has been closed")
                os.system("shutdown /s /t 1")
            elif "power of computer" in querry:
                speak("Computer has been closed")
                os.system("shutdown /s /t 1")
            elif "shutdown computer" in querry or "shut down computer" in querry:
                speak("Computer has been closed")
                os.system("shutdown /s /t 1")
            elif "computer shutdown" in querry or "computer shut down" in querry:
                speak("Computer has been closed")
                os.system("shutdown /s /t 1")
            elif "quit computer" in querry:
                speak("Computer has been power off")
                os.system("shutdown /s /t 1")
            elif "restartcomputer" in querry:
                speak("We restarting your PC")
                os.system("shutdown /r /t 1")
            elif "restart computer" in querry:
                speak("We restarting your PC")
                os.system("shutdown /r /t 1")
            elif "rstart computer" in querry:
                speak("We restarting your PC")
                os.system("shutdown /r /t 1")
            elif "restart computer" in querry:
                speak("We restarting your PC")
                os.system("shutdown /r /t 1")
            elif "hybrid" in querry or "hybernate" in querry or "hybernation" in querry or "hibernation" in querry:
                speak("We set your PC to sleeping mode")
                os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")
            elif "sleep" in querry or "sleap" in querry:
                speak("We set your PC to sleeping mode")
                os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")
            elif "vscode" in querry or "vs code" in querry:
                speak("Vs code open to you Vicky")

                os.system("code .")

                
            # end
            if "commands" in querry or "command" in querry:
                i=0
                while True:
                    if i==0:
                        i=1
                        wishme()
                    querry=takecommand().lower()
                    if 'wikipedia' in querry:
                        speak('Searching wikipedia...')
                        querry=querry.replace('wikipedia','')
                        querry=querry.replace('please','')
                        
                        results=wikipedia.summary(querry,sentences=2)
                        speak('According to wikipedia, ')
                        print(results)
                        speak(results)
                    elif "vscode" in querry or "vs code" in querry:
                        speak("Vs code open to you Vicky")
                        os.system("code .")
                    elif 'who are you' in querry:
                        print('I am Computer Sir!')
                        speak('I am Computer Sir!')
                    elif 'made you' in querry:
                        print('I am made by you Sir Waqas powered by Vicky World Production')
                        speak('I am made by you Sir Waqas powered by Vicky World Production')

                    elif "sleep" in querry or "sleap" in querry:
                        speak("We set your PC to sleeping mode")
                        # os.system("Powercfg -H OFF")
                        os.system("rundll32.exe Powercfg -H OFF,SetSuspendState 0,1,0")
                    
                    elif 'open youtube' in querry:
                        url=('youtube.com')
                        chrome_webbrowser(chrome_path,url)
                        # webbrowser.open('youtube.com')
                        speak('Youtube has been opened dear Vicky')
                        
                    elif 'open google' in querry or 'open chrome' in querry:
                        # webbrowser.open('google.com')
                        url=('google.com')
                        chrome_webbrowser(chrome_path,url)
                        speak('Google Has been opened dear Vicky')
                        
                    elif 'stack overflow' in querry:
                        # webbrowser.open('stackoverflow.com')
                        url=('stackoverflow.com')
                        chrome_webbrowser(chrome_path,url)


                    elif 'stackoverflow' in querry:
                        url=('stackoverflow.com')
                        chrome_webbrowser(chrome_path,url)
                    elif 'time' in querry:
                        str=datetime.datetime.now().strftime('%H:%M:%S')
                        print(f"Time is{str}")
                        speak(f"Time is {str}")                    
                    elif 'search' in querry:
                        querry=querry.replace('search','')
                        querry=querry.replace('please','')
                        chrome_webbrowser(chrome_path,querry)
                    elif 'song' in querry or 'songs' in querry:
                        

                        music_dir=r'E:\D\New folder (2)'
                        songs=os.listdir(music_dir)
                        print(songs)
                        files_len= len([name for name in os.listdir('.') if os.path.isfile(name)])
                        print(files_len)
                        r= random.randint(0, files_len-1)
                        print(songs[r])
                        os.startfile(os.path.join(music_dir,songs[r]))

                    elif 'stop' in querry:
                        print('Commands has been stopped Thank You Sir!')
                        speak('Commands has been stopped Thank You Sir!')
                        break

                    elif 'quit' in querry or 'exit' in querry:
                        print('Commands has been stopped. Thank You Sir!')
                        speak('Commands has been stopped. Thank You Sir!')
                        break
                    elif "shutdown computer" in querry or "shut down computer" in querry:
                        speak("Computer has been closed")
                        os.system("shutdown /s /t 1")
                    elif "computer shutdown" in querry or "computer shut down" in querry:
                        speak("Computer has been closed")
                        os.system("shutdown /s /t 1")                   
                    
                    elif "poweroff computer" in querry:
                        speak("Computer has been closed")
                        os.system("shutdown /s /t 1")
                    elif "power off computer" in querry:
                        speak("Computer has been closed")
                        os.system("shutdown /s /t 1")
                    elif "power of computer" in querry:
                        speak("Computer has been closed")
                        os.system("shutdown /s /t 1")
                    elif "quit Computer" in querry:
                        speak("Computer has been power off")
                        os.system("shutdown /s /t 1")
                    elif "restartcomputer" in querry:
                        speak("We restarting your PC")
                        os.system("shutdown /r /t 1")
                    elif "restart computer" in querry:
                        speak("We restarting your PC")
                        os.system("shutdown /r /t 1")
                    elif "rstart computer" in querry:
                        speak("We restarting your PC")
                        os.system("shutdown /r /t 1")
                    elif "restart Computer" in querry:
                        speak("We restarting your PC")
                        os.system("shutdown /r /t 1")
except Exception as e:
    speak('An unknown Error has been occured Check Your Connection Please')