import json
import os

BASE_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\polity\Historical-Background-Making-of-Constitution\Indian-Councils-Act-1892"
HI_DIR = os.path.join(BASE_DIR, "hi")

# ----------------- 50 UNIQUE PRACTICE QUESTIONS (ENGLISH) -----------------
practice_questions = [
    {
        "q": "Which of the following Acts first introduced the right to discuss the budget in the legislative council?",
        "opts": ["Indian Councils Act, 1861", "Indian Councils Act, 1892", "Indian Councils Act, 1909", "Government of India Act, 1919"],
        "ans": 1,
        "sol": "The Indian Councils Act of 1892 expanded the functions of the legislative councils by giving them the power of discussing the budget."
    },
    {
        "q": "What was the limit of additional (non-official) members in the Central Legislative Council under the Indian Councils Act of 1892?",
        "opts": ["6 to 12 members", "10 to 16 members", "16 to 20 members", "20 to 24 members"],
        "ans": 1,
        "sol": "The Act increased the number of additional members in the Central Legislative Council to a minimum of 10 and a maximum of 16."
    },
    {
        "q": "Under the Indian Councils Act of 1892, how was the budget to be dealt with by the legislative council?",
        "opts": [
            "Members could discuss the budget but had no power to vote or propose resolutions.",
            "Members had the power to vote on the budget and reject it.",
            "Members could only vote on the budget but not discuss it.",
            "The budget was not presented to the council at all."
        ],
        "ans": 0,
        "sol": "The Act allowed the councils to discuss the annual financial statement, but members could not vote on it, propose resolutions, or divide the house."
    },
    {
        "q": "Which of the following was a key demand of the Indian National Congress (formed in 1885) that was partially addressed by the Act of 1892?",
        "opts": ["Complete Independence", "Reforms of the legislative councils and expansion of representation", "Abolition of the Viceroy's office", "Establishment of a Supreme Court"],
        "ans": 1,
        "sol": "The Congress demanded reform of the legislative councils to include more Indian representatives, which led to the expansion of councils under the 1892 Act."
    },
    {
        "q": "With reference to the Indian Councils Act of 1892, consider the following statements:\n1. It allowed members of the legislative councils to ask questions.\n2. It permitted members to ask supplementary questions.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect because the right to ask supplementary questions was not allowed under the 1892 Act; it was introduced by the 1909 Act."
    },
    {
        "q": "Which word was deliberately avoided in the official text of the Indian Councils Act, 1892, despite introducing its mechanism?",
        "opts": ["Nomination", "Representation", "Election", "Council"],
        "ans": 2,
        "sol": "The word 'election' was carefully avoided in the text of the Act. The process was described as nomination made on the recommendation of certain bodies."
    },
    {
        "q": "Under the 1892 Act, non-official members of the Central Legislative Council were nominated by the Viceroy on the recommendation of which of the following?",
        "opts": ["The British House of Commons", "Provincial Legislative Councils and the Bengal Chamber of Commerce", "Municipalities and District Boards directly", "The Secretary of State for India"],
        "ans": 1,
        "sol": "For the Central Legislative Council, nominations were made by the Viceroy on the recommendation of the provincial legislative councils and the Bengal Chamber of Commerce."
    },
    {
        "q": "Who was empowered to nominate non-official members to the provincial legislative councils under the 1892 Act?",
        "opts": ["The Viceroy of India", "The Secretary of State", "The Governors of the respective provinces", "The Municipal Commissioners"],
        "ans": 2,
        "sol": "The Governors of the provinces nominated non-official members to the provincial legislative councils on the recommendation of local bodies."
    },
    {
        "q": "What notice period was required for legislative council members to ask questions under the Indian Councils Act of 1892?",
        "opts": ["3 days", "6 days", "10 days", "14 days"],
        "ans": 1,
        "sol": "Members were allowed to ask questions of the executive on matters of public interest, subject to a mandatory six days' notice."
    },
    {
        "q": "Who held the absolute power to disallow any question asked by a member in the legislative council under the 1892 Act?",
        "opts": ["The Secretary of State", "The President of the Council (Viceroy/Governor)", "The Chief Justice of Calcutta", "The Prime Minister of Great Britain"],
        "ans": 1,
        "sol": "The President of the Council had the power to disallow any question without giving any reason, and his decision was final."
    },
    {
        "q": "Under the Indian Councils Act of 1892, the official majority in the legislative councils was:",
        "opts": [
            "Abolished in both Central and provincial councils.",
            "Maintained in both Central and provincial councils.",
            "Maintained only in provincial councils.",
            "Replaced by an Indian non-official majority."
        ],
        "ans": 1,
        "sol": "The Act increased the number of non-official members, but the official majority (British officials) was strictly maintained in both Central and provincial legislative councils."
    },
    {
        "q": "Which of the following local bodies could recommend members for nomination to the provincial legislative councils under the 1892 Act?\n1. District Boards\n2. Municipalities\n3. Universities\n4. Zamindars\nSelect the correct answer:",
        "opts": ["1 and 2 only", "1, 2 and 3 only", "3 and 4 only", "1, 2, 3 and 4"],
        "ans": 3,
        "sol": "Recommendations for provincial legislative councils were made by district boards, municipalities, universities, zamindars, and chambers."
    },
    {
        "q": "The introduction of the representative principle by the Act of 1892 was classified as which form of election?",
        "opts": ["Direct Election", "Indirect Election", "Universal Adult Suffrage", "Proportional Representation"],
        "ans": 1,
        "sol": "The system was a form of indirect election, as seats were filled through nominations based on recommendations from intermediate civic bodies."
    },
    {
        "q": "Which Act laid the first foundation of the parliamentary system in India by introducing discussion on public finance and executive questioning?",
        "opts": ["Charter Act of 1853", "Indian Councils Act of 1861", "Indian Councils Act of 1892", "Indian Councils Act of 1909"],
        "ans": 2,
        "sol": "The Indian Councils Act of 1892 laid the foundation of the parliamentary system by introducing budget discussion and questioning of the executive."
    },
    {
        "q": "Who was the Viceroy of India when the Indian Councils Act of 1892 was enacted?",
        "opts": ["Lord Canning", "Lord Dufferin", "Lord Lansdowne", "Lord Curzon"],
        "ans": 2,
        "sol": "Lord Lansdowne was the Viceroy of India (1888–1894) when the Indian Councils Act of 1892 was enacted."
    },
    {
        "q": "What was the maximum number of additional members allowed in the Bengal Legislative Council under the 1892 Act?",
        "opts": ["12 members", "15 members", "20 members", "25 members"],
        "ans": 2,
        "sol": "The provincial legislative council of Bengal was expanded to a maximum of 20 additional members under the 1892 reforms."
    },
    {
        "q": "What was the maximum number of additional members allowed in the North-Western Provinces and Oudh Legislative Council under the 1892 Act?",
        "opts": ["10 members", "12 members", "15 members", "20 members"],
        "ans": 2,
        "sol": "The council for the North-Western Provinces and Oudh was expanded to a maximum of 15 members."
    },
    {
        "q": "The commercial body authorized to recommend non-official members to the Central Legislative Council under the 1892 Act was:",
        "opts": [
            "The Madras Chamber of Commerce",
            "The Bombay Chamber of Commerce",
            "The Bengal Chamber of Commerce",
            "The East India Association"
        ],
        "ans": 2,
        "sol": "The Bengal Chamber of Commerce was authorized to recommend members to the Central Legislative Council."
    },
    {
        "q": "With reference to the legislative powers under the 1892 Act, consider the following statements:\n1. Members could discuss the budget before it was finalized.\n2. Members could propose amendments to bills.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Members could discuss the annual financial statement and could propose and debate amendments on legislative bills (though budget voting was barred)."
    },
    {
        "q": "The primary limitation of the budget discussion under the Indian Councils Act of 1892 was:",
        "opts": [
            "It was held in private, away from public record.",
            "It was limited to military expenditures only.",
            "No member could vote on any portion of the budget or move resolutions.",
            "It required the prior assent of the British Prime Minister."
        ],
        "ans": 2,
        "sol": "The primary limitation was that members could not vote on any budget items, nor could they propose resolutions regarding public finance."
    },
    {
        "q": "Which of the following is correct about the non-official majority in the provincial legislative councils under the 1892 Act?",
        "opts": [
            "An official majority was maintained in all provincial councils.",
            "A non-official majority was introduced in all provincial councils.",
            "A non-official majority was introduced only in the Bombay council.",
            "Provincial councils had no official members."
        ],
        "ans": 0,
        "sol": "Under the 1892 Act, the official majority (government officials) was strictly maintained in both the Central Council and all provincial councils."
    },
    {
        "q": "In which year did the Indian National Congress pass its first resolution demanding reform of the legislative councils?",
        "opts": ["1885", "1888", "1890", "1892"],
        "ans": 0,
        "sol": "In its inaugural session in 1885, the Indian National Congress passed a resolution demanding the reform and expansion of legislative councils."
    },
    {
        "q": "Who was the Secretary of State for India when the Indian Councils Act of 1892 was drafted and introduced?",
        "opts": ["Lord Morley", "Lord Cross", "Lord Salisbury", "Lord Hamilton"],
        "ans": 1,
        "sol": "Lord Cross was the Secretary of State for India who introduced the bill in the British Parliament."
    },
    {
        "q": "The parliamentary process of asking questions to the executive in the legislative assembly is formally called:",
        "opts": ["Interpellation", "Adjournment", "Resolution", "Veto"],
        "ans": 0,
        "sol": "Interpellation is the formal right of assembly members to submit questions to the executive branch of government."
    },
    {
        "q": "Which of the following describes the nature of the electorate under the 1892 Act?",
        "opts": [
            "Direct voting by all taxpayers.",
            "Indirect representation via recommendations of institutional bodies.",
            "Universal franchise for all college graduates.",
            "Separate electorates based on religious communities."
        ],
        "ans": 1,
        "sol": "There was no direct electorate. The electorate consisted of local bodies like municipalities, district boards, and universities making recommendations."
    },
    {
        "q": "Under the 1892 Act, the term of office for nominated additional members was:",
        "opts": ["1 year", "2 years", "3 years", "5 years"],
        "ans": 1,
        "sol": "Like the 1861 Act, the term of office for additional members nominated under the 1892 Act remained two years."
    },
    {
        "q": "What proportion of the total members in the Central Legislative Council under the 1892 Act was required to be non-official?",
        "opts": ["At least one-third", "At least two-fifths", "At least half", "At least two-thirds"],
        "ans": 1,
        "sol": "The Act mandated that not less than ten additional members were to be added, with at least two-fifths of them being non-official."
    },
    {
        "q": "Which of the following is correct regarding the right of interpellation under the 1892 Act?",
        "opts": [
            "It allowed members to ask questions on any subject without restriction.",
            "It allowed questions on public matters, but barred questions on military and foreign affairs without Viceroy's sanction.",
            "It allowed questions on military affairs only.",
            "It was restricted to native states matters only."
        ],
        "ans": 1,
        "sol": "Questions could be asked on public matters, but areas like military affairs, foreign relations, and public debt required prior sanction or could be disallowed."
    },
    {
        "q": "Under the 1892 Act, what happened if a member's question was disallowed by the President of the Council?",
        "opts": [
            "The member could appeal to the British Parliament.",
            "The question was referred to the Secretary of State.",
            "The decision was final and could not be challenged in any manner.",
            "The member was suspended from the council."
        ],
        "ans": 2,
        "sol": "The President's decision to disallow a question was absolute, final, and could not be appealed or challenged."
    },
    {
        "q": "Which of the following bodies recommended non-official members to the Madras Legislative Council under the 1892 Act?",
        "opts": [
            "The Madras Chamber of Commerce and Municipalities",
            "The Bengal Chamber of Commerce",
            "The Viceroy directly",
            "The British House of Lords"
        ],
        "ans": 0,
        "sol": "Local bodies in Madras, including the Madras Chamber of Commerce and municipalities, made recommendations to the Governor of Madras."
    },
    {
        "q": "The Indian Councils Act of 1892 is considered a significant constitutional advance because:",
        "opts": [
            "It introduced fully elected cabinet ministers in India.",
            "It conceded the principle of election and expanded legislative functions.",
            "It granted administrative autonomy to native princely states.",
            "It separated the judiciary from the executive."
        ],
        "ans": 1,
        "sol": "It was a major advance because it conceded the elective principle (indirectly) and expanded legislative functions to include budget discussions and questioning."
    },
    {
        "q": "How did the 1892 Act affect the overall powers of the Viceroy over the legislative councils?",
        "opts": [
            "It curtailed the Viceroy's powers considerably.",
            "It maintained the Viceroy's supreme authority, including veto power and the right to make regulations.",
            "It made the Viceroy subordinate to the council's majority vote.",
            "It transferred the Viceroy's veto to the Bengal Chamber of Commerce."
        ],
        "ans": 1,
        "sol": "The Viceroy's ultimate veto and regulatory powers remained fully intact, ensuring imperial authority was not compromised."
    },
    {
        "q": "Which of the following statements is correct regarding the 'recommendation' system of the 1892 Act?",
        "opts": [
            "It was a binding process; the Viceroy had to nominate whoever was recommended.",
            "It was technically advisory, but the Viceroy/Governors followed the recommendations in practice.",
            "It was rejected by the Viceroy in almost all cases.",
            "It required recommendations to be signed by the Mughal Emperor's descendants."
        ],
        "ans": 1,
        "sol": "Technically, the recommendations were not legally binding on the Viceroy, but in practice, they were accepted, making it act as an indirect election."
    },
    {
        "q": "The demand for 'No Taxation Without Representation' in India's freedom struggle was first linked to which legislative limitation?",
        "opts": [
            "The ban on discussing the budget in 1861.",
            "The ban on voting on the budget in 1892.",
            "The separate electorates of 1909.",
            "The dyarchy system of 1919."
        ],
        "ans": 1,
        "sol": "Since the 1892 Act allowed budget discussion but prohibited voting, nationalists used it to demand actual voting power, raising the slogan of representation."
    },
    {
        "q": "Under the 1892 Act, the minimum number of additional members in the Central Legislative Council was fixed at:",
        "opts": ["6 members", "8 members", "10 members", "12 members"],
        "ans": 2,
        "sol": "The minimum number of additional legislative members was increased to 10."
    },
    {
        "q": "Under the 1892 Act, the maximum number of additional members in the Central Legislative Council was fixed at:",
        "opts": ["12 members", "16 members", "20 members", "24 members"],
        "ans": 1,
        "sol": "The maximum number of additional legislative members was increased to 16."
    },
    {
        "q": "Which of the following provincial legislative councils was NOT expanded under the Indian Councils Act of 1892?",
        "opts": ["Bombay", "Madras", "Bengal", "Punjab"],
        "ans": 3,
        "sol": "Punjab's legislative council was established in 1897 under the 1861 Act's provisions. The 1892 Act expanded existing councils of Bombay, Madras, Bengal, and NWFP."
    },
    {
        "q": "The first Indian members who entered the Central Legislative Council via the recommendation system of 1892 included:",
        "opts": [
            "Gopal Krishna Gokhale and Rash Behari Ghosh",
            "Jawaharlal Nehru and Sardar Patel",
            "Mahatma Gandhi and Subhas Chandra Bose",
            "Bal Gangadhar Tilak and B.R. Ambedkar"
        ],
        "ans": 0,
        "sol": "Prominent nationalists like Gopal Krishna Gokhale, Rash Behari Ghosh, and Pherozeshah Mehta entered the council under these reforms."
    },
    {
        "q": "With reference to Pherozeshah Mehta's entry into the Central Legislative Council in 1893, he was recommended by:",
        "opts": [
            "The Bengal Chamber of Commerce",
            "The Bombay Legislative Council",
            "The Madras Municipality",
            "The Viceroy directly"
        ],
        "ans": 1,
        "sol": "Pherozeshah Mehta was recommended by the Bombay Provincial Legislative Council to the Central Legislative Council."
    },
    {
        "q": "What was a major criticism of the 1892 Act by the early nationalist leaders?",
        "opts": [
            "It gave too much power to local district boards.",
            "It kept the franchise extremely narrow, indirect, and denied budget voting.",
            "It abolished provincial councils.",
            "It allowed native states to govern British India."
        ],
        "ans": 1,
        "sol": "The early nationalists criticized the Act because it failed to give Indians the power to vote on budgets or ask supplementary questions, keeping representation indirect and symbolic."
    },
    {
        "q": "Under the 1892 Act, how many additional members were to be added to the Bombay Legislative Council?",
        "opts": ["Minimum 4, Maximum 8", "Minimum 8, Maximum 20", "Minimum 10, Maximum 16", "Minimum 12, Maximum 24"],
        "ans": 1,
        "sol": "For Bombay, the number of additional members was expanded to a minimum of 8 and a maximum of 20."
    },
    {
        "q": "Under the 1892 Act, how many additional members were to be added to the Madras Legislative Council?",
        "opts": ["Minimum 4, Maximum 8", "Minimum 8, Maximum 20", "Minimum 10, Maximum 16", "Minimum 12, Maximum 24"],
        "ans": 1,
        "sol": "For Madras, the additional members were expanded to a minimum of 8 and a maximum of 20."
    },
    {
        "q": "The power of interpellation introduced in 1892 served as a precursor to which modern legislative device?",
        "opts": ["Zero Hour", "Question Hour", "No-Confidence Motion", "Censure Motion"],
        "ans": 1,
        "sol": "Interpellation is the historical antecedent of the modern Question Hour in the Indian Parliament."
    },
    {
        "q": "Who was authorized to frame the rules and regulations for the nomination of members under the 1892 Act?",
        "opts": [
            "The Viceroy (with the approval of the Secretary of State)",
            "The British House of Commons exclusively",
            "The local district boards",
            "The Supreme Court of Calcutta"
        ],
        "ans": 0,
        "sol": "The Viceroy in India was authorized to frame the specific regulations for nominations, subject to the final approval of the Secretary of State."
    },
    {
        "q": "Which of the following is correct regarding the discussion of the budget under the 1892 Act?",
        "opts": [
            "It took place only if the Viceroy specifically requested a vote.",
            "It was a general discussion on the financial policy and accounts of the government.",
            "It was restricted to the military budget only.",
            "It was held only when the government was in a deficit."
        ],
        "ans": 1,
        "sol": "It was a general discussion where members could raise concerns about taxes, administration, and financial policies, though no voting took place."
    },
    {
        "q": "Under the 1892 Act, additional members were added to the councils of which of the following presidencies?\n1. Bombay\n2. Madras\n3. Bengal\nSelect the correct answer:",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        "ans": 3,
        "sol": "All three presidencies—Bombay, Madras, and Bengal—had their legislative councils expanded under the Act of 1892."
    },
    {
        "q": "The Indian Councils Act of 1892 was an amendment of which previous principal Act?",
        "opts": ["Government of India Act 1858", "Indian Councils Act 1861", "Regulating Act 1773", "Charter Act 1833"],
        "ans": 1,
        "sol": "The Indian Councils Act of 1892 was passed as an amendment to the Indian Councils Act of 1861."
    },
    {
        "q": "Which of the following is correct regarding the nature of the legislative councils after 1892?",
        "opts": [
            "They remained advisory bodies with expanded deliberative powers.",
            "They became sovereign parliaments.",
            "They were subordinate to native courts.",
            "They were stripped of law-making powers."
        ],
        "ans": 0,
        "sol": "The councils remained advisory bodies under the executive, though their deliberative functions (budget, questions) were expanded."
    },
    {
        "q": "The introduction of the representative element in 1892 was intended by the British to:",
        "opts": [
            "Prepare India for immediate self-rule.",
            "Placate moderate nationalists while keeping executive power absolute.",
            "Establish a federal republic.",
            "Abolish the Governor-General's veto."
        ],
        "ans": 1,
        "sol": "The British sought to pacify the moderate elements of the Indian National Congress by granting minor concessions, while keeping imperial executive power absolute."
    },
    {
        "q": "How did the 1892 Act affect the relationship between the central and provincial legislative councils?",
        "opts": [
            "Provincial councils were subordinated to the Central Council's members.",
            "Provincial councils were given the right to recommend members to the Central Council.",
            "Provincial councils were abolished.",
            "Provincial councils were merged with the Central Council."
        ],
        "ans": 1,
        "sol": "Provincial legislative councils were given the right to recommend non-official members to the Central Legislative Council."
    }
]

