from pydantic import BaseModel

class Flashcard(BaseModel):
    foreign_vocabulary: str
    english_translation: str

class ThaiFlashcardConverter:
    def __init__(self, conversation):
        self.conversation_ = conversation

    def convert_to_flashcards(self, input_path: str):
        with open(input_path, 'rb') as f:
            file_content = f.read()

        if input_path.lower().endswith('.jpg'):
            self.conversation_.add_image(file_content)
        elif input_path.lower().endswith('.jpeg'):
            self.conversation_.add_image(file_content)
        elif input_path.lower().endswith('.txt'):
            self.conversation_.add_text(file_content.decode('utf-8'))

        self.conversation_.add_text(
            "Convert the provided content into a list of flashcards for learning Thai vocabulary. "
            "Each flashcard should contain a 'foreign_vocabulary' in Thai and its corresponding 'english_translation'. "
            "Return the flashcards in JSON format as a list of objects with 'foreign_vocabulary' and 'english_translation' fields."
        )

        flashcards = self.conversation_.get_structured_output(list[Flashcard])

        return flashcards