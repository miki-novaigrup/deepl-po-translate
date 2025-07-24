import polib
import requests
import time

DEEPL_API_KEY = 'your_deepl_api_key_here'  # Replace with your actual API key
SOURCE_LANG = 'ES'
TARGET_LANG = 'PT'

ORIGIN_FILE = 'origin/xxxxx.po'
RESULT_FILE = 'result/xxxxx.po'

def translate_text(text):
    url = 'https://api-free.deepl.com/v2/translate'
    data = {
        'auth_key': DEEPL_API_KEY,
        'text': text,
        'source_lang': SOURCE_LANG,
        'target_lang': TARGET_LANG
    }
    response = requests.post(url, data=data)
    result = response.json()
    if 'translations' in result:
        return result['translations'][0]['text']
    else:
        print(f"DeepL error: {result}")
        return text

po = polib.pofile(ORIGIN_FILE)

for entry in po.untranslated_entries():
    print(f"Translating: {entry.msgid}")
    translated = translate_text(entry.msgid)
    entry.msgstr = translated
    time.sleep(1)  # Avoid hitting rate limits

po.save(RESULT_FILE)
print(f"Translation complete! Output: {RESULT_FILE}")