# ----------------- 10 UNIQUE MOCK QUESTIONS (ENGLISH) -----------------
mock_questions = [
    {
        "q": "With reference to the Indian Councils Act of 1892, consider the following statements:\n1. It introduced the elective principle for the first time in British India.\n2. The word 'election' was explicitly used in the provisions of the Act.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct: it introduced the elective principle indirectly. Statement 2 is incorrect because the word 'election' was deliberately avoided in the text of the Act."
    },
    {
        "q": "<strong>Assertion (A):</strong> The Indian Councils Act of 1892 is a landmark in the constitutional history of India.<br><strong>Reason (R):</strong> It allowed the legislative councils to discuss the financial budget and ask questions of the executive branch.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both Assertion and Reason are true. The expansion of legislative functions to include budget discussion and executive questioning is a primary reason why it is considered a milestone."
    },
    {
        "q": "Consider the following statements regarding the Legislative Councils under the Indian Councils Act, 1892:\n1. The official majority of British officers was replaced by a non-official Indian majority in provincial councils.\n2. The provincial legislative councils were given the right to recommend members for the Central Legislative Council.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect because the official majority was maintained in all councils. Statement 2 is correct."
    },
    {
        "q": "Consider the following statements regarding the right to ask questions under the 1892 Act:\nStatement I: Members had the right to ask questions on matters of public interest, subject to a six days' notice.\nStatement II: Members could ask supplementary questions if the executive's answer was unsatisfactory.\nWhich of the following is correct?",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 0,
        "sol": "Statement I is correct. Statement II is incorrect because supplementary questions were strictly prohibited under the 1892 Act."
    },
    {
        "q": "Under the Indian Councils Act of 1892, which of the following bodies recommended non-official members to the provincial legislative councils?\n1. Universities\n2. Municipalities\n3. District Boards\n4. Chambers of Commerce\nSelect the correct answer using the codes given below:",
        "opts": ["1 and 2 only", "1, 2 and 3 only", "2 and 4 only", "1, 2, 3 and 4"],
        "ans": 3,
        "sol": "All these local civic and commercial bodies (universities, municipalities, district boards, and chambers of commerce) were authorized to make recommendations for provincial council nominations."
    },
    {
        "q": "With reference to the budget discussion under the 1892 Act, consider the following statements:\n1. The members had the right to propose resolutions regarding public expenditure.\n2. The members had the right to vote on the budget.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 3,
        "sol": "Both statements are incorrect. Under the 1892 Act, members could only discuss the budget; they could neither propose resolutions nor vote on it."
    },
    {
        "q": "<strong>Assertion (A):</strong> The Indian Councils Act of 1892 introduced indirect elections to legislative councils.<br><strong>Reason (R):</strong> The non-official seats were filled through nomination based on the recommendations of local bodies.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both Assertion and Reason are true. The recommendation system operated as a practical method of indirect election, which explains the assertion."
    },
    {
        "q": "Consider the following statements regarding the composition of the Central Legislative Council under the 1892 Act:\n1. The minimum number of additional members was fixed at 10.\n2. The maximum number of additional members was fixed at 16.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. The number of additional members was increased to a minimum of 10 and a maximum of 16."
    },
    {
        "q": "Which of the following describes the key limitation of the right of interpellation under the 1892 Act?",
        "opts": [
            "The President of the Council could disallow any question without stating reasons.",
            "All questions had to be approved by the British Prime Minister first.",
            "No Indian member was allowed to ask questions.",
            "Questions could only be asked in the local vernacular language."
        ],
        "ans": 0,
        "sol": "The President of the Council held absolute power to disallow any question without stating reasons, representing a major limitation."
    },
    {
        "q": "Consider the following statements regarding the historical context of the 1892 Act:\n1. The Act was passed during the viceroyalty of Lord Lansdowne.\n2. The Indian National Congress welcomed the Act as fully satisfying their demands.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect because the Congress was highly dissatisfied with the limitations of the Act (narrow franchise, lack of budget voting, no supplementaries)."
    }
]

