import os
import re
import subprocess

POLITY_FALLBACKS = {
    "add_fundamental_rights_mindmaps.py": '''return [
        {
            "label": "Part III: Fundamental Rights\\n(Articles 12-35)",
            "type": "branch",
            "date": "Part III",
            "children": [
                {
                    "label": "Core Rights & Articles", "type": "sub", "date": "Art 14-32",
                    "children": [
                        {"label": "Art 14-18 (Equality), Art 19-22 (Freedom), Art 23-24 (Against Exploitation), Art 25-28 (Religion), Art 29-30 (Culture/Education)", "type": "leaf"},
                        {"label": "Art 32: Right to Constitutional Remedies (habeas corpus, mandamus, prohibition, certiorari, quo warranto; heart & soul)", "type": "leaf"},
                        {"label": "Reasonable Restrictions: Art 19(2) to 19(6) define constitutional boundaries based on public order, morality, and sovereignty", "type": "leaf"}
                    ]
                }
            ]
        },
        {
            "label": "DPSP & Duties\\n(Articles 36-51A)",
            "type": "branch",
            "date": "Part IV & IV-A",
            "children": [
                {
                    "label": "State Policy & Duties", "type": "sub", "date": "Directive Principles",
                    "children": [
                        {"label": "Directive Principles (Art 36-51): Socialistic (Art 38, 39, 41), Gandhian (Art 40, 43, 47), Liberal-Intellectual (Art 44, 48, 50)", "type": "leaf"},
                        {"label": "Fundamental Duties (Art 51A): 11 duties; 42nd Amendment (10 duties, Swaran Singh); 86th Amendment (11th duty, education)", "type": "leaf"}
                    ]
                }
            ]
        }
    ]''',

    "add_constitutional_bodies_mindmaps.py": '''return [
        {
            "label": "Constitutional Bodies\\n(Art 76, 148, 280, 324)",
            "type": "branch",
            "date": "Constitutional",
            "children": [
                {
                    "label": "Core Offices & Articles", "type": "sub", "date": "Key Offices",
                    "children": [
                        {"label": "Art 324: Election Commission of India (ECI); Art 148: Comptroller and Auditor General (CAG) of India", "type": "leaf"},
                        {"label": "Art 280: Finance Commission (recommends vertical/horizontal tax devolution); Art 76: Attorney General of India", "type": "leaf"},
                        {"label": "Art 315-323: Union Public Service Commission (UPSC) and State Public Service Commissions (SPSC)", "type": "leaf"}
                    ]
                }
            ]
        },
        {
            "label": "Non-Constitutional Bodies",
            "type": "branch",
            "date": "Extra-Constitutional",
            "children": [
                {
                    "label": "Statutory & Executive", "type": "sub", "date": "Non-Constitutional",
                    "children": [
                        {"label": "Statutory: NHRC (Human Rights Act 1993), Central Information Commission (RTI Act 2005), Lokpal & Lokayuktas Act 2013", "type": "leaf"},
                        {"label": "Executive: NITI Aayog (established Jan 1, 2015, replacing Planning Commission; chaired by PM; think-tank model)", "type": "leaf"}
                    ]
                }
            ]
        }
    ]''',

    "add_judiciary_mindmaps.py": '''return [
        {
            "label": "Supreme Court\\n(Articles 124-147)",
            "type": "branch",
            "date": "Union Judiciary",
            "children": [
                {
                    "label": "Jurisdiction & Powers", "type": "sub", "date": "Key Articles",
                    "children": [
                        {"label": "Art 124: Establishment and constitution of Supreme Court; collegium system of appointments (3 Judges Cases)", "type": "leaf"},
                        {"label": "Art 131 (Original jurisdiction), Art 132-134 (Appellate jurisdiction), Art 136 (Special Leave Petition), Art 143 (Advisory)", "type": "leaf"},
                        {"label": "Art 129: Court of Record (power to punish for contempt of itself); Art 137: Power of review of its own judgments", "type": "leaf"}
                    ]
                }
            ]
        },
        {
            "label": "High Courts & Subordinate",
            "type": "branch",
            "date": "State Judiciary",
            "children": [
                {
                    "label": "State & District Courts", "type": "sub", "date": "Art 214-237",
                    "children": [
                        {"label": "High Courts (Art 214-231): Art 226 writ jurisdiction (broader than Art 32; covers legal rights as well as FRs)", "type": "leaf"},
                        {"label": "Subordinate Courts (Art 233-237): District Judges appointed by Governor in consultation with High Court", "type": "leaf"}
                    ]
                }
            ]
        }
    ]''',

    "add_local_government_mindmaps.py": '''return [
        {
            "label": "Panchayats & Municipalities\\n(Articles 243-243ZG)",
            "type": "branch",
            "date": "Local Govt",
            "children": [
                {
                    "label": "73rd & 74th Amendments", "type": "sub", "date": "Art 243",
                    "children": [
                        {"label": "73rd Amendment 1992: Part IX, Articles 243-243O, 11th Schedule (29 functional items for Panchayats)", "type": "leaf"},
                        {"label": "74th Amendment 1992: Part IX-A, Articles 243P-243ZG, 12th Schedule (18 functional items for Municipalities)", "type": "leaf"},
                        {"label": "Art 243I: State Finance Commission; Art 243K: State Election Commission; Art 243ZD: District Planning Committee", "type": "leaf"}
                    ]
                }
            ]
        },
        {
            "label": "UTs & Scheduled Areas",
            "type": "branch",
            "date": "UTs & Schedules",
            "children": [
                {
                    "label": "Special Administrations", "type": "sub", "date": "Art 239 & 244",
                    "children": [
                        {"label": "Union Territories (Art 239-241): Administered by President through Administrator/LG; Art 239AA: Special status for Delhi", "type": "leaf"},
                        {"label": "Scheduled & Tribal Areas (Art 244-244A): 5th Schedule (Tribes Advisory Council), 6th Schedule (Autonomous District Councils)", "type": "leaf"}
                    ]
                }
            ]
        }
    ]''',

    "add_political_dynamics_mindmaps.py": '''return [
        {
            "label": "Elections & Parties\\n(Articles 324-329)",
            "type": "branch",
            "date": "Part XV",
            "children": [
                {
                    "label": "Electoral Framework", "type": "sub", "date": "Elections",
                    "children": [
                        {"label": "Art 324: Superintendence, direction, and control of elections vested in the Election Commission of India", "type": "leaf"},
                        {"label": "Art 325: No person ineligible for inclusion in electoral roll on grounds of religion, race, caste, or sex", "type": "leaf"},
                        {"label": "Art 326: Elections to Lok Sabha and State Legislative Assemblies on the basis of adult suffrage (voting age 18)", "type": "leaf"}
                    ]
                }
            ]
        },
        {
            "label": "Representation of People",
            "type": "branch",
            "date": "Statutory Controls",
            "children": [
                {
                    "label": "Representation Acts", "type": "sub", "date": "RPA 1950 & 1951",
                    "children": [
                        {"label": "Representation of the People Act 1950: Allocation of seats, delimitation of constituencies, registration of electors", "type": "leaf"},
                        {"label": "Representation of the People Act 1951: Conduct of elections, qualifications/disqualifications of members, corrupt practices", "type": "leaf"}
                    ]
                }
            ]
        }
    ]''',

    "add_state_executive_mindmaps.py": '''return [
        {
            "label": "State Executive\\n(Articles 153-167)",
            "type": "branch",
            "date": "Part VI Executive",
            "children": [
                {
                    "label": "Governor & CM", "type": "sub", "date": "State Executive",
                    "children": [
                        {"label": "Art 153: Governors of States; Art 154: Executive power of State vested in Governor; holds office during President's pleasure", "type": "leaf"},
                        {"label": "Art 163: Council of Ministers with CM to aid and advise Governor (discretionary powers wider than President's)", "type": "leaf"},
                        {"label": "Art 164: Other provisions as to Ministers (collective responsibility to the Legislative Assembly of the State)", "type": "leaf"}
                    ]
                }
            ]
        },
        {
            "label": "State Legislature\\n(Articles 168-212)",
            "type": "branch",
            "date": "Part VI Legislature",
            "children": [
                {
                    "label": "Assembly & Council", "type": "sub", "date": "State Assembly",
                    "children": [
                        {"label": "Art 168: Constitution of Legislatures in States; Art 169: Abolition or creation of Legislative Councils (Vidhan Parishad)", "type": "leaf"},
                        {"label": "Art 200: Assent to bills by Governor (options to give assent, withhold assent, return bill, or reserve for President)", "type": "leaf"}
                    ]
                }
            ]
        }
    ]''',

    "add_system_of_governance_mindmaps.py": '''return [
        {
            "label": "Centre-State Relations\\n(Articles 245-293)",
            "type": "branch",
            "date": "Federal Setup",
            "children": [
                {
                    "label": "Relations & Devolution", "type": "sub", "date": "Art 245-293",
                    "children": [
                        {"label": "Art 245-255: Legislative relations; distribution of legislative lists (Union, State, Concurrent) in the 7th Schedule", "type": "leaf"},
                        {"label": "Art 256-263: Administrative relations; Art 257 Union control; Art 263 Inter-State Council (Sarkaria Commission recommendation)", "type": "leaf"},
                        {"label": "Art 268-293: Financial relations; Art 275 grants-in-aid; Art 280 Finance Commission; Art 279A GST Council", "type": "leaf"}
                    ]
                }
            ]
        },
        {
            "label": "Emergency Provisions\\n(Articles 352-360)",
            "type": "branch",
            "date": "Part XVIII",
            "children": [
                {
                    "label": "Emergency Types", "type": "sub", "date": "Emergencies",
                    "children": [
                        {"label": "Art 352: National Emergency (war, external aggression, or armed rebellion); Art 358 & 359: suspension of fundamental rights", "type": "leaf"},
                        {"label": "Art 356: President's Rule (failure of constitutional machinery in State); Art 365: non-compliance with Union directions", "type": "leaf"},
                        {"label": "Art 360: Financial Emergency (declared by President if financial stability or credit of India is threatened)", "type": "leaf"}
                    ]
                }
            ]
        }
    ]''',

    "add_union_executive_mindmaps.py": '''return [
        {
            "label": "Union Executive\\n(Articles 52-78)",
            "type": "branch",
            "date": "Part V Executive",
            "children": [
                {
                    "label": "President & Cabinet", "type": "sub", "date": "Union Executive",
                    "children": [
                        {"label": "Art 52: The President of India; Art 54: Electoral College; Art 61: Impeachment procedure for violation of Constitution", "type": "leaf"},
                        {"label": "Art 72: Power of President to grant pardons; Art 123: Power to promulgate ordinances during recess of Parliament", "type": "leaf"},
                        {"label": "Art 74: Council of Ministers to aid and advise President; Art 75: Collective responsibility of ministers to Lok Sabha", "type": "leaf"}
                    ]
                }
            ]
        },
        {
            "label": "Parliament of India\\n(Articles 79-122)",
            "type": "branch",
            "date": "Part V Parliament",
            "children": [
                {
                    "label": "Houses & Procedures", "type": "sub", "date": "Union Parliament",
                    "children": [
                        {"label": "Art 79: Constitution of Parliament (President, Lok Sabha, Rajya Sabha); Art 85: Sessions, prorogation, and dissolution", "type": "leaf"},
                        {"label": "Art 105: Powers, privileges, and immunities of Parliament and its members; Art 110: Definition of Money Bills", "type": "leaf"}
                    ]
                }
            ]
        }
    ]'''
}

