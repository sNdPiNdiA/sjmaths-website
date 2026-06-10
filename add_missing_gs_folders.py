import os

directories = [
    # Environment
    "gs-question-bank/environment/ecology-and-ecosystems",
    "gs-question-bank/environment/biodiversity-and-conservation",
    "gs-question-bank/environment/climate-change",
    "gs-question-bank/environment/environmental-pollution",
    "gs-question-bank/environment/environmental-impact-assessment",
    "gs-question-bank/environment/national-laws-and-policies",
    "gs-question-bank/environment/international-conventions-and-treaties",
    
    # Science & Tech (Distinct from General Science)
    "gs-question-bank/science-and-tech/space-technology",
    "gs-question-bank/science-and-tech/defense-technology",
    "gs-question-bank/science-and-tech/biotechnology",
    "gs-question-bank/science-and-tech/information-and-communication-technology",
    "gs-question-bank/science-and-tech/nanotechnology",
    "gs-question-bank/science-and-tech/nuclear-technology",
    "gs-question-bank/science-and-tech/robotics-and-ai",
    "gs-question-bank/science-and-tech/health-and-diseases-tech",
    "gs-question-bank/science-and-tech/intellectual-property-rights",

    # Ethics (Crucial for UPSC GS 4)
    "gs-question-bank/ethics/ethics-and-human-interface",
    "gs-question-bank/ethics/attitude-and-aptitude",
    "gs-question-bank/ethics/emotional-intelligence",
    "gs-question-bank/ethics/contributions-of-moral-thinkers",
    "gs-question-bank/ethics/public-service-values-and-probity",
    "gs-question-bank/ethics/case-studies",

    # International Relations
    "gs-question-bank/international-relations/india-and-its-neighborhood",
    "gs-question-bank/international-relations/bilateral-regional-global-groupings",
    "gs-question-bank/international-relations/policies-of-developed-and-developing-countries",
    "gs-question-bank/international-relations/important-international-institutions",
    "gs-question-bank/international-relations/indian-diaspora"
]

for d in directories:
    os.makedirs(d, exist_ok=True)

print(f"Successfully added {len(directories)} missing sub-folders.")
