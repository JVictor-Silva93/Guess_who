NAMES = ("Michael", "James", "Oscar", "Fred", "Steve", "Ace", "Bill", "Marcus", "Brian", "Jeremy",
         "Eliza", "Faith", "Sally", "Maria", "Jacqueline", "Cheri", "Ashley", "Emily", "Bianca", "Alice")
GENDERS = ("male", "female")
EYE_COLORS = ("blue", "green", "brown")
HAIR_COLORS = ("black", "red", "blonde", "grey", "brown")
RACE = ("white", "black", "hispanic", "asian")
FACIAL_HAIR = ("none", "mustache", "beard")
JEWELRY = ("necklace", "ear rings", "glasses", "none")

question_bank = [" "]

def question_generator():

    for gender in GENDERS:
        question_bank.append(f"Are you a {gender}?")
    for eye_color in EYE_COLORS:
        question_bank.append(f"Does your person have {eye_color} eyes?")
    for hair_color in HAIR_COLORS:
        question_bank.append(f"Does your person have {hair_color} hair?")
    for race in RACE:
        question_bank.append(f"Is your person {race}?")
    for style in FACIAL_HAIR:
        if style == "none":
            question_bank.append(f"Was your person skipped when God handed out the facial hair genes?")
        else:
            question_bank.append(f"Does your person have a {style}")
    for item in JEWELRY:
        if item == "none":
            question_bank.append(f"Is your person NOT wearing glasses or jewelry?")
        else:
            question_bank.append(f"Is your person wearing {item}")
    for name in NAMES:
        question_bank.append(f"Is your person {name}?")

    question_num = 1
    for question in question_bank:
        if question != " ":
            print(f"{question_num}. {question}")
            question_num += 1



question_generator()