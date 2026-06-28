import os
import re
import json

BASE_DIR = r"upsc/polity/Governance-Welfare-Schemes"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'psu', 'psus', 'shg', 'shgs', 'ngo', 'ngos', 'fcra', 'spv', 'dbt', 'jam', 'uidai', 'upi', 'pmksy', ' SSA', 'rmsa', 'nep', 'pm', 'jay', 'nhm', 'nrhm', 'nuhm', 'mmr', 'sym', 'apy', 'pmay', 'mgnrega', 'nrlm', 'nulm', 'nfsa', 'pmmvy', 'cag', 'cvc', 'pac'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# 3-Tier Deep-Dive Mappings for Governance and Welfare Schemes
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. Structure of Ministries/Departments
    if 'ministries' in fl or 'departments' in fl:
        return [
            {
                "label": "Organizational Hierarchy",
                "type": "branch",
                "date": "Administrative Setup",
                "children": [
                    {
                        "label": "Political vs Administrative", "type": "sub", "date": "Heads", "children": [
                            {"label": "Minister (Political Head, policy direction) -> Secretary (Administrative Head, IAS officer, implementation)", "type": "leaf"},
                            {"label": "Hierarchical flow: Secretary -> Additional Secretary -> Joint Secretary (runs a Wing) -> Director", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Internal Units", "type": "sub", "date": "Departments", "children": [
                            {"label": "Organized systematically into Wings, Divisions, Branches, and Sections (the lowest organizational unit)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. Secretariat vs Executive Offices
    elif 'secretariat' in fl or 'attached' in fl or 'subordinate' in fl or 'executive-organization' in fl:
        return [
            {
                "label": "Secretariat Role",
                "type": "branch",
                "date": "Policy Agency",
                "children": [
                    {
                        "label": "Policy & Staffing", "type": "sub", "date": "Staff", "children": [
                            {"label": "Secretariat is the staff agency; focuses on policy formulation, drafting legislation, budgeting, and performance evaluation", "type": "leaf"},
                            {"label": "Protects ministers from routine administrative details, ensuring objective evaluation of field projects", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Executive Agencies",
                "type": "branch",
                "date": "Line Agencies",
                "children": [
                    {
                        "label": "Attached vs Subordinate", "type": "sub", "date": "Execution", "children": [
                            {"label": "Attached Offices: Provide technical advice and detailed data to the ministry (e.g., DGCA, CPWD)", "type": "leaf"},
                            {"label": "Subordinate Offices: Field execution agencies; execute policies at local grassroot levels (e.g., passport offices)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. PSUs
    elif 'public-sector' in fl or 'undertaking' in fl:
        return [
            {
                "label": "Autonomy Categories",
                "type": "branch",
                "date": "PSU Tiers",
                "children": [
                    {
                        "label": "Maharatna & Navratna", "type": "sub", "date": "Autonomy", "children": [
                            {"label": "Maharatna: TIER 1 autonomy; can invest up to Rs 5,000 crore in single project without Govt permission (e.g., NTPC, ONGC)", "type": "leaf"},
                            {"label": "Navratna: TIER 2 autonomy; can invest up to Rs 1,000 crore without permission; Miniratna Category I/II have lower limits", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Disinvestment Tiers",
                "type": "branch",
                "date": "Capital Raising",
                "children": [
                    {
                        "label": "Capital Raising Models", "type": "sub", "date": "Disinvestment", "children": [
                            {"label": "Minority Disinvestment: Govt retains 51%+ shareholding control; Strategic Disinvestment: selling 50%+ and transfer of management control", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. Improvements & Reforms
    elif 'recommendations' in fl or 'strengths' in fl or 'weaknesses' in fl or 'governing-institutions' in fl or 'organization' in fl:
        return [
            {
                "label": "Weaknesses & Reforms",
                "type": "branch",
                "date": "Administrative Reforms",
                "children": [
                    {
                        "label": "Structural Defects", "type": "sub", "date": "Defects", "children": [
                            {"label": "Red-tapism, bureaucratic inertia, lack of specialization, over-centralization of decision making, and fragmented departments", "type": "leaf"},
                            {"label": "First Administrative Reforms Commission (ARC - 1966) & Second ARC (2005): Recommended delegation of power, citizen charters", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Structural Improvements", "type": "sub", "date": "Solutions", "children": [
                            {"label": "Implementation of e-Office systems, lateral entry of domain experts at Joint Secretary levels, and restructuring ministries", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. SHG, NGOs, Civil Society
    elif 'shg' in fl or 'ngo' in fl or 'civil-society' in fl:
        return [
            {
                "label": "Self Help Groups (SHGs)",
                "type": "branch",
                "date": "SHG Linkage",
                "children": [
                    {
                        "label": "Microfinance & Empowerment", "type": "sub", "date": "NABARD", "children": [
                            {"label": "SHG-Bank Linkage Program (NABARD): Promotes micro-credit, thrift, and financial inclusion among rural women", "type": "leaf"},
                            {"label": "Kudumbashree (Kerala) & JEEViKA (Bihar): Successful models of community mobilization and poverty alleviation", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "NGOs & Civil Society",
                "type": "branch",
                "date": "Advocacy",
                "children": [
                    {
                        "label": "Social Audits & Regulation", "type": "sub", "date": "FCRA", "children": [
                            {"label": "NGOs act as pressure groups and fill delivery gaps; participate in social auditing of welfare programs (e.g., MGNREGA)", "type": "leaf"},
                            {"label": "FCRA (Foreign Contribution Regulation Act) compliance mandatory; checks foreign funding transparency and checks subversion", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. Smart Cities
    elif 'smart-cities' in fl:
        return [
            {
                "label": "Core Features",
                "type": "branch",
                "date": "Urban Development",
                "children": [
                    {
                        "label": "Execution Pillars", "type": "sub", "date": "Smart Cities", "children": [
                            {"label": "Launched in 2015 under Ministry of Housing and Urban Affairs; target of developing 100 cities into smart cities", "type": "leaf"},
                            {"label": "Key components: Area-based development (retrofitting, redevelopment, greenfield) & Pan-city smart solutions", "type": "leaf"},
                            {"label": "SPV (Special Purpose Vehicle): Created for each city to plan, appraise, release funds, and implement projects", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 7. Digital India
    elif 'digital-india' in fl:
        return [
            {
                "label": "Digital Platforms",
                "type": "branch",
                "date": "Technology",
                "children": [
                    {
                        "label": "E-Governance Services", "type": "sub", "date": "Digital Welfare", "children": [
                            {"label": "Aadhaar (UIDAI) forms the bedrock of JAM trinity (Jan Dhan-Aadhaar-Mobile) for Direct Benefit Transfer (DBT)", "type": "leaf"},
                            {"label": "BharatNet: Connecting 2.5 lakh gram panchayats via high-speed optical fiber network; PM WANI for public Wi-Fi", "type": "leaf"},
                            {"label": "DigiLocker, UMANG app, UPI digital payment infrastructure, and NeGD (National e-Governance Division) coordinating role", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 8. Disability
    elif 'disability' in fl:
        return [
            {
                "label": "Legal & Schemes",
                "type": "branch",
                "date": "Divyangjan Welfare",
                "children": [
                    {
                        "label": "Rights & Accessibility", "type": "sub", "date": "RPwD Act 2016", "children": [
                            {"label": "RPwD Act 2016: Increases reservation in higher education (to 5%) & public employment (to 4%); lists 21 disabilities", "type": "leaf"},
                            {"label": "Accessible India Campaign (Sugamya Bharat Abhiyan): Enhancing accessibility of built environment, transport, & ICT", "type": "leaf"},
                            {"label": "Deendayal Disabled Rehabilitation Scheme (DDRS): Financial assistance to NGOs providing vocational training and schools", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 9. Education
    elif 'education' in fl:
        return [
            {
                "label": "Primary & Secondary Education",
                "type": "branch",
                "date": "Human Capital",
                "children": [
                    {
                        "label": "Universal Access & Food", "type": "sub", "date": "Education", "children": [
                            {"label": "Samagra Shiksha Abhiyan: Integrates Sarva Shiksha Abhiyan (SSA), Rashtriya Madhyamik (RMSA), and Teacher Education", "type": "leaf"},
                            {"label": "PM POSHAN (MDM): Hot cooked meals; addresses classroom hunger and improves school nutritional outcomes", "type": "leaf"},
                            {"label": "National Education Policy (NEP) 2020: Target of 100% Gross Enrolment Ratio in school education by 2030", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 10. Health
    elif 'health' in fl:
        return [
            {
                "label": "Universal Health Insurance",
                "type": "branch",
                "date": "Public Health",
                "children": [
                    {
                        "label": "PM-JAY & Health Centers", "type": "sub", "date": "Ayushman Bharat", "children": [
                            {"label": "Ayushman Bharat PM-JAY: Health cover of Rs 5 lakh per family per year for secondary/tertiary hospitalization (~50 crore beneficiaries)", "type": "leaf"},
                            {"label": "Health & Wellness Centers (HWCs): Upgrading primary health sub-centers for comprehensive primary care & diagnostic tests", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "National Health Mission (NHM)", "type": "sub", "date": "Missions", "children": [
                            {"label": "Sub-missions: National Rural Health Mission (NRHM) & Urban Health Mission (NUHM); strengthens health systems", "type": "leaf"},
                            {"label": "Janani Suraksha Yojana (JSY): Cash incentives to promote institutional delivery and reduce Maternal Mortality Rate (MMR)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 11. Inclusive Growth & Social Security
    elif 'inclusive' in fl or 'social-security' in fl:
        return [
            {
                "label": "Unorganized Sector Schemes",
                "type": "branch",
                "date": "Social Security",
                "children": [
                    {
                        "label": "Pensions & Insurance", "type": "sub", "date": "Schemes", "children": [
                            {"label": "PM Shram Yogi Maan-dhan (PM-SYM): Voluntary pension scheme for unorganized workers; monthly Rs 3,000 post 60 age", "type": "leaf"},
                            {"label": "PM Suraksha Bima Yojana (Accident Insurance, Rs 2 lakh cover) & PM Jeevan Jyoti Bima Yojana (Life Insurance)", "type": "leaf"},
                            {"label": "Atal Pension Yojana (APY): Channeled towards unorganized workers; guaranteed minimum pension return", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 12. Rural & Urban Development
    elif 'rural' in fl or 'urban' in fl:
        return [
            {
                "label": "Rural & Urban Housing",
                "type": "branch",
                "date": "Welfare Development",
                "children": [
                    {
                        "label": "PMAY & MGNREGA", "type": "sub", "date": "Shelter & Jobs", "children": [
                            {"label": "PMAY-Gramin (Ministry of Rural Development) & PMAY-Urban (MoHUA); credit-linked subsidy scheme for affordable housing", "type": "leaf"},
                            {"label": "MGNREGA 2005: Legal guarantee of 100 days of unskilled manual work per financial year to rural households", "type": "leaf"},
                            {"label": "Deendayal Antyodaya Yojana - NRLM/NULM: Skill development and micro-enterprises support for urban/rural poor", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 13. Vulnerable Sectors
    elif 'vulnerable' in fl:
        return [
            {
                "label": "Targeted Upliftment",
                "type": "branch",
                "date": "Vulnerable Groups",
                "children": [
                    {
                        "label": "Scheduled Castes & Tribes", "type": "sub", "date": "Vulnerable", "children": [
                            {"label": "PM ADY (Adarsh Gram Yojana) for tribal development; Stand-Up India scheme facilitating SC/ST/Women entrepreneurs", "type": "leaf"},
                            {"label": "PM Garib Kalyan Anna Yojana (PMGKAY): Free foodgrains (5kg/person/month) to NFSA beneficiaries", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 14. Women & Child
    elif 'women' in fl or 'child' in fl:
        return [
            {
                "label": "Maternal & Child Health",
                "type": "branch",
                "date": "Human Development",
                "children": [
                    {
                        "label": "PMMVY & Poshan", "type": "sub", "date": "Nutrition", "children": [
                            {"label": "PM Matru Vandana Yojana (PMMVY): Direct benefit transfer (DBT) of Rs 5,000 to pregnant women for first child nutrition", "type": "leaf"},
                            {"label": "Poshan Abhiyaan (National Nutrition Mission): Aims to reduce stunting, wasting, anemia, and low birth weight in children", "type": "leaf"},
                            {"label": "Beti Bachao Beti Padhao: Focuses on declining child sex ratio, promoting education and welfare of girls", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 15. Audit & Transparency
    elif 'audit' in fl or 'cag' in fl or 'cvc' in fl or 'lokpal' in fl or 'lokayukta' in fl:
        return [
            {
                "label": "Audit & Transparency",
                "type": "branch",
                "date": "Institutions",
                "children": [
                    {
                        "label": "Anti-Graft Panels", "type": "sub", "date": "Anti-Corruption", "children": [
                            {"label": "CAG: Audits public accounts to ensure transparency and accountability; reports analyzed by Public Accounts Committee (PAC)", "type": "leaf"},
                            {"label": "CVC: Statutory body; advises Govt on vigilance cases; superintendence over CBI corruption probes", "type": "leaf"},
                            {"label": "Lokpal & Lokayukta Act 2013: Ombudsman to investigate corruption complaints against public servants (including PM/Ministers)", "type": "leaf"}
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

