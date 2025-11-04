from google import genai
from google.genai import types
from dotenv import load_dotenv

class GeminiConversation:
    MODEL_NAME = "gemini-2.5-flash"

    def __init__(self):
        load_dotenv()
        self.client_ = genai.Client()
        self.message_list_ = []

    def add_image(self, image_bytes):
        image_message = types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/jpeg",
        )
        self.message_list_.append(image_message)

    def add_text(self, text):
        self.message_list_.append(text)

    def get_structured_output(self, output_type):
        response = self.client_.models.generate_content(
            model=self.MODEL_NAME,
            contents=self.message_list_,
            config={
                "response_mime_type": "application/json",
                "response_schema": output_type,
            },
        )

        return response.parsed