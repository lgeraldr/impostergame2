# word_data.py
import random

# ============================================================
# WORD LIST
# Format: ("word", difficulty)
# Difficulty: 1 (very common) → 5 (very obscure)
# ============================================================

word_list = [
    # --- Geography / Countries ---
    ("city", 1), ("country", 1), ("river", 1), ("lake", 1), ("ocean", 1),
    ("mountain", 1), ("island", 2), ("continent", 2), ("desert", 1),
    ("forest", 1), ("valley", 2), ("canyon", 2), ("plateau", 3),
    ("glacier", 3), ("volcano", 2), ("harbor", 2), ("coast", 1),
    ("peninsula", 3), ("archipelago", 4), ("fjord", 4), ("delta", 3),
    ("savanna", 3), ("tundra", 4), ("bay", 2), ("reef", 3), ("strait", 3),
    ("Antarctica", 2), ("Australia", 2), ("Brazil", 1), ("Canada", 1),
    ("China", 1), ("Egypt", 2), ("France", 1), ("Germany", 1), ("India", 1),
    ("Italy", 1), ("Japan", 1), ("Kenya", 2), ("Mexico", 1), ("Norway", 2),
    ("Peru", 2), ("Russia", 1), ("Spain", 1), ("Thailand", 2), ("UK", 1),
    ("USA", 1), ("Vietnam", 2), ("Zimbabwe", 3),
    # Added 50 more countries
    ("Argentina", 2), ("Belgium", 2), ("Chile", 2), ("Colombia", 2), ("Cuba", 2),
    ("Denmark", 2), ("Finland", 2), ("Greece", 2), ("Hungary", 3), ("Iceland", 3),
    ("Ireland", 2), ("Israel", 2), ("Jordan", 3), ("Kazakhstan", 4), ("Laos", 3),
    ("Lebanon", 3), ("Malaysia", 3), ("Morocco", 3), ("Nepal", 3), ("Netherlands", 2),
    ("New Zealand", 2), ("Nigeria", 3), ("North Korea", 4), ("Pakistan", 3), ("Poland", 2),
    ("Portugal", 2), ("Romania", 3), ("Saudi Arabia", 3), ("Scotland", 2), ("Senegal", 3),
    ("South Africa", 2), ("South Korea", 2), ("Sweden", 2), ("Switzerland", 2), ("Syria", 3),
    ("Turkey", 2), ("Ukraine", 2), ("United Arab Emirates", 3), ("Venezuela", 3), ("Wales", 2),
    ("Yemen", 3), ("Zambia", 3), ("Bhutan", 4), ("Burundi", 4), ("Cambodia", 3),
    ("Costa Rica", 2), ("El Salvador", 3), ("Ethiopia", 3), ("Ghana", 3), ("Guatemala", 3),

    # --- Science ---
    ("atom", 2), ("molecule", 2), ("cell", 2), ("protein", 2), ("dna", 2),
    ("species", 3), ("ecosystem", 3), ("gravity", 2), ("energy", 2), ("force", 2),
    ("motion", 2), ("velocity", 3), ("density", 3), ("radiation", 3), ("mutation", 3),
    ("quantum", 4), ("neuron", 3), ("enzyme", 3), ("hormone", 2), ("photosynthesis", 4),
    ("blackhole", 5), ("electron", 2), ("atomos", 4), ("chlorophyll", 4),
    ("galaxy", 3), ("planet", 2), ("star", 1), ("nebula", 4), ("comet", 3),
    ("voltage", 2), ("current", 2), ("magnet", 2), ("bacteria", 3), ("virus", 3),
    ("fungus", 3),
    # Added ~50 more science concepts
    ("crystal", 2), ("element", 2), ("ion", 2), ("gravitywave", 5), ("blackbody", 4),
    ("osmosis", 3), ("photosphere", 4), ("chloroplast", 3), ("ribosome", 3), ("chromosome", 3),
    ("mitosis", 3), ("meiosis", 4), ("plasma", 3), ("supernova", 4), ("paleontology", 4),
    ("geology", 2), ("mineral", 2), ("sediment", 3), ("volcanology", 5), ("meteorology", 3),
    ("neutron", 3), ("proton", 3), ("antimatter", 4), ("darkmatter", 5), ("fission", 3),
    ("fusion", 3), ("catalyst", 3), ("thermodynamics", 4), ("entropy", 4), ("acidity", 2),
    ("alkali", 3), ("isotope", 3), ("vapor", 2), ("precipitate", 3), ("solution", 2),
    ("colloid", 3), ("polymer", 3), ("crustacean", 3), ("arachnid", 3), ("mollusk", 3),
    ("cellulose", 3), ("proteinase", 4), ("ligand", 4), ("enzymeactivity", 4), ("gene", 2),
    ("chromatin", 4), ("receptor", 3), ("synapse", 3), ("axon", 3), ("dendrite", 3),

    # --- Technology ---
    ("computer", 1), ("software", 2), ("hardware", 2), ("algorithm", 3),
    ("database", 3), ("network", 2), ("encryption", 4), ("robot", 2),
    ("automation", 3), ("drone", 2), ("ai", 3), ("blockchain", 4), ("sensor", 2),
    ("compiler", 3), ("virtualreality", 4), ("server", 2), ("wifi", 1), ("python", 2),
    ("javascript", 3), ("interface", 2), ("debug", 2), ("kernel", 4), ("processor", 3),
    ("protocol", 3), ("simulation", 3), ("cybersecurity", 4), ("firewall", 3),
    # Added ~50 more tech terms
    ("laptop", 1), ("tablet", 1), ("smartphone", 1), ("cloud", 2), ("algorithmic", 3),
    ("encryptionkey", 4), ("bandwidth", 3), ("virtualmachine", 4), ("cache", 2), ("driver", 2),
    ("router", 2), ("modem", 2), ("firmware", 3), ("gigabyte", 2), ("terabyte", 3),
    ("pixel", 1), ("resolution", 2), ("bluetooth", 2), ("ethernet", 2), ("usb", 1),
    ("html", 1), ("css", 1), ("json", 2), ("xml", 2), ("api", 2),
    ("framework", 3), ("library", 2), ("debugger", 3), ("terminal", 2), ("script", 2),
    ("bot", 2), ("automationtool", 3), ("patch", 2), ("serverfarm", 4), ("datacenter", 3),
    ("mainframe", 3), ("virtualization", 4), ("microchip", 3), ("sensorarray", 4), ("quantumcomputer", 5),

    # --- Arts ---
    ("art", 1), ("music", 1), ("painting", 2), ("sculpture", 3), ("novel", 1),
    ("story", 1), ("film", 1), ("movie", 1), ("gallery", 2), ("museum", 2),
    # Added ~50 more arts
    ("poetry", 2), ("opera", 3), ("theater", 2), ("ballet", 3), ("graffiti", 3),
    ("installation", 4), ("sketch", 2), ("photography", 3), ("design", 2),
    ("literature", 2), ("animation", 3), ("calligraphy", 4), ("drama", 2),
    ("symphony", 3), ("chorus", 2), ("monologue", 3), ("ensemble", 3),
    ("composition", 3), ("improv", 2), ("portrait", 2), ("stilllife", 3),
    ("watercolor", 3), ("mosaic", 3), ("etching", 3), ("acrylic", 3),
    ("filmnoir", 4), ("cinematography", 4), ("setdesign", 3), ("lighting", 2),
    ("soundtrack", 2), ("score", 2), ("lyric", 2), ("verse", 2), ("chorale", 3),
    ("tapestry", 3), ("puppet", 2), ("marionette", 3), ("operahouse", 4), ("galleryopening", 4),
    ("artinstallation", 4), ("abstractpainting", 4), ("realism", 3), ("surrealism", 4), ("cubism", 4),

    # --- Food ---
    ("bread", 1), ("cheese", 1), ("meat", 1), ("fruit", 1), ("vegetable", 1),
    ("pizza", 1), ("burger", 1), ("coffee", 1), ("tea", 1), ("soup", 1),
    ("cake", 1), ("cookie", 1), ("rice", 1), ("pasta", 1),
    # Added ~50 more food
    ("sushi", 2), ("taco", 2), ("noodle", 2), ("dumpling", 3), ("hummus", 3),
    ("quinoa", 3), ("curry", 2), ("steak", 2), ("salad", 1), ("bagel", 2),
    ("burrito", 2), ("chocolate", 2), ("sausage", 2), ("oatmeal", 1),
    ("smoothie", 2), ("pancake", 1), ("lasagna", 2), ("ramen", 2), ("pudding", 2),
    ("muffin", 2), ("croissant", 2), ("waffle", 1), ("scone", 2), ("mocha", 2),
    ("latte", 2), ("espresso", 2), ("milkshake", 2), ("pie", 1), ("brownie", 2),
    ("nachos", 2), ("saag", 3), ("kimchi", 3), ("ceviche", 3), ("tempura", 3),
    ("tofu", 2), ("edamame", 2), ("tortilla", 2), ("falafel", 2), ("paella", 3),
    ("sambal", 3), ("gelato", 2), ("bruschetta", 3), ("goulash", 3), ("pierogi", 3),

    # --- Abstract ---
    ("idea", 1), ("thought", 1), ("logic", 2), ("reason", 2), ("emotion", 1),
    ("fear", 1), ("hope", 1), ("identity", 2), ("freedom", 1), ("justice", 1),
    # Added ~50 more abstract
    ("truth", 1), ("belief", 2), ("morality", 3), ("ethics", 2), ("consciousness", 4),
    ("intuition", 3), ("wisdom", 2), ("perception", 3), ("creativity", 3), ("knowledge", 2),
    ("faith", 1), ("curiosity", 2), ("imagination", 3), ("dream", 1), ("soul", 2),
    ("virtue", 3), ("vulnerability", 3), ("mind", 1), ("spirit", 2), ("empathy", 2),
    ("compassion", 2), ("anger", 1), ("jealousy", 1), ("hopefulness", 2), ("courage", 2),
    ("patience", 2), ("love", 1), ("hate", 1), ("envy", 1), ("regret", 2),
    ("optimism", 2), ("pessimism", 2), ("reflection", 2), ("impression", 2),
    ("perseverance", 2), ("adaptation", 3), ("innovation", 3), ("freethinking", 4),
    ("contemplation", 3), ("meditation", 3), ("symbolism", 3), ("metaphor", 2),
    ("altruism", 3), ("ego", 2), ("id", 2), ("superconscious", 5), ("awareness", 2),
    ("reasoning", 2), ("logicism", 4), ("ethos", 3), ("pathos", 3), ("logos", 3),

    # --- Misc / Random ---
    ("kangaroo", 3), ("zeppelin", 4), ("marshmallow", 2), ("telescope", 3),
    ("jungle", 2), ("glitch", 3), ("origami", 3), ("carnival", 2), ("puzzle", 1),
    ("labyrinth", 4), ("robotics", 3), ("astronaut", 3), ("volcanoes", 3),
    ("avalanche", 4), ("comet", 3), ("wizard", 3), ("pyramid", 2),
    # Added ~50 more misc
    ("sphinx", 3), ("unicorn", 3), ("phoenix", 4), ("dragon", 3), ("mermaid", 3),
    ("witch", 2), ("wizardry", 4), ("gnome", 3), ("elf", 3), ("fairy", 2),
    ("robotdog", 4), ("mech", 3), ("spaceship", 3), ("satellite", 3), ("laser", 2),
    ("timecapsule", 3), ("fossil", 2), ("artifact", 2), ("treasure", 2), ("scroll", 2),
    ("crystalball", 3), ("magicwand", 3), ("spellbook", 4), ("alchemy", 4), ("potion", 3),
    ("curse", 3), ("talisman", 3), ("totem", 3), ("obelisk", 4), ("monolith", 4)
]

