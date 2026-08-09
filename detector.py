def scan(text):
    text_lower = text.lower()
    matches = []
    for phrase in SUSPICIOUS_PHRASES:
        if phrase in text_lower:
            matches.append(phrase)
    return matches


def is_suspicious(text):
    return len(scan(text)) > 0
