import os
import re
import json

BASE_DIR = r"upsc/polity/Fundamental-Rights-DPSP-Fundamental-Duties"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'frs', 'fds'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs', 'outside']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# 3-Tier Deep-Dive Mappings for Fundamental Rights, DPSPs, and Duties
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. ARTICLE 12 (DEFINITION OF STATE)
    if 'article-12' in fl:
        return [
            {
                "label": "Constitutional Scope",
                "type": "branch",
                "date": "Article 12",
                "children": [
                    {
                        "label": "State Organs", "type": "sub", "date": "Government", "children": [
                            {"label": "Executive & Legislative organs of Central Govt (President, PM, Parliament) & State Govts", "type": "leaf"},
                            {"label": "All local authorities: Municipalities, Panchayats, District Boards, & Port Trusts", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Other Authorities", "type": "sub", "date": "Agencies", "children": [
                            {"label": "Statutory or non-statutory bodies acting as agencies of state: LIC, ONGC, SAIL, GAIL", "type": "leaf"},
                            {"label": "Private bodies acting as instruments of state (under deep state control/funding) fall under Art 12", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. ARTICLE 13 (LAWS INCONSISTENT WITH FRS)
    elif 'article-13' in fl:
        return [
            {
                "label": "Judicial Shield",
                "type": "branch",
                "date": "Article 13",
                "children": [
                    {
                        "label": "Inconsistency & Voidability", "type": "sub", "date": "Doctrines", "children": [
                            {"label": "All pre-constitution & post-constitution laws inconsistent with FRs are void to that extent (Art 13(1) & (2))", "type": "leaf"},
                            {"label": "Doctrine of Severability: Only the offensive part of the statute is declared void, not the entire act", "type": "leaf"},
                            {"label": "Doctrine of Eclipse: Inconsistent law remains dormant/shadowed, becomes active again if FR is amended", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Definition of Law", "type": "sub", "date": "Article 13(3)", "children": [
                            {"label": "Includes permanent laws (Parliament/State acts), temporary laws (Ordinances), statutory instruments (bye-laws, rules)", "type": "leaf"},
                            {"label": "Art 13(3): Custom or usage having the force of law can be challenged if violating FRs", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. JUDICIAL REVIEW
    elif 'judicial-review' in fl:
        return [
            {
                "label": "Constitutional Core",
                "type": "branch",
                "date": "Doctrine",
                "children": [
                    {
                        "label": "Scope & Mandate", "type": "sub", "date": "Judicial Power", "children": [
                            {"label": "Power of judiciary to examine constitutionality of legislative acts and executive orders; basic structure feature", "type": "leaf"},
                            {"label": "Articles 13, 32, 131-136, 143, 226, 246 provide explicit basis for judicial review in India", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Evolutionary Benchmarks",
                "type": "branch",
                "date": "Cases",
                "children": [
                    {
                        "label": "Key Cases", "type": "sub", "date": "Supreme Court", "children": [
                            {"label": "Kesavananda Bharati (1973): Established Basic Structure doctrine; limits Parliament's amending power under Art 368", "type": "leaf"},
                            {"label": "L. Chandra Kumar (1997): Declared judicial review under Art 32 & 226 as part of basic structure", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. RULE OF LAW & PROCESSES
    elif 'rule-of-law' in fl or 'due-process' in fl or 'procedure-established' in fl:
        return [
            {
                "label": "Dicey's Rule of Law",
                "type": "branch",
                "date": "Dicey Model",
                "children": [
                    {
                        "label": "Three Pillars", "type": "sub", "date": "Pillars", "children": [
                            {"label": "Absence of arbitrary power (no man punished except for distinct breach of law); Equality before law (Art 14)", "type": "leaf"},
                            {"label": "Primacy of individual rights (Constitution is the result of individual rights, modified in India)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Procedure vs Due Process",
                "type": "branch",
                "date": "Article 21",
                "children": [
                    {
                        "label": "Article 21 Evolution", "type": "sub", "date": "Process", "children": [
                            {"label": "Procedure Established by Law (UK): Checks executive action only; law must be validly enacted (Gopalan Case 1950)", "type": "leaf"},
                            {"label": "Due Process of Law (US): Checks both executive & legislative actions; law must be just, fair, & reasonable", "type": "leaf"},
                            {"label": "Maneka Gandhi Case (1978): Supreme Court read 'Due Process' into Article 21, establishing natural justice", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. EQUALITY RIGHTS (ART 14-18)
    elif 'equality-rights' in fl or 'equality' in fl:
        return [
            {
                "label": "Equality & Class",
                "type": "branch",
                "date": "Article 14-16",
                "children": [
                    {
                        "label": "Art 14 & 15", "type": "sub", "date": "Foundations", "children": [
                            {"label": "Art 14: Equality before law (negative, UK) & Equal protection of laws (positive, US; allows reasonable classification)", "type": "leaf"},
                            {"label": "Art 15: No discrimination on grounds ONLY of religion, race, caste, sex, or place of birth; allows special provisions for women/children/OBCs", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Art 16", "type": "sub", "date": "Employment", "children": [
                            {"label": "Equal opportunity in public employment; Art 16(4) allows reservation for backward classes not adequately represented", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Social Abolitions",
                "type": "branch",
                "date": "Article 17-18",
                "children": [
                    {
                        "label": "Untouchability & Titles", "type": "sub", "date": "Abolition", "children": [
                            {"label": "Art 17: Abolition of Untouchability; absolute right (no exceptions); enforced via Civil Rights Protection Act 1955", "type": "leaf"},
                            {"label": "Art 18: Abolition of Titles (except military & academic); checks noble hierarchies; National Awards (Bharat Ratna) are not titles", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. RIGHT TO FREEDOM (ART 19-22)
    elif 'right-to-freedom' in fl and 'religion' not in fl:
        return [
            {
                "label": "Six Freedoms (Art 19)",
                "type": "branch",
                "date": "Article 19",
                "children": [
                    {
                        "label": "Article 19(1)", "type": "sub", "date": "Freedoms", "children": [
                            {"label": "Speech & expression, assembly (peaceful/no arms), association (includes co-ops), movement, residence, profession", "type": "leaf"},
                            {"label": "Restrictions: Article 19(2)-(6) lists reasonable restrictions (sovereignty, security, public order, morality)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Protection Rights",
                "type": "branch",
                "date": "Article 20-22",
                "children": [
                    {
                        "label": "Art 20, 21, & 22", "type": "sub", "date": "Protections", "children": [
                            {"label": "Art 20: Protection against conviction (no ex-post facto laws, no double jeopardy, no self-incrimination)", "type": "leaf"},
                            {"label": "Art 21: Protection of life & personal liberty; includes right to privacy, clean air, livelihood, and speedy trial", "type": "leaf"},
                            {"label": "Art 22: Protection against arrest & detention; punitive vs preventive detention (max 3 months without advisory board review)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 7. RIGHT AGAINST EXPLOITATION (ART 23-24)
    elif 'exploitation' in fl:
        return [
            {
                "label": "Forced Labor & Trafficking",
                "type": "branch",
                "date": "Article 23",
                "children": [
                    {
                        "label": "Prohibitions", "type": "sub", "date": "Forced Labor", "children": [
                            {"label": "Prohibits traffic in human beings, begar (forced labor without payment), and other similar forms of forced labor", "type": "leaf"},
                            {"label": "Exception: State can impose compulsory service for public purposes (military/social duty) without discrimination", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Child Labor",
                "type": "branch",
                "date": "Article 24",
                "children": [
                    {
                        "label": "Bans & Amendments", "type": "sub", "date": "Child Labor", "children": [
                            {"label": "Prohibits employment of children below 14 years in hazardous industries (factories, mines, railways)", "type": "leaf"},
                            {"label": "Child Labour Amendment Act 2016 bans all commercial child employment below 14, and adolescents (14-18) in hazardous jobs", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 8. FREEDOM OF RELIGION (ART 25-28)
    elif 'religion' in fl:
        return [
            {
                "label": "Individual & Group Rights",
                "type": "branch",
                "date": "Article 25-26",
                "children": [
                    {
                        "label": "Art 25 & 26", "type": "sub", "date": "Practices", "children": [
                            {"label": "Art 25: Freedom of conscience, free profession, practice, & propagation of religion; subject to public order, health, morality", "type": "leaf"},
                            {"label": "Art 26: Right to manage religious affairs, establish institutions, own property, & administer it in accordance with law", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Taxes & Instruction",
                "type": "branch",
                "date": "Article 27-28",
                "children": [
                    {
                        "label": "Art 27 & 28", "type": "sub", "date": "Secularism", "children": [
                            {"label": "Art 27: Freedom from payment of taxes for promotion of any particular religion (secular state principle)", "type": "leaf"},
                            {"label": "Art 28: No religious instruction in educational institutions wholly maintained out of State funds", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 9. CULTURAL & EDUCATIONAL RIGHTS (ART 29-30)
    elif 'cultural' in fl or 'educational' in fl:
        return [
            {
                "label": "Protection of Interests",
                "type": "branch",
                "date": "Article 29",
                "children": [
                    {
                        "label": "Citizens script & culture", "type": "sub", "date": "Interests", "children": [
                            {"label": "Any section of citizens with distinct language, script, or culture has right to conserve the same (applies to both majority & minorities)", "type": "leaf"},
                            {"label": "No citizen denied admission to state-aided institutions on grounds only of religion, race, caste, or language", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Institutional Rights",
                "type": "branch",
                "date": "Article 30",
                "children": [
                    {
                        "label": "Minority institutions", "type": "sub", "date": "Establishment", "children": [
                            {"label": "All religious & linguistic minorities have right to establish and administer educational institutions of their choice", "type": "leaf"},
                            {"label": "State shall not discriminate in granting aid to minority-managed educational institutions", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 10. CONSTITUTIONAL REMEDIES (ART 32)
    elif 'remedies' in fl or 'article-32' in fl:
        return [
            {
                "label": "Heart & Soul",
                "type": "branch",
                "date": "Article 32",
                "children": [
                    {
                        "label": "Article 32 Mandate", "type": "sub", "date": "Jurisdiction", "children": [
                            {"label": "Right to move Supreme Court for enforcement of FRs is itself a Fundamental Right; basic structure component", "type": "leaf"},
                            {"label": "Supreme Court has original and concurrent jurisdiction (with High Court under Article 226) for FR enforcement", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Five Writs",
                "type": "branch",
                "date": "Writs",
                "children": [
                    {
                        "label": "Prerogative Writs", "type": "sub", "date": "Types", "children": [
                            {"label": "Habeas Corpus (produce the body); Mandamus (we command public duty); Prohibition (inactive lower court check)", "type": "leaf"},
                            {"label": "Certiorari (to be certified, quashes order); Quo Warranto (by what authority, checks public office claim)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 11. DPSP (PART IV, ART 36-51)
    elif 'dpsp' in fl or 'directive' in fl or 'principles' in fl:
        return [
            {
                "label": "Nature & Classification",
                "type": "branch",
                "date": "Art 36-51",
                "children": [
                    {
                        "label": "Basic Features", "type": "sub", "date": "Features", "children": [
                            {"label": "Non-justiciable in courts (Art 37) but fundamental in governance of the country; instrument of instructions", "type": "leaf"},
                            {"label": "Aim: Establish a Welfare State and promote socio-economic democracy (FRs establish political democracy)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Socialistic & Gandhian", "type": "sub", "date": "Principles", "children": [
                            {"label": "Socialistic: Art 38 (minimize inequalities), Art 39 (equal pay, distribute resources), Art 41 (right to work), Art 43", "type": "leaf"},
                            {"label": "Gandhian: Art 40 (village panchayats), Art 43B (cooperative societies), Art 47 (ban intoxicating drinks), Art 48", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Liberal-Intellectual", "type": "sub", "date": "Principles", "children": [
                            {"label": "Liberal: Art 44 (Uniform Civil Code), Art 45 (early childhood care), Art 48A (environment), Art 50 (separate judiciary)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Amendments & Conflict",
                "type": "branch",
                "date": "Dynamics",
                "children": [
                    {
                        "label": "DPSP Amendments", "type": "sub", "date": "DPSP changes", "children": [
                            {"label": "42nd Amendment (1976): Added Art 39A (free legal aid), Art 43A (workers in management), Art 48A (environment)", "type": "leaf"},
                            {"label": "44th Amendment (1978): Added Art 38(2) (minimize status inequalities); 86th Amendment (2002): Modified Art 45", "type": "leaf"},
                            {"label": "97th Amendment (2011): Added Art 43B regarding promotion of cooperative societies", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Conflict with FRs", "type": "sub", "date": "Court Benchmarks", "children": [
                            {"label": "Champakam Dorairajan (1951): FRs prevail over DPSP; Minerva Mills (1980): Harmony & balance between FRs & DPSP", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 12. FUNDAMENTAL DUTIES (ART 51A)
    elif 'duties' in fl or 'duty' in fl:
        return [
            {
                "label": "Features & List",
                "type": "branch",
                "date": "Article 51A",
                "children": [
                    {
                        "label": "Swaran Singh Setup", "type": "sub", "date": "Features", "children": [
                            {"label": "Added by 42nd Constitutional Amendment 1976 on Swaran Singh Committee report; inspired by USSR constitution", "type": "leaf"},
                            {"label": "Initially 10 duties; 11th duty (parental duty for child education 6-14 yrs) added by 86th Amendment 2002", "type": "leaf"},
                            {"label": "Non-justiciable; apply only to citizens; Verma Committee (1999) identified legal provisions for enforcing certain duties", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Duties Content", "type": "sub", "date": "List", "children": [
                            {"label": "Abide by Constitution, respect National Flag/Anthem; cherish freedom struggle ideals; protect sovereignty, unity & integrity", "type": "leaf"},
                            {"label": "Promote harmony & brotherhood; value rich composite heritage; protect natural environment; develop scientific temper", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 13. CLASSIFICATION OF RIGHTS
    elif 'property' in fl or 'vote' in fl or 'legal-constitutional' in fl:
        return [
            {
                "label": "Classification of Rights",
                "type": "branch",
                "date": "Syllabus Core",
                "children": [
                    {
                        "label": "Right to Property", "type": "sub", "date": "Art 300A", "children": [
                            {"label": "Right to Property: Removed from FR (Art 19(1)(f) & 31) by 44th Amendment 1978; made legal right under Art 300A", "type": "leaf"},
                            {"label": "Constitutional protection: Property cannot be acquired by state without authority of law and public purpose", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Right to Vote", "type": "sub", "date": "Art 326", "children": [
                            {"label": "Right to Vote: Constitutional right under Art 326; not a fundamental right (dictated by statutory terms)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 14. PART III MEANING & EVOLUTION
    elif 'meaning-objectives-evolution' in fl:
        return [
            {
                "label": "Part III Evolution",
                "type": "branch",
                "date": "Historical",
                "children": [
                    {
                        "label": "Genesis & Purpose", "type": "sub", "date": "Magna Carta", "children": [
                            {"label": "Inspired by Bill of Rights (USA) & Magna Carta (1215); drafted by Advisory Committee on Fundamental Rights (Patel)", "type": "leaf"},
                            {"label": "Meaning: Negative injunctions preventing state overreach; justiciable in courts (guaranteed by Art 32/226)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 15. OTHER DIMENSIONS OF FRS
    elif 'other-dimensions' in fl:
        return [
            {
                "label": "Special Statuses",
                "type": "branch",
                "date": "Article 33 & 34",
                "children": [
                    {
                        "label": "Armed Forces & Martial Law", "type": "sub", "date": "Exemptions", "children": [
                            {"label": "Art 33: Parliament can restrict/abrogate FRs of members of armed forces, paramilitary, police, intelligence agencies", "type": "leaf"},
                            {"label": "Art 34: Restrictions on FRs while martial law (military rule) is in force in any area; distinct from National Emergency", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 16. REASONABLE RESTRICTIONS ON FRS
    elif 'reasonable-restriction' in fl:
        return [
            {
                "label": "Reasonable Restrictions",
                "type": "branch",
                "date": "Article 19 Limits",
                "children": [
                    {
                        "label": "Article 19(2) Grounds", "type": "sub", "date": "FR Limits", "children": [
                            {"label": "Sovereignty & integrity of India, security of the State, friendly relations with foreign States, public order, decency or morality", "type": "leaf"},
                            {"label": "Contempt of court, defamation, or incitement to an offense; restrictions must not be arbitrary or disproportionate", "type": "leaf"}
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

