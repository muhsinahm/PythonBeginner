#letter template given below with name and date.
letter = '''Dear <|Name|>
            You are selected
            <|Date|>'''
print(letter.replace("<|Name|>","Muhsin").replace("<|Date|>","30th April "))