# ----------------- 50 UNIQUE PRACTICE QUESTIONS (HINDI) -----------------
practice_questions_hi = [
    {
        "q": "निम्नलिखित में से किस अधिनियम ने पहली बार विधायी परिषद में बजट पर चर्चा करने का अधिकार प्रदान किया?",
        "opts": ["भारतीय परिषद अधिनियम, 1861", "भारतीय परिषद अधिनियम, 1892", "भारतीय परिषद अधिनियम, 1909", "भारत सरकार अधिनियम, 1919"],
        "ans": 1,
        "sol": "1892 के भारतीय परिषद अधिनियम ने विधायी परिषदों को बजट पर चर्चा करने की शक्ति देकर उनके कार्यों का विस्तार किया।"
    },
    {
        "q": "1892 के भारतीय परिषद अधिनियम के तहत केंद्रीय विधायी परिषद में अतिरिक्त (गैर-सरकारी) सदस्यों की सीमा क्या थी?",
        "opts": ["6 से 12 सदस्य", "10 to 16 सदस्य", "16 से 20 सदस्य", "20 से 24 सदस्य"],
        "ans": 1,
        "sol": "अधिनियम ने केंद्रीय विधायी परिषद में अतिरिक्त सदस्यों की संख्या बढ़ाकर न्यूनतम 10 और अधिकतम 16 कर दी।"
    },
    {
        "q": "1892 के भारतीय परिषद अधिनियम के तहत विधायी परिषद द्वारा बजट को किस प्रकार निपटाया जाना था?",
        "opts": [
            "सदस्य बजट पर चर्चा कर सकते थे लेकिन उन्हें मतदान करने या प्रस्ताव रखने का कोई अधिकार नहीं था।",
            "सदस्यों के पास बजट पर मतदान करने और इसे अस्वीकार करने की शक्ति थी।",
            "सदस्य केवल बजट पर मतदान कर सकते थे लेकिन उस पर चर्चा नहीं कर सकते थे।",
            "बजट को परिषद के समक्ष बिल्कुल प्रस्तुत नहीं किया जाता था।"
        ],
        "ans": 0,
        "sol": "अधिनियम ने परिषदों को वार्षिक वित्तीय विवरण पर चर्चा करने की अनुमति दी, लेकिन सदस्य उस पर मतदान नहीं कर सकते थे और न ही कोई प्रस्ताव रख सकते थे।"
    },
    {
        "q": "निम्नलिखित में से कौन सी भारतीय राष्ट्रीय कांग्रेस (1885 में स्थापित) की एक प्रमुख मांग थी जिसे 1892 के अधिनियम द्वारा आंशिक रूप से संबोधित किया गया था?",
        "opts": ["पूर्ण स्वतंत्रता", "विधायी परिषदों के सुधार और प्रतिनिधित्व का विस्तार", "वायसराय के कार्यालय का उन्मूलन", "एक सर्वोच्च न्यायालय की स्थापना"],
        "ans": 1,
        "sol": "कांग्रेस ने अधिक भारतीय प्रतिनिधियों को शामिल करने के लिए विधायी परिषदों में सुधार की मांग की, जिसके कारण 1892 के अधिनियम के तहत परिषदों का विस्तार किया गया।"
    },
    {
        "q": "1892 के भारतीय परिषद अधिनियम के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. इसने विधायी परिषदों के सदस्यों को प्रश्न पूछने की अनुमति दी।\n2. इसने सदस्यों को पूरक प्रश्न पूछने की अनुमति दी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 0,
        "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि 1892 के अधिनियम के तहत पूरक प्रश्न पूछने का अधिकार नहीं था; इसे 1909 के अधिनियम द्वारा शुरू किया गया था।"
    },
    {
        "q": "1892 के भारतीय परिषद अधिनियम के आधिकारिक पाठ में किस शब्द के प्रयोग से जानबूझकर बचा गया था, हालांकि इसकी प्रणाली शुरू की गई थी?",
        "opts": ["नामांकन (Nomination)", "प्रतिनिधित्व (Representation)", "चुनाव (Election)", "परिषद (Council)"],
        "ans": 2,
        "sol": "अधिनियम के पाठ में 'चुनाव' शब्द से सावधानीपूर्वक बचा गया था। इस प्रक्रिया को विशिष्ट निकायों की सिफारिशों पर नामांकन के रूप में वर्णित किया गया था।"
    },
    {
        "q": "1892 के अधिनियम के तहत, केंद्रीय विधायी परिषद के गैर-सरकारी सदस्यों को वायसराय द्वारा निम्नलिखित में से किसकी सिफारिश पर नामांकित किया जाता था?",
        "opts": ["ब्रिटिश हाउस ऑफ कॉमन्स", "प्रांतीय विधायी परिषदों और बंगाल चैंबर ऑफ कॉमर्स", "सीधे नगर पालिकाओं और जिला बोर्डों", "भारत के राज्य सचिव"],
        "ans": 1,
        "sol": "केंद्रीय विधायी परिषद के लिए, नामांकन वायसराय द्वारा प्रांतीय विधायी परिषदों और बंगाल चैंबर ऑफ कॉमर्स की सिफारिश पर किए जाते थे।"
    },
    {
        "q": "1892 के अधिनियम के तहत प्रांतीय विधायी परिषदों में गैर-सरकारी सदस्यों को नामांकित करने का अधिकार किसे दिया गया था?",
        "opts": ["भारत के वायसराय", "राज्य सचिव", "संबंधित प्रांतों के गवर्नर", "नगर आयुक्त"],
        "ans": 2,
        "sol": "प्रांतों के गवर्नर स्थानीय निकायों की सिफारिश पर प्रांतीय विधायी परिषदों में गैर-सरकारी सदस्यों को नामांकित करते थे।"
    },
    {
        "q": "1892 के भारतीय परिषद अधिनियम के तहत विधायी परिषद के सदस्यों को प्रश्न पूछने के लिए कितने दिन की पूर्व सूचना देना आवश्यक था?",
        "opts": ["3 दिन", "6 दिन", "10 दिन", "14 दिन"],
        "ans": 1,
        "sol": "सदस्यों को जनहित के मामलों पर कार्यपालिका से प्रश्न पूछने की अनुमति थी, बशर्ते कि वे छह दिन का पूर्व नोटिस दें।"
    },
    {
        "q": "1892 के अधिनियम के तहत विधायी परिषद में किसी सदस्य द्वारा पूछे गए प्रश्न को अस्वीकार करने का अंतिम अधिकार किसके पास था?",
        "opts": ["राज्य सचिव", "परिषद के अध्यक्ष (वायसराय/गवर्नर)", "कलकत्ता के मुख्य न्यायाधीश", "ग्रेट ब्रिटेन के प्रधानमंत्री"],
        "ans": 1,
        "sol": "परिषद के अध्यक्ष के पास बिना कोई कारण बताए किसी भी प्रश्न को अस्वीकार करने का अधिकार था, और उनका निर्णय अंतिम था।"
    },
    {
        "q": "1892 के भारतीय परिषद अधिनियम के तहत, विधायी परिषदों में सरकारी बहुमत की स्थिति क्या थी?",
        "opts": [
            "केंद्रीय और प्रांतीय दोनों परिषदों में समाप्त कर दिया गया था।",
            "केंद्रीय और प्रांतीय दोनों परिषदों में बनाए रखा गया था।",
            "केवल प्रांतीय परिषदों में बनाए रखा गया था।",
            "भारतीय गैर-सरकारी बहुमत द्वारा प्रतिस्थापित किया गया था।"
        ],
        "ans": 1,
        "sol": "अधिनियम ने गैर-सरकारी सदस्यों की संख्या में वृद्धि की, लेकिन केंद्रीय और प्रांतीय दोनों विधायी परिषदों में सरकारी बहुमत (ब्रिटिश अधिकारियों का बहुमत) को सख्ती से बनाए रखा।"
    },
    {
        "q": "1892 के अधिनियम के तहत निम्नलिखित में से कौन से स्थानीय निकाय प्रांतीय विधायी परिषदों में नामांकन के लिए सदस्यों की सिफारिश कर सकते थे?\n1. जिला बोर्ड\n2. नगर पालिकाएं\n3. विश्वविद्यालय\n4. जमींदार\nसही उत्तर चुनें:",
        "opts": ["केवल 1 और 2", "केवल 1, 2 और 3", "केवल 3 and 4", "1, 2, 3 और 4"],
        "ans": 3,
        "sol": "प्रांतीय विधायी परिषदों के लिए सिफारिशें जिला बोर्डों, नगर पालिकाओं, विश्वविद्यालयों, जमींदारों और वाणिज्य मंडलों द्वारा की जाती थीं।"
    },
    {
        "q": "1892 के अधिनियम द्वारा शुरू किए गए प्रतिनिधित्व सिद्धांत को किस प्रकार के चुनाव के रूप में वर्गीकृत किया गया था?",
        "opts": ["प्रत्यक्ष चुनाव (Direct Election)", "अप्रत्यक्ष चुनाव (Indirect Election)", "सार्वभौमिक वयस्क मताधिकार", "आनुपातिक प्रतिनिधित्व"],
        "ans": 1,
        "sol": "यह प्रणाली अप्रत्यक्ष चुनाव का एक रूप थी, क्योंकि सीटें मध्यवर्ती नागरिक निकायों की सिफारिशों पर नामांकन के माध्यम से भरी जाती थीं।"
    },
    {
        "q": "किस अधिनियम ने सार्वजनिक वित्त पर चर्चा और कार्यकारी से प्रश्न पूछने की शुरुआत करके भारत में संसदीय प्रणाली की पहली नींव रखी?",
        "opts": ["1853 का चार्टर अधिनियम", "1861 का भारतीय परिषद अधिनियम", "1892 का भारतीय परिषद अधिनियम", "1909 का भारतीय परिषद अधिनियम"],
        "ans": 2,
        "sol": "1892 के भारतीय परिषद अधिनियम ने बजट चर्चा और कार्यपालिका से प्रश्न पूछने की शुरुआत करके भारत में संसदीय प्रणाली की नींव रखी।"
    },
    {
        "q": "1892 का भारतीय परिषद अधिनियम पारित होने के समय भारत के वायसराय कौन थे?",
        "opts": ["लॉर्ड कैनिंग", "लॉर्ड डफरिन", "लॉर्ड लैंसडाउन", "लॉर्ड कर्जन"],
        "ans": 2,
        "sol": "1892 का भारतीय परिषद अधिनियम पारित होने के समय लॉर्ड लैंसडाउन (1888-1894) भारत के वायसराय थे।"
    },
    {
        "q": "1892 के अधिनियम के तहत बंगाल विधायी परिषद में अधिकतम कितने अतिरिक्त सदस्यों की अनुमति थी?",
        "opts": ["12 सदस्य", "15 सदस्य", "20 सदस्य", "25 सदस्य"],
        "ans": 2,
        "sol": "1892 के सुधारों के तहत बंगाल की प्रांतीय विधायी परिषद का विस्तार अधिकतम 20 अतिरिक्त सदस्यों तक किया गया था।"
    },
    {
        "q": "1892 के अधिनियम के तहत उत्तर-पश्चिमी प्रांतों और अवध विधायी परिषद में अधिकतम कितने अतिरिक्त सदस्यों की अनुमति थी?",
        "opts": ["10 सदस्य", "12 सदस्य", "15 सदस्य", "20 सदस्य"],
        "ans": 2,
        "sol": "उत्तर-पश्चिमी प्रांतों और अवध के लिए विधायी परिषद का विस्तार अधिकतम 15 सदस्यों तक किया गया था।"
    },
    {
        "q": "1892 के अधिनियम के तहत केंद्रीय विधायी परिषद में गैर-सरकारी सदस्यों की सिफारिश करने के लिए अधिकृत व्यावसायिक निकाय कौन सा था?",
        "opts": [
            "मद्रास चैंबर ऑफ कॉमर्स",
            "बॉम्बे चैंबर ऑफ कॉमर्स",
            "बंगाल चैंबर ऑफ कॉमर्स",
            "इस्ट इंडिया एसोसिएशन"
        ],
        "ans": 2,
        "sol": "बंगाल चैंबर ऑफ कॉमर्स को केंद्रीय विधायी परिषद में गैर-सरकारी सदस्यों की सिफारिश करने का अधिकार दिया गया था।"
    },
    {
        "q": "1892 के अधिनियम के तहत विधायी शक्तियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. सदस्य बजट पर अंतिम रूप दिए जाने से पहले उस पर चर्चा कर सकते थे।\n2. सदस्य विधेयकों पर संशोधन प्रस्तावित कर सकते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["ASCII 1", "ASCII 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 2,
        "sol": "दोनों कथन सही हैं। सदस्य बजट पर चर्चा कर सकते थे और विधेयकों पर संशोधन प्रस्तावित और बहस कर सकते थे (हालांकि बजट पर मतदान वर्जित था)।"
    },
    {
        "q": "1892 के भारतीय परिषद अधिनियम के तहत बजट चर्चा की प्राथमिक सीमा क्या थी?",
        "opts": [
            "यह सार्वजनिक रिकॉर्ड से दूर, निजी तौर पर आयोजित की जाती थी।",
            "यह केवल सैन्य खर्चों तक सीमित थी।",
            "कोई भी सदस्य बजट के किसी भी हिस्से पर मतदान नहीं कर सकता था और न ही कोई प्रस्ताव रख सकता था।",
            "इसके लिए ब्रिटिश प्रधानमंत्री की पूर्व सहमति आवश्यक थी।"
        ],
        "ans": 2,
        "sol": "प्राथमिक सीमा यह थी कि सदस्य बजट के मदों पर मतदान नहीं कर सकते थे, और न ही वित्तीय नीतियों से संबंधित प्रस्ताव रख सकते थे।"
    },
    {
        "q": "1892 के अधिनियम के तहत प्रांतीय विधायी परिषदों में गैर-सरकारी बहुमत के बारे में निम्नलिखित में से कौन सा सही है?",
        "opts": [
            "सभी प्रांतीय परिषदों में सरकारी बहुमत बनाए रखा गया था।",
            "सभी प्रांतीय परिषदों में गैर-सरकारी बहुमत शुरू किया गया था।",
            "गैर-सरकारी बहुमत केवल बॉम्बे परिषद में शुरू किया गया था।",
            "प्रांतीय परिषदों में कोई सरकारी सदस्य नहीं थे।"
        ],
        "ans": 0,
        "sol": "1892 के अधिनियम के तहत, केंद्रीय परिषद और सभी प्रांतीय परिषदों दोनों में सरकारी बहुमत (ब्रिटिश अधिकारी) को सख्ती से बनाए रखा गया था।"
    },
    {
        "q": "भारतीय राष्ट्रीय कांग्रेस ने किस वर्ष विधायी परिषदों में सुधार की मांग करते हुए अपना पहला प्रस्ताव पारित किया था?",
        "opts": ["1885", "1888", "1890", "1892"],
        "ans": 0,
        "sol": "1885 में अपने उद्घाटन सत्र में, भारतीय राष्ट्रीय कांग्रेस ने विधायी परिषदों के सुधार और विस्तार की मांग करते हुए एक प्रस्ताव पारित किया था।"
    },
    {
        "q": "1892 का भारतीय परिषद अधिनियम जब तैयार और पेश किया गया, तब भारत के राज्य सचिव कौन थे?",
        "opts": ["लॉर्ड मार्ले", "लॉर्ड क्रॉस", "लॉर्ड सैलिसबरी", "लॉर्ड हैमिल्टन"],
        "ans": 1,
        "sol": "लॉर्ड क्रॉस भारत के राज्य सचिव थे जिन्होंने ब्रिटिश संसद में यह विधेयक पेश किया था।"
    },
    {
        "q": "विधायी सभा में कार्यपालिका से प्रश्न पूछने की संसदीय प्रक्रिया को औपचारिक रूप से क्या कहा जाता है?",
        "opts": ["इंटरपेलेशन (Interpellation)", "स्थगन (Adjournment)", "प्रस्ताव (Resolution)", "वीटो (Veto)"],
        "ans": 0,
        "sol": "इंटरपेलेशन (Interpellation) सभा के सदस्यों का कार्यपालिका से प्रश्न पूछने का औपचारिक अधिकार है।"
    },
    {
        "q": "निम्नलिखित में से कौन सा 1892 के अधिनियम के तहत निर्वाचक मंडल (electorate) की प्रकृति का वर्णन करता है?",
        "opts": [
            "सभी करदाताओं द्वारा प्रत्यक्ष मतदान।",
            "संस्थागत निकायों की सिफारिशों के माध्यम से अप्रत्यक्ष प्रतिनिधित्व।",
            "सभी कॉलेज स्नातकों के लिए सार्वभौमिक मताधिकार।",
            "धार्मिक समुदायों के आधार पर पृथक निर्वाचन मंडल।"
        ],
        "ans": 1,
        "sol": "कोई प्रत्यक्ष निर्वाचक मंडल नहीं था। नगर पालिकाओं, जिला बोर्डों और विश्वविद्यालयों जैसे स्थानीय निकायों द्वारा सिफारिशें की जाती थीं।"
    },
    {
        "q": "1892 के अधिनियम के तहत मनोनीत अतिरिक्त सदस्यों का कार्यकाल कितना था?",
        "opts": ["1 वर्ष", "2 वर्ष", "3 वर्ष", "5 वर्ष"],
        "ans": 1,
        "sol": "1861 के अधिनियम की तरह, 1892 के अधिनियम के तहत मनोनीत अतिरिक्त सदस्यों का कार्यकाल दो वर्ष ही रहा।"
    },
    {
        "q": "1892 के अधिनियम के तहत केंद्रीय विधायी परिषद में कुल सदस्यों में से कितने सदस्यों का गैर-सरकारी होना आवश्यक था?",
        "opts": ["कम से कम एक-तिहाई", "कम से कम दो-पांचवां", "कम से कम आधा", "कम से कम दो-तिहाई"],
        "ans": 1,
        "sol": "अधिनियम में प्रावधान था कि कम से कम दस अतिरिक्त सदस्य जोड़े जाएं, जिनमें से कम से कम दो-पांचवां हिस्सा गैर-सरकारी होना चाहिए।"
    },
    {
        "q": "1892 के अधिनियम के तहत इंटरपेलेशन (प्रश्न पूछने) के अधिकार के संबंध में निम्नलिखित में से कौन सा सही है?",
        "opts": [
            "इसने सदस्यों को बिना किसी प्रतिबंध के किसी भी विषय पर प्रश्न पूछने की अनुमति दी।",
            "इसने जनहित के मामलों पर प्रश्न पूछने की अनुमति दी, लेकिन वायसराय की मंजूरी के बिना सैन्य और विदेश मामलों पर प्रश्न पूछने पर रोक लगा दी।",
            "इसने केवल सैन्य मामलों पर प्रश्नों की अनुमति दी।",
            "यह केवल देशी राज्यों के मामलों तक सीमित था।"
        ],
        "ans": 1,
        "sol": "लोकहित के मामलों पर प्रश्न पूछे जा सकते थे, लेकिन सैन्य, विदेश नीति और सार्वजनिक ऋण जैसे क्षेत्रों के लिए पूर्व मंजूरी आवश्यक थी या उन्हें अस्वीकार किया जा सकता था।"
    },
    {
        "q": "1892 के अधिनियम के तहत यदि किसी सदस्य के प्रश्न को परिषद के अध्यक्ष द्वारा अस्वीकार कर दिया जाता था, तो क्या होता था?",
        "opts": [
            "सदस्य ब्रिटिश संसद में अपील कर सकता था।",
            "प्रश्न राज्य सचिव के पास भेजा जाता था।",
            "निर्णय अंतिम होता था और उसे किसी भी तरह से चुनौती नहीं दी जा सकती थी।",
            "सदस्य को परिषद से निलंबित कर दिया जाता था।"
        ],
        "ans": 2,
        "sol": "प्रश्न को अस्वीकार करने का अध्यक्ष का निर्णय पूर्ण और अंतिम था, जिसे कहीं भी चुनौती नहीं दी जा सकती थी।"
    },
    {
        "q": "1892 के अधिनियम के तहत निम्नलिखित में से किस निकाय ने मद्रास विधायी परिषद में गैर-सरकारी सदस्यों की सिफारिश की थी?",
        "opts": [
            "मद्रास चैंबर ऑफ कॉमर्स और नगर पालिकाएं",
            "बंगाल चैंबर ऑफ कॉमर्स",
            "सीधे वायसराय",
            "ब्रिटिश हाउस ऑफ लॉर्ड्स"
        ],
        "ans": 0,
        "sol": "मद्रास के स्थानीय निकायों, जिनमें मद्रास चैंबर ऑफ कॉमर्स और नगर पालिकाएं शामिल थीं, ने मद्रास के गवर्नर को सिफारिशें भेजी थीं।"
    },
    {
        "q": "1892 के भारतीय परिषद अधिनियम को एक महत्वपूर्ण संवैधानिक प्रगति माना जाता है क्योंकि:",
        "opts": [
            "इसने भारत में पूरी तरह से निर्वाचित कैबिनेट मंत्रियों की शुरुआत की।",
            "इसने अप्रत्यक्ष रूप से चुनाव के सिद्धांत को स्वीकार किया और विधायी कार्यों का विस्तार किया।",
            "इसने देशी रियासतों को प्रशासनिक स्वायत्तता प्रदान की।",
            "इसने न्यायपालिका को कार्यपालिका से अलग कर दिया।"
        ],
        "ans": 1,
        "sol": "यह एक बड़ी प्रगति थी क्योंकि इसने अप्रत्यक्ष रूप से चुनाव के सिद्धांत को स्वीकार किया और बजट चर्चा तथा प्रश्न पूछने जैसे विधायी कार्यों का विस्तार किया।"
    },
    {
        "q": "1892 के अधिनियम ने विधायी परिषदों पर वायसराय की समग्र शक्तियों को कैसे प्रभावित किया?",
        "opts": [
            "इसने वायसराय की शक्तियों में काफी कटौती की।",
            "इसने वायसराय के सर्वोच्च अधिकार को बनाए रखा, जिसमें वीटो शक्ति और नियम बनाने का अधिकार शामिल था।",
            "इसने वायसराय को परिषद के बहुमत के अधीन कर दिया।",
            "इसने वायसराय के वीटो को बंगाल चैंबर ऑफ कॉमर्स को सौंप दिया।"
        ],
        "ans": 1,
        "sol": "वायसराय के वीटो और नियम बनाने के सर्वोच्च अधिकार पूरी तरह से बने रहे, ताकि ब्रिटिश संप्रभुता सुरक्षित रहे।"
    },
    {
        "q": "1892 के अधिनियम की 'सिफारिश' प्रणाली के संबंध में निम्नलिखित में से कौन सा कथन सही है?",
        "opts": [
            "यह एक बाध्यकारी प्रक्रिया थी; वायसराय को हर अनुशंसित व्यक्ति को नामांकित करना पड़ता था।",
            "यह तकनीकी रूप से सलाहकार थी, लेकिन व्यवहार में वायसराय/गवर्नर इन सिफारिशों को स्वीकार करते थे।",
            "लगभग सभी मामलों में वायसराय द्वारा सिफारिशों को खारिज कर दिया जाता था।",
            "इसके लिए सिफारिशों पर मुगल सम्राट के वंशजों के हस्ताक्षर होना आवश्यक था।"
        ],
        "ans": 1,
        "sol": "तकनीकी रूप से यह बाध्यकारी नहीं था, लेकिन व्यवहार में इसे स्वीकार कर लिया जाता था, जिससे यह एक अप्रत्यक्ष चुनाव की तरह काम करता था।"
    },
    {
        "q": "भारत के स्वतंत्रता संग्राम में 'प्रतिनिधित्व के बिना कोई कर नहीं' की मांग पहली बार किस विधायी सीमा से जुड़ी थी?",
        "opts": [
            "1861 में बजट पर चर्चा पर पूर्ण प्रतिबंध।",
            "1892 में बजट पर मतदान करने के अधिकार पर रोक।",
            "1909 के पृथक निर्वाचन मंडल।",
            "1919 की द्वैध शासन प्रणाली।"
        ],
        "ans": 1,
        "sol": "कचूँकि 1892 के अधिनियम में बजट पर केवल चर्चा की अनुमति थी लेकिन मतदान नहीं, राष्ट्रवादियों ने वास्तविक मतदान शक्ति की मांग करते हुए प्रतिनिधित्व का नारा बुलंद किया।"
    },
    {
        "q": "1892 के अधिनियम के तहत केंद्रीय विधायी परिषद में अतिरिक्त सदस्यों की न्यूनतम संख्या कितनी तय की गई थी?",
        "opts": ["6 सदस्य", "8 सदस्य", "10 सदस्य", "12 सदस्य"],
        "ans": 2,
        "sol": "अअतिरिक्त विधायी सदस्यों की न्यूनतम संख्या बढ़ाकर 10 कर दी गई थी।"
    },
    {
        "q": "1892 के अधिनियम के तहत केंद्रीय विधायी परिषद में अतिरिक्त सदस्यों की अधिकतम संख्या कितनी तय की गई थी?",
        "opts": ["12 सदस्य", "16 सदस्य", "20 सदस्य", "24 सदस्य"],
        "ans": 1,
        "sol": "अअतिरिक्त विधायी सदस्यों की अधिकतम संख्या बढ़ाकर 16 कर दी गई थी।"
    },
    {
        "q": "1892 के भारतीय परिषद अधिनियम के तहत निम्नलिखित में से किस प्रांतीय विधायी परिषद का विस्तार नहीं किया गया था?",
        "opts": ["बॉम्बे", "मद्रास", "बंगाल", "पंजाब"],
        "ans": 3,
        "sol": "पंजाब की विधायी परिषद की स्थापना 1897 में 1861 के अधिनियम के तहत हुई थी। 1892 के अधिनियम ने बॉम्बे, मद्रास, बंगाल और NWFP की परिषदों का विस्तार किया।"
    },
    {
        "q": "1892 की सिफारिश प्रणाली के माध्यम से केंद्रीय विधायी परिषद में प्रवेश करने वाले पहले भारतीय सदस्यों में शामिल थे:",
        "opts": [
            "गोपाल कृष्ण गोखले और रास बिहारी घोष",
            "जवाहरलाल नेहरू और सरदार पटेल",
            "महात्मा गांधी और सुभाष चंद्र बोस",
            "बाल गंगाधर तिलक और बी.आर. अंबेडकर"
        ],
        "ans": 0,
        "sol": "गोपाल कृष्ण गोखले, रास बिहारी घोष और फिरोजशाह मेहता जैसे प्रमुख राष्ट्रवादी नेता इन सुधारों के तहत परिषद में शामिल हुए थे।"
    },
    {
        "q": "1893 में केंद्रीय विधायी परिषद में फिरोजशाह मेहता के प्रवेश के संदर्भ में, उनकी सिफारिश किसके द्वारा की गई थी?",
        "opts": [
            "बंगाल चैंबर ऑफ कॉमर्स",
            "बॉम्बे प्रांतीय विधायी परिषद",
            "मद्रास नगर पालिका",
            "सीधे वायसराय द्वारा"
        ],
        "ans": 1,
        "sol": "फिरोजशाह मेहता को बॉम्बे प्रांतीय विधायी परिषद द्वारा केंद्रीय विधायी परिषद के लिए अनुशंसित किया गया था।"
    },
    {
        "q": "प्रारंभिक राष्ट्रवादी नेताओं द्वारा 1892 के अधिनियम की एक प्रमुख आलोचना क्या थी?",
        "opts": [
            "इसने स्थानीय जिला बोर्डों को बहुत अधिक शक्तियां दीं।",
            "इसने मताधिकार को अत्यंत सीमित, अप्रत्यक्ष रखा और बजट पर मतदान का अधिकार नहीं दिया।",
            "इसने प्रांतीय परिषदों को समाप्त कर दिया।",
            "इसने देशी रियासतों को ब्रिटिश भारत पर शासन करने की अनुमति दी।"
        ],
        "ans": 1,
        "sol": "प्रारंभिक राष्ट्रवादियों ने इस अधिनियम की आलोचना की क्योंकि यह बजट पर मतदान करने या पूरक प्रश्न पूछने का अधिकार नहीं देता था, जिससे प्रतिनिधित्व केवल प्रतीकात्मक रहा।"
    },
    {
        "q": "1892 के अधिनियम के तहत बॉम्बे विधायी परिषद में कितने अतिरिक्त सदस्य जोड़े जाने थे?",
        "opts": ["न्यूनतम 4, अधिकतम 8", "न्यूनतम 8, अधिकतम 20", "न्यूनतम 10, अधिकतम 16", "न्यूनतम 12, अधिकतम 24"],
        "ans": 1,
        "sol": "बॉम्बे के लिए अतिरिक्त सदस्यों की संख्या बढ़ाकर न्यूनतम 8 और अधिकतम 20 कर दी गई थी।"
    },
    {
        "q": "1892 के अधिनियम के तहत मद्रास विधायी परिषद में कितने अतिरिक्त सदस्य जोड़े जाने थे?",
        "opts": ["न्यूनतम 4, अधिकतम 8", "न्यूनतम 8, अधिकतम 20", "न्यूनतम 10, अधिकतम 16", "न्यूनतम 12, अधिकतम 24"],
        "ans": 1,
        "sol": "मद्रास के लिए अतिरिक्त सदस्यों की संख्या बढ़ाकर न्यूनतम 8 और अधिकतम 20 कर दी गई थी।"
    },
    {
        "q": "1892 में शुरू की गई इंटरपेलेशन (प्रश्न पूछने) की शक्ति किस आधुनिक विधायी व्यवस्था की अग्रदूत थी?",
        "opts": ["शून्य काल (Zero Hour)", "प्रश्न काल (Question Hour)", "अविश्वास प्रस्ताव", "निंदा प्रस्ताव"],
        "ans": 1,
        "sol": "कार्यपालिका से प्रश्न पूछने का अधिकार आधुनिक भारतीय संसद के 'प्रश्न काल' का ऐतिहासिक पूर्ववृत्त है।"
    },
    {
        "q": "1892 के अधिनियम के तहत सदस्यों के नामांकन के लिए नियम और कानून बनाने के लिए कौन अधिकृत था?",
        "opts": [
            "वायसराय (भारत सचिव की मंजूरी के साथ)",
            "विशेष रूप से ब्रिटिश हाउस ऑफ कॉमन्स",
            "स्थानीय जिला बोर्ड",
            "कलकत्ता का सर्वोच्च न्यायालय"
        ],
        "ans": 0,
        "sol": "भारत में वायसराय को नामांकन के नियम बनाने का अधिकार दिया गया था, जो भारत सचिव की मंजूरी के अधीन था।"
    },
    {
        "q": "1892 के अधिनियम के तहत बजट पर चर्चा के संबंध में निम्नलिखित में से कौन सा सही है?",
        "opts": [
            "यह केवल तभी होता था जब वायसराय विशेष रूप से मतदान का अनुरोध करता था।",
            "यह सरकार की वित्तीय नीति और खातों पर एक सामान्य चर्चा थी।",
            "यह केवल सैन्य बजट तक सीमित था।",
            "यह केवल तभी आयोजित किया जाता था जब सरकार घाटे में होती थी।"
        ],
        "ans": 1,
        "sol": "यह एक सामान्य चर्चा थी जहाँ सदस्य करों, प्रशासन और वित्तीय नीतियों पर चिंता व्यक्त कर सकते थे, हालाँकि कोई मतदान नहीं होता था।"
    },
    {
        "q": "1892 के अधिनियम के तहत, निम्नलिखित में से किस प्रेसीडेंसी की विधायी परिषदों में अतिरिक्त सदस्य जोड़े गए थे?\n1. बॉम्बे\n2. मद्रास\n3. बंगाल\nसही उत्तर चुनें:",
        "opts": ["केवल 1 और 2", "ASCII 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans": 3,
        "sol": "तीनों प्रेसीडेंसियों—बॉम्बे, मद्रास और बंगाल—की विधायी परिषदों का विस्तार 1892 के अधिनियम के तहत किया गया था।"
    },
    {
        "q": "1892 का भारतीय परिषद अधिनियम किस पिछले मुख्य अधिनियम का संशोधन था?",
        "opts": ["भारत सरकार अधिनियम 1858", "1861 का भारतीय परिषद अधिनियम", "1773 का रेगुलेटिंग एक्ट", "1833 का चार्टर अधिनियम"],
        "ans": 1,
        "sol": "1892 का भारतीय परिषद अधिनियम वास्तव में 1861 के भारतीय परिषद अधिनियम में संशोधन करने के लिए पारित किया गया था।"
    },
    {
        "q": "1892 के बाद विधायी परिषदों की प्रकृति के संबंध में निम्नलिखित में से कौन सा सही है?",
        "opts": [
            "वे की विस्तारित विमर्शी शक्तियों वाली सलाहकार समितियाँ बनी रहीं।",
            "वे संप्रभु संसद बन गईं।",
            "वे स्थानीय देशी न्यायालयों के अधीन हो गईं।",
            "उन्हें कानून बनाने की शक्तियों से वंचित कर दिया गया।"
        ],
        "ans": 0,
        "sol": "परिषदों का दर्जा मुख्य रूप से वायसराय/गवर्नर के अधीन सलाहकार निकायों का ही रहा, यद्यपि उनके कार्यों का विस्तार किया गया था।"
    },
    {
        "q": "1892 में प्रतिनिधित्व के तत्व को शामिल करने का अंग्रेजों का मुख्य उद्देश्य क्या था?",
        "opts": [
            "भारत को तत्काल स्वशासन के लिए तैयार करना।",
            "कार्यकारी शक्ति को पूर्ण रखते हुए उदारवादी राष्ट्रवादियों को शांत करना।",
            "एक संघीय गणराज्य की स्थापना करना।",
            "गवर्नर-जनरल के वीटो को समाप्त करना।"
        ],
        "ans": 1,
        "sol": "ब्रिटिश सरकार वास्तविक सत्ता को अपने पास सुरक्षित रखते हुए भारतीय राष्ट्रीय कांग्रेस के उदारवादी नेताओं की शिकायतों को आंशिक रूप से शांत करना चाहती थी।"
    },
    {
        "q": "1892 के अधिनियम ने केंद्रीय और प्रांतीय विधायी परिषदों के बीच संबंधों को कैसे प्रभावित किया?",
        "opts": [
            "प्रांतीय परिषदों को केंद्रीय परिषद के सदस्यों के अधीन कर दिया गया।",
            "प्रांतीय परिषदों को केंद्रीय परिषद के लिए सदस्यों की सिफारिश करने का अधिकार दिया गया।",
            "प्रांतीय परिषदों को समाप्त कर दिया गया।",
            "प्रांतीय परिषदों को केंद्रीय परिषद में मिला दिया गया।"
        ],
        "ans": 1,
        "sol": "प्रांतीय विधायी परिषदों को केंद्रीय विधायी परिषद में गैर-सरकारी सदस्यों के नामांकन के लिए नाम अनुशंसित करने का अधिकार दिया गया था।"
    }
]

# ----------------- 10 UNIQUE MOCK QUESTIONS (HINDI) -----------------
mock_questions_hi = [
    {
        "q": "1892 के भारतीय परिषद अधिनियम के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. इसने ब्रिटिश भारत में पहली बार चुनाव के सिद्धांत की शुरुआत की।\n2. अधिनियम के प्रावधानों में 'चुनाव' (election) शब्द का स्पष्ट रूप से उपयोग किया गया था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 0,
        "sol": "कथन 1 सही है क्योंकि इसने अप्रत्यक्ष रूप से चुनाव सिद्धांत की शुरुआत की। कथन 2 गलत है क्योंकि अधिनियम के पाठ में 'चुनाव' शब्द से जानबूझकर परहेज किया गया था।"
    },
    {
        "q": "<strong>कथन (A):</strong> 1892 का भारतीय परिषद अधिनियम भारत के संवैधानिक इतिहास में एक मील का पत्थर है।<br><strong>कारण (R):</strong> इसने विधायी परिषदों को वित्तीय बजट पर चर्चा करने और कार्यपालिका से प्रश्न पूछने की अनुमति दी।<br>सही कोड चुनें:",
        "opts": [
            "A और R दोनों सत्य हैं और R, A की सही व्याख्या है",
            "A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है",
            "A सत्य है लेकिन R असत्य है",
            "A असत्य है लेकिन R सत्य है"
        ],
        "ans": 0,
        "sol": "कथन और कारण दोनों सही हैं। विधायी कार्यों का विस्तार करके बजट चर्चा और कार्यकारी प्रश्न पूछने की अनुमति देना ही इस अधिनियम को मील का पत्थर बनाता है।"
    },
    {
        "q": "1892 के भारतीय परिषद अधिनियम के तहत विधायी परिषदों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. प्रांतीय परिषदों में ब्रिटिश अधिकारियों के सरकारी बहुमत को समाप्त कर भारतीय गैर-सरकारी बहुमत लाया गया।\n2. प्रांतीय विधायी परिषदों को केंद्रीय विधायी परिषद के लिए सदस्यों की सिफारिश करने का अधिकार दिया गया था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 1,
        "sol": "कथन 1 गलत है क्योंकि सभी परिषदों में सरकारी बहुमत को सख्ती से बनाए रखा गया था। कथन 2 सही है।"
    },
    {
        "q": "1892 के अधिनियम के तहत प्रश्न पूछने के अधिकार के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\nकथन I: सदस्यों को सार्वजनिक हित के मामलों पर प्रश्न पूछने का अधिकार था, बशर्ते कि वे छह दिन का नोटिस दें।\nकथन II: यदि कार्यपालिका का उत्तर असंतोषजनक हो, तो सदस्य पूरक प्रश्न पूछ सकते थे।\nनिम्नलिखित में से कौन सा सही है?",
        "opts": [
            "कथन I सही है लेकिन कथन II गलत है",
            "कथन II सही है लेकिन कथन I गलत है",
            "कथन I और कथन II दोनों सही हैं",
            "कथन I और कथन II दोनों गलत हैं"
        ],
        "ans": 0,
        "sol": "कथन I सही है। कथन II गलत है क्योंकि 1892 के अधिनियम के तहत पूरक प्रश्न पूछने पर पूर्ण प्रतिबंध था।"
    },
    {
        "q": "1892 के भारतीय परिषद अधिनियम के तहत, निम्नलिखित में से किस निकाय ने प्रांतीय विधायी परिषदों के लिए गैर-सरकारी सदस्यों की सिफारिश की थी?\n1. विश्वविद्यालय\n2. नगर पालिकाएं\n3. जिला बोर्ड\n4. वाणिज्य मंडल (Chambers of Commerce)\nसही उत्तर चुनें:",
        "opts": ["केवल 1 और 2", "केवल 1, 2 और 3", "केवल 2 और 4", "1, 2, 3 और 4"],
        "ans": 3,
        "sol": "इन सभी स्थानीय नागरिक और वाणिज्यिक निकायों (विश्वविद्यालयों, नगर पालिकाओं, जिला बोर्डों और वाणिज्य मंडलों) को प्रांतीय परिषद के नामांकन के लिए सिफारिशें करने का अधिकार था।"
    },
    {
        "q": "1892 के अधिनियम के तहत बजट चर्चा के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. सदस्यों के पास सार्वजनिक व्यय से संबंधित प्रस्ताव रखने का अधिकार था।\n2. सदस्यों के पास बजट पर मतदान करने का अधिकार था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 3,
        "sol": "दोनों कथन गलत हैं। 1892 के अधिनियम के तहत सदस्य केवल बजट पर चर्चा कर सकते थे; वे न तो प्रस्ताव रख सकते थे और न ही मतदान कर सकते थे।"
    },
    {
        "q": "<strong>कथन (A):</strong> 1892 के भारतीय परिषद अधिनियम ने विधायी परिषदों में अप्रत्यक्ष चुनाव की शुरुआत की।<br><strong>कारण (R):</strong> गैर-सरकारी सीटें स्थानीय निकायों की सिफारिशों के आधार पर नामांकन के माध्यम से भरी जाती थीं।<br>सही कोड चुनें:",
        "opts": [
            "A और R दोनों सत्य हैं और R, A की सही व्याख्या है",
            "A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है",
            "A सत्य है लेकिन R असत्य है",
            "A असत्य है लेकिन R सत्य है"
        ],
        "ans": 0,
        "sol": "कथन और कारण दोनों सही हैं। सिफारिश प्रणाली अप्रत्यक्ष चुनाव की तरह काम करती थी, जो कथन की सही व्याख्या है।"
    },
    {
        "q": "1892 के अधिनियम के तहत केंद्रीय विधायी परिषद की संरचना के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. अतिरिक्त सदस्यों की न्यूनतम संख्या 10 निर्धारित की गई थी।\n2. अतिरिक्त सदस्यों की अधिकतम संख्या 16 निर्धारित की गई थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 2,
        "sol": "दोनों कथन सही हैं। अतिरिक्त सदस्यों की संख्या बढ़ाकर न्यूनतम 10 और अधिकतम 16 कर दी गई थी।"
    },
    {
        "q": "1892 के अधिनियम के तहत इंटरपेलेशन (प्रश्न पूछने) के अधिकार की मुख्य सीमा का वर्णन कौन सा कथन करता है?",
        "opts": [
            "परिषद के अध्यक्ष बिना कोई कारण बताए किसी भी प्रश्न को अस्वीकार कर सकते थे।",
            "सभी प्रश्नों को पहले ब्रिटिश प्रधानमंत्री द्वारा अनुमोदित किया जाना आवश्यक था।",
            "किसी भी भारतीय सदस्य को प्रश्न पूछने की अनुमति नहीं थी।",
            "प्रश्न केवल स्थानीय क्षेत्रीय भाषा में ही पूछे जा सकते थे।"
        ],
        "ans": 0,
        "sol": "अध्यक्ष के पास बिना कोई कारण बताए किसी भी प्रश्न को खारिज करने का पूर्ण अधिकार था, जो इसकी एक प्रमुख सीमा थी।"
    },
    {
        "q": "1892 के अधिनियम के ऐतिहासिक संदर्भ के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. यह अधिनियम लॉर्ड लैंसडाउन के वायसराय काल के दौरान पारित किया गया था।\n2. भारतीय राष्ट्रीय कांग्रेस ने इस अधिनियम का स्वागत किया क्योंकि यह उनकी मांगों को पूरी तरह से संतुष्ट करता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 0,
        "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि कांग्रेस इसकी सीमाओं (सीमित मताधिकार, बजट पर मतदान न होना, पूरक प्रश्नों पर रोक) से बहुत असंतुष्ट थी।"
    }
]

# ----------------- MASTERY QUESTIONS GENERATION -----------------
# 3 Sections for 1892 Act
SECTIONS = [
    {
        "id": 1,
        "title_en": "1. Expansion of Legislative Councils & Official Majority",
        "title_hi": "1. विधायी परिषदों का विस्तार और सरकारी बहुमत",
        "facts": [
            ("The Act expanded the number of additional (non-official) members in the Central Legislative Council.", "अधिनियम ने केंद्रीय विधायी परिषद में अतिरिक्त (गैर-सरकारी) सदस्यों की संख्या का विस्तार किया।"),
            ("The Central Council additional members were increased to a minimum of ten and a maximum of sixteen.", "केंद्रीय परिषद के अतिरिक्त सदस्यों की संख्या बढ़ाकर न्यूनतम दस और अधिकतम सोलह कर दी गई थी।"),
            ("In the provincial legislative councils, the number of additional members was also increased.", "प्रांतीय विधायी परिषदों में भी अतिरिक्त सदस्यों की संख्या में वृद्धि की गई थी।"),
            ("The British official majority was strictly maintained in both Central and provincial councils.", "केंद्रीय और प्रांतीय दोनों परिषदों में ब्रिटिश सरकारी बहुमत को सख्ती से बनाए रखा गया था।"),
            ("The non-official members in the Central Council were nominated by the Viceroy on recommendations.", "केंद्रीय परिषद में गैर-सरकारी सदस्यों को सिफारिशों के आधार पर वायसराय द्वारा नामांकित किया गया था।"),
            ("The provincial legislative councils were expanded, for instance, Bengal got twenty additional members.", "प्रांतीय विधायी परिषदों का विस्तार किया गया, उदाहरण के लिए, बंगाल को बीस अतिरिक्त सदस्य मिले।"),
            ("Official members were British officials who held a voting majority to pass any government bill.", "सरकारी सदस्य ब्रिटिश अधिकारी थे जिनके पास किसी भी सरकारी विधेयक को पारित करने के लिए मतदान का बहुमत था।"),
            ("The expansion was a response to persistent demands from the Indian National Congress.", "यह विस्तार भारतीय राष्ट्रीय कांग्रेस की निरंतर मांगों के जवाब में किया गया था।")
        ]
    },
    {
        "id": 2,
        "title_en": "2. Budget Discussion & Right to Ask Questions",
        "title_hi": "2. बजट चर्चा और प्रश्न पूछने का अधिकार",
        "facts": [
            ("The Act of 1892 permitted legislative council members to discuss the annual financial statement (budget).", "1892 के अधिनियम ने विधायी परिषद के सदस्यों को वार्षिक वित्तीय विवरण (बजट) पर चर्चा करने की अनुमति दी।"),
            ("Members were strictly prohibited from voting on the budget or proposing budget resolutions.", "सदस्यों को बजट पर मतदान करने या बजट से संबंधित प्रस्ताव पेश करने की सख्त मनाही थी।"),
            ("Members were granted the right to ask questions of the executive on public interest matters.", "सदस्यों को जनहित के मामलों पर कार्यपालिका से प्रश्न पूछने का अधिकार दिया गया था।"),
            ("A notice period of six days was mandatory before asking questions in the council.", "परिषद में प्रश्न पूछने से पहले छह दिन की नोटिस अवधि अनिवार्य थी।"),
            ("No supplementary questions or follow-ups were allowed under the 1892 Act.", "1892 के अधिनियम के तहत कोई पूरक प्रश्न या अनुवर्ती प्रश्न पूछने की अनुमति नहीं थी।"),
            ("The President of the Council held absolute power to disallow any question without reason.", "परिषद के अध्यक्ष के पास बिना कोई कारण बताए किसी भी प्रश्न को अस्वीकार करने का पूर्ण अधिकार था।"),
            ("The right to discuss the budget marked a key beginning of legislative oversight of finance.", "बजट पर चर्चा करने के अधिकार ने वित्त पर विधायी निरीक्षण की एक महत्वपूर्ण शुरुआत की।"),
            ("The right to ask questions formed the historical root of the modern parliamentary Question Hour.", "प्रश्न पूछने का अधिकार आधुनिक संसदीय प्रश्नकाल का ऐतिहासिक आधार बना।")
        ]
    },
    {
        "id": 3,
        "title_en": "3. Introduction of Representative Principle & Indirect Elections",
        "title_hi": "3. प्रतिनिधित्व सिद्धांत और अप्रत्यक्ष चुनाव की शुरुआत",
        "facts": [
            ("The Act introduced the representative principle indirectly by filling seats through recommendations.", "अधिनियम ने सिफारिशों के माध्यम से सीटों को भरकर अप्रत्यक्ष रूप से प्रतिनिधित्व सिद्धांत की शुरुआत की।"),
            ("The word 'election' was deliberately avoided in the official text of the 1892 Act.", "1892 के अधिनियम के आधिकारिक पाठ में 'चुनाव' शब्द से जानबूझकर परहेज किया गया था।"),
            ("Viceroy nominated Central Council non-officials on recommendations of provincial councils and Bengal Chamber of Commerce.", "वायसराय ने प्रांतीय परिषदों और बंगाल चैंबर ऑफ कॉमर्स की सिफारिशों पर केंद्रीय परिषद के गैर-सरकारी सदस्यों को मनोनीत किया।"),
            ("Governors nominated provincial council members on recommendations of local civic bodies.", "गवर्नरों ने स्थानीय नागरिक निकायों की सिफारिशों के आधार पर प्रांतीय परिषद के सदस्यों को मनोनीत किया।"),
            ("The recommending local bodies included municipalities, district boards, universities, and zamindars.", "सिफारिश करने वाले स्थानीय निकायों में नगर पालिकाएं, जिला बोर्ड, विश्वविद्यालय और जमींदार शामिल थे।"),
            ("The recommendations made the nomination process function practically as an indirect election.", "सिफारिशों ने नामांकन प्रक्रिया को व्यावहारिक रूप से एक अप्रत्यक्ष चुनाव के रूप में कार्य करने योग्य बनाया।"),
            ("The Bengal Chamber of Commerce was one of the key commercial bodies making recommendations.", "बंगाल चैंबर ऑफ कॉमर्स सिफारिशें करने वाले प्रमुख वाणिज्यिक निकायों में से एक था।"),
            ("The representative principle laid the conceptual path for future fully representative reforms.", "प्रतिनिधित्व के सिद्धांत ने भविष्य के पूर्ण प्रतिनिधि सुधारों के लिए वैचारिक मार्ग प्रशस्त किया।")
        ]
    }
]

# Section-specific Unique Questions definitions to prevent repetition

def generate_mcqs(sec, lang):
    mcqs = []
    # 5 unique MCQs per section
    if lang == "en":
        if sec["id"] == 1:
            # Q1
            mcqs.append({
                "type": "MCQ",
                "q": "What was the minimum number of additional members in the Central Legislative Council under the 1892 Act?",
                "opts": ["6 members", "8 members", "10 members", "12 members"],
                "ans": 2,
                "sol": "The minimum number of additional legislative members was increased to 10."
            })
            # Q2
            mcqs.append({
                "type": "MCQ",
                "q": "What was the maximum number of additional members in the Central Legislative Council under the 1892 Act?",
                "opts": ["12 members", "16 members", "20 members", "24 members"],
                "ans": 1,
                "sol": "The maximum number of additional legislative members was increased to 16."
            })
            # Q3
            mcqs.append({
                "type": "MCQ",
                "q": "Which body's persistent demands led to the expansion of councils under the 1892 Act?",
                "opts": ["East India Company", "Indian National Congress", "House of Lords", "Bengal Landholders Association"],
                "ans": 1,
                "sol": "The expansion was a direct response to the demands of the Indian National Congress (founded in 1885)."
            })
            # Q4
            mcqs.append({
                "type": "MCQ",
                "q": "Who held the voting majority to pass any government bill under the 1892 Act?",
                "opts": ["Indian non-official majority", "British official majority", "Joint native committee", "Bengal Chamber of Commerce"],
                "ans": 1,
                "sol": "The British official majority of government officials was strictly maintained in both Central and provincial councils."
            })
            # Q5
            mcqs.append({
                "type": "MCQ",
                "q": "Under the 1892 Act, how many additional members were added to the Bengal Legislative Council?",
                "opts": ["12 members", "15 members", "20 members", "25 members"],
                "ans": 2,
                "sol": "The provincial legislative council of Bengal was expanded to a maximum of 20 additional members."
            })
        elif sec["id"] == 2:
            # Q1
            mcqs.append({
                "type": "MCQ",
                "q": "Which of the following was allowed under the 1892 Act regarding the budget?",
                "opts": [
                    "Voting on specific tax cuts",
                    "Proposing resolutions on spending",
                    "Discussion of the annual financial statement",
                    "Absolute veto on military expenditure"
                ],
                "ans": 2,
                "sol": "The Act permitted legislative council members to discuss the annual financial statement (budget), though they could not vote on it."
            })
            # Q2
            mcqs.append({
                "type": "MCQ",
                "q": "What notice period was mandatory for asking questions under the 1892 Act?",
                "opts": ["3 days", "6 days", "10 days", "14 days"],
                "ans": 1,
                "sol": "A notice period of six days was mandatory before asking questions in the council."
            })
            # Q3
            mcqs.append({
                "type": "MCQ",
                "q": "Which of the following was strictly prohibited under the 1892 Act?",
                "opts": [
                    "Asking primary questions",
                    "Asking supplementary questions",
                    "Expressing views on civil departments",
                    "Reviewing public debt data"
                ],
                "ans": 1,
                "sol": "No supplementary questions or follow-ups were allowed under the 1892 Act."
            })
            # Q4
            mcqs.append({
                "type": "MCQ",
                "q": "Who held the power to disallow any question without reason under the 1892 Act?",
                "opts": ["The Secretary of State", "The President of the Council", "The Chief Justice", "The Prime Minister"],
                "ans": 1,
                "sol": "The President of the Council held absolute power to disallow any question without stating reasons."
            })
            # Q5
            mcqs.append({
                "type": "MCQ",
                "q": "The right to ask questions in the 1892 Act laid the foundation of which modern parliamentary process?",
                "opts": ["Zero Hour", "Question Hour", "No-Confidence Motion", "Adjournment Motion"],
                "ans": 1,
                "sol": "The right to ask questions formed the historical root of the modern parliamentary Question Hour."
            })
        else:
            # Q1
            mcqs.append({
                "type": "MCQ",
                "q": "Which principle was introduced for the first time in India by the 1892 Act?",
                "opts": ["Separate electorate", "Representative principle", "Universal franchise", "Dyarchy"],
                "ans": 1,
                "sol": "The Act introduced the representative principle indirectly by filling seats through recommendations."
            })
            # Q2
            mcqs.append({
                "type": "MCQ",
                "q": "Which word was carefully avoided in the text of the 1892 Act?",
                "opts": ["Nomination", "Recommendation", "Election", "Council"],
                "ans": 2,
                "sol": "The word 'election' was deliberately avoided in the official text of the 1892 Act."
            })
            # Q3
            mcqs.append({
                "type": "MCQ",
                "q": "Who recommended non-official members to the Central Legislative Council?",
                "opts": [
                    "Provincial councils and Bengal Chamber of Commerce",
                    "Municipalities and District Boards directly",
                    "The British Monarch",
                    "The Viceroy's cabinet exclusively"
                ],
                "ans": 0,
                "sol": "The Viceroy nominated Central Council non-officials on recommendations of provincial councils and Bengal Chamber of Commerce."
            })
            # Q4
            mcqs.append({
                "type": "MCQ",
                "q": "On whose recommendations did Governors nominate members to provincial councils?",
                "opts": [
                    "Local bodies like municipalities and district boards",
                    "The House of Commons",
                    "The Viceroy of India",
                    "Native princely states"
                ],
                "ans": 0,
                "sol": "Governors nominated provincial council members on recommendations of local civic bodies like district boards, municipalities, and universities."
            })
            # Q5
            mcqs.append({
                "type": "MCQ",
                "q": "Which commercial chamber had the right to recommend members to the Central Legislative Council?",
                "opts": [
                    "Bombay Chamber of Commerce",
                    "Bengal Chamber of Commerce",
                    "Madras Chamber of Commerce",
                    "London Chamber of Commerce"
                ],
                "ans": 1,
                "sol": "The Bengal Chamber of Commerce was one of the key commercial bodies making recommendations for the Central Council."
            })
    else:
        # Hindi MCQs
        if sec["id"] == 1:
            mcqs.append({
                "type": "MCQ",
                "q": "1892 के अधिनियम के तहत केंद्रीय विधायी परिषद में अतिरिक्त सदस्यों की न्यूनतम संख्या कितनी थी?",
                "opts": ["6 सदस्य", "8 सदस्य", "10 सदस्य", "12 सदस्य"],
                "ans": 2,
                "sol": "अतिरिक्त विधायी सदस्यों की न्यूनतम संख्या बढ़ाकर 10 कर दी गई थी।"
            })
            mcqs.append({
                "type": "MCQ",
                "q": "1892 के अधिनियम के तहत केंद्रीय विधायी परिषद में अतिरिक्त सदस्यों की अधिकतम संख्या कितनी थी?",
                "opts": ["12 सदस्य", "16 सदस्य", "20 सदस्य", "24 सदस्य"],
                "ans": 1,
                "sol": "अतिरिक्त विधायी सदस्यों की अधिकतम संख्या बढ़ाकर 16 कर दी गई थी।"
            })
            mcqs.append({
                "type": "MCQ",
                "q": "किस संस्था की निरंतर मांगों के कारण 1892 के अधिनियम के तहत परिषदों का विस्तार किया गया था?",
                "opts": ["ईस्ट इंडिया कंपनी", "भारतीय राष्ट्रीय कांग्रेस", "हाउस ऑफ लॉर्ड्स", "बंगाल जमींदार संघ"],
                "ans": 1,
                "sol": "परिषदों का विस्तार भारतीय राष्ट्रीय कांग्रेस (1885 में स्थापित) की मांगों के जवाब में किया गया था।"
            })
            mcqs.append({
                "type": "MCQ",
                "q": "1892 के अधिनियम के तहत किसी भी सरकारी विधेयक को पारित करने के लिए मतदान का बहुमत किसके पास था?",
                "opts": ["भारतीय गैर-सरकारी बहुमत", "ब्रिटिश सरकारी बहुमत", "संयुक्त देशी समिति", "बंगाल चैंबर ऑफ कॉमर्स"],
                "ans": 1,
                "sol": "केंद्रीय और प्रांतीय दोनों परिषदों में ब्रिटिश सरकारी अधिकारियों का सरकारी बहुमत सख्ती से बनाए रखा गया था।"
            })
            mcqs.append({
                "type": "MCQ",
                "q": "1892 के अधिनियम के तहत बंगाल विधायी परिषद में कितने अतिरिक्त सदस्य जोड़े गए थे?",
                "opts": ["12 सदस्य", "15 सदस्य", "20 सदस्य", "25 सदस्य"],
                "ans": 2,
                "sol": "बंगाल की प्रांतीय विधायी परिषद का विस्तार अधिकतम 20 अतिरिक्त सदस्यों तक किया गया था।"
            })
        elif sec["id"] == 2:
            mcqs.append({
                "type": "MCQ",
                "q": "बजट के संबंध में 1892 के अधिनियम के तहत निम्नलिखित में से किसकी अनुमति थी?",
                "opts": [
                    "विशिष्ट कर कटौती पर मतदान",
                    "खर्च पर प्रस्ताव पेश करना",
                    "वार्षिक वित्तीय विवरण पर चर्चा",
                    "सैन्य खर्च पर पूर्ण वीटो"
                ],
                "ans": 2,
                "sol": "अधिनियम ने विधायी परिषद के सदस्यों को वार्षिक वित्तीय विवरण (बजट) पर चर्चा करने की अनुमति दी, हालांकि वे मतदान नहीं कर सकते थे।"
            })
            mcqs.append({
                "type": "MCQ",
                "q": "1892 के अधिनियम के तहत प्रश्न पूछने के लिए कितने दिन पहले नोटिस देना अनिवार्य था?",
                "opts": ["3 दिन", "6 दिन", "10 दिन", "14 दिन"],
                "ans": 1,
                "sol": "परिषद में प्रश्न पूछने से पहले छह दिन की नोटिस अवधि अनिवार्य थी।"
            })
            mcqs.append({
                "type": "MCQ",
                "q": "1892 के अधिनियम के तहत निम्नलिखित में से क्या पूर्णतः प्रतिबंधित था?",
                "opts": [
                    "प्राथमिक प्रश्न पूछना",
                    "पूरक प्रश्न पूछना",
                    "नागरिक विभागों पर विचार व्यक्त करना",
                    "सार्वजनिक ऋण डेटा की समीक्षा करना"
                ],
                "ans": 1,
                "sol": "1892 के अधिनियम के तहत कोई भी पूरक प्रश्न (अनुवर्ती प्रश्न) पूछने की अनुमति नहीं थी।"
            })
            mcqs.append({
                "type": "MCQ",
                "q": "1892 के अधिनियम के तहत बिना कोई कारण बताए किसी भी प्रश्न को अस्वीकार करने की शक्ति किसके पास थी?",
                "opts": ["राज्य सचिव", "परिषद के अध्यक्ष", "मुख्य न्यायाधीश", "प्रधानमंत्री"],
                "ans": 1,
                "sol": "परिषद के अध्यक्ष के पास बिना कोई कारण बताए किसी भी प्रश्न को अस्वीकार करने का पूर्ण अधिकार था।"
            })
            mcqs.append({
                "type": "MCQ",
                "q": "1892 के अधिनियम में प्रश्न पूछने के अधिकार ने किस आधुनिक संसदीय प्रक्रिया की नींव रखी?",
                "opts": ["शून्य काल", "प्रश्न काल", "अविश्वास प्रस्ताव", "स्थगन प्रस्ताव"],
                "ans": 1,
                "sol": "प्रश्न पूछने का अधिकार आधुनिक संसदीय प्रश्नकाल का ऐतिहासिक आधार बना।"
            })
        else:
            mcqs.append({
                "type": "MCQ",
                "q": "1892 के अधिनियम द्वारा भारत में पहली बार कौन सा सिद्धांत पेश किया गया था?",
                "opts": ["पृथक निर्वाचन क्षेत्र", "प्रतिनिधित्व सिद्धांत", "सार्वभौमिक मताधिकार", "द्वैध शासन"],
                "ans": 1,
                "sol": "अधिनियम ने सिफारिशों के माध्यम से सीटों को भरकर अप्रत्यक्ष रूप से प्रतिनिधित्व सिद्धांत की शुरुआत की।"
            })
            mcqs.append({
                "type": "MCQ",
                "q": "1892 के अधिनियम के आधिकारिक पाठ में किस शब्द के प्रयोग से जानबूझकर बचा गया था?",
                "opts": ["नामांकन (Nomination)", "सिफारिश (Recommendation)", "चुनाव (Election)", "परिषद (Council)"],
                "ans": 2,
                "sol": "1892 के अधिनियम के आधिकारिक पाठ में 'चुनाव' शब्द से जानबूझकर परहेज किया गया था।"
            })
            mcqs.append({
                "type": "MCQ",
                "q": "केंद्रीय विधायी परिषद में गैर-सरकारी सदस्यों की सिफारिश किसने की थी?",
                "opts": [
                    "प्रांतीय परिषदों और बंगाल चैंबर ऑफ कॉमर्स",
                    "सीधे नगर पालिकाओं और जिला बोर्डों",
                    "ब्रिटिश सम्राट",
                    "विशेष रूप से वायसराय के कैबिनेट"
                ],
                "ans": 0,
                "sol": "वायसराय ने प्रांतीय परिषदों और बंगाल चैंबर ऑफ कॉमर्स की सिफारिशों पर केंद्रीय परिषद के गैर-सरकारी सदस्यों को मनोनीत किया।"
            })
            mcqs.append({
                "type": "MCQ",
                "q": "गवर्नरों ने किसकी सिफारिशों पर प्रांतीय परिषदों में सदस्यों को नामांकित किया था?",
                "opts": [
                    "नगर पालिकाओं और जिला बोर्डों जैसे स्थानीय निकायों",
                    "हाउस ऑफ कॉमन्स",
                    "भारत के वायसराय",
                    "देशी रियासतों"
                ],
                "ans": 0,
                "sol": "गवर्नरों ने नगर पालिकाओं, जिला बोर्डों और विश्वविद्यालयों जैसे स्थानीय नागरिक निकायों की सिफारिशों के आधार पर प्रांतीय परिषद के सदस्यों को नामांकित किया था।"
            })
            mcqs.append({
                "type": "MCQ",
                "q": "केंद्रीय विधायी परिषद में सदस्यों की सिफारिश करने का अधिकार किस व्यावसायिक चैंबर के पास था?",
                "opts": [
                    "बॉम्बे चैंबर ऑफ कॉमर्स",
                    "बंगाल चैंबर ऑफ कॉमर्स",
                    "मद्रास चैंबर ऑफ कॉमर्स",
                    "लंदन चैंबर ऑफ कॉमर्स"
                ],
                "ans": 1,
                "sol": "बंगाल चैंबर ऑफ कॉमर्स केंद्रीय परिषद के लिए सिफारिशें करने वाले प्रमुख व्यावसायिक निकायों में से एक था।"
            })
    return mcqs

def generate_mastery_multi_mcqs(sec, lang):
    mcqs = []
    # 5 unique Multiple Correct MCQs per section
    if lang == "en":
        if sec["id"] == 1:
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "Which of the following councils were expanded under the Indian Councils Act of 1892? (Select all that apply)",
                "opts": ["Central Legislative Council", "Bengal Provincial Council", "Bombay Provincial Council", "Punjab Provincial Council"],
                "ans": [0, 1, 2],
                "sol": "Central, Bengal, and Bombay councils were expanded. Punjab's council was established later in 1897, so it was not expanded in 1892."
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "Which elements of the Central Legislative Council were nominated by the Viceroy under the 1892 Act? (Select all that apply)",
                "opts": [
                    "Non-official members recommended by Bengal Chamber of Commerce",
                    "Non-official members recommended by provincial legislative councils",
                    "Official members recommended by the Secretary of State",
                    "Elected representatives voted by direct franchise"
                ],
                "ans": [0, 1],
                "sol": "Nominations were made on recommendations of provincial councils and the Bengal Chamber of Commerce. Official members were appointed directly, not based on local recommendations."
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "What were the key characteristics of the 'official majority' under the 1892 Act? (Select all that apply)",
                "opts": [
                    "Composed of British officers and civil servants",
                    "Maintained voting control to pass any government bill",
                    "Allowed the government to override non-official objections",
                    "Required matching approval from Indian native princes"
                ],
                "ans": [0, 1, 2],
                "sol": "The official majority consisted of British officials, held voting control, and allowed passing of government bills without non-official consent."
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "Which provincial councils had their maximum additional members expanded to 15 or more under the 1892 Act? (Select all that apply)",
                "opts": ["Bengal", "North-Western Provinces and Oudh", "Madras", "Punjab"],
                "ans": [0, 1, 2],
                "sol": "Bengal was raised to 20, NWP to 15, Madras to 20. Punjab's council was not yet created in 1892."
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "Which of the following describe the demands of the Indian National Congress regarding councils in 1885? (Select all that apply)",
                "opts": [
                    "Reform of the legislative councils",
                    "Admission of elected members to councils",
                    "Immediate dissolution of all provincial assemblies",
                    "Discussion of public finance and budgets"
                ],
                "ans": [0, 1, 3],
                "sol": "Congress demanded council reform, elective representation, and budget discussion, but did not seek dissolution of provincial assemblies."
            })
        elif sec["id"] == 2:
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "What rights did council members have regarding the budget under the 1892 Act? (Select all that apply)",
                "opts": [
                    "Discuss the annual financial statement",
                    "Express opinions on public revenue",
                    "Vote on budget expenditures",
                    "Propose resolutions to reduce specific taxes"
                ],
                "ans": [0, 1],
                "sol": "Members could discuss the budget and express opinions, but voting and proposing budget resolutions were strictly barred."
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "Which of the following were limitations of the questioning power in the 1892 Act? (Select all that apply)",
                "opts": [
                    "Mandated a six days' notice period",
                    "Supplementary questions were barred",
                    "President of the Council could disallow any question",
                    "Questions could only be asked in the House of Lords"
                ],
                "ans": [0, 1, 2],
                "sol": "Questioning required 6 days' notice, supplementaries were barred, and the President could disallow any question."
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "Under the 1892 Act, which subjects required prior sanction or were restricted for questions? (Select all that apply)",
                "opts": ["Military matters", "Foreign relations", "Public debt", "Local municipality budgets"],
                "ans": [0, 1, 2],
                "sol": "Imperial subjects like military affairs, foreign relations, and public debt required prior sanction or were disallowed."
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "How did the 1892 Act expand the functions of legislative councils compared to 1861? (Select all that apply)",
                "opts": [
                    "Allowed budget discussion",
                    "Allowed asking questions of the executive",
                    "Allowed members to declare war",
                    "Allowed appointing native ministers to the executive"
                ],
                "ans": [0, 1],
                "sol": "The 1892 Act added budget discussion and questioning. It did not allow declaring war or appointing native ministers."
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "Which statements are true about the President of the Council's power over questions? (Select all that apply)",
                "opts": [
                    "Could disallow any question without giving a reason",
                    "His decision was final and absolute",
                    "No appeal could be made against his decision",
                    "Required a majority vote of the council to disallow a question"
                ],
                "ans": [0, 1, 2],
                "sol": "The President had absolute, final power to disallow questions without reason; no council vote was needed."
            })
        else:
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "Which bodies were authorized to recommend non-official members to provincial councils under the 1892 Act? (Select all that apply)",
                "opts": ["Municipalities", "District Boards", "Universities", "Trade Unions"],
                "ans": [0, 1, 2],
                "sol": "District boards, municipalities, and universities recommended members. Modern trade unions were not in this category."
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "How was the elective principle implemented under the 1892 Act? (Select all that apply)",
                "opts": [
                    "Through nomination on recommendation of civic bodies",
                    "Indirectly through intermediate local councils",
                    "Avoiding the explicit word 'election' in the text",
                    "Through direct popular voting by all educated Indians"
                ],
                "ans": [0, 1, 2],
                "sol": "The elective principle was introduced indirectly via nomination on recommendations, avoiding the word 'election'. Direct voting was not used."
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "Who made recommendations for Central Legislative Council seats? (Select all that apply)",
                "opts": [
                    "Bengal Chamber of Commerce",
                    "Provincial Legislative Councils",
                    "The Indian National Congress directly",
                    "District boards directly to the Viceroy"
                ],
                "ans": [0, 1],
                "sol": "Recommendations for the Central Council came from provincial councils and the Bengal Chamber of Commerce."
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "What were the early nationalist criticisms of the 1892 representation system? (Select all that apply)",
                "opts": [
                    "The franchise was extremely narrow and elite-focused",
                    "The process of indirect election was too complex and symbolic",
                    "It gave too much representation to rural peasants",
                    "It left the final nominating veto with the Viceroy"
                ],
                "ans": [0, 1, 3],
                "sol": "Nationalists criticized the narrow franchise, indirect representation, and Viceroy's final veto."
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "Which statements are correct regarding the legal nature of 'recommendations'? (Select all that apply)",
                "opts": [
                    "They were technically advisory and not legally binding",
                    "The Viceroy/Governors held final nominating authority",
                    "In practice, recommendations were accepted and functioned as indirect elections",
                    "They required direct signature from the British Prime Minister"
                ],
                "ans": [0, 1, 2],
                "sol": "Recommendations were advisory but accepted in practice, and final authority remained with the Viceroy/Governor."
            })
    else:
        # Hindi versions
        if sec["id"] == 1:
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "1892 के भारतीय परिषद अधिनियम के तहत किन परिषदों का विस्तार किया गया था? (सभी लागू विकल्प चुनें)",
                "opts": ["केंद्रीय विधायी परिषद", "बंगाल प्रांतीय परिषद", "बॉम्बे प्रांतीय परिषद", "पंजाब प्रांतीय परिषद"],
                "ans": [0, 1, 2],
                "sol": "केंद्रीय, बंगाल और बॉम्बे परिषदों का विस्तार किया गया। पंजाब की परिषद 1897 में बनी थी।"
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "1892 के अधिनियम के तहत केंद्रीय विधायी परिषद के किन तत्वों को वायसराय द्वारा नामांकित किया गया था? (सभी लागू विकल्प चुनें)",
                "opts": [
                    "बंगाल चैंबर ऑफ कॉमर्स द्वारा अनुशंसित गैर-सरकारी सदस्य",
                    "प्रांतीय विधायी परिषदों द्वारा अनुशंसित गैर-सरकारी सदस्य",
                    "राज्य सचिव द्वारा अनुशंसित सरकारी सदस्य",
                    "प्रत्यक्ष मताधिकार द्वारा चुने गए प्रतिनिधि"
                ],
                "ans": [0, 1],
                "sol": "नामांकन प्रांतीय परिषदों और बंगाल चैंबर ऑफ कॉमर्स की सिफारिशों पर किए गए थे।"
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "1892 के अधिनियम के तहत 'सरकारी बहुमत' की प्रमुख विशेषताएं क्या थीं? (सभी लागू विकल्प चुनें)",
                "opts": [
                    "ब्रिटिश अधिकारियों और सिविल सेवकों से मिलकर बना था",
                    "किसी भी सरकारी विधेयक को पारित करने के लिए मतदान का नियंत्रण रखता था",
                    "सरकार को गैर-सरकारी आपत्तियों को दरकिनार करने की अनुमति देता था",
                    "भारतीय रियासतों से मिलान अनुमोदन की आवश्यकता थी"
                ],
                "ans": [0, 1, 2],
                "sol": "सरकारी बहुमत ब्रिटिश अधिकारियों का था, जो विधेयकों को पारित करने के लिए मतदान नियंत्रण रखता था।"
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "1892 के अधिनियम के तहत किन प्रांतीय परिषदों के अतिरिक्त सदस्यों की अधिकतम संख्या 15 या उससे अधिक की गई थी? (सभी लागू विकल्प चुनें)",
                "opts": ["बंगाल", "उत्तर-पश्चिमी प्रांत और अवध", "मद्रास", "पंजाब"],
                "ans": [0, 1, 2],
                "sol": "बंगाल को 20, NWP को 15, मद्रास को 20 किया गया। पंजाब की परिषद 1892 में नहीं बनी थी।"
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "1885 में परिषदों के संबंध में भारतीय राष्ट्रीय कांग्रेस की मांगों का वर्णन कौन सा कथन करता है? (सभी लागू विकल्प चुनें)",
                "opts": [
                    "विधायी परिषदों में सुधार",
                    "परिषदों में निर्वाचित सदस्यों का प्रवेश",
                    "सभी प्रांतीय विधानसभाओं को तुरंत भंग करना",
                    "सार्वजनिक वित्त और बजट पर चर्चा"
                ],
                "ans": [0, 1, 3],
                "sol": "कांग्रेस ने सुधार, निर्वाचित प्रतिनिधित्व और बजट चर्चा की मांग की थी।"
            })
        elif sec["id"] == 2:
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "1892 के अधिनियम के तहत बजट के संबंध में परिषद सदस्यों के पास क्या अधिकार थे? (सभी लागू विकल्प चुनें)",
                "opts": [
                    "वार्षिक वित्तीय विवरण पर चर्चा करना",
                    "सार्वजनिक राजस्व पर विचार व्यक्त करना",
                    "बजट व्यय पर मतदान करना",
                    "विशिष्ट करों को कम करने के प्रस्ताव रखना"
                ],
                "ans": [0, 1],
                "sol": "बजट पर चर्चा और विचार व्यक्त करने की अनुमति थी, लेकिन मतदान या प्रस्ताव रखना वर्जित था।"
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "1892 के अधिनियम में प्रश्न पूछने की शक्ति की क्या सीमाएँ थीं? (सभी लागू विकल्प चुनें)",
                "opts": [
                    "छह दिन की नोटिस अवधि अनिवार्य थी",
                    "पूरक प्रश्न पूछने पर रोक थी",
                    "परिषद के अध्यक्ष किसी भी प्रश्न को अस्वीकार कर सकते थे",
                    "प्रश्न केवल हाउस ऑफ लॉर्ड्स में ही पूछे जा सकते थे"
                ],
                "ans": [0, 1, 2],
                "sol": "6 दिन का नोटिस आवश्यक था, पूरक प्रश्नों पर रोक थी, और अध्यक्ष प्रश्नों को खारिज कर सकते थे।"
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "1892 के अधिनियम के तहत किन विषयों पर प्रश्न पूछने के लिए पूर्व मंजूरी आवश्यक थी या वे प्रतिबंधित थे? (सभी लागू विकल्प चुनें)",
                "opts": ["सैन्य मामले", "विदेशी संबंध", "सार्वजनिक ऋण", "स्थानीय नगर पालिका बजट"],
                "ans": [0, 1, 2],
                "sol": "सैन्य, विदेश संबंध और सार्वजनिक ऋण जैसे शाही विषयों पर प्रश्न पूछने के लिए पूर्व मंजूरी आवश्यक थी।"
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "1861 की तुलना में 1892 के अधिनियम ने विधायी परिषदों के कार्यों का विस्तार कैसे किया? (सभी लागू विकल्प चुनें)",
                "opts": [
                    "बजट चर्चा की अनुमति दी",
                    "कार्यपालिका से प्रश्न पूछने की अनुमति दी",
                    "सदस्यों को युद्ध घोषित करने की अनुमति दी",
                    "कार्यपालिका में देशी मंत्रियों की नियुक्ति की अनुमति दी"
                ],
                "ans": [0, 1],
                "sol": "1892 के अधिनियम ने बजट चर्चा और प्रश्न पूछने की शक्ति जोड़ी थी।"
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "प्रश्नों पर परिषद के अध्यक्ष की शक्ति के बारे में कौन से कथन सही हैं? (सभी लागू विकल्प चुनें)",
                "opts": [
                    "बिना कोई कारण बताए किसी भी प्रश्न को अस्वीकार कर सकते थे",
                    "उनका निर्णय अंतिम और पूर्ण था",
                    "उनके निर्णय के विरुद्ध कोई अपील नहीं की जा सकती थी",
                    "प्रश्न अस्वीकार करने के लिए परिषद के बहुमत वोट की आवश्यकता थी"
                ],
                "ans": [0, 1, 2],
                "sol": "अध्यक्ष के पास प्रश्नों को खारिज करने का अंतिम और पूर्ण अधिकार था, जिसके लिए किसी परिषद वोट की आवश्यकता नहीं थी।"
            })
        else:
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "1892 के अधिनियम के तहत प्रांतीय परिषदों में गैर-सरकारी सदस्यों की सिफारिश करने के लिए कौन से निकाय अधिकृत थे? (सभी लागू विकल्प चुनें)",
                "opts": ["नगर पालिकाएं", "जिला बोर्ड", "विश्वविद्यालय", "व्यापार संघ (Trade Unions)"],
                "ans": [0, 1, 2],
                "sol": "जिला बोर्ड, नगर पालिकाएं और विश्वविद्यालय सिफारिशें करते थे।"
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "1892 के अधिनियम के तहत प्रतिनिधित्व सिद्धांत को कैसे लागू किया गया था? (सभी लागू विकल्प चुनें)",
                "opts": [
                    "नागरिक निकायों की सिफारिशों पर नामांकन के माध्यम से",
                    "मध्यवर्ती स्थानीय परिषदों के माध्यम से अप्रत्यक्ष रूप से",
                    "पाठ में स्पष्ट रूप से 'चुनाव' शब्द से बचते हुए",
                    "सभी शिक्षित भारतीयों द्वारा प्रत्यक्ष लोकप्रिय मतदान के माध्यम से"
                ],
                "ans": [0, 1, 2],
                "sol": "प्रतिनिधित्व सिद्धांत सिफारिशों पर नामांकन के माध्यम से अप्रत्यक्ष रूप से पेश किया गया था, जिसमें 'चुनाव' शब्द से परहेज किया गया।"
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "केंद्रीय विधायी परिषद की सीटों के लिए किसने सिफारिशें की थीं? (सभी लागू विकल्प चुनें)",
                "opts": [
                    "बंगाल चैंबर ऑफ कॉमर्स",
                    "प्रांतीय विधायी परिषदें",
                    "सीधे भारतीय राष्ट्रीय कांग्रेस",
                    "सीधे वायसराय को जिला बोर्ड"
                ],
                "ans": [0, 1],
                "sol": "केंद्रीय परिषद के लिए सिफारिशें प्रांतीय परिषदों और बंगाल चैंबर ऑफ कॉमर्स से आती थीं।"
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "1892 की प्रतिनिधित्व प्रणाली की प्रारंभिक राष्ट्रवादी आलोचनाएँ क्या थीं? (सभी लागू विकल्प चुनें)",
                "opts": [
                    "मताधिकार अत्यंत संकीर्ण और कुलीन-केंद्रित था",
                    "अप्रत्यक्ष चुनाव की प्रक्रिया बहुत जटिल और प्रतीकात्मक थी",
                    "इसने ग्रामीण किसानों को बहुत अधिक प्रतिनिधित्व दिया",
                    "इसने अंतिम नामांकन वीटो वायसराय के पास छोड़ दिया"
                ],
                "ans": [0, 1, 3],
                "sol": "राष्ट्रवादियों ने सीमित मताधिकार, अप्रत्यक्ष प्रतिनिधित्व और वायसराय के वीटो की आलोचना की थी।"
            })
            mcqs.append({
                "type": "Multiple Correct MCQ",
                "q": "सिफारिशों की कानूनी प्रकृति के संबंध में कौन से कथन सही हैं? (सभी लागू विकल्प चुनें)",
                "opts": [
                    "वे तकनीकी रूप से सलाहकार थीं और कानूनी रूप से बाध्यकारी नहीं थीं",
                    "वायसराय/गवर्नर के पास अंतिम नामांकन अधिकार थे",
                    "व्यवहार में, सिफारिशें स्वीकार की जाती थीं और अप्रत्यक्ष चुनाव के रूप में काम करती थीं",
                    "उनके लिए ब्रिटिश प्रधानमंत्री के सीधे हस्ताक्षर की आवश्यकता थी"
                ],
                "ans": [0, 1, 2],
                "sol": "सिफारिशें सलाहकार थीं लेकिन व्यावहारिक रूप से स्वीकृत थीं, और अंतिम निर्णय वायसराय/गवर्नर का था।"
            })
    return mcqs

