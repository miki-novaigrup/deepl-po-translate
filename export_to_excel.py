import polib
import config
from openpyxl import Workbook

# Input and output file names
po_file = 'messages.pt.po'
xlsx_file = 'messages.pt.xlsx'

# Load PO file
po = polib.pofile(po_file)

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
wb.save(xlsx_file)

print(f"✅ Exported: {xlsx_file}")
