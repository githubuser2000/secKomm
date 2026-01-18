import sys

def xor_cipher(data, key):
    # Konvertierung in Byte-Arrays
    data_bytes = data.encode('utf-8')
    key_bytes = key.encode('utf-8')
    
    result = bytearray()
    for i in range(len(data_bytes)):
        # Wiederholung des Passworts durch Modulo
        key_byte = key_bytes[i % len(key_bytes)]
        result.append(data_bytes[i] ^ key_byte)
    return result

if __name__ == "__main__":
    # Prüfung, ob genug Argumente übergeben wurden
    if len(sys.argv) < 3:
        print("Nutzung: python xor_tool.py '<Text>' '<Passwort>'")
        sys.exit(1)

    input_text = sys.argv[1]
    password = sys.argv[2]

    # Operation durchführen
    output = xor_cipher(input_text, password)

    print(f"Eingabe:  {input_text}")
    print(f"Passwort: {password}")
    print("-" * 20)
    # Ausgabe als Hexadezimal-String, da das Ergebnis oft kein lesbarer Text ist
    print(f"Ergebnis (Hex): {output.hex()}")
    
    # Falls man das Ergebnis direkt wieder in Text umwandeln will (nur bei Entschlüsselung sinnvoll)
    try:
        print(f"Ergebnis (Text): {output.decode('utf-8')}")
    except UnicodeDecodeError:
        print("Ergebnis (Text): [Nicht als UTF-8 darstellbar - Binärdaten]")