def generate_tf(sec, lang):
    tf = []
    for i in range(8):
        fact = sec["facts"][i % len(sec["facts"])]
        txt = fact[0] if lang == "en" else fact[1]
        is_true = (i % 2 == 0)
        
        if is_true:
            q = f"True or False: {txt}" if lang == "en" else f"सत्य या असत्य: {txt}"
            ans = True
            sol = "This statement is correct according to the historical provisions." if lang == "en" else "ऐतिहासिक प्रावधानों के अनुसार यह कथन बिल्कुल सही है।"
        else:
            if lang == "en":
                false_txt = txt.replace("1892", "1861").replace("ten", "five").replace("sixteen", "thirty").replace("six days", "ten days").replace("Viceroy", "British Monarch").replace("majority", "minority").replace("Bengal", "Punjab").replace("supplementary", "unlimited")
                if false_txt == txt:
                    false_txt = "Not true that: " + txt
                q = f"True or False: {false_txt}"
                ans = False
                sol = f"This statement is false. The correct fact is: {txt}"
            else:
                false_txt = txt.replace("1892", "1861").replace("दस", "पांच").replace("सोलह", "तीस").replace("छह दिन", "दस दिन").replace("वायसराय", "ब्रिटिश सम्राट").replace("बहुमत", "अल्पमत").replace("बंगाल", "पंजाब").replace("पूरक", "असीमित")
                if false_txt == txt:
                    false_txt = "यह सच नहीं है कि: " + txt
                q = f"सत्य या असत्य: {false_txt}"
                ans = False
                sol = f"यह कथन असत्य है। सही तथ्य यह है: {txt}"
                
        tf.append({
            "type": "True/False",
            "q": q,
            "ans": is_true,
            "sol": sol
        })
    return tf

