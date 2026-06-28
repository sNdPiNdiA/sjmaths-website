import os
import re
import json

BASE_DIR = r"upsc/polity/Constitutional-Extra-Constitutional-Bodies"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'upsc', 'spsc', 'jspsc', 'cag', 'cvc', 'cic', 'sic', 'nhrc', 'shrc', 'lop', 'pm', 'wto', 'ncsc', 'ncst', 'rti'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Extremely Detailed, Multi-Branch, Multi-Sub, Multi-Leaf 3-Tier Mindmaps
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. PUBLIC SERVICE COMMISSIONS (UPSC, SPSC, JSPSC)
    if 'upsc' in fl or 'public-service' in fl or 'spsc' in fl or 'jspsc' in fl:
        return [
            {
                "label": "Composition & Appointment",
                "type": "branch",
                "date": "Article 316",
                "children": [
                    {
                        "label": "UPSC Structure", "type": "sub", "date": "Federal", "children": [
                            {"label": "Appointed by President; 9 to 11 members; term of 6 years or until age 65 (whichever is earlier)", "type": "leaf"},
                            {"label": "Removal: Only by President on grounds of misbehavior after Supreme Court inquiry (Art 317)", "type": "leaf"},
                            {"label": "Art 319: Chairman ineligible for further Govt office; members only eligible as UPSC/SPSC Chairman", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "SPSC & JSPSC Structure", "type": "sub", "date": "State/Joint", "children": [
                            {"label": "SPSC: Appointed by Governor but removed ONLY by President; term of 6 years or until age 62", "type": "leaf"},
                            {"label": "JSPSC: Statutory body created by Parliament on state request; members appointed & removed by President; 6 yrs/62 age", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Functions & Autonomy",
                "type": "branch",
                "date": "Article 320",
                "children": [
                    {
                        "label": "Duties & Mandate", "type": "sub", "date": "Syllabus Core", "children": [
                            {"label": "Conducts exams for appointments to services; consulted on civil service recruitment methods & rules", "type": "leaf"},
                            {"label": "Advises on disciplinary matters, pension claims, and legal costs; advice is advisory, not binding", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Autonomy Safeguards", "type": "sub", "date": "Independence", "children": [
                            {"label": "Expenses charged on Consolidated Fund of India/State (non-votable); conditions of service cannot be varied to disadvantage", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. ELECTION COMMISSION & ELECTIONS & REFORMS
    elif 'election-commission' in fl or 'elections' in fl or 'electoral' in fl:
        return [
            {
                "label": "ECI Structure",
                "type": "branch",
                "date": "Article 324",
                "children": [
                    {
                        "label": "Constitutional Mandate", "type": "sub", "date": "ECI Chamber", "children": [
                            {"label": "Superintendence, direction, and control of elections to Parliament, State Legislatures, President & VP", "type": "leaf"},
                            {"label": "CEC & 2 ECs appointed by President based on selection panel (PM, Union Cabinet Minister, LoP)", "type": "leaf"},
                            {"label": "CEC removal matches SC Judge; other ECs removed only on specific recommendation of CEC (Art 324(5))", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Franchise & Conduct", "type": "sub", "date": "Adult Suffrage", "children": [
                            {"label": "Art 325: No person ineligible for electoral roll on grounds of religion, race, caste, or sex", "type": "leaf"},
                            {"label": "Art 326: Universal Adult Suffrage; 61st CA (1988) reduced voting age limit from 21 to 18", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Electoral Reforms",
                "type": "branch",
                "date": "Reforms & Panels",
                "children": [
                    {
                        "label": "Key Committees", "type": "sub", "date": "Recommendations", "children": [
                            {"label": "Dinesh Goswami Committee: Recommended state funding in kind, checking proxy voting, & EVM usage", "type": "leaf"},
                            {"label": "Indrajit Gupta Committee: Recommended state funding of elections to curb muscle and black money power", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Legislative Reforms", "type": "sub", "date": "Technology", "children": [
                            {"label": "Introduction of VVPAT (Voter Verifiable Paper Audit Trail), NOTA, ceiling on election expenses, and declaration of criminal assets", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. COMPTROLLER AND AUDITOR GENERAL OF INDIA
    elif 'cag' in fl or 'comptroller' in fl:
        return [
            {
                "label": "Office & Independence",
                "type": "branch",
                "date": "Article 148",
                "children": [
                    {
                        "label": "Appointment & Tenure", "type": "sub", "date": "CAG Standing", "children": [
                            {"label": "Appointed by President under warrant; 6 years or 65 years age limit; removed like an SC Judge", "type": "leaf"},
                            {"label": "Post-retirement: Ineligible for further office under Central/State Govt to ensure independence", "type": "leaf"},
                            {"label": "Salary & administrative expenses charged on Consolidated Fund of India; conditions of service cannot be varied to disadvantage", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Duties & Reports",
                "type": "branch",
                "date": "Article 149-151",
                "children": [
                    {
                        "label": "Audit Jurisdiction", "type": "sub", "date": "Audit Scope", "children": [
                            {"label": "Audits Consolidated, Contingency, & Public Accounts of Union, States, & UTs with assemblies (Article 149)", "type": "leaf"},
                            {"label": "Audits receipts and expenditures of bodies substantially financed from Central or State revenues", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Reporting Mechanism", "type": "sub", "date": "Reports", "children": [
                            {"label": "Submits 3 audit reports (Appropriation, Finance, Commercial) to President (Art 151), examined by PAC", "type": "leaf"},
                            {"label": "CAG acts as friend, philosopher, and guide to Public Accounts Committee (PAC) during report scrutiny", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. ATTORNEY GENERAL OF INDIA
    elif 'attorney-general' in fl:
        return [
            {
                "label": "Appointment & Standing",
                "type": "branch",
                "date": "Article 76",
                "children": [
                    {
                        "label": "Constitutional Status", "type": "sub", "date": "AG Office", "children": [
                            {"label": "Appointed by President; must be qualified to be appointed a Supreme Court Judge", "type": "leaf"},
                            {"label": "Tenure: Holds office during the pleasure of the President; no fixed term in Constitution", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Rights & Audiences", "type": "sub", "date": "Rights", "children": [
                            {"label": "Right of audience in all courts in the territory of India; right to participate in Parliament (Art 88) but NO voting right", "type": "leaf"},
                            {"label": "Enjoys all privileges and immunities available to a Member of Parliament", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Duties & Limits",
                "type": "branch",
                "date": "Functions",
                "children": [
                    {
                        "label": "Advisory Role", "type": "sub", "date": "Advisory", "children": [
                            {"label": "Chief law officer of Govt; advises Union on legal matters referred by President; performs duties assigned by Constitution", "type": "leaf"},
                            {"label": "Appears on behalf of Govt in Supreme Court in all cases concerning Union under Article 143 references", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Limitations", "type": "sub", "date": "Restrictions", "children": [
                            {"label": "Cannot advise against Union Govt; cannot defend accused in criminal prosecutions without Govt permission; not a full-time civil servant", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. ADVOCATE GENERAL
    elif 'advocate-general' in fl:
        return [
            {
                "label": "Appointment & Standing",
                "type": "branch",
                "date": "Article 165",
                "children": [
                    {
                        "label": "Constitutional Status", "type": "sub", "date": "AG Office", "children": [
                            {"label": "Appointed by Governor; must be qualified to be appointed a High Court Judge", "type": "leaf"},
                            {"label": "Tenure: Holds office during the pleasure of the Governor; remuneration determined by Governor; no fixed term", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Rights in Legislature", "type": "sub", "date": "Rights", "children": [
                            {"label": "Right to speak & participate in State Legislature and its committees; enjoys privileges of MLA but NO voting rights", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Duties & Roles",
                "type": "branch",
                "date": "Functions",
                "children": [
                    {
                        "label": "State Advisor", "type": "sub", "date": "Advisory", "children": [
                            {"label": "Highest law officer of the state; advises State Govt on legal matters; performs duties assigned by Governor", "type": "leaf"},
                            {"label": "Represents the State Govt in the High Court and subordinate courts in all major civil and criminal suits", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. FINANCE COMMISSION
    elif 'finance' in fl:
        return [
            {
                "label": "Constitution & Devolution",
                "type": "branch",
                "date": "Article 280",
                "children": [
                    {
                        "label": "Composition", "type": "sub", "date": "Chamber", "children": [
                            {"label": "Quasi-judicial body appointed by President every 5th year; Chairman + 4 members", "type": "leaf"},
                            {"label": "Qualifications of members determined by Parliament under Finance Commission Act 1951", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Devolution Principles", "type": "sub", "date": "Devolution", "children": [
                            {"label": "Recommends vertical distribution of net tax proceeds between Union & States; horizontal distribution among states", "type": "leaf"},
                            {"label": "Horizontal criteria: Population (Census 2011), forest cover, income distance, area, and demographic performance", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Grants & Advice",
                "type": "branch",
                "date": "Article 275",
                "children": [
                    {
                        "label": "Grants-in-Aid", "type": "sub", "date": "Grants", "children": [
                            {"label": "Recommends principles governing grants-in-aid to states out of Consolidated Fund under Article 275", "type": "leaf"},
                            {"label": "Measures to augment Consolidated Fund of a State to supplement resources of Panchayats & Municipalities", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Advisory Power", "type": "sub", "date": "Recommends", "children": [
                            {"label": "Recommendations are only advisory in nature; Govt not constitutionally bound to implement them, though usually accepted", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 7. NATIONAL COMMISSION FOR SCS / STS
    elif 'scs' in fl or 'sts' in fl:
        return [
            {
                "label": "Constitutional Splitting",
                "type": "branch",
                "date": "Art 338 & 338A",
                "children": [
                    {
                        "label": "NCSC & NCST Setup", "type": "sub", "date": "Bifurcation", "children": [
                            {"label": "89th Constitutional Amendment (2003) bifurcated former joint body into NCSC (Art 338) & NCST (Art 338A)", "type": "leaf"},
                            {"label": "Consists of Chairperson, Vice-Chairperson, and 3 other members appointed by President under warrant", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Duties & Investigation", "type": "sub", "date": "Investigation", "children": [
                            {"label": "Investigates all matters relating to constitutional safeguards for SCs & STs; inquires into specific complaints", "type": "leaf"},
                            {"label": "Participates and advises on planning process of socio-economic development of SCs/STs; submits annual reports", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Civil Court Powers",
                "type": "branch",
                "date": "Judicial Power",
                "children": [
                    {
                        "label": "Judicial Authority", "type": "sub", "date": "Civil Court", "children": [
                            {"label": "Vested with powers of a civil court while investigating complaints (summoning witnesses, requiring documents, receiving affidavit evidence)", "type": "leaf"},
                            {"label": "Union & State Govts must consult the commission on all major policy matters affecting SCs & STs", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 8. SPECIAL OFFICER FOR LINGUISTIC MINORITY
    elif 'linguistic' in fl:
        return [
            {
                "label": "Constitutional Status",
                "type": "branch",
                "date": "Article 350B",
                "children": [
                    {
                        "label": "Linguistic Officer", "type": "sub", "date": "Setup", "children": [
                            {"label": "Created by 7th Constitutional Amendment Act (1956) based on States Reorganisation Commission recommendation", "type": "leaf"},
                            {"label": "Appointed by President of India; designated as Commissioner for Linguistic Minorities with headquarters at Prayagraj", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Duties & Reports", "type": "sub", "date": "Reports", "children": [
                            {"label": "Investigates all matters relating to safeguards provided for linguistic minorities under the Constitution", "type": "leaf"},
                            {"label": "Submits reports to President at designated intervals, which are laid before both Houses of Parliament", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 9. NITI AAYOG
    elif 'niti' in fl:
        return [
            {
                "label": "Cooperative Federalism",
                "type": "branch",
                "date": "Structure",
                "children": [
                    {
                        "label": "Creation & Governing Council", "type": "sub", "date": "Chamber", "children": [
                            {"label": "Extra-constitutional, non-statutory body created via Cabinet Resolution in 2015 to replace Planning Commission", "type": "leaf"},
                            {"label": "Chaired by PM; Governing Council includes all State CMs & UT Lt. Governors to promote cooperative federalism", "type": "leaf"},
                            {"label": "Structure: Vice-Chairperson (appointed by PM), CEO (fixed tenure), full-time members, & ex-officio union ministers", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Policy Think Tank", "type": "sub", "date": "Advice", "children": [
                            {"label": "Acts as a directional and policy think tank; provides strategic & technical advice to Central and State Govts", "type": "leaf"},
                            {"label": "Fosters structured support initiatives and mechanisms with States on a continuous basis, recognizing strong states make a strong nation", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "NITI vs Planning Commission",
                "type": "branch",
                "date": "Differences",
                "children": [
                    {
                        "label": "Key Differences", "type": "sub", "date": "Allocations", "children": [
                            {"label": "NITI adopts bottom-up approach; Planning Commission imposed top-down five-year plans", "type": "leaf"},
                            {"label": "NITI has NO power to allocate funds (done by Finance Ministry); Planning Commission had powers to allocate funds to ministries/states", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 10. NHRC & SHRC & HUMAN RIGHTS
    elif 'nhrc' in fl or 'shrc' in fl or 'human-right' in fl:
        return [
            {
                "label": "NHRC Structure & Mandate",
                "type": "branch",
                "date": "Statutory Status",
                "children": [
                    {
                        "label": "Statutory Origin", "type": "sub", "date": "NHRC", "children": [
                            {"label": "Established under Protection of Human Rights Act 1993; chaired by retired CJI or Supreme Court Judge", "type": "leaf"},
                            {"label": "Selection Committee: Chaired by PM, includes Lok Sabha Speaker, Home Minister, Leaders of Opposition in both houses", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Powers & Limits", "type": "sub", "date": "Limits", "children": [
                            {"label": "Civil court powers; can only recommend compensation; cannot punish violators; recommendations not binding on Govt", "type": "leaf"},
                            {"label": "Armed Forces limitation: Commission has highly restricted powers regarding human rights violations by armed forces", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "SHRC Framework",
                "type": "branch",
                "date": "State Level",
                "children": [
                    {
                        "label": "State Level Setup", "type": "sub", "date": "SHRC", "children": [
                            {"label": "Established at state level; inquires into violations of human rights only in respect of entries in State List & Concurrent List", "type": "leaf"},
                            {"label": "Members appointed by Governor based on committee chaired by State CM, Speaker, & State Home Minister", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 11. CVC (CENTRAL VIGILANCE COMMISSION)
    elif 'cvc' in fl:
        return [
            {
                "label": "Vigilance Setup",
                "type": "branch",
                "date": "CVC Act 2003",
                "children": [
                    {
                        "label": "Statutory Authority", "type": "sub", "date": "Santhanam Committee", "children": [
                            {"label": "Set up in 1964 on Santhanam Committee recommendations; granted statutory status by CVC Act 2003", "type": "leaf"},
                            {"label": "Chaired by Central Vigilance Commissioner + max 2 Vigilance Commissioners; 4 years or 65 years age term", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Superintendence", "type": "sub", "date": "Jurisdiction", "children": [
                            {"label": "Exercises superintendence over functioning of Delhi Special Police Establishment (CBI) for corruption cases", "type": "leaf"},
                            {"label": "Receives complaints under Whistleblowers Protection Act; advises Central Govt on disciplinary proceedings", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 12. CENTRAL / STATE INFORMATION COMMISSION
    elif 'information' in fl or 'cic' in fl or 'sic' in fl:
        return [
            {
                "label": "RTI Mandate",
                "type": "branch",
                "date": "RTI Act 2005",
                "children": [
                    {
                        "label": "Information Commission", "type": "sub", "date": "CIC Structure", "children": [
                            {"label": "Statutory bodies established under Right to Information (RTI) Act 2005; decide appeals on public records", "type": "leaf"},
                            {"label": "CIC appointed by President based on panel of PM, Leader of Opposition in LS, & Union Cabinet Minister", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "State Commission", "type": "sub", "date": "SIC Structure", "children": [
                            {"label": "SIC appointed by Governor based on panel of CM, LoP in Legislative Assembly, & State Cabinet Minister", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 13. LOKPAL AND LOKAYUKTAS
    elif 'lokpal' in fl or 'lokayukta' in fl:
        return [
            {
                "label": "Ombudsman Structure",
                "type": "branch",
                "date": "Act of 2013",
                "children": [
                    {
                        "label": "Lokpal Framework", "type": "sub", "date": "Central", "children": [
                            {"label": "Statutory body established under Lokpal & Lokayuktas Act 2013; Chaired by judicial member + max 8 members", "type": "leaf"},
                            {"label": "Jurisdiction covers Prime Minister, Union Ministers, MPs, and Groups A, B, C, & D federal officers", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Lokayukta Setup", "type": "sub", "date": "State Equivalent", "children": [
                            {"label": "Lokayukta: Equivalent anti-corruption ombudsman established at state levels to investigate state public servants", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 14. ALL INDIA SERVICES
    elif 'all-india-services' in fl:
        return [
            {
                "label": "Constitutional Basis",
                "type": "branch",
                "date": "Article 312",
                "children": [
                    {
                        "label": "Article 312 Resolution", "type": "sub", "date": "Services", "children": [
                            {"label": "Rajya Sabha has exclusive power to create new All-India Services by passing a resolution supported by 2/3rd majority", "type": "leaf"},
                            {"label": "Currently three services: Indian Administrative Service (IAS), Indian Police Service (IPS), and Indian Forest Service (IFS)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Control & Cadre", "type": "sub", "date": "Control Model", "children": [
                            {"label": "Joint control: Recruited & trained by Central Govt (UPSC), but work under respective State cadres", "type": "leaf"},
                            {"label": "Disciplinary action: State Govts can suspend, but ultimate power to dismiss/remove lies with Central Govt (President)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # --- GENERAL FALLBACK (Highly detailed 3-Tier Structure) ---

# Patching Logic


    raise Exception(f"Folder '{folder_name}' has no custom mindmap branch mapped!")

def patch_html(filepath, tree_data, title_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Clean previous mindmap tags to prevent duplicates (using ?v=3 to force cache bypass)
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    mindmap_div_pattern = r'            <!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '<!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    script_pattern = r'    <!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # Re-inject CSS
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    # Re-inject Mindmap Div
    instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand — opening one automatically closes its siblings.'
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
    deep_dive_pattern = r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)'
    if re.search(deep_dive_pattern, html):
        html = re.sub(deep_dive_pattern, mindmap_card + r'\1', html)
    else:
        # Fallback
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

    # Re-inject script with ?v=3 to force reload of wrapping logic
    tree_json = json.dumps(tree_data)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=3"></script>
    <script>
    renderMindmap({tree_json}, undefined, 'en');
    </script>
'''
    html = html.replace('</body>', inline_script + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  Successfully patched: {filepath}")
    return True

# Main execution
def main():
    folders = sorted([f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f))])
    print(f"Found {len(folders)} topics to process.")
    
    for idx, folder in enumerate(folders):
        folder_path = os.path.join(BASE_DIR, folder)
        html_path = os.path.join(folder_path, 'index.html')
        content_path = os.path.join(folder_path, 'content.json')
        
        if not os.path.exists(html_path):
            print(f"[{idx+1}/{len(folders)}] Skipping {folder} (index.html not found)")
            continue
            
        topic_name = get_clean_title(folder)
        if os.path.exists(content_path):
            try:
                with open(content_path, 'r', encoding='utf-8') as f:
                    content_data = json.load(f)
                    topic_name = content_data.get('hero', {}).get('title', topic_name)
            except Exception:
                pass
        
        # Build custom, 3-tier deep-dive topic-specific mindmap data
        branches = get_custom_branches(folder)
        mindmap_data = {
            "label": get_clean_title(folder),
            "type": "root",
            "children": branches
        }
        
        title_text = f"{topic_name} &mdash; Interactive Mindmap"
        success = patch_html(html_path, mindmap_data, title_text)
        if success:
            print(f"[{idx+1}/{len(folders)}] Processed {folder}")
        else:
            print(f"[{idx+1}/{len(folders)}] Failed to patch {folder}")

if __name__ == '__main__':
    main()

def patch_html(filepath, tree_data, title_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Clean previous mindmap tags to prevent duplicates (using ?v=3 to force cache bypass)
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    mindmap_div_pattern = r'            <!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '<!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    script_pattern = r'    <!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # Re-inject CSS
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    # Re-inject Mindmap Div
    instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand — opening one automatically closes its siblings.'
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
    deep_dive_pattern = r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)'
    if re.search(deep_dive_pattern, html):
        html = re.sub(deep_dive_pattern, mindmap_card + r'\1', html)
    else:
        # Fallback
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

    # Re-inject script with ?v=3 to force reload of wrapping logic
    tree_json = json.dumps(tree_data)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=3"></script>
    <script>
    renderMindmap({tree_json}, undefined, 'en');
    </script>
'''
    html = html.replace('</body>', inline_script + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  Successfully patched: {filepath}")
    return True

# Main execution
def main():
    folders = sorted([f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f))])
    print(f"Found {len(folders)} topics to process.")
    
    for idx, folder in enumerate(folders):
        folder_path = os.path.join(BASE_DIR, folder)
        html_path = os.path.join(folder_path, 'index.html')
        content_path = os.path.join(folder_path, 'content.json')
        
        if not os.path.exists(html_path):
            print(f"[{idx+1}/{len(folders)}] Skipping {folder} (index.html not found)")
            continue
            
        topic_name = get_clean_title(folder)
        if os.path.exists(content_path):
            try:
                with open(content_path, 'r', encoding='utf-8') as f:
                    content_data = json.load(f)
                    topic_name = content_data.get('hero', {}).get('title', topic_name)
            except Exception:
                pass
        
        # Build custom, 3-tier deep-dive topic-specific mindmap data
        branches = get_custom_branches(folder)
        mindmap_data = {
            "label": get_clean_title(folder),
            "type": "root",
            "children": branches
        }
        
        title_text = f"{topic_name} &mdash; Interactive Mindmap"
        success = patch_html(html_path, mindmap_data, title_text)
        if success:
            print(f"[{idx+1}/{len(folders)}] Processed {folder}")
        else:
            print(f"[{idx+1}/{len(folders)}] Failed to patch {folder}")

if __name__ == '__main__':
    main()

