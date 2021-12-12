favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    } 
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+".")

if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll!")
