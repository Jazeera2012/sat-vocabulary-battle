# Python SAT Vocabulary Game
import random


def welcome():
    print("=" * 40)
    print("     📚 ADVANCED VOCABULARY TRIVIA")
    print("=" * 40)

    print("\nWelcome to my vocabulary quiz! 🎉")
    print("""
    This project is based on SAToplam SAT Vocabulary
    and other SAT vocabulary resources.

    Students often struggle with choosing which
    words to learn and understanding complex
    definitions.

    This quiz is designed to make vocabulary
    learning easier and more interactive.

    You will learn advanced words organized by
    titles and sets, review their meanings and
    examples,
    and then test your knowledge.

    Good luck! 🚀
    """)


def vocabulary_section():
    print("\n" + "=" * 40)
    print("          📖 VOCABULARY")
    print("=" * 40)

    # Store each vocabulary word together with its meaning and example sentence.
    vocabulary = {
        "Erratic": {
            "meaning": "unpredictable, inconsistent, or irregular",
            "example": "His erratic behavior made it difficult to predict what he would do next."
        },

        "Secluded": {
            "meaning": "isolated, hidden, or away from people",
            "example": "They found a secluded cabin in the mountains."
        },

        "Fluctuate": {
            "meaning": "to rise and fall or change repeatedly",
            "example": "Prices fluctuate throughout the year."
        },

        "Exalt": {
            "meaning": "to praise or glorify highly",
            "example": "The poem exalts the beauty of nature."
        },

        "Admonish": {
            "meaning": "to warn or scold someone",
            "example": "The teacher admonished him for being late."
        },

        "Abrupt": {
            "meaning": "sudden or unexpected",
            "example": "The meeting came to an abrupt end."
        },

        "Content": {
            "meaning": "satisfied or pleased with something",
            "example": "She was content with her life in the countryside."
        },

        "Eccentric": {
            "meaning": "unusually strange or unconventional",
            "example": "The artist was known for his eccentric personality."
        },

        "Mired": {
            "meaning": "stuck or trapped in something",
            "example": "The project became mired in financial problems."
        },

        "Colloquial": {
            "meaning": "informal language used in everyday conversation",
            "example": "The word 'kids' is a colloquial term for 'children'."
        },

        "Reconcile": {
            "meaning": "to make peace or resolve differences",
            "example": "The two friends reconciled after their argument."
        },

        "Alienate": {
            "meaning": "to make someone feel isolated or distant",
            "example": "His rude behavior alienated his classmates."
        },

        "Distinguish": {
            "meaning": "to recognize or identify a difference between things",
            "example": "It can be difficult to distinguish fact from opinion."
        },

        "Adequate": {
            "meaning": "sufficient or enough for a particular purpose",
            "example": "The room was adequate for two people."
        },

        "Contend": {
            "meaning": "to deal with something or to argue or claim something",
            "example": "The author contends that technology has changed education."
        },

        "Skeptical": {
            "meaning": "doubtful or not easily convinced",
            "example": "She was skeptical about his explanation."
        },

        "Enfranchise": {
            "meaning": "to give someone the right to vote",
            "example": "The new law enfranchised thousands of citizens."
        },

        "Sophisticated": {
            "meaning": "advanced, complex, or highly developed",
            "example": "The laboratory uses sophisticated technology."
        },

        "Radical": {
            "meaning": "extreme, fundamental, or revolutionary",
            "example": "The government proposed radical changes to the system."
        },

        "Formulate": {
            "meaning": "to create, develop, or devise a plan or idea",
            "example": "The researchers formulated a new hypothesis."
        },

        "Attest": {
            "meaning": "to confirm, verify, or provide evidence of something",
            "example": "The documents attest to his achievements."
        },

        "Vexing": {
            "meaning": "annoying, frustrating, or irritating",
            "example": "Finding a solution to the problem was particularly vexing."
        },

        "Unassuming": {
            "meaning": "humble, modest, and not trying to attract attention",
            "example": "Despite her success, she remained unassuming."
        },

        "Coerce": {
            "meaning": "to force someone to do something through pressure or threats",
            "example": "They tried to coerce him into signing the document."
        },

        "Adept": {
            "meaning": "very skilled or proficient at something",
            "example": "She is adept at solving difficult problems."
        }
    }

    # Display all words with their definitions and example sentences.
    for word, information in vocabulary.items():
        print(f"\n📚 {word}")
        print(f"Meaning: {information['meaning']}")
        print(f"Example: {information['example']}")

    return vocabulary


