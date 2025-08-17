# Transcriptions Utility

This module provides functions to read and format transcriptions of specific creators stored in a JSON file.

---

## Functions

### `get_creator_transcriptions(creator_name)`
Reads the transcriptions of a specific creator from the JSON file and returns them formatted in Markdown.

**Args:**
- `creator_name (str)`: Creator's name (e.g., `'jeffnippard'`, `'kallaway'`).

**Returns:**
- `str`: Transcriptions formatted in Markdown or an error message.

**Error Messages:**
- `"Creator '<name>' not found. Available creators: [...]"`
- `"No transcription found for creator '<name>'"`
- `"File transcriptions.json not found. Run transcripter.py first."`
- `"Error reading transcriptions.json. File corrupted."`
- `"Unexpected error: <error message>"`

---

### `list_available_creators()`
Lists all available creators from the JSON file.

**Returns:**
- `str`: List of available creators.

**Error Messages:**
- `"No creators found in the file."`
- `"File transcriptions.json not found."`
- `"Error while listing creators: <error message>"`

---

## Notes
- All transcriptions are loaded from `transcriptions.json`.
- Transcriptions are returned in a simple Markdown format for readability.
