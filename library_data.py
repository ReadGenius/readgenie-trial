import streamlit as st
from library_data import LIBRARY

st.set_page_config(page_title="ReadGenius", page_icon="📚", layout="centered")

# ---------------------------------------------------------------------------
# Theme: library / book-cover aesthetic
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
    .rg-header h1 { color: #F6F4EE !important; font-weight: 700; font-size: 2.2rem; margin: 0; }
    .rg-header p { color: #C9D1C6; margin: 0.4rem 0 0 0; font-size: 1rem; }

    .rg-badge {
        display: inline-block; border: 1.5px dashed #C99A3E; color: #2F5D50;
        padding: 0.15rem 0.7rem; border-radius: 999px; font-size: 0.8rem;
        font-weight: 700; letter-spacing: 0.03em; text-transform: uppercase; margin-bottom: 0.6rem;
    }
    .rg-card {
        background: #FFFFFF; border-left: 4px solid #C99A3E; border-radius: 6px;
        padding: 1rem 1.2rem; margin-top: 0.6rem; margin-bottom: 0.8rem;
    }
    .rg-passage {
        background: #FFFFFF; border-left: 4px solid #2F5D50; border-radius: 6px;
        padding: 1.1rem 1.3rem; font-size: 1.05rem; line-height: 1.85; margin-bottom: 1rem;
    }
    .rg-hw {
        background: #FAEEDA; color: #8A5A0B; border-radius: 3px; padding: 1px 5px;
        font-weight: 700; border-bottom: 2px dashed #C99A3E;
    }
    .rg-vipbadge {
        display: inline-block; padding: 3px 10px; border-radius: 6px;
        font-size: 12px; font-weight: 700; margin-bottom: 8px;
    }
    .vb-V { background: #FAEEDA; color: #854F0B; }
    .vb-I { background: #EEEDFE; color: #3C3489; }
    .vb-P { background: #FBEAF0; color: #993556; }
    .vb-E { background: #E6F1FB; color: #0C447C; }
    .vb-R { background: #EAF3DE; color: #3B6D11; }

    .rg-phonicslink {
        background: #F6F4EE; border: 1.5px dashed #2F5D50; border-radius: 6px;
        padding: 0.7rem 1rem; margin: 0.5rem 0 1rem 0; font-size: 0.92rem;
    }
    .rg-progress-label { font-size: 0.85rem; color: #5F5E5A; margin-bottom: 0.3rem; }

    .stTabs [data-baseweb="tab-list"] { gap: 4px; border-bottom: 2px solid #DDE2D8; }
    .stTabs [data-baseweb="tab"] { background-color: transparent; border-radius: 8px 8px 0 0; padding: 0.6rem 1.2rem; }
    .stTabs [aria-selected="true"] { background-color: #FFFFFF; border-bottom: 3px solid #2F5D50; }
    .stButton button { border-radius: 8px; font-weight: 700; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="rg-header">
        <h1>📚 ReadGenius</h1>
        <p>Build a reading activity, then launch it for your pupils.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

VIP_LABELS = [
    ("V", "Vocabulary", "vb-V"),
    ("I", "Infer", "vb-I"),
    ("P", "Predict", "vb-P"),
    ("E", "Explain", "vb-E"),
    ("R", "Retrieve", "vb-R"),
]

# ---------------------------------------------------------------------------
# Default demo content — preloaded so the builder is useful immediately
# ---------------------------------------------------------------------------
DEFAULT_TITLE = "The Mystery of the Old Mill"
DEFAULT_SUBTITLE = "A reading adventure · Year 3"
DEFAULT_PASSAGE = (
    "Layla and her dog Pepper raced down the muddy path towards the old mill. The mill "
    "had stood at the edge of the village for hundreds of years, but nobody went near it "
    "any more. Rumours said that strange lights flickered in the windows at night.\n\n"
    "\"I'm not nervous,\" Layla told Pepper, even though her hands were trembling.\n\n"
    "Pepper sniffed the air and let out a low growl. Then Layla saw it — a faint glow "
    "coming from behind the mill's broken door. She took a deep breath and stepped "
    "cautiously forward.\n\n"
    "Inside, the floor was covered in old straw and crumbling stone. In the corner sat a "
    "small wooden box, glowing with a soft golden light. Layla knelt down and slowly "
    "opened the lid."
)
DEFAULT_VOCAB = [
    ("nervous", "Scared or worried about something that might happen."),
    ("trembling", "Shaking quickly with small movements — often because of cold or fear."),
    ("cautiously", "Moving carefully and quietly, watching out for danger."),
    ("crumbling", "Falling apart or breaking into small pieces over time."),
]
DEFAULT_PHONICS = [
    {
        "prompt": 'Look at the word "crumbling" — which part makes the short /u/ sound?',
        "tiles": ["cr", "u", "mb", "ling"],
        "correct": 1,
        "expl": 'cr-u-mb-ling — the letter "u" spells the short /u/ sound.',
    },
    {
        "prompt": 'Which word uses the "igh" trigraph (three letters, one sound)?',
        "tiles": ["light", "mill", "straw", ""],
        "correct": 0,
        "expl": '"l-igh-t" — the letters "igh" together spell the long /ai/ sound, as in night, right, fight.',
    },
]
DEFAULT_VIPERS = [
    {
        "q": "Which word in the story tells us the light wasn't very bright?",
        "opts": ["glowing", "faint", "golden", "soft"],
        "correct": 1,
        "fb": '"Faint" means dim or not very strong. Look for describing words the writer uses to create atmosphere.',
    },
    {
        "q": "Layla says \"I'm not nervous\" but her hands are trembling. What does this tell us about her?",
        "opts": ["She isn't scared at all.", "She's trying to be brave but is actually scared.",
                 "She is cold from the weather.", "She is angry with Pepper."],
        "correct": 1,
        "fb": "Layla is saying one thing but her body is doing another — writers do this to show what a character really feels inside.",
    },
    {
        "q": "Layla slowly opens the lid. What do you think is most likely inside the glowing box?",
        "opts": ["A sandwich", "An old map or hidden treasure", "A mobile phone", "Some mud"],
        "correct": 1,
        "fb": "A map or treasure fits the clues — a mysterious glowing box in an old mill sounds like a discovery! Use what you know about mystery stories to predict.",
    },
    {
        "q": "Why did nobody go near the mill any more? Find the reason from the text.",
        "opts": ["It was too far from the village.", "It was too busy inside.",
                 "Rumours about strange lights scared people away.", "The door was locked."],
        "correct": 2,
        "fb": 'The text says "Rumours said that strange lights flickered in the windows at night" — that\'s what kept people away. Always look for evidence directly in the text.',
    },
    {
        "q": "What did the writer say covered the floor inside the mill?",
        "opts": ["Old straw and crumbling stone", "Mud and broken glass",
                 "A wooden box and a window", "Rumours and old doors"],
        "correct": 0,
        "fb": 'The text says "the floor was covered in old straw and crumbling stone." Retrieve questions have their answer word-for-word in the text.',
    },
]

# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------
if "rg_view" not in st.session_state:
    st.session_state.rg_view = "teacher"
if "n_vocab" not in st.session_state:
    st.session_state.n_vocab = len(DEFAULT_VOCAB)
if "n_phonics" not in st.session_state:
    st.session_state.n_phonics = len(DEFAULT_PHONICS)
if "n_vipers" not in st.session_state:
    st.session_state.n_vipers = len(DEFAULT_VIPERS)
if "loaded_from_library" not in st.session_state:
    st.session_state.loaded_from_library = False

def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

tab1, tab2, tab3 = st.tabs(["🏗️ Activity Builder", "🔎 Book Finder", "🔤 Quick Phonics"])

# ===========================================================================
# TAB 1: Activity Builder (teacher form + pupil flow)
# ===========================================================================
with tab1:

    # -----------------------------------------------------------------
    # TEACHER VIEW
    # -----------------------------------------------------------------
    if st.session_state.rg_view == "teacher":
        st.subheader("Start from the text library, or write your own")
        source_mode = st.radio(
            "Source", ["📚 Browse text library", "✍️ Write your own passage"],
            horizontal=True, label_visibility="collapsed",
        )

        if source_mode == "📚 Browse text library":
            years = ["Any"] + sorted({p["year"] for p in LIBRARY})
            genres = ["Any"] + sorted({p["genre"] for p in LIBRARY})

            fc1, fc2, fc3 = st.columns(3)
            year_choice = fc1.selectbox("Year group", years)
            genre_choice = fc2.selectbox("Genre", genres)
            length_choice = fc3.selectbox("Text length", ["Any", "~100 words", "~200 words", "~300 words", "~400 words"])

            def bucket(wc):
                return min([100, 200, 300, 400], key=lambda b: abs(b - wc))

            length_map = {"~100 words": 100, "~200 words": 200, "~300 words": 300, "~400 words": 400}

            matches = [
                p for p in LIBRARY
                if (year_choice == "Any" or p["year"] == year_choice)
                and (genre_choice == "Any" or p["genre"] == genre_choice)
                and (length_choice == "Any" or bucket(p["word_count"]) == length_map[length_choice])
            ]

            st.caption(f"{len(matches)} text(s) match.")

            if not matches:
                st.warning("No texts match that combination yet — try widening your filters. The library is still growing.")
            else:
                titles = [f"{p['title']} ({p['year']} · {p['genre']} · {p['word_count']}w)" for p in matches]
                pick = st.selectbox("Choose a text", titles)
                chosen = matches[titles.index(pick)]

                st.markdown(f'<div class="rg-passage">{chosen["text"].replace(chr(10)+chr(10), "<br><br>")}</div>', unsafe_allow_html=True)

                sounds = ", ".join(f"`{s}`" for s in chosen["phonics_focus"])
                words = ", ".join(f"**{w}**" for w in chosen["phonics_words"])
                st.markdown(
                    f'<div class="rg-phonicslink">🔤 <strong>Phonics link for this text:</strong> practises {sounds}<br>'
                    f'Example words to spot: {words}</div>',
                    unsafe_allow_html=True,
                )

                if st.button("📥 Load this text into the builder", type="primary"):
                    st.session_state.t_title = chosen["title"]
                    st.session_state.t_subtitle = f"{chosen['year']} · {chosen['genre']}"
                    st.session_state.t_passage = chosen["text"]
                    st.session_state.n_vocab = len(chosen["vocab"])
                    for i, (w, d) in enumerate(chosen["vocab"]):
                        st.session_state[f"vocab_word_{i}"] = w
                        st.session_state[f"vocab_def_{i}"] = d
                    st.session_state.n_phonics = 0
                    st.session_state.n_vipers = 0
                    st.session_state.loaded_from_library = True
                    st.rerun()

            st.markdown("---")
            st.caption("Once loaded below, add your own phonics tile questions and VIPERS comprehension questions for this text, then launch.")

        st.subheader("1. Activity details")
        st.text_input("Story / activity title", value=DEFAULT_TITLE, key="t_title")
        st.text_input("Pupil-facing subtitle (optional)", value=DEFAULT_SUBTITLE, key="t_subtitle")

        st.subheader("2. Reading passage")
        st.caption("100–150 words works well for intervention groups.")
        st.text_area("Passage text", value=DEFAULT_PASSAGE, height=200, key="t_passage")

        st.subheader("3. Vocabulary words")
        st.caption("Pupils will be able to tap these words to reveal a definition.")
        for i in range(st.session_state.n_vocab):
            c1, c2 = st.columns([1, 2])
            default_w = DEFAULT_VOCAB[i][0] if i < len(DEFAULT_VOCAB) else ""
            default_d = DEFAULT_VOCAB[i][1] if i < len(DEFAULT_VOCAB) else ""
            c1.text_input(f"Word {i+1}", value=default_w, key=f"vocab_word_{i}")
            c2.text_input(f"Definition {i+1}", value=default_d, key=f"vocab_def_{i}")
        vc1, vc2 = st.columns(2)
        if vc1.button("+ Add vocabulary word"):
            st.session_state.n_vocab += 1
            st.rerun()
        if st.session_state.n_vocab > 0 and vc2.button("− Remove last word"):
            st.session_state.n_vocab -= 1
            st.rerun()

        st.subheader("4. Phonics questions")
        st.caption("Up to 3. Pupils pick the correct tile from up to 4 options.")
        for i in range(st.session_state.n_phonics):
            with st.container():
                st.markdown(f"**Phonics question {i+1}**")
                dp = DEFAULT_PHONICS[i] if (i < len(DEFAULT_PHONICS) and not st.session_state.loaded_from_library) else {"prompt": "", "tiles": ["", "", "", ""], "correct": 0, "expl": ""}
                st.text_input("Prompt", value=dp["prompt"], key=f"ph_prompt_{i}")
                tc = st.columns(4)
                for t in range(4):
                    tile_val = dp["tiles"][t] if t < len(dp["tiles"]) else ""
                    tc[t].text_input(f"Tile {t+1}", value=tile_val, key=f"ph_tile_{i}_{t}")
                st.radio("Correct tile", options=[0, 1, 2, 3], format_func=lambda x: f"Tile {x+1}",
                          index=dp["correct"], key=f"ph_correct_{i}", horizontal=True)
                st.text_input("Explanation shown after answering", value=dp["expl"], key=f"ph_expl_{i}")
                st.divider()
        pc1, pc2 = st.columns(2)
        if st.session_state.n_phonics < 3 and pc1.button("+ Add phonics question"):
            st.session_state.n_phonics += 1
            st.rerun()
        if st.session_state.n_phonics > 0 and pc2.button("− Remove last phonics question"):
            st.session_state.n_phonics -= 1
            st.rerun()

        st.subheader("5. Comprehension questions (VIPERS)")
        st.caption("Up to 5 — Vocabulary, Infer, Predict, Explain, Retrieve.")
        for i in range(st.session_state.n_vipers):
            letter, label, cls = VIP_LABELS[i % 5]
            with st.container():
                st.markdown(
                    f'<span class="rg-vipbadge {cls}">{letter} – {label}</span>',
                    unsafe_allow_html=True,
                )
                dv = DEFAULT_VIPERS[i] if (i < len(DEFAULT_VIPERS) and not st.session_state.loaded_from_library) else {"q": "", "opts": ["", "", "", ""], "correct": 0, "fb": ""}
                st.text_area("Question", value=dv["q"], key=f"vip_q_{i}", height=68)
                oc = st.columns(2)
                for o in range(4):
                    oc[o % 2].text_input(f"Option {chr(65+o)}", value=dv["opts"][o], key=f"vip_opt_{i}_{o}")
                st.selectbox("Correct option", options=[0, 1, 2, 3],
                              format_func=lambda x: f"Option {chr(65+x)}",
                              index=dv["correct"], key=f"vip_correct_{i}")
                st.text_area("Feedback / explanation", value=dv["fb"], key=f"vip_fb_{i}", height=68)
                st.divider()
        ec1, ec2 = st.columns(2)
        if st.session_state.n_vipers < 5 and ec1.button("+ Add comprehension question"):
            st.session_state.n_vipers += 1
            st.rerun()
        if st.session_state.n_vipers > 0 and ec2.button("− Remove last comprehension question"):
            st.session_state.n_vipers -= 1
            st.rerun()

        st.markdown("---")
        if st.button("▶ Launch pupil activity", type="primary"):
            # Collect everything into one activity object, mirroring a real launch
            vocab = []
            for i in range(st.session_state.n_vocab):
                w = st.session_state.get(f"vocab_word_{i}", "").strip()
                d = st.session_state.get(f"vocab_def_{i}", "").strip()
                if w and d:
                    vocab.append((w, d))

            phonics = []
            for i in range(st.session_state.n_phonics):
                prompt = st.session_state.get(f"ph_prompt_{i}", "").strip()
                tiles = [st.session_state.get(f"ph_tile_{i}_{t}", "").strip() for t in range(4)]
                tiles = [t for t in tiles if t]
                correct = st.session_state.get(f"ph_correct_{i}", 0)
                expl = st.session_state.get(f"ph_expl_{i}", "").strip()
                if prompt and tiles:
                    phonics.append({"prompt": prompt, "tiles": tiles, "correct": correct, "expl": expl})

            vipers = []
            for i in range(st.session_state.n_vipers):
                q = st.session_state.get(f"vip_q_{i}", "").strip()
                opts = [st.session_state.get(f"vip_opt_{i}_{o}", "").strip() for o in range(4)]
                correct = st.session_state.get(f"vip_correct_{i}", 0)
                fb = st.session_state.get(f"vip_fb_{i}", "").strip()
                letter, label, cls = VIP_LABELS[i % 5]
                if q and all(opts):
                    vipers.append({"q": q, "opts": opts, "correct": correct, "fb": fb, "label": f"{letter} – {label}", "cls": cls})

            st.session_state.activity = {
                "title": st.session_state.get("t_title", "Reading Activity"),
                "subtitle": st.session_state.get("t_subtitle", ""),
                "passage": st.session_state.get("t_passage", ""),
                "vocab": vocab,
                "phonics": phonics,
                "vipers": vipers,
            }
            st.session_state.rg_view = "pupil"
            st.session_state.pupil_stage = "intro"
            st.session_state.score = {"ph": 0, "vi": 0}
            st.session_state.ph_idx = 0
            st.session_state.vip_idx = 0
            st.session_state.revealed_word = None
            st.session_state.answered_ph = {}
            st.session_state.answered_vip = {}
            st.rerun()

    # -----------------------------------------------------------------
    # PUPIL VIEW
    # -----------------------------------------------------------------
    else:
        activity = st.session_state.activity
        top_l, top_r = st.columns([4, 1])
        top_l.markdown(f"### {esc(activity['title'])}")
        if top_r.button("← Teacher view"):
            st.session_state.rg_view = "teacher"
            st.rerun()
        if activity["subtitle"]:
            st.caption(activity["subtitle"])

        stage = st.session_state.pupil_stage

        # --- INTRO ---
        if stage == "intro":
            st.markdown(
                """
                <div class="rg-card">
                📖 Read the story, 🔤 practise some tricky sounds, and 🎯 answer questions about
                what you've read. Tap a vocabulary word below the story to find out what it means.
                Good luck, detective!
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Start →", type="primary"):
                st.session_state.pupil_stage = "fluency"
                st.rerun()

        # --- FLUENCY (reading + vocab) ---
        elif stage == "fluency":
            st.markdown('<div class="rg-progress-label">Part 1 of 3 · Read aloud</div>', unsafe_allow_html=True)
            st.progress(1 / 3)

            passage_html = esc(activity["passage"]).replace("\n\n", "<br><br>").replace("\n", "<br>")
            for w, d in activity["vocab"]:
                passage_html = passage_html.replace(esc(w), f'<span class="rg-hw">{esc(w)}</span>')
            st.markdown(f'<div class="rg-passage">{passage_html}</div>', unsafe_allow_html=True)

            if activity["vocab"]:
                st.write("**Tap a word to see what it means:**")
                cols = st.columns(min(len(activity["vocab"]), 4))
                for i, (w, d) in enumerate(activity["vocab"]):
                    if cols[i % len(cols)].button(w, key=f"vocabbtn_{i}"):
                        st.session_state.revealed_word = i
                if st.session_state.revealed_word is not None:
                    w, d = activity["vocab"][st.session_state.revealed_word]
                    st.info(f"**{w}** — {d}")

            if st.button("I've finished reading →", type="primary"):
                st.session_state.pupil_stage = "phonics"
                st.rerun()

        # --- PHONICS ---
        elif stage == "phonics":
            st.markdown('<div class="rg-progress-label">Part 2 of 3 · Phonics</div>', unsafe_allow_html=True)
            st.progress(2 / 3)

            if not activity["phonics"]:
                st.write("No phonics questions were set for this activity.")
                if st.button("Next: comprehension →", type="primary"):
                    st.session_state.pupil_stage = "vipers"
                    st.rerun()
            else:
                idx = st.session_state.ph_idx
                q = activity["phonics"][idx]
                st.caption(f"Question {idx + 1} of {len(activity['phonics'])}")
                st.markdown(f"**{esc(q['prompt'])}**")

                answered = idx in st.session_state.answered_ph
                cols = st.columns(len(q["tiles"]))
                for t, tile in enumerate(q["tiles"]):
                    label = tile
                    if answered:
                        chosen = st.session_state.answered_ph[idx]
                        if t == q["correct"]:
                            label = f"✅ {tile}"
                        elif t == chosen:
                            label = f"❌ {tile}"
                    if cols[t].button(label, key=f"tile_{idx}_{t}", disabled=answered):
                        st.session_state.answered_ph[idx] = t
                        if t == q["correct"]:
                            st.session_state.score["ph"] += 1
                        st.rerun()

                if answered:
                    correct = st.session_state.answered_ph[idx] == q["correct"]
                    if correct:
                        st.success(f"✓ {q['expl']}")
                    else:
                        st.error(f"✗ {q['expl']}")
                    is_last = idx == len(activity["phonics"]) - 1
                    if st.button("Next: comprehension →" if is_last else "Next question →", type="primary"):
                        if is_last:
                            st.session_state.pupil_stage = "vipers"
                        else:
                            st.session_state.ph_idx += 1
                        st.rerun()

        # --- VIPERS ---
        elif stage == "vipers":
            st.markdown('<div class="rg-progress-label">Part 3 of 3 · Comprehension</div>', unsafe_allow_html=True)
            st.progress(3 / 3)

            with st.expander("📖 Show / hide the story"):
                st.write(activity["passage"])

            if not activity["vipers"]:
                st.write("No comprehension questions were set for this activity.")
                if st.button("See my results →", type="primary"):
                    st.session_state.pupil_stage = "end"
                    st.rerun()
            else:
                idx = st.session_state.vip_idx
                q = activity["vipers"][idx]
                st.markdown(f'<span class="rg-vipbadge {q["cls"]}">{q["label"]}</span>', unsafe_allow_html=True)
                st.markdown(f"**{esc(q['q'])}**")

                answered = idx in st.session_state.answered_vip
                for o, opt in enumerate(q["opts"]):
                    label = opt
                    if answered:
                        chosen = st.session_state.answered_vip[idx]
                        if o == q["correct"]:
                            label = f"✅ {opt}"
                        elif o == chosen:
                            label = f"❌ {opt}"
                    if st.button(label, key=f"opt_{idx}_{o}", disabled=answered, use_container_width=True):
                        st.session_state.answered_vip[idx] = o
                        if o == q["correct"]:
                            st.session_state.score["vi"] += 1
                        st.rerun()

                if answered:
                    correct = st.session_state.answered_vip[idx] == q["correct"]
                    if correct:
                        st.success(f"✓ {q['fb']}")
                    else:
                        st.error(f"✗ {q['fb']}")
                    is_last = idx == len(activity["vipers"]) - 1
                    if st.button("See my results →" if is_last else "Next →", type="primary"):
                        if is_last:
                            st.session_state.pupil_stage = "end"
                        else:
                            st.session_state.vip_idx += 1
                        st.rerun()

        # --- END ---
        elif stage == "end":
            ph_total = len(activity["phonics"])
            vi_total = len(activity["vipers"])
            total = st.session_state.score["ph"] + st.session_state.score["vi"]
            out_of = ph_total + vi_total

            st.markdown("### 🕵️ Case solved!")
            st.metric("Score", f"{total} / {out_of}" if out_of else "–")
            c1, c2 = st.columns(2)
            c1.metric("Phonics", f"{st.session_state.score['ph']} / {ph_total}" if ph_total else "–")
            c2.metric("Comprehension", f"{st.session_state.score['vi']} / {vi_total}" if vi_total else "–")

            pct = (total / out_of) if out_of else 0
            if pct >= 0.8:
                msg = "⭐ **Amazing work, detective!** You read carefully and showed brilliant understanding."
            elif pct >= 0.5:
                msg = "👍 **Really good effort!** Next time, look back at the text when you're not sure — the clues are always in there."
            else:
                msg = "🌱 **Well done for giving this a go!** Try reading the story again — you'll be a reading detective in no time."
            st.markdown(f'<div class="rg-card">{msg}</div>', unsafe_allow_html=True)

            if st.button("Try again", type="primary"):
                st.session_state.pupil_stage = "fluency"
                st.session_state.score = {"ph": 0, "vi": 0}
                st.session_state.ph_idx = 0
                st.session_state.vip_idx = 0
                st.session_state.answered_ph = {}
                st.session_state.answered_vip = {}
                st.session_state.revealed_word = None
                st.rerun()

# ===========================================================================
# TAB 2: Book recommendations
# ===========================================================================
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

# ===========================================================================
# TAB 3: Quick phonics (standalone, no builder needed)
# ===========================================================================
import random

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