def generate_blanks(sec, lang):
    blanks = []
    for i in range(8):
        fact = sec["facts"][i % len(sec["facts"])]
        txt = fact[0] if lang == "en" else fact[1]
        
        if lang == "en":
            if "1892" in txt:
                q = txt.replace("1892", "______")
                ans = "1892"
            elif "Viceroy" in txt:
                q = txt.replace("Viceroy", "______")
                ans = "Viceroy"
            elif "six days" in txt:
                q = txt.replace("six days", "______")
                ans = "six days"
            elif "budget" in txt:
                q = txt.replace("budget", "______")
                ans = "budget"
            elif "official majority" in txt:
                q = txt.replace("official majority", "______")
                ans = "official majority"
            elif "election" in txt:
                q = txt.replace("election", "______")
                ans = "election"
            else:
                q = txt.replace("ten", "______")
                ans = "ten"
                
            blanks.append({
                "type": "Fill in the Blank",
                "q": f"Fill in the blank: {q}",
                "ans": ans,
                "sol": f"The correct answer is {ans}. Complete statement: {txt}"
            })
        else:
            # Hindi
            if "1892" in txt:
                q = txt.replace("1892", "______")
                ans = "1892"
            elif "वायसराय" in txt:
                q = txt.replace("वायसराय", "______")
                ans = "वायसराय"
            elif "छह दिन" in txt:
                q = txt.replace("छह दिन", "______")
                ans = "छह दिन"
            elif "बजट" in txt:
                q = txt.replace("बजट", "______")
                ans = "बजट"
            elif "सरकारी बहुमत" in txt:
                q = txt.replace("सरकारी बहुमत", "______")
                ans = "सरकारी बहुमत"
            elif "चुनाव" in txt:
                q = txt.replace("चुनाव", "______")
                ans = "चुनाव"
            else:
                q = txt.replace("दस", "______")
                ans = "दस"
                
            blanks.append({
                "type": "Fill in the Blank",
                "q": f"रिक्त स्थान भरें: {q}",
                "ans": ans,
                "sol": f"सही उत्तर {ans} है। पूरा कथन: {txt}"
            })
    return blanks

