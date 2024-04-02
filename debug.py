data1 = ['Notes', 'WorkSpace', 'React', 'Angular', 'Veu', 'Public', 'General', 'Downloads', 'Word File.doc',
         'Excel File.doc']
data2 = ['notes', 'workspace', 'react', 'angular', 'veu', 'public', 'general', 'downloads', 'wordFile', 'excelFile']

print(str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower())
print(data2)

data1 = str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower()
data2 = str(data2).replace(' ', '').lower()

assert data1 == data2
