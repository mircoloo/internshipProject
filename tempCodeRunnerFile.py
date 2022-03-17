data = []
for i in range(len(numbers)):
    data.append([numbers[i], types[i], scores[i]])
df = pd.DataFrame(data, columns=['Number', 'Type', 'Score'])

print(df)



