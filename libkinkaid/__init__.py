import re
import sys

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


def decode(text: str, helper=True):
    for code, item in _ALL.items():
        repl = item
        if helper:
            repl = f'{item} ({code})'
        text = text.replace(code, repl)

    for regex, repl in _CLEANUP:
        text = regex.sub(repl, text)

    return text


print(decode(sys.argv[1]))