# CATEGORY DETECTION
CATEGORY_KEYWORDS = {
    "geography": [w for (w, _) in word_list if w in [
        "city", "country", "river", "lake", "ocean", "mountain", "island", "continent",
        "desert", "forest", "valley", "canyon", "plateau", "glacier", "harbor", "coast",
        "volcano", "peninsula", "archipelago", "fjord", "delta", "savanna", "tundra",
        "bay", "reef", "strait", "Antarctica", "Australia", "Brazil", "Canada", "China",
        "Egypt", "France", "Germany", "India", "Italy", "Japan", "Kenya", "Mexico", "Norway",
        "Peru", "Russia", "Spain", "Thailand", "UK", "USA", "Vietnam", "Zimbabwe", "Argentina",
        "Belgium", "Chile", "Colombia", "Cuba", "Denmark", "Finland", "Greece", "Hungary",
        "Iceland", "Ireland", "Israel", "Jordan", "Kazakhstan", "Laos", "Lebanon", "Malaysia",
        "Morocco", "Nepal", "Netherlands", "New Zealand", "Nigeria", "North Korea", "Pakistan",
        "Poland", "Portugal", "Romania", "Saudi Arabia", "Scotland", "Senegal", "South Africa",
        "South Korea", "Sweden", "Switzerland", "Syria", "Turkey", "Ukraine",
        "United Arab Emirates", "Venezuela", "Wales", "Yemen", "Zambia", "Bhutan", "Burundi",
        "Cambodia", "Costa Rica", "El Salvador", "Ethiopia", "Ghana", "Guatemala"
    ]],
    # Repeat for other categories like before
    "science": [w for (w, _) in word_list if w in [
        "atom", "molecule", "cell", "protein", "dna", "species", "ecosystem", "gravity",
        "energy", "force", "motion", "velocity", "density", "radiation", "mutation",
        "quantum", "neuron", "enzyme", "hormone", "photosynthesis", "blackhole",
        "electron", "atomos", "chlorophyll", "galaxy", "planet", "star", "nebula",
        "comet", "voltage", "current", "magnet", "bacteria", "virus", "fungus",
        "crystal", "element", "ion", "gravitywave", "blackbody", "osmosis", "photosphere",
        "chloroplast", "ribosome", "chromosome", "mitosis", "meiosis", "plasma", "supernova",
        "paleontology", "geology", "mineral", "sediment", "volcanology", "meteorology",
        "neutron", "proton", "antimatter", "darkmatter", "fission", "fusion", "catalyst",
        "thermodynamics", "entropy", "acidity", "alkali", "isotope", "vapor", "precipitate",
        "solution", "colloid", "polymer", "crustacean", "arachnid", "mollusk", "cellulose",
        "proteinase","ligand","enzymeactivity","gene","chromatin","receptor","synapse",
        "axon","dendrite","ribosome","chloroplast","photosystem","microbe","fungicide",
        "biodiversity","taxonomy","ecology","biome","habitat","mutationrate","allele",
        "genome","chromatid","karyotype","phylogeny","botany","zoology","paleobotany",
        "geochemistry","biochemistry","nanotechnology","astrophysics","cosmology","seismology"
    ]],
    "technology": [w for (w, _) in word_list if w in [
        "computer","software","hardware","algorithm","database","network","encryption",
        "robot","automation","drone","ai","blockchain","sensor","compiler","virtualreality",
        "server","wifi","python","javascript","interface","debug","kernel","processor",
        "protocol","simulation","cybersecurity","firewall","laptop","tablet","smartphone",
        "cloud","algorithmic","encryptionkey","bandwidth","virtualmachine","cache","driver",
        "router","modem","firmware","gigabyte","terabyte","pixel","resolution","bluetooth",
        "ethernet","usb","html","css","json","xml","api","framework","library","debugger",
        "terminal","script","bot","automationtool","patch","serverfarm","datacenter",
        "mainframe","virtualization","microchip","sensorarray","quantumcomputer",
        "internet","iot","protocolstack","loadbalancer","datamining","machinelearning",
        "deeplearning","neuralnetwork","cryptography","compilerdesign","algorithmanalysis",
        "opensource","repository","git","docker","kubernetes","virtualenv"
    ]],
    "arts": [w for (w, _) in word_list if w in [
        "art","music","painting","sculpture","novel","story","film","movie","gallery",
        "museum","poetry","opera","theater","ballet","graffiti","installation","sketch",
        "photography","design","literature","animation","calligraphy","drama","symphony",
        "chorus","monologue","ensemble","composition","improv","portrait","stilllife",
        "watercolor","mosaic","etching","acrylic","filmnoir","cinematography","setdesign",
        "lighting","soundtrack","score","lyric","verse","chorale","tapestry","puppet",
        "marionette","operahouse","galleryopening","artinstallation","abstractpainting",
        "realism","surrealism","cubism","expressionism","impressionism","minimalism",
        "conceptualart","performanceart","digitalart","popart","streetart","mural","etching",
        "collage","illustration","storyboard","characterdesign"
    ]],
    "food": [w for (w, _) in word_list if w in [
        "bread","cheese","meat","fruit","vegetable","pizza","burger","coffee","tea","soup",
        "cake","cookie","rice","pasta","sushi","taco","noodle","dumpling","hummus","quinoa",
        "curry","steak","salad","bagel","burrito","chocolate","sausage","oatmeal","smoothie",
        "pancake","lasagna","ramen","pudding","muffin","croissant","waffle","scone","mocha",
        "latte","espresso","milkshake","pie","brownie","nachos","saag","kimchi","ceviche",
        "tempura","tofu","edamame","tortilla","falafel","paella","sambal","gelato","bruschetta",
        "goulash","pierogi","tapas","risotto","fondue","cevapcici","chowder","biryani","tagine",
        "pho","sashimi","mochi","dumpling","arepa","empanada","gnocchi","kebab","shawarma"
    ]],
    "abstract": [w for (w, _) in word_list if w in [
        "idea","thought","logic","reason","emotion","fear","hope","identity","freedom",
        "justice","truth","belief","morality","ethics","consciousness","intuition","wisdom",
        "perception","creativity","knowledge","faith","curiosity","imagination","dream",
        "soul","virtue","vulnerability","mind","spirit","empathy","compassion","anger",
        "jealousy","hopefulness","courage","patience","love","hate","envy","regret","optimism",
        "pessimism","reflection","impression","perseverance","adaptation","innovation",
        "freethinking","contemplation","meditation","symbolism","metaphor","altruism","ego",
        "id","superconscious","awareness","reasoning","logicism","ethos","pathos","logos",
        "mindfulness","selfesteem","concentration","focus","intuitionism","determinism","existentialism",
        "nihilism","relativism","objectivism","subjectivism","phenomenology","pragmatism"
    ]],
    "misc": [w for (w, _) in word_list if w not in [
        "city","country","river","lake","ocean","mountain","island","continent",
        "desert","forest","valley","canyon","plateau","glacier","harbor","coast",
        "volcano","peninsula","archipelago","fjord","delta","savanna","tundra",
        "bay","reef","strait","Antarctica","Australia","Brazil","Canada","China",
        "Egypt","France","Germany","India","Italy","Japan","Kenya","Mexico","Norway",
        "Peru","Russia","Spain","Thailand","UK","USA","Vietnam","Zimbabwe","Argentina",
        "Belgium","Chile","Colombia","Cuba","Denmark","Finland","Greece","Hungary",
        "Iceland","Ireland","Israel","Jordan","Kazakhstan","Laos","Lebanon","Malaysia",
        "Morocco","Nepal","Netherlands","New Zealand","Nigeria","North Korea","Pakistan",
        "Poland","Portugal","Romania","Saudi Arabia","Scotland","Senegal","South Africa",
        "South Korea","Sweden","Switzerland","Syria","Turkey","Ukraine",
        "United Arab Emirates","Venezuela","Wales","Yemen","Zambia","Bhutan","Burundi",
        "Cambodia","Costa Rica","El Salvador","Ethiopia","Ghana","Guatemala","kangaroo",
        "zeppelin","marshmallow","telescope","jungle","glitch","origami","carnival",
        "puzzle","labyrinth","robotics","astronaut","volcanoes","sphinx","unicorn",
        "phoenix","dragon","mermaid","witch","wizardry","gnome","elf","fairy","robotdog",
        "mech","spaceship","satellite","laser","timecapsule","fossil","artifact",
        "treasure","scroll","crystalball","magicwand","spellbook","alchemy","potion",
        "curse","talisman","totem","obelisk","monolith"
    ]]
}
def detect_category(word):
    """Return the category a word belongs to."""
    for cat, words in CATEGORY_KEYWORDS.items():
        if word in words:
            return cat
    return "misc"

def get_same_category_words(secret_word, difficulty):
    """
    Returns a list of words in the same category as secret_word
    that are at or below the given difficulty, excluding the secret_word itself.
    """
    category = detect_category(secret_word)
    candidates = [
        w for (w, lvl) in word_list
        if lvl <= difficulty and detect_category(w) == category and w != secret_word
    ]
    return candidates if candidates else ["BLANK"]
# question_list for question mode
question_list = [
    "What's your favorite color?",
    "If you could travel anywhere, where would you go?",
    "What's your favorite food?",
    "Do you prefer cats or dogs?",
    "What's your favorite movie?"
    # add as many as you want
]

