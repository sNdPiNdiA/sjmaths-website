import os
import shutil

def create_inflation_and_business_cycle_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "macro-economics",
        "inflation-and-business-cycle"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Inflation_Fundamentals": [
            "Meaning_of_Inflation",
            "Inflation_Characteristics",
            "Price_Level_Changes",
            "Inflationary_Process",
            "Inflation_Measurement",
            "Inflation_Indicators",
            "Economic_Importance",
            "Historical_Perspective"
        ],

        "02_Types_of_Inflation": [
            "Creeping_Inflation",
            "Walking_Inflation",
            "Running_Inflation",
            "Hyperinflation",
            "Open_Inflation",
            "Suppressed_Inflation",
            "Balanced_Inflation",
            "Unbalanced_Inflation"
        ],

        "03_Demand_Pull_Inflation": [
            "Excess_Demand",
            "Aggregate_Demand_Expansion",
            "Consumption_Boom",
            "Investment_Surge",
            "Government_Spending_Impact",
            "Demand_Pressures",
            "Output_Gap",
            "Policy_Responses"
        ],

        "04_Cost_Push_Inflation": [
            "Rising_Input_Costs",
            "Wage_Push_Inflation",
            "Energy_Price_Shocks",
            "Raw_Material_Costs",
            "Imported_Inflation",
            "Supply_Side_Pressures",
            "Cost_Escalation",
            "Inflationary_Impact"
        ],

        "05_Structural_Inflation": [
            "Supply_Bottlenecks",
            "Infrastructure_Constraints",
            "Agricultural_Rigidities",
            "Market_Inefficiencies",
            "Developmental_Factors",
            "Structural_Imbalances",
            "Long_Term_Pressures",
            "Policy_Challenges"
        ],

        "06_Inflation_Indices": [
            "Consumer_Price_Index",
            "Wholesale_Price_Index",
            "GDP_Deflator",
            "Core_Inflation",
            "Headline_Inflation",
            "Inflation_Basket",
            "Index_Construction",
            "Comparative_Analysis"
        ],

        "07_CPI_in_India": [
            "CPI_Combined",
            "Rural_CPI",
            "Urban_CPI",
            "Weight_Assignment",
            "Consumption_Basket",
            "Inflation_Targeting_Linkage",
            "Data_Collection",
            "Policy_Importance"
        ],

        "08_WPI_in_India": [
            "WPI_Components",
            "Primary_Articles",
            "Fuel_and_Power",
            "Manufactured_Products",
            "Wholesale_Prices",
            "Index_Methodology",
            "Historical_Importance",
            "Current_Relevance"
        ],

        "09_Core_and_Headline_Inflation": [
            "Core_Inflation_Concept",
            "Food_Exclusion",
            "Fuel_Exclusion",
            "Headline_Inflation_Concept",
            "Volatility_Analysis",
            "Underlying_Price_Trends",
            "Policy_Interpretation",
            "Economic_Significance"
        ],

        "10_Inflation_and_Growth": [
            "Growth_Inflation_Tradeoff",
            "Investment_Decisions",
            "Savings_Behaviour",
            "Consumption_Patterns",
            "Business_Confidence",
            "Economic_Expansion",
            "Growth_Constraints",
            "Long_Term_Implications"
        ],

        "11_Inflation_and_Income_Distribution": [
            "Fixed_Income_Groups",
            "Wage_Earners",
            "Borrowers_and_Lenders",
            "Wealth_Redistribution",
            "Purchasing_Power",
            "Social_Impact",
            "Income_Inequality",
            "Vulnerable_Groups"
        ],

        "12_Inflation_Expectations": [
            "Adaptive_Expectations",
            "Rational_Expectations",
            "Consumer_Expectations",
            "Business_Expectations",
            "Expectation_Formation",
            "Inflation_Persistence",
            "Confidence_Effects",
            "Policy_Communication"
        ],

        "13_Stagflation": [
            "Stagflation_Concept",
            "High_Inflation",
            "Low_Growth",
            "High_Unemployment",
            "Supply_Shocks",
            "Policy_Dilemmas",
            "Historical_Examples",
            "Modern_Relevance"
        ],

        "14_Disinflation_and_Deflation": [
            "Disinflation",
            "Deflation",
            "Negative_Inflation",
            "Price_Decline",
            "Demand_Contraction",
            "Debt_Deflation",
            "Economic_Consequences",
            "Policy_Measures"
        ],

        "15_Inflation_Control_Measures": [
            "Demand_Management",
            "Supply_Management",
            "Price_Stabilization",
            "Market_Interventions",
            "Administrative_Measures",
            "Anti_Inflation_Strategy",
            "Policy_Mix",
            "Effectiveness"
        ],

        "16_Business_Cycle_Fundamentals": [
            "Business_Cycle_Concept",
            "Economic_Fluctuations",
            "Cyclical_Movements",
            "Aggregate_Activity",
            "Economic_Variability",
            "Cycle_Characteristics",
            "Periodic_Movements",
            "Economic_Dynamics"
        ],

        "17_Phases_of_Business_Cycle": [
            "Expansion",
            "Peak",
            "Contraction",
            "Trough",
            "Recovery",
            "Turning_Points",
            "Cycle_Transitions",
            "Economic_Indicators"
        ],

        "18_Theories_of_Business_Cycles": [
            "Monetary_Theory",
            "Innovation_Theory",
            "Psychological_Theory",
            "Multiplier_Accelerator_Theory",
            "Keynesian_Approach",
            "Real_Business_Cycle",
            "Overinvestment_Theory",
            "Modern_Explanations"
        ],

        "19_Leading_Lagging_and_Coincident_Indicators": [
            "Leading_Indicators",
            "Lagging_Indicators",
            "Coincident_Indicators",
            "Economic_Forecasting",
            "Indicator_Analysis",
            "Trend_Identification",
            "Cycle_Prediction",
            "Data_Interpretation"
        ],

        "20_Recession_and_Depression": [
            "Recession",
            "Technical_Recession",
            "Economic_Slowdown",
            "Depression",
            "Output_Decline",
            "Employment_Losses",
            "Historical_Cases",
            "Recovery_Policies"
        ],

        "21_Boom_and_Overheating": [
            "Economic_Boom",
            "Asset_Bubbles",
            "Credit_Expansion",
            "Speculative_Activity",
            "Overheating_Economy",
            "Demand_Surge",
            "Market_Euphoria",
            "Correction_Risks"
        ],

        "22_Output_Gap": [
            "Potential_Output",
            "Actual_Output",
            "Positive_Output_Gap",
            "Negative_Output_Gap",
            "Capacity_Utilization",
            "Economic_Slack",
            "Growth_Assessment",
            "Policy_Relevance"
        ],

        "23_Phillips_Curve": [
            "Inflation_Unemployment_Tradeoff",
            "Short_Run_Phillips_Curve",
            "Long_Run_Phillips_Curve",
            "Natural_Rate",
            "NAIRU",
            "Expectations_Augmentation",
            "Policy_Debates",
            "Modern_Interpretation"
        ],

        "24_Inflation_in_India": [
            "Food_Inflation",
            "Fuel_Inflation",
            "Imported_Inflation",
            "Rural_Inflation",
            "Urban_Inflation",
            "Inflation_Trends",
            "Structural_Factors",
            "Policy_Challenges"
        ],

        "25_Business_Cycles_in_India": [
            "Growth_Fluctuations",
            "Investment_Cycles",
            "Industrial_Cycles",
            "Consumption_Cycles",
            "External_Shocks",
            "Economic_Resilience",
            "Historical_Experience",
            "Recent_Trends"
        ],

        "26_Global_Inflation_and_Cycles": [
            "Global_Inflation_Trends",
            "Commodity_Price_Cycles",
            "Oil_Shocks",
            "Financial_Crises",
            "Global_Recessions",
            "Pandemic_Impact",
            "International_Linkages",
            "Spillover_Effects"
        ],

        "27_Current_Affairs_and_Macroeconomic_Trends": [
            "Latest_CPI_Data",
            "Latest_WPI_Data",
            "Inflation_Trends",
            "Growth_Projections",
            "Business_Cycle_Indicators",
            "Economic_Survey_Findings",
            "Recent_Developments",
            "UPSC_High_Yield_Topics"
        ],

        "28_Reports_Data_and_Exam_Themes": [
            "Inflation_Statistics",
            "CPI_Reports",
            "WPI_Reports",
            "Growth_Data",
            "Economic_Survey_Macroeconomics",
            "Government_Publications",
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

    print(f"Creating Inflation and Business Cycle structure in: {target_base}")

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
    create_inflation_and_business_cycle_structure()