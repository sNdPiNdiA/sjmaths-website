/**
 * UPSSSC Lower Mains Polity Page Generator
 * Uses Gemini API (gemini-2.0-flash-lite) to generate THEORY ONLY content for 25 polity topics
 * Run: node scripts/gen_polity_pages.js
 *
 * NOTE: Only theory/concepts section is generated now.
 *       Practice, PYQs, and Test sections are placeholders for future generation.
 */

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'polity');

// ─── Topic Definitions ────────────────────────────────────────────────────────
const TOPICS = [
  {
    key: 'salient-features-preamble',
    titleEn: 'Salient Features & Preamble of the Constitution',
    titleHi: 'संविधान की प्रमुख विशेषताएं एवं प्रस्तावना',
    breadEn: 'Salient Features & Preamble',
    breadHi: 'प्रमुख विशेषताएं और प्रस्तावना',
    descEn: 'Comprehensive study guide covering the salient features and Preamble of the Indian Constitution for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए भारतीय संविधान की प्रमुख विशेषताएं और प्रस्तावना की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Salient Features & Preamble of the Indian Constitution" (संविधान की प्रमुख विशेषताएं एवं प्रस्तावना). Cover: nature of Indian constitution, federal vs unitary features, key characteristics (written, rigid/flexible, parliamentary, secular, independent judiciary), Preamble text, keywords (sovereign, socialist, secular, democratic, republic), 42nd Amendment significance, Berubari & Kesavananda cases related to Preamble.`
  },
  {
    key: 'constituent-assembly-making-of-the-constitution',
    titleEn: 'Constituent Assembly & Making of the Constitution',
    titleHi: 'संविधान सभा एवं संविधान निर्माण',
    breadEn: 'Constituent Assembly',
    breadHi: 'संविधान सभा',
    descEn: 'Comprehensive study guide covering the Constituent Assembly, its composition, committees, and the constitution-making process for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए संविधान सभा, उसकी संरचना, समितियां और संविधान निर्माण प्रक्रिया की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Constituent Assembly & Making of the Indian Constitution" (संविधान सभा एवं संविधान निर्माण). Cover: Cabinet Mission Plan 1946, composition of Constituent Assembly (389 members), key members (Dr. B.R. Ambedkar, Dr. Rajendra Prasad, Jawaharlal Nehru, Sardar Patel), all important committees and their chairpersons (Drafting Committee, Union Constitution Committee, etc.), Objective Resolution, dates of adoption (26 Nov 1949) and enforcement (26 Jan 1950), sources of Indian Constitution from various countries.`
  },
  {
    key: 'government-of-india-acts-1858-1919-1935',
    titleEn: 'Government of India Acts (1858, 1919, 1935)',
    titleHi: 'भारत सरकार अधिनियम (1858, 1919, 1935)',
    breadEn: 'GoI Acts 1858-1935',
    breadHi: 'भारत सरकार अधिनियम',
    descEn: 'Comprehensive study guide covering the Government of India Acts of 1858, 1919, and 1935 for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए 1858, 1919 और 1935 के भारत सरकार अधिनियमों की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Government of India Acts 1858, 1919, 1935" (भारत सरकार अधिनियम). Cover: Act of 1858 (abolition of East India Company, Secretary of State, Council of India), Morley-Minto Reforms 1909, Government of India Act 1919 (Montagu-Chelmsford Reforms, dyarchy, bicameral legislature, public service commission), Government of India Act 1935 (provincial autonomy, federal features, federal court, RBI, dyarchy at centre, All India Federation).`
  },
  {
    key: 'regulating-act-1773-to-charter-act-1853',
    titleEn: 'Regulating Act 1773 to Charter Act 1853',
    titleHi: 'रेग्युलेटिंग एक्ट 1773 से चार्टर एक्ट 1853',
    breadEn: 'Regulating Act to Charter Acts',
    breadHi: 'रेग्युलेटिंग एक्ट से चार्टर एक्ट',
    descEn: 'Comprehensive study guide covering British constitutional legislation from Regulating Act 1773 to Charter Act 1853 for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए 1773 के रेग्युलेटिंग एक्ट से 1853 के चार्टर एक्ट तक की ब्रिटिश संवैधानिक विधायिका की व्यापक मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Regulating Act 1773 to Charter Act 1853" (रेग्युलेटिंग एक्ट 1773 से चार्टर एक्ट 1853). Cover: Regulating Act 1773 (first step by British Parliament, Governor-General, Supreme Court Calcutta), Pitt's India Act 1784 (Board of Control, double government), Charter Act 1813, Charter Act 1833 (Governor-General of India, end of trade monopoly, law commission, Macaulay), Charter Act 1853 (open civil services, legislative council enlarged, separation of executive and legislative functions).`
  },
  {
    key: 'indian-independence-act-1947',
    titleEn: 'Indian Independence Act 1947',
    titleHi: 'भारतीय स्वतंत्रता अधिनियम 1947',
    breadEn: 'Indian Independence Act 1947',
    breadHi: 'भारतीय स्वतंत्रता अधिनियम 1947',
    descEn: 'Comprehensive study guide covering the Indian Independence Act 1947 and its constitutional impact for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए भारतीय स्वतंत्रता अधिनियम 1947 और उसके संवैधानिक प्रभाव की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Indian Independence Act 1947" (भारतीय स्वतंत्रता अधिनियम 1947). Cover: Background (Mountbatten Plan / 3 June Plan), key provisions (two dominions India & Pakistan, partition of Bengal and Punjab, Governor-General for each dominion, Constituent Assembly became sovereign, lapse of paramountcy over princely states, Governor-General's power to adapt laws, Secretary of State for India abolished), constitutional significance and impact on Indian polity.`
  },
  {
    key: 'fundamental-rights-duties',
    titleEn: 'Fundamental Rights & Fundamental Duties',
    titleHi: 'मौलिक अधिकार एवं मौलिक कर्तव्य',
    breadEn: 'Fundamental Rights & Duties',
    breadHi: 'मौलिक अधिकार और कर्तव्य',
    descEn: 'Comprehensive study guide covering all Fundamental Rights (Articles 12-35) and Fundamental Duties (Article 51A) for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए सभी मौलिक अधिकारों (अनुच्छेद 12-35) और मौलिक कर्तव्यों (अनुच्छेद 51A) की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Fundamental Rights & Fundamental Duties" (मौलिक अधिकार एवं मौलिक कर्तव्य). Cover: All 6 categories of Fundamental Rights (Right to Equality Art.14-18, Right to Freedom Art.19-22, Right against Exploitation Art.23-24, Right to Freedom of Religion Art.25-28, Cultural & Educational Rights Art.29-30, Right to Constitutional Remedies Art.32), important Supreme Court cases (Maneka Gandhi, Kesavananda Bharati, Minerva Mills), writs (habeas corpus, mandamus, prohibition, certiorari, quo warranto), 11 Fundamental Duties added by 42nd Amendment (Art.51A), 86th Amendment adding 12th duty (education of children), Verma Committee on Fundamental Duties.`
  },
  {
    key: 'directive-principles-of-state-policy-dpsp',
    titleEn: 'Directive Principles of State Policy (DPSP)',
    titleHi: 'राज्य के नीति निदेशक तत्व (DPSP)',
    breadEn: 'Directive Principles (DPSP)',
    breadHi: 'नीति निदेशक तत्व',
    descEn: 'Comprehensive study guide covering Directive Principles of State Policy (Articles 36-51), their classification, and relationship with Fundamental Rights for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए राज्य के नीति निदेशक तत्व (अनुच्छेद 36-51), उनका वर्गीकरण और मौलिक अधिकारों से संबंध की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Directive Principles of State Policy DPSP" (राज्य के नीति निदेशक तत्व). Cover: Articles 36-51, source (Irish Constitution), non-justiciable nature, classification (Socialistic, Gandhian, Liberal-Intellectual principles), all important articles (Art.39A legal aid, Art.40 Gram Panchayats, Art.44 Uniform Civil Code, Art.45 free education, Art.47 prohibition, Art.48 cow slaughter, Art.48A environment, Art.50 separation of judiciary), DPSP vs Fundamental Rights conflict (State of Madras vs Champakam Dorairajan, Golaknath case, 25th Amendment, Minerva Mills), 42nd & 44th Amendments and DPSP.`
  },
  {
    key: 'union-executive-president-pm-council-of-ministers',
    titleEn: 'Union Executive: President, PM & Council of Ministers',
    titleHi: 'संघ कार्यपालिका: राष्ट्रपति, प्रधानमंत्री एवं मंत्रिपरिषद',
    breadEn: 'Union Executive',
    breadHi: 'संघ कार्यपालिका',
    descEn: 'Comprehensive study guide covering the Union Executive - President, Vice-President, Prime Minister, and Council of Ministers for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए संघ कार्यपालिका - राष्ट्रपति, उपराष्ट्रपति, प्रधानमंत्री और मंत्रिपरिषद की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Union Executive: President, Vice President, Prime Minister and Council of Ministers" (संघ कार्यपालिका). Cover: President (election by Electoral College Art.54-55, qualifications, term 5 years, impeachment Art.61, powers - executive/legislative/financial/judicial/emergency/military, veto powers/pocket veto, ordinance power Art.123, pardoning powers Art.72), Vice-President (Art.63-71, ex-officio Chairman of Rajya Sabha), Prime Minister (Art.74-75, appointment, powers, relation with President and Cabinet), Council of Ministers (collective responsibility Art.75, individual responsibility, cabinet committees), Attorney General of India (Art.76).`
  },
  {
    key: 'union-legislature-parliament-lok-sabha-rajya-sabha',
    titleEn: 'Union Legislature: Parliament, Lok Sabha & Rajya Sabha',
    titleHi: 'संघ विधायिका: संसद, लोक सभा एवं राज्य सभा',
    breadEn: 'Union Legislature',
    breadHi: 'संघ विधायिका',
    descEn: 'Comprehensive study guide covering Parliament, Lok Sabha, Rajya Sabha, legislative process, and parliamentary procedures for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए संसद, लोक सभा, राज्य सभा, विधायी प्रक्रिया और संसदीय प्रक्रियाओं की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Union Legislature: Parliament, Lok Sabha and Rajya Sabha" (संघ विधायिका). Cover: Composition of Lok Sabha (543+2, Art.81), Rajya Sabha (250, 12 nominated, Art.80), speaker and deputy speaker, Rajya Sabha Chairman, sessions (Budget, Monsoon, Winter), quorum, joint sitting (Art.108), types of bills (ordinary, money bill Art.110, financial bill, constitutional amendment bill Art.368), Speaker's role, parliamentary privileges (Art.105), no-confidence motion, question hour, zero hour, adjournment motion, calling attention motion, Parliamentary Committees (PAC, Estimates, Public Undertakings), Budget process.`
  },
  {
    key: 'state-executive-legislature',
    titleEn: 'State Executive & Legislature',
    titleHi: 'राज्य कार्यपालिका एवं विधायिका',
    breadEn: 'State Executive & Legislature',
    breadHi: 'राज्य कार्यपालिका और विधायिका',
    descEn: 'Comprehensive study guide covering State Executive (Governor, CM, Council of Ministers) and State Legislature (Vidhan Sabha, Vidhan Parishad) for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए राज्य कार्यपालिका (राज्यपाल, मुख्यमंत्री, मंत्रिपरिषद) और राज्य विधायिका (विधान सभा, विधान परिषद) की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "State Executive and Legislature" (राज्य कार्यपालिका एवं विधायिका). Cover: Governor (Art.153-162, appointment by President, discretionary powers, Art.200 reserving bills, Art.356 President's Rule recommendation), Chief Minister and State Council of Ministers, collective responsibility, Advocate General (Art.165), State Legislature - Vidhan Sabha (Art.170, maximum 500 minimum 60), Vidhan Parishad (Art.171, states having Vidhan Parishad - UP included, composition 1/3+1/6+1/12+1/12+governor nominees), legislative process at state level, special status states (Art.371).`
  },
  {
    key: 'judiciary-supreme-court-high-courts-subordinate-courts',
    titleEn: 'Judiciary: Supreme Court, High Courts & Subordinate Courts',
    titleHi: 'न्यायपालिका: सर्वोच्च न्यायालय, उच्च न्यायालय एवं अधीनस्थ न्यायालय',
    breadEn: 'Judiciary',
    breadHi: 'न्यायपालिका',
    descEn: 'Comprehensive study guide covering the Indian Judiciary - Supreme Court, High Courts, and Subordinate Courts for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए भारतीय न्यायपालिका - सर्वोच्च न्यायालय, उच्च न्यायालय और अधीनस्थ न्यायालयों की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Judiciary: Supreme Court, High Courts and Subordinate Courts" (न्यायपालिका). Cover: Supreme Court (Art.124-147, establishment 1950, composition - CJI + judges, qualifications, removal by impeachment, jurisdiction - original/appellate/advisory/writ, Art.137 review power), High Courts (Art.214-231, writ jurisdiction Art.226, supervisory jurisdiction Art.227), District Courts and subordinate courts, Lok Adalats, PIL (Public Interest Litigation), judicial review, judicial activism, independence of judiciary - security of tenure, fixed service conditions, contempt of court power, key landmark judgments.`
  },
  {
    key: 'emergency-provisions',
    titleEn: 'Emergency Provisions',
    titleHi: 'आपातकालीन प्रावधान',
    breadEn: 'Emergency Provisions',
    breadHi: 'आपातकालीन प्रावधान',
    descEn: 'Comprehensive study guide covering all three types of Emergency Provisions (National, State, Financial) under the Indian Constitution for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए भारतीय संविधान के तीनों प्रकार के आपातकालीन प्रावधानों (राष्ट्रीय, राज्य, वित्तीय) की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Emergency Provisions in Indian Constitution" (आपातकालीन प्रावधान). Cover: National Emergency Art.352 (grounds - war/external aggression/armed rebellion, proclamation, approval 2/3 majority + absolute majority, duration, effects on Centre-State relations and Fundamental Rights, past emergencies 1962/1971/1975), President's Rule Art.356 (grounds, approval, duration 6 months extendable to maximum 3 years, 44th Amendment safeguards, Bommai case 1994), Financial Emergency Art.360 (grounds, effects, never imposed), 44th Amendment changes to emergency provisions.`
  },
  {
    key: 'amendment-of-the-constitution-basic-structure',
    titleEn: 'Amendment of the Constitution & Basic Structure Doctrine',
    titleHi: 'संविधान संशोधन एवं मूल ढांचा सिद्धांत',
    breadEn: 'Constitutional Amendment',
    breadHi: 'संविधान संशोधन',
    descEn: 'Comprehensive study guide covering constitutional amendment procedures (Article 368) and the Basic Structure Doctrine for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए संवैधानिक संशोधन प्रक्रिया (अनुच्छेद 368) और मूल ढांचा सिद्धांत की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Amendment of the Constitution and Basic Structure Doctrine" (संविधान संशोधन एवं मूल ढांचा सिद्धांत). Cover: Article 368 (procedure for amendment), three methods (simple majority, special majority, special majority + state ratification), Golaknath case 1967, 24th Amendment, Kesavananda Bharati case 1973 (Basic Structure doctrine), Indira Gandhi vs Raj Narain case, Minerva Mills case 1980, 42nd Amendment (Mini Constitution) and 44th Amendment, important constitutional amendments (1st, 7th, 24th, 25th, 42nd, 44th, 52nd, 61st, 73rd, 74th, 86th, 91st, 99th, 101st, 102nd, 103rd), basic structure elements identified by Supreme Court.`
  },
  {
    key: 'constitutional-non-constitutional-bodies',
    titleEn: 'Constitutional & Non-Constitutional Bodies',
    titleHi: 'संवैधानिक एवं गैर-संवैधानिक निकाय',
    breadEn: 'Constitutional & Non-Constitutional Bodies',
    breadHi: 'संवैधानिक और गैर-संवैधानिक निकाय',
    descEn: 'Comprehensive study guide covering all Constitutional and Non-Constitutional bodies in India for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए भारत के सभी संवैधानिक और गैर-संवैधानिक निकायों की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Constitutional and Non-Constitutional Bodies in India" (संवैधानिक एवं गैर-संवैधानिक निकाय). Cover: Constitutional Bodies - Election Commission (Art.324), UPSC (Art.315-323), CAG (Art.148-151), Finance Commission (Art.280), National Commission for SC (Art.338), National Commission for ST (Art.338A); Non-Constitutional/Statutory Bodies - NHRC, NITI Aayog (vs Planning Commission), CBI, CVC, National Commission for Women, National Commission for Minorities, National Commission for Backward Classes; Inter-State Council (Art.263), Zonal Councils, NDC. Include composition, functions, powers and appointment process for each.`
  },
  {
    key: 'lokpal-and-lokayukta',
    titleEn: 'Lokpal & Lokayukta',
    titleHi: 'लोकपाल एवं लोकायुक्त',
    breadEn: 'Lokpal & Lokayukta',
    breadHi: 'लोकपाल और लोकायुक्त',
    descEn: 'Comprehensive study guide covering Lokpal (national level) and Lokayukta (state level) anti-corruption institutions for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए लोकपाल (राष्ट्रीय स्तर) और लोकायुक्त (राज्य स्तर) भ्रष्टाचार विरोधी संस्थाओं की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Lokpal and Lokayukta" (लोकपाल एवं लोकायुक्त). Cover: Background (First ARC 1966 recommendation), Lokpal Bill history (introduction 1968, repeated lapsing), Anna Hazare movement 2011, Lokpal and Lokayuktas Act 2013, composition (1 chairperson + 8 members, half judicial), jurisdiction (PM under conditions, Union Ministers, MPs, Group A/B/C/D officers), powers and functions, Lokayukta in states (first - Maharashtra 1971, UP Lokayukta), UP Lokayukta Act 1975, difference between Lokpal and Lokayukta.`
  },
  {
    key: 'right-to-information-rti-act',
    titleEn: 'Right to Information (RTI) Act',
    titleHi: 'सूचना का अधिकार अधिनियम (RTI)',
    breadEn: 'RTI Act',
    breadHi: 'RTI अधिनियम',
    descEn: 'Comprehensive study guide covering the Right to Information Act 2005, its provisions, and implementation for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए सूचना का अधिकार अधिनियम 2005, उसके प्रावधान और कार्यान्वयन की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Right to Information RTI Act 2005" (सूचना का अधिकार अधिनियम). Cover: Background (Freedom of Information Act 2002, RTI Act 2005 came into force 12 Oct 2005), key provisions - definition of information, Public Information Officers (PIO), First Appellate Authority, Central/State Information Commissions (CIC/SIC), time limit for providing information (30 days, 48 hours if life/liberty), Section 8 exemptions (10 categories), Section 24 (security/intelligence organizations exempt), fees and appeal process, penalties (Rs.250/day max Rs.25000), proactive disclosure Section 4, RTI Amendment Act 2019, state of RTI in Uttar Pradesh.`
  },
  {
    key: 'official-language-provisions',
    titleEn: 'Official Language Provisions',
    titleHi: 'राजभाषा संबंधी प्रावधान',
    breadEn: 'Official Language Provisions',
    breadHi: 'राजभाषा प्रावधान',
    descEn: 'Comprehensive study guide covering Official Language provisions (Articles 343-351) of the Indian Constitution for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए भारतीय संविधान के राजभाषा प्रावधानों (अनुच्छेद 343-351) की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Official Language Provisions in Indian Constitution" (राजभाषा संबंधी प्रावधान). Cover: Part XVII of Constitution (Art.343-351), Art.343 (Hindi in Devanagari script as Official Language of Union), Art.344 (Official Language Commission), Art.345-347 (official language of states), Art.348 (language of Supreme Court and High Courts - English), Art.350 (language for grievances), Art.350A (mother tongue instruction), Art.350B (Special Officer for linguistic minorities), Art.351 (directive for development of Hindi), Eighth Schedule (22 languages), Official Languages Act 1963, Three Language Formula, Commissioner for Linguistic Minorities, Hindi Divas 14 September.`
  },
  {
    key: '73rd-constitutional-amendment-act-panchayati-raj',
    titleEn: '73rd Constitutional Amendment Act – Panchayati Raj',
    titleHi: '73वाँ संविधान संशोधन अधिनियम – पंचायती राज',
    breadEn: '73rd Amendment – Panchayati Raj',
    breadHi: '73वाँ संशोधन – पंचायती राज',
    descEn: 'Comprehensive study guide covering the 73rd Constitutional Amendment Act 1992 (Panchayati Raj) for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए 73वें संविधान संशोधन अधिनियम 1992 (पंचायती राज) की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "73rd Constitutional Amendment Act 1992 Panchayati Raj" (73वाँ संविधान संशोधन – पंचायती राज). Cover: Background (Balwant Rai Mehta Committee 1957, Ashok Mehta Committee 1977, L M Singhvi Committee 1986), 73rd Amendment 1992 (added Part IX Art.243-243O and 11th Schedule), three-tier structure (Gram Panchayat, Panchayat Samiti/Intermediate, Zila Parishad), 29 subjects in 11th Schedule, State Finance Commission (Art.243I), State Election Commission (Art.243K), reservations (1/3 for women, SC/ST proportional), Gram Sabha, status in UP (UP Panchayat Raj Act), Gram Pradhan, Kshetra Panchayat, Zila Panchayat in UP.`
  },
  {
    key: '74th-constitutional-amendment-act-municipalities',
    titleEn: '74th Constitutional Amendment Act – Municipalities',
    titleHi: '74वाँ संविधान संशोधन अधिनियम – नगरपालिकाएं',
    breadEn: '74th Amendment – Municipalities',
    breadHi: '74वाँ संशोधन – नगरपालिकाएं',
    descEn: 'Comprehensive study guide covering the 74th Constitutional Amendment Act 1992 (Urban Local Bodies) for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए 74वें संविधान संशोधन अधिनियम 1992 (शहरी स्थानीय निकाय) की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "74th Constitutional Amendment Act 1992 Urban Local Bodies Municipalities" (74वाँ संविधान संशोधन – नगरपालिकाएं). Cover: 74th Amendment 1992 (added Part IX-A Art.243P-243ZG and 12th Schedule), types of Urban Local Bodies (Nagar Panchayat, Municipal Council/Nagar Palika Parishad, Municipal Corporation/Nagar Nigam), 18 subjects in 12th Schedule, Ward Committees, Metropolitan Planning Committees (Art.243ZE), District Planning Committees (Art.243ZD), reservations for women (1/3) and SC/ST, State Finance Commission, UP Urban Bodies, Lucknow Nagar Nigam, Mayor, Nagar Ayukta.`
  },
  {
    key: 'evolution-committees-balwant-rai-mehta-ashok-mehta',
    titleEn: 'Evolution & Committees: Balwant Rai Mehta & Ashok Mehta',
    titleHi: 'विकास एवं समितियां: बलवंत राय मेहता और अशोक मेहता',
    breadEn: 'PR Evolution & Committees',
    breadHi: 'पंचायती राज विकास और समितियां',
    descEn: 'Comprehensive study guide covering the evolution of Panchayati Raj and key committees (Balwant Rai Mehta, Ashok Mehta, L.M. Singhvi) for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए पंचायती राज के विकास और प्रमुख समितियों (बलवंत राय मेहता, अशोक मेहता, एल.एम. सिंघवी) की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Evolution of Panchayati Raj: Balwant Rai Mehta Committee, Ashok Mehta Committee and other committees" (पंचायती राज का विकास). Cover: Pre-independence background (Ripon's Resolution 1882), Constituent Assembly debate, CDP 1952, Balwant Rai Mehta Committee 1957 (three-tier Panchayati Raj, Rajasthan first 1959), Ashok Mehta Committee 1977 (two-tier system, district level primary unit, mandatory seats for weaker sections), G.V.K. Rao Committee 1985, L.M. Singhvi Committee 1986 (constitutional status to PR), P.K. Thungon Committee 1989, 64th Constitutional Amendment Bill (failed), 73rd Amendment 1992, comparative table of all committee recommendations.`
  },
  {
    key: 'community-development-programme-cdp-1952',
    titleEn: 'Community Development Programme (CDP) 1952',
    titleHi: 'सामुदायिक विकास कार्यक्रम (CDP) 1952',
    breadEn: 'Community Development Programme',
    breadHi: 'सामुदायिक विकास कार्यक्रम',
    descEn: 'Comprehensive study guide covering the Community Development Programme 1952, its implementation, success, and failure for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए सामुदायिक विकास कार्यक्रम 1952, इसके कार्यान्वयन, सफलता और विफलता की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Community Development Programme CDP 1952" (सामुदायिक विकास कार्यक्रम 1952). Cover: Background and genesis (Etawah Pilot Project 1948 by Albert Mayer, Nilokheri experiment), CDP launched on 2 October 1952 (Gandhi Jayanti), objectives (all-round development of rural areas), structure (Development Block - BDO, Gram Sevak, Block Advisory Committee), National Extension Service (NES) 1953, achievements (roads, schools, wells, agricultural extension), failures (top-down approach, bypassing Panchayats, benefits to rich farmers), Paul committee (1960 evaluation), Balwant Rai Mehta Committee criticism and shift to Panchayati Raj model.`
  },
  {
    key: 'pesa-act-1996',
    titleEn: 'PESA Act 1996 (Panchayats Extension to Scheduled Areas)',
    titleHi: 'पेसा अधिनियम 1996 (अनुसूचित क्षेत्रों में पंचायतों का विस्तार)',
    breadEn: 'PESA Act 1996',
    breadHi: 'पेसा अधिनियम 1996',
    descEn: 'Comprehensive study guide covering PESA Act 1996 (Panchayats Extension to Scheduled Areas Act) for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए पेसा अधिनियम 1996 (अनुसूचित क्षेत्रों में पंचायतों का विस्तार अधिनियम) की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "PESA Act 1996 - Panchayats Extension to Scheduled Areas" (पेसा अधिनियम 1996). Cover: Background (73rd Amendment did not automatically extend to Scheduled/Fifth Schedule areas), Bhuria Committee 1994-95 recommendations, PESA Act 1996, applicability (10 states with Fifth Schedule areas - Andhra Pradesh, Telangana, Chhattisgarh, Gujarat, Himachal Pradesh, Jharkhand, Madhya Pradesh, Maharashtra, Odisha, Rajasthan), key provisions (Gram Sabha as competent authority, rights over minor forest produce, land acquisition consent, money lending regulation, management of markets, control over intoxicants, ownership rights), significance for tribal self-governance.`
  },
  {
    key: 'public-policy-formulation-implementation',
    titleEn: 'Public Policy: Formulation & Implementation',
    titleHi: 'सार्वजनिक नीति: निर्माण एवं क्रियान्वयन',
    breadEn: 'Public Policy',
    breadHi: 'सार्वजनिक नीति',
    descEn: 'Comprehensive study guide covering Public Policy formulation, implementation, evaluation, and key welfare policies for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए सार्वजनिक नीति निर्माण, क्रियान्वयन, मूल्यांकन और प्रमुख कल्याण नीतियों की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Public Policy: Formulation and Implementation" (सार्वजनिक नीति: निर्माण एवं क्रियान्वयन). Cover: Concept of public policy (definition, types - distributive, redistributive, regulatory, constituent), policy cycle (agenda-setting, formulation, legitimation, implementation, evaluation), actors in policy making (legislature, executive, judiciary, bureaucracy, pressure groups, media), implementation challenges (gap between policy and outcome, bureaucratic hurdles, resource constraints), policy evaluation (ex-ante and ex-post), key welfare policies in India (MGNREGS, National Food Security Act, Ayushman Bharat, PM Awas Yojana, Swachh Bharat Mission), role of NITI Aayog in policy formulation, Planning Commission vs NITI Aayog.`
  },
  {
    key: 'various-welfare-schemes-for-vulnerable-sections',
    titleEn: 'Various Welfare Schemes for Vulnerable Sections',
    titleHi: 'कमजोर वर्गों के लिए विभिन्न कल्याण योजनाएं',
    breadEn: 'Welfare Schemes for Vulnerable Sections',
    breadHi: 'कमजोर वर्गों के लिए कल्याण योजनाएं',
    descEn: 'Comprehensive study guide covering government welfare schemes for SC, ST, OBC, women, children, disabled, and elderly for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए SC, ST, OBC, महिलाओं, बच्चों, दिव्यांगों और वृद्धों के लिए सरकारी कल्याण योजनाओं की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Welfare Schemes for Vulnerable Sections in India" (कमजोर वर्गों के लिए कल्याण योजनाएं). Cover: Constitutional provisions for marginalized sections (Art.15(4), 16(4), 17, 46), schemes for SC/ST (Scheduled Castes Sub Plan, Post-Matric Scholarship, Ambedkar Gram Sabha Vikas Yojana), welfare for women (Beti Bachao Beti Padhao, Sukanya Samriddhi Yojana, Ujjwala Yojana, Mahila Shakti Kendra, One Stop Centres), child welfare (ICDS, POSHAN Abhiyaan, PM POSHAN), schemes for elderly (PM Vaya Vandana Yojana, IGNOAPS), for disabled (RPwD Act 2016, ADIP Scheme), UP-specific schemes (Kanya Sumangala Yojana, Vridhavastha Pension, Divyang Pension), OBC welfare schemes.`
  },
  {
    key: 'role-of-ngos-and-shgs',
    titleEn: 'Role of NGOs and Self Help Groups (SHGs)',
    titleHi: 'NGOs और स्वयं सहायता समूहों (SHGs) की भूमिका',
    breadEn: 'Role of NGOs & SHGs',
    breadHi: 'NGO और SHG की भूमिका',
    descEn: 'Comprehensive study guide covering the role of NGOs and Self Help Groups in rural development and governance for UPSSSC Lower Mains.',
    descHi: 'UPSSSC लोअर मेन्स के लिए ग्रामीण विकास और शासन में NGO और स्वयं सहायता समूहों की भूमिका की व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Role of NGOs and Self Help Groups SHGs in Governance and Rural Development" (NGO और स्वयं सहायता समूहों की भूमिका). Cover: Definition and types of NGOs, legal framework (Societies Registration Act 1860, FCRA 2010), NGO roles (service delivery, advocacy, watchdog, capacity building), challenges for NGOs (FCRA restrictions, accountability), Self Help Groups definition (10-20 members, microfinance), SHG-Bank Linkage Programme (NABARD 1992), Mahila Samakhya, Kudumbashree (Kerala), SEWA, DAY-NRLM (National Rural Livelihoods Mission), SHGs in UP (State Rural Livelihoods Mission), impact of SHGs on women empowerment, microfinance and SHGs, challenges facing SHGs.`
  }
];