def generate_match(sec, lang):
    match = []
    # 3 unique matching questions
    for i in range(3):
        if lang == "en":
            if sec["id"] == 1:
                if i == 0:
                    items = [
                        {"left": "I. Central Council additional members", "key": "A"},
                        {"left": "II. Bengal Council additional members", "key": "B"},
                        {"left": "III. NWF Province additional members", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "Minimum 10 and Maximum 16"},
                        {"val": "B", "text": "Expanded up to 20 members"},
                        {"val": "C", "text": "Expanded up to 15 members"}
                    ]
                    sol = "Central Council (I-A), Bengal Council (II-B), NWFP (III-C)."
                elif i == 1:
                    items = [
                        {"left": "I. Official members", "key": "A"},
                        {"left": "II. Non-official members", "key": "B"},
                        {"left": "III. Viceroy", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "Government officers holding majority"},
                        {"val": "B", "text": "Recommended by local bodies"},
                        {"val": "C", "text": "Vested with final nomination power"}
                    ]
                    sol = "Official members (I-A), Non-official members (II-B), Viceroy (III-C)."
                else:
                    items = [
                        {"left": "I. 1861 Central limit", "key": "A"},
                        {"left": "II. 1892 Central limit", "key": "B"},
                        {"left": "III. Official majority status", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "6 to 12 additional members"},
                        {"val": "B", "text": "10 to 16 additional members"},
                        {"val": "C", "text": "Strictly maintained by the British"}
                    ]
                    sol = "1861 limit (I-A), 1892 limit (II-B), Official majority (III-C)."
            elif sec["id"] == 2:
                if i == 0:
                    items = [
                        {"left": "I. Financial statement", "key": "A"},
                        {"left": "II. Question submission", "key": "B"},
                        {"left": "III. Supplementary questions", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "Allowed budget discussion, no voting"},
                        {"val": "B", "text": "Mandated six days' prior notice"},
                        {"val": "C", "text": "Strictly barred under the 1892 Act"}
                    ]
                    sol = "Financial statement (I-A), Notice period (II-B), Supplementaries (III-C)."
                elif i == 1:
                    items = [
                        {"left": "I. Interpellation", "key": "A"},
                        {"left": "II. President of Council", "key": "B"},
                        {"left": "III. Discussion limits", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "The right to ask questions of executive"},
                        {"val": "B", "text": "Empowered to disallow any question"},
                        {"val": "C", "text": "No power to vote or move resolutions"}
                    ]
                    sol = "Interpellation (I-A), President's power (II-B), Discussion limits (III-C)."
                else:
                    items = [
                        {"left": "I. 1861 Financial rules", "key": "A"},
                        {"left": "II. 1892 Financial rules", "key": "B"},
                        {"left": "III. Questioning limits", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "Financial discussions completely barred"},
                        {"val": "B", "text": "Budget discussion allowed, no voting"},
                        {"val": "C", "text": "Limited to primary questions only"}
                    ]
                    sol = "1861 rules (I-A), 1892 rules (II-B), Questioning limits (III-C)."
            else:
                if i == 0:
                    items = [
                        {"left": "I. 'Election' word", "key": "A"},
                        {"left": "II. Recommending body", "key": "B"},
                        {"left": "III. Central nomination", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "Deliberately avoided in the official text"},
                        {"val": "B", "text": "Municipalities and chambers of commerce"},
                        {"val": "C", "text": "Vested in the Viceroy based on recommendations"}
                    ]
                    sol = "Election word (I-A), Recommending body (II-B), Central nomination (III-C)."
                elif i == 1:
                    items = [
                        {"left": "I. Bengal Chamber", "key": "A"},
                        {"left": "II. Provincial Councils", "key": "B"},
                        {"left": "III. District Boards", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "Recommended commercial seats to Central Council"},
                        {"val": "B", "text": "Recommended seats to Central Legislative Council"},
                        {"val": "C", "text": "Recommended seats to Provincial Councils"}
                    ]
                    sol = "Bengal Chamber (I-A), Provincial Councils (II-B), District Boards (III-C)."
                else:
                    items = [
                        {"left": "I. Elective Principle", "key": "A"},
                        {"left": "II. 1892 System", "key": "B"},
                        {"left": "III. 1909 System", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "Laid conceptual path for future reforms"},
                        {"val": "B", "text": "Indirect election via recommendations"},
                        {"val": "C", "text": "Direct election with limited franchise"}
                    ]
                    sol = "Elective Principle (I-A), 1892 System (II-B), 1909 System (III-C)."
        else:
            # Hindi matching
            if sec["id"] == 1:
                if i == 0:
                    items = [
                        {"left": "I. केंद्रीय परिषद अतिरिक्त सदस्य", "key": "A"},
                        {"left": "II. बंगाल परिषद अतिरिक्त सदस्य", "key": "B"},
                        {"left": "III. NWF प्रांत अतिरिक्त सदस्य", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "न्यूनतम 10 और अधिकतम 16"},
                        {"val": "B", "text": "अधिकतम 20 सदस्यों तक विस्तारित"},
                        {"val": "C", "text": "अधिकतम 15 सदस्यों तक विस्तारित"}
                    ]
                    sol = "केंद्रीय परिषद (I-A), बंगाल परिषद (II-B), NWFP (III-C)।"
                elif i == 1:
                    items = [
                        {"left": "I. सरकारी सदस्य", "key": "A"},
                        {"left": "II. गैर-सरकारी सदस्य", "key": "B"},
                        {"left": "III. वायसराय", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "बहुमत रखने वाले सरकारी अधिकारी"},
                        {"val": "B", "text": "स्थानीय निकायों द्वारा अनुशंसित"},
                        {"val": "C", "text": "अंतिम नामांकन शक्ति से युक्त"}
                    ]
                    sol = "सरकारी सदस्य (I-A), गैर-सरकारी सदस्य (II-B), वायसराय (III-C)।"
                else:
                    items = [
                        {"left": "I. 1861 केंद्रीय सीमा", "key": "A"},
                        {"left": "II. 1892 केंद्रीय सीमा", "key": "B"},
                        {"left": "III. सरकारी बहुमत की स्थिति", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "6 से 12 अतिरिक्त सदस्य"},
                        {"val": "B", "text": "10 से 16 अतिरिक्त सदस्य"},
                        {"val": "C", "text": "अंग्रेजों द्वारा सख्ती से बनाए रखा गया"}
                    ]
                    sol = "1861 सीमा (I-A), 1892 सीमा (II-B), सरकारी बहुमत (III-C)।"
            elif sec["id"] == 2:
                if i == 0:
                    items = [
                        {"left": "I. वित्तीय विवरण (बजट)", "key": "A"},
                        {"left": "II. प्रश्न प्रस्तुत करना", "key": "B"},
                        {"left": "III. पूरक प्रश्न", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "बजट पर चर्चा की अनुमति, मतदान नहीं"},
                        {"val": "B", "text": "छह दिन के पूर्व नोटिस की आवश्यकता"},
                        {"val": "C", "text": "1892 के अधिनियम के तहत पूर्णतः वर्जित"}
                    ]
                    sol = "वित्तीय विवरण (I-A), नोटिस अवधि (II-B), पूरक प्रश्न (III-C)।"
                elif i == 1:
                    items = [
                        {"left": "I. इंटरपेलेशन (प्रश्नकाल)", "key": "A"},
                        {"left": "II. परिषद के अध्यक्ष", "key": "B"},
                        {"left": "III. चर्चा की सीमाएं", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "कार्यपालिका से प्रश्न पूछने का अधिकार"},
                        {"val": "B", "text": "किसी भी प्रश्न को अस्वीकार करने का अधिकार"},
                        {"val": "C", "text": "मतदान या प्रस्ताव रखने का कोई अधिकार नहीं"}
                    ]
                    sol = "इंटरपेलेशन (I-A), अध्यक्ष की शक्ति (II-B), चर्चा की सीमाएं (III-C)।"
                else:
                    items = [
                        {"left": "I. 1861 वित्तीय नियम", "key": "A"},
                        {"left": "II. 1892 वित्तीय नियम", "key": "B"},
                        {"left": "III. प्रश्न पूछने की सीमाएं", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "वित्तीय चर्चा पूरी तरह से प्रतिबंधित"},
                        {"val": "B", "text": "बजट चर्चा की अनुमति, मतदान नहीं"},
                        {"val": "C", "text": "केवल प्राथमिक प्रश्नों तक सीमित"}
                    ]
                    sol = "1861 नियम (I-A), 1892 नियम (II-B), प्रश्न पूछने की सीमाएं (III-C)।"
            else:
                if i == 0:
                    items = [
                        {"left": "I. 'चुनाव' शब्द", "key": "A"},
                        {"left": "II. सिफारिशी निकाय", "key": "B"},
                        {"left": "III. केंद्रीय नामांकन", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "आधिकारिक पाठ में जानबूझकर परहेज किया गया"},
                        {"val": "B", "text": "नगर पालिकाएं और वाणिज्य मंडल"},
                        {"val": "C", "text": "सिफारिशों के आधार पर वायसराय में निहित"}
                    ]
                    sol = "चुनाव शब्द (I-A), सिफारिशी निकाय (II-B), केंद्रीय नामांकन (III-C)।"
                elif i == 1:
                    items = [
                        {"left": "I. बंगाल चैंबर", "key": "A"},
                        {"left": "II. प्रांतीय परिषदें", "key": "B"},
                        {"left": "III. जिला बोर्ड", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "केंद्रीय परिषद में व्यापारिक सीटों की सिफारिश की"},
                        {"val": "B", "text": "केंद्रीय विधायी परिषद में सीटों की सिफारिश की"},
                        {"val": "C", "text": "प्रांतीय परिषदों में सीटों की सिफारिश की"}
                    ]
                    sol = "बंगाल चैंबर (I-A), प्रांतीय परिषदें (II-B), जिला बोर्ड (III-C)।"
                else:
                    items = [
                        {"left": "I. चुनावी सिद्धांत", "key": "A"},
                        {"left": "II. 1892 की प्रणाली", "key": "B"},
                        {"left": "III. 1909 की प्रणाली", "key": "C"}
                    ]
                    options = [
                        {"val": "A", "text": "भविष्य के सुधारों के लिए वैचारिक मार्ग प्रशस्त किया"},
                        {"val": "B", "text": "सिफारिशों के माध्यम से अप्रत्यक्ष चुनाव"},
                        {"val": "C", "text": "सीमित मताधिकार के साथ प्रत्यक्ष चुनाव"}
                    ]
                    sol = "चुनावी सिद्धांत (I-A), 1892 प्रणाली (II-B), 1909 प्रणाली (III-C)।"
                
        match.append({
            "type": "Match the Following",
            "q": "Match the items of Column I with the correct descriptions in Column II:" if lang == "en" else "स्तंभ I की मदों का स्तंभ II के सही विवरणों से मिलान करें:",
            "items": items,
            "options": options,
            "sol": sol
        })
    return match

