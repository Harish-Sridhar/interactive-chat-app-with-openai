import whisper

model = whisper.load_model("base")
result = model.transcribe("voice.wav")
print(result["text"])