// ─── HTML Template ────────────────────────────────────────────────────────────

function pageShell(topic, theoryHtml) {
  return `<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topic.titleEn} - UPSSSC Lower Mains Polity</title>
    <meta name="description" content="${topic.descEn}">

    <!-- CSS Dependencies -->
    <link
        href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Inter:wght@400;500;600;700&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=05feb74c">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=c323837a">
    <link rel="stylesheet" href="/assets/css/topic-details.min.css?v=7bf51abb">
    <link rel="stylesheet" href="/assets/css/upsssc-lower.min.css?v=9d684fc1">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({startOnLoad:true});</script>
</head>

<body>
    <div class="container">
        <div class="top-controls">
            <button class="lang-toggle-btn" onclick="toggleLang()">A/अ</button>
        </div>

        <div class="breadcrumbs">
            <div class="breadcrumbs-path">
                <a href="../../index.html">Syllabus</a>
                <i class="fas fa-chevron-right"></i>
                <a href="../../index.html#polity">Polity</a>
                <i class="fas fa-chevron-right"></i>
                <span class="lang-en">${topic.breadEn}</span>
                <span class="lang-hi">${topic.breadHi}</span>
            </div>
        </div>

        <div class="topic-header">
            <h1>
                <span class="lang-en">${topic.titleEn}</span>
                <span class="lang-hi">${topic.titleHi}</span>
            </h1>
            <p>
                <span class="lang-en">${topic.descEn}</span>
                <span class="lang-hi">${topic.descHi}</span>
            </p>
        </div>

        <div class="subject-nav">
            <button class="sub-nav-item active" data-tab="theory" onclick="switchTab('theory')">
                <span class="lang-en">Theory &amp; Concepts</span>
                <span class="lang-hi">सिद्धांत और अवधारणाएं</span>
            </button>
            <button class="sub-nav-item" data-tab="practice" onclick="switchTab('practice')">
                <span class="lang-en">Practice (30 Qs)</span>
                <span class="lang-hi">अभ्यास (30 प्रश्न)</span>
            </button>
            <button class="sub-nav-item" data-tab="pyqs" onclick="switchTab('pyqs')">
                <span class="lang-en">UP Gov PYQs</span>
                <span class="lang-hi">यूपी सरकार PYQs</span>
            </button>
            <button class="sub-nav-item" data-tab="test" onclick="switchTab('test')">
                <span class="lang-en">15-Q Test</span>
                <span class="lang-hi">15-प्रश्न टेस्ट</span>
            </button>
        </div>

        <div class="topic-content">

            <div id="tab-theory" class="tab-content" style="display:block">
${theoryHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="practice" onclick="switchTab('practice')">
                        <span class="lang-en">Next: Practice Questions</span>
                        <span class="lang-hi">अगला: अभ्यास प्रश्न</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-practice" class="tab-content" style="display:none">
                <div class="info-banner">
                    <span class="lang-en">Practice questions coming soon! Check back later.</span>
                    <span class="lang-hi">अभ्यास प्रश्न जल्द आ रहे हैं! बाद में देखें।</span>
                </div>
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="pyqs" onclick="switchTab('pyqs')">
                        <span class="lang-en">Next: UP Gov PYQs</span>
                        <span class="lang-hi">अगला: यूपी सरकार PYQs</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-pyqs" class="tab-content" style="display:none">
                <div class="info-banner">
                    <span class="lang-en">Previous Year Questions coming soon!</span>
                    <span class="lang-hi">पिछले वर्ष के प्रश्न जल्द आ रहे हैं!</span>
                </div>
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="test" onclick="switchTab('test')">
                        <span class="lang-en">Next: 15-Q Test</span>
                        <span class="lang-hi">अगला: 15-प्रश्न टेस्ट</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-test" class="tab-content" style="display:none">
                <div class="info-banner">
                    <span class="lang-en">Timed test coming soon!</span>
                    <span class="lang-hi">समयबद्ध टेस्ट जल्द आ रहे हैं!</span>
                </div>
            </div>

        </div>
    </div>

        <script>
            window.upssscTestData = [];
        </script>
        <script src="/assets/js/upsssc-lower.min.js?v=117a746d"></script>
        <script src="/assets/js/main.min.js?v=86340191"></script>
</body>

</html>`;
}

