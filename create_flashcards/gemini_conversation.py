from google import genai
from google.genai import types
from dotenv import load_dotenv

class GeminiConversation:
    MODEL_NAME = "gemini-2.5-flash"

    def __init__(self):
        load_dotenv()
        self.client_ = genai.Client()
        self.message_list_ = []

    def clear_messages(self):
        self.message_list_ = []

    def add_jpg(self, image_bytes):
        image_message = types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/jpeg",
        )
        self.message_list_.append(image_message)

    def add_png(self, image_bytes):
        image_message = types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/png",
        )
        self.message_list_.append(image_message)

    def add_text(self, text):
        self.message_list_.append(text)
    
    def add_file(self, input_path):
        with open(input_path, 'rb') as f:
            file_content = f.read()

        if input_path.lower().endswith('.jpg'):
            self.add_jpg(file_content)
        elif input_path.lower().endswith('.jpeg'):
            self.add_jpg(file_content)
        elif input_path.lower().endswith('.png'):
            self.add_png(file_content)
        elif input_path.lower().endswith('.txt'):
            self.add_text(file_content.decode('utf-8'))

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