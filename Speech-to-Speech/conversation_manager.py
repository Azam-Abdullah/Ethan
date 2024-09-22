import asyncio
import language_model_processor, text_to_speech, transcription

class ConversationManager:
    def __init__(self):
        self.transcription_response = ""
        self.llm = language_model_processor.LanguageModelProcessor()

    async def main(self):
        def handle_full_sentence(full_sentence):
            self.transcription_response = full_sentence

        # Loop indefinitely until "goodbye" is detected
        while True:
            await transcription.get_transcript(handle_full_sentence)
            
            # Check for "goodbye" to exit the loop
            if "goodbye" in self.transcription_response.lower():
                break
            
            llm_response = self.llm.process(self.transcription_response)
            tts = text_to_speech.TextToSpeech()
            tts.speak(llm_response)

            # Reset transcription_response for the next loop iteration
            self.transcription_response = ""
