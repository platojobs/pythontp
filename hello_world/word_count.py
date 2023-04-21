def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
             contens = f.read()
    except FileNotFoundError:
        print(f'Sorry, the file {filename} does not exist.')
    else:
        words = contens.split()
        num_words = len(words)
        print(f'The file {filename} has about {num_words} words.')

