DEEPL_AUTH_KEY = "a6da2cc8-76a5-40e4-8a2c-fe08b7aa288c:fx"

def read_german_protocol():
    pass

def chunk_text():
    pass

def translate_chunk():
    pass

def create_english_protocol():
    pass

def write_document():
    pass

def translate_agenda(agenda): #Written by Tim
    tops = agenda.split("><li>")[1:]

    for (i, top) in enumerate(tops):
        tops[i] = top[:top.find("<")]

    payload = {
        "text" : tops,
        "target_lang" : "EN-US"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"DeepL-Auth-Key {DEEPL_AUTH_KEY}"
    }

    response = requests.post(
        DEEPL_URL,
        json = payload,
        headers = headers
    )

    agenda_english = agenda

    for (i, top) in enumerate(tops):
        agenda_english = agenda_english.replace(top, response.json()["translations"][i]["text"])

    return agenda_english

