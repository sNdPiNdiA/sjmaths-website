# Helpers for generating bilingual questions

EN_AR_OPTS = [
    "Both A and R are true and R is the correct explanation of A",
    "Both A and R are true but R is not the correct explanation of A",
    "A is true but R is false",
    "A is false but R is true"
]
HI_AR_OPTS = [
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
    "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है",
    "A सही है लेकिन R गलत है",
    "A गलत है लेकिन R सही है"
]

def add_mcq(sec_en, sec_hi, q_en, q_hi, opts_en, opts_hi, ans, sol_en, sol_hi):
    sec_en.append({"type": "MCQ", "q": q_en, "opts": opts_en, "ans": ans, "sol": sol_en})
    sec_hi.append({"type": "MCQ", "q": q_hi, "opts": opts_hi, "ans": ans, "sol": sol_hi})

def add_multi_mcq(sec_en, sec_hi, q_en, q_hi, opts_en, opts_hi, ans_list, sol_en, sol_hi):
    sec_en.append({"type": "Multiple Correct MCQ", "q": q_en, "opts": opts_en, "ans": ans_list, "sol": sol_en})
    sec_hi.append({"type": "Multiple Correct MCQ", "q": q_hi, "opts": opts_hi, "ans": ans_list, "sol": sol_hi})

def add_tf(sec_en, sec_hi, q_en, q_hi, ans, sol_en, sol_hi):
    sec_en.append({"type": "True/False", "q": q_en, "ans": ans, "sol": sol_en})
    sec_hi.append({"type": "True/False", "q": q_hi, "ans": ans, "sol": sol_hi})

def add_blank(sec_en, sec_hi, q_en, q_hi, ans_en, ans_hi, sol_en, sol_hi):
    sec_en.append({"type": "Fill in the Blank", "q": q_en, "ans": ans_en, "sol": sol_en})
    sec_hi.append({"type": "Fill in the Blank", "q": q_hi, "ans": ans_hi, "sol": sol_hi})

def add_match(sec_en, sec_hi, q_en, q_hi, items_en, items_hi, opts_en, opts_hi, sol_en, sol_hi):
    keys = ['A', 'B', 'C']
    roman = ['I. ', 'II. ', 'III. ']
    items_en_objs = [{"left": roman[i] + items_en[i], "key": keys[i]} for i in range(len(items_en))]
    items_hi_objs = [{"left": roman[i] + items_hi[i], "key": keys[i]} for i in range(len(items_hi))]
    
    options_en_objs = [
        {"val": "B", "text": "A. " + opts_en[1]},
        {"val": "C", "text": "B. " + opts_en[2]},
        {"val": "A", "text": "C. " + opts_en[0]}
    ]
    options_hi_objs = [
        {"val": "B", "text": "A. " + opts_hi[1]},
        {"val": "C", "text": "B. " + opts_hi[2]},
        {"val": "A", "text": "C. " + opts_hi[0]}
    ]
    
    sec_en.append({"type": "Match the Following", "q": q_en, "items": items_en_objs, "options": options_en_objs, "sol": sol_en})
    sec_hi.append({"type": "Match the Following", "q": q_hi, "items": items_hi_objs, "options": options_hi_objs, "sol": sol_hi})

def add_oneliner(sec_en, sec_hi, q_en, q_hi, sol_en, sol_hi):
    sec_en.append({"type": "One-Liner", "q": q_en, "sol": sol_en})
    sec_hi.append({"type": "One-Liner", "q": q_hi, "sol": sol_hi})

def add_ar(sec_en, sec_hi, q_en, q_hi, ans, sol_en, sol_hi):
    sec_en.append({"type": "Assertion-Reason", "q": q_en, "opts": EN_AR_OPTS, "ans": ans, "sol": sol_en})
    sec_hi.append({"type": "Assertion-Reason", "q": q_hi, "opts": HI_AR_OPTS, "ans": ans, "sol": sol_hi})

def add_stmt(sec_en, sec_hi, q_en, q_hi, opts_en, opts_hi, ans, sol_en, sol_hi):
    sec_en.append({"type": "Statement-Based", "q": q_en, "opts": opts_en, "ans": ans, "sol": sol_en})
    sec_hi.append({"type": "Statement-Based", "q": q_hi, "opts": opts_hi, "ans": ans, "sol": sol_hi})

def add_open(sec_en, sec_hi, qtype, q_en, q_hi, sol_en, sol_hi):
    sec_en.append({"type": qtype, "q": q_en, "sol": sol_en})
    sec_hi.append({"type": qtype, "q": q_hi, "sol": sol_hi})
