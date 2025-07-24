# Auto-Translate `.po` Files with DeepL API (Windows)

This tool allows you to automatically translate gettext `.po` files (used in many PHP/WordPress/Statamic/localization systems) using the **DeepL API**.

---

## 🧩 Requirements

- Windows 10/11
- Python 3.12+ installed
- DeepL API Key (Free or Pro)
- Internet connection

---

## 🛠️ 1. Install Python

1. Download Python for Windows from:  
    👉 [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

2. Run the installer:
   - ✅ **Check "Add Python to PATH"**
   - Click **"Install Now"**

3. Verify installation:
   ```bash
   python --version
   ```

4. Install dependencies
    ```bash
    pip install polib requests
    ```

    - polib – for reading and writing .po files
    - requests – for calling the DeepL API

## 2. Configure py script

1. Add the DeepL API key:
    ```python
    DEEPL_API_KEY = 'your_deepl_api_key_here'
    ```

2. Set the origin and result language:
    ```python
    SOURCE_LANG = 'origin/xxxx.po'
    TARGET_LANG = 'result/xxxx.po'
    ```

3. Set the origin and result files:
    ```python
    ORIGIN_FILE = 'origin/xxxx.po'
    RESULT_FILE = 'result/xxxx.po'
    ```

4. Modify the time between translations (optional):
    ```python
    time.sleep(1)
    ```

## 3. Execute script

1. Execute py command: 

    ```bash
    python translate_po.py
    ```