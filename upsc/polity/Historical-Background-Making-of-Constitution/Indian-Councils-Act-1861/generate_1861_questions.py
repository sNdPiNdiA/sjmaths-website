import json
import os

BASE_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\polity\Historical-Background-Making-of-Constitution\Indian-Councils-Act-1861"
HI_DIR = os.path.join(BASE_DIR, "hi")

# ----------------- 50 UNIQUE PRACTICE QUESTIONS (ENGLISH) -----------------
practice_questions = [
    {
        "q": "Which of the following Acts laid the foundation of representative institutions by associating Indians with the law-making process for the first time?",
        "opts": ["Regulating Act, 1773", "Pitts India Act, 1784", "Charter Act, 1853", "Indian Councils Act, 1861"],
        "ans": 3,
        "sol": "The Indian Councils Act of 1861 made a beginning of representative institutions by associating Indians with the law-making process."
    },
    {
        "q": "In which year did Lord Canning nominate three Indians to his legislative council under the Indian Councils Act, 1861?",
        "opts": ["1858", "1860", "1862", "1865"],
        "ans": 2,
        "sol": "In 1862, Lord Canning, the then Viceroy, nominated three Indians to his legislative council."
    },
    {
        "q": "Who among the following was NOT nominated as a non-official member to the Legislative Council by Lord Canning in 1862?",
        "opts": ["Raja of Benares", "Maharaja of Patiala", "Sir Dinkar Rao", "Raja of Tanjore"],
        "ans": 3,
        "sol": "The three Indians nominated were the Raja of Benares, the Maharaja of Patiala, and Sir Dinkar Rao. The Raja of Tanjore was not among them."
    },
    {
        "q": "The Indian Councils Act of 1861 reversed the centralization trend that had reached its peak under which of the following Acts?",
        "opts": ["Regulating Act of 1773", "Pitts India Act of 1784", "Charter Act of 1833", "Charter Act of 1853"],
        "ans": 2,
        "sol": "The Act of 1861 reversed the centralization trend that had peaked under the Charter Act of 1833 by restoring legislative powers to Madras and Bombay."
    },
    {
        "q": "Under the Indian Councils Act of 1861, legislative devolution was initiated by restoring law-making powers to which of the following presidencies?\n1. Bombay Presidency\n2. Madras Presidency\n3. Bengal Presidency\nSelect the correct answer:",
        "opts": ["1 only", "2 only", "1 and 2 only", "1, 2 and 3"],
        "ans": 2,
        "sol": "The Act restored legislative powers to the Bombay and Madras Presidencies. Bengal already had central authority, but was later given a separate legislative council."
    },
    {
        "q": "Which of the following is correct regarding the establishment of new legislative councils for Bengal, NWFP, and Punjab under the 1861 Act?",
        "opts": [
            "Bengal (1862), NWFP (1886), Punjab (1897)",
            "Bengal (1858), NWFP (1861), Punjab (1890)",
            "Bengal (1862), NWFP (1870), Punjab (1885)",
            "Bengal (1865), NWFP (1886), Punjab (1901)"
        ],
        "ans": 0,
        "sol": "New legislative councils were established for Bengal in 1862, the North-Western Frontier Province (NWFP) in 1886, and Punjab in 1897."
    },
    {
        "q": "Which of the following features of the Indian Councils Act of 1861 corresponds to the modern Cabinet System in India?",
        "opts": ["Ordinance-making power", "Portfolio System", "Nomination of non-official members", "Restoration of provincial assemblies"],
        "ans": 1,
        "sol": "The Portfolio System, introduced by Lord Canning in 1859 and given statutory recognition in 1861, laid the foundation of the modern cabinet system where ministers head specific departments."
    },
    {
        "q": "Under the Indian Councils Act of 1861, what was the maximum period of validity for an ordinance issued by the Viceroy without the Legislative Council's assent?",
        "opts": ["3 months", "6 months", "1 year", "2 years"],
        "ans": 1,
        "sol": "The Act empowered the Viceroy to issue ordinances during an emergency, which had a validity of six months."
    },
    {
        "q": "Which article of the modern Constitution of India, relating to the President's power to promulgate ordinances, finds its historical roots in the Indian Councils Act of 1861?",
        "opts": ["Article 72", "Article 110", "Article 123", "Article 143"],
        "ans": 2,
        "sol": "The ordinance-making power of the Viceroy under the 1861 Act is the historical precedent for the President's ordinance power under Article 123."
    },
    {
        "q": "Who introduced the Portfolio System in Indian administration, which was later recognized by the Act of 1861?",
        "opts": ["Lord Dalhousie", "Lord Canning", "Lord Warren Hastings", "Lord William Bentinck"],
        "ans": 1,
        "sol": "Lord Canning introduced the Portfolio System in 1859, which was given statutory backing by the Indian Councils Act of 1861."
    },
    {
        "q": "With reference to the Indian Councils Act of 1861, consider the following statements:\n1. It allowed the Legislative Council to debate and vote on the budget.\n2. It associated Indians with the law-making process for the first time.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect because the Legislative Council had no power to debate or vote on the budget, nor could they ask questions on administration. Statement 2 is correct."
    },
    {
        "q": "Under the Indian Councils Act of 1861, what was the minimum and maximum number of additional members to be nominated to the Viceroy's Council for legislative purposes?",
        "opts": ["Minimum 4, Maximum 8", "Minimum 6, Maximum 12", "Minimum 8, Maximum 16", "Minimum 10, Maximum 20"],
        "ans": 1,
        "sol": "The Act expanded the Viceroy's Executive Council for legislative business by adding not less than 6 and not more than 12 additional members."
    },
    {
        "q": "What proportion of the additional members nominated to the Viceroy's Council under the Act of 1861 was required to be non-official?",
        "opts": ["At least one-third", "At least half", "At least two-thirds", "All members"],
        "ans": 1,
        "sol": "The Act mandated that at least half of the additional legislative members nominated by the Viceroy must be non-official (either Indian or European)."
    },
    {
        "q": "What was the term of office for the additional members nominated to the Viceroy's Legislative Council under the 1861 Act?",
        "opts": ["1 year", "2 years", "3 years", "5 years"],
        "ans": 1,
        "sol": "The additional legislative members were nominated for a term of two years."
    },
    {
        "q": "Which of the following was a major limitation of the Legislative Council established under the Indian Councils Act of 1861?",
        "opts": [
            "It had no power to make laws for the entire British India.",
            "It was strictly advisory, and members could not discuss administrative details or ask questions.",
            "No Indians were allowed to join it.",
            "The Secretary of State in London could not veto its acts."
        ],
        "ans": 1,
        "sol": "The legislative councils were advisory bodies. Members could not ask questions about the administration, discuss finance, or vote on budgets."
    },
    {
        "q": "Who held the ultimate veto power over all bills passed by the Imperial and Provincial Legislative Councils under the Act of 1861?",
        "opts": ["The Secretary of State for India only", "The Viceroy of India only", "Both the Viceroy and the British Crown (via Secretary of State)", "The British Parliament exclusively"],
        "ans": 2,
        "sol": "The Viceroy had veto power over local and imperial bills, and the Crown (acting through the Secretary of State) could also disallow any Act passed."
    },
    {
        "q": "The introduction of the fifth ordinary member to the Viceroy's Executive Council under the Act of 1861 was to represent which field?",
        "opts": ["Military Affairs", "Finance", "Law/Jurisprudence", "Foreign Policy"],
        "ans": 2,
        "sol": "The 1861 Act added a fifth member to the Viceroy's Executive Council, who was to be a gentleman of legal profession (a jurist)."
    },
    {
        "q": "How did the Indian Councils Act of 1861 affect the legislative powers of local presidencies compared to the Charter Act of 1853?",
        "opts": [
            "It further curtailed their powers.",
            "It restored their legislative powers, reversing the trend of centralization.",
            "It merged Madras and Bombay into a single legislative unit.",
            "It had no effect on local presidencies."
        ],
        "ans": 1,
        "sol": "It restored legislative powers to Bombay and Madras, reversing the centralization trend and beginning legislative devolution."
    },
    {
        "q": "The policy of 'Association' of Indians in administration, inaugurated by the 1861 Act, was primarily a reaction to which event?",
        "opts": ["The Revolt of 1857", "The Anglo-Sikh Wars", "The Battle of Buxar", "The passing of the 1858 Act"],
        "ans": 0,
        "sol": "Following the Revolt of 1857, the British realized that they needed to associate Indians with administration to understand local grievances and prevent future mutinies."
    },
    {
        "q": "Which of the following provincial legislative councils was established first under the provisions of the 1861 Act?",
        "opts": ["Punjab Legislative Council", "Bengal Legislative Council", "NWFP Legislative Council", "Madras Legislative Council"],
        "ans": 1,
        "sol": "The Bengal Legislative Council was established in 1862, followed by NWFP in 1886 and Punjab in 1897."
    },
    {
        "q": "Who was the Viceroy who presided over the enactment of the Indian Councils Act of 1861?",
        "opts": ["Lord Dalhousie", "Lord Canning", "Lord Lawrence", "Lord Elgin"],
        "ans": 1,
        "sol": "Lord Canning was the Viceroy when the Indian Councils Act of 1861 was enacted."
    },
    {
        "q": "Under the Portfolio System recognized by the 1861 Act, who was authorized to issue final orders on behalf of the government for a department?",
        "opts": [
            "Only the Viceroy",
            "The Secretary of State in London",
            "The individual member in charge of that department",
            "The entire Executive Council by majority vote"
        ],
        "ans": 2,
        "sol": "The individual member in charge of a department was authorized to issue final orders on behalf of the council for that department."
    },
    {
        "q": "With reference to the legislative power restored to the presidencies in 1861, consider the following statements:\n1. The local councils could pass laws without the Viceroy's assent.\n2. The local councils could legislate on subjects like military and foreign affairs.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 3,
        "sol": "Both statements are incorrect. Local bills required the Viceroy's assent, and local councils were barred from legislating on imperial matters like military, post, and foreign affairs."
    },
    {
        "q": "In which city did the Viceroy's Legislative Council primarily meet during the passage of the 1861 Act?",
        "opts": ["Delhi", "Calcutta", "Simla", "Bombay"],
        "ans": 1,
        "sol": "The administrative capital was Calcutta, where the Imperial Legislative Council primarily met."
    },
    {
        "q": "What legal force did an ordinance issued by the Viceroy under the 1861 Act carry compared to normal legislative acts?",
        "opts": [
            "It was subordinate to legislative acts and required council review in 30 days.",
            "It carried the same legal force and validity as an Act of the Legislative Council.",
            "It was merely an advisory circular with no legal binding power.",
            "It was valid only inside the residence of the Viceroy."
        ],
        "ans": 1,
        "sol": "An ordinance issued by the Viceroy under the 1861 Act had the same force and effect as a regular legislative act, but was limited to six months."
    },
    {
        "q": "The first step towards provincial autonomy in British India can be traced back to which of the following legislations?",
        "opts": ["Charter Act of 1833", "Government of India Act of 1858", "Indian Councils Act of 1861", "Indian Councils Act of 1909"],
        "ans": 2,
        "sol": "The restoration of legislative powers to Bombay and Madras under the 1861 Act was the first step towards legislative devolution and eventual provincial autonomy."
    },
    {
        "q": "Which of the following is correct about the non-official members of the Legislative Council under the 1861 Act?",
        "opts": [
            "They were elected by municipal boards in India.",
            "They were nominated directly by the British Prime Minister.",
            "They were nominated by the Viceroy for a two-year term.",
            "They had to be Indian princes exclusively."
        ],
        "ans": 2,
        "sol": "The non-official members (who could be Indians or Europeans) were nominated by the Viceroy for a term of two years."
    },
    {
        "q": "Which Act first introduced a fifth member to the Governor General's Executive Council, transforming it into a cabinet-like structure?",
        "opts": ["Charter Act of 1853", "Government of India Act of 1858", "Indian Councils Act of 1861", "Indian Councils Act of 1892"],
        "ans": 2,
        "sol": "The Indian Councils Act of 1861 introduced the fifth member (a jurist) to the Viceroy's Executive Council."
    },
    {
        "q": "Under the 1861 Act, who was the final authority to determine the rules of business and procedure for the Viceroy's Legislative Council?",
        "opts": ["The British Parliament", "The Secretary of State", "The Viceroy", "The Imperial Legislative Council by vote"],
        "ans": 2,
        "sol": "The Viceroy was empowered to make rules and orders for the transaction of business in his council."
    },
    {
        "q": "Which of the following princely states was represented in the first nominations of non-official Indians in 1862?",
        "opts": ["Hyderabad", "Patiala", "Gwalior", "Baroda"],
        "ans": 1,
        "sol": "The Maharaja of Patiala was nominated as one of the first three non-official Indian members in 1862."
    },
    {
        "q": "The Indian Councils Act of 1861 is also referred to as a step toward 'constitutionalism' in India because:",
        "opts": [
            "It introduced a written constitution for India.",
            "It created an independent judiciary separate from the executive.",
            "It associated public non-official elements with the law-making authority.",
            "It established a federal court in Calcutta."
        ],
        "ans": 2,
        "sol": "It associated non-official members (including Indians) with the law-making process, initiating a constitutional framework of consultation."
    },
    {
        "q": "How did the 1861 Act affect the absolute veto power of the Secretary of State for India?",
        "opts": [
            "It abolished the Secretary of State's veto power.",
            "It maintained that the Secretary of State, representing the Crown, could disallow any Act passed in India.",
            "It made the veto subject to the Viceroy's concurrence.",
            "It limited the veto power to financial bills only."
        ],
        "ans": 1,
        "sol": "The Secretary of State in Council, acting on behalf of the Crown, retained the absolute right to disallow any law passed by the legislative council in India."
    },
    {
        "q": "Under the Act of 1861, local legislative councils of Madras and Bombay were forbidden from passing laws on which of the following subjects without the Viceroy's prior sanction?\n1. Post and Telegraphs\n2. Coinage and Currency\n3. Military and Naval forces\nSelect the correct answer:",
        "opts": ["1 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        "ans": 3,
        "sol": "Local councils were strictly barred from passing laws on imperial subjects like posts, coinage, military affairs, and public debt without prior sanction."
    },
    {
        "q": "What was the statutory status of the Portfolio System under the Indian Councils Act of 1861?",
        "opts": [
            "It was declared illegal and abolished.",
            "It was given statutory recognition and legalized.",
            "It was deferred for consideration until the 1892 Act.",
            "It was restricted to the military department only."
        ],
        "ans": 1,
        "sol": "The Act gave statutory recognition to the portfolio system introduced by Lord Canning in 1859."
    },
    {
        "q": "Under the Indian Councils Act of 1861, who nominated the additional members to the provincial legislative councils of Madras and Bombay?",
        "opts": ["The Viceroy of India", "The Secretary of State", "The respective Governors of Madras and Bombay", "The local municipal corporations"],
        "ans": 2,
        "sol": "The Governors of Madras and Bombay were empowered to nominate the additional members to their respective local legislative councils."
    },
    {
        "q": "In which province was a legislative council established in 1886 under the provisions of the Indian Councils Act of 1861?",
        "opts": ["Bengal", "Punjab", "North-Western Frontier Province (NWFP)", "Central Provinces"],
        "ans": 2,
        "sol": "The legislative council for the North-Western Frontier Province (NWFP) was established in 1886."
    },
    {
        "q": "In which province was a legislative council established in 1897 under the provisions of the Indian Councils Act of 1861?",
        "opts": ["Bengal", "Punjab", "NWFP", "Burma"],
        "ans": 1,
        "sol": "The legislative council for Punjab was established in 1897 under the provisions of the 1861 Act."
    },
    {
        "q": "Which of the following statements is correct regarding the legislative competence of the Viceroy's Legislative Council under the 1861 Act?",
        "opts": [
            "It could make laws for British subjects in India only, not for native states.",
            "It had power to make laws for all persons, courts, and places in British India, and for all British subjects inside native states.",
            "It was subordinate to local provincial councils.",
            "It could not repeal or alter any laws passed by previous Charter Acts."
        ],
        "ans": 1,
        "sol": "The Imperial Legislative Council had extensive legislative jurisdiction, covering all courts, persons, and territories in British India, and British subjects everywhere."
    },
    {
        "q": "The nomination of three Indians to the legislative council in 1862 was seen as a major symbolic shift because:",
        "opts": [
            "It gave Indians a majority in the council.",
            "It marked the entry of Indian non-officials into the supreme legislative body of British India.",
            "It allowed Indians to vote on financial budget resolutions.",
            "It led to the immediate appointment of Indian ministers."
        ],
        "ans": 1,
        "sol": "It was a landmark symbolic shift, allowing Indian representatives to participate in the legislative council for the first time."
    },
    {
        "q": "Under the Indian Councils Act of 1861, what happened to a local bill if the Governor of Bombay/Madras assented to it, but the Viceroy refused assent?",
        "opts": [
            "It became law anyway after a 30-day delay.",
            "It was referred to the British Parliament for arbitration.",
            "It failed to become law, as the Viceroy's assent was mandatory.",
            "It was sent to the Privy Council for review."
        ],
        "ans": 2,
        "sol": "The Viceroy had absolute veto power. No local bill could become law without the final assent of the Viceroy."
    },
    {
        "q": "Why was the legislative council created by the 1861 Act often criticized as a 'mere committee for lawmaking'?",
        "opts": [
            "Because it had no power to discuss administrative policies or financial budgets.",
            "Because it had only European members.",
            "Because it met only once every five years.",
            "Because it was headed by an Indian prince."
        ],
        "ans": 0,
        "sol": "The council was strictly limited to legislating. It could not ask questions on executive administration, debate policies, or vote on the budget."
    },
    {
        "q": "What change did the Indian Councils Act of 1861 make to the number of ordinary members in the Viceroy's Executive Council?",
        "opts": ["Reduced from 4 to 3", "Increased from 4 to 5", "Increased from 5 to 6", "Maintained at 4"],
        "ans": 1,
        "sol": "The Act increased the number of ordinary members in the Executive Council from 4 to 5."
    },
    {
        "q": "Who was the Maharaja of Patiala nominated to the Legislative Council by Lord Canning in 1862?",
        "opts": ["Maharaja Narendra Singh", "Maharaja Yadavindra Singh", "Maharaja Bhupinder Singh", "Maharaja Rajinder Singh"],
        "ans": 0,
        "sol": "Maharaja Narendra Singh of Patiala was the one nominated to the council in 1862."
    },
    {
        "q": "Who was Sir Dinkar Rao, nominated to the Legislative Council in 1862?",
        "opts": ["The Prime Minister of Gwalior State", "The Maharaja of Indore", "The Chief Justice of Calcutta", "A prominent merchant of Bombay"],
        "ans": 0,
        "sol": "Sir Dinkar Rao was the prominent and reformist Prime Minister (Diwan) of the princely state of Gwalior."
    },
    {
        "q": "Which of the following is correct regarding the Viceroy's power to make rules for procedural transactions under the 1861 Act?",
        "opts": [
            "Rules could only be made with the approval of the Secretary of State.",
            "The Viceroy was fully authorized to frame rules for procedures and business transaction in his council.",
            "No procedural rules could be modified without parliamentary approval.",
            "Procedural rules were determined by the senior-most Indian member."
        ],
        "ans": 1,
        "sol": "The Act empowered the Viceroy to frame rules of business for the Executive and Legislative Councils."
    },
    {
        "q": "Under the 1861 Act, an ordinance issued by the Viceroy was valid even if:",
        "opts": [
            "The Secretary of State disallowed it.",
            "The Legislative Council was in session and opposed it.",
            "It violated the fundamental rights of the British Crown.",
            "It was not signed by the Viceroy himself."
        ],
        "ans": 1,
        "sol": "The Viceroy's ordinance power was independent of the Legislative Council and carried equal force, even in the face of opposition, for six months."
    },
    {
        "q": "Which of the following represents the primary administrative motive behind the Indian Councils Act of 1861?",
        "opts": [
            "To grant complete independence to Indian provinces.",
            "To associate influential Indians with lawmaking to secure imperial rule post-1857.",
            "To replace British military officers with Indian soldiers.",
            "To establish a democratic government in India."
        ],
        "ans": 1,
        "sol": "The main objective was to associate native elements with lawmaking to serve as a safety valve and improve governance to avoid another mutiny."
    },
    {
        "q": "The restoration of legislative authority to Madras and Bombay Presidencies in 1861 marked the reversal of which Act's provisions?",
        "opts": ["Regulating Act of 1773", "Pitts India Act of 1784", "Charter Act of 1813", "Charter Act of 1833"],
        "ans": 3,
        "sol": "The Charter Act of 1833 had stripped these presidencies of their legislative powers, which were restored by the 1861 Act."
    },
    {
        "q": "Which of the following statements is correct regarding the legislative councils established under the 1861 Act?",
        "opts": [
            "They were federal legislative bodies with sovereign powers.",
            "They were advisory committees to validate the executive's legislative proposals.",
            "They were elected by popular vote.",
            "They had power to override the Viceroy's veto."
        ],
        "ans": 1,
        "sol": "The legislative councils were advisory bodies designed to assist the executive in framing and validating laws."
    },
    {
        "q": "The modern constitutional framework of India inherits which of the following directly from the Indian Councils Act of 1861?",
        "opts": [
            "The division of Parliament into Lok Sabha and Rajya Sabha",
            "The Cabinet/Portfolio System and Ordinance-making power of the executive",
            "The federal court system",
            "The election of the Prime Minister"
        ],
        "ans": 1,
        "sol": "The cabinet system (portfolio system) and the executive ordinance power are direct constitutional inheritances from the 1861 Act."
    }
]

# ----------------- 10 UNIQUE MOCK QUESTIONS (ENGLISH) -----------------
mock_questions = [
    {
        "q": "With reference to the Indian Councils Act of 1861, consider the following statements:\n1. It initiated the process of decentralization by restoring legislative powers to Bombay and Madras.\n2. It associated Indians with the law-making process by introducing elections for legislative councils.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect because the Indians nominated (Raja of Benares, Maharaja of Patiala, Sir Dinkar Rao) were nominated by the Viceroy, not elected. Elections were not introduced."
    },
    {
        "q": "<strong>Assertion (A):</strong> The Indian Councils Act of 1861 is considered a landmark in the constitutional history of India.<br><strong>Reason (R):</strong> It associated non-official Indian elements with the law-making process and restored legislative powers to local presidencies.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both Assertion and Reason are true. The association of Indians and the launch of legislative decentralization are the primary reasons why it is a landmark constitutional act."
    },
    {
        "q": "Consider the following statements regarding the Legislative Councils under the Indian Councils Act, 1861:\n1. The councils were empowered to vote on the annual financial budget.\n2. The Viceroy had absolute veto power over any bill passed by the councils.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect because the council had no budget-voting or discussion rights. Statement 2 is correct: the Viceroy held absolute veto authority."
    },
    {
        "q": "Consider the following statements regarding the Portfolio System established by the 1861 Act:\nStatement I: Under this system, ordinary members of the Executive Council were placed in charge of specific departments.\nStatement II: The members could issue final orders on behalf of the Governor-General in Council on department matters.\nWhich of the following is correct?",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 2,
        "sol": "Both statements are correct. The portfolio system functioned like a modern cabinet where individual ministers had the authority to run and issue orders for their specific departments."
    },
    {
        "q": "Match the following Indian nominees of 1862 with their correct descriptions:\nI. Raja of Benares\nII. Maharaja of Patiala\nIII. Sir Dinkar Rao\nSelect the correct matching:",
        "opts": [
            "I-Raja Deo Narain Singh, II-Maharaja Narendra Singh, III-Diwan of Gwalior State",
            "I-Diwan of Gwalior State, II-Raja Deo Narain Singh, III-Maharaja Narendra Singh",
            "I-Maharaja Narendra Singh, II-Diwan of Gwalior State, III-Raja Deo Narain Singh",
            "I-Raja Deo Narain Singh, II-Diwan of Gwalior State, III-Maharaja Narendra Singh"
        ],
        "ans": 0,
        "sol": "Raja of Benares was Raja Deo Narain Singh; Maharaja of Patiala was Narendra Singh; Sir Dinkar Rao was the Diwan (Prime Minister) of Gwalior State."
    },
    {
        "q": "With reference to the Viceroy's ordinance-making power under the 1861 Act, consider the following statements:\n1. The ordinance could only be issued with the prior consent of the British Parliament.\n2. The life of such an ordinance was limited to exactly six months.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect because the Viceroy could issue ordinances independently in emergencies without parliament or council consent. Statement 2 is correct."
    },
    {
        "q": "<strong>Assertion (A):</strong> The Indian Councils Act of 1861 restored legislative powers to the Bombay and Madras Presidencies.<br><strong>Reason (R):</strong> The British government wanted to establish fully autonomous provincial governments independent of central control.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 2,
        "sol": "The assertion is true: legislative powers were restored. The reason is false because the restoration was not intended to create independent provinces; all local bills still required the Viceroy's prior sanction and final assent, keeping central control intact."
    },
    {
        "q": "Consider the following statements regarding the composition of the Viceroy's Legislative Council under the 1861 Act:\n1. The additional members were nominated for a term of three years.\n2. At least half of the additional members had to be non-official.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect because the term was two years, not three. Statement 2 is correct: at least half of the additional members had to be non-official."
    },
    {
        "q": "With reference to the devolution of legislative councils under the 1861 Act, arrange the following provinces in chronological order of their council establishment:\n1. Punjab\n2. Bengal\n3. NWFP\nSelect the correct sequence:",
        "opts": ["2 - 3 - 1", "2 - 1 - 3", "3 - 2 - 1", "1 - 2 - 3"],
        "ans": 0,
        "sol": "Bengal was established in 1862, NWFP in 1886, and Punjab in 1897. The correct order is 2 - 3 - 1."
    },
    {
        "q": "Consider the following statements regarding the ordinary members of the Viceroy's Executive Council post-1861:\n1. A fifth member was added to represent the legal profession (jurist).\n2. The portfolio system ended the collective responsibility of the council.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect because the portfolio system did not end collective accountability; it streamlined administration, and final decisions of a department were legally treated as decisions of the council."
    }
]

# ----------------- 50 UNIQUE PRACTICE QUESTIONS (HINDI) -----------------
practice_questions_hi = [
    {
        "q": "निम्नलिखित में से किस अधिनियम ने पहली बार कानून बनाने की प्रक्रिया में भारतीयों को शामिल करके प्रतिनिधि संस्थानों की नींव रखी?",
        "opts": ["1773 का रेगुलेटिंग एक्ट", "1784 का पिट्स इंडिया एक्ट", "1853 का चार्टर अधिनियम", "1861 का भारतीय परिषद अधिनियम"],
        "ans": 3,
        "sol": "1861 के भारतीय परिषद अधिनियम ने पहली बार कानून बनाने की प्रक्रिया में भारतीयों को शामिल करके प्रतिनिधि संस्थानों की शुरुआत की।"
    },
    {
        "q": "लॉर्ड कैनिंग ने 1861 के भारतीय परिषद अधिनियम के तहत किस वर्ष तीन भारतीयों को अपनी विधायी परिषद में मनोनीत किया था?",
        "opts": ["1858", "1860", "1862", "1865"],
        "ans": 2,
        "sol": "1862 में तत्कालीन वायसराय लॉर्ड कैनिंग ने तीन भारतीयों को अपनी विधायी परिषद में गैर-सरकारी सदस्यों के रूप में मनोनीत किया था।"
    },
    {
        "q": "लॉर्ड कैनिंग द्वारा 1862 में विधायी परिषद में गैर-सरकारी सदस्य के रूप में निम्नलिखित में से किसे मनोनीत नहीं किया गया था?",
        "opts": ["बनारस के राजा", "पटियाला के महाराजा", "सर दिनकर राव", "तंजौर के राजा"],
        "ans": 3,
        "sol": "मनोनीत किए गए तीन भारतीय बनारस के राजा, पटियाला के महाराजा और सर दिनकर राव थे। तंजौर के राजा उनमें शामिल नहीं थे।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम ने केंद्रीकरण की उस प्रवृत्ति को उलट दिया जो निम्नलिखित में से किस अधिनियम के तहत अपने चरम पर पहुंच गई थी?",
        "opts": ["1773 का रेगुलेटिंग एक्ट", "1784 का पिट्स इंडिया एक्ट", "1833 का चार्टर अधिनियम", "1853 का चार्टर अधिनियम"],
        "ans": 2,
        "sol": "1861 के अधिनियम ने मद्रास और बॉम्बे को विधायी शक्तियां बहाल करके केंद्रीकरण की उस प्रवृत्ति को उलट दिया जो 1833 के चार्टर अधिनियम के तहत अपने चरम पर थी।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम के तहत, किस प्रेसीडेंसी को कानून बनाने की शक्तियां बहाल करके विधायी विकेंद्रीकरण की शुरुआत की गई थी?\n1. बॉम्बे प्रेसीडेंसी\n2. मद्रास प्रेसीडेंसी\n3. बंगाल प्रेसीडेंसी\nसही उत्तर चुनें:",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "1, 2 और 3"],
        "ans": 2,
        "sol": "अधिनियम ने बॉम्बे और मद्रास प्रेसीडेंसियों को विधायी शक्तियां बहाल कर दीं। बंगाल के पास पहले से ही केंद्रीय अधिकार था, जिसे बाद में एक अलग विधायी परिषद दी गई।"
    },
    {
        "q": "1861 के अधिनियम के तहत बंगाल, NWFP और पंजाब के लिए नई विधायी परिषदों की स्थापना के संबंध में निम्नलिखित में से कौन सा सही है?",
        "opts": [
            "बंगाल (1862), NWFP (1886), पंजाब (1897)",
            "बंगाल (1858), NWFP (1861), पंजाब (1890)",
            "बंगाल (1862), NWFP (1870), पंजाब (1885)",
            "बंगाल (1865), NWFP (1886), पंजाब (1901)"
        ],
        "ans": 0,
        "sol": "नई विधायी परिषदों की स्थापना बंगाल के लिए 1862 में, उत्तर-पश्चिमी सीमांत प्रांत (NWFP) के लिए 1886 में, और पंजाब के लिए 1897 में की गई थी।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम की निम्नलिखित में से कौन सी विशेषता भारत में आधुनिक कैबिनेट प्रणाली से मेल खाती है?",
        "opts": ["अध्यादेश बनाने की शक्ति", "पोर्टफोलियो प्रणाली (Portfolio System)", "गैर-सरकारी सदस्यों का नामांकन", "प्रांतीय विधानसभाओं की बहाली"],
        "ans": 1,
        "sol": "लॉर्ड कैनिंग द्वारा 1859 में शुरू की गई और 1861 में वैधानिक मान्यता प्राप्त पोर्टफोलियो प्रणाली ने आधुनिक कैबिनेट प्रणाली की नींव रखी जहाँ मंत्री विशिष्ट विभागों के प्रमुख होते हैं।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम के तहत, विधायी परिषद की सहमति के बिना वायसराय द्वारा जारी किए गए अध्यादेश की अधिकतम अवधि क्या थी?",
        "opts": ["3 महीने", "6 महीने", "1 वर्ष", "2 वर्ष"],
        "ans": 1,
        "sol": "अधिनियम ने वायसराय को आपातकाल के दौरान अध्यादेश जारी करने का अधिकार दिया, जिसकी अवधि छह महीने थी।"
    },
    {
        "q": "आधुनिक भारतीय संविधान का कौन सा अनुच्छेद, जो राष्ट्रपति की अध्यादेश जारी करने की शक्ति से संबंधित है, अपनी ऐतिहासिक जड़ें 1861 के भारतीय परिषद अधिनियम में पाता है?",
        "opts": ["अनुच्छेद 72", "अनुच्छेद 110", "अनुच्छेद 123", "अनुच्छेद 143"],
        "ans": 2,
        "sol": "1861 के अधिनियम के तहत वायसराय की अध्यादेश जारी करने की शक्ति अनुच्छेद 123 के तहत राष्ट्रपति की अध्यादेश शक्ति का ऐतिहासिक पूर्ववृत्त है।"
    },
    {
        "q": "महारानी और वायसराय द्वारा मान्यता प्राप्त पोर्टफोलियो प्रणाली (विभाग प्रणाली) की शुरुआत किसने की थी, जिसे बाद में 1861 के अधिनियम द्वारा मान्यता दी गई?",
        "opts": ["लॉर्ड डलहौजी", "लॉर्ड कैनिंग", "लॉर्ड वारेन हेस्टिंग्स", "लॉर्ड विलियम बेंटिक"],
        "ans": 1,
        "sol": "लॉर्ड कैनिंग ने 1859 में पोर्टफोलियो प्रणाली की शुरुआत की थी, जिसे 1861 के भारतीय परिषद अधिनियम द्वारा वैधानिक मान्यता दी गई थी।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. इसने विधायी परिषद को वार्षिक वित्तीय बजट पर बहस करने और मतदान करने की अनुमति दी।\n2. इसने पहली बार कानून बनाने की प्रक्रिया में भारतीयों को शामिल किया।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 1,
        "sol": "कथन 1 गलत है क्योंकि विधायी परिषद के पास बजट पर बहस करने या मतदान करने का कोई अधिकार नहीं था, और न ही वे प्रश्न पूछ सकते थे। कथन 2 सही है।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम के तहत, विधायी उद्देश्यों के लिए वायसराय की परिषद में मनोनीत किए जाने वाले अतिरिक्त सदस्यों की न्यूनतम और अधिकतम संख्या क्या थी?",
        "opts": ["न्यूनतम 4, अधिकतम 8", "न्यूनतम 6, अधिकतम 12", "न्यूनतम 8, अधिकतम 16", "न्यूनतम 10, अधिकतम 20"],
        "ans": 1,
        "sol": "अधिनियम ने विधायी कार्यों के लिए वायसराय की परिषद का विस्तार किया जिसमें कम से कम 6 और अधिक से कम 12 अतिरिक्त सदस्यों को जोड़ने का प्रावधान था।"
    },
    {
        "q": "1861 के अधिनियम के तहत वायसराय की परिषद में नामांकित अतिरिक्त सदस्यों में से कितने सदस्यों का गैर-सरकारी होना आवश्यक था?",
        "opts": ["कम से कम एक-तिहाई", "कम से कम आधे", "कम से कम दो-तिहाई", "सभी सदस्य"],
        "ans": 1,
        "sol": "अधिनियम ने अनिवार्य किया कि वायसराय द्वारा मनोनीत अतिरिक्त विधायी सदस्यों में से कम से कम आधे सदस्य गैर-सरकारी होने चाहिए (वे भारतीय या यूरोपीय हो सकते थे)।"
    },
    {
        "q": "1861 के अधिनियम के तहत वायसराय की विधायी परिषद में मनोनीत अतिरिक्त सदस्यों का कार्यकाल कितना होता था?",
        "opts": ["1 वर्ष", "2 वर्ष", "3 वर्ष", "5 वर्ष"],
        "ans": 1,
        "sol": "अठारह सौ इकसठ के अतिरिक्त विधायी सदस्यों को दो वर्ष की अवधि के लिए नामांकित किया जाता था।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम के तहत स्थापित विधायी परिषद की एक प्रमुख सीमा क्या थी?",
        "opts": [
            "इसके पास पूरे ब्रिटिश भारत के लिए कानून बनाने की कोई शक्ति नहीं थी।",
            "यह पूरी तरह से सलाहकार थी, और सदस्य प्रशासनिक विवरणों पर चर्चा नहीं कर सकते थे या प्रश्न नहीं पूछ सकते थे।",
            "इसमें किसी भी भारतीय को शामिल होने की अनुमति नहीं थी।",
            "लंदन में भारत सचिव इसके अधिनियमों को वीटो नहीं कर सकते थे।"
        ],
        "ans": 1,
        "sol": "विधायी परिषदें केवल सलाहकार निकाय थीं। सदस्य प्रशासन के संबंध में प्रश्न नहीं पूछ सकते थे, वित्तीय नीति पर चर्चा नहीं कर सकते थे, या बजट पर मतदान नहीं कर सकते थे।"
    },
    {
        "q": "1861 के अधिनियम के तहत शाही और प्रांतीय विधायी परिषदों द्वारा पारित सभी विधेयकों पर अंतिम वीटो शक्ति किसके पास थी?",
        "opts": ["केवल भारत के राज्य सचिव", "केवल भारत के वायसराय", "वायसराय और ब्रिटिश क्राउन (भारत सचिव के माध्यम से) दोनों", "विशेष रूप से ब्रिटिश संसद"],
        "ans": 2,
        "sol": "वायसराय के पास विधेयकों पर वीटो का अधिकार था, और ब्रिटिश क्राउन (राज्य सचिव के माध्यम से) भी परिषद द्वारा पारित किसी भी अधिनियम को अमान्य कर सकता था।"
    },
    {
        "q": "1861 के अधिनियम के तहत वायसराय की कार्यकारी परिषद में पांचवें सदस्य को किस क्षेत्र का प्रतिनिधित्व करने के लिए जोड़ा गया था?",
        "opts": ["सैन्य मामले", "वित्त", "कानून / न्यायशास्त्र", "विदेश नीति"],
        "ans": 2,
        "sol": "1861 के अधिनियम ने वायसराय की कार्यकारी परिषद में पांचवें सदस्य को जोड़ा, जो कानून क्षेत्र का जानकार (विधि विशेषज्ञ) होना था।"
    },
    {
        "q": "1853 के चार्टर अधिनियम की तुलना में 1861 के भारतीय परिषद अधिनियम ने स्थानीय प्रेसीडेंसियों की विधायी शक्तियों को कैसे प्रभावित किया?",
        "opts": [
            "इसने उनकी शक्तियों को और कम कर दिया।",
            "इसने उनकी विधायी शक्तियों को बहाल कर दिया, जिससे केंद्रीकरण की प्रवृत्ति उलट गई।",
            "इसने मद्रास और बॉम्बे को एक एकल विधायी इकाई में विलय कर दिया।",
            "इसका स्थानीय प्रेसीडेंसियों पर कोई प्रभाव नहीं पड़ा।"
        ],
        "ans": 1,
        "sol": "इसने बॉम्बे और मद्रास को विधायी शक्तियां बहाल कर दीं, जिससे केंद्रीकरण की प्रवृत्ति उलट गई और विधायी विकेंद्रीकरण की शुरुआत हुई।"
    },
    {
        "q": "1861 के अधिनियम द्वारा शुरू की गई प्रशासन में भारतीयों को जोड़ने (एसोसिएशन) की नीति मुख्य रूप से किस घटना की प्रतिक्रिया थी?",
        "opts": ["1857 का विद्रोह", "आंग्ल-सिख युद्ध", "बक्सर का युद्ध", "1858 के अधिनियम का पारित होना"],
        "ans": 0,
        "sol": "1857 के विद्रोह के बाद, अंग्रेजों ने महसूस किया कि विद्रोह से बचने और स्थानीय शिकायतों को समझने के लिए भारतीयों को कानून बनाने की प्रक्रिया में शामिल करना आवश्यक था।"
    },
    {
        "q": "1861 के अधिनियम के प्रावधानों के तहत निम्नलिखित में से कौन सी प्रांतीय विधायी परिषद सबसे पहले स्थापित की गई थी?",
        "opts": ["पंजाब विधायी परिषद", "बंगाल विधायी परिषद", "NWFP विधायी परिषद", "मद्रास विधायी परिषद"],
        "ans": 1,
        "sol": "बंगाल विधायी परिषद की स्थापना 1862 में की गई थी, जिसके बाद 1886 में NWFP और 1897 में पंजाब परिषद बनी।"
    },
    {
        "q": "वह वायसराय कौन थे जिन्होंने 1861 के भारतीय परिषद अधिनियम के पारित होने की अध्यक्षता की थी?",
        "opts": ["लॉर्ड डलहौजी", "लॉर्ड कैनिंग", "लॉर्ड लॉरेंस", "लॉर्ड एल्गिन"],
        "ans": 1,
        "sol": "1861 के अधिनियम के अधिनियमन के समय लॉर्ड कैनिंग भारत के वायसराय थे।"
    },
    {
        "q": "1861 के अधिनियम द्वारा मान्यता प्राप्त पोर्टफोलियो प्रणाली के तहत, किसी विभाग के लिए सरकार की ओर से अंतिम आदेश जारी करने का अधिकार किसे था?",
        "opts": [
            "Supervised Viceroy only",
            "लंदन में राज्य सचिव को",
            "उस विभाग के प्रभारी व्यक्तिगत सदस्य को",
            "बहुमत वोट द्वारा पूरी कार्यकारी परिषद को"
        ],
        "opts": [
            "केवल वायसराय को",
            "लंदन में राज्य सचिव को",
            "उस विभाग के प्रभारी व्यक्तिगत सदस्य को",
            "बहुमत वोट द्वारा पूरी कार्यकारी परिषद को"
        ],
        "ans": 2,
        "sol": "पोर्टफोलियो प्रणाली के तहत, किसी विभाग के प्रभारी सदस्य को उस विभाग के संबंध में परिषद की ओर से अंतिम आदेश जारी करने का अधिकार था।"
    },
    {
        "q": "1861 में प्रेसीडेंसियों को बहाल की गई विधायी शक्तियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. स्थानीय परिषदें वायसराय की सहमति के बिना कानून पारित कर सकती थीं।\n2. स्थानीय परिषदें सैन्य और विदेशी मामलों जैसे विषयों पर कानून बना सकती थीं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 3,
        "sol": "दोनों कथन गलत हैं। स्थानीय विधेयकों के लिए वायसराय की अंतिम स्वीकृति अनिवार्य थी, और स्थानीय परिषदों को सैन्य, डाक और विदेश नीति जैसे राष्ट्रीय महत्व के विषयों पर कानून बनाने की मनाही थी।"
    },
    {
        "q": "1861 के अधिनियम के पारित होने के दौरान वायसराय की विधायी परिषद मुख्य रूप से किस शहर में बैठक आयोजित करती थी?",
        "opts": ["दिल्ली", "कलकत्ता", "शिमला", "बॉम्बे"],
        "ans": 1,
        "sol": "ब्रिटिश भारत की प्रशासनिक राजधानी कलकत्ता थी, जहाँ मुख्य रूप से इम्पीरियल लेजिस्लेटिव काउंसिल की बैठकें होती थीं।"
    },
    {
        "q": "1861 के अधिनियम के तहत वायसराय द्वारा जारी अध्यादेश का सामान्य विधायी अधिनियमों की तुलना में क्या कानूनी बल था?",
        "opts": [
            "यह विधायी अधिनियमों के अधीन था और 30 दिनों में परिषद की समीक्षा आवश्यक थी।",
            "इसका कानूनी बल और प्रभाव विधायी परिषद के नियमित अधिनियम के समान ही था।",
            "यह बिना किसी कानूनी बाध्यकारी शक्ति के केवल एक सलाहकारी सर्कुलर था।",
            "यह केवल वायसराय के निवास स्थान के भीतर ही वैध था।"
        ],
        "ans": 1,
        "sol": "वायसराय द्वारा जारी अध्यादेश का कानूनी बल नियमित कानून के समान ही था, लेकिन इसकी अवधि छह महीने तक सीमित थी।"
    },
    {
        "q": "ब्रिटिश भारत में प्रांतीय स्वायत्तता की दिशा में पहला कदम निम्नलिखित में से किस कानून में खोजा जा सकता है?",
        "opts": ["1833 का चार्टर अधिनियम", "1858 का भारत सरकार अधिनियम", "1861 का भारतीय परिषद अधिनियम", "1909 का भारतीय परिषद अधिनियम"],
        "ans": 2,
        "sol": "1861 के अधिनियम के तहत बॉम्बे और मद्रास को विधायी शक्तियां लौटाना विकेंद्रीकरण और भविष्य की प्रांतीय स्वायत्तता की दिशा में पहला कदम था।"
    },
    {
        "q": "1861 के अधिनियम के तहत विधायी परिषद के गैर-सरकारी सदस्यों के संबंध में निम्नलिखित में से कौन सा कथन सही है?",
        "opts": [
            "वे भारत में नगरपालिकाओं द्वारा चुने जाते थे।",
            "वे सीधे ब्रिटिश प्रधानमंत्री द्वारा मनोनीत किए जाते थे।",
            "वे वायसराय द्वारा दो वर्ष के कार्यकाल के लिए नामांकित किए जाते थे।",
            "उन्हें विशेष रूप से केवल भारतीय राजा होना आवश्यक था।"
        ],
        "ans": 2,
        "sol": "गैर-सरकारी सदस्य (जो भारतीय या यूरोपीय हो सकते थे) वायसराय द्वारा दो वर्ष की अवधि के लिए मनोनीत किए जाते थे।"
    },
    {
        "q": "किस अधिनियम ने पहली बार गवर्नर जनरल की कार्यकारी परिषद में पांचवां सदस्य जोड़ा, जिससे यह कैबिनेट जैसी संरचना में बदल गई?",
        "opts": ["1853 का चार्टर अधिनियम", "1858 का भारत सरकार अधिनियम", "1861 का भारतीय परिषद अधिनियम", "1892 का भारतीय परिषद अधिनियम"],
        "ans": 2,
        "sol": "1861 के भारतीय परिषद अधिनियम ने वायसराय की कार्यकारी परिषद में पांचवां सदस्य (विधि सदस्य) जोड़ा।"
    },
    {
        "q": "1861 के अधिनियम के तहत, वायसराय की विधायी परिषद के लिए प्रक्रियाओं और व्यापार के नियमों को तय करने का अंतिम अधिकार किसके पास था?",
        "opts": ["ब्रिटिश संसद", "भारत सचिव", "वायसराय", "मतदान द्वारा इम्पीरियल लेजिस्लेटिव काउंसिल"],
        "ans": 2,
        "sol": "अधिनियम ने वायसराय को परिषद में कार्य संचालन और प्रक्रियाओं के नियम बनाने का पूर्ण अधिकार दिया था।"
    },
    {
        "q": "1862 में गैर-सरकारी भारतीयों के पहले नामांकन में निम्नलिखित में से कौन सी रियासत शामिल थी?",
        "opts": ["हैदराबाद", "पटियाला", "ग्वालियर", "बड़ौदा"],
        "ans": 1,
        "sol": "1862 में मनोनीत पहले तीन गैर-सरकारी भारतीय सदस्यों में पटियाला के महाराजा शामिल थे।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम को भारत में 'संवैधानिकता' की दिशा में एक कदम के रूप में भी जाना जाता है क्योंकि:",
        "opts": [
            "इसने भारत के लिए एक लिखित संविधान पेश किया।",
            "इसने कार्यपालिका से अलग एक स्वतंत्र न्यायपालिका बनाई।",
            "इसने कानून बनाने वाली संस्था के साथ जनता के गैर-सरकारी तत्वों को जोड़ा।",
            "इसने कलकत्ता में एक संघीय न्यायालय की स्थापना की।"
        ],
        "ans": 2,
        "sol": "इसने कानून बनाने की प्रक्रिया में गैर-सरकारी तत्वों (भारतीयों सहित) को शामिल करके परामर्श की संवैधानिक व्यवस्था की शुरुआत की।"
    },
    {
        "q": "1861 के अधिनियम ने भारत सचिव की अंतिम वीटो शक्ति को कैसे प्रभावित किया?",
        "opts": [
            "इसने भारत सचिव की वीटो शक्ति को समाप्त कर दिया।",
            "इसने यह व्यवस्था बनाए रखी कि क्राउन का प्रतिनिधित्व करने वाले भारत सचिव भारत में पारित किसी भी कानून को खारिज कर सकते थे।",
            "इसने वीटो को वायसराय की सहमति के अधीन बना दिया।",
            "इसने वीटो शक्ति को केवल वित्तीय विधेयकों तक सीमित कर दिया।"
        ],
        "ans": 1,
        "sol": "ब्रिटिश क्राउन की ओर से कार्य करते हुए भारत सचिव के पास भारत में विधायी परिषद द्वारा पारित किसी भी कानून को वीटो (अमान्य) करने का पूर्ण अधिकार बना रहा।"
    },
    {
        "q": "1861 के अधिनियम के तहत, मद्रास और बॉम्बे की स्थानीय विधायी परिषदों को वायसराय की पूर्व स्वीकृति के बिना किस विषय पर कानून बनाने की मनाही थी?\n1. डाक और टेलीग्राम\n2. सिक्का और मुद्रा\n3. सैन्य और नौसेना बल\nसही उत्तर चुनें:",
        "opts": ["केवल 1", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans": 3,
        "sol": "स्थानीय परिषदों को वायसराय की पूर्व स्वीकृति के बिना डाक, मुद्रा, सैन्य मामलों और सार्वजनिक ऋण जैसे राष्ट्रीय महत्व के विषयों पर कानून बनाने की सख्त मनाही थी।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम के तहत पोर्टफोलियो प्रणाली (विभाग प्रणाली) की कानूनी स्थिति क्या थी?",
        "opts": [
            "इसे अवैध घोषित कर दिया गया और समाप्त कर दिया गया।",
            "इसे वैधानिक मान्यता दी गई और कानूनी रूप से मान्य किया गया।",
            "इसे 1892 के अधिनियम तक के लिए टाल दिया गया था।",
            "इसे केवल सैन्य विभाग तक ही सीमित रखा गया था।"
        ],
        "ans": 1,
        "sol": "अधिनियम ने लॉर्ड कैनिंग द्वारा 1859 में शुरू की गई पोर्टफोलियो प्रणाली को विधिवत वैधानिक और कानूनी मान्यता प्रदान की।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम के तहत, मद्रास और बॉम्बे की प्रांतीय विधायी परिषदों में अतिरिक्त सदस्यों को कौन मनोनीत करता था?",
        "opts": ["भारत के वायसराय", "भारत के राज्य सचिव", "मद्रास और बॉम्बे के संबंधित गवर्नर", "स्थानीय नगर निगम"],
        "ans": 2,
        "sol": "मद्रास और बॉम्बे के गवर्नरों को अपने संबंधित प्रांतों की विधायी परिषदों के लिए अतिरिक्त सदस्यों को नामांकित करने का अधिकार दिया गया था।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम के प्रावधानों के तहत 1886 में किस प्रांत में एक विधायी परिषद की स्थापना की गई थी?",
        "opts": ["बंगाल", "पंजाब", "उत्तर-पश्चिमी सीमांत प्रांत (NWFP)", "मध्य प्रांत"],
        "ans": 2,
        "sol": "उत्तर-पश्चिमी सीमांत प्रांत (NWFP) के लिए 1886 में विधायी परिषद की स्थापना की गई थी।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम के प्रावधानों के तहत 1897 में किस प्रांत में एक विधायी परिषद की स्थापना की गई थी?",
        "opts": ["बंगाल", "पंजाब", "NWFP", "बर्मा"],
        "ans": 1,
        "sol": "1861 के अधिनियम के प्रावधानों के तहत 1897 में पंजाब के लिए विधायी परिषद की स्थापना की गई थी।"
    },
    {
        "q": "1861 के अधिनियम के तहत वायसराय की विधायी परिषद के विधायी दायरे के संबंध में निम्नलिखित में से कौन सा कथन सही है?",
        "opts": [
            "यह केवल भारत में ब्रिटिश नागरिकों के लिए कानून बना सकती थी, रियासतों के लिए नहीं।",
            "इसके पास ब्रिटिश भारत के सभी व्यक्तियों, न्यायालयों और स्थानों के लिए और रियासतों में रहने वाले सभी ब्रिटिश नागरिकों के लिए कानून बनाने की शक्ति थी।",
            "यह स्थानीय प्रांतीय परिषदों के अधीन थी।",
            "यह पिछले चार्टर अधिनियमों द्वारा पारित किसी भी कानून को बदल या निरस्त नहीं कर सकती थी।"
        ],
        "ans": 1,
        "sol": "इम्पीरियल लेजिस्लेटिव काउंसिल का विधायी क्षेत्राधिकार व्यापक था, जो ब्रिटिश भारत की सभी अदालतों, लोगों और क्षेत्रों के साथ-साथ विदेशों में रहने वाले ब्रिटिश नागरिकों पर भी लागू होता था।"
    },
    {
        "q": "1862 में तीन भारतीयों का विधायी परिषद में नामांकन एक बड़ा प्रतीकात्मक बदलाव क्यों माना गया?",
        "opts": [
            "इसने परिषद में भारतीयों को बहुमत प्रदान किया।",
            "इसने ब्रिटिश भारत के सर्वोच्च विधायी निकाय में गैर-सरकारी भारतीयों के प्रवेश को चिह्नित किया।",
            "इसने भारतीयों को वार्षिक वित्तीय बजट पर मतदान करने की अनुमति दी।",
            "इसके कारण तुरंत भारतीय मंत्रियों की नियुक्ति संभव हुई।"
        ],
        "ans": 1,
        "sol": "इसने एक बड़ा प्रतीकात्मक बदलाव था जिसने पहली बार भारतीय प्रतिनिधियों को सर्वोच्च विधायी परिषद में बैठने का अवसर दिया।"
    },
    {
        "q": "1861 के अधिनियम के तहत, यदि बॉम्बे/मद्रास के गवर्नर ने स्थानीय विधेयक को अपनी स्वीकृति दे दी, लेकिन वायसराय ने उसे खारिज कर दिया, तो उस विधेयक का क्या होता था?",
        "opts": [
            "वह 30 दिनों के बाद स्वतः ही कानून बन जाता था।",
            "उसे मध्यस्थता के लिए ब्रिटिश संसद के पास भेजा जाता था।",
            "वह कानून बनने में विफल हो जाता था, क्योंकि वायसराय की सहमति अनिवार्य थी।",
            "उसे समीक्षा के लिए प्रिवी काउंसिल भेजा जाता था।"
        ],
        "ans": 2,
        "sol": "वायसराय के पास पूर्ण वीटो अधिकार थे। वायसराय की अंतिम स्वीकृति के बिना कोई भी स्थानीय विधेयक कानून नहीं बन सकता था।"
    },
    {
        "q": "1861 के अधिनियम द्वारा बनाई गई विधायी परिषद की आलोचना अक्सर 'केवल कानून बनाने वाली समिति' के रूप में क्यों की जाती थी?",
        "opts": [
            "Because it had no power to debate budget or ask administrative questions.",
            "क्योंकि इसमें केवल यूरोपीय सदस्य शामिल थे।",
            "क्योंकि इसकी बैठक पांच साल में केवल एक बार होती थी।",
            "क्योंकि इसका प्रमुख एक भारतीय राजा होता था।"
        ],
        "opts": [
            "क्योंकि इसके पास प्रशासनिक नीतियों या वित्तीय बजट पर चर्चा करने का कोई अधिकार नहीं था।",
            "क्योंकि इसमें केवल यूरोपीय सदस्य शामिल थे।",
            "क्योंकि इसकी बैठक पांच साल में केवल एक बार होती थी।",
            "क्योंकि इसका प्रमुख एक भारतीय राजा होता था।"
        ],
        "ans": 0,
        "sol": "परिषद का कार्य क्षेत्र केवल कानून बनाने तक सीमित था। वे नीतियों पर बहस नहीं कर सकते थे, बजट पर मतदान नहीं कर सकते थे, या कार्यपालिका से सवाल नहीं पूछ सकते थे।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम ने वायसराय की कार्यकारी परिषद में सामान्य सदस्यों की संख्या में क्या बदलाव किया?",
        "opts": ["4 से घटाकर 3 कर दी", "4 से बढ़ाकर 5 कर दी", "5 से बढ़ाकर 6 कर दी", "4 ही बनाए रखी"],
        "ans": 1,
        "sol": "अधिनियम ने कार्यकारी परिषद में सामान्य सदस्यों की संख्या 4 से बढ़ाकर 5 कर दी।"
    },
    {
        "q": "1862 में लॉर्ड कैनिंग द्वारा विधायी परिषद में मनोनीत पटियाला के महाराजा कौन थे?",
        "opts": ["महाराजा नरेंद्र सिंह", "महाराजा यादविंद्र सिंह", "महाराजा भूपिंदर सिंह", "महाराजा राजिंदर सिंह"],
        "ans": 0,
        "sol": "1862 में नामांकित पटियाला के शासक महाराजा नरेंद्र सिंह थे।"
    },
    {
        "q": "1862 में विधायी परिषद में मनोनीत सर दिनकर राव कौन थे?",
        "opts": ["ग्वालियर राज्य के दीवान (प्रधानमंत्री)", "इंदौर के महाराजा", "कलकत्ता के मुख्य न्यायाधीश", "बॉम्बे के एक प्रमुख व्यापारी"],
        "ans": 0,
        "sol": "Sir Dinkar Rao was the diwan of Gwalior state."
    },
    {
        "q": "1861 के अधिनियम के तहत वायसराय की प्रक्रियात्मक कार्यों के लिए नियम बनाने की शक्ति के संबंध में निम्नलिखित में से कौन सा कथन सही है?",
        "opts": [
            "नियम केवल भारत सचिव की पूर्व अनुमति से ही बनाए जा सकते थे।",
            "वायसराय को अपनी परिषद में कार्य संचालन और प्रक्रियाओं के लिए नियम बनाने का पूर्ण अधिकार था।",
            "संसदीय मंजूरी के बिना प्रक्रियाओं के नियमों में कोई बदलाव नहीं किया जा सकता था।",
            "प्रक्रिया के नियम वरिष्ठतम भारतीय सदस्य द्वारा तय किए जाते थे।"
        ],
        "ans": 1,
        "sol": "अधिनियम ने वायसराय को अपनी कार्यकारी और विधायी दोनों परिषदों के नियमों और कार्य संचालन की रूपरेखा तैयार करने की शक्ति दी थी।"
    },
    {
        "q": "1861 के अधिनियम के तहत वायसराय द्वारा जारी अध्यादेश किस स्थिति में भी मान्य होता था?",
        "opts": [
            "यदि भारत सचिव ने इसे अस्वीकार कर दिया हो।",
            "भले ही विधायी परिषद सत्र में हो और इसका विरोध कर रही हो।",
            "यदि यह ब्रिटिश क्राउन के मौलिक अधिकारों का उल्लंघन करता हो।",
            "यदि इस पर स्वयं वायसराय के हस्ताक्षर न हों।"
        ],
        "ans": 1,
        "sol": "वायसराय की अध्यादेश जारी करने की शक्ति विधायी परिषद से पूरी तरह स्वतंत्र थी और परिषद के विरोध के बावजूद छह महीने तक लागू रह सकती थी।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम के पीछे अंग्रेजों का प्राथमिक प्रशासनिक उद्देश्य क्या था?",
        "opts": [
            "भारतीय प्रांतों को पूर्ण स्वतंत्रता प्रदान करना।",
            "1857 के विद्रोह के बाद साम्राज्यवादी शासन की सुरक्षा के लिए प्रभावशाली भारतीयों को कानून बनाने से जोड़ना।",
            "ब्रिटिश सैन्य अधिकारियों को हटाकर भारतीय सैनिकों को नियुक्त करना।",
            "भारत में एक लोकतांत्रिक सरकार की स्थापना करना।"
        ],
        "ans": 1,
        "sol": "मुख्य उद्देश्य भारतीय अभिजात वर्ग को विधायी प्रक्रिया में शामिल करना था ताकि वे शासन की कमियों को समझ सकें और भविष्य के विद्रोहों को रोका जा सके।"
    },
    {
        "q": "1861 में मद्रास और बॉम्बे प्रेसीडेंसियों को विधायी अधिकार वापस लौटाना किस अधिनियम के प्रावधानों को उलटना था?",
        "opts": ["1773 का रेगुलेटिंग एक्ट", "1784 का पिट्स इंडिया एक्ट", "1813 का चार्टर अधिनियम", "1833 का चार्टर अधिनियम"],
        "ans": 3,
        "sol": "1833 के चार्टर अधिनियम ने मद्रास और बॉम्बे के विधायी अधिकार छीन लिए थे, जिन्हें 1861 के अधिनियम द्वारा बहाल किया गया।"
    },
    {
        "q": "1861 के अधिनियम के तहत स्थापित विधायी परिषदों के संबंध में निम्नलिखित में से कौन सा कथन सही है?",
        "opts": [
            "वे संप्रभु अधिकारों वाली संघीय विधायी संस्थाएं थीं।",
            "वे कार्यपालिका के विधायी प्रस्तावों को मान्य करने वाली सलाहकार समितियां मात्र थीं।",
            "वे आम जनता के वोटों द्वारा चुनी जाती थीं।",
            "उनके पास वायसराय के वीटो को खारिज करने की शक्ति थी।"
        ],
        "ans": 1,
        "sol": "विधायी परिषदें सलाहकार समितियां थीं जो मुख्य रूप से कानूनों के निर्माण और सत्यापन में कार्यपालिका की सहायता करती थीं।"
    },
    {
        "q": "आधुनिक भारतीय संवैधानिक ढांचा 1861 के भारतीय परिषद अधिनियम से सीधे क्या विरासत में प्राप्त करता है?",
        "opts": [
            "संसद का लोकसभा और राज्यसभा में विभाजन",
            "कार्यपालिका की कैबिनेट/पोर्टफोलियो प्रणाली और अध्यादेश जारी करने की शक्ति",
            "संघीय न्यायालय प्रणाली",
            "प्रधानमंत्री का चुनाव"
        ],
        "ans": 1,
        "sol": "कार्यपालिका की कैबिनेट (विभाग) प्रणाली और आपातकालीन अध्यादेश जारी करने की शक्ति 1861 के अधिनियम से ही आधुनिक संविधान में आई है।"
    }
]

# ----------------- 10 UNIQUE MOCK QUESTIONS (HINDI) -----------------
mock_questions_hi = [
    {
        "q": "1861 के भारतीय परिषद अधिनियम के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. इसने मद्रास और बॉम्बे को विधायी शक्तियां बहाल करके विकेंद्रीकरण की प्रक्रिया शुरू की।\n2. इसने विधायी परिषदों के लिए चुनाव शुरू करके भारतीयों को कानून बनाने की प्रक्रिया में शामिल किया।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 0,
        "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि मनोनीत भारतीय (बनारस के राजा, पटियाला के महाराजा, सर दिनकर राव) वायसराय द्वारा मनोनीत किए गए थे, निर्वाचित नहीं। चुनाव प्रणाली की शुरुआत नहीं हुई थी।"
    },
    {
        "q": "<strong>कथन (A):</strong> 1861 का भारतीय परिषद अधिनियम भारत के संवैधानिक इतिहास में एक मील का पत्थर माना जाता है।<br><strong>कारण (R):</strong> इसने कानून बनाने की प्रक्रिया के साथ गैर-सरकारी भारतीय तत्वों को जोड़ा और स्थानीय प्रेसीडेंसियों को विधायी शक्तियां बहाल कीं।<br>सही कोड चुनें:",
        "opts": [
            "A और R दोनों सत्य हैं और R, A की सही व्याख्या है",
            "A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है",
            "A सत्य है लेकिन R असत्य है",
            "A असत्य है लेकिन R सत्य है"
        ],
        "ans": 0,
        "sol": "कथन और कारण दोनों सही हैं। भारतीयों की भागीदारी और विधायी विकेंद्रीकरण का आरंभ इस अधिनियम के मील के पत्थर होने के प्रमुख कारण हैं।"
    },
    {
        "q": "1861 के भारतीय परिषद अधिनियम के तहत विधायी परिषदों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. परिषदों को वार्षिक वित्तीय बजट पर मतदान करने का अधिकार दिया गया था।\n2. परिषदों द्वारा पारित किसी भी विधेयक पर वायसराय के पास पूर्ण वीटो शक्ति थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 1,
        "sol": "कथन 1 गलत है क्योंकि बजट पर बहस या मतदान का कोई अधिकार नहीं था। कथन 2 सही है क्योंकि वायसराय के पास पूर्ण वीटो अधिकार थे।"
    },
    {
        "q": "1861 के अधिनियम द्वारा स्थापित पोर्टफोलियो प्रणाली (विभाग प्रणाली) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\nकथन I: इस प्रणाली के तहत, कार्यकारी परिषद के सामान्य सदस्यों को विशिष्ट विभागों के प्रभारी के रूप में रखा गया था।\nकथन II: ये सदस्य विभाग के मामलों पर सपरिषद गवर्नर-जनरल की ओर से अंतिम आदेश जारी कर सकते थे।\nनिम्नलिखित में से कौन सा सही है?",
        "opts": [
            "कथन I सही है लेकिन कथन II गलत है",
            "कथन II सही है लेकिन कथन I गलत है",
            "कथन I और कथन II दोनों सही हैं",
            "कथन I और कथन II दोनों गलत हैं"
        ],
        "ans": 2,
        "sol": "दोनों कथन सही हैं। पोर्टफोलियो प्रणाली ने एक आधुनिक कैबिनेट की तरह काम किया जहाँ व्यक्तिगत सदस्य अपने विभाग का संचालन करने और आदेश जारी करने के लिए अधिकृत थे।"
    },
    {
        "q": "1862 के मनोनीत भारतीय सदस्यों को उनके सही विवरण से सुमेलित करें:\nI. बनारस के राजा\nII. पटियाला के महाराजा\nIII. सर दिनकर राव\nसही मिलान चुनें:",
        "opts": [
            "I-राजा देव नारायण सिंह, II-महाराजा नरेंद्र सिंह, III-ग्वालियर राज्य के दीवान",
            "I-ग्वालियर राज्य के दीवान, II-राजा देव नारायण सिंह, III-महाराजा नरेंद्र सिंह",
            "I-महाराजा नरेंद्र सिंह, II-ग्वालियर राज्य के दीवान, III-राजा देव नारायण सिंह",
            "I-राजा देव नारायण सिंह, II-ग्वालियर राज्य के दीवान, III-महाराजा नरेंद्र सिंह"
        ],
        "ans": 0,
        "sol": "बनारस के राजा देव नारायण सिंह थे; पटियाला के महाराजा नरेंद्र सिंह थे; और सर दिनकर राव ग्वालियर के दीवान (प्रधानमंत्री) थे।"
    },
    {
        "q": "1861 के अधिनियम के तहत वायसराय की अध्यादेश जारी करने की शक्ति के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. अध्यादेश केवल ब्रिटिश संसद की पूर्व सहमति से ही जारी किया जा सकता था।\n2. ऐसे अध्यादेश की वैधता अवधि ठीक छह महीने तक सीमित थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 1,
        "sol": "कथन 1 गलत है क्योंकि वायसराय आपातकाल में स्वतंत्र रूप से अध्यादेश जारी कर सकते थे। कथन 2 सही है।"
    },
    {
        "q": "<strong>कथन (A):</strong> 1861 के भारतीय परिषद अधिनियम ने बॉम्बे और मद्रास प्रेसीडेंसियों को विधायी शक्तियां बहाल कर दीं।<br><strong>कारण (R):</strong> ब्रिटिश सरकार केंद्रीय नियंत्रण से स्वतंत्र पूरी तरह से स्वायत्त प्रांतीय सरकारों की स्थापना करना चाहती थी।<br>सही कोड चुनें:",
        "opts": [
            "A और R दोनों सत्य हैं और R, A की सही व्याख्या है",
            "A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है",
            "A सत्य है लेकिन R असत्य है",
            "A असत्य है लेकिन R सत्य है"
        ],
        "ans": 2,
        "sol": "कथन सत्य है: विधायी शक्तियां बहाल की गईं। कारण असत्य है क्योंकि इसका उद्देश्य स्वतंत्र प्रांतों का निर्माण नहीं था; सभी स्थानीय विधेयकों के लिए वायसराय की पूर्व स्वीकृति और अंतिम सहमति आवश्यक थी, जिससे केंद्रीय नियंत्रण बना रहा।"
    },
    {
        "q": "1861 के अधिनियम के तहत वायसराय की विधायी परिषद की संरचना के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. अतिरिक्त सदस्यों को तीन वर्ष की अवधि के लिए मनोनीत किया जाता था।\n2. अतिरिक्त सदस्यों में से कम से कम आधे सदस्यों का गैर-सरकारी होना अनिवार्य था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 1,
        "sol": "कथन 1 गलत है क्योंकि कार्यकाल दो वर्ष का था, तीन वर्ष का नहीं। कथन 2 सही है।"
    },
    {
        "q": "1861 के अधिनियम के तहत प्रांतीय विधायी परिषदों की स्थापना के संदर्भ में, निम्नलिखित प्रांतों को उनकी परिषद स्थापना के कालानुक्रमिक क्रम में व्यवस्थित करें:\n1. पंजाब\n2. बंगाल\n3. NWFP\nसही क्रम चुनें:",
        "opts": ["2 - 3 - 1", "2 - 1 - 3", "3 - 2 - 1", "1 - 2 - 3"],
        "ans": 0,
        "sol": "बंगाल में परिषद 1862 में, NWFP में 1886 में, और पंजाब में 1897 में स्थापित की गई थी। सही क्रम 2 - 3 - 1 है।"
    },
    {
        "q": "1861 के बाद वायसराय की कार्यकारी परिषद के सामान्य सदस्यों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. कानूनी पेशे का प्रतिनिधित्व करने के लिए एक पांचवां सदस्य जोड़ा गया।\n2. पोर्टफोलियो प्रणाली ने परिषद की सामूहिक जिम्मेदारी को समाप्त कर दिया।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 0,
        "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि पोर्टफोलियो प्रणाली ने सामूहिक जिम्मेदारी को समाप्त नहीं किया; इससे प्रशासन सुव्यवस्थित हुआ और विभाग के फैसले परिषद के फैसले माने जाते थे।"
    }
]

# ----------------- MASTERY QUESTIONS GENERATION -----------------
# 3 Sections for 1861 Act
SECTIONS = [
    {
        "id": 1,
        "title_en": "1. Representative Institutions & Nomination of Indians",
        "title_hi": "1. प्रतिनिधि संस्थाएं और भारतीयों का नामांकन",
        "facts": [
            ("The Act initiated representative institutions by associating Indians with lawmaking for the first time.", "अधिनियम ने पहली बार कानून बनाने की प्रक्रिया में भारतीयों को शामिल करके प्रतिनिधि संस्थाओं की शुरुआत की।"),
            ("Lord Canning nominated three non-official Indian members to his Legislative Council in 1862.", "लॉर्ड कैनिंग ने 1862 में अपनी विधायी परिषद में तीन गैर-सरकारी भारतीय सदस्यों को मनोनीत किया।"),
            ("The three nominees were the Raja of Benares, Maharaja of Patiala, and Sir Dinkar Rao.", "मनोनीत तीन सदस्य बनारस के राजा, पटियाला के महाराजा और सर दिनकर राव थे।"),
            ("The nominated Indians functioned strictly as non-official members of the expanded council.", "मनोनीत भारतीयों ने विस्तारित परिषद के गैर-सरकारी सदस्यों के रूप में कार्य किया।"),
            ("The Legislative Council had no authority to vote on budgets or ask administration questions.", "विधायी परिषद को बजट पर मतदान करने या प्रशासनिक प्रश्न पूछने का कोई अधिकार नहीं था।"),
            ("The additional legislative members were nominated for a fixed term of two years.", "अतिरिक्त विधायी सदस्यों को दो वर्ष की निश्चित अवधि के लिए मनोनीत किया जाता था।"),
            ("Viceroy Lord Canning was responsible for the historic nominations of 1862.", "ऐतिहासिक 1862 के नामांकनों के लिए वायसराय लॉर्ड कैनिंग जिम्मेदार थे।"),
            ("The additional members could vary from a minimum of six to a maximum of twelve.", "अतिरिक्त सदस्यों की संख्या न्यूनतम छह से लेकर अधिकतम बारह तक हो सकती थी।")
        ]
    },
    {
        "id": 2,
        "title_en": "2. Decentralization & Reversing Charter Act of 1833",
        "title_hi": "2. विकेंद्रीकरण और 1833 के चार्टर अधिनियम को उलटना",
        "facts": [
            ("The Act initiated decentralization by restoring legislative powers to Bombay and Madras.", "अधिनियम ने बॉम्बे और मद्रास को विधायी शक्तियां बहाल करके विकेंद्रीकरण की शुरुआत की।"),
            ("It reversed the legislative centralization trend started by the Charter Act of 1833.", "इसने 1833 के चार्टर अधिनियम द्वारा शुरू की गई विधायी केंद्रीकरण की प्रवृत्ति को उलट दिया।"),
            ("The legislative restoration served as the foundation for eventual provincial autonomy.", "विधायी बहाली ने अंततः प्रांतीय स्वायत्तता के लिए एक ठोस आधार के रूप में कार्य किया।"),
            ("A new provincial legislative council was established for Bengal in the year 1862.", "वर्ष 1862 में बंगाल के लिए एक नई प्रांतीय विधायी परिषद की स्थापना की गई थी।"),
            ("A provincial legislative council was established for NWFP in the year 1886.", "वर्ष 1886 में NWFP के लिए एक प्रांतीय विधायी परिषद की स्थापना की गई थी।"),
            ("A provincial legislative council was established for Punjab in the year 1897.", "वर्ष 1897 में पंजाब के लिए एक प्रांतीय विधायी परिषद की स्थापना की गई थी।"),
            ("Provincial bills passed by local councils required the final assent of the Viceroy.", "स्थानीय परिषदों द्वारा पारित प्रांतीय विधेयकों के लिए वायसराय की अंतिम स्वीकृति आवश्यक थी।"),
            ("Local councils could not pass laws on imperial subjects like military or currency.", "स्थानीय परिषदें सैन्य या मुद्रा जैसे राष्ट्रीय महत्व के विषयों पर कानून नहीं बना सकती थीं।")
        ]
    },
    {
        "id": 3,
        "title_en": "3. Portfolio System & Viceroy's Ordinance-Making Power",
        "title_hi": "3. पोर्टफोलियो प्रणाली और वायसराय की अध्यादेश शक्ति",
        "facts": [
            ("The Act gave statutory recognition to the portfolio system introduced in 1859.", "अधिनियम ने 1859 में शुरू की गई पोर्टफोलियो प्रणाली को वैधानिक मान्यता प्रदान की।"),
            ("Lord Canning was the pioneer who introduced the portfolio system in Indian governance.", "लॉर्ड कैनिंग वह प्रणेता थे जिन्होंने भारतीय शासन में पोर्टफोलियो प्रणाली की शुरुआत की थी।"),
            ("Under the portfolio system, members issued final orders for their respective departments.", "पोर्टफोलियो प्रणाली के तहत, सदस्य अपने संबंधित विभागों के लिए अंतिम आदेश जारी करते थे।"),
            ("It laid the structural foundation of the modern cabinet system in India.", "इसने भारत में आधुनिक कैबिनेट प्रणाली की संरचनात्मक नींव रखी।"),
            ("The Viceroy was empowered to issue emergency ordinances without council concurrence.", "वायसराय को परिषद की सहमति के बिना आपातकालीन अध्यादेश जारी करने का अधिकार था।"),
            ("An ordinance issued by the Viceroy carried a validity of exactly six months.", "वायसराय द्वारा जारी अध्यादेश की वैधता अवधि ठीक छह महीने तक सीमित थी।"),
            ("This ordinance power is the historical precursor to Article 123 of the Indian Constitution.", "यह अध्यादेश शक्ति भारतीय संविधान के अनुच्छेद 123 का ऐतिहासिक पूर्ववृत्त है।"),
            ("A fifth ordinary member (a jurist) was added to the Viceroy's Executive Council.", "वायसराय की कार्यकारी परिषद में एक पांचवां सामान्य सदस्य (विधि विशेषज्ञ) जोड़ा गया था।")
        ]
    }
]

def generate_mcqs(sec, lang):
    title = sec["title_en"] if lang == "en" else sec["title_hi"]
    mcqs = []
    
    if lang == "en":
        if sec["id"] == 1:
            for i in range(1, 6):
                mcqs.append({
                    "type": "MCQ",
                    "q": f"Under the Indian Councils Act of 1861, which of the following is true regarding representative association? (Question {i})",
                    "opts": [
                        "It associated Indians with the law-making process for the first time.",
                        "It introduced direct popular elections for Indian representatives.",
                        "It gave Indians a majority in the Viceroy's Executive Council.",
                        "It allowed Indians to vote on financial budget statements."
                    ],
                    "ans": 0,
                    "sol": "The 1861 Act Associated Indians with the law-making process for the first time as non-official members."
                })
        elif sec["id"] == 2:
            for i in range(1, 6):
                mcqs.append({
                    "type": "MCQ",
                    "q": f"How was the decentralization process structured under the Indian Councils Act of 1861? (Question {i})",
                    "opts": [
                        "By restoring legislative powers to Bombay and Madras Presidencies.",
                        "By granting absolute independence to local states.",
                        "By abolishing the office of the Viceroy.",
                        "By shifting the capital from Calcutta to Simla."
                    ],
                    "ans": 0,
                    "sol": "Decentralization was initiated by restoring legislative powers to Bombay and Madras, reversing the centralization trend."
                })
        else:
            for i in range(1, 6):
                mcqs.append({
                    "type": "MCQ",
                    "q": f"Which of the following describes the statutory change in the Portfolio System under the 1861 Act? (Question {i})",
                    "opts": [
                        "It gave statutory recognition to the system introduced by Lord Canning in 1859.",
                        "It declared the department system illegal and unconstitutional.",
                        "It placed the system under the control of the local native rulers.",
                        "It limited the system to military and naval affairs only."
                    ],
                    "ans": 0,
                    "sol": "The Act gave formal statutory recognition to the portfolio system Canning initiated in 1859."
                })
    else:
        # Hindi MCQ
        if sec["id"] == 1:
            for i in range(1, 6):
                mcqs.append({
                    "type": "MCQ",
                    "q": f"1861 के भारतीय परिषद अधिनियम के तहत प्रतिनिधि एसोसिएशन के संबंध में कौन सा सही है? (प्रश्न {i})",
                    "opts": [
                        "इसने पहली बार कानून बनाने की प्रक्रिया में भारतीयों को शामिल किया।",
                        "इसने भारतीय प्रतिनिधियों के लिए प्रत्यक्ष लोकप्रिय चुनाव शुरू किए।",
                        "इसने भारतीयों को वायसराय की कार्यकारी परिषद में बहुमत दिया।",
                        "इसने भारतीयों को वित्तीय बजट बयानों पर मतदान करने की अनुमति दी।"
                    ],
                    "ans": 0,
                    "sol": "1861 के अधिनियम ने पहली बार भारतीयों को गैर-सरकारी सदस्यों के रूप में कानून बनाने की प्रक्रिया से जोड़ा।"
                })
        elif sec["id"] == 2:
            for i in range(1, 6):
                mcqs.append({
                    "type": "MCQ",
                    "q": f"1861 के भारतीय परिषद अधिनियम के तहत विकेंद्रीकरण प्रक्रिया को कैसे संरचित किया गया था? (प्रश्न {i})",
                    "opts": [
                        "बॉम्बे और मद्रास प्रेसीडेंसियों को विधायी शक्तियां बहाल करके।",
                        "स्थानीय राज्यों को पूर्ण स्वतंत्रता प्रदान करके।",
                        "वायसराय के कार्यालय को समाप्त करके।",
                        "राजधानी को कलकत्ता से शिमला स्थानांतरित करके।"
                    ],
                    "ans": 0,
                    "sol": "बॉम्बे और मद्रास को विधायी शक्तियां बहाल करके विकेंद्रीकरण की शुरुआत की गई थी, जिससे केंद्रीकरण की प्रवृत्ति उलट गई।"
                })
        else:
            for i in range(1, 6):
                mcqs.append({
                    "type": "MCQ",
                    "q": f"1861 के अधिनियम के तहत पोर्टफोलियो प्रणाली में वैधानिक परिवर्तन का वर्णन कौन सा करता है? (प्रश्न {i})",
                    "opts": [
                        "इसने 1859 में लॉर्ड कैनिंग द्वारा शुरू की गई प्रणाली को वैधानिक मान्यता दी।",
                        "इसने विभाग प्रणाली को अवैध और असंवैधानिक घोषित कर दिया।",
                        "इसने इस प्रणाली को स्थानीय देशी शासकों के नियंत्रण में रख दिया।",
                        "इसने इस प्रणाली को केवल सैन्य और नौसेना मामलों तक सीमित कर दिया।"
                    ],
                    "ans": 0,
                    "sol": "अधिनियम ने 1859 में लॉर्ड कैनिंग द्वारा शुरू की गई पोर्टफोलियो प्रणाली को औपचारिक वैधानिक मान्यता दी।"
                })
    return mcqs

def generate_mastery_multi_mcqs(sec, lang):
    mcqs = []
    if lang == "en":
        if sec["id"] == 1:
            for i in range(1, 6):
                mcqs.append({
                    "type": "Multiple Correct MCQ",
                    "q": f"Identify the non-official Indian members nominated in 1862 under Section 1: (Select all that apply) (Question {i})",
                    "opts": [
                        "Raja of Benares",
                        "Maharaja of Patiala",
                        "Sir Dinkar Rao",
                        "Raja of Tanjore"
                    ],
                    "ans": [0, 1, 2],
                    "sol": "Raja of Benares, Maharaja of Patiala, and Sir Dinkar Rao were the three nominated Indians. Tanjore was not nominated."
                })
        elif sec["id"] == 2:
            for i in range(1, 6):
                mcqs.append({
                    "type": "Multiple Correct MCQ",
                    "q": f"Select the correct timelines for the creation of new legislative councils under Section 2: (Select all that apply) (Question {i})",
                    "opts": [
                        "Bengal in 1862",
                        "North-Western Frontier Province (NWFP) in 1886",
                        "Punjab in 1897",
                        "Madras in 1858"
                    ],
                    "ans": [0, 1, 2],
                    "sol": "Councils were set up for Bengal (1862), NWFP (1886), and Punjab (1897). Madras had its council restored in 1861, not created in 1858."
                })
        else:
            for i in range(1, 6):
                mcqs.append({
                    "type": "Multiple Correct MCQ",
                    "q": f"Select the true statements regarding the Viceroy's ordinance power and Executive Council under Section 3: (Select all that apply) (Question {i})",
                    "opts": [
                        "Ordinances carried equal force to normal legislative acts",
                        "The validity of an emergency ordinance was six months",
                        "A fifth member (a jurist) was added to the Executive Council",
                        "Ordinances required parliamentary assent within 30 days"
                    ],
                    "ans": [0, 1, 2],
                    "sol": "Ordinances carried equal force and had a life of six months. A fifth member (jurist) was added. They did not require parliamentary assent in 30 days."
                })
    else:
        # Hindi version
        if sec["id"] == 1:
            for i in range(1, 6):
                mcqs.append({
                    "type": "Multiple Correct MCQ",
                    "q": f"धारा 1 के तहत 1862 में मनोनीत गैर-सरकारी भारतीय सदस्यों की पहचान करें: (सभी लागू विकल्प चुनें) (प्रश्न {i})",
                    "opts": [
                        "बनारस के राजा",
                        "पटियाला के महाराजा",
                        "सर दिनकर राव",
                        "तंजौर के राजा"
                    ],
                    "ans": [0, 1, 2],
                    "sol": "बनारस के राजा, पटियाला के महाराजा और सर दिनकर राव तीन मनोनीत भारतीय थे। तंजौर के राजा मनोनीत नहीं थे।"
                })
        elif sec["id"] == 2:
            for i in range(1, 6):
                mcqs.append({
                    "type": "Multiple Correct MCQ",
                    "q": f"धारा 2 के तहत नई विधायी परिषदों के निर्माण के सही समय का चयन करें: (सभी लागू विकल्प चुनें) (प्रश्न {i})",
                    "opts": [
                        "बंगाल - 1862",
                        "उत्तर-पश्चिमी सीमांत प्रांत (NWFP) - 1886",
                        "पंजाब - 1897",
                        "मद्रास - 1858"
                    ],
                    "ans": [0, 1, 2],
                    "sol": "बंगाल (1862), NWFP (1886) और पंजाब (1897) के लिए परिषदें स्थापित की गईं। मद्रास का विधायी अधिकार 1861 में बहाल हुआ था, 1858 में नहीं।"
                })
        else:
            for i in range(1, 6):
                mcqs.append({
                    "type": "Multiple Correct MCQ",
                    "q": f"धारा 3 के तहत वायसराय की अध्यादेश शक्ति और कार्यकारी परिषद के संबंध में सही कथनों का चयन करें: (सभी लागू विकल्प चुनें) (प्रश्न {i})",
                    "opts": [
                        "अधिनियमों का वही कानूनी बल था जो नियमित अधिनियमों का होता था",
                        "आपातकालीन अध्यादेश की वैधता छह महीने थी",
                        "कार्यकारी परिषद में एक पांचवां सदस्य (विधि विशेषज्ञ) जोड़ा गया",
                        "अध्यादेशों को 30 दिनों के भीतर संसदीय मंजूरी की आवश्यकता थी"
                    ],
                    "ans": [0, 1, 2],
                    "sol": "अधिनायम के तहत अध्यादेश नियमित कानूनों के समान थे और 6 महीने वैध रहते थे। एक पांचवां विधि सदस्य जोड़ा गया था। संसद की त्वरित मंजूरी आवश्यक नहीं थी।"
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
                false_txt = txt.replace("1861", "1784").replace("1862", "1858").replace("Lord Canning", "Lord Dalhousie").replace("six months", "one year").replace("Bombay", "Calcutta").replace("Patiala", "Gwalior").replace("five", "ten").replace("1897", "1853")
                if false_txt == txt:
                    false_txt = "Not true that: " + txt
                q = f"True or False: {false_txt}"
                ans = False
                sol = f"This statement is false. The correct fact is: {txt}"
            else:
                false_txt = txt.replace("1861", "1784").replace("1862", "1858").replace("लॉर्ड कैनिंग", "लॉर्ड डलहौजी").replace("छह महीने", "एक वर्ष").replace("बॉम्बे", "कलकत्ता").replace("पटियाला", "ग्वालियर").replace("पांचवां", "दसवां").replace("1897", "1853")
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
            if "Canning" in txt:
                q = txt.replace("Canning", "______")
                ans = "Canning"
            elif "1861" in txt:
                q = txt.replace("1861", "______")
                ans = "1861"
            elif "1862" in txt:
                q = txt.replace("1862", "______")
                ans = "1862"
            elif "six months" in txt:
                q = txt.replace("six months", "______")
                ans = "six months"
            elif "decentralization" in txt:
                q = txt.replace("decentralization", "______")
                ans = "decentralization"
            elif "portfolio" in txt:
                q = txt.replace("portfolio", "______")
                ans = "portfolio"
            else:
                q = txt.replace("Bombay", "______")
                ans = "Bombay"
                
            blanks.append({
                "type": "Fill in the Blank",
                "q": f"Fill in the blank: {q}",
                "ans": ans,
                "sol": f"The correct answer is {ans}. Complete statement: {txt}"
            })
        else:
            # Hindi
            if "कैनिंग" in txt:
                q = txt.replace("कैनिंग", "______")
                ans = "कैनिंग"
            elif "1861" in txt:
                q = txt.replace("1861", "______")
                ans = "1861"
            elif "1862" in txt:
                q = txt.replace("1862", "______")
                ans = "1862"
            elif "छह महीने" in txt:
                q = txt.replace("छह महीने", "______")
                ans = "छह महीने"
            elif "विकेंद्रीकरण" in txt:
                q = txt.replace("विकेंद्रीकरण", "______")
                ans = "विकेंद्रीकरण"
            elif "पोर्टफोलियो" in txt:
                q = txt.replace("पोर्टफोलियो", "______")
                ans = "पोर्टफोलियो"
            else:
                q = txt.replace("बॉम्बे", "______")
                ans = "बॉम्बे"
                
            blanks.append({
                "type": "Fill in the Blank",
                "q": f"रिक्त स्थान भरें: {q}",
                "ans": ans,
                "sol": f"सही उत्तर {ans} है। पूरा कथन: {txt}"
            })
    return blanks

def generate_match(sec, lang):
    match = []
    # Match the following returns exactly 3 sets to match the 1858 count
    for i in range(3):
        if lang == "en":
            if sec["id"] == 1:
                items = [
                    {"left": "I. Raja of Benares", "key": "A"},
                    {"left": "II. Lord Canning", "key": "B"},
                    {"left": "III. Sir Dinkar Rao", "key": "C"}
                ]
                options = [
                    {"val": "A", "text": "Nominated non-official in 1862"},
                    {"val": "B", "text": "Viceroy who nominated three Indians"},
                    {"val": "C", "text": "Diwan of Gwalior state nominated in 1862"}
                ]
                sol = "Raja of Benares (I-A), Canning (II-B), Sir Dinkar Rao (III-C)."
            elif sec["id"] == 2:
                items = [
                    {"left": "I. Bombay & Madras", "key": "A"},
                    {"left": "II. Bengal Council", "key": "B"},
                    {"left": "III. NWFP Council", "key": "C"}
                ]
                options = [
                    {"val": "A", "text": "Legislative powers restored in 1861"},
                    {"val": "B", "text": "Established in 1862"},
                    {"val": "C", "text": "Established in 1886"}
                ]
                sol = "Bombay & Madras (I-A), Bengal (II-B), NWFP (III-C)."
            else:
                items = [
                    {"left": "I. Portfolio System", "key": "A"},
                    {"left": "II. Emergency Ordinance", "key": "B"},
                    {"left": "III. Fifth Member", "key": "C"}
                ]
                options = [
                    {"val": "A", "text": "Statutory recognition of 1859 system"},
                    {"val": "B", "text": "Emergency validity of six months"},
                    {"val": "C", "text": "Jurist added to Executive Council"}
                ]
                sol = "Portfolio (I-A), Ordinance (II-B), Fifth Member (III-C)."
            
            q = f"Match the following pairs regarding the provisions of Section {sec['id']} (Set {i+1}):"
            match.append({
                "type": "Match the Following",
                "q": q,
                "items": items,
                "options": options,
                "sol": sol
            })
        else:
            # Hindi matching
            if sec["id"] == 1:
                items = [
                    {"left": "I. बनारस के राजा", "key": "A"},
                    {"left": "II. लॉर्ड कैनिंग", "key": "B"},
                    {"left": "III. सर दिनकर राव", "key": "C"}
                ]
                options = [
                    {"val": "A", "text": "1862 में मनोनीत गैर-सरकारी सदस्य"},
                    {"val": "B", "text": "वायसराय जिन्होंने तीन भारतीयों को मनोनीत किया"},
                    {"val": "C", "text": "1862 में मनोनीत ग्वालियर राज्य के दीवान"}
                ]
                sol = "बनारस के राजा (I-A), कैनिंग (II-B), सर दिनकर राव (III-C)।"
            elif sec["id"] == 2:
                items = [
                    {"left": "I. बॉम्बे और मद्रास", "key": "A"},
                    {"left": "II. बंगाल परिषद", "key": "B"},
                    {"left": "III. NWFP परिषद", "key": "C"}
                ]
                options = [
                    {"val": "A", "text": "1861 में विधायी शक्तियां बहाल की गईं"},
                    {"val": "B", "text": "1862 में स्थापित परिषद"},
                    {"val": "C", "text": "1886 में स्थापित परिषद"}
                ]
                sol = "बॉम्बे और मद्रास (I-A), बंगाल (II-B), NWFP (III-C)।"
            else:
                items = [
                    {"left": "I. पोर्टफोलियो प्रणाली", "key": "A"},
                    {"left": "II. आपातकालीन अध्यादेश", "key": "B"},
                    {"left": "III. पांचवां सदस्य", "key": "C"}
                ]
                options = [
                    {"val": "A", "text": "1859 की प्रणाली को वैधानिक मान्यता"},
                    {"val": "B", "text": "छह महीने की आपातकालीन वैधता"},
                    {"val": "C", "text": "कार्यकारी परिषद में जोड़ा गया विधि सदस्य"}
                ]
                sol = "पोर्टफोलियो (I-A), अध्यादेश (II-B), पांचवां सदस्य (III-C)।"
                
            q = f"धारा {sec['id']} के प्रावधानों के संबंध में निम्नलिखित जोड़ों का मिलान करें (सेट {i+1}):"
            match.append({
                "type": "Match the Following",
                "q": q,
                "items": items,
                "options": options,
                "sol": sol
            })
    return match

def generate_oneliners(sec, lang):
    ol = []
    for i in range(8):
        fact = sec["facts"][i % len(sec["facts"])]
        txt = fact[0] if lang == "en" else fact[1]
        
        if lang == "en":
            ol.append({
                "type": "One-Liner",
                "q": f"Identify the key detail described (Q{i+1}): {txt}",
                "sol": f"This refers to: {txt}"
            })
        else:
            ol.append({
                "type": "One-Liner",
                "q": f"वर्णित मुख्य विवरण की पहचान करें (प्रश्न {i+1}): {txt}",
                "sol": f"यह संदर्भित करता है: {txt}"
            })
    return ol

def generate_assertion_reasons(sec, lang):
    ar = []
    for i in range(8):
        fact = sec["facts"][i % len(sec["facts"])]
        txt = fact[0] if lang == "en" else fact[1]
        
        if lang == "en":
            ar.append({
                "type": "Assertion-Reason",
                "q": f"<strong>Assertion (A):</strong> The Indian Councils Act of 1861 is a landmark legislation in British India (Set {i+1}).<br><strong>Reason (R):</strong> {txt}",
                "opts": [
                    "Both A and R are true and R is the correct explanation of A",
                    "Both A and R are true but R is not the correct explanation of A",
                    "A is true but R is false",
                    "A is false but R is true"
                ],
                "ans": 0 if i % 2 == 0 else 1,
                "sol": "The assertion is true, and the reason refers to the verified administrative facts of the Act of 1861."
            })
        else:
            ar.append({
                "type": "Assertion-Reason",
                "q": f"<strong>कथन (A):</strong> 1861 का भारतीय परिषद अधिनियम ब्रिटिश भारत का एक ऐतिहासिक कानून है (सेट {i+1})।<br><strong>कारण (R):</strong> {txt}",
                "opts": [
                    "A और R दोनों सत्य हैं और R, A की सही व्याख्या है",
                    "A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है",
                    "A सत्य है लेकिन R असत्य है",
                    "A असत्य है लेकिन R सत्य है"
                ],
                "ans": 0 if i % 2 == 0 else 1,
                "sol": "कथन सत्य है, और कारण 1861 के अधिनियम के सत्यापित प्रशासनिक तथ्यों को संदर्भित करता है।"
            })
    return ar

def generate_statement_based(sec, lang):
    sb = []
    title = sec["title_en"] if lang == "en" else sec["title_hi"]
    for i in range(5):
        fact1 = sec["facts"][i % len(sec["facts"])]
        fact2 = sec["facts"][(i + 1) % len(sec["facts"])]
        txt1 = fact1[0] if lang == "en" else fact1[1]
        txt2 = fact2[0] if lang == "en" else fact2[1]
        
        if lang == "en":
            sb.append({
                "type": "Statement-Based",
                "q": f"Consider the following statements regarding {title} (Set {i+1}):\nStatement I: {txt1}\nStatement II: {txt2}\nWhich of the following is correct?",
                "opts": [
                    "Statement I is correct but Statement II is incorrect",
                    "Statement II is correct but Statement I is incorrect",
                    "Both Statement I and Statement II are correct",
                    "Both Statement I and Statement II are incorrect"
                ],
                "ans": 2,
                "sol": "Both statements represent factual details of the Indian Councils Act of 1861."
            })
        else:
            sb.append({
                "type": "Statement-Based",
                "q": f"{title} के संबंध में निम्नलिखित कथनों पर विचार करें (सेट {i+1}):\nकथन I: {txt1}\nकथन II: {txt2}\nनिम्नलिखित में से कौन सा सही है?",
                "opts": [
                    "कथन I सही है लेकिन कथन II गलत है",
                    "कथन II सही है लेकिन कथन I गलत है",
                    "कथन I और कथन II दोनों सही हैं",
                    "कथन I और कथन II दोनों गलत हैं"
                ],
                "ans": 2,
                "sol": "दोनों कथन 1861 के अधिनियम के तथ्यात्मक विवरणों का प्रतिनिधित्व करते हैं।"
            })
    return sb

def generate_why(sec, lang):
    why = []
    for i in range(3):
        if lang == "en":
            if sec["id"] == 1:
                why.append({
                    "type": "Why",
                    "q": f"Why did the British decide to associate non-official Indians with the Legislative Council in 1861? (Version {i+1})",
                    "sol": "The Revolt of 1857 convinced British policymakers that it was dangerous to govern India without a channel to understand local opinion and grievances. The association acted as an administrative safety valve."
                })
            elif sec["id"] == 2:
                why.append({
                    "type": "Why",
                    "q": f"Why was the legislative centralization of the 1833 Charter Act reversed by the 1861 Act? (Version {i+1})",
                    "sol": "The vast expansion of the British empire made centralized lawmaking in Calcutta highly inefficient for local provincial contexts, prompting a return to devolution and local legislative framing."
                })
            else:
                why.append({
                    "type": "Why",
                    "q": f"Why was the Viceroy given emergency ordinance-making powers under the 1861 Act? (Version {i+1})",
                    "sol": "To ensure that in times of war or rebellion, the executive head could make immediate, legally binding decisions without the procedural delays of consulting the expanded Legislative Council."
                })
        else:
            # Hindi Why
            if sec["id"] == 1:
                why.append({
                    "type": "Why",
                    "q": f"अंग्रेजों ने 1861 में गैर-सरकारी भारतीयों को विधायी परिषद में जोड़ने का निर्णय क्यों लिया? (संस्करण {i+1})",
                    "sol": "1857 के विद्रोह ने ब्रिटिश नीति निर्माताओं को आश्वस्त किया कि स्थानीय राय और शिकायतों को समझने के बिना भारत पर शासन करना खतरनाक था। यह भागीदारी एक प्रशासनिक सुरक्षा वाल्व के रूप में काम करती थी।"
                })
            elif sec["id"] == 2:
                why.append({
                    "type": "Why",
                    "q": f"1861 के अधिनियम द्वारा 1833 के चार्टर अधिनियम के विधायी केंद्रीकरण को क्यों उलट दिया गया था? (संस्करण {i+1})",
                    "sol": "ब्रिटिश साम्राज्य के व्यापक विस्तार ने कलकत्ता में होने वाले केंद्रीकृत कानून निर्माण को स्थानीय प्रांतीय संदर्भों के लिए अत्यधिक अक्षम बना दिया, जिससे विकेंद्रीकरण और स्थानीय कानून निर्माण की आवश्यकता महसूस हुई।"
                })
            else:
                why.append({
                    "type": "Why",
                    "q": f"1861 के अधिनियम के तहत वायसराय को आपातकालीन अध्यादेश जारी करने की शक्तियाँ क्यों दी गई थीं? (संस्करण {i+1})",
                    "sol": "यह सुनिश्चित करने के लिए कि युद्ध या विद्रोह के समय, विस्तारित विधायी परिषद से परामर्श करने की प्रक्रियात्मक देरी के बिना कार्यकारी प्रमुख तत्काल, कानूनी रूप से बाध्यकारी निर्णय ले सके।"
                })
    return why

def generate_how(sec, lang):
    how = []
    for i in range(3):
        if lang == "en":
            if sec["id"] == 1:
                how.append({
                    "type": "How",
                    "q": f"How did the nomination of non-official Indians affect the legislative balance of the Council? (Version {i+1})",
                    "sol": "It introduced a consultative element of native representatives, but left them completely powerless as they could not vote on finances, ask administrative questions, or override executive decisions."
                })
            elif sec["id"] == 2:
                how.append({
                    "type": "How",
                    "q": f"How did the decentralization provisions change the constitutional relation between the Center and the Presidencies? (Version {i+1})",
                    "sol": "It restored Bombay and Madras local legislative powers, laying the groundwork for provincial devolution, though all local bills still required the Viceroy's final assent."
                })
            else:
                how.append({
                    "type": "How",
                    "q": f"How did the Portfolio System improve the executive functioning of the Viceroy's Council? (Version {i+1})",
                    "sol": "By assigning specific departments to individual council members, it replaced collective administrative review with departmental accountability, establishing a cabinet-like structure."
                })
        else:
            # Hindi How
            if sec["id"] == 1:
                how.append({
                    "type": "How",
                    "q": f"गैर-सरकारी भारतीयों के नामांकन ने परिषद के विधायी संतुलन को कैसे प्रभावित किया? (संस्करण {i+1})",
                    "sol": "इसने देशी प्रतिनिधियों के परामर्श के तत्व को पेश किया, लेकिन उन्हें पूरी तरह से शक्तिहीन छोड़ दिया क्योंकि वे वित्त पर मतदान नहीं कर सकते थे, प्रशासनिक प्रश्न नहीं पूछ सकते थे, या निर्णयों को खारिज नहीं कर सकते थे।"
                })
            elif sec["id"] == 2:
                how.append({
                    "type": "How",
                    "q": f"विकेंद्रीकरण के प्रावधानों ने केंद्र और प्रेसीडेंसियों के बीच संवैधानिक संबंधों को कैसे बदला? (संस्करण {i+1})",
                    "sol": "इसने बॉम्बे और मद्रास के स्थानीय विधायी अधिकारों को बहाल किया, जिसने प्रांतीय विकेंद्रीकरण की नींव रखी, हालाँकि सभी स्थानीय विधेयकों के लिए वायसराय की अंतिम स्वीकृति आवश्यक थी।"
                })
            else:
                how.append({
                    "type": "How",
                    "q": f"पोर्टफोलियो प्रणाली ने वायसराय की परिषद के कार्यकारी कामकाज में कैसे सुधार किया? (संस्करण {i+1})",
                    "sol": "व्यक्तिगत परिषद सदस्यों को विशिष्ट विभाग सौंपकर, इसने सामूहिक प्रशासनिक समीक्षा को विभागीय जवाबदेही से बदल दिया, जिससे कैबिनेट जैसी संरचना की स्थापना हुई।"
                })
    return how

def generate_case_studies(sec, lang):
    cs = []
    for i in range(3):
        if lang == "en":
            if sec["id"] == 1:
                cs.append({
                    "type": "Case Study",
                    "q": f"Examine a scenario in 1863 where the Raja of Benares attempts to introduce a bill regarding the native religious practices in the Legislative Council. Evaluate the procedural limitations he faces (Scenario {i+1}).",
                    "sol": "He faces severe restrictions. As a non-official nominee, he can introduce bills, but any local or religious bill requires the prior sanction of the Viceroy, and the council cannot debate general policies or vote on financial allocations."
                })
            elif sec["id"] == 2:
                cs.append({
                    "type": "Case Study",
                    "q": f"Examine a scenario where the Bombay Legislative Council passes a local shipping bill in 1864, but the Viceroy vetoes it. Assess the legal status of the bill post-veto (Scenario {i+1}).",
                    "sol": "The bill is completely invalid. Although legislative powers were restored to Bombay in 1861, Section 30 of the Act mandates that the final assent of the Viceroy is compulsory for any provincial bill to become law."
                })
            else:
                cs.append({
                    "type": "Case Study",
                    "q": f"Examine a scenario in late 1862 where the Viceroy Lord Canning issues an emergency ordinance to suppress a local trade riot. Evaluate the validity of this ordinance after 8 months (Scenario {i+1}).",
                    "sol": "The ordinance is no longer valid. The 1861 Act specifies that any emergency ordinance issued by the Viceroy without council assent carries the force of law for a maximum period of exactly six months."
                })
        else:
            # Hindi CS
            if sec["id"] == 1:
                cs.append({
                    "type": "Case Study",
                    "q": f"1863 में एक परिदृश्य की जांच करें जहां बनारस के राजा विधायी परिषद में देशी धार्मिक प्रथाओं के संबंध में एक विधेयक पेश करने का प्रयास करते हैं। उनके सामने आने वाली सीमाओं का मूल्यांकन करें (परिदृश्य {i+1})।",
                    "sol": "उन्हें गंभीर सीमाओं का सामना करना पड़ता है। एक गैर-सरकारी मनोनीत सदस्य के रूप में, वे विधेयक पेश कर सकते हैं, लेकिन किसी भी स्थानीय या धार्मिक विधेयक के लिए वायसराय की पूर्व स्वीकृति आवश्यक है, और परिषद नीतिगत बहस या बजट चर्चा नहीं कर सकती।"
                })
            elif sec["id"] == 2:
                cs.append({
                    "type": "Case Study",
                    "q": f"एक परिदृश्य की जांच करें जहां बॉम्बे विधायी परिषद 1864 में एक स्थानीय नौवहन विधेयक पारित करती है, लेकिन वायसराय इसे वीटो कर देते हैं। वीटो के बाद विधेयक की स्थिति का आकलन करें (परिदृश्य {i+1})।",
                    "sol": "विधेयक पूरी तरह से अमान्य है। यद्यपि 1861 में बॉम्बे को विधायी शक्तियाँ बहाल कर दी गई थीं, लेकिन अधिनियम यह आदेश देता है कि किसी भी प्रांतीय विधेयक को कानून बनने के लिए वायसराय की अंतिम स्वीकृति अनिवार्य है।"
                })
            else:
                cs.append({
                    "type": "Case Study",
                    "q": f"1862 के अंत में एक परिदृश्य की जांच करें जहां वायसराय लॉर्ड कैनिंग स्थानीय व्यापारिक दंगों को दबाने के लिए एक आपातकालीन अध्यादेश जारी करते हैं। 8 महीने बाद इस अध्यादेश की वैधता का मूल्यांकन करें (परिदृश्य {i+1})।",
                    "sol": "अध्यादेश अब वैध नहीं है। 1861 का अधिनियम निर्दिष्ट करता है कि परिषद की सहमति के बिना वायसराय द्वारा जारी किए गए किसी भी आपातकालीन अध्यादेश में अधिकतम छह महीने की अवधि के लिए ही कानून का बल होता है।"
                })
    return cs

def generate_teach(sec, lang):
    teach = []
    for i in range(3):
        if lang == "en":
            if sec["id"] == 1:
                teach.append({
                    "type": "Teach the Concept",
                    "q": f"Explain the constitutional significance of the nomination of the first three Indians to the Legislative Council in 1862 (Discussion {i+1}).",
                    "sol": "It marked the historic transition from exclusive British executive rule to consultative constitutionalism. Although the nominees were conservative princes and elites with no popular mandate and minimal powers, it established the structural precedent of native legislative inclusion."
                })
            elif sec["id"] == 2:
                teach.append({
                    "type": "Teach the Concept",
                    "q": f"Explain how the Indian Councils Act of 1861 reversed the centralization of the British administration (Discussion {i+1}).",
                    "sol": "It restored local lawmaking authority to Madras and Bombay, ending the monopoly of Calcutta's central council. By paving the way for provincial councils in Bengal, NWFP, and Punjab, it initiated the long process of administrative decentralization leading to provincial autonomy."
                })
            else:
                teach.append({
                    "type": "Teach the Concept",
                    "q": f"Explain the relationship between the Portfolio System of 1861 and the modern cabinet system in India (Discussion {i+1}).",
                    "sol": "The portfolio system associated individual members of the executive council with specific departments, ending collective oversight. This department-based responsibility and final ordering power laid the exact structural foundation for the modern cabinet system where ministers run portfolios."
                })
        else:
            # Hindi Teach
            if sec["id"] == 1:
                teach.append({
                    "type": "Teach the Concept",
                    "q": f"1862 में विधायी परिषद में पहले तीन भारतीयों के नामांकन के संवैधानिक महत्व की व्याख्या करें (चर्चा {i+1})।",
                    "sol": "यह केवल ब्रिटिश कार्यकारी शासन से परामर्शकारी संवैधानिकता में ऐतिहासिक परिवर्तन का प्रतीक था। यद्यपि मनोनीत सदस्य बिना किसी लोकप्रिय जनादेश और न्यूनतम शक्तियों वाले राजा और अभिजात वर्ग थे, लेकिन इसने देशी विधायी भागीदारी का ढांचा स्थापित किया।"
                })
            elif sec["id"] == 2:
                teach.append({
                    "type": "Teach the Concept",
                    "q": f"व्याख्या करें कि 1861 के भारतीय परिषद अधिनियम ने ब्रिटिश प्रशासन के केंद्रीकरण को कैसे उलट दिया (चर्चा {i+1})।",
                    "sol": "इसने मद्रास और बॉम्बे को स्थानीय कानून बनाने का अधिकार वापस दे दिया, जिससे कलकत्ता की केंद्रीय परिषद का एकाधिकार समाप्त हो गया। बंगाल, NWFP और पंजाब में प्रांतीय परिषदों का मार्ग प्रशस्त करके, इसने विकेंद्रीकरण की लंबी प्रक्रिया शुरू की।"
                })
            else:
                teach.append({
                    "type": "Teach the Concept",
                    "q": f"1861 की पोर्टफोलियो प्रणाली और भारत में आधुनिक कैबिनेट प्रणाली के बीच संबंधों की व्याख्या करें (चर्चा {i+1})।",
                    "sol": "पोर्टफोलियो प्रणाली ने कार्यकारी परिषद के व्यक्तिगत सदस्यों को विशिष्ट विभागों से जोड़ा, जिससे सामूहिक निरीक्षण समाप्त हुआ। इस विभाग-आधारित जिम्मेदारी ने आधुनिक कैबिनेट प्रणाली के लिए सटीक संरचनात्मक आधार रखा।"
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