def generate_oneliners(sec, lang):
    oneline = []
    for i in range(8):
        fact = sec["facts"][i % len(sec["facts"])]
        txt = fact[0] if lang == "en" else fact[1]
        
        oneline.append({
            "type": "One-Liner",
            "q": f"Identify the legislative detail described: {txt}" if lang == "en" else f"वर्णित विधायी विवरण की पहचान करें: {txt}",
            "sol": f"This refers to the core provision under the 1892 reforms: {txt}" if lang == "en" else f"यह 1892 के सुधारों के तहत मुख्य प्रावधान को संदर्भित करता है: {txt}"
        })
    return oneline

def generate_assertion_reasons(sec, lang):
    ar = []
    for i in range(8):
        fact1 = sec["facts"][i % len(sec["facts"])]
        fact2 = sec["facts"][(i + 1) % len(sec["facts"])]
        txt1 = fact1[0] if lang == "en" else fact1[1]
        txt2 = fact2[0] if lang == "en" else fact2[1]
        
        if lang == "en":
            q = f"<strong>Assertion (A):</strong> {txt1}<br><strong>Reason (R):</strong> {txt2}."
            ar.append({
                "type": "Assertion-Reason",
                "q": q,
                "opts": [
                    "Both A and R are true and R is the correct explanation of A",
                    "Both A and R are true but R is not the correct explanation of A",
                    "A is true but R is false",
                    "A is false but R is true"
                ],
                "ans": 1,
                "sol": "Both statements represent true historical facts of the 1892 Act."
            })
        else:
            q = f"<strong>कथन (A):</strong> {txt1}<br><strong>कारण (R):</strong> {txt2}."
            ar.append({
                "type": "Assertion-Reason",
                "q": q,
                "opts": [
                    "A और R दोनों सत्य हैं और R, A की सही व्याख्या है",
                    "A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है",
                    "A सत्य है लेकिन R असत्य है",
                    "A असत्य है लेकिन R सत्य है"
                ],
                "ans": 1,
                "sol": "दोनों कथन 1892 के अधिनियम के सत्य ऐतिहासिक तथ्यों का प्रतिनिधित्व करते हैं।"
            })
    return ar

def generate_statement_based(sec, lang):
    sb = []
    for i in range(5):
        fact1 = sec["facts"][i % len(sec["facts"])]
        fact2 = sec["facts"][(i + 2) % len(sec["facts"])]
        txt1 = fact1[0] if lang == "en" else fact1[1]
        txt2 = fact2[0] if lang == "en" else fact2[1]
        
        if lang == "en":
            q = f"Consider the following statements:<br>Statement I: {txt1}<br>Statement II: {txt2}"
            sb.append({
                "type": "Statement-Based",
                "q": q,
                "opts": [
                    "Statement I is correct but Statement II is incorrect",
                    "Statement II is correct but Statement I is incorrect",
                    "Both Statement I and Statement II are correct",
                    "Both Statement I and Statement II are incorrect"
                ],
                "ans": 2,
                "sol": "Both statements contain true provisions of the 1892 Act."
            })
        else:
            q = f"निम्नलिखित कथनों पर विचार करें:<br>कथन I: {txt1}<br>कथन II: {txt2}"
            sb.append({
                "type": "Statement-Based",
                "q": q,
                "opts": [
                    "कथन I सही है लेकिन कथन II गलत है",
                    "कथन II सही है लेकिन कथन I गलत है",
                    "कथन I और कथन II दोनों सही हैं",
                    "कथन I और कथन II दोनों गलत हैं"
                ],
                "ans": 2,
                "sol": "दोनों कथनों में 1892 के अधिनियम के सत्य प्रावधान शामिल हैं।"
            })
    return sb

def generate_why(sec, lang):
    why = []
    # 3 unique questions
    for i in range(3):
        if lang == "en":
            if sec["id"] == 1:
                if i == 0:
                    q = "Why did the British expand the councils while maintaining an official majority?"
                    sol = "To pacify moderate Indian demands for representation while ensuring the British administration retained absolute voting power to pass any bill."
                elif i == 1:
                    q = "Why did the Indian National Congress demand reform of the legislative councils in 1885?"
                    sol = "To ensure greater representation and voice for Indians in the administration of their own country."
                else:
                    q = "Why were provincial councils like Bengal given a larger maximum member limit than the Central council?"
                    sol = "Because provincial administrations managed larger local populations and required more diverse regional representatives."
            elif sec["id"] == 2:
                if i == 0:
                    q = "Why was voting on the budget prohibited under the 1892 Act?"
                    sol = "The British executive did not want to compromise its absolute control over public finance and tax collections to non-official members."
                elif i == 1:
                    q = "Why were supplementary questions barred under the 1892 Act?"
                    sol = "To prevent Indian members from cross-examining British officials and exposing flaws in administration."
                else:
                    q = "Why was a six days' notice required for asking questions?"
                    sol = "To give the executive ample time to draft answers and screen out politically sensitive inquiries."
            else:
                if i == 0:
                    q = "Why did the British Parliament deliberately avoid using the word 'election' in the Act?"
                    sol = "Due to conservative opposition in Britain to introducing democratic electoral principles in India, so it was legally framed as nomination by recommendation."
                elif i == 1:
                    q = "Why did the British allow local bodies to recommend members?"
                    sol = "To associate influential local classes (zamindars, merchants, academics) with the administration to secure their loyalty."
                else:
                    q = "Why did early nationalists critique the recommendation system?"
                    sol = "Because it was highly indirect, restricted to a tiny elite, and left the final power of appointment with the Viceroy."
        else:
            # Hindi
            if sec["id"] == 1:
                if i == 0:
                    q = "अंग्रेजों ने सरकारी बहुमत बनाए रखते हुए परिषदों का विस्तार क्यों किया?"
                    sol = "ब्रिटिश प्रशासन द्वारा विधेयकों को पारित करने के लिए मतदान का पूर्ण अधिकार बनाए रखने को सुनिश्चित करते हुए प्रतिनिधित्व के लिए मध्यम भारतीय मांगों को शांत करने के लिए।"
                elif i == 1:
                    q = "भारतीय राष्ट्रीय कांग्रेस ने 1885 में विधायी परिषदों में सुधार की मांग क्यों की थी?"
                    sol = "यह सुनिश्चित करने के लिए कि भारतीयों को अपने देश के प्रशासन में अधिक प्रतिनिधित्व और आवाज मिले।"
                else:
                    q = "बंगाल जैसे प्रांतीय परिषदों को केंद्रीय परिषद की तुलना में अधिक सदस्य सीमा क्यों दी गई थी?"
                    sol = "क्योंकि प्रांतीय प्रशासन बड़ी स्थानीय आबादी का प्रबंधन करते थे और उन्हें अधिक विविध क्षेत्रीय प्रतिनिधियों की आवश्यकता थी।"
            elif sec["id"] == 2:
                if i == 0:
                    q = "1892 के अधिनियम के तहत बजट पर मतदान को क्यों प्रतिबंधित किया गया था?"
                    sol = "ब्रिटिश कार्यपालिका सार्वजनिक वित्त और कर संग्रह पर अपना पूर्ण नियंत्रण गैर-सरकारी सदस्यों को सौंपना नहीं चाहती थी।"
                elif i == 1:
                    q = "1892 के अधिनियम के तहत पूरक प्रश्न पूछने पर क्यों रोक लगाई गई थी?"
                    sol = "भारतीय सदस्यों को ब्रिटिश अधिकारियों से जिरह करने और प्रशासन में कमियों को उजागर करने से रोकने के लिए।"
                else:
                    q = "प्रश्न पूछने के लिए छह दिन का नोटिस क्यों आवश्यक था?"
                    sol = "कार्यपालिका को उत्तर तैयार करने और राजनीतिक रूप से संवेदनशील प्रश्नों को स्क्रीन करने के लिए पर्याप्त समय देने के लिए।"
            else:
                if i == 0:
                    q = "ब्रिटिश संसद ने अधिनियम में जानबूझकर 'चुनाव' शब्द का उपयोग करने से क्यों परहेज किया?"
                    sol = "भारत में लोकतांत्रिक चुनावी सिद्धांतों को शुरू करने के लिए ब्रिटेन में रूढ़िवादी विरोध के कारण, इसलिए इसे कानूनी रूप से सिफारिश द्वारा नामांकन के रूप में तैयार किया गया था।"
                elif i == 1:
                    q = "अंग्रेजों ने स्थानीय निकायों को सदस्यों की सिफारिश करने की अनुमति क्यों दी?"
                    sol = "प्रभावशाली स्थानीय वर्गों (जमींदारों, व्यापारियों, शिक्षाविदों) को उनकी वफादारी हासिल करने के लिए प्रशासन से जोड़ना।"
                else:
                    q = "प्रारंभिक राष्ट्रवादियों ने सिफारिश प्रणाली की आलोचना क्यों की?"
                    sol = "क्योंकि यह अत्यधिक अप्रत्यक्ष थी, एक छोटे से अभिजात वर्ग तक सीमित थी, और नियुक्ति की अंतिम शक्ति वायसराय के पास छोड़ दी थी।"
                
        why.append({
            "type": "Why",
            "q": q,
            "sol": sol
        })
    return why

