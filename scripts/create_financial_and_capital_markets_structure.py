import os
import shutil

def create_financial_and_capital_markets_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "indian-economy",
        "financial-and-capital-markets"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Financial_System_Fundamentals": [
            "Meaning_of_Financial_System",
            "Financial_Assets",
            "Financial_Institutions",
            "Financial_Markets",
            "Financial_Services",
            "Role_in_Economy",
            "Financial_Intermediation",
            "Structure_of_Financial_System"
        ],

        "02_Financial_Markets_Overview": [
            "Money_Market",
            "Capital_Market",
            "Primary_Market",
            "Secondary_Market",
            "Debt_Market",
            "Equity_Market",
            "Commodity_Market",
            "Market_Linkages"
        ],

        "03_Money_Market": [
            "Call_Money_Market",
            "Notice_Money_Market",
            "Treasury_Bills",
            "Commercial_Papers",
            "Certificates_of_Deposit",
            "Repo_Market",
            "Money_Market_Mutual_Funds",
            "Liquidity_Management"
        ],

        "04_Capital_Market": [
            "Long_Term_Finance",
            "Capital_Formation",
            "Market_Participants",
            "Capital_Mobilization",
            "Investment_Channels",
            "Market_Development",
            "Resource_Allocation",
            "Economic_Significance"
        ],

        "05_Primary_Market": [
            "Initial_Public_Offer",
            "Follow_On_Public_Offer",
            "Rights_Issue",
            "Bonus_Issue",
            "Private_Placement",
            "Book_Building",
            "Issue_Pricing",
            "Prospectus"
        ],

        "06_Secondary_Market": [
            "Stock_Trading",
            "Market_Liquidity",
            "Price_Discovery",
            "Trading_Platforms",
            "Settlement_Process",
            "Market_Efficiency",
            "Investor_Participation",
            "Trading_Mechanism"
        ],

        "07_Stock_Exchanges": [
            "BSE",
            "NSE",
            "Stock_Exchange_Functions",
            "Listing_Requirements",
            "Market_Infrastructure",
            "Trading_Systems",
            "Clearing_Corporations",
            "Market_Development"
        ],

        "08_SEBI": [
            "SEBI_Establishment",
            "Regulatory_Powers",
            "Investor_Protection",
            "Market_Regulation",
            "Disclosure_Norms",
            "Enforcement_Actions",
            "Market_Surveillance",
            "Institutional_Framework"
        ],

        "09_Equity_Market": [
            "Equity_Shares",
            "Shareholders",
            "Voting_Rights",
            "Market_Capitalization",
            "Growth_Investing",
            "Value_Investing",
            "Dividend_Income",
            "Equity_Risk"
        ],

        "10_Debt_Market": [
            "Government_Securities",
            "Corporate_Bonds",
            "Municipal_Bonds",
            "Debt_Instruments",
            "Bond_Yields",
            "Credit_Ratings",
            "Fixed_Income_Market",
            "Debt_Trading"
        ],

        "11_Government_Securities_Market": [
            "G_Secs",
            "Treasury_Bills",
            "SDLs",
            "Yield_Curve",
            "Primary_Dealers",
            "Sovereign_Debt",
            "Borrowing_Programme",
            "Market_Development"
        ],

        "12_Mutual_Funds": [
            "Mutual_Fund_Concept",
            "Equity_Funds",
            "Debt_Funds",
            "Hybrid_Funds",
            "Index_Funds",
            "ETF",
            "SIP",
            "Fund_Management"
        ],

        "13_Insurance_Market": [
            "Life_Insurance",
            "General_Insurance",
            "Health_Insurance",
            "IRDAI",
            "Insurance_Penetration",
            "Insurance_Density",
            "Risk_Coverage",
            "Market_Development"
        ],

        "14_Pension_and_Retirement_Markets": [
            "NPS",
            "PFRDA",
            "Retirement_Planning",
            "Pension_Funds",
            "Annuities",
            "Long_Term_Savings",
            "Pension_Reforms",
            "Coverage_Expansion"
        ],

        "15_Derivatives_Market": [
            "Futures",
            "Options",
            "Forwards",
            "Swaps",
            "Hedging",
            "Speculation",
            "Risk_Management",
            "Derivative_Trading"
        ],

        "16_Foreign_Exchange_Market": [
            "Forex_Market",
            "Exchange_Rates",
            "Currency_Trading",
            "Forex_Derivatives",
            "Market_Participants",
            "Currency_Risk",
            "Forex_Regulation",
            "Market_Dynamics"
        ],

        "17_Foreign_Portfolio_Investment": [
            "FPI",
            "Foreign_Investors",
            "Capital_Flows",
            "Market_Impact",
            "Regulatory_Framework",
            "Investment_Limits",
            "Volatility",
            "Policy_Reforms"
        ],

        "18_Venture_Capital_and_Private_Equity": [
            "Venture_Capital",
            "Private_Equity",
            "Startup_Funding",
            "Angel_Investors",
            "Growth_Capital",
            "Exit_Strategies",
            "Innovation_Finance",
            "Investment_Ecosystem"
        ],

        "19_Credit_Rating_Agencies": [
            "Credit_Ratings",
            "CRISIL",
            "ICRA",
            "CARE_Ratings",
            "Rating_Methodology",
            "Debt_Assessment",
            "Investor_Confidence",
            "Regulatory_Framework"
        ],

        "20_Depositories_and_Custodians": [
            "NSDL",
            "CDSL",
            "Demat_Accounts",
            "Electronic_Holdings",
            "Custodian_Services",
            "Settlement_System",
            "Investor_Convenience",
            "Market_Efficiency"
        ],

        "21_Investment_Banking": [
            "Merchant_Banking",
            "Issue_Management",
            "Underwriting",
            "Corporate_Advisory",
            "Mergers_and_Acquisitions",
            "Capital_Raising",
            "Financial_Advisory",
            "Market_Intermediation"
        ],

        "22_Financial_Inclusion_and_Markets": [
            "Retail_Investors",
            "Financial_Awareness",
            "Investor_Education",
            "Inclusive_Investing",
            "Digital_Investment_Platforms",
            "Market_Access",
            "Small_Investors",
            "Inclusion_Strategies"
        ],

        "23_FinTech_and_Digital_Finance": [
            "FinTech",
            "Robo_Advisory",
            "Digital_Brokerage",
            "Online_Investing",
            "Blockchain_in_Finance",
            "WealthTech",
            "RegTech",
            "Innovation_Trends"
        ],

        "24_Market_Risks_and_Investor_Protection": [
            "Market_Risk",
            "Credit_Risk",
            "Liquidity_Risk",
            "Operational_Risk",
            "Investor_Grievances",
            "Fraud_Prevention",
            "Risk_Disclosure",
            "Protection_Mechanisms"
        ],

        "25_Financial_Stability_and_Markets": [
            "Systemic_Risk",
            "Market_Volatility",
            "Financial_Contagion",
            "Macroprudential_Policies",
            "Crisis_Management",
            "Market_Resilience",
            "Regulatory_Coordination",
            "Stability_Framework"
        ],

        "26_Financial_Sector_Reforms": [
            "Market_Reforms",
            "SEBI_Reforms",
            "Corporate_Bond_Market",
            "Ease_of_Investing",
            "Financial_Liberalization",
            "Institutional_Changes",
            "Committee_Recommendations",
            "Future_Reforms"
        ],

        "27_Current_Affairs_and_Market_Issues": [
            "IPO_Trends",
            "Stock_Market_Performance",
            "Bond_Market_Developments",
            "SEBI_Updates",
            "FinTech_Regulations",
            "Global_Market_Events",
            "Investment_Trends",
            "UPSC_High_Yield_Topics"
        ],

        "28_Reports_Data_and_Exam_Themes": [
            "Market_Indices",
            "Capital_Market_Data",
            "Investment_Trends",
            "SEBI_Reports",
            "Financial_Statistics",
            "Market_Indicators",
            "PYQ_Themes",
            "Assertion_Reason_Topics"
        ]
    }

    leaf_files = [
        "facts.json", "one_liner.json", "mcq_easy.json", "mcq_medium.json",
        "mcq_hard.json", "multiple_statement.json", "assertion_reason.json",
        "match_following.json", "fill_blanks.json", "true_false.json",
        "chronology.json", "arrange_sequence.json", "pair_matching.json",
        "odd_one_out.json", "map_based.json", "source_based.json",
        "passage_based.json", "case_study.json", "short_answer.json",
        "long_answer.json", "mains_10m.json", "mains_15m.json",
        "mains_20m.json", "pyq_upsc.json", "pyq_ssc.json",
        "pyq_railway.json", "pyq_state_pcs.json", "pyq_teaching.json",
        "interview.json", "flashcards.json", "revision_questions.json",
        "concept_traps.json", "common_mistakes.json", "memory_hooks.json"
    ]

    print(f"Creating Financial and Capital Markets structure in: {target_base}")

    for category, topics in structure.items():
        category_path = os.path.join(target_base, category)
        os.makedirs(category_path, exist_ok=True)

        for topic in topics:
            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)

            for filename in leaf_files:
                file_path = os.path.join(topic_path, filename)

                if not os.path.exists(file_path):
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write("[]")

if __name__ == "__main__":
    create_financial_and_capital_markets_structure()