import json
from pathlib import Path


def get_creator_transcriptions(creator_name):
    """
    Reads the transcriptions of a specific creator from the JSON file
    and returns them formatted in markdown.

    Args:
        creator_name (str): Creator's name (e.g., 'jeffnippard', 'kallaway')

    Returns:
        str: Transcriptions formatted in markdown or an error message
    """
    try:
        with open("transcriptions.json", "r", encoding="utf-8") as f:
            transcriptions = json.load(f)

        if creator_name not in transcriptions:
            return f"Creator '{creator_name}' not found. Available creators: {list(transcriptions.keys())}"

        creator_transcriptions = transcriptions[creator_name]

        if not creator_transcriptions:
            return f"No transcription found for creator '{creator_name}'"

        formatted_transcriptions = []
        for i, item in enumerate(creator_transcriptions, 1):
            video_name = item["video"]
            transcription = item["transcription"]
            formatted_transcriptions.append(f"Transcript {i}\n{transcription}")

        return "\n\n".join(formatted_transcriptions)

    except FileNotFoundError:
        return "File transcriptions.json not found. Run transcripter.py first."
    except json.JSONDecodeError:
        return "Error reading transcriptions.json. File corrupted."
    except Exception as e:
        return f"Unexpected error: {str(e)}"


def list_available_creators():
    """
    Lists all available creators from the JSON file.

    Returns:
        str: List of available creators
    """
    try:
        with open("transcriptions.json", "r", encoding="utf-8") as f:
            transcriptions = json.load(f)

        creators = list(transcriptions.keys())
        if creators:
            return f"Available creators: {', '.join(creators)}"
        else:
            return "No creators found in the file."

    except FileNotFoundError:
        return "File transcriptions.json not found."
    except Exception as e:
        return f"Error while listing creators: {str(e)}"
