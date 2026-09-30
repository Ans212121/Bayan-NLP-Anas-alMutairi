"""Shared correction preprocessing contract; NFC + whitespace + course PII masking."""
import re, unicodedata
VERSION = "bayan-protected-nfc/1.0.0"
def prepare(text):
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "<EMAIL>", text)
    text = re.sub(r"(?<!\d)(?:\+?966|0)?5\d{8}(?!\d)", "<PHONE>", text)
    return " ".join(text.split())