// ─── Gemini Prompt Builder (Theory Only) ─────────────────────────────────────

function buildTheoryPrompt(topic) {
  return `You are an expert UPSSSC Lower Mains exam content creator for Indian Polity & Governance.
Generate ONLY the THEORY/CONCEPTS section for: "${topic.titleEn}" (${topic.titleHi})

IMPORTANT: Return ONLY a valid JSON object. No markdown, no explanation. Just the JSON.

Generate this exact JSON structure:
{
  "theory": "<VERY DETAILED HTML string with 12-18 card-premium divs>"
}

THEORY HTML RULES (CRITICAL - MAKE EXTREMELY DETAILED):
- Use these exact CSS classes: card-premium, card-title, theory-heading, theory-para, theory-highlight, theory-overflow-mb, tab-active-bar, theory-section-sep
- Each card structure: <div class="card-premium"><h3 class="card-title">...</h3>...</div>
- Use <span class="lang-en">English text</span> and <span class="lang-hi">Hindi text</span> for ALL text content
- Use <h4 class="lang-en theory-heading">heading</h4> and <h4 class="lang-hi theory-heading">heading in Hindi</h4> for subheadings
- Use tables with <thead> and <tbody>, add class="tab-active-bar" to <tr> inside <thead>
- Highlight key facts, articles, dates with <div class="theory-highlight"><span class="lang-en">...</span><span class="lang-hi">...</span></div>
- Use <p class="theory-para"><span class="lang-en">...</span><span class="lang-hi">...</span></p> for paragraphs
- MAKE CONTENT EXTREMELY DETAILED:
  * First card MUST contain a Mindmap summarizing the topic. For the mindmap, YOU MUST generate TWO separate Mermaid diagrams: one entirely in English wrapped in <div class="lang-en"><div class="mermaid">...</div></div> and one entirely in Hindi wrapped in <div class="lang-hi"><div class="mermaid">...</div></div>. CRITICAL: Since you are returning JSON, you MUST escape newlines in the Mermaid code as \\n (e.g. <div class="lang-en"><div class="mermaid">mindmap\\n  root((Topic))\\n    Subtopic1</div></div><div class="lang-hi"><div class="mermaid">mindmap\\n  root((विषय))\\n    उपविषय</div></div>).
  * Second card MUST contain a comprehensive Comparison Table summarizing the topic.
  * 12-18 cards covering ALL aspects of the topic
  * Each card must have 3-5 paragraphs with specific facts, article numbers, dates, names
  * Include multiple comparison tables with important data
  * Cover all subtopics exhaustively suitable for UPSSSC Lower Mains and UP PCS
  * Include specific article numbers, committee names, landmark cases, years, statistics
  * Add memory tips and important mnemonics in theory-highlight divs
  * Include special UP-relevant context where applicable

Topic details: ${topic.prompt}

CRITICAL REMINDERS:
1. Theory MUST start with comparison tables and mindmaps/overviews, followed by a detailed explanation.
2. Theory MUST have 12-18 cards with extensive, exam-focused content
3. Include ALL article numbers, important dates, names relevant to the topic
4. Use dual language (English + Hindi) throughout ALL content
5. Make content suitable for UP state government exams (UPSSSC Lower Mains, UP PCS)
6. Include landmark Supreme Court cases, important amendments, committee names with chairpersons
7. Add comparison tables wherever relevant (comparing different acts, bodies, provisions)`;
}

