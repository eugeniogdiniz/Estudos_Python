favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
        ", see your favorite language is " +
        favorite_languages[name].title() + "!")
    if 'erin' not in favorite_languages.keys():
        print("Erin, pelase take our poll!")