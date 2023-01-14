from re import sub

with open('script.txt', 'r') as file:
    lines = file.readlines()
html = ''
num = 1
characters = dict()
counts = dict()
for line in lines:
    if line.strip():
        match line[0]:
            case '#':
                html += f'<div class="h1 row"><h1><p>{line[1:].strip()}</p></h1></div>\n'
            case '【':
                html += f'<div class="h2 row"><h2><p>{line.strip()}</p></h2></div>\n'
            case '〔':
                html += f'<div class="h3 row"><h3><p>{line.strip()}</p></h3></div>\n'
            case '\'':
                html += f'<div class="stage-direction row"><div class="character column"></div><div class="line column"><p>{line[1:].strip()}</p></div><div class="number column"><p>{num}</p></div></div>\n'
                num += 1
            case _:
                character = line.split(':')[0]
                names = character.split('@')[0].split('、')
                count = len(sub('[，！？、。「」…“”《》~—\n,.!?’ ]','',sub('（.*?）', '',''.join(line.split(":")[1:]))))
                for name in names:
                    if name not in characters:
                        characters.update({name: len(characters)})
                        counts.update({name: 0})
                    counts[name] += count
                classname = ' '.join(f"c{characters[name]}" for name in names)
                displayname = character.split('@')[-1]
                nameclass = 'wide ' if len(displayname)==2 or '、' in displayname else ('gapped ' if len(displayname)==3 else '')
                html += f'<div class="dialogue row {classname}"><div class="character column"><p class="{nameclass}name">{displayname.replace("、","<br>")}</p></div><div class="line column"><p>{"：".join(line.split(":")[1:])}</p></div><div class="number column"><p>{num}</p></div></div>\n'
                num += 1
with open('script.html', 'w') as file:
    file.write(html)

items = ''
for name in sorted(counts, key=counts.get, reverse=True):
    items += f'<div class="item" id="c{characters[name]}" onclick="toggle(this);"><p>{name}</p></div>\n'
    print(characters[name], name, counts[name])
with open('characters.html', 'w') as file:
    file.write(items)