def ready():
    print("\n" + "=" * 40)
    print("              🤓 READY?")
    print("""You've learned all 25 words.
Now it's time to put them to the test! 🧠

    You will get 25 sentences with missing words.
    Use the vocabulary from Set 1 to complete them.

    No options.
    No hints.
    Just you and your vocabulary. 😈""")

    # Keep asking until the user gives a valid yes/no response.
    while True:
        answer = input("Are you ready to take this test? (yes/no): ").lower()

        if answer == "yes":
            print("\nLet's start the test! 📓")
            return True

        elif answer == "no":
            print("\nNo problem! Let's review the vocab again! 📖")
            return False

        else:
            print("\nI didn't understand you! Please type again! (yes/no)")


questions = [
    {
        "sentence": "The weather was so _____ that no one could predict if the picnic would be rained out. The constant changes made it hard to plan anything outdoors.",
        "answer": "erratic"
    },

    {
        "sentence": "The old house was _____ deep in the woods, making it the perfect hideaway for those seeking privacy. Few people ever ventured that far into the forest.",
        "answer": "secluded"
    },

    {
        "sentence": "Stock prices tend to _____ throughout the day, with values rising and falling unpredictably. Investors need to be prepared for these constant changes.",
        "answer": "fluctuate"
    },

    {
        "sentence": "The community gathered to _____ their leader, showing their admiration with songs and speeches. His contributions were widely recognized and celebrated.",
        "answer": "exalt"
    },

    {
        "sentence": "The teacher had to _____ the students for not completing their homework on time. Her warning made it clear they needed to be more responsible.",
        "answer": "admonish"
    },

    {
        "sentence": "His departure from the meeting was so _____ that no one had time to ask him any questions. The sudden exit caught everyone by surprise.",
        "answer": "abrupt"
    },

    {
        "sentence": "She was _____ with her meal, feeling satisfied with the delicious food. She leaned back in her chair with a smile.",
        "answer": "content"
    },

    {
        "sentence": "His _____ clothing choices often drew attention, as he preferred to wear mismatched patterns and bright colors. People found his style both strange and intriguing.",
        "answer": "eccentric"
    },

    {
        "sentence": "After the heavy rain, the tractor became _____ in the field and couldn't move. The mud made it impossible to get the wheels out.",
        "answer": "mired"
    },

    {
        "sentence": "He prefers using _____ expressions when talking to friends, opting for casual, everyday language instead of formal speech. It makes the conversation feel more relaxed.",
        "answer": "colloquial"
    },

    {
        "sentence": "After years of disagreement, the two brothers finally decided to _____ their differences and work together again. They both wanted to restore their relationship.",
        "answer": "reconcile"
    },

    {
        "sentence": "His constant criticism began to _____ his teammates, making them feel unwanted and distant from the group. Eventually, they stopped asking for his opinion.",
        "answer": "alienate"
    },

    {
        "sentence": "It can be difficult to _____ between a reliable source and a misleading one when both present similar information. Careful analysis is necessary.",
        "answer": "distinguish"
    },

    {
        "sentence": "The small apartment was _____ for two people, providing enough space and basic furniture for their needs. It wasn't luxurious, but it was comfortable enough.",
        "answer": "adequate"
    },

    {
        "sentence": "The researcher _____ that regular exercise can improve concentration and memory. He supported his claim with evidence from several studies.",
        "answer": "contend"
    },

    {
        "sentence": "She was _____ of the advertisement's promises and wanted to see more evidence before believing the company's claims.",
        "answer": "skeptical"
    },

    {
        "sentence": "The new law helped _____ thousands of citizens by giving them the right to participate in elections. It marked an important step toward political equality.",
        "answer": "enfranchise"
    },

    {
        "sentence": "The hospital uses _____ equipment that allows doctors to detect and treat complicated medical conditions with great precision.",
        "answer": "sophisticated"
    },

    {
        "sentence": "The company made a _____ decision to completely change its approach to environmental policy. The new strategy was very different from its previous one.",
        "answer": "radical"
    },

    {
        "sentence": "Before beginning the experiment, the scientists needed to _____ a clear plan that included each step of the research process.",
        "answer": "formulate"
    },

    {
        "sentence": "The photographs _____ to the fact that the building had been damaged long before the renovation began. They provided clear evidence of its condition.",
        "answer": "attest"
    },

    {
        "sentence": "Finding a solution to the complicated problem was particularly _____. No matter what the team tried, another difficulty appeared.",
        "answer": "vexing"
    },

    {
        "sentence": "Despite winning several awards, the scientist remained _____ and rarely talked about her achievements. She preferred to let her work speak for itself.",
        "answer": "unassuming"
    },

    {
        "sentence": "The criminals attempted to _____ the witness into changing his statement by putting intense pressure on him.",
        "answer": "coerce"
    },

    {
        "sentence": "She is _____ at solving complex mathematical problems and can quickly identify patterns that others often miss.",
        "answer": "adept"
    }
]


