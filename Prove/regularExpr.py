import re
"""
text = "tellows Valutazione per 34535345 : Score 55"


windows_filepath = r'\b[A-Z]:\\[A-Za-z0-9-_\.\\]+\b'
score = r"Score\s?(\d+)"


result  = re.findall(windows_filepath, text)

print(result)

"""


x = 'tellows valutazione per 34535345 : Score 55'
#output = re.search('(?<=Your number is )<b>(\d+)</b>',x).group(1)
output = re.search('Score\s?(\d+)',x).group(1)
print(output)