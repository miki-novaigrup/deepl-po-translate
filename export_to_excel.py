import polib
import config
from openpyxl import Workbook

xlsx_file = 'messages.pt.xlsx'

# Load PO file
po = polib.pofile(config.ORIGIN_FILE)

# Create workbook
wb = Workbook()
ws = wb.active
ws.title = "Translations"

# Add headers
ws.append(["msgid (Original)", "msgstr (Portuguese Translation)"])

# Add entries
for entry in po:
    ws.append([entry.msgid, entry.msgstr])

# Save Excel file
wb.save(config.EXPORTED_XLSX_FILE)

print(f"✅ Exported: {config.EXPORTED_XLSX_FILE}")
