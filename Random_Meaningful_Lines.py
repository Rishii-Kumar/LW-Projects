def generate_random_meaningful_lines():
    try:
        import random
        import nltk
        from nltk.corpus import words

        # Get the list of English words from the NLTK corpus
        english_words = words.words()

        def generate_random_word():
            return random.choice(english_words)

        def generate_random_words(num_words):
            return [generate_random_word() for _ in range(num_words)]

        num_words = random.randint(1, 5)
        random_words = generate_random_words(num_words)
        ret = ""
        for word in random_words:
            if ret == "":
                ret = word
            else:
                ret = ret + " " + word
        return ret
    except Exception as e:
        generate_random_meaningful_lines()