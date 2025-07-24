import polib
import requests
import time
import config

def translate_text(text):
    url = DEEPL_API_URL
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
