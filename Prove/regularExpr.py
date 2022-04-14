#!python3

import re 



t = "ocr ha segnalato Sconosciuto con il numero 393482764328 come Truffa 15/03/22 14.00 Avevano il mio numero ma cercavano mia madre per la bolletta della luce, molto molto sospetto. Appena ho chiesto come avessero il mio numero hanno attaccato 6 Valutazioni per +393482764328 (Vodafone (cellulare))"

pattern = re.compile(r'\+?\d{7,15}')
output = pattern.search(t)
print(output.group(0))
