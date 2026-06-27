#!/usr/bin/env python3
"""
Injects interactive mindmap into ALL Prehistory topic index pages (EN + HI).
Uses shared assets/css/mindmap.min.css and assets/js/mindmap-engine.min.js.
Only the unique tree data is embedded inline per page.
"""

import os
import re
import json

BASE = r"upsc/ancient_history/Prehistory"

# ── ENGLISH TREE DATA ──────────────────────────────────────────

TREE_GEO = {
    "label": "Geographical\nDistribution",
    "type": "root",
    "children": [
        {
            "label": "Lower Paleo\nDistribution",
            "date": "2 MYA \u2013 100k BCE",
            "type": "branch",
            "children": [
                {"label": "Soan Valley & NW:\nPebble choppers, Soanian", "type": "sub", "date": "2 MYA onward",
                 "children": [
                     {"label": "Soan River:\nQuartzite pebble tools", "type": "leaf"},
                     {"label": "Potwar Plateau:\nGlacial/interglacial", "type": "leaf"}
                 ]},
                {"label": "Peninsular India:\nAcheulian handaxes", "type": "sub", "date": "1.5 MYA \u2013 100k BCE",
                 "children": [
                     {"label": "Attirampakkam:\n1.5 MYA, cosmic dating", "type": "leaf"},
                     {"label": "Hunsgi (KA):\nLimestone tool factory", "type": "leaf"},
                     {"label": "Bhimbetka (MP):\n700+ rock shelters", "type": "leaf"},
                     {"label": "Didwana (RJ):\n16R dune profile", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Middle & Upper\nPaleo Distribution",
            "date": "100k \u2013 10k BCE",
            "type": "branch",
            "children": [
                {"label": "River Valleys", "type": "sub", "date": "100k \u2013 40k BCE",
                 "children": [
                     {"label": "Narmada Valley:\nHathnora fossil skull", "type": "leaf"},
                     {"label": "Luni Valley (RJ):\nLuni Industry, chert scrapers", "type": "leaf"},
                     {"label": "Belan Valley (UP):\nContinuous sequence", "type": "leaf"}
                 ]},
                {"label": "Artistic Expressions", "type": "sub", "date": "40k \u2013 10k BCE",
                 "children": [
                     {"label": "Patne (MH):\nOstrich eggshell beads", "type": "leaf"},
                     {"label": "Kurnool Caves (AP):\nBone tools & ash", "type": "leaf"},
                     {"label": "Renigunta (AP):\nBlade tool industry", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Mesolithic\nDistribution",
            "date": "10k \u2013 4k BCE",
            "type": "branch",
            "children": [
                {"label": "Desert & Dune Sites", "type": "sub", "date": "10k \u2013 8k BCE",
                 "children": [
                     {"label": "Bagor (RJ):\nLargest site, domestication", "type": "leaf"},
                     {"label": "Langhnaj (GJ):\nDune dwelling, burials", "type": "leaf"},
                     {"label": "Teri Sites (TN):\nRed sand dune microliths", "type": "leaf"}
                 ]},
                {"label": "Gangetic & Central", "type": "sub", "date": "8k \u2013 4k BCE",
                 "children": [
                     {"label": "Sarai Nahar Rai (UP):\nLake settlement", "type": "leaf"},
                     {"label": "Bhimbetka (MP):\nMesolithic rock art", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Neolithic &\nChalcolithic Zones",
            "date": "7k \u2013 1k BCE",
            "type": "branch",
            "children": [
                {"label": "Northern Neolithic", "type": "sub", "date": "7k \u2013 3k BCE",
                 "children": [
                     {"label": "Mehrgarh (Balochistan):\n~7000 BCE, farming", "type": "leaf"},
                     {"label": "Burzahom (J&K):\nPit dwellings, Karewas", "type": "leaf"},
                     {"label": "Chirand (Bihar):\nBone tool assemblage", "type": "leaf"}
                 ]},
                {"label": "Chalcolithic Cultures", "type": "sub", "date": "2k \u2013 700 BCE",
                 "children": [
                     {"label": "Kayatha (MP):\nEarliest Chalcolithic", "type": "leaf"},
                     {"label": "Ahar-Banas (RJ):\nBlack & Red Ware", "type": "leaf"},
                     {"label": "Malwa (MP):\nPainted orange-slip", "type": "leaf"},
                     {"label": "Jorwe (MH):\nInamgaon, Daimabad", "type": "leaf"}
                 ]},
                {"label": "NE & E. India", "type": "sub", "date": "3k \u2013 1k BCE",
                 "children": [
                     {"label": "Daojali Hading (AS):\nJade celts, corded pottery", "type": "leaf"},
                     {"label": "Ash Mounds (KA):\nUtnur, Kupgal", "type": "leaf"}
                 ]}
            ]
        }
    ]
}

TREE_PALEO = {
    "label": "Paleolithic / Old\nStone Age",
    "type": "root",
    "children": [
        {
            "label": "Lower\nPaleolithic",
            "date": "2.6 MYA \u2013 100k BCE",
            "type": "branch",
            "children": [
                {"label": "Soanian Culture\n(NW India)", "type": "sub", "date": "2 MYA \u2013 100k BCE",
                 "children": [
                     {"label": "Pebble choppers &\nchopping tools", "type": "leaf"},
                     {"label": "Soan Valley &\nPotwar Plateau", "type": "leaf"}
                 ]},
                {"label": "Madrasian /\nAcheulian", "type": "sub", "date": "1.5 MYA \u2013 100k BCE",
                 "children": [
                     {"label": "Handaxes, cleavers,\nbifacial tools", "type": "leaf"},
                     {"label": "Attirampakkam:\nOldest Acheulian in India", "type": "leaf"},
                     {"label": "Bhimbetka:\nRock shelters, quartzite", "type": "leaf"}
                 ]},
                {"label": "Key Acheulian\nSites", "type": "sub", "date": "1.5 MYA \u2013 100k BCE",
                 "children": [
                     {"label": "Hunsgi (KA):\nLimestone handaxes", "type": "leaf"},
                     {"label": "Chirki-Nevasa (MH):\nFactory site", "type": "leaf"},
                     {"label": "Didwana (RJ):\n16R sand dune", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Middle\nPaleolithic",
            "date": "100k \u2013 40k BCE",
            "type": "branch",
            "children": [
                {"label": "Tool\nTechnology", "type": "sub", "date": "100k \u2013 40k BCE",
                 "children": [
                     {"label": "Scrapers, points,\nborers", "type": "leaf"},
                     {"label": "Chert, jasper,\nchalcedony", "type": "leaf"},
                     {"label": "Smaller flakes than\nLower Paleo", "type": "leaf"}
                 ]},
                {"label": "Major\nSites", "type": "sub", "date": "100k \u2013 40k BCE",
                 "children": [
                     {"label": "Nevasan Industry:\nPravara River, MH", "type": "leaf"},
                     {"label": "Luni Valley (RJ):\nLuni Industry", "type": "leaf"},
                     {"label": "Belan Valley (UP):\nContinuous sequence", "type": "leaf"}
                 ]},
                {"label": "Environmental\nContext", "type": "sub", "date": "100k \u2013 40k BCE",
                 "children": [
                     {"label": "Arid & semi-arid\nclimate", "type": "leaf"},
                     {"label": "Toba eruption\n~74k year marker", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Upper\nPaleolithic",
            "date": "40k \u2013 10k BCE",
            "type": "branch",
            "children": [
                {"label": "Cultural\nAdvances", "type": "sub", "date": "40k \u2013 10k BCE",
                 "children": [
                     {"label": "Homo sapiens\nemergence", "type": "leaf"},
                     {"label": "Blades, burins,\nbone tools", "type": "leaf"},
                     {"label": "Ostrich eggshell\nbeads at Patne", "type": "leaf"}
                 ]},
                {"label": "Rock Art\n& Sites", "type": "sub", "date": "40k \u2013 10k BCE",
                 "children": [
                     {"label": "Bhimbetka:\nUpper Paleo paintings", "type": "leaf"},
                     {"label": "Kurnool Caves:\nAsh & bone fossils", "type": "leaf"},
                     {"label": "Peak Ice Age:\nDry & arid climate", "type": "leaf"}
                 ]}
            ]
        }
    ]
}

TREE_MESO = {
    "label": "Mesolithic / Middle\nStone Age",
    "type": "root",
    "children": [
        {
            "label": "Holocene\nContext",
            "date": "~10,000 BCE onward",
            "type": "branch",
            "children": [
                {"label": "Climate\nTransition", "type": "sub", "date": "10k \u2013 8k BCE",
                 "children": [
                     {"label": "End of Ice Age:\nWarmer & wetter", "type": "leaf"},
                     {"label": "Forest expansion,\nmonsoon stabilization", "type": "leaf"},
                     {"label": "Smaller, faster\nanimals emerged", "type": "leaf"}
                 ]},
                {"label": "Environmental\nImpact", "type": "sub", "date": "10k \u2013 8k BCE",
                 "children": [
                     {"label": "Shift to microlithic\ntools", "type": "leaf"},
                     {"label": "Incipient animal\ndomestication", "type": "leaf"},
                     {"label": "Semi-permanent\nsettlements", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Microliths\n& Tools",
            "date": "10k \u2013 8k BCE",
            "type": "branch",
            "children": [
                {"label": "Geometric\nTypes", "type": "sub", "date": "10k \u2013 8k BCE",
                 "children": [
                     {"label": "Lunates,\ntriangles, trapezes", "type": "leaf"},
                     {"label": "Size 1\u20135 cm:\nComposite tools", "type": "leaf"}
                 ]},
                {"label": "Non-Geometric\nTypes", "type": "sub", "date": "10k \u2013 8k BCE",
                 "children": [
                     {"label": "Backed blades,\nborers, points", "type": "leaf"},
                     {"label": "Microburin\ntechnique", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Key\nSites",
            "date": "10k \u2013 4k BCE",
            "type": "branch",
            "children": [
                {"label": "North & West\nIndia", "type": "sub", "date": "10k \u2013 8k BCE",
                 "children": [
                     {"label": "Bagor (RJ):\nLargest site", "type": "leaf"},
                     {"label": "Langhnaj (GJ):\nFlexed burials", "type": "leaf"},
                     {"label": "Tilwara (RJ):\nLuni basin dunes", "type": "leaf"}
                 ]},
                {"label": "Central & East\nIndia", "type": "sub", "date": "10k \u2013 8k BCE",
                 "children": [
                     {"label": "Bhimbetka (MP):\nRock art masterpieces", "type": "leaf"},
                     {"label": "Adamgarh (MP):\nEarliest domestication", "type": "leaf"},
                     {"label": "Sarai Nahar Rai (UP):\nGangetic lake site", "type": "leaf"}
                 ]},
                {"label": "Southern\nIndia", "type": "sub", "date": "10k \u2013 8k BCE",
                 "children": [
                     {"label": "Teri Sites (TN):\nRed coastal dunes", "type": "leaf"},
                     {"label": "Birbhanpur (WB):\nMicrolith industry", "type": "leaf"}
                 ]}
            ]
        }
    ]
}

TREE_NEO = {
    "label": "Neolithic / New\nStone Age",
    "type": "root",
    "children": [
        {
            "label": "Neolithic\nRevolution",
            "date": "8k \u2013 2k BCE",
            "type": "branch",
            "children": [
                {"label": "Economic\nTransformation", "type": "sub", "date": "8k \u2013 3k BCE",
                 "children": [
                     {"label": "Food-gathering to\nfood-producing", "type": "leaf"},
                     {"label": "Wheat, barley &\nrice cultivation", "type": "leaf"},
                     {"label": "Settled village life,\npottery making", "type": "leaf"}
                 ]},
                {"label": "Key\nInnovations", "type": "sub", "date": "8k \u2013 3k BCE",
                 "children": [
                     {"label": "Wheel-made\npottery", "type": "leaf"},
                     {"label": "Animal\ndomestication", "type": "leaf"},
                     {"label": "Mud-brick\narchitecture", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Polished Stone\nTools",
            "date": "8k \u2013 2k BCE",
            "type": "branch",
            "children": [
                {"label": "Ground &\nPolished Tools", "type": "sub", "date": "8k \u2013 2k BCE",
                 "children": [
                     {"label": "Celts, axes,\nadzes", "type": "leaf"},
                     {"label": "Saddle querns &\ngrinding stones", "type": "leaf"},
                     {"label": "Mace heads &\nring stones", "type": "leaf"}
                 ]},
                {"label": "Bone &\nOther Tools", "type": "sub", "date": "8k \u2013 2k BCE",
                 "children": [
                     {"label": "Bone needles,\nharpoons (Burzahom)", "type": "leaf"},
                     {"label": "Antler picks\n(Chirand)", "type": "leaf"},
                     {"label": "Jade celts\n(Daojali Hading)", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Regional\nCultures",
            "date": "8k \u2013 2k BCE",
            "type": "branch",
            "children": [
                {"label": "North & NW\nIndia", "type": "sub", "date": "7k \u2013 3k BCE",
                 "children": [
                     {"label": "Mehrgarh:\n~7000 BCE, earliest", "type": "leaf"},
                     {"label": "Burzahom:\nPit dwellings, J&K", "type": "leaf"},
                     {"label": "Gufkral:\nCave + settlement", "type": "leaf"}
                 ]},
                {"label": "Gangetic\nPlain", "type": "sub", "date": "6k \u2013 2k BCE",
                 "children": [
                     {"label": "Lahuradewa:\nEarliest rice ~8000 BCE", "type": "leaf"},
                     {"label": "Koldihwa:\nCord-impressed pottery", "type": "leaf"},
                     {"label": "Chirand:\nExtensive bone tools", "type": "leaf"}
                 ]},
                {"label": "South & NE\nIndia", "type": "sub", "date": "3k \u2013 1k BCE",
                 "children": [
                     {"label": "Ash Mounds:\nUtnur, Kupgal (KA)", "type": "leaf"},
                     {"label": "Daojali Hading:\nJade celts (Assam)", "type": "leaf"},
                     {"label": "Piklihal:\nCattle herders", "type": "leaf"}
                 ]}
            ]
        }
    ]
}

TREE_CHALCO = {
    "label": "Chalcolithic\n(Copper-Stone) Age",
    "type": "root",
    "children": [
        {
            "label": "Regional\nCultures",
            "date": "2,000 \u2013 700 BCE",
            "type": "branch",
            "children": [
                {"label": "Kayatha\nCulture (MP)", "type": "sub", "date": "~2000 BCE",
                 "children": [
                     {"label": "Earliest Chalcolithic\nin India", "type": "leaf"},
                     {"label": "White-painted\nblack & red ware", "type": "leaf"},
                     {"label": "Copper tools &\nstone blades", "type": "leaf"}
                 ]},
                {"label": "Malwa\nCulture (MP)", "type": "sub", "date": "1700 \u2013 1200 BCE",
                 "children": [
                     {"label": "Painted orange-\nslip ware", "type": "leaf"},
                     {"label": "Navdatoli,\nMaheshwar sites", "type": "leaf"},
                     {"label": "Wheat, barley &\npulses farming", "type": "leaf"}
                 ]},
                {"label": "Jorwe\nCulture (MH)", "type": "sub", "date": "1400 \u2013 700 BCE",
                 "children": [
                     {"label": "Inamgaon &\nDaimabad", "type": "leaf"},
                     {"label": "Early & Late\nJorwe phases", "type": "leaf"},
                     {"label": "Canal irrigation,\nsocial hierarchy", "type": "leaf"}
                 ]},
                {"label": "Ahar-Banas\nCulture (RJ)", "type": "sub", "date": "2000 \u2013 1500 BCE",
                 "children": [
                     {"label": "Black & Red\nWare (BRW)", "type": "leaf"},
                     {"label": "Copper smelting\nevidence", "type": "leaf"},
                     {"label": "Rice & millet\ncultivation", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Pottery\n& Material",
            "date": "2,000 \u2013 700 BCE",
            "type": "branch",
            "children": [
                {"label": "Pottery\nTypes", "type": "sub", "date": "2,000 \u2013 700 BCE",
                 "children": [
                     {"label": "Black & Red Ware\n(BRW)", "type": "leaf"},
                     {"label": "Painted Orange-\nSlip Ware", "type": "leaf"},
                     {"label": "White-painted\nBlack Ware", "type": "leaf"}
                 ]},
                {"label": "Metal &\nTrade", "type": "sub", "date": "2,000 \u2013 700 BCE",
                 "children": [
                     {"label": "Copper tools &\nweapons", "type": "leaf"},
                     {"label": "Chert bladelets\nfrom imported raw", "type": "leaf"},
                     {"label": "Lapis lazuli &\nbead trade", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Economy\n& Society",
            "date": "2,000 \u2013 700 BCE",
            "type": "branch",
            "children": [
                {"label": "Agriculture\n& Diet", "type": "sub", "date": "2,000 \u2013 700 BCE",
                 "children": [
                     {"label": "Wheat, barley,\npulses, rice", "type": "leaf"},
                     {"label": "Cattle, sheep,\n goat rearing", "type": "leaf"},
                     {"label": "Hunting &\nfishing supplement", "type": "leaf"}
                 ]},
                {"label": "Settlement\nPattern", "type": "sub", "date": "2,000 \u2013 700 BCE",
                 "children": [
                     {"label": "Rectangular &\napsidal houses", "type": "leaf"},
                     {"label": "Pit dwellings &\nwattle-and-daub", "type": "leaf"},
                     {"label": "Fortified &\nunfortified villages", "type": "leaf"}
                 ]}
            ]
        }
    ]
}

TREE_IRON = {
    "label": "Early Iron Age\n& Megaliths",
    "type": "root",
    "children": [
        {
            "label": "Iron\nTechnology",
            "date": "1,500 BCE \u2013 100 CE",
            "type": "branch",
            "children": [
                {"label": "Earliest Iron\nin India", "type": "sub", "date": "~1800 BCE",
                 "children": [
                     {"label": "Malhar (UP):\nIron smelting ~1800 BCE", "type": "leaf"},
                     {"label": "Raja Nala Ka Tila:\nEarly iron working", "type": "leaf"},
                     {"label": "Gangetic Plain:\nSpread of iron", "type": "leaf"}
                 ]},
                {"label": "Impact of\nIron", "type": "sub", "date": "1200 \u2013 600 BCE",
                 "children": [
                     {"label": "Forest clearing\nintensified", "type": "leaf"},
                     {"label": "Agricultural\nsurplus", "type": "leaf"},
                     {"label": "Population growth\n& urbanization", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Megalithic\nCulture",
            "date": "1,200 BCE \u2013 100 CE",
            "type": "branch",
            "children": [
                {"label": "Megalith\nTypes", "type": "sub", "date": "1,200 \u2013 100 CE",
                 "children": [
                     {"label": "Dolmens:\nTable-like structures", "type": "leaf"},
                     {"label": "Menhirs:\nUpright standing stones", "type": "leaf"},
                     {"label": "Cist burials &\nstone circles", "type": "leaf"},
                     {"label": "Rock-cut\nchambers", "type": "leaf"}
                 ]},
                {"label": "Key\nSites", "type": "sub", "date": "1,200 \u2013 100 CE",
                 "children": [
                     {"label": "Adichanallur (TN):\nUrn burials with iron", "type": "leaf"},
                     {"label": "Brahmagiri (KA):\nMegalithic + early hist.", "type": "leaf"},
                     {"label": "Maski (KA):\nAshokan edict, megaliths", "type": "leaf"},
                     {"label": "Juni Karan (GJ):\nHarbour megaliths", "type": "leaf"}
                 ]}
            ]
        },
        {
            "label": "Pottery\nSequence",
            "date": "1200 \u2013 200 BCE",
            "type": "branch",
            "children": [
                {"label": "PGW\n(Painted Grey Ware)", "type": "sub", "date": "1100 \u2013 600 BCE",
                 "children": [
                     {"label": "Later Vedic\nperiod", "type": "leaf"},
                     {"label": "Grey pottery with\nblack painted motifs", "type": "leaf"},
                     {"label": "Hastinapur,\nAhichhatra", "type": "leaf"}
                 ]},
                {"label": "NBPW\n(Northern Black Polished)", "type": "sub", "date": "600 \u2013 200 BCE",
                 "children": [
                     {"label": "Mahajanapadas &\n2nd Urbanisation", "type": "leaf"},
                     {"label": "Lustrous black\nfinish", "type": "leaf"},
                     {"label": "Associated with\nearly cities", "type": "leaf"}
                 ]}
            ]
        }
    ]
}

# ── HINDI TREE DATA (encoded as Unicode escapes for script safety) ──

TREE_GEO_HI = {
    "label": "\u092d\u0942\u0917\u094b\u0932\u093f\u0915\n\u0935\u093f\u0924\u0930\u0923",
    "type": "root",
    "children": [
        {"label": "\u0928\u093f\u092e\u094d\u0928 \u092a\u0941\u0930\u093e\u092a\u093e\u0937\u093e\u0923\n\u0935\u093f\u0924\u0930\u0923", "date": "2 MYA \u2013 1,00,000 BCE", "type": "branch",
         "children": [
             {"label": "\u0938\u094b\u0906\u0928 \u0918\u093e\u091f\u0940", "date": "2 MYA \u0938\u0947", "type": "sub",
              "children": [
                  {"label": "\u0938\u094b\u0906\u0928 \u0928\u0926\u0940:\n\u0915\u094d\u0935\u093e\u0930\u094d\u091f\u094d\u091c\u093e\u0907\u091f \u0915\u0902\u0915\u0921\u093c \u0909\u092a\u0915\u0930\u0923", "type": "leaf"},
                  {"label": "\u092a\u0949\u091f\u0935\u093e\u0930 \u092a\u0920\u093e\u0930:\n\u0939\u093f\u092e\u093e\u0928\u0940 \u0914\u0930 \u0905\u0902\u0924\u0930 \u0939\u093f\u092e\u093e\u0928\u0940 \u0915\u093e\u0932", "type": "leaf"}
              ]},
             {"label": "\u0926\u0915\u094d\u0937\u093f\u0923 \u092d\u093e\u0930\u0924:\n\u090f\u0936\u0932\u093f\u092f\u0928 \u0939\u0938\u094d\u0924\u0915\u0941\u0920\u093e\u0930", "date": "1.5 MYA \u2013 1,00,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u0905\u0924\u094d\u0924\u093f\u0930\u092e\u094d\u092a\u0915\u094d\u0915\u092e:\n1.5 \u092e\u093f.\u0935. \u0915\u0949\u0938\u094d\u092e\u093f\u0915 \u0921\u0947\u091f\u093f\u0902\u0917", "type": "leaf"},
                  {"label": "\u0939\u0941\u0902\u0938\u0917\u0940:\n\u091a\u0942\u0928\u093e\u092a\u0924\u094d\u0925\u0930 \u0915\u093e\u0930\u0916\u093e\u0928\u093e", "type": "leaf"},
                  {"label": "\u092d\u0940\u092e\u092c\u0947\u091f\u0915\u093e:\n700+ \u0936\u0948\u0932\u093e\u0936\u094d\u0930\u092f", "type": "leaf"},
                  {"label": "\u0926\u093f\u0921\u0935\u093e\u0928\u093e:\n16R \u0930\u0947\u0924 \u091f\u0940\u0932\u093e", "type": "leaf"}
              ]}
         ]},
        {"label": "\u092e\u0927\u094d\u092f \u090f\u0935\u0902\n\u0909\u091a\u094d\u091a \u092a\u0941\u0930\u093e\u092a\u093e\u0937\u093e\u0923", "date": "1,00,000 \u2013 10,000 BCE", "type": "branch",
         "children": [
             {"label": "\u0928\u0926\u0940 \u0918\u093e\u091f\u0940\u092f\u093e\u0901", "date": "1,00,000 \u2013 40,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u0928\u0930\u094d\u092e\u0926\u093e \u0918\u093e\u091f\u0940:\n\u0939\u0920\u0928\u094b\u0930\u093e \u091c\u0940\u0935\u093e\u0936\u094d\u092e \u0916\u094b\u092a\u095c\u0940", "type": "leaf"},
                  {"label": "\u0932\u0942\u0928\u0940 \u0918\u093e\u091f\u0940:\n\u0932\u0942\u0928\u0940 \u0909\u0926\u094d\u092f\u094b\u0917", "type": "leaf"},
                  {"label": "\u092c\u0947\u0932\u0928 \u0918\u093e\u091f\u0940:\n\u0928\u093f\u0930\u0902\u0924\u0930 \u0905\u0928\u0941\u0915\u094d\u0930\u092e", "type": "leaf"}
              ]},
             {"label": "\u0915\u0932\u093e\u0924\u094d\u092e\u0915 \u0905\u092d\u093f\u0935\u094d\u092f\u0915\u094d\u0924\u093f", "date": "40,000 \u2013 10,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u092a\u091f\u0928\u0947:\n\u0936\u0941\u0924\u0941\u0930\u092e\u0941\u0930\u094d\u0917 \u0905\u0902\u0921\u093e \u092e\u0928\u0915\u0947", "type": "leaf"},
                  {"label": "\u0915\u0941\u0930\u094d\u0928\u0942\u0932 \u0917\u0941\u092b\u093e\u090f\u0901:\n\u0905\u0938\u094d\u0925\u093f \u0914\u0930 \u0930\u093e\u0916", "type": "leaf"}
              ]}
         ]},
        {"label": "\u092e\u0927\u094d\u092f\u092a\u093e\u0937\u093e\u0923\n\u0935\u093f\u0924\u0930\u0923", "date": "10,000 \u2013 4,000 BCE", "type": "branch",
         "children": [
             {"label": "\u092e\u0930\u0941\u0938\u094d\u0925\u0932 \u0935 \u091f\u0942\u0928\u093e \u0938\u094d\u0925\u0932", "date": "10,000 \u2013 8,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u092c\u093e\u0917\u094b\u0930:\n\u0938\u092c\u0938\u0947 \u092c\u095c\u093e \u0938\u094d\u0925\u0932", "type": "leaf"},
                  {"label": "\u0932\u0902\u0918\u0928\u091c:\n\u092e\u0941\u095c\u0947 \u0939\u0941\u090f \u0936\u0935", "type": "leaf"},
                  {"label": "\u091f\u0947\u0930\u0940 \u0938\u094d\u0925\u0932:\n\u0932\u093e\u0932 \u092c\u093e\u0932\u0941 \u0915\u0947 \u091f\u0942\u0928\u0947", "type": "leaf"}
              ]},
             {"label": "\u0917\u0902\u0917\u093e \u0914\u0930 \u092e\u0927\u094d\u092f \u092d\u093e\u0930\u0924", "date": "8,000 \u2013 4,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u0938\u0930\u093e\u0908 \u0928\u0939\u0930 \u0930\u093e\u0908:\n\u091d\u0940\u0932 \u092c\u0938\u094d\u0924\u0940", "type": "leaf"},
                  {"label": "\u092d\u0940\u092e\u092c\u0947\u091f\u0915\u093e:\n\u092e\u0927\u094d\u092f\u092a\u093e\u0937\u093e\u0923 \u0936\u0948\u0932\u091a\u093f\u0924\u094d\u0930", "type": "leaf"}
              ]}
         ]},
        {"label": "\u0928\u0935\u092a\u093e\u0937\u093e\u0923 \u0914\u0930\n\u0924\u093e\u092e\u094d\u0930\u092a\u093e\u0937\u093e\u0923", "date": "7,000 \u2013 1,000 BCE", "type": "branch",
         "children": [
             {"label": "\u0909\u0924\u094d\u0924\u0930\u0940 \u0928\u0935\u092a\u093e\u0937\u093e\u0923", "date": "7,000 \u2013 3,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u092e\u0947\u0939\u0930\u0917\u095c:\n~7000 BCE \u0915\u0943\u0937\u093f", "type": "leaf"},
                  {"label": "\u092c\u0941\u0930\u094d\u091c\u0939\u094b\u092e:\n\u0917\u095d\u0947 \u0906\u0935\u093e\u0938", "type": "leaf"},
                  {"label": "\u091a\u093f\u0930\u093e\u0902\u0921:\n\u0939\u0921\u094d\u0921\u0940 \u0909\u092a\u0915\u0930\u0923", "type": "leaf"}
              ]},
             {"label": "\u0924\u093e\u092e\u094d\u0930\u092a\u093e\u0937\u093e\u0923 \u0938\u0902\u0938\u094d\u0915\u0943\u0924\u093f\u092f\u093e\u0901", "date": "2,000 \u2013 700 BCE", "type": "sub",
              "children": [
                  {"label": "\u0915\u093e\u092f\u0925\u093e:\n\u092a\u094d\u0930\u093e\u091a\u0940\u0928\u0924\u092e", "type": "leaf"},
                  {"label": "\u0905\u0939\u093e\u0930-\u092c\u0928\u093e\u0938:\n\u0915\u093e\u0932\u093e \u0914\u0930 \u0932\u093e\u0932 \u092e\u0943\u0926\u094d\u092d\u093e\u0902\u0921", "type": "leaf"},
                  {"label": "\u092e\u093e\u0932\u0935\u093e:\n\u091a\u093f\u0924\u094d\u0930\u093f\u0924 \u092e\u0943\u0926\u094d\u092d\u093e\u0902\u0921", "type": "leaf"},
                  {"label": "\u091c\u094b\u0930\u0935\u0947:\n\u0907\u0928\u093e\u092e\u0917\u093e\u0902\u0935", "type": "leaf"}
              ]}
         ]}
    ]
}

TREE_PALEO_HI = {
    "label": "\u092a\u0941\u0930\u093e\u092a\u093e\u0937\u093e\u0923\n\u0915\u093e\u0932",
    "type": "root",
    "children": [
        {"label": "\u0928\u093f\u092e\u094d\u0928\n\u092a\u0941\u0930\u093e\u092a\u093e\u0937\u093e\u0923", "date": "2.6 MYA \u2013 1,00,000 BCE", "type": "branch",
         "children": [
             {"label": "\u0938\u094b\u0928\u093f\u092f\u0928 \u0938\u0902\u0938\u094d\u0915\u0943\u0924\u093f", "date": "2 MYA \u2013 1,00,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u0915\u0902\u0915\u0921\u093c \u091b\u0947\u0926\u0915\n\u0914\u0930 \u0915\u093e\u091f\u0928\u0947 \u0915\u0947 \u0909\u092a\u0915\u0930\u0923", "type": "leaf"},
                  {"label": "\u0938\u094b\u0906\u0928 \u0918\u093e\u091f\u0940\n\u0914\u0930 \u092a\u0949\u091f\u0935\u093e\u0930 \u092a\u0920\u093e\u0930", "type": "leaf"}
              ]},
             {"label": "\u092e\u0926\u094d\u0930\u093e\u0938\u093f\u092f\u0928 / \u090f\u0936\u0932\u093f\u092f\u0928", "date": "1.5 MYA \u2013 1,00,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u0939\u0938\u094d\u0924\u0915\u0941\u0920\u093e\u0930\n\u0914\u0930 \u0935\u093f\u0926\u093e\u0930\u0915", "type": "leaf"},
                  {"label": "\u0905\u0924\u094d\u0924\u093f\u0930\u092e\u094d\u092a\u0915\u094d\u0915\u092e:\n\u092a\u094d\u0930\u093e\u091a\u0940\u0928\u0924\u092e \u090f\u0936\u0932\u093f\u092f\u0928", "type": "leaf"},
                  {"label": "\u092d\u0940\u092e\u092c\u0947\u091f\u0915\u093e:\n\u0915\u094d\u0935\u093e\u0930\u094d\u091f\u094d\u091c\u093e\u0907\u091f \u0909\u092a\u0915\u0930\u0923", "type": "leaf"}
              ]}
         ]},
        {"label": "\u092e\u0927\u094d\u092f\n\u092a\u0941\u0930\u093e\u092a\u093e\u0937\u093e\u0923", "date": "1,00,000 \u2013 40,000 BCE", "type": "branch",
         "children": [
             {"label": "\u0909\u092a\u0915\u0930\u0923 \u092a\u094d\u0930\u094c\u0926\u094d\u092f\u094b\u0917\u093f\u0915\u0940", "date": "1,00,000 \u2013 40,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u0916\u0941\u0930\u091a\u0928\u0940, \u092c\u093f\u0902\u0926\u0941,\n\u092c\u0947\u0927\u0915", "type": "leaf"},
                  {"label": "\u091a\u0930\u094d\u091f, \u091c\u0947\u0938\u094d\u092a\u0930,\n\u091a\u093e\u0932\u094d\u0938\u0947\u0921\u0928\u0940", "type": "leaf"},
                  {"label": "\u0928\u093f\u092e\u094d\u0928 \u092a\u0941\u0930\u093e\u092a\u093e\u0937\u093e\u0923 \u0938\u0947\n\u0938\u0942\u0915\u094d\u0937\u094d\u092e \u0936\u0932\u094d\u0915", "type": "leaf"}
              ]},
             {"label": "\u092a\u094d\u0930\u092e\u0941\u0916 \u0938\u094d\u0925\u0932", "date": "1,00,000 \u2013 40,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u0928\u0947\u0935\u093e\u0938\u0928 \u0909\u0926\u094d\u092f\u094b\u0917:\n\u092a\u094d\u0930\u0935\u0930\u093e \u0928\u0926\u0940", "type": "leaf"},
                  {"label": "\u0932\u0942\u0928\u0940 \u0918\u093e\u091f\u0940:\n\u0932\u0942\u0928\u0940 \u0909\u0926\u094d\u092f\u094b\u0917", "type": "leaf"},
                  {"label": "\u092c\u0947\u0932\u0928 \u0918\u093e\u091f\u0940:\n\u0928\u093f\u0930\u0902\u0924\u0930 \u0905\u0928\u0941\u0915\u094d\u0930\u092e", "type": "leaf"}
              ]}
         ]},
        {"label": "\u0909\u091a\u094d\u091a\n\u092a\u0941\u0930\u093e\u092a\u093e\u0937\u093e\u0923", "date": "40,000 \u2013 10,000 BCE", "type": "branch",
         "children": [
             {"label": "\u0938\u093e\u0902\u0938\u094d\u0915\u0943\u0924\u093f\u0915 \u092a\u094d\u0930\u0917\u0924\u093f", "date": "40,000 \u2013 10,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u0939\u094b\u092e\u094b \u0938\u0947\u092a\u093f\u092f\u0928\u094d\u0938\n\u0915\u093e \u0909\u0926\u094d\u092d\u0935", "type": "leaf"},
                  {"label": "\u092c\u094d\u0932\u0947\u0921, \u092c\u0941\u0930\u093f\u0928,\n\u0939\u0921\u094d\u0921\u0940 \u0915\u0947 \u0909\u092a\u0915\u0930\u0923", "type": "leaf"},
                  {"label": "\u092a\u091f\u0928\u0947:\u0936\u0941\u0924\u0941\u0930\u092e\u0941\u0930\u094d\u0917 \u0905\u0902\u0921\u093e", "type": "leaf"}
              ]},
             {"label": "\u0936\u0948\u0932\u091a\u093f\u0924\u094d\u0930 \u0914\u0930 \u0938\u094d\u0925\u0932", "date": "40,000 \u2013 10,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u092d\u0940\u092e\u092c\u0947\u091f\u0915\u093e:\n\u090a\u092a\u0930\u0940 \u092a\u0941\u0930\u093e\u092a\u093e\u0937\u093e\u0923 \u091a\u093f\u0924\u094d\u0930\u0915\u0932\u093e", "type": "leaf"},
                  {"label": "\u0915\u0941\u0930\u094d\u0928\u0942\u0932 \u0917\u0941\u092b\u093e:\n\u0930\u093e\u0916 \u0914\u0930 \u091c\u0940\u0935\u093e\u0936\u094d\u092e", "type": "leaf"}
              ]}
         ]}
    ]
}

TREE_MESO_HI = {
    "label": "\u092e\u0927\u094d\u092f\u092a\u093e\u0937\u093e\u0923\n\u0915\u093e\u0932",
    "type": "root",
    "children": [
        {"label": "\u0939\u094b\u0932\u094b\u0938\u0940\u0928\n\u0938\u0902\u0926\u0930\u094d\u092d", "date": "~10,000 BCE \u0938\u0947", "type": "branch",
         "children": [
             {"label": "\u091c\u0932\u0935\u093e\u092f\u0941 \u092a\u0930\u093f\u0935\u0930\u094d\u0924\u0928", "date": "10,000 \u2013 8,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u0939\u093f\u092e \u092f\u0941\u0917 \u0915\u093e \u0905\u0902\u0924:\n\u0917\u0930\u092e \u0914\u0930 \u0906\u0930\u094d\u0926\u094d\u0930", "type": "leaf"},
                  {"label": "\u0935\u0928 \u0935\u093f\u0938\u094d\u0924\u093e\u0930\n\u092e\u0928\u0938\u0942\u0928 \u0938\u094d\u0925\u093f\u0930\u0940\u0915\u0930\u0923", "type": "leaf"},
                  {"label": "\u091b\u094b\u091f\u0947 \u0924\u0947\u091c\u093c\nu091c\u093e\u0928\u0935\u0930 \u0909\u092d\u0930\u0947", "type": "leaf"}
              ]}
         ]},
        {"label": "\u0938\u0942\u0915\u094d\u0937\u094d\u092e\u092a\u093e\u0937\u093e\u0923\n\u0909\u092a\u0915\u0930\u0923", "date": "10,000 \u2013 8,000 BCE", "type": "branch",
         "children": [
             {"label": "\u091c\u094d\u092f\u093e\u092e\u093f\u0924\u0940\u092f \u092a\u094d\u0930\u0915\u093e\u0930", "date": "10,000 \u2013 8,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u091a\u0902\u0926\u094d\u0930\u093e\u0915\u093e\u0930, \u0924\u094d\u0930\u093f\u092d\u0941\u091c,\n\u0938\u092e\u0932\u092e\u094d\u092c", "type": "leaf"},
                  {"label": "\u0906\u0915\u093e\u0930 1\u20135 cm:\n\u0938\u0902\u092f\u0941\u0915\u094d\u0924 \u0909\u092a\u0915\u0930\u0923", "type": "leaf"}
              ]},
             {"label": "\u0905\u091c\u094d\u092f\u093e\u092e\u093f\u0924\u0940\u092f \u092a\u094d\u0930\u0915\u093e\u0930", "date": "10,000 \u2013 8,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u092a\u0943\u0937\u094d\u0920\u093f\u0915\u093e \u092c\u094d\u0932\u0947\u0921,\n\u092c\u0947\u0927\u0915", "type": "leaf"},
                  {"label": "\u092e\u093e\u0907\u0915\u094d\u0930\u094b\u092c\u0941\u0930\u093f\u0928\nt\u0947\u0915\u0928\u0940\u0915", "type": "leaf"}
              ]}
         ]},
        {"label": "\u092a\u094d\u0930\u092e\u0941\u0916\n\u0938\u094d\u0925\u0932", "date": "10,000 \u2013 4,000 BCE", "type": "branch",
         "children": [
             {"label": "\u0909\u0924\u094d\u0924\u0930 \u0914\u0930 \u092a\u0936\u094d\u091a\u093f\u092e", "date": "10,000 \u2013 8,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u092c\u093e\u0917\u094b\u0930:\n\u0938\u092c\u0938\u0947 \u092c\u095c\u093e \u0938\u094d\u0925\u0932", "type": "leaf"},
                  {"label": "\u0932\u0902\u0918\u0928\u091c:\n\u092e\u0941\u095c\u0947 \u0939\u0941\u090f \u0936\u0935", "type": "leaf"},
                  {"label": "\u091f\u093f\u0932\u0935\u093e\u0921\u093c\u093e:\n\u0932\u0942\u0928\u0940 \u092c\u0947\u0938\u093f\u0928 \u091f\u0942\u0928\u0947", "type": "leaf"}
              ]},
             {"label": "\u092e\u0927\u094d\u092f \u0914\u0930 \u092a\u0942\u0930\u094d\u0935", "date": "10,000 \u2013 8,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u092d\u0940\u092e\u092c\u0947\u091f\u0915\u093e:\n\u0936\u0948\u0932\u091a\u093f\u0924\u094d\u0930 \u0915\u0940 \u0909\u0924\u094d\u0915\u0943\u0937\u094d\u091f \u0915\u0943\u0924\u093f", "type": "leaf"},
                  {"label": "\u0906\u0926\u092e\u0917\u095d:\n\u092a\u094d\u0930\u093e\u091a\u0940\u0928\u0924\u092e \u092a\u0936\u0941\u092a\u093e\u0932\u0928", "type": "leaf"},
                  {"label": "\u0938\u0930\u093e\u0908 \u0928\u0939\u0930 \u0930\u093e\u0908:\n\u0917\u0902\u0917\u093e \u091d\u0940\u0932 \u092c\u0938\u094d\u0924\u0940", "type": "leaf"}
              ]}
         ]}
    ]
}

TREE_NEO_HI = {
    "label": "\u0928\u0935\u092a\u093e\u0937\u093e\u0923\n\u0915\u093e\u0932",
    "type": "root",
    "children": [
        {"label": "\u0928\u0935\u092a\u093e\u0937\u093e\u0923\n\u0915\u094d\u0930\u093e\u0902\u0924\u093f", "date": "8,000 \u2013 2,000 BCE", "type": "branch",
         "children": [
             {"label": "\u0906\u0930\u094d\u0925\u093f\u0915 \u092a\u0930\u093f\u0935\u0930\u094d\u0924\u0928", "date": "8,000 \u2013 3,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u0916\u093e\u0926\u094d\u092f \u0938\u0902\u0917\u094d\u0930\u0939 \u0938\u0947\n\u0916\u093e\u0926\u094d\u092f \u0909\u0924\u094d\u092a\u093e\u0926\u0928", "type": "leaf"},
                  {"label": "\u0917\u0947\u0939\u0942\u0902, \u091c\u094c,\n\u0914\u0930 \u091a\u093e\u0935\u0932 \u0915\u0940 \u0916\u0947\u0924\u0940", "type": "leaf"},
                  {"label": "\u0938\u094d\u0925\u093e\u092f\u0940 \u0917\u093e\u0901\u0935\n\u0914\u0930 \u092e\u0943\u0926\u094d\u092d\u093e\u0902\u0921", "type": "leaf"}
              ]}
         ]},
        {"label": "\u092a\u0949\u0932\u093f\u0936 \u092a\u093e\u0937\u093e\u0923\n\u0909\u092a\u0915\u0930\u0923", "date": "8,000 \u2013 2,000 BCE", "type": "branch",
         "children": [
             {"label": "\u092a\u0940\u0938\u0947 \u0914\u0930 \u092a\u0949\u0932\u093f\u0936 \u0909\u092a\u0915\u0930\u0923", "date": "8,000 \u2013 2,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u0938\u0947\u0932\u094d\u091f, \u0915\u0941\u0932\u094d\u0939\u093e\u095c\u0940,\n\u092c\u0938\u0942\u0932\u093e", "type": "leaf"},
                  {"label": "\u091c\u093e\u0902\u0924 \u0914\u0930\n\u092a\u0940\u0938\u0928\u0947 \u0915\u0947 \u092a\u0924\u094d\u0925\u0930", "type": "leaf"},
                  {"label": "\u0917\u0926\u093e \u0936\u0940\u0930\u094d\u0937\n\u0914\u0930 \u0935\u0932\u092f \u092a\u0924\u094d\u0925\u0930", "type": "leaf"}
              ]}
         ]},
        {"label": "\u0915\u094d\u0937\u0947\u0924\u094d\u0930\u0940\u092f\nu0938\u0902\u0938\u094d\u0915\u0943\u0924\u093f\u092f\u093e\u0901", "date": "8,000 \u2013 2,000 BCE", "type": "branch",
         "children": [
             {"label": "\u0909\u0924\u094d\u0924\u0930 \u092d\u093e\u0930\u0924", "date": "7,000 \u2013 3,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u092e\u0947\u0939\u0930\u0917\u095c:\n~7000 BCE", "type": "leaf"},
                  {"label": "\u092c\u0941\u0930\u094d\u091c\u0939\u094b\u092e:\n\u0917\u095d\u0947 \u0906\u0935\u093e\u0938", "type": "leaf"}
              ]},
             {"label": "\u0917\u0902\u0917\u093e \u092e\u0948\u0926\u093e\u0928", "date": "6,000 \u2013 2,000 BCE", "type": "sub",
              "children": [
                  {"label": "\u0932\u0939\u0941\u0930\u093e\u0926\u0947\u0935:\n\u092a\u094d\u0930\u093e\u091a\u0940\u0928\u0924\u092e \u091a\u093e\u0935\u0932", "type": "leaf"},
                  {"label": "\u0915\u094b\u0932\u094d\u0921\u093f\u0939\u0935\u093e:\n\u0930\u091c\u094d\u091c\u0942 \u092e\u0943\u0926\u094d\u092d\u093e\u0902\u0921", "type": "leaf"},
                  {"label": "\u091a\u093f\u0930\u093e\u0902\u0921:\n\u0939\u0921\u094d\u0921\u0940 \u0909\u092a\u0915\u0930\u0923", "type": "leaf"}
              ]}
         ]}
    ]
}

TREE_CHALCO_HI = {
    "label": "\u0924\u093e\u092e\u094d\u0930\u092a\u093e\u0937\u093e\u0923\nu092f\u0941\u0917",
    "type": "root",
    "children": [
        {"label": "\u0915\u094d\u0937\u0947\u0924\u094d\u0930\u0940\u092f\n\u0938\u0902\u0938\u094d\u0915\u0943\u0924\u093f\u092f\u093e\u0901", "date": "2,000 \u2013 700 BCE", "type": "branch",
         "children": [
             {"label": "\u0915\u093e\u092f\u0925\u093e \u0938\u0902\u0938\u094d\u0915\u0943\u0924\u093f", "date": "~2000 BCE", "type": "sub",
              "children": [
                  {"label": "\u092d\u093e\u0930\u0924 \u092e\u0947\u0902\n\u092a\u094d\u0930\u093e\u091a\u0940\u0928\u0924\u092e", "type": "leaf"},
                  {"label": "\u0938\u092b\u0947\u0926 \u092a\u0947\u0902\u091f \u0915\u093e\u0932\u093e\n\u0914\u0930 \u0932\u093e\u0932 \u092e\u0943\u0926\u094d\u092d\u093e\u0902\u0921", "type": "leaf"},
                  {"label": "\u0924\u093e\u0902\u092c\u0947 \u0915\u0947 \u0909\u092a\u0915\u0930\u0923\n\u0914\u0930 \u092a\u0924\u094d\u0925\u0930 \u0915\u0947 \u092c\u094d\u0932\u0947\u0921", "type": "leaf"}
              ]},
             {"label": "\u092e\u093e\u0932\u0935\u093e \u0938\u0902\u0938\u094d\u0915\u0943\u0924\u093f", "date": "1700 \u2013 1200 BCE", "type": "sub",
              "children": [
                  {"label": "\u091a\u093f\u0924\u094d\u0930\u093f\u0924\n\u0928\u093e\u0930\u0902\u0917\u0940 \u092e\u0943\u0926\u094d\u092d\u093e\u0902\u0921", "type": "leaf"},
                  {"label": "\u0928\u0935\u0926\u093e\u091f\u094b\u0932\u0940,\n\u092e\u0939\u0947\u0936\u094d\u0935\u0930", "type": "leaf"}
              ]},
             {"label": "\u091c\u094b\u0930\u0935\u0947 \u0938\u0902\u0938\u094d\u0915\u0943\u0924\u093f", "date": "1400 \u2013 700 BCE", "type": "sub",
              "children": [
                  {"label": "\u0907\u0928\u093e\u092e\u0917\u093e\u0902\u0935\n\u0914\u0930 \u0926\u093e\u092f\u092e\u093e\u092c\u093e\u0926", "type": "leaf"},
                  {"label": "\u0928\u0939\u0930 \u0938\u093f\u0902\u091a\u093e\u0907\n\u0914\u0930 \u0938\u093e\u092e\u093e\u091c\u093f\u0915 \u0938\u094d\u0924\u0930\u0940\u0915\u0930\u0923", "type": "leaf"}
              ]},
             {"label": "\u0905\u0939\u093e\u0930-\u092c\u0928\u093e\u0938", "date": "2000 \u2013 1500 BCE", "type": "sub",
              "children": [
                  {"label": "\u0915\u093e\u0932\u093e \u0914\u0930 \u0932\u093e\u0932\n\u092e\u0943\u0926\u094d\u092d\u093e\u0902\u0921", "type": "leaf"},
                  {"label": "\u0924\u093e\u0902\u092c\u0947 \u0915\u093e\n\u092a\u093f\u0918\u0932\u0928\u0947 \u0915\u0947 \u0938\u092c\u0942\u0924", "type": "leaf"}
              ]}
         ]}
    ]
}

TREE_IRON_HI = {
    "label": "\u0932\u094c\u0939 \u092f\u0941\u0917\n\u0914\u0930 \u092e\u0939\u093e\u092a\u093e\u0937\u093e\u0923",
    "type": "root",
    "children": [
        {"label": "\u0932\u094c\u0939\n\u092a\u094d\u0930\u094c\u0926\u094d\u092f\u094b\u0917\u093f\u0915\u0940", "date": "1,500 BCE \u2013 100 CE", "type": "branch",
         "children": [
             {"label": "\u092d\u093e\u0930\u0924 \u092e\u0947\u0902 \u092a\u094d\u0930\u093e\u091a\u0940\u0928\u0924\u092e \u0932\u094b\u0939\u093e", "date": "~1800 BCE", "type": "sub",
              "children": [
                  {"label": "\u092e\u0932\u094d\u0939\u093e\u0930:\n~1800 BCE \u0932\u094c\u0939 \u092a\u093f\u0918\u0932\u0928", "type": "leaf"},
                  {"label": "\u0930\u093e\u091c\u093e \u0928\u0932\u093e \u0915\u093e \u091f\u093f\u0932\u093e:\n\u092a\u094d\u0930\u093e\u091a\u0940\u0928 \u0932\u094c\u0939 \u0915\u093e\u0930\u094d\u092f", "type": "leaf"},
                  {"label": "\u0917\u0902\u0917\u093e \u092e\u0948\u0926\u093e\u0928:\n\u0932\u094b\u0939\u0947 \u0915\u093e \u092a\u094d\u0930\u0938\u093e\u0930", "type": "leaf"}
              ]},
             {"label": "\u0932\u094b\u0939\u0947 \u0915\u093e \u092a\u094d\u0930\u092d\u093e\u0935", "date": "1200 \u2013 600 BCE", "type": "sub",
              "children": [
                  {"label": "\u0935\u0928 \u0915\u091f\u093e\u0908\n\u092e\u0947\u0902 \u0935\u0943\u0926\u094d\u0927\u093f", "type": "leaf"},
                  {"label": "\u0915\u0943\u0937\u093f\n\u0905\u0927\u093f\u0936\u0947\u0937", "type": "leaf"},
                  {"label": "\u091c\u0928\u0938\u0902\u0916\u094d\u092f\u093e \u0935\u0943\u0926\u094d\u0927\u093f\n\u0914\u0930 \u0928\u0917\u0930\u0940\u0915\u0930\u0923", "type": "leaf"}
              ]}
         ]},
        {"label": "\u092e\u0939\u093e\u092a\u093e\u0937\u093e\u0923\n\u0938\u0902\u0938\u094d\u0915\u0943\u0924\u093f", "date": "1,200 BCE \u2013 100 CE", "type": "branch",
         "children": [
             {"label": "\u092e\u0939\u093e\u092a\u093e\u0937\u093e\u0923 \u0915\u0947 \u092a\u094d\u0930\u0915\u093e\u0930", "date": "1,200 \u2013 100 CE", "type": "sub",
              "children": [
                  {"label": "\u0921\u094b\u0932\u092e\u0947\u0928:\n\u092e\u0947\u091c\u093e\u0915\u093e\u0930 \u0938\u0902\u0930\u091a\u0928\u093e\u090f\u0901", "type": "leaf"},
                  {"label": "\u092e\u0947\u0928\u0939\u093f\u0930:\n\u0938\u0940\u0927\u0947 \u0916\u095c\u0947 \u092a\u0924\u094d\u0925\u0930", "type": "leaf"},
                  {"label": "\u092a\u0924\u094d\u0925\u0930 \u0915\u0947 \u0918\u0947\u0930\u0947\n\u0914\u0930 \u0938\u093f\u0938\u094d\u091f \u0915\u092c\u094d\u0930", "type": "leaf"}
              ]},
             {"label": "\u092a\u094d\u0930\u092e\u0941\u0916 \u0938\u094d\u0925\u0932", "date": "1,200 \u2013 100 CE", "type": "sub",
              "children": [
                  {"label": "\u0905\u0921\u093f\u091a\u0928\u0932\u094d\u0932\u0942\u0930:\n\u0932\u094b\u0939\u0947 \u0915\u0947 \u0938\u093e\u0925 \u0915\u0932\u0936 \u0936\u0935", "type": "leaf"},
                  {"label": "\u092c\u094d\u0930\u0939\u094d\u092e\u0917\u093f\u0930\u093f:\n\u092e\u0939\u093e\u092a\u093e\u0937\u093e\u0923 \u0914\u0930 \u090f\u0924\u093f\u0939\u093e\u0938\u093f\u0915", "type": "leaf"},
                  {"label": "\u091c\u0942\u0928\u0940 \u0915\u093e\u0930\u0923:\n\u092c\u0902\u0926\u0930\u0917\u093e\u0939 \u092e\u0939\u093e\u092a\u093e\u0937\u093e\u0923", "type": "leaf"}
              ]}
         ]}
    ]
}


# ── MAP TOPIC → TREE DATA ─────────────────────────────────────

TOPICS = {
    "Geographical-Distribution-and-Characteristics-of-Pre-History": {
        "en_title": "Geographical Distribution & Characteristics of Pre-History &mdash; Interactive Mindmap",
        "hi_title": "\u092d\u0942\u0917\u094b\u0932\u093f\u0915 \u0935\u093f\u0924\u0930\u0923 \u0914\u0930 \u0935\u093f\u0936\u0947\u0937\u0924\u093e\u090f\u0901 &mdash; \u0907\u0902\u091f\u0930\u0948\u0915\u094d\u091f\u093f\u0935 \u092e\u093e\u0907\u0902\u0921\u092e\u0948\u092a",
        "tree_en": TREE_GEO,
        "tree_hi": TREE_GEO_HI
    },
    "History-of-Paleolithic-or-Old-Stone-Age": {
        "en_title": "Paleolithic / Old Stone Age &mdash; Interactive Mindmap",
        "hi_title": "\u092a\u0941\u0930\u093e\u092a\u093e\u0937\u093e\u0923 \u0915\u093e\u0932 &mdash; \u0907\u0902\u091f\u0930\u0948\u0915\u094d\u091f\u093f\u0935 \u092e\u093e\u0907\u0902\u0921\u092e\u0948\u092a",
        "tree_en": TREE_PALEO,
        "tree_hi": TREE_PALEO_HI
    },
    "History-of-Mesolithic-or-Middle-Stone-Age": {
        "en_title": "Mesolithic / Middle Stone Age &mdash; Interactive Mindmap",
        "hi_title": "\u092e\u0927\u094d\u092f\u092a\u093e\u0937\u093e\u0923 \u0915\u093e\u0932 &mdash; \u0907\u0902\u091f\u0930\u0948\u0915\u094d\u091f\u093f\u0935 \u092e\u093e\u0907\u0902\u0921\u092e\u0948\u092a",
        "tree_en": TREE_MESO,
        "tree_hi": TREE_MESO_HI
    },
    "History-of-Neolithic-Age-or-New-Stone-Age": {
        "en_title": "Neolithic / New Stone Age &mdash; Interactive Mindmap",
        "hi_title": "\u0928\u0935\u092a\u093e\u0937\u093e\u0923 \u0915\u093e\u0932 &mdash; \u0907\u0902\u091f\u0930\u0948\u0915\u094d\u091f\u093f\u0935 \u092e\u093e\u0907\u0902\u0921\u092e\u0948\u092a",
        "tree_en": TREE_NEO,
        "tree_hi": TREE_NEO_HI
    },
    "History-of-Chalcolithic-Age": {
        "en_title": "Chalcolithic (Copper-Stone) Age &mdash; Interactive Mindmap",
        "hi_title": "\u0924\u093e\u092e\u094d\u0930\u092a\u093e\u0937\u093e\u0923 \u092f\u0941\u0917 &mdash; \u0907\u0902\u091f\u0930\u0948\u0915\u094d\u091f\u093f\u0935 \u092e\u093e\u0907\u0902\u0921\u092e\u0948\u092a",
        "tree_en": TREE_CHALCO,
        "tree_hi": TREE_CHALCO_HI
    },
    "History-of-Early-Iron-Age": {
        "en_title": "Early Iron Age & Megaliths &mdash; Interactive Mindmap",
        "hi_title": "\u0932\u094c\u0939 \u092f\u0941\u0917 \u0914\u0930 \u092e\u0939\u093e\u092a\u093e\u0937\u093e\u0923 &mdash; \u0907\u0902\u091f\u0930\u0948\u0915\u094d\u091f\u093f\u0935 \u092e\u093e\u0907\u0902\u0921\u092e\u0948\u092a",
        "tree_en": TREE_IRON,
        "tree_hi": TREE_IRON_HI
    }
}

# ── PATCHING LOGIC ────────────────────────────────────────────

def patch_html(filepath, tree_data, is_hindi, title_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add mindmap CSS link before closing </head>
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    # 2. Add mindmap card HTML in #notes-panel (after tab-panel opening, before deep-dive-section)
    if is_hindi:
        instr = '\u0915\u093f\u0938\u0940 <strong style="color:#a78bfa;">\u092c\u0948\u0902\u0917\u0928\u0940</strong> \u092f\u093e <strong style="color:#2ecc71;">\u0939\u0930\u0947</strong> <strong>+</strong> \u091f\u0949\u0917\u0932 \u092a\u0930 \u0915\u094d\u0932\u093f\u0915 \u0915\u0930\u0947\u0902 \u2014 \u090f\u0915 \u0915\u094b \u0916\u094b\u0932\u0928\u0947 \u092a\u0930 \u0926\u0942\u0938\u0930\u0947 \u0938\u094d\u0935\u0924\u0903 \u092c\u0902\u0926 \u0939\u094b \u091c\u093e\u090f\u0902\u0917\u0947\u0964'
    else:
        instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand \u2014 opening one automatically closes its siblings.'
    mindmap_card = f'''            <!-- Interactive Mindmap -->
            <div class="card-premium" id="mindmap-card">
                <h2 class="card-title"><i class="fas fa-diagram-project"></i> {title_text}</h2>
                <p style="color:var(--text-light);font-size:.87rem;margin-bottom:1.25rem;">
                    <i class="fas fa-circle-info" style="color:#8b5cf6;margin-right:5px;"></i>
                    {instr}
                </p>
                <div id="prehistory-mindmap-container"></div>
            </div>
            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->
'''
    # Find the deep-dive-section div and insert before it
    # Pattern: it's either <!-- Deep-Dive ... --> followed by <div id="deep-dive-section">
    deep_dive_pattern = r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)'
    if re.search(deep_dive_pattern, html):
        # Insert mindmap card before deep-dive section
        html = re.sub(deep_dive_pattern, mindmap_card + r'\1', html)
    else:
        # Fallback: insert after <!-- ==================== TAB 1: STUDY NOTES ==================== -->
        tab1_marker = '<!-- ==================== TAB 1: STUDY NOTES ==================== -->'
        if tab1_marker in html:
            idx = html.index(tab1_marker)
            # Find the first card-premium after this marker
            insert_pos = html.find('<div class="tab-panel active" id="notes-panel"', idx)
            if insert_pos > 0:
                # Find the first child element
                first_child = html.find('<div class="card-premium"', insert_pos)
                if first_child > 0:
                    html = html[:first_child] + mindmap_card + html[first_child:]
                else:
                    # Insert at end of tab-panel opening
                    html = html.replace(
                        '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">',
                        '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">\n' + mindmap_card,
                        1
                    )

    # 3. Add JS engine and tree data before </body>
    # First check if mindmap-engine is already loaded
    if 'mindmap-engine.min.js' not in html:
        # Create the inline script with tree data
        tree_json = json.dumps(tree_data)
        lang = "'hi'" if is_hindi else "'en'"
        inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=1"></script>
    <script>
    renderMindmap({tree_json}, undefined, {lang});
    </script>
'''
        html = html.replace('</body>', inline_script + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  Patched: {filepath}")


# ── MAIN ──────────────────────────────────────────────────────

if __name__ == '__main__':
    for folder, info in TOPICS.items():
        # English version
        en_path = os.path.join(BASE, folder, 'index.html')
        if os.path.exists(en_path):
            patch_html(en_path, info['tree_en'], False, info['en_title'])
        else:
            print(f"  SKIP (not found): {en_path}")

        # Hindi version
        hi_path = os.path.join(BASE, folder, 'hi', 'index.html')
        if os.path.exists(hi_path):
            patch_html(hi_path, info['tree_hi'], True, info['hi_title'])
        else:
            print(f"  SKIP (not found): {hi_path}")

    print("\nDone! All mindmaps injected successfully.")