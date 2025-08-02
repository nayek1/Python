# Write a proram to fill in letter template given below with name and date.

letter = '''Dear <|NAME|>,
          You are selected!
          <|DATE|>'''
print(letter.replace("<|NAME|>", "Sagar").replace("<|DATE|>", "1st Jan 2200"))
