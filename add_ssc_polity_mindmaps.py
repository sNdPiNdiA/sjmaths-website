import os
import re
import json

BASE_DIR = r"ssc-cgl/general-awareness/general-policy-polity"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'frs', 'fds', 'nri', 'pio', 'oci', 'caa', 'src', 'jvp', 'ist', 'gmt', 'utc', 'uv', 'co2', 'tisco', 'jnpt', 'cag', 'niti', 'upsc', 'spsc', 'nhrc', 'cic', 'cvc', 'sc', 'st', 'obc', 'dpsp', 'vp', 'pm', 'amtm', 'hc'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs', 'outside', 'between', 'or', 'life', 'major', 'era', 'sects', 'teachings', 'councils', 'findings', 'trade', 'sites', 'rig', 'later']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Complete detailed mindmaps for all 6 CGL Polity folders
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. MAKING OF CONSTITUTION, PREAMBLE, SOURCES, PARTS & SCHEDULES
    if 'making-of-constitution' in fl:
        return [
            {
                "label": "Making & Constituent Assembly", "type": "branch", "date": "1946 - 1950",
                "children": [
                    {
                        "label": "Assembly Formation & Timeline", "type": "sub", "date": "Chronology",
                        "children": [
                            {"label": "Formed under Cabinet Mission Plan (Nov 1946); total strength 389 (296 British India, 93 Princely States); first meeting Dec 9, 1946", "type": "leaf"},
                            {"label": "Permanent President: Dr. Rajendra Prasad (elected Dec 11, 1946); Vice President: H.C. Mukherjee; Advisor: B.N. Rau", "type": "leaf"},
                            {"label": "Objective Resolution: Moved by Nehru on Dec 13, 1946 (unanimously adopted Jan 22, 1947; became Preamble basis)", "type": "leaf"},
                            {"label": "Completion: Taken 2 years, 11 months, and 18 days; adopted Nov 26, 1949; came into force Jan 26, 1950", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Drafting Committee & Officers", "type": "sub", "date": "Committees",
                        "children": [
                            {"label": "Drafting Committee (set up Aug 29, 1947): 7 members chaired by Dr. B.R. Ambedkar (Father of Constitution)", "type": "leaf"},
                            {"label": "Union Powers/Union Constitution: J.L. Nehru; Provincial Constitution: Vallabhbhai Patel; Steering: Rajendra Prasad", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Preamble & Sources", "type": "branch", "date": "Foundations",
                "children": [
                    {
                        "label": "Preamble Features", "type": "sub", "date": "Preamble",
                        "children": [
                            {"label": "Nature of State: Sovereign, Socialist, Secular, Democratic, Republic; Objectives: Justice, Liberty, Equality, Fraternity", "type": "leaf"},
                            {"label": "42nd Amendment (1976): Added three words: 'Socialist', 'Secular', and 'Integrity' to Preamble", "type": "leaf"},
                            {"label": "Legal Status: Kesavananda Bharati (1973) held Preamble is a part of the Constitution and can be amended under Article 368", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Borrowed Sources", "type": "sub", "date": "Foreign Influence",
                        "children": [
                            {"label": "UK: Parliamentary system, Rule of Law, single citizenship, bicameralism, legislative procedure, writs", "type": "leaf"},
                            {"label": "USA: Fundamental Rights, Judicial Review, written Constitution, impeachment of President, removal of SC/HC judges", "type": "leaf"},
                            {"label": "Ireland: DPSP, nomination of members to Rajya Sabha, method of Presidential election; Australia: Concurrent List, Joint Sitting", "type": "leaf"},
                            {"label": "Canada: Strong federation, residual powers; Germany: Emergency provisions; USSR: Fundamental Duties; Japan: Procedure established by law", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Parts & Schedules", "type": "branch", "date": "Constitutional Structure",
                "children": [
                    {
                        "label": "Key Parts", "type": "sub", "date": "Parts",
                        "children": [
                            {"label": "Part I: Union/Territory (Art 1-4); Part II: Citizenship (Art 5-11); Part III: Fundamental Rights (Art 12-35)", "type": "leaf"},
                            {"label": "Part IV: DPSP (Art 36-51); Part IV-A: Fundamental Duties (Art 51A); Part V: Union (Art 52-151); Part VI: States (Art 152-237)", "type": "leaf"},
                            {"label": "Part IX: Panchayats (Art 243-243O); Part XV: Elections (Art 324-329); Part XX: Constitutional Amendments (Art 368)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Schedules (1 to 12)", "type": "sub", "date": "Schedules",
                        "children": [
                            {"label": "Schedules 1-4: States/UTs boundaries, salaries/emoluments, oaths/affirmations, allocation of Rajya Sabha seats", "type": "leaf"},
                            {"label": "Schedules 5-8: Scheduled areas, tribal areas (Assam, Meghalaya, Tripura, Mizoram), Seventh Schedule list division, 22 official languages", "type": "leaf"},
                            {"label": "Schedules 9-12: Land reforms (1st Amend 1951), Anti-defection (52nd Amend 1985), Panchayats (73rd Amend), Municipalities (74th Amend)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. FUNDAMENTAL RIGHTS, FUNDAMENTAL DUTIES & DPSP
    elif 'fundamental-rights' in fl:
        return [
            {
                "label": "Fundamental Rights (Articles 12-35)", "type": "branch", "date": "Part III",
                "children": [
                    {
                        "label": "Equality & Freedom (Art 14-22)", "type": "sub", "date": "Core Rights",
                        "children": [
                            {"label": "Right to Equality: Art 14 (Equality before law), Art 15 (No discrimination), Art 16 (Equal employment), Art 17 (Untouchability), Art 18 (Titles)", "type": "leaf"},
                            {"label": "Right to Freedom: Art 19 (Six democratic freedoms), Art 20 (Double jeopardy/self-incrimination protection), Art 21 (Life & personal liberty), Art 21A (Education)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Exploitation, Religion & Minorities (Art 23-30)", "type": "sub", "date": "Socio-Religious",
                        "children": [
                            {"label": "Exploitation: Art 23 (Trafficking/forced labor ban), Art 24 (hazardous child labor ban under 14 years)", "type": "leaf"},
                            {"label": "Religion: Art 25-28 (Freedom of conscience, profession, practice, propagation, management of religious affairs)", "type": "leaf"},
                            {"label": "Minorities: Art 29 (Language/culture protection), Art 30 (Establishment of educational institutions)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Constitutional Remedies & Writs (Art 32)", "type": "sub", "date": "Remedies",
                        "children": [
                            {"label": "Article 32: Heart and Soul (Ambedkar); allows filing petitions directly in Supreme Court for FR enforcement", "type": "leaf"},
                            {"label": "Writs: Habeas Corpus (release illegal detainee), Mandamus (perform public duty), Prohibition (lower court stop), Certiorari (quash order), Quo Warranto (by what authority)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Directive Principles of State Policy (Articles 36-51)", "type": "branch", "date": "Part IV",
                "children": [
                    {
                        "label": "Nature & Features", "type": "sub", "date": "DPSP",
                        "children": [
                            {"label": "Borrowed from Ireland; non-justiciable (Article 37); aim to establish economic democracy and a welfare state", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Classifications", "type": "sub", "date": "Categories",
                        "children": [
                            {"label": "Socialistic: Art 38 (minimize inequality), Art 39 (equal pay), Art 39A (free legal aid), Art 41 (right to work/public assistance)", "type": "leaf"},
                            {"label": "Gandhian: Art 40 (Village Panchayats), Art 43 (cottage industries), Art 46 (SC/ST interests), Art 47 (liquor ban), Art 48 (cow slaughter ban)", "type": "leaf"},
                            {"label": "Liberal-Intellectual: Art 44 (Uniform Civil Code), Art 45 (early education), Art 48A (environment), Art 50 (separate judiciary from executive), Art 51 (international peace)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Fundamental Duties & Citizenship", "type": "branch", "date": "Duties & Citizen",
                "children": [
                    {
                        "label": "Fundamental Duties (Art 51A)", "type": "sub", "date": "Part IV-A",
                        "children": [
                            {"label": "Added by 42nd Amendment (1976) under Swaran Singh Committee; originally 10 duties, 11th added by 86th Amendment (2002)", "type": "leaf"},
                            {"label": "Non-justiciable; apply only to Indian citizens; include honoring National Flag, safeguarding public property", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Citizenship (Articles 5-11)", "type": "sub", "date": "Part II",
                        "children": [
                            {"label": "Single citizenship model (borrowed from UK); Article 9 states persons acquiring foreign citizenship automatically lose Indian status", "type": "leaf"},
                            {"label": "Article 11: Parliament possesses exclusive authority to regulate citizenship legislation (governed by Citizenship Act 1955)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. UNION GOVERNMENT (President, PM, Cabinet, Parliament structures)
    elif 'union-government' in fl:
        return [
            {
                "label": "Union Executive", "type": "branch", "date": "Executive Core",
                "children": [
                    {
                        "label": "President of India (Articles 52-62)", "type": "sub", "date": "Head of State",
                        "children": [
                            {"label": "Election: Indirectly by Electoral College (elected MPs + elected MLAs); oath by Chief Justice of India", "type": "leaf"},
                            {"label": "Impeachment (Article 61): Initiated in either house, requires 2/3rd majority of total membership for violation of Constitution", "type": "leaf"},
                            {"label": "Powers: Pardoning (Article 72), Ordinance making (Article 123), executive appointments (Governors, CAG, CJI)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "VP, PM & Attorney General", "type": "sub", "date": "Other Officers",
                        "children": [
                            {"label": "Vice President (Art 63-71): Ex-officio chairman of Rajya Sabha; elected by electoral college of both Houses", "type": "leaf"},
                            {"label": "Prime Minister & Cabinet: Real executive; PM appointed by President (majority leader); Cabinet collectively responsible to Lok Sabha", "type": "leaf"},
                            {"label": "Attorney General (Article 76): Highest law officer; right of audience in all courts, participates in Parliament (no vote)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Parliament Structure & Officers", "type": "branch", "date": "Legislature",
                "children": [
                    {
                        "label": "Bicameral Chambers", "type": "sub", "date": "Houses",
                        "children": [
                            {"label": "Rajya Sabha (Upper, Art 80): Max 250 members (12 nominated); permanent chamber, 1/3rd retire every 2 years; 6-year term", "type": "leaf"},
                            {"label": "Lok Sabha (Lower, Art 81): Max 550 members directly elected by adult suffrage; normal tenure 5 years", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Officers & Presiding Officers", "type": "sub", "date": "Speakers",
                        "children": [
                            {"label": "Speaker of Lok Sabha: Elected by LS; decides Money Bills, casts deciding vote (casting vote), presides over joint sittings", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Proceedings, Bills & Committees", "type": "branch", "date": "Procedures",
                "children": [
                    {
                        "label": "Parliamentary Devices", "type": "sub", "date": "Sessions",
                        "children": [
                            {"label": "Sessions: Budget (Feb-May), Monsoon (July-Sept), Winter (Nov-Dec); max gap is 6 months", "type": "leaf"},
                            {"label": "Question Hour (starred/unstarred/short notice); Zero Hour (12 PM, raises matters without prior notice)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Bills & Joint Sittings", "type": "sub", "date": "Bills",
                        "children": [
                            {"label": "Money Bill (Art 110): Introduced in LS on President recommendation; RS can only hold/delay for 14 days", "type": "leaf"},
                            {"label": "Joint Sitting (Art 108): Summoned by President, presided by Speaker to resolve deadlocks on Ordinary/Financial bills", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Parliamentary Committees", "type": "sub", "date": "Committees",
                        "children": [
                            {"label": "Public Accounts Committee (PAC): 22 members (15 LS + 7 RS), scrutinizes CAG reports; Estimates Committee: 30 members (all LS, largest)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. STATE GOVERNMENT (Governor, CM, State Legislature, Judiciary)
    elif 'state-government' in fl:
        return [
            {
                "label": "State Executive & Legislature", "type": "branch", "date": "State Core",
                "children": [
                    {
                        "label": "State Executive", "type": "sub", "date": "Executive",
                        "children": [
                            {"label": "Governor (Articles 153-162): Constitutional head appointed by President; holds office during President's pleasure", "type": "leaf"},
                            {"label": "Chief Minister & Council: Real executive at state; Governor appoints CM; CM acts as channel between Governor and Council", "type": "leaf"},
                            {"label": "Advocate General for State (Article 165): Highest state law officer; appointed by Governor", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "State Legislature Structure", "type": "sub", "date": "Legislature",
                        "children": [
                            {"label": "Vidhan Sabha (Assembly): Directly elected; normal term 5 years; size limit 60 to 500 members", "type": "leaf"},
                            {"label": "Vidhan Parishad (Council, Art 169): Created/abolished by Parliament on Assembly resolution; max size 1/3 of Assembly, min 40", "type": "leaf"},
                            {"label": "Bicameral States: Only 6 states currently have Councils (UP, Bihar, Maharashtra, Karnataka, Andhra Pradesh, Telangana)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Judicial Structure (SC & HC)", "type": "branch", "date": "Judiciary",
                "children": [
                    {
                        "label": "Supreme Court of India (Articles 124-147)", "type": "sub", "date": "Apex Court",
                        "children": [
                            {"label": "Appointment: Collegium system, appointed by President; retire age 65; removed by parliamentary address (impeachment)", "type": "leaf"},
                            {"label": "Jurisdictions: Original (Art 131), Appellate, Advisory (President reference, Art 143), Writ (Art 32), Court of Record (Art 129)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "High Courts & Subordinate Courts", "type": "sub", "date": "State Courts",
                        "children": [
                            {"label": "High Courts: 25 HCs in India; judges retire at 62; Writ jurisdiction (Article 226) covers fundamental and legal rights", "type": "leaf"},
                            {"label": "Subordinate Courts: District judges appointed by State Governor in consultation with High Court", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. LOCAL GOVERNMENT (Panchayati Raj & Municipalities)
    elif 'local-government' in fl:
        return [
            {
                "label": "Panchayati Raj System", "type": "branch", "date": "Rural Local Bodies",
                "children": [
                    {
                        "label": "73rd Amendment Act 1992", "type": "sub", "date": "73rd Amendment",
                        "children": [
                            {"label": "Constitutional status; added Part IX, Articles 243 to 243O, and 11th Schedule (29 functional subjects)", "type": "leaf"},
                            {"label": "Three-Tier Structure: Gram Panchayat (village), Panchayat Samiti (block), Zilla Parishad (district)", "type": "leaf"},
                            {"label": "Gram Sabha: Legislative body at village; consists of all registered voters; reserves 1/3rd seats for women (Art 243D)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "State Election & Finance", "type": "sub", "date": "Panchayat Machinery",
                        "children": [
                            {"label": "State Election Commission (Art 243K): Appointed by Governor, conducts Panchayat elections", "type": "leaf"},
                            {"label": "State Finance Commission (Art 243I): Recommends revenue distribution, constituted every 5 years by Governor", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Municipalities (Urban Bodies)", "type": "branch", "date": "Urban Local Bodies",
                "children": [
                    {
                        "label": "74th Amendment Act 1992", "type": "sub", "date": "74th Amendment",
                        "children": [
                            {"label": "Added Part IX-A, Articles 243P to 243ZG, and 12th Schedule (18 functional subjects)", "type": "leaf"},
                            {"label": "Types: Nagar Panchayat (transitional), Municipal Council (small urban), Municipal Corporation (large urban)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Evolutionary Committees", "type": "branch", "date": "Committees",
                "children": [
                    {
                        "label": "Panchayat Committees", "type": "sub", "date": "Milestones",
                        "children": [
                            {"label": "Balwant Rai Mehta (1957): Recommended 3-tier; Rajasthan (Nagaur district, Oct 2, 1959) was first to adopt", "type": "leaf"},
                            {"label": "Ashok Mehta (1977): Recommended 2-tier; L.M. Singhvi (1986): Recommended constitutional status", "type": "leaf"},
                            {"label": "G.V.K. Rao (1985): Termed Panchayati Raj 'grass without roots' due to bureaucratic control", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. BODIES (CAG, Election Commission, NITI Aayog, Finance Commission)
    elif 'bodies-cag' in fl:
        return [
            {
                "label": "Constitutional Bodies", "type": "branch", "date": "Constitutional",
                "children": [
                    {
                        "label": "Elections & Finance", "type": "sub", "date": "EC & FC",
                        "children": [
                            {"label": "Election Commission (Art 324): 3 members; conducts Lok Sabha, Rajya Sabha, President, and Assembly elections", "type": "leaf"},
                            {"label": "Finance Commission (Art 280): Appointed every 5 years; recommends tax devolution between Centre and States", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "CAG & Law Officers", "type": "sub", "date": "Audits & Advice",
                        "children": [
                            {"label": "Comptroller & Auditor General (CAG, Art 148): Audits Union & State accounts; term 6 years or 65 age limit", "type": "leaf"},
                            {"label": "Attorney General of India (Art 76): Appointed by President; Advocate General of State (Art 165): Appointed by Governor", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "National Commissions", "type": "sub", "date": "Commissions",
                        "children": [
                            {"label": "NC for Scheduled Castes (Art 338), NC for Scheduled Tribes (Art 338A), NC for OBCs (Art 338B)", "type": "leaf"},
                            {"label": "UPSC & SPSC (Art 315-323): Public service commissions; Special Officer for Linguistic Minorities (Art 350B)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Non-Constitutional & Statutory", "type": "branch", "date": "Executive & Statutory",
                "children": [
                    {
                        "label": "NITI Aayog", "type": "sub", "date": "NITI",
                        "children": [
                            {"label": "Formed Jan 1, 2015 replacing Planning Commission; non-constitutional advisory body for bottom-up federalism", "type": "leaf"},
                            {"label": "Structure: PM (Chairperson), Vice-Chairperson (appointed by PM), CEO, Governing Council (all CMs + UT Governors)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Statutory Bodies", "type": "sub", "date": "Statutory",
                        "children": [
                            {"label": "NHRC: Established under Protection of Human Rights Act 1993; CVC: Central Vigilance Commission (statutory 2003)", "type": "leaf"},
                            {"label": "CIC: Central Information Commission (RTI Act 2005); Lokpal & Lokayuktas (2013): Anti-corruption ombudsman", "type": "leaf"}
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
