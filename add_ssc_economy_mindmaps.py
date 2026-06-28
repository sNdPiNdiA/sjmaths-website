import os
import re
import json

BASE_DIR = r"ssc-cgl/general-awareness/economic-scene-economy"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'frs', 'fds', 'nri', 'pio', 'oci', 'caa', 'src', 'jvp', 'ist', 'gmt', 'utc', 'uv', 'co2', 'tisco', 'jnpt', 'cag', 'niti', 'upsc', 'spsc', 'nhrc', 'cic', 'cvc', 'sc', 'st', 'obc', 'dpsp', 'vp', 'pm', 'amtm', 'hc', 'gdp', 'gnp', 'ndp', 'nnp', 'nfia', 'pdi', 'gva', 'cso', 'nso', 'fyp', 'ndc', 'rbi', 'crr', 'slr', 'msf', 'omo', 'npa', 'ibc', 'mat', 'frbm', 'msme', 'lpg', 'fdi', 'fii', 'psu', 'bop', 'cacp', 'msp', 'frp'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs', 'outside', 'between', 'or', 'life', 'major', 'era', 'sects', 'teachings', 'councils', 'findings', 'trade', 'sites', 'rig', 'later']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Complete detailed mindmaps for all 5 CGL Economy folders
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. NATIONAL INCOME: GDP, GNP, NDP, NNP CONCEPTS & CALCULATION
    if 'national-income-gdp' in fl:
        return [
            {
                "label": "Core Aggregates", "type": "branch", "date": "Aggregates",
                "children": [
                    {
                        "label": "GDP & NDP", "type": "sub", "date": "Domestic Product",
                        "children": [
                            {"label": "GDP: Total market value of all final goods and services produced within domestic territory in a year; focus is boundary", "type": "leaf"},
                            {"label": "NDP: GDP minus Depreciation (wear and tear of capital assets); shows actual net domestic value", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "GNP & NNP", "type": "sub", "date": "National Product",
                        "children": [
                            {"label": "GNP: GDP plus Net Factor Income from Abroad (NFIA); focus is nationality of producers", "type": "leaf"},
                            {"label": "NNP: GNP minus Depreciation; NNP at Factor Cost (NNP_FC) is equal to National Income", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Pricing & Measurements", "type": "branch", "date": "Valuation",
                "children": [
                    {
                        "label": "Factor Cost vs Market Price", "type": "sub", "date": "Pricing",
                        "children": [
                            {"label": "Market Price (MP) = Factor Cost (FC) + Net Indirect Taxes (Indirect Taxes - Subsidies)", "type": "leaf"},
                            {"label": "Nominal GDP: Calculated at current prices; Real GDP: Calculated at base year prices (current base year 2011-12)", "type": "leaf"},
                            {"label": "GDP Deflator: Ratio of Nominal GDP to Real GDP multiplied by 100; measures price inflation level", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Income Aggregates", "type": "sub", "date": "Personal Income",
                        "children": [
                            {"label": "Personal Income (PI): National Income minus undistributed profits, corporate taxes, net interest plus transfer payments", "type": "leaf"},
                            {"label": "Personal Disposable Income (PDI): Personal Income minus direct taxes and fees/fines", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Methods & History", "type": "branch", "date": "Calculation",
                "children": [
                    {
                        "label": "Three Calculation Methods", "type": "sub", "date": "Methods",
                        "children": [
                            {"label": "Product Method (GVA): Value of Output minus Intermediate Consumption; Income Method: Wages + Rent + Interest + Profit", "type": "leaf"},
                            {"label": "Expenditure Method: Private Consumption (C) + Govt Expenditure (G) + Investment (I) + Net Exports (X-M)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Historical Milestones", "type": "sub", "date": "History",
                        "children": [
                            {"label": "Dadabhai Naoroji (1867-68): First estimate in 'Poverty & Un-British Rule in India'; per capita Rs 20", "type": "leaf"},
                            {"label": "V.K.R.V. Rao (1931-32): First scientific estimate; CSO (now NSO) calculates it currently in India", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. ECONOMIC PLANNING: FIVE YEAR PLANS HISTORY & NITI AAYOG STRUCTURE
    elif 'economic-planning-five' in fl:
        return [
            {
                "label": "Early Plans & Planning Commission", "type": "branch", "date": "Pre-1951 Planning",
                "children": [
                    {
                        "label": "Planning Milestones", "type": "sub", "date": "Milestones",
                        "children": [
                            {"label": "Visvesvaraya Plan (1934): 10-year plan in 'Planned Economy for India'; National Planning Committee (1938) chaired by Nehru", "type": "leaf"},
                            {"label": "Bombay Plan (1944) by industrialists; People's Plan (1945) by M.N. Roy; Gandhian (1944); Sarvodaya Plan (1950) by J.P. Narayan", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Planning Commission Setup", "type": "sub", "date": "Commission",
                        "children": [
                            {"label": "Planning Commission: March 15, 1950 by executive resolution; advisory; PM is chairman; National Development Council (1952) approves plans", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Five Year Plans (1st to 12th Plan)", "type": "branch", "date": "Plans Chronology",
                "children": [
                    {
                        "label": "Plans 1 to 4", "type": "sub", "date": "1951 - 1974",
                        "children": [
                            {"label": "First Plan (1951-56): Harrod-Domar model; agriculture & dams focus; Second Plan (1956-61): Nehru-Mahalanobis model; heavy industries focus", "type": "leaf"},
                            {"label": "Third Plan (1961-66): Self-reliance; failed due to Sino-Indian (1962), Indo-Pak (1965) wars; followed by Plan Holidays (1966-69)", "type": "leaf"},
                            {"label": "Fourth Plan (1969-74): Growth with stability; nationalization of 14 banks (1969), Green Revolution peak", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Plans 5 to 12", "type": "sub", "date": "1974 - 2017",
                        "children": [
                            {"label": "Fifth Plan (1974-79): Slogan 'Garibi Hatao'; terminated early; Sixth Plan (1980-85): Family planning, NABARD (1982)", "type": "leaf"},
                            {"label": "Seventh Plan (1985-90): Food work and productivity; Annual Plans (1990-92) due to balance of payments crisis", "type": "leaf"},
                            {"label": "Eighth Plan (1992-97): Rao-Manmohan model, economic reforms (LPG); Tenth Plan: Double per capita income", "type": "leaf"},
                            {"label": "Eleventh Plan (2007-12): Inclusive growth; Twelfth Plan (2012-17): Faster, sustainable and more inclusive (last FYP)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "NITI Aayog", "type": "branch", "date": "Cooperative Federalism",
                "children": [
                    {
                        "label": "NITI Structure", "type": "sub", "date": "Setup",
                        "children": [
                            {"label": "Formed Jan 1, 2015 replacing Planning Commission; policy think-tank; bottom-up planning model", "type": "leaf"},
                            {"label": "Governing Council: PM as Chairperson, Vice-Chairperson, CEO, Chief Ministers of all states, and Lt Governors of UTs", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. MONEY, INFLATION, RBI, MONETARY TOOLS, BANKING SYSTEM & NPAs
    elif 'money-inflation' in fl:
        return [
            {
                "label": "Money Supply & Inflation", "type": "branch", "date": "Monetary Core",
                "children": [
                    {
                        "label": "Money Supply aggregates", "type": "sub", "date": "Aggregates",
                        "children": [
                            {"label": "M1 (Narrow Money) = Currency with public + Demand deposits + Other deposits with RBI; M2 = M1 + Post office savings", "type": "leaf"},
                            {"label": "M3 (Broad Money) = M1 + Time deposits with banks; M4 = M3 + Total post office deposits", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Inflation Types & Measures", "type": "sub", "date": "Inflation",
                        "children": [
                            {"label": "Demand-Pull (excess demand) vs. Cost-Push (rising costs); Stagflation: High inflation + low growth + high unemployment", "type": "leaf"},
                            {"label": "Wholesale Price Index (WPI) vs. Consumer Price Index (CPI); CPI is RBI's key tool for inflation targeting (4% +/- 2%)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "RBI & Monetary Policy Tools", "type": "branch", "date": "RBI Tools",
                "children": [
                    {
                        "label": "RBI Setup", "type": "sub", "date": "Reserve Bank",
                        "children": [
                            {"label": "Established April 1, 1935 on Hilton Young Commission recommendation; nationalized Jan 1, 1949", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Quantitative Policy Tools", "type": "sub", "date": "Quantitative",
                        "children": [
                            {"label": "Cash Reserve Ratio (CRR): Cash reserves kept with RBI; Statutory Liquidity Ratio (SLR): Liquid assets kept with self", "type": "leaf"},
                            {"label": "Repo Rate: Short-term lending rate to banks; Reverse Repo: Borrowing rate from banks; Bank Rate: Long-term rate without collateral", "type": "leaf"},
                            {"label": "Open Market Operations (OMO): Buying/selling government securities in market to regulate cash flow", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Banking History & NPAs", "type": "branch", "date": "Banking Reforms",
                "children": [
                    {
                        "label": "Nationalization & NPAs", "type": "sub", "date": "NPAs",
                        "children": [
                            {"label": "Nationalization: 14 banks in 1969, 6 banks in 1980; Non-Performing Assets (NPAs): Loans outstanding for more than 90 days", "type": "leaf"},
                            {"label": "Reforms: Insolvency and Bankruptcy Code (IBC 2016), SARFAESI Act (2002), NARCL (Bad Bank), Basel III norms", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. PUBLIC FINANCE, TAXATION SYSTEM, GST, UNION BUDGET & DEFICITS
    elif 'public-finance' in fl:
        return [
            {
                "label": "Taxation System in India", "type": "branch", "date": "Taxation",
                "children": [
                    {
                        "label": "Direct vs Indirect Taxes", "type": "sub", "date": "Taxes",
                        "children": [
                            {"label": "Direct (incidence/impact on same person): Income Tax, Corporate Tax, Capital Gains Tax, MAT", "type": "leaf"},
                            {"label": "Indirect (incidence shifted): Excise duty, Custom duty, Service tax (mostly merged into GST)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "GST Framework", "type": "sub", "date": "GST",
                        "children": [
                            {"label": "101st Amendment Act 2016; implemented July 1, 2017; GST Council (Art 279A) chaired by Union Finance Minister", "type": "leaf"},
                            {"label": "Slabs: 0%, 5%, 12%, 18%, 28%; petroleum, alcohol, electricity kept outside GST purview", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Union Budget & Accounts", "type": "branch", "date": "Fiscal Budget",
                "children": [
                    {
                        "label": "Budget Presentation", "type": "sub", "date": "Annual Statement",
                        "children": [
                            {"label": "Presented Feb 1; Article 112 calls it 'Annual Financial Statement'; Railway Budget merged in 2017 (Debroy committee)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Government Accounts", "type": "sub", "date": "Accounts",
                        "children": [
                            {"label": "Consolidated Fund of India (Art 266(1)): All revenues; Public Account (Art 266(2)): PF; Contingency Fund (Art 267)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Deficit Metrics & Rules", "type": "branch", "date": "Deficits",
                "children": [
                    {
                        "label": "Budget Deficits", "type": "sub", "date": "Deficits",
                        "children": [
                            {"label": "Revenue Deficit = Revenue Expenditure - Revenue Receipts; Fiscal Deficit: Total borrowing needs of government", "type": "leaf"},
                            {"label": "Primary Deficit = Fiscal Deficit - Interest Payments; FRBM Act (2003): Aimed to limit fiscal deficit to 3% of GDP", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. SECTORS, REFORMS, AGRICULTURE, MSMEs, & LPG REFORMS SINCE 1991
    elif 'sectors-reforms' in fl:
        return [
            {
                "label": "Economic Sectors", "type": "branch", "date": "Sectors",
                "children": [
                    {
                        "label": "Primary, Secondary, Tertiary", "type": "sub", "date": "Activity",
                        "children": [
                            {"label": "Primary: Agriculture, Mining, Fishing; contributes ~18% to GDP but employs ~45% population", "type": "leaf"},
                            {"label": "Secondary: Manufacturing, Construction; Industrial Policy Resolution 1956 is the economic constitution", "type": "leaf"},
                            {"label": "Tertiary: Services, Banking, IT; largest contributor to India's GDP (~55% GVA share)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Agriculture & MSME Frameworks", "type": "branch", "date": "Sectors Detail",
                "children": [
                    {
                        "label": "Agricultural Policies", "type": "sub", "date": "Agriculture",
                        "children": [
                            {"label": "Minimum Support Price (MSP): Mandated for 22 crops + FRP for Sugarcane on CACP recommendations", "type": "leaf"},
                            {"label": "Land Reforms: Zamindari abolition, tenancy reforms, ceilings on landholdings, consolidation of holdings", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "MSMEs Definition", "type": "sub", "date": "MSME",
                        "children": [
                            {"label": "Micro: Investment <= Rs 1 cr, Turnover <= Rs 5 cr; Small: Investment <= Rs 10 cr, Turnover <= Rs 50 cr; Medium: Investment <= Rs 50 cr, Turnover <= Rs 250 cr (revised 2020)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "1991 LPG Reforms", "type": "branch", "date": "LPG reforms",
                "children": [
                    {
                        "label": "BoP Crisis & LPG Response", "type": "sub", "date": "1991 Reforms",
                        "children": [
                            {"label": "Balance of Payments (BoP) crisis in 1991 led to Rao-Manmohan reforms; Liberalization: Abolished licensing", "type": "leaf"},
                            {"label": "Privatization: Disinvestment of public sector undertakings (PSUs); Globalization: Tariff cuts, opening up to FDI/FII", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    raise Exception(f"Folder '{folder_name}' has no custom mindmap branch mapped!")

# Patching Logic
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
    # We find "id="traps-section"" to inject the mindmap card after it
    if 'id="traps-section"' in html:
        pos = html.find('id="traps-section"')
        end_div = html.find('</div>', pos)
        if end_div != -1:
            insert_pos = end_div + len('</div>')
            html = html[:insert_pos] + "\n" + mindmap_card + "\n" + html[insert_pos:]
    elif '<!-- Prep Tracker -->' in html:
        html = html.replace('<!-- Prep Tracker -->', mindmap_card + '\n<!-- Prep Tracker -->', 1)
    else:
        # Fallback to checklist
        pos = html.find('Self-Evaluation Checklist')
        if pos != -1:
            card_pos = html.rfind('<div class="card-premium">', 0, pos)
            if card_pos != -1:
                html = html[:card_pos] + mindmap_card + "\n" + html[card_pos:]

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
