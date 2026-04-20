import random

def friends_translator(text, character):
    text = text.strip()

    if not text:
        return "Say something!"

    lower_text = text.lower()

    # ================= JOEY =================
    if character == "JOEY":
        if "food" in lower_text or "hungry" in lower_text:
            return "JOEY DOESN'T SHARE FOOD!"

        templates = [
            f"{text}... How you doin'?",
            f"{text}? How YOU doin'?",
            f"{text}... Hey, how YOU doin'?"
        ]
        return random.choice(templates)

    # ================= CHANDLER =================
    elif character == "CHANDLER":
        word = lower_text.replace("i'm", "").replace("i am", "").strip()

        if not word:
            word = "this"

        templates = [
            f"Could I BE any more {word}?",
            f"Oh wow, could that BE any more {word}?",
            f"Could this situation BE any more {word}?",
            f"Could that BE any more ridiculous?"
        ]
        return random.choice(templates)

    # ================= ROSS =================
    elif character == "ROSS":
        if "pivot" in lower_text:
            return "PIVOT! PIVOT! PIVOT!"

        if "we were on a break" in lower_text:
            return "WE WERE ON A BREAK!"

        if "sandwich" in lower_text:
            return "MY SANDWICH?! MY SANDWICH?!"

        templates = [
            f"{text}!!!",
            f"I mean, {text}...",
            f"{text}! This is unbelievable!",
            f"{text}! Why does this keep happening?!"
        ]
        return random.choice(templates)

    # ================= PHOEBE =================
    elif character == "PHOEBE":
        if "my eyes" in lower_text and lower_text.count("my eyes") >= 2:
            return "MY EYES! MY EYES!"

        if "cat" in lower_text:
            return "Smelly Cat, Smelly Cat, what are they feeding you?"

        templates = [
            f"{text}... but like in a weird, cosmic way.",
            f"{text}... ooooh that reminds me of a song!",
            f"This is brand new information!",
            f"{text}... but what if it's actually a spirit?",
            f"{text}... I feel like this is about your aura."
        ]
        return random.choice(templates)

    # ================= MONICA =================
    elif character == "MONICA":
        if "mess" in lower_text or "dirty" in lower_text:
            return "THIS IS A DISASTER!"

        if "hungry" in lower_text or "food" in lower_text:
            food_templates = [
                "Okay, what do we have to eat? Let me organize this.",
                "Alright, nobody panic. I’ll handle the food situation.",
                "We need a plan. Food first. Then everything else."
            ]
            return random.choice(food_templates)

        templates = [
            f"{text}! This is completely out of control!",
            f"{text}. I’ll fix this.",
            f"{text}! I KNOW!",
            f"{text}. Okay, we need a plan. RIGHT NOW."
        ]
        return random.choice(templates)

    # ================= RACHEL =================
    elif character == "RACHEL":
        if "job" in lower_text:
            return "I'm gonna go get one of those job things!"

        if "love" in lower_text:
            return "Oh my God, I love that!"

        templates = [
            f"{text}?! No way!",
            f"Oh my God, {text}!",
            f"{text}... I can’t even.",
            f"{text}! Are you serious?",
            f"{text}?! This is insane!"
        ]
        return random.choice(templates)

    # ================= DEFAULT =================
    return text