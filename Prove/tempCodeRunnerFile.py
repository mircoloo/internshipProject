pattern = re.compile(r'+')
output = pattern.search(t)
driver.implicitly_wait(3)
print(output.group(0))