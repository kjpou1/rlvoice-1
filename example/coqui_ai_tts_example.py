import rlvoice

engine = rlvoice.init("coqui_ai_tts")
engine.say("this is an english text to voice test.")
engine.runAndWait()

# cloning someone's voice:

engine = rlvoice.init("coqui_ai_tts")
engine.setProperty("speaker_wav", "./someones_voice.wav")
engine.say("this is an english text to voice test.")
engine.runAndWait()
