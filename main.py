with open('books/frankenstein.txt') as f:
    file_content = f.read()
    words = file_content.split()
    final = {}
    characters = []


    for l in file_content.lower():
        if l.isalpha() == False:
            pass
        elif final.get(l) == None:
            final[l] = 1
            characters.append(l)
        else:
            final[l] += 1
    
    characters.sort()
    
    report = []


    for l in characters:
        statement = f'The "{l}" character was found {final[l]} times'
        report.append(statement)
    
    report = '\n'.join(report)
    
    print(f'''
            --- Begin report of books/frankenstein.txt ---
                {len(words)} words found in the document

                {report}

                --- End report ---    
    ''')
    
    
