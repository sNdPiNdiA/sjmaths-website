import os
import shutil

def create_environmental_impact_assessment_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "environment",
        "environmental-impact-assessment"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_EIA_Fundamentals": [
            "Meaning_of_EIA",
            "Objectives_of_EIA",
            "Principles_of_EIA",
            "Need_for_EIA",
            "Evolution_of_EIA",
            "Global_History_of_EIA",
            "Environmental_Decision_Making",
            "Sustainable_Development_Linkage"
        ],

        "02_EIA_Legal_and_Policy_Framework": [
            "Environment_Protection_Act_1986",
            "EIA_Notification_1994",
            "EIA_Notification_2006",
            "Subsequent_Amendments",
            "Legal_Basis_of_EIA",
            "Environmental_Clearance_Regime",
            "Regulatory_Authorities",
            "Compliance_Requirements"
        ],

        "03_EIA_Process_Overview": [
            "Screening",
            "Scoping",
            "Baseline_Data_Collection",
            "Impact_Prediction",
            "Impact_Evaluation",
            "Mitigation_Planning",
            "Decision_Making",
            "Post_Project_Monitoring"
        ],

        "04_Screening_in_EIA": [
            "Purpose_of_Screening",
            "Project_Categorization",
            "Category_A_Projects",
            "Category_B_Projects",
            "Threshold_Criteria",
            "Environmental_Sensitivity",
            "Screening_Methods",
            "Screening_Challenges"
        ],

        "05_Scoping_in_EIA": [
            "Purpose_of_Scoping",
            "Terms_of_Reference",
            "Key_Environmental_Issues",
            "Stakeholder_Inputs",
            "Alternative_Assessment",
            "Project_Boundaries",
            "Scoping_Methodologies",
            "Scoping_Challenges"
        ],

        "06_Baseline_Environmental_Studies": [
            "Physical_Environment_Data",
            "Biological_Environment_Data",
            "Socio_Economic_Data",
            "Land_Use_Assessment",
            "Water_Quality_Assessment",
            "Air_Quality_Assessment",
            "Noise_Level_Assessment",
            "Ecological_Surveys"
        ],

        "07_Impact_Identification": [
            "Direct_Impacts",
            "Indirect_Impacts",
            "Cumulative_Impacts",
            "Short_Term_Impacts",
            "Long_Term_Impacts",
            "Positive_Impacts",
            "Negative_Impacts",
            "Impact_Matrices"
        ],

        "08_Impact_Prediction_and_Assessment": [
            "Prediction_Methods",
            "Mathematical_Models",
            "Simulation_Techniques",
            "Risk_Assessment",
            "Significance_Evaluation",
            "Uncertainty_Analysis",
            "Environmental_Indicators",
            "Assessment_Methodologies"
        ],

        "09_Mitigation_Measures": [
            "Avoidance_Strategies",
            "Minimization_Strategies",
            "Restoration_Measures",
            "Compensation_Measures",
            "Pollution_Control_Measures",
            "Biodiversity_Protection",
            "Waste_Management_Plans",
            "Monitoring_Frameworks"
        ],

        "10_Environmental_Management_Plan": [
            "EMP_Concept",
            "Components_of_EMP",
            "Monitoring_Programme",
            "Compliance_Framework",
            "Emergency_Response_Plan",
            "Budgeting_for_EMP",
            "Reporting_Requirements",
            "Implementation_Mechanism"
        ],

        "11_Public_Consultation_and_Hearing": [
            "Public_Hearing_Process",
            "Stakeholder_Engagement",
            "Community_Participation",
            "Transparency_in_EIA",
            "Public_Objections",
            "Consultation_Methods",
            "Role_of_Local_Communities",
            "Challenges_in_Public_Hearings"
        ],

        "12_Environmental_Clearance": [
            "Environmental_Clearance_Process",
            "Expert_Appraisal_Committee",
            "State_Expert_Appraisal_Committee",
            "Appraisal_Criteria",
            "Conditional_Clearance",
            "Rejection_of_Projects",
            "Compliance_Conditions",
            "Validity_of_Clearance"
        ],

        "13_Post_Clearance_Monitoring": [
            "Compliance_Monitoring",
            "Environmental_Auditing",
            "Periodic_Reporting",
            "Monitoring_Indicators",
            "Third_Party_Audits",
            "Corrective_Actions",
            "Violation_Handling",
            "Performance_Evaluation"
        ],

        "14_Strategic_Environmental_Assessment": [
            "SEA_Concept",
            "SEA_vs_EIA",
            "Policy_Level_Assessment",
            "Programme_Assessment",
            "Regional_Assessment",
            "Decision_Support",
            "Advantages_of_SEA",
            "Global_Practices"
        ],

        "15_Cumulative_Impact_Assessment": [
            "Meaning_of_Cumulative_Impacts",
            "Spatial_Cumulative_Impacts",
            "Temporal_Cumulative_Impacts",
            "Regional_Impacts",
            "Assessment_Methods",
            "Threshold_Analysis",
            "Case_Studies",
            "Policy_Relevance"
        ],

        "16_Sector_Specific_EIA": [
            "Mining_Projects",
            "Thermal_Power_Projects",
            "Hydropower_Projects",
            "Industrial_Projects",
            "Infrastructure_Projects",
            "Highway_Projects",
            "Ports_and_Harbours",
            "Urban_Development_Projects"
        ],

        "17_Ecological_and_Social_Impact_Assessment": [
            "Biodiversity_Impact_Assessment",
            "Wildlife_Impact_Assessment",
            "Forest_Impact_Assessment",
            "Social_Impact_Assessment",
            "Livelihood_Impacts",
            "Displacement_and_Resettlement",
            "Indigenous_Communities",
            "Gender_Considerations"
        ],

        "18_EIA_Tools_and_Techniques": [
            "Checklist_Method",
            "Matrix_Method",
            "Network_Method",
            "Overlay_Method",
            "GIS_in_EIA",
            "Remote_Sensing",
            "Environmental_Modeling",
            "Decision_Support_Systems"
        ],

        "19_Challenges_and_Criticism_of_EIA": [
            "Data_Limitations",
            "Weak_Enforcement",
            "Conflict_of_Interest",
            "Quality_of_EIA_Reports",
            "Public_Participation_Issues",
            "Monitoring_Gaps",
            "Project_Delays",
            "Suggested_Reforms"
        ],

        "20_Current_Affairs_and_EIA_Developments": [
            "Recent_EIA_Amendments",
            "Draft_EIA_Notifications",
            "Landmark_Court_Judgements",
            "NGT_Decisions",
            "Environmental_Clearance_Controversies",
            "Government_Reforms",
            "International_Best_Practices",
            "UPSC_High_Yield_Topics"
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

    print(f"Creating Environmental Impact Assessment structure in: {target_base}")

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
    create_environmental_impact_assessment_structure()