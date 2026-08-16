import random
import streamlit as st

st.set_page_config(page_title="ReadGenius", page_icon="📚", layout="centered")

st.title("📚 ReadGenius")
st.write("Reading comprehension, book recommendations, and phonics practice — all in one place.")

tab1, tab2, tab3 = st.tabs(["📖 Comprehension", "🔎 Book Finder", "🔤 Phonics"])

# ---------------------------------------------------------------------------
# TAB 1: Reading comprehension practice
# ---------------------------------------------------------------------------
PASSAGES = [
    {
        "title": "The Lost Kitten",
        "text": (
            "Maya heard a tiny meow coming from behind the garden shed. She crept closer "
            "and found a small grey kitten shivering in the rain. Maya wrapped the kitten "
            "in her scarf and carried it inside. Her mum gave it warm milk and a soft towel "
            "to sleep on. By morning, the kitten was purring happily on Maya's lap."
        ),
        "questions": [
            {
                "q": "Where did Maya find the kitten?",
                "options": ["In a tree", "Behind the garden shed", "In the kitchen", "Under her bed"],
                "answer": "Behind the garden shed",
            },
            {
                "q": "What did Maya wrap the kitten in?",
                "options": ["A blanket", "A towel", "Her scarf", "A jumper"],
                "answer": "Her scarf",
            },
            {
                "q": "How did the kitten feel by morning?",
                "options": ["Scared", "Hungry", "Happy and purring", "Still shivering"],
                "answer": "Happy and purring",
            },
        ],
    },
    {
        "title": "The School Fair",
        "text": (
            "Every autumn, Hillside School held a fair on the playground. There were stalls "
            "selling cakes, a coconut shy, and a raffle with a giant teddy bear as the prize. "
            "Tom spent his pocket money on three raffle tickets. He didn't win the teddy bear, "
            "but he did win a bag of sweets, which made him just as happy."
        ),
        "questions": [
            {
                "q": "What season was the fair held in?",
                "options": ["Spring", "Summer", "Autumn", "Winter"],
                "answer": "Autumn",
            },
            {
                "q": "How many raffle tickets did Tom buy?",
                "options": ["One", "Two", "Three", "Four"],
                "answer": "Three",
            },
            {
                "q": "What did Tom actually win?",
                "options": ["The teddy bear", "A bag of sweets", "Nothing", "A cake"],
                "answer": "A bag of sweets",
            },
        ],
    },
]

with tab1:
    if "passage_idx" not in st.session_state:
        st.session_state.passage_idx = random.randrange(len(PASSAGES))

    passage = PASSAGES[st.session_state.passage_idx]

    st.subheader(passage["title"])
    st.write(passage["text"])

    if st.button("🔀 New passage"):
        st.session_state.passage_idx = random.randrange(len(PASSAGES))
        st.rerun()

    st.divider()
    st.write("**Answer the questions below:**")

    score = 0
    for i, item in enumerate(passage["questions"]):
        choice = st.radio(item["q"], item["options"], index=None, key=f"q_{st.session_state.passage_idx}_{i}")
        if choice is not None:
            if choice == item["answer"]:
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Not quite — the answer is: {item['answer']}")

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
