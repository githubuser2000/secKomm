#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import zlib
import sys

def split_by_length(text, max_length=80):
    """Zerlegt einen String in Stücke von maximal max_length Zeichen."""
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]

def main():
    if len(sys.argv) < 2:
        print("Nutzung: python skript.py dateiname.txt")
        return

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 1. Schritt: Splitten nach Trennzeichen
        initial_parts = [s.strip() for s in re.split(r'[\n,\.\?\!]', content) if s.strip()]

        # 2. Schritt: Falls ein Teil > 80 Zeichen ist, weiter zerlegen
        final_substrings = []
        for part in initial_parts:
            if len(part) > 80:
                final_substrings.extend(split_by_length(part, 80))
            else:
                final_substrings.append(part)

        # Ausgabe
        print(f"{'Teilstring (Auszug)':<40} | {'Länge':<5} | {'CRC32 (Hex)':<12}")
        print("-" * 65)

        for s in final_substrings:
            crc_val = zlib.crc32(s.encode('utf-8'))
            # Anzeige auf 37 Zeichen kürzen für die Tabelle, falls nötig
            display_str = (s[:37] + '..') if len(s) > 37 else s
            print(f"{display_str:<40} | {len(s):<5} | {hex(crc_val)}")

    except FileNotFoundError:
        print(f"Fehler: Datei '{file_path}' nicht gefunden.")

if __name__ == "__main__":
    main()

