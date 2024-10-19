import argparse
import sys

verschiebung = 5

# Verschlüsselung
def decodeIt(eingabe):
    verschluesselt = ""
    for i in range(len(eingabe)):
        char = eingabe[i]
        zahlChar = ord(char)
        geaenderteZahlChar = zahlChar + (i + verschiebung)
        geaendertesChar = chr(geaenderteZahlChar)
        verschluesselt += geaendertesChar
    print(verschluesselt)

# Entschlüsselung
def encodeIt(verschluesselt):
    entschluesselt = ""
    for i in range(len(verschluesselt)):
        char = verschluesselt[i]
        zahlChar = ord(char)
        geaenderteZahlChar = zahlChar - (i + verschiebung)
        geaendertesChar = chr(geaenderteZahlChar)
        entschluesselt += geaendertesChar
    print(entschluesselt)

def main(text, decode):
    if decode:
        decodeIt(text)
    else:
        encodeIt(text)

def str2bool(value):
    if value.lower() in ('true', '1'):
        return True
    elif value.lower() in ('false', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError(f"Invalid boolean value: {value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verschlüsselungs Tool")
    parser.add_argument("text", type=str, help="Der Text, der decodiert bzw. encodiert werden soll")
    parser.add_argument("decode", type=str2bool, help="Ein boolescher Wert (true/false)")

    if len(sys.argv) < 3:
        print("Fehler: Bitte gebe sowohl einen Text der decodiert bzw. encodiert werden soll, als auch einen booleschen Wert an.")
        print("Beispiel: python main.py \"abcd\" true")
        print("Beispiel: python main.py \"fhjl\" false")
        sys.exit(1)
    
    args = parser.parse_args()
    
    main(args.text, args.decode)
