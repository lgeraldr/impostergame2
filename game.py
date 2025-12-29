import random
from word_data import word_list, get_same_category_words, question_list

def weighted_imposter_count(players):
    options = [1, 2, 3, 4, 5]
    weights = [75, 18, 3, 3, 1]
    count = random.choices(options, weights=weights, k=1)[0]
    return min(count, players)

def create_game(players, difficulty, mode="classic"):
    mode = mode.lower()
    if mode not in ["classic", "imposter_no_word", "question"]:
        mode = "classic"

    imposters_count = weighted_imposter_count(players)
    imposters = random.sample(range(players), imposters_count)

    roles = []
    secret_word = None
    category = None

    if mode in ["classic", "imposter_no_word"]:
        eligible = [w for w in word_list if w[1] <= difficulty]
        if not eligible:
            secret_word, category = "DEFAULT", "default"
        else:
            secret_word, category = random.choice(eligible)

        same_cat_words = get_same_category_words(secret_word, difficulty)
        if secret_word in same_cat_words:
            same_cat_words.remove(secret_word)

        for i in range(players):
            if i in imposters:
                if mode == "classic":
                    roles.append(random.choice(same_cat_words) if same_cat_words else secret_word)
                else:
                    roles.append(None)
            else:
                roles.append(secret_word)

    elif mode == "question":
        categories = list(set(cat for _, cat in question_list))
        category = random.choice(categories)

        main_candidates = [q for q, cat_q in question_list if cat_q == category]
        main_question = random.choice(main_candidates)

        for i in range(players):
            if i in imposters:
                imp_candidates = [q for q in main_candidates if q != main_question]
                roles.append(random.choice(imp_candidates) if imp_candidates else main_question)
            else:
                roles.append(main_question)

    # **Do not shuffle roles** — keep indices consistent for final reveal
    starting_player = random.randint(0, players - 1)

    return {
        "players": players,
        "difficulty": difficulty,
        "roles": roles,
        "imposters": imposters,  # these are indices 0..players-1
        "mode": mode,
        "current_player": starting_player,
        "secret_word": secret_word
    }


