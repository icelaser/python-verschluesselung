# python-verschluesselung
kleines Demo Projekt von einer Verschlüsselung

Anhand der Asci Tabelle wird an einem kleinen Beispiel einfach mal jedes Zeichen um eine Zahl verschoben und somit die Ausgabe verschlüsselt.
Damit es nicht ganz so einfach ist. z.b. wenn man als Text nur "aaaa" eingibt, wäre der verschlüsselter Text sehr leicht herausfindbar. Daher wird sogar anhand des Indexes des Zeichen noch zusätzlich verschlüsselt. Also sehr einfach.


Aufgerufen werden kann es mit 2 Argumenten:

Dieses Beispiel verschlüsselt den String "abcd". Das Argument true gibt an, das der Text verschlüsselt wird.

python main.py \"abcd\" true



Dieses Beispiel entschlüsselt den String "fhjl". Das Argument false gibt an, das der Text entschlüsselt wird.

python main.py \"fhjl\" false

