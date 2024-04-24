import random
firsword = [
    "quick", "lazy", "sleepy", "noisy", "hungry", "scary", "spooky", "silly",
    "messy", "lucky", "happy", "sad", "angry", "tiny", "huge", "giant",
    "blue", "red", "green", "yellow", "purple", "orange", "pink", "brown",
    "black", "white", "gray", "bright", "dark", "light", "heavy", "thin",
    "thick", "narrow", "wide", "tall", "short", "small", "large", "big",
    "good", "bad", "fantastic", "terrible", "awesome", "awful", "beautiful",
    "ugly", "handsome", "pretty", "cute", "elegant", "fancy", "plain",
    "fuzzy", "smooth", "soft", "hard", "cold", "hot", "warm", "cool",
    "wet", "dry", "clean", "dirty", "empty", "full", "new", "old",
    "young", "ancient", "modern", "fast", "slow", "early", "late",
    "bright", "shiny", "dull", "sparkling", "glowing", "flickering", "flashing",
    "blazing", "burning", "freezing", "cooling", "breezy", "windy", "stormy",
    "thundering", "sunny", "cloudy", "rainy", "snowy", "frosty", "foggy"
]
secondword = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yam", "zucchini",
    "actor", "baker", "carpenter", "doctor", "engineer", "farmer", "golfer", "hunter",
    "instructor", "jeweler", "knight", "lawyer", "musician", "nurse", "officer", "painter",
    "quarterback", "racer", "sailor", "teacher", "umpire", "veterinarian", "writer", "xylophonist",
    "yogi", "zoologist", "ant", "bat", "cat", "dog", "elephant", "frog", "giraffe", "hippopotamus",
    "iguana", "jaguar", "kangaroo", "lion", "monkey", "newt", "octopus", "penguin", "quail", "rabbit",
    "shark", "tiger", "urchin", "vulture", "whale", "xerus", "yak", "zebra", "airplane", "bicycle",
    "car", "drone", "elevator", "ferry", "glider", "helicopter", "island", "jeep", "kayak", "limousine",
    "motorcycle", "narrowboat", "ocean liner", "paddleboat", "quad bike", "raft", "submarine", "train",
    "unicycle", "van", "wagon", "yacht", "zeppelin"
]
thirdword = [
    "aboard", "about", "above", "across", "after", "against", "along", "amid",
    "among", "around", "as", "at", "before", "behind", "below", "beneath",
    "beside", "between", "beyond", "but", "by", "concerning", "considering",
    "despite", "down", "during", "except", "for", "from", "in", "inside",
    "into", "like", "minus", "near", "of", "off", "on", "onto", "opposite",
    "out", "outside", "over", "past", "per", "plus", "regarding", "round",
    "since", "than", "through", "to", "toward", "under", "underneath", "unlike",
    "until", "up", "upon", "versus", "via", "with", "within", "without",
    "according to", "ahead of", "apart from", "as for", "as of", "as per",
    "as regards", "aside from", "back to", "because of", "close to", "due to",
    "except for", "far from", "in to", "inside of", "instead of", "left of",
    "near to", "next to", "on to", "opposite of", "opposite to", "out from",
    "out of", "outside of", "over to", "prior to", "right of", "thanks to",
    "up to", "via"
]

plugin_active_message = "welcome to the end"

def dem():
    print("endmessage: " + random.choice(firsword) + " " + random.choice(secondword) + " " + random.choice(thirdword) + " the " + random.choice(secondword))