// ─── Model Pool ───────────────────────────────────────────────────────────────
const MODEL_POOL = [
  'gemini-3.1-flash-lite',   // Primary: Gemini 3.1 Flash Lite (as requested)
  'gemini-3.5-flash',        // Fallback: Gemini 3.5 Flash
];

// ─── Main Generator ───────────────────────────────────────────────────────────

async function generateTopic(topic) {
  console.log(`\n Generating theory for: ${topic.titleEn}...`);

  const prompt = buildTheoryPrompt(topic);

  let raw;
  const MAX_RETRIES = MODEL_POOL.length * 2; // 4 attempts total
  const BASE_DELAY = 15000; // 15s between retries (free tier needs breathing room)

  for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
    const model = MODEL_POOL[attempt % MODEL_POOL.length];
    try {
      console.log(`  -> Using model: ${model} (attempt ${attempt + 1}/${MAX_RETRIES})`);
      const response = await ai.models.generateContent({
        model,
        contents: prompt,
        config: {
          thinkingConfig: { thinkingBudget: 0 },
          temperature: 0.7,
          maxOutputTokens: 65536
        }
      });
      raw = response.text;
      console.log(`  OK Got response from ${model}`);
      break; // success
    } catch (err) {
      const isRetryable = err.message && (
        err.message.includes('503') ||
        err.message.includes('UNAVAILABLE') ||
        err.message.includes('high demand') ||
        err.message.includes('overloaded') ||
        err.message.includes('429') ||
        err.message.includes('RESOURCE_EXHAUSTED')
      );
      if (isRetryable && attempt < MAX_RETRIES - 1) {
        const delay = BASE_DELAY * (attempt + 1);
        console.log(`  WARN ${model} error (attempt ${attempt + 1}) -> switching model in ${delay / 1000}s...`);
        await new Promise(r => setTimeout(r, delay));
      } else {
        console.error(`  FAIL All models failed for ${topic.key}:`, err.message);
        throw err;
      }
    }
  }

  // Extract JSON from response (handle markdown code blocks)
  let jsonStr = raw.trim();
  // Strip markdown code fences if present
  jsonStr = jsonStr.replace(/^```(?:json)?\n?/m, '').replace(/\n?```$/m, '');

  let data;
  try {
    data = JSON.parse(jsonStr);
  } catch (e) {
    // Try to extract JSON object
    const match = jsonStr.match(/\{[\s\S]*\}/);
    if (match) {
      try { data = JSON.parse(match[0]); }
      catch (e2) {
        console.error(`  FAIL JSON parse failed for ${topic.key}`);
        console.error('  Raw (first 500):', jsonStr.substring(0, 500));
        throw e2;
      }
    } else {
      throw e;
    }
  }

  const theoryHtml = data.theory || '<p>Content generation failed. Please retry.</p>';
  const html = pageShell(topic, theoryHtml);

  const outDir = path.join(BASE, topic.key);
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
  const outFile = path.join(outDir, 'index.html');
  fs.writeFileSync(outFile, html, 'utf8');

  const sizeKB = Math.round(html.length / 1024);
  console.log(`  OK Written: polity/${topic.key}/index.html (${sizeKB} KB)`);
}

