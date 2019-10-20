import re

_PLAYERS = {
    "🛡": "Armia",
    "🐆": "Byron",
    "🍳": "Chiarot",
    "👨‍👦‍👦": "Cousins",
    "⚜️": "Danault",
    "Ⓜ️": "Domi",
    "✍🏽": "Drouin",
    "✝️": "Folin",
    "👨🏼": "Gallagher",
    "👶🏻": "Kotkaniemi",
    "❄️": "Kulak",
    "🇫🇮": "Lehkonen",
    "🥩": "Mete",
    "🧫": "Petry",
    "💲": "Price",
    "🏍": "Suzuki",
    "🐟": "Tatar",
    "🧔🏻": "Thompson",
    "🎡": "Weal",
    "🚀": "Weber",
}

_OTHERS = {"🚨": "Goal", "🍎": "Assist", "w/": "with"}

_ALL = {}
_ALL.update(_PLAYERS)
_ALL.update(_OTHERS)


_CLEANUP = [
    (re.compile(r"\s+[,\.]\s*", re.IGNORECASE), ", "),
    (re.compile(r"\s+\)"), ")"),
    (re.compile(r"\(\s+"), "("),
    (re.compile(r"\s+"), " "),
]


def decode(source: str, helper=False):
    for emoji, text in _ALL.items():
        repl = f'{text} ({emoji})' if helper else text
        source = source.replace(emoji, repl)

    for regex, repl in _CLEANUP:
        source = regex.sub(repl, source)

    return source


def encode(source: str, helper=False):
    for emoji, text in _ALL.items():
        repl = f'{emoji} ({text})' if helper else emoji
        source = re.sub(text, repl, source, flags=re.IGNORECASE)
    return source
