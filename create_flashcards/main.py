from . import genanki_helpers
from .gemini_conversation import GeminiConversation
from .thai_flashcard_converter import ThaiFlashcardConverter
import argparse

def main():

    # Parse arguments
    parser = argparse.ArgumentParser(description='Create Anki flashcards using generative AI')

    # Get the provided text files (one or more)
    parser.add_argument('files', nargs='+', type=str, help='The files to convert to flashcards')
    # Required output filename for the generated .apkg
    parser.add_argument('-o', '--output', dest='output', required=True, type=str,
                        help='Output .apkg filename (required)')

    # Parse arguments
    args = parser.parse_args()

    gemini_conversation = GeminiConversation()
    flashcard_converter = ThaiFlashcardConverter(gemini_conversation)

    # Create a new deck with new mandarin flashcards
    deck = genanki_helpers.create_deck("New flashcards")
    model = genanki_helpers.create_model()

    # Process each provided file and add its flashcards to the deck
    for input_path in args.files:
        flashcards = flashcard_converter.convert_to_flashcards(input_path)

        # Loop through all flashcards in json and create a note for each one
        for flashcard in flashcards:
            print(flashcard)
            note = genanki_helpers.create_note(model, [flashcard.foreign_vocabulary, flashcard.english_translation])
            genanki_helpers.add_note_to_deck(deck, note)

    # Use the required output filename and ensure it ends with .apkg
    apkg_file_name = args.output
    if not apkg_file_name.lower().endswith('.apkg'):
        apkg_file_name += '.apkg'

    genanki_helpers.generate_anki_file(deck, apkg_file_name)

if __name__ == "__main__":
    main()