def generate_how(sec, lang):
    how = []
    # 3 unique questions
    for i in range(3):
        if lang == "en":
            if sec["id"] == 1:
                if i == 0:
                    q = "How did the 1892 Act expand the size of the Central Legislative Council?"
                    sol = "By raising the number of additional members from the 1861 range of 6-12 to a minimum of 10 and a maximum of 16."
                elif i == 1:
                    q = "How was the official majority maintained in the Central Legislative Council?"
                    sol = "By ensuring that the number of official British government members always exceeded the number of non-official members."
                else:
                    q = "How did the 1892 Act respond to the demands of the Indian National Congress?"
                    sol = "By conceding a minor expansion of legislative councils and allowing limited discussion on budgets, though failing to grant full representation."
            elif sec["id"] == 2:
                if i == 0:
                    q = "How did the 1892 Act initiate financial oversight in the legislative councils?"
                    sol = "By granting members the right to discuss the annual financial statement (budget), which was previously completely prohibited."
                elif i == 1:
                    q = "How did the President of the Council control the right of interpellation?"
                    sol = "By exercising absolute authority to disallow any question without stating reasons, keeping debate restricted."
                else:
                    q = "How did the 1892 Act initiate executive accountability?"
                    sol = "By allowing members to ask questions of the executive, starting the practice of public questioning of state policy."
            else:
                if i == 0:
                    q = "How did the recommendation system function as an indirect election?"
                    sol = "Local civic bodies recommended candidates to the Governor/Viceroy, who then formally nominated those candidates to the councils."
                elif i == 1:
                    q = "How did the Bengal Chamber of Commerce influence the Central Legislative Council?"
                    sol = "By having the exclusive right to recommend a commercial member, ensuring British business interests were protected."
                else:
                    q = "How did the 1892 reforms lay the groundwork for the 1909 Morley-Minto reforms?"
                    sol = "By proving the feasibility of Indian representation, which led to demands for direct elections and larger councils."
        else:
            # Hindi
            if sec["id"] == 1:
                if i == 0:
                    q = "1892 के अधिनियम ने केंद्रीय विधायी परिषद के आकार का विस्तार कैसे किया?"
                    sol = "अतिरिक्त सदस्यों की संख्या को 1861 की 6-12 की सीमा से बढ़ाकर न्यूनतम 10 और अधिकतम 16 करके।"
                elif i == 1:
                    q = "केंद्रीय विधायी परिषद में सरकारी बहुमत कैसे बनाए रखा गया था?"
                    sol = "यह सुनिश्चित करके कि सरकारी ब्रिटिश सदस्यों की संख्या हमेशा गैर-सरकारी सदस्यों की संख्या से अधिक हो।"
                else:
                    q = "1892 के अधिनियम ने भारतीय राष्ट्रीय कांग्रेस की मांगों का जवाब कैसे दिया?"
                    sol = "विधायी परिषदों के मामूली विस्तार को स्वीकार करके और बजट पर सीमित चर्चा की अनुमति देकर, हालांकि पूर्ण प्रतिनिधित्व देने में विफल रहा।"
            elif sec["id"] == 2:
                if i == 0:
                    q = "1892 के अधिनियम ने विधायी परिषदों में वित्तीय निरीक्षण की शुरुआत कैसे की?"
                    sol = "सदस्यों को वार्षिक वित्तीय विवरण (बजट) पर चर्चा करने का अधिकार देकर, जो पहले पूरी तरह से प्रतिबंधित था।"
                elif i == 1:
                    q = "परिषद के अध्यक्ष ने प्रश्नकाल (interpellation) के अधिकार को कैसे नियंत्रित किया?"
                    sol = "बिना कोई कारण बताए किसी भी प्रश्न को अस्वीकार करने के अपने पूर्ण अधिकार का प्रयोग करके, चर्चा को सीमित रखा।"
                else:
                    q = "1892 के अधिनियम ने कार्यपालिका की जवाबदेही कैसे शुरू की?"
                    sol = "सदस्यों को कार्यपालिका से प्रश्न पूछने की अनुमति देकर, राज्य की नीति पर जनता द्वारा प्रश्न पूछने की प्रथा शुरू की।"
            else:
                if i == 0:
                    q = "1892 की सिफारिश प्रणाली ने अप्रत्यक्ष चुनाव के रूप में कैसे काम किया?"
                    sol = "स्थानीय नागरिक निकाय उम्मीदवारों की सिफारिश गवर्नर/वायसराय को करते थे, जो फिर औपचारिक रूप से उन उम्मीदवारों को परिषदों में नामांकित करते थे।"
                elif i == 1:
                    q = "बंगाल चैंबर ऑफ कॉमर्स ने केंद्रीय विधायी परिषद को कैसे प्रभावित किया?"
                    sol = "एक व्यापारिक सदस्य की सिफारिश करने का अनन्य अधिकार प्राप्त करके, यह सुनिश्चित किया कि ब्रिटिश व्यावसायिक हित सुरक्षित रहें।"
                else:
                    q = "1892 के सुधारों ने 1909 के मार्ले-मिंटो सुधारों के लिए आधार कैसे तैयार किया?"
                    sol = "भारतीय प्रतिनिधित्व की व्यवहार्यता को साबित करके, जिसके कारण प्रत्यक्ष चुनाव और बड़ी परिषदों की मांग उठी।"
                
        how.append({
            "type": "How",
            "q": q,
            "sol": sol
        })
    return how

def generate_case_studies(sec, lang):
    cs = []
    # 3 unique questions
    for i in range(3):
        if lang == "en":
            if sec["id"] == 1:
                if i == 0:
                    q = "Analyze a case where a nationalist member wants to block a British bill in the Central Council of 1893."
                    sol = "The nationalist member would fail because the British official majority had more votes than the expanded non-official members, guaranteeing the bill's passage."
                elif i == 1:
                    q = "An Indian merchant from Calcutta wants to join the Central Legislative Council under the 1892 reforms. Analyze the process they must go through."
                    sol = "They must secure a recommendation from the Bengal Chamber of Commerce or a provincial council, which the Viceroy then uses to formally nominate them."
                else:
                    q = "The Bengal Legislative Council in 1894 proposes a local sanitation bill that is opposed by the British members. Analyze how the official majority affects this bill."
                    sol = "The bill would be defeated because the British official majority retains absolute control over the provincial council voting process."
            elif sec["id"] == 2:
                if i == 0:
                    q = "Analyze a case where Gopal Krishna Gokhale wants to ask a follow-up question in the legislative council after the Finance Member replies to his query."
                    sol = "His request would be denied because supplementary questions were strictly prohibited under the 1892 Act."
                elif i == 1:
                    q = "A member of the Bombay Legislative Council in 1894 wants to introduce a resolution to reduce land revenue tax. Analyze the validity of this action."
                    sol = "The action would be disallowed because members had no power to propose resolutions or vote on budget matters."
                else:
                    q = "A member wishes to ask a question regarding secret military movements on the North-Western frontier in 1894. Analyze how the President of the Council would handle this."
                    sol = "The President would disallow the question under his absolute power, as it concerns sensitive imperial defense matters."
            else:
                if i == 0:
                    q = "A municipal board in Bombay in 1893 selects a candidate to represent them in the provincial council. Describe the final steps to seat this member."
                    sol = "The board submits the recommendation to the Governor of Bombay, who then formally nominates the candidate to the provincial legislative council."
                elif i == 1:
                    q = "In 1893, the Viceroy rejects a recommended candidate from a provincial council. Analyze if this is legally permitted."
                    sol = "Yes, it is legally permitted because recommendations were technically advisory and the Viceroy held absolute nominating authority."
                else:
                    q = "The Bengal Chamber of Commerce recommends a British merchant to the Central Legislative Council in 1894. Analyze how this affects Indian representation."
                    sol = "It represents commercial interests, but since the member is British, it does not increase native Indian representation in the council."
        else:
            # Hindi
            if sec["id"] == 1:
                if i == 0:
                    q = "एक ऐसे मामले का विश्लेषण करें जहां एक राष्ट्रवादी सदस्य 1893 की केंद्रीय परिषद में ब्रिटिश विधेयक को रोकना चाहता है।"
                    sol = "राष्ट्रवादी सदस्य विफल हो जाएगा क्योंकि ब्रिटिश सरकारी बहुमत के पास विस्तारित गैर-सरकारी सदस्यों की तुलना में अधिक वोट थे, जिससे विधेयक का पारित होना सुनिश्चित था।"
                elif i == 1:
                    q = "कलकत्ता का एक भारतीय व्यापारी 1892 के सुधारों के तहत केंद्रीय विधायी परिषद में शामिल होना चाहता है। विश्लेषण करें कि उसे किस प्रक्रिया से गुजरना होगा।"
                    sol = "उसे बंगाल चैंबर ऑफ कॉमर्स या प्रांतीय परिषद से सिफारिश प्राप्त करनी होगी, जिसे वायसराय औपचारिक रूप से नामांकित करने के लिए उपयोग करता है।"
                else:
                    q = "बंगाल विधायी परिषद 1894 में एक स्थानीय स्वच्छता विधेयक का प्रस्ताव करती है जिसका ब्रिटिश सदस्यों द्वारा विरोध किया जाता है। विश्लेषण करें कि सरकारी बहुमत इस विधेयक को कैसे प्रभावित करता है।"
                    sol = "विधेयक हार जाएगा क्योंकि ब्रिटिश सरकारी बहुमत प्रांतीय परिषद की मतदान प्रक्रिया पर पूर्ण नियंत्रण रखता है।"
            elif sec["id"] == 2:
                if i == 0:
                    q = "एक ऐसे मामले का विश्लेषण करें जहां गोपाल कृष्ण गोखले वित्त सदस्य द्वारा उनके प्रश्न का उत्तर देने के बाद विधायी परिषद में एक अनुवर्ती प्रश्न पूछना चाहते हैं।"
                    sol = "उनका अनुरोध अस्वीकार कर दिया जाएगा क्योंकि 1892 के अधिनियम के तहत पूरक प्रश्न पूछना सख्त वर्जित था।"
                elif i == 1:
                    q = "1894 में बॉम्बे विधायी परिषद का एक सदस्य भूमि राजस्व कर को कम करने के लिए एक प्रस्ताव पेश करना चाहता है। इस कार्रवाई की वैधता का विश्लेषण करें।"
                    sol = "कार्रवाई को अस्वीकार कर दिया जाएगा क्योंकि सदस्यों के पास बजट मामलों पर प्रस्ताव रखने या मतदान करने की कोई शक्ति नहीं थी।"
                else:
                    q = "एक सदस्य 1894 में उत्तर-पश्चिमी सीमा पर गुप्त सैन्य गतिविधियों के संबंध में प्रश्न पूछना चाहता है। विश्लेषण करें कि परिषद के अध्यक्ष इसे कैसे संभालेंगे।"
                    sol = "अध्यक्ष अपने पूर्ण अधिकार के तहत प्रश्न को अस्वीकार कर देंगे, क्योंकि यह संवेदनशील शाही रक्षा मामलों से संबंधित है।"
            else:
                if i == 0:
                    q = "1893 में बॉम्बे में एक नगरपालिका बोर्ड प्रांतीय परिषद में उनका प्रतिनिधित्व करने के लिए एक उम्मीदवार का चयन करता है। इस सदस्य को सीट देने के अंतिम चरणों का वर्णन करें।"
                    sol = "बोर्ड बॉम्बे के गवर्नर को सिफारिश सौंपता है, जो औपचारिक रूप से प्रांतीय विधायी परिषद में उम्मीदवार को नामांकित करते हैं।"
                elif i == 1:
                    q = "1893 में, वायसराय प्रांतीय परिषद के एक अनुशंसित उम्मीदवार को खारिज कर देते हैं। विश्लेषण करें कि क्या यह कानूनी रूप से अनुमत है।"
                    sol = "हाँ, यह कानूनी रूप से अनुमत है क्योंकि सिफारिशें तकनीकी रूप से सलाहकार थीं और वायसराय के पास पूर्ण नामांकन अधिकार था।"
                else:
                    q = "बंगाल चैंबर ऑफ कॉमर्स 1894 में केंद्रीय विधायी परिषद के लिए एक ब्रिटिश व्यापारी की सिफारिश करता है। विश्लेषण करें कि यह भारतीय प्रतिनिधित्व को कैसे प्रभावित करता है।"
                    sol = "यह वाणिज्यिक हितों का प्रतिनिधित्व करता है, लेकिन चूंकि सदस्य ब्रिटिश है, यह परिषद में मूल भारतीय प्रतिनिधित्व को नहीं बढ़ाता है।"
                
        cs.append({
            "type": "Case Study",
            "q": q,
            "sol": sol
        })
    return cs

def generate_teach(sec, lang):
    teach = []
    # 3 unique questions
    for i in range(3):
        if lang == "en":
            if sec["id"] == 1:
                if i == 0:
                    q = "Explain the political reasons for the expansion of legislative councils under the 1892 Act."
                    sol = "The expansion was a concession to the newly formed Indian National Congress (1885), giving Indians a larger voice in administration while maintaining absolute British veto and official majority."
                elif i == 1:
                    q = "Explain the concept of 'Official Majority' and its imperial significance."
                    sol = "Official majority ensured that the British government always had enough votes to pass any law or budget, preventing any democratic deadlock."
                else:
                    q = "Explain why the expansion of councils in 1892 did not lead to self-government."
                    sol = "Because the executive remained completely unaccountable to the councils, and the British retained voting majorities and absolute veto power."
            elif sec["id"] == 2:
                if i == 0:
                    q = "Explain the historical importance of the right of interpellation introduced in 1892."
                    sol = "It was the absolute beginning of parliamentary accountability of the executive to the legislature in India, establishing a precedent for modern Question Hour."
                elif i == 1:
                    q = "Explain the difference between budget discussion and budget voting."
                    sol = "Discussion allowed members to voice opinions and criticisms. Voting allowed members to approve or reject expenditure, which was denied in 1892."
                else:
                    q = "Explain the historical significance of the 1892 questioning rules."
                    sol = "They marked the birth of parliamentary oversight and question hour in India, despite heavy imperial restrictions."
            else:
                if i == 0:
                    q = "Explain the relationship between the 1892 recommendation system and modern elections."
                    sol = "The recommendation system was the first practical experiment with indirect election. It created a transition from pure executive nomination to elective representation."
                elif i == 1:
                    q = "Explain why the 1892 Act is said to have introduced 'indirect elections'."
                    sol = "Because while the word 'election' was not used, the process of local bodies selecting and recommending candidates functioned practically as an indirect election."
                else:
                    q = "Explain the significance of the Bengal Chamber of Commerce in the 1892 representation scheme."
                    sol = "It was the sole commercial body given the right to recommend members to the Central Council, reflecting the priority of British trade interests."
        else:
            # Hindi
            if sec["id"] == 1:
                if i == 0:
                    q = "1892 के अधिनियम के तहत विधायी परिषदों के विस्तार के राजनीतिक कारणों की व्याख्या करें।"
                    sol = "यह विस्तार नवनिर्मित भारतीय राष्ट्रीय कांग्रेस (1885) के लिए एक रियायत थी, जिससे प्रशासन में भारतीयों को अधिक आवाज मिली, जबकि पूर्ण ब्रिटिश वीटो और सरकारी बहुमत बना रहा।"
                elif i == 1:
                    q = "सरकारी बहुमत की अवधारणा और इसके साम्राज्यवादी महत्व की व्याख्या करें।"
                    sol = "सरकारी बहुमत ने यह सुनिश्चित किया कि ब्रिटिश सरकार के पास हमेशा किसी भी कानून या बजट को पारित करने के लिए पर्याप्त वोट हों, जिससे किसी भी लोकतांत्रिक गतिरोध को रोका जा सके।"
                else:
                    q = "व्याख्या करें कि 1892 में परिषदों के विस्तार से स्वशासन क्यों नहीं आया।"
                    sol = "क्योंकि कार्यपालिका परिषदों के प्रति पूरी तरह से गैर-जवाबदेह रही, और अंग्रेजों ने मतदान के बहुमत और पूर्ण वीटो शक्तियों को अपने पास सुरक्षित रखा।"
            elif sec["id"] == 2:
                if i == 0:
                    q = "1892 में शुरू किए गए इंटरपेलेशन (प्रश्न पूछने के अधिकार) के ऐतिहासिक महत्व की व्याख्या करें।"
                    sol = "यह भारत में विधायिका के प्रति कार्यपालिका की संसदीय जवाबदेही की पूर्ण शुरुआत थी, जिसने आधुनिक प्रश्न काल के लिए एक मिसाल कायम की।"
                elif i == 1:
                    q = "बजट पर चर्चा और बजट पर मतदान के बीच अंतर स्पष्ट करें।"
                    sol = "चर्चा ने सदस्यों को अपने विचार और आलोचना व्यक्त करने की अनुमति दी। मतदान ने सदस्यों को खर्चों को स्वीकार या अस्वीकार करने की अनुमति दी, जिसे 1892 में मना कर दिया गया था।"
                else:
                    q = "1892 के प्रश्न पूछने के नियमों के ऐतिहासिक महत्व की व्याख्या करें।"
                    sol = "उन्होंने भारी साम्राज्यवादी प्रतिबंधों के बावजूद भारत में विधायी निरीक्षण और प्रश्नकाल के जन्म का संकेत दिया।"
            else:
                if i == 0:
                    q = "1892 की सिफारिश प्रणाली और आधुनिक चुनावों के बीच संबंधों की व्याख्या करें।"
                    sol = "सिफारिश प्रणाली अप्रत्यक्ष चुनाव का पहला व्यावहारिक प्रयोग थी। इसने शुद्ध कार्यकारी नामांकन से चुनावी प्रतिनिधित्व की ओर एक संक्रमण काल का निर्माण किया।"
                elif i == 1:
                    q = "व्याख्या करें कि ऐसा क्यों कहा जाता है कि 1892 के अधिनियम ने 'अप्रत्यक्ष चुनाव' की शुरुआत की थी।"
                    sol = "क्योंकि भले ही 'चुनाव' शब्द का इस्तेमाल नहीं किया गया था, लेकिन स्थानीय निकायों द्वारा उम्मीदवारों का चयन करने और सिफारिश करने की प्रक्रिया व्यावहारिक रूप से एक अप्रत्यक्ष चुनाव के रूप में काम करती थी।"
                else:
                    q = "1892 की प्रतिनिधित्व योजना में बंगाल चैंबर ऑफ कॉमर्स के महत्व की व्याख्या करें।"
                    sol = "यह एकमात्र व्यापारिक निकाय था जिसे केंद्रीय परिषद में सदस्यों की सिफारिश करने का अधिकार दिया गया था, जो ब्रिटिश व्यापारिक हितों की प्राथमिकता को दर्शाता है।"
                
        teach.append({
            "type": "Teach the Concept",
            "q": q,
            "sol": sol
        })
    return teach

def main():
    for lang in ["en", "hi"]:
        data = {
            "sections": []
        }
        
        for sec in SECTIONS:
            sec_title = sec["title_en"] if lang == "en" else sec["title_hi"]
            
            mastery_zone = []
            mastery_zone.extend(generate_mcqs(sec, lang))
            mastery_zone.extend(generate_mastery_multi_mcqs(sec, lang))
            mastery_zone.extend(generate_tf(sec, lang))
            mastery_zone.extend(generate_blanks(sec, lang))
            mastery_zone.extend(generate_match(sec, lang))
            mastery_zone.extend(generate_oneliners(sec, lang))
            mastery_zone.extend(generate_assertion_reasons(sec, lang))
            mastery_zone.extend(generate_statement_based(sec, lang))
            mastery_zone.extend(generate_why(sec, lang))
            mastery_zone.extend(generate_how(sec, lang))
            mastery_zone.extend(generate_case_studies(sec, lang))
            mastery_zone.extend(generate_teach(sec, lang))
            
            assert len(mastery_zone) == 62, f"Section {sec['id']} has {len(mastery_zone)} questions instead of 62"
            
            data["sections"].append({
                "title": sec_title,
                "masteryZone": mastery_zone
            })
            
        if lang == "hi":
            out_file = os.path.join(HI_DIR, "mastery.json")
        else:
            out_file = os.path.join(BASE_DIR, "mastery.json")
            
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"Generated {out_file} successfully.")

    # Also output practice data
    with open(os.path.join(BASE_DIR, "practice.json"), "w", encoding="utf-8") as f:
        json.dump({"practiceQuestions": practice_questions, "mockTestQuestions": mock_questions}, f, ensure_ascii=False, indent=2)

    with open(os.path.join(HI_DIR, "practice.json"), "w", encoding="utf-8") as f:
        json.dump({"practiceQuestions": practice_questions_hi, "mockTestQuestions": mock_questions_hi}, f, ensure_ascii=False, indent=2)

    print("Practice/Mock questions saved.")

if __name__ == "__main__":
    main()
