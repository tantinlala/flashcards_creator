from pydantic import BaseModel

class Flashcard(BaseModel):
    foreign_vocabulary: str
    english_translation: str

class ThaiFlashcardConverter:
    def __init__(self, conversation):
        self.conversation_ = conversation

    def convert_to_flashcards(self, input_path: str):
        self.conversation_.add_file(input_path)
        self.conversation_.add_text(
            "Convert the provided content into a list of flashcards for learning Thai vocabulary. "
            "Each flashcard should contain a 'foreign_vocabulary' in Thai and its corresponding 'english_translation'. "
            "Return the flashcards in JSON format as a list of objects with 'foreign_vocabulary' and 'english_translation' fields."
            "Don't create flash cards out of the example sentences."
        )

        flashcards = self.conversation_.get_structured_output(list[Flashcard])
        self.conversation_.clear_messages()

        return flashcards