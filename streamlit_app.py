import random
import streamlit as st

st.set_page_config(page_title="ReadGenius", page_icon="📚", layout="centered")

# ---------------------------------------------------------------------------
# Theme: library / book-cover aesthetic
# Ink navy + library green + gilt gold on a soft sage paper background.
# Body text uses Atkinson Hyperlegible — a typeface designed by the Braille
# Institute specifically for reading clarity, which fits a literacy tool.
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Atkinson+Hyperlegible:wght@400;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Atkinson Hyperlegible', sans-serif;
    }
    h1, h2, h3, .stTabs [data-baseweb="tab"] p {
        font-family: 'Fraunces', serif !important;
    }

    .rg-header {
        background: #1F2A3C;
        padding: 1.8rem 2rem 1.5rem 2rem;
        border-radius: 10px;
        margin-bottom: 1.6rem;
        border-bottom: 4px solid #C99A3E;
    }
    .rg-header h1 {
        color: #F6F4EE !important;
        font-weight: 700;
        font-size: 2.2rem;
        letter-spacing: 0.01em;
        margin: 0;
    }
    .rg-header p {
        color: #C9D1C6;
        margin: 0.4rem 0 0 0;
        font-size: 1rem;
    }

    .rg-badge {
        display: inline-block;
        border: 1.5px dashed #C99A3E;
        color: #2F5D50;
        padding: 0.15rem 0.7rem;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.03em;
        text-transform: uppercase;
        margin-bottom: 0.6rem;
    }

    .rg-card {
        background: #FFFFFF;
        border-left: 4px solid #C99A3E;
        border-radius: 6px;
        padding: 1rem 1.2rem;
        margin-top: 0.6rem;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        border-bottom: 2px solid #DDE2D8;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 8px 8px 0 0;
        padding: 0.6rem 1.2rem;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FFFFFF;
        border-bottom: 3px solid #2F5D50;
    }

    .stButton button {
        border-radius: 8px;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="rg-header">
        <h1>📚 ReadGenius</h1>
        <p>Reading comprehension, book recommendations, and phonics practice — all in one place.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

tab1, tab2, tab3 = st.tabs(["📖 Comprehension", "🔎 Book Finder", "🔤 Phonics"])

# ---------------------------------------------------------------------------
# TAB 1: Reading comprehension practice
# ---------------------------------------------------------------------------
PASSAGES = [
    {
        "title": "The Lost Kitten",
        "genre": "Animals",
        "text": (
            "Maya heard a tiny meow coming from behind the garden shed. She crept closer "
            "and found a small grey kitten shivering in the rain. Its fur was soaked and "
            "its paws were muddy, and it looked up at Maya with wide, frightened eyes. Maya "
            "wrapped the kitten in her scarf and carried it inside, keeping her steps slow so "
            "she wouldn't scare it further. Her mum gave it warm milk and a soft towel to "
            "sleep on, and together they made a cosy bed from an old shoebox by the fireplace. "
            "They checked outside for a worried owner but found no one, so they put up posters "
            "around the street just in case. By morning, the kitten was purring happily on "
            "Maya's lap, and Maya quietly hoped that nobody would come to claim it."
        ),
        "phonics_focus": ["sh", "ee"],
        "phonics_words": ["shed", "sheep", "shivering", "sleep"],
        "questions": [
            {"q": "Where did Maya find the kitten?",
             "options": ["In a tree", "Behind the garden shed", "In the kitchen", "Under her bed"],
             "answer": "Behind the garden shed"},
            {"q": "What did Maya wrap the kitten in?",
             "options": ["A blanket", "A towel", "Her scarf", "A jumper"],
             "answer": "Her scarf"},
            {"q": "How did the kitten feel by morning?",
             "options": ["Scared", "Hungry", "Happy and purring", "Still shivering"],
             "answer": "Happy and purring"},
        ],
    },
    {
        "title": "The School Fair",
        "genre": "Friendship",
        "text": (
            "Every autumn, Hillside School held a fair on the playground, and the whole school "
            "looked forward to it for weeks. There were stalls selling cakes, a coconut shy, "
            "a bouncy castle, and a raffle with a giant teddy bear as the prize. Tom spent his "
            "pocket money on three raffle tickets, hoping his name would be pulled out of the "
            "big glass jar. His best friend Priya crossed her fingers for him the whole time "
            "the numbers were being called. When the winning ticket was read out, it wasn't "
            "Tom's number after all — he didn't win the teddy bear. But moments later, he won "
            "a bag of sweets from the tombola stall instead, and he happily shared them with "
            "Priya on the walk home, which made the day feel just as good as winning."
        ),
        "phonics_focus": ["ea", "ai"],
        "phonics_words": ["each", "autumn", "raffle", "sweets"],
        "questions": [
            {"q": "What season was the fair held in?",
             "options": ["Spring", "Summer", "Autumn", "Winter"],
             "answer": "Autumn"},
            {"q": "How many raffle tickets did Tom buy?",
             "options": ["One", "Two", "Three", "Four"],
             "answer": "Three"},
            {"q": "What did Tom actually win?",
             "options": ["The teddy bear", "A bag of sweets", "Nothing", "A cake"],
             "answer": "A bag of sweets"},
        ],
    },
    {
        "title": "The Dragon's Cave",
        "genre": "Fantasy",
        "text": (
            "High on the misty mountain, a small dragon named Ember lived alone in a cave. "
            "Most of the villagers below believed dragons were dangerous, so nobody ever "
            "climbed up to visit her. Every night she would sigh, wishing for a friend to "
            "share her stories with. One evening, a lost hiker named Finn stumbled into her "
            "cave to escape the pouring rain, his torch flickering weakly in the dark. Ember "
            "froze, unsure whether to hide or say hello. Finn, surprised but curious, offered "
            "her a slice of his bread instead of running away. They talked until the storm "
            "passed, and Finn promised to keep her cave a secret. From that night on, Ember "
            "and Finn met at the cave whenever the moon was bright, and the mountain no "
            "longer felt so quiet."
        ),
        "phonics_focus": ["oa", "igh"],
        "phonics_words": ["moan", "high", "night", "bright", "light"],
        "questions": [
            {"q": "Where did Ember live?",
             "options": ["In a forest", "In a cave", "In a castle", "By the sea"],
             "answer": "In a cave"},
            {"q": "Why did Finn come into the cave?",
             "options": ["He was exploring", "To escape the rain", "He was looking for Ember", "He was lost forever"],
             "answer": "To escape the rain"},
            {"q": "What did Finn offer Ember?",
             "options": ["Gold", "A map", "A slice of bread", "A blanket"],
             "answer": "A slice of bread"},
        ],
    },
    {
        "title": "The Missing Trophy",
        "genre": "Mystery",
        "text": (
            "The football trophy had vanished from the school cabinet overnight, and Mr Patel "
            "was determined to find out who had taken it. Three pupils were seen near the "
            "hall that morning: Ola, who had football practice; Sam, who was collecting props "
            "for the play; and Bea, who said she was just tying her shoelace. Ola noticed muddy "
            "footprints leading from the hall to the sports cupboard. Inside, wrapped carefully "
            "in a spare kit bag, was the trophy. It turned out the caretaker had moved it to "
            "polish the shelf and simply forgotten to put it back before going home for the "
            "evening."
        ),
        "phonics_focus": ["or", "ur"],
        "phonics_words": ["morning", "sports", "turned", "further"],
        "questions": [
            {"q": "Who was determined to solve the mystery?",
             "options": ["Ola", "Sam", "Bea", "Mr Patel"],
             "answer": "Mr Patel"},
            {"q": "What clue led to the trophy?",
             "options": ["A note", "Muddy footprints", "A photograph", "A witness"],
             "answer": "Muddy footprints"},
            {"q": "Who had actually moved the trophy?",
             "options": ["Ola", "Sam", "The caretaker", "Bea"],
             "answer": "The caretaker"},
        ],
    },
    {
        "title": "The Class Assembly",
        "genre": "Funny",
        "text": (
            "Year 4 were putting on an assembly about the water cycle, and Charlie had been "
            "given the important role of Cloud Number Two. He practised his one line all week: "
            "\"I am a cloud, full of rain, ready to fall again.\" On the big day, Charlie walked "
            "on stage in his cotton-wool costume, opened his mouth, and completely forgot the "
            "words. Instead, he shouted, \"I am a cloud... and I am VERY fluffy!\" The whole hall "
            "burst out laughing, including the teachers, and a few even wiped away tears from "
            "laughing so hard. Charlie went bright red at first, but soon he was laughing too. "
            "Afterwards, everyone agreed it was the best assembly they had ever seen."
        ),
        "phonics_focus": ["ow", "ch"],
        "phonics_words": ["cloud", "shout", "cotton", "much"],
        "questions": [
            {"q": "What was the assembly about?",
             "options": ["Space", "The water cycle", "Animals", "History"],
             "answer": "The water cycle"},
            {"q": "What role did Charlie play?",
             "options": ["The sun", "A raindrop", "Cloud Number Two", "The narrator"],
             "answer": "Cloud Number Two"},
            {"q": "What did Charlie shout instead of his line?",
             "options": ["\"I forgot my line!\"", "\"I am a cloud... and I am VERY fluffy!\"", "Nothing at all", "\"Where is my costume?\""],
             "answer": "\"I am a cloud... and I am VERY fluffy!\""},
        ],
    },
    {
        "title": "Diving with Dolphins",
        "genre": "Nature",
        "text": (
            "Off the coast of a small fishing village, a pod of dolphins swam close to shore "
            "every summer. Marine scientist Dr Osei had studied this pod for over ten years, "
            "learning to recognise each dolphin by the shape of its fin. Her favourite, a "
            "curious young dolphin named Pearl, often swam alongside the research boat. One "
            "afternoon, Pearl led the boat towards a tangled fishing net caught on some rocks. "
            "Dr Osei realised a young seal was trapped inside. Working carefully, her team "
            "freed the seal within minutes. Dr Osei always said that Pearl seemed to understand "
            "far more than anyone gave dolphins credit for, and this day proved her right. The "
            "story was later shared in the village school, inspiring pupils to learn more about "
            "protecting sea life near their own coastline."
        ),
        "phonics_focus": ["oi", "ar"],
        "phonics_words": ["coast", "point", "marine", "far"],
        "questions": [
            {"q": "What was Dr Osei's job?",
             "options": ["Fisherwoman", "Marine scientist", "Teacher", "Sailor"],
             "answer": "Marine scientist"},
            {"q": "How did Dr Osei recognise individual dolphins?",
             "options": ["By their colour", "By the shape of their fin", "By their size", "By counting them"],
             "answer": "By the shape of their fin"},
            {"q": "What had Pearl led the boat towards?",
             "options": ["A shipwreck", "A trapped seal in a net", "Another pod of dolphins", "A storm"],
             "answer": "A trapped seal in a net"},
        ],
    },
    {
        "title": "The Treasure Map",
        "genre": "Adventure",
        "text": (
            "Rosa found the old map tucked inside a battered tin box while clearing out her "
            "grandad's attic. The paper was yellow and crumbling at the edges, but the "
            "drawing was still clear: a winding path from the old lighthouse, past three "
            "twisted oak trees, and down to a mark labelled simply 'X'. Rosa's grandad had "
            "always told stories about a treasure hidden somewhere near the coast when he was "
            "a boy, though nobody in the family had ever believed him. Curious, Rosa packed a "
            "torch, a bottle of water, and the map into her rucksack and set off along the "
            "cliff path the very next morning. The lighthouse was easy to find, standing tall "
            "and white against the grey sky, but the three oak trees took much longer to spot, "
            "hidden behind a thick tangle of brambles. After nearly giving up, Rosa noticed "
            "three trunks growing close together further down the slope. She counted forty "
            "paces from the middle tree, just as the map instructed, and began to dig where "
            "the ground felt slightly softer than the rest. Her spade struck something solid. "
            "Carefully brushing away the soil, Rosa uncovered a small rusted box. Inside, "
            "instead of gold, she found a bundle of old photographs and a letter written in "
            "her grandad's handwriting, describing the very same walk he had taken as a boy. "
            "Rosa realised the real treasure had never been gold at all — it was a piece of "
            "her grandad's childhood, waiting patiently for someone to find it."
        ),
        "phonics_focus": ["oa", "ai"],
        "phonics_words": ["coast", "road", "paces", "trail"],
        "questions": [
            {"q": "Where did Rosa find the old map?",
             "options": ["In a drawer", "In a tin box in the attic", "On the beach", "In a library book"],
             "answer": "In a tin box in the attic"},
            {"q": "What landmark helped Rosa find the oak trees?",
             "options": ["A church", "The old lighthouse", "A bridge", "A farmhouse"],
             "answer": "The old lighthouse"},
            {"q": "What did Rosa actually find in the box?",
             "options": ["Gold coins", "Jewels", "Old photographs and a letter", "Nothing at all"],
             "answer": "Old photographs and a letter"},
        ],
    },
    {
        "title": "The Great Fire of London",
        "genre": "History",
        "text": (
            "In September 1666, a small fire broke out in a bakery on Pudding Lane in London. "
            "At first, it seemed like nothing unusual — fires were common in a city built mostly "
            "of wood and thatch, packed tightly together along narrow streets. But that summer "
            "had been unusually dry, and a strong wind soon carried the flames from house to "
            "house. Firefighting in those days meant forming a line of people passing buckets "
            "of water, or pulling down buildings to stop the fire from spreading further, but "
            "neither method could keep up with the speed of the blaze. Within hours the fire "
            "had grown far beyond anyone's control. People rushed to save what belongings they "
            "could, loading carts and boats with furniture, clothes and food, while others fled "
            "on foot carrying whatever they could hold. The fire burned for four days, "
            "destroying thousands of homes, dozens of churches, and many important buildings, "
            "including the old St Paul's Cathedral, whose roof was said to have melted in the "
            "heat. Remarkably, official records from the time show that very few people died, "
            "although many historians believe the true number may never be fully known. "
            "Afterwards, King Charles II ordered that the city be rebuilt using brick and stone "
            "instead of wood, a change that made London much safer from fire in the years that "
            "followed. Streets were also widened to stop flames leaping so easily from building "
            "to building. Many of the streets and buildings we can still visit in London today "
            "were shaped by decisions made in the months after the fire, making it one of the "
            "most important turning points in the city's history."
        ),
        "phonics_focus": ["th", "wh"],
        "phonics_words": ["thatch", "within", "wheat", "when"],
        "questions": [
            {"q": "Where did the fire start?",
             "options": ["A church", "A bakery on Pudding Lane", "A wooden bridge", "The Tower of London"],
             "answer": "A bakery on Pudding Lane"},
            {"q": "How many days did the fire burn for?",
             "options": ["One", "Two", "Four", "Seven"],
             "answer": "Four"},
            {"q": "What material was London mostly rebuilt with afterwards?",
             "options": ["Wood", "Brick and stone", "Straw", "Metal"],
             "answer": "Brick and stone"},
        ],
    },
    {
        "title": "The Robot Who Couldn't Dance",
        "genre": "Funny",
        "text": (
            "Bolt was the newest robot at Sunnydale Robotics Academy, built to be faster and "
            "stronger than any robot before him. He could lift ten times his own weight, run "
            "at incredible speed, and solve puzzles that stumped even the senior robots. But "
            "there was one thing Bolt simply could not do: dance. Every time music played, his "
            "joints locked up and he would wobble stiffly like a broken toy, arms swinging in "
            "the wrong direction entirely. The other robots giggled, though never unkindly, "
            "and Bolt tried to laugh along even though it stung a little each time. At the end "
            "of term, the Academy always held a Founders Day show, where every robot performed "
            "something to celebrate the school's history. Bolt dreaded the thought of wobbling "
            "in front of the whole audience. Determined to improve, he spent every evening in "
            "the empty practice hall long after the other robots had powered down, watching "
            "videos of dancers and copying their moves one tiny step at a time. At first "
            "nothing seemed to change, and some nights he wanted to give up entirely. But weeks "
            "passed, and slowly his movements grew smoother, his timing sharper, and his "
            "confidence steadier. On the night of the show, Bolt walked on stage expecting to "
            "wobble as usual, his circuits buzzing with nerves. Instead, when the music "
            "started, something clicked into place. He spun, dipped and slid across the floor "
            "perfectly, as though he had been dancing his whole life. The whole audience "
            "cheered, and even the strictest teachers were seen tapping their feet. Afterwards, "
            "Bolt realised that even the stiffest beginner can become brilliant with enough "
            "practice and a little patience, and he never dreaded Founders Day again."
        ),
        "phonics_focus": ["oo", "ea"],
        "phonics_words": ["academy", "smoother", "weeks", "cheered"],
        "questions": [
            {"q": "What could Bolt not do at first?",
             "options": ["Lift heavy things", "Run fast", "Dance", "Speak"],
             "answer": "Dance"},
            {"q": "How did Bolt try to improve?",
             "options": ["He asked another robot to teach him", "He watched videos and practised every evening", "He gave up", "He built a new body"],
             "answer": "He watched videos and practised every evening"},
            {"q": "What happened at the Founders Day show?",
             "options": ["Bolt wobbled again", "Bolt danced perfectly", "Bolt broke down", "Bolt refused to perform"],
             "answer": "Bolt danced perfectly"},
        ],
    },
]

# Compute word counts automatically so filters stay accurate even if text changes
for p in PASSAGES:
    p["word_count"] = len(p["text"].split())

GENRES = ["Any"] + sorted({p["genre"] for p in PASSAGES})

with tab1:
    st.write("**Choose a genre and text length to find a suitable passage.**")

    col1, col2 = st.columns(2)
    with col1:
        genre_choice = st.selectbox("Genre", GENRES)
    with col2:
        length_range = st.select_slider(
            "Text length (words)",
            options=[100, 150, 200, 250, 300, 350],
            value=(100, 350),
        )

    filtered = [
        p for p in PASSAGES
        if (genre_choice == "Any" or p["genre"] == genre_choice)
        and length_range[0] <= p["word_count"] <= length_range[1]
    ]

    st.caption(f"{len(filtered)} passage(s) match this genre and length range.")

    if not filtered:
        st.warning("No passages match — try widening the length range or choosing 'Any' genre.")
    else:
        # Keep the chosen passage stable until "New passage" is clicked, or filters change the pool
        filtered_titles = tuple(p["title"] for p in filtered)
        if (
            "current_title" not in st.session_state
            or st.session_state.current_title not in filtered_titles
        ):
            st.session_state.current_title = random.choice(filtered_titles)

        if st.button("🔀 New passage from this selection"):
            st.session_state.current_title = random.choice(filtered_titles)
            st.rerun()

        passage = next(p for p in filtered if p["title"] == st.session_state.current_title)

        st.subheader(passage["title"])
        st.markdown(
            f'<span class="rg-badge">{passage["genre"]} · {passage["word_count"]} words</span>',
            unsafe_allow_html=True,
        )
        st.write(passage["text"])

        st.divider()
        st.write("**Answer the questions below:**")

        for i, item in enumerate(passage["questions"]):
            choice = st.radio(
                item["q"], item["options"], index=None,
                key=f"q_{passage['title']}_{i}",
            )
            if choice is not None:
                if choice == item["answer"]:
                    st.success("Correct!")
                else:
                    st.error(f"Not quite — the answer is: {item['answer']}")

        st.divider()
        phonics_sounds = ", ".join(f"<code>{s}</code>" for s in passage["phonics_focus"])
        phonics_words_html = ", ".join(f"<strong>{w}</strong>" for w in passage["phonics_words"])
        st.markdown(
            f"""
            <div class="rg-card">
                <strong>🔤 Phonics focus for this text</strong><br>
                This passage practises the sounds: {phonics_sounds}<br><br>
                Spot these sounds in words from the passage:<br>
                {phonics_words_html}
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("Ask pupils to find and read these words aloud in the passage above, or spot other words with the same sounds.")

# ---------------------------------------------------------------------------
# TAB 2: Book recommendations
# ---------------------------------------------------------------------------
BOOK_LIBRARY = {
    ("Adventure", "5-7"): ["The Owl Who Was Afraid of the Dark", "Winnie the Witch"],
    ("Adventure", "8-11"): ["The Girl Who Drank the Moon", "Percy Jackson: The Lightning Thief"],
    ("Animals", "5-7"): ["The Tiger Who Came to Tea", "Dear Zoo"],
    ("Animals", "8-11"): ["The One and Only Ivan", "Varjak Paw"],
    ("Funny", "5-7"): ["Mr Gum", "Aliens Love Underpants"],
    ("Funny", "8-11"): ["The Boy in the Dress", "Diary of a Wimpy Kid"],
    ("Mystery", "5-7"): ["Winnie and Wilbur: The Big Book", "Mixed-Up Fairy Tales"],
    ("Mystery", "8-11"): ["The London Eye Mystery", "Nancy Parker's Diary of Detection"],
}

with tab2:
    st.subheader("Find the right book")
    st.write("Answer two quick questions to get book suggestions.")

    age_group = st.selectbox("Age group", ["5-7", "8-11"])
    genre = st.selectbox("What do they enjoy?", ["Adventure", "Animals", "Funny", "Mystery"])

    if st.button("Find books"):
        results = BOOK_LIBRARY.get((genre, age_group), [])
        st.write(f"**Recommended for {genre} fans, ages {age_group}:**")
        for book in results:
            st.write(f"- {book}")

# ---------------------------------------------------------------------------
# TAB 3: Phonics practice
# ---------------------------------------------------------------------------
PHONICS_WORDS = [
    {"word": "cat", "sounds": ["c", "a", "t"]},
    {"word": "ship", "sounds": ["sh", "i", "p"]},
    {"word": "dream", "sounds": ["d", "r", "ea", "m"]},
    {"word": "night", "sounds": ["n", "igh", "t"]},
    {"word": "frog", "sounds": ["f", "r", "o", "g"]},
]

with tab3:
    st.subheader("Sound it out")
    if "phonics_idx" not in st.session_state:
        st.session_state.phonics_idx = random.randrange(len(PHONICS_WORDS))

    current = PHONICS_WORDS[st.session_state.phonics_idx]

    st.write("**Sound out the word, then check your answer.**")
    st.markdown(f"## {current['word']}")

    if st.button("🔀 New word"):
        st.session_state.phonics_idx = random.randrange(len(PHONICS_WORDS))
        st.rerun()

    if st.toggle("Show sound breakdown"):
        st.write(" — ".join(current["sounds"]))
        st.caption(f"{len(current['sounds'])} sounds in this word")
