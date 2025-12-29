import random
from word_data import word_list, get_same_category_words, question_list

def weighted_imposter_count(players):
    """Decide how many imposters based on number of players."""
    options = [1, 2, 3, 4, 5]
    weights = [75, 18, 3, 3, 1]
    count = random.choices(options, weights=weights, k=1)[0]
    return min(count, players)

def create_game(players, difficulty, mode="classic"):
    """
    Create a game dictionary with all roles and settings.
    Modes:
      - classic: imposters get a different word from same category
      - imposter_no_word: imposters get None, told they are the imposter
      - question: everyone gets a question; imposters get a different question
    """
    mode = mode.lower()
    valid_modes = ["classic", "imposter_no_word", "question"]
    if mode not in valid_modes:
        mode = "classic"

    imposters_count = weighted_imposter_count(players)
    imposters = random.sample(range(players), imposters_count)

    roles = []

    if mode in ["classic", "imposter_no_word"]:
        eligible_words = [w for w in word_list if w[1] <= difficulty]
        if not eligible_words:
            secret_word, category = ("default", "default")
        else:
            secret_word, category = random.choice(eligible_words)

        same_cat_words = get_same_category_words(secret_word, difficulty)

        for i in range(players):
            if i in imposters:
                if mode == "classic":
                    roles.append(random.choice(same_cat_words))
                else:  # imposter_no_word
                    roles.append(None)
            else:
                roles.append(secret_word)

    elif mode == "question":
        main_question = random.choice(question_list)
        imposter_question = random.choice([q for q in question_list if q != main_question])

        for i in range(players):
            if i in imposters:
                roles.append(imposter_question)
            else:
                roles.append(main_question)

    # Shuffle roles and keep track of original indices
    combined = list(zip(range(players), roles))
    random.shuffle(combined)
    _, roles = zip(*combined)
    roles = list(roles)

    starting_player = random.randint(0, players - 1)

    return {
        "players": players,
        "difficulty": difficulty,
        "roles": roles,
        "imposters": imposters,
        "mode": mode,
        "current_player": starting_player,
        "secret_word": secret_word if mode != "question" else None
    }
