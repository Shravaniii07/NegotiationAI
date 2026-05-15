def calculate_score(sentiment):

    score = 50

    if "positive" in sentiment:
        score += 20
    elif "negative" in sentiment:
        score -= 10

    return max(0, min(score, 100))