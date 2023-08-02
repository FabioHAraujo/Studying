from google.cloud import translate

def translate_text(text, target_language):
    key = "AIzaSyD2cgdJgplhS45t8NmDMUFjbhfyvUXGfQc"
    client = translate.TranslationServiceClient(credentials=key)
    response = client.translate_text(
        parent="projeto-tradutor-392611",
        contents=[text],
        target_language_code=target_language,
    )

    translated_text = response.translations[0].translated_text
    return translated_text

# Exemplo de uso
text_to_translate = "Hello, how are you?"
target_language = "pt"

translated_text = translate_text(text_to_translate, target_language)
print(translated_text)
