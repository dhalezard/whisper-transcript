import whisper

model = whisper.load_model('medium')
result = model.transcribe('teo-interview.mp3', language='Spanish', verbose=True, word_timestamps=True)

# pa  ver

with open('transcription.txt', 'w', encoding='utf-8') as f:
    f.write(result['text'])