def update_file(filename, fallback_code):
    if not os.path.exists(filename):
        return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the fallback comment
    fallback_comment = "# --- GENERAL FALLBACK"
    pos = content.find(fallback_comment)
    if pos == -1:
        fallback_comment = "# Fallback"
        pos = content.find(fallback_comment)
        
    if pos == -1:
        print(f"Skipping (no fallback comment): {filename}")
        return

    # Find return statement
    return_pos = content.find("return [", pos)
    if return_pos == -1:
        print(f"Skipping (no return statement found): {filename}")
        return
        
    # Match brackets to find the end
    bracket_count = 1
    i = return_pos + 8
    while i < len(content) and bracket_count > 0:
        if content[i] == '[':
            bracket_count += 1
        elif content[i] == ']':
            bracket_count -= 1
        i += 1
        
    if bracket_count != 0:
        print(f"Skipping (unbalanced brackets in return statement): {filename}")
        return
        
    content = content[:return_pos] + fallback_code + content[i:]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated advanced fallback: {filename}")

def main():
    print("Updating polity scripts with advanced fallbacks featuring constitutional articles...")
    for filename, fallback_code in POLITY_FALLBACKS.items():
        update_file(filename, fallback_code)
        
    print("\nRe-running all updated polity scripts...")
    for filename in POLITY_FALLBACKS.keys():
        print(f"Running {filename}...")
        subprocess.run(["python", filename], check=True)
        print(f"Finished {filename}\n")

if __name__ == '__main__':
    main()