async function main() {
  console.log('=== UPSSSC Lower Mains Polity Theory Generator ===');
  console.log(`Using Gemini API Key: ${API_KEY ? API_KEY.substring(0, 10) + '...' : 'NOT FOUND'}`);
  console.log('Mode: THEORY ONLY (Practice/PYQ/Test = placeholder)\n');

  if (!API_KEY) {
    console.error('ERROR: GEMINI_API_KEY not found in .env');
    process.exit(1);
  }

  // Support RETRY_KEYS env var to re-run only specific topics
  // e.g. RETRY_KEYS=salient-features-preamble,emergency-provisions node scripts/gen_polity_pages.js
  const retryKeys = process.env.RETRY_KEYS
    ? process.env.RETRY_KEYS.split(',').map(k => k.trim())
    : null;
  const topicsToRun = retryKeys
    ? TOPICS.filter(t => retryKeys.includes(t.key))
    : TOPICS;

  if (retryKeys) console.log(`Retrying only: ${retryKeys.join(', ')}`);
  console.log(`Topics to generate: ${topicsToRun.length}`);

  const failed = [];
  for (const topic of topicsToRun) {
    try {
      await generateTopic(topic);
      // Delay between API calls to avoid rate limiting
      await new Promise(r => setTimeout(r, 12000));
    } catch (err) {
      console.error(`  FAIL Failed: ${topic.key} - ${err.message}`);
      failed.push(topic.key);
    }
  }

  console.log('\n=== Generation Complete ===');
  if (failed.length > 0) {
    console.log(`Failed topics (${failed.length}): ${failed.join(', ')}`);
    console.log(`\nRetry with:`);
    console.log(`  RETRY_KEYS=${failed.join(',')} node scripts/gen_polity_pages.js`);
  } else {
    console.log('All polity theory pages generated successfully!');
  }
}

main().catch(console.error);
