import pyttsx3
engine = pyttsx3.init()

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
  
# Use female voice 
engine.setProperty('voice', voice_id)
engine.say("Hello Raghav This is Jarvis")
engine.runAndWait()