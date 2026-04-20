import re

catchphrases = {
    "ROSS": [
        r"we\s+were\s+on\s+a\s+break",
        r"pivot",
        r"unagi",
        r"i[' ]?m\s+fine",
        r"my\s+sandwich",
        r"you\s+ate\s+my\s+sandwich",
        r"i\s+got\s+off\s+the\s+plane",
        r"\bhi\b",
        r"tastes\s+like\s+feet"
    ],

    "CHANDLER": [
        r"could\s+i\s+be",
        r"could\s+this\s+be",
        r"sarcastic\s+comment",
        r"we\s+had\s+a\s+deal",
        r"hopeless\s+and\s+awkward",
        r"q[- ]?tip",
        r"oh\s+crap",
        r"not\s+even\s+a\s+word"
    ],

    "RACHEL": [
        r"no\s+uterus\s+no\s+opinion",
        r"not\s+that\s+common",
        r"big\s+deal",
        r"dessert\s+thief",
        r"you\s+fell\s+asleep",
        r"job\s+things",
        r"beef\s+in\s+the\s+trifle"
    ],

    "MONICA": [
        r"i\s+know",
        r"welcome\s+to\s+the\s+real\s+world",
        r"seven",
        r"this\s+is\s+a\s+disaster",
        r"organized",
        r"rules\s+are\s+good",
        r"i\s+am\s+breezy"
    ],

    "JOEY": [
        r"how\s+you\s+doin['g]?",
        r"joey\s+doesn[' ]?t\s+share\s+food",
        r"moo\s+point",
        r"thanksgiving\s+without\s+turkey",
        r"i[' ]?m\s+curvy",
        r"i[' ]?m\s+not\s+even\s+sorry"
    ],

    "PHOEBE": [
        r"smelly\s+cat",
        r"they\s+don[' ]?t\s+know\s+that\s+we\s+know",
        r"oh\s+no",
        r"brand\s+new\s+information",
        r"he[' ]?s\s+her\s+lobster",
        r"burning\s+in\s+hell",
        r"my\s+eyes[,!\s]*my\s+eyes"
    ]
}


def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s']", "", text)
    return text


def detect_catchphrase(text):
    clean_text = preprocess(text)

    for character, patterns in catchphrases.items():
        for pattern in patterns:
            if re.search(pattern, clean_text):
                return character, pattern

    return None, None