def fighting_time(questions):
    print("\n" + "=" * 40)
    print("             🧠 QUIZ")
    print("=" * 40)

    print("Use the words below to complete the sentences!\n")
    print("You can use each word only once!\n")

    # Extract the correct answers to create the word bank shown before the quiz.
    words = [question["answer"] for question in questions]

    for word in words:
        print(f"∙ {word}")

    print("\nGood luck! 🍀 You can handle this! ✌🏻")

    # Randomize the question order so each quiz attempt is different.
    random.shuffle(questions)

    score = 0

    # Track the question number while processing every question in the shuffled list.
    for number, question in enumerate(questions, start=1):
        print("\n" + "=" * 40)
        print(f"             🥊 BATTLE {number} / 25")
        print("=" * 40)

        print(f"\n{question['sentence']}")

        answer = input("Enter your answer: ").strip().lower()

        if answer == question["answer"].lower():
            print("✅ Correct! You've nailed it! 💗")
            score += 1

        else:
            print("Ohh😞... ❌ Incorrect! But, you can do it! Hard work pay off! 🎀")
            print(f"Correct answer: {question['answer']}")

    return score


def battle_results(score):
    print("\n" + "=" * 40)
    print("             🏆 BATTLE RESULTS")
    print("=" * 40)
    print("So, it's time to see your score! 🌟")
    print("Of course, it is so exciting 😭")
    print(f"\nYour score: {score}/25")

    # Use score ranges to provide different feedback based on the user's performance.
    if score == 25:
        print("🔥 PERFECT! You mastered all 25 words! 🧠 You are the best! 🌹")

    elif score >= 20:
        print("EXCELLENT JOB! 👏🏻 Your vocabulary skills are strong! 📓")

    elif score >= 15:
        print("Good job! 👍")

    else:
        print("📚 Keep practicing...! You still have to review the vocab!")


def play_again():
    # Keep the game running until the user chooses a valid option.
    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()

        if answer == "yes":
            return True

        elif answer == "no":
            return False

        else:
            print("\nI can't understand you! Please type again! (yes/no)!")


welcome()
vocabulary = vocabulary_section()

if ready():
    while True:
        score = fighting_time(questions)
        battle_results(score)

        if play_again():
            print("\n😼 Let's fight again!")

        else:
            print("\n👋 Thanks for playing!")
            print("Keep learning and keep fighting! 📚🥊")
            break
