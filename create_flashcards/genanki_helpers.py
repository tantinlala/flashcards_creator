import genanki

def create_deck(deck_name):
    deck_id = 2059400110 #uuid.uuid4().int & (1<<64)-1
    return genanki.Deck(deck_id, deck_name)

def create_model():
    model_id = 1607392319 #uuid.uuid4().int & (1<<64)-1

    my_model = genanki.Model(model_id, 'Simple Model', fields=[
    {'name': 'Vocabulary'},
    {'name': 'English'}], templates= [
    {
      'name': 'Flashcard',
      'qfmt': '{{English}}',
      'afmt': '{{English}}<hr id="answer">{{Vocabulary}}',
    }])
    return my_model

def create_note(model, fields):
    return genanki.Note(model=model, fields=fields)

def add_note_to_deck(deck, note):
    deck.add_note(note)

def generate_anki_file(deck, file_name):
    genanki.Package(deck).write_to_file(file_name)
