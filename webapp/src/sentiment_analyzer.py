def get_positive_words():
    words = [
    "positive",
    "good",
    "great",
    "excellent",
    "wonderful",
    "fantastic",
    "amazing",
    "awesome",
    "love",
    "happy",
    "joy",
    "fun",
    "terrific",
    "brilliant",
    "outstanding",
    "superb",
    "smile",
    "laugh",
    "delight",
    "victory",
    "paradise",
    "beautiful",
    "beauty"
    ]
    return words


def get_negative_words():
    words = [
    "negative",
    "bad",
    "poor",
    "terrible",
    "awful",
    "horrible",
    "dreadful",
    "hate",
    "sad",
    "unhappy",
    "pain",
    "disaster",
    "depressed",
    "overwhelming",
    "tragic",
    "grief",
    "regret",
    "fail",
    "disappointment",
    "defeat",
    "suffer",
    "nightmare",
    "ugly"
    ]  
    return words


def analyze(text: str):
    # Get positive and negative words
    positive_words = get_positive_words()
    negative_words = get_negative_words()

    # Split text into words
    words = text.split(" ")
    # Analyze text words
    polarity = 0
    for word in words:
        if word in positive_words:
            polarity += 1
        elif word in negative_words:
            polarity -= 1

    if polarity >= 1:
        return "positive"
    if polarity <= -1:
        return "negative"
    return "neutral"