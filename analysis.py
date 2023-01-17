from re import sub

with open('script.txt', 'r') as file:
    lines = file.readlines()

act = -1
scene = 0
counts = dict()

requirement = ''

for line in lines:
    if line.strip():
        match line[0]:
            case '【':
                act += 1
                scene = 0
            case '〔':
                # clean up
                total = 0
                for name in counts:
                    requirement += f'"{name}": {counts[name]}, '
                    total += counts[name]
                requirement = requirement[:-2] + f'}}, {total}], '
                print(requirement)
                # next
                scene += 1
                counts = dict()
                requirement = f'["{act}.{scene} {line.split(":")[1][:-2]}", {{'
            case '\'':
                pass
            case _:
                character = line.split(':')[0]
                names = character.split('@')[0].split('、')
                count = len(sub('[，！？、。「」…“”《》~—\n,.!?’ ]','',sub('（.*?）', '',''.join(line.split(":")[1:]))))
                for name in names:
                    if name not in counts:
                        counts.update({name: 0})
                    counts[name] += count
            