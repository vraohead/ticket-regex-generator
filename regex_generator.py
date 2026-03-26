import re

def generate_regex(text, enable_mapping=False):
    patterns = {}

    date_pattern = r"\b\d{2}[/-]\d{2}[/-]\d{4}\b|\b\w+\s\d{1,2},\s\d{4}\b"
    time_pattern = r"\b\d{1,2}:\d{2}\s?(AM|PM|am|pm)?\b"
    pax_pattern = r"(?:Pax|Guests|Adults|Total)[:\s]*(\d+)"

    if re.search(date_pattern, text):
        patterns["date"] = date_pattern

    if re.search(time_pattern, text):
        patterns["time"] = time_pattern

    if re.search(pax_pattern, text):
        patterns["total_pax_count"] = pax_pattern

    lines = [l.strip() for l in text.split("\n") if l.strip()]
    raw_experience = lines[0] if lines else "Unknown"

    result = {
        "experience_name": raw_experience,
        "mapping_enabled": enable_mapping,
        "patterns": patterns
    }

    if enable_mapping:
        result["mappings"] = {
            "experience": {}
        }

    return result
