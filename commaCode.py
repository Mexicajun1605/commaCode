#commaCode

RomLangs = ['Spanish', 'French', 'Italian', 'Portuguese', 'Romanian']
Cats = ['Michi', 'Ruth', 'Little Teeth', 'Beatrice']

def comma(hidledidi):
    if hidledidi[-1]:
        hidledidi[-1] = 'and ' + hidledidi[-1]
    lalala = ', '.join(hidledidi)
    print(lalala)


comma(RomLangs)
comma(Cats)