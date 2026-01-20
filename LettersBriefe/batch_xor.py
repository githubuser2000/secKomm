#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def xor_cipher(data, key):
    data_bytes = data.encode('utf-8')
    key_bytes = key.encode('utf-8')
    result = bytearray()
    for i in range(len(data_bytes)):
        key_byte = key_bytes[i % len(key_bytes)]
        result.append(data_bytes[i] ^ key_byte)
    return result

def process_hashes(hash_list, password):
    print(f"{'Original Hash':<24} | {'XOR-Ergebnis (Hex)'}")
    print("-" * 45)
    
    for h in hash_list:
        h = h.strip() # Entfernt Zeilenumbrüche
        if not h: continue
        
        encrypted = xor_cipher(h, password)
        print(f"{h:<24} | {encrypted.hex()}")

if __name__ == "__main__":
    # Erwartet: 1. Eine durch Komma getrennte Liste von Hashes (oder Dateipfad) 
    # 2. Das Passwort
    if len(sys.argv) < 3:
        print("Nutzung: python batch_xor.py 'hash1,hash2,hash3' 'passwort'")
        sys.exit(1)

    # Hashes aus dem ersten Argument extrahieren (getrennt durch Komma)
    input_hashes = sys.argv[1].split(',')
    password = sys.argv[2]

    process_hashes(input_hashes, password)

