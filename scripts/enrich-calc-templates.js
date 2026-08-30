import fs from 'fs';
import path from 'path';

const ftaPath = path.resolve('learning/data/class-10/mathematics/chapter-1-real-numbers/fta.json');
const data = JSON.parse(fs.readFileSync(ftaPath, 'utf8'));

// Type 2 Templates
const t2Templates = {
  "fta_t2_p01_7_11_13": [
    {
      step_number: 1,
      calc_prompt: "Enter the common factor and resulting simplified factor:",
      calc_template: {
        format_latex: "7 \\times 11 \\times 13 + 13 = \\boxed{\\text{Factor 1}} \\times \\boxed{\\text{Factor 2}}",
        fields: [
          { key: "f1", label: "Common Factor", placeholder: "e.g. 13", expected: 13 },
          { key: "f2", label: "Resulting Factor (7×11+1)", placeholder: "e.g. 78", expected: 78 }
        ]
      }
    },
    {
      step_number: 2,
      calc_prompt: "Enter the two factors greater than 1 that prove the number is composite:",
      calc_template: {
        format_latex: "\\text{Two factors } > 1 \\text{ are } \\boxed{?} \\text{ and } \\boxed{?}",
        fields: [
          { key: "f1", label: "Factor 1", placeholder: "e.g. 13", expected: 13, pair_group: "factors_13_78" },
          { key: "f2", label: "Factor 2", placeholder: "e.g. 78", expected: 78, pair_group: "factors_13_78" }
        ]
      }
    }
  ],
  "fta_t2_p02_factorial5": [
    {
      step_number: 1,
      calc_prompt: "Enter the common factor and resulting simplified factor:",
      calc_template: {
        format_latex: "7 \\times 6 \\times 5 \\times 4 \\times 3 \\times 2 \\times 1 + 5 = \\boxed{\\text{Factor 1}} \\times \\boxed{\\text{Factor 2}}",
        fields: [
          { key: "f1", label: "Common Factor", placeholder: "e.g. 5", expected: 5 },
          { key: "f2", label: "Resulting Factor (1008+1)", placeholder: "e.g. 1009", expected: 1009 }
        ]
      }
    },
    {
      step_number: 2,
      calc_prompt: "Enter the two factors greater than 1 that prove the number is composite:",
      calc_template: {
        format_latex: "\\text{Two factors } > 1 \\text{ are } \\boxed{?} \\text{ and } \\boxed{?}",
        fields: [
          { key: "f1", label: "Factor 1", placeholder: "e.g. 5", expected: 5, pair_group: "factors_5_1009" },
          { key: "f2", label: "Factor 2", placeholder: "e.g. 1009", expected: 1009, pair_group: "factors_5_1009" }
        ]
      }
    }
  ],
  "fta_t2_p03_5_7_11": [
    {
      step_number: 1,
      calc_prompt: "Enter the common factor and resulting simplified factor:",
      calc_template: {
        format_latex: "5 \\times 7 \\times 11 + 7 = \\boxed{\\text{Factor 1}} \\times \\boxed{\\text{Factor 2}}",
        fields: [
          { key: "f1", label: "Common Factor", placeholder: "e.g. 7", expected: 7 },
          { key: "f2", label: "Resulting Factor (55+1)", placeholder: "e.g. 56", expected: 56 }
        ]
      }
    },
    {
      step_number: 2,
      calc_prompt: "Enter the two factors greater than 1 that prove the number is composite:",
      calc_template: {
        format_latex: "\\text{Two factors } > 1 \\text{ are } \\boxed{?} \\text{ and } \\boxed{?}",
        fields: [
          { key: "f1", label: "Factor 1", placeholder: "e.g. 7", expected: 7, pair_group: "factors_7_56" },
          { key: "f2", label: "Factor 2", placeholder: "e.g. 56", expected: 56, pair_group: "factors_7_56" }
        ]
      }
    }
  ]
};

// Type 3 Templates
const t3Templates = {
  "fta_t3_p01_6n": [
    {
      step_number: 1,
      calc_prompt: "Which two prime factors must a number contain to end in digit 0 (since 10 = 2 × 5)?",
      calc_template: {
        format_latex: "10 = \\boxed{\\text{Prime 1}} \\times \\boxed{\\text{Prime 2}}",
        fields: [
          { key: "f1", label: "Prime 1", placeholder: "e.g. 2", expected: 2, pair_group: "primes_2_5" },
          { key: "f2", label: "Prime 2", placeholder: "e.g. 5", expected: 5, pair_group: "primes_2_5" }
        ]
      }
    },
    {
      step_number: 2,
      calc_prompt: "Enter the two prime factors of the base 6 (6 = 2 × 3):",
      calc_template: {
        format_latex: "6 = \\boxed{\\text{Prime 1}} \\times \\boxed{\\text{Prime 2}} \\implies 6^n = (\\boxed{\\text{Prime 1}} \\times \\boxed{\\text{Prime 2}})^n",
        fields: [
          { key: "f1", label: "Prime 1", placeholder: "e.g. 2", expected: 2, pair_group: "primes_2_3" },
          { key: "f2", label: "Prime 2", placeholder: "e.g. 3", expected: 3, pair_group: "primes_2_3" }
        ]
      }
    },
    {
      step_number: 3,
      calc_prompt: "Which required prime factor is missing from 6ⁿ for it to end with 0?",
      calc_template: {
        format_latex: "\\text{Missing prime factor required to end in 0} = \\boxed{?}",
        fields: [
          { key: "f1", label: "Missing Prime", placeholder: "e.g. 5", expected: 5 }
        ]
      }
    }
  ],
  "fta_t3_p02_4n": [
    {
      step_number: 1,
      calc_prompt: "Which prime factor (besides 2) is strictly required to end with digit 0?",
      calc_template: {
        format_latex: "\\text{Mandatory prime factor to end in 0} = \\boxed{?}",
        fields: [
          { key: "f1", label: "Required Prime", placeholder: "e.g. 5", expected: 5 }
        ]
      }
    },
    {
      step_number: 2,
      calc_prompt: "Enter the base prime factor of 4 (4 = 2²):",
      calc_template: {
        format_latex: "4 = \\boxed{\\text{Prime}}^2 \\implies 4^n = (\\boxed{\\text{Prime}}^2)^n",
        fields: [
          { key: "f1", label: "Base Prime", placeholder: "e.g. 2", expected: 2 }
        ]
      }
    },
    {
      step_number: 3,
      calc_prompt: "Which required prime factor is missing from 4ⁿ?",
      calc_template: {
        format_latex: "\\text{Missing prime factor} = \\boxed{?}",
        fields: [
          { key: "f1", label: "Missing Prime", placeholder: "e.g. 5", expected: 5 }
        ]
      }
    }
  ],
  "fta_t3_p03_12n": [
    {
      step_number: 1,
      calc_prompt: "Which prime factor must be present along with 2 to end in 0?",
      calc_template: {
        format_latex: "\\text{Mandatory prime factor to end in 0} = \\boxed{?}",
        fields: [
          { key: "f1", label: "Required Prime", placeholder: "e.g. 5", expected: 5 }
        ]
      }
    },
    {
      step_number: 2,
      calc_prompt: "Enter the two prime factors of the base 12 (12 = 2² × 3):",
      calc_template: {
        format_latex: "12 = \\boxed{\\text{Prime 1}}^2 \\times \\boxed{\\text{Prime 2}}",
        fields: [
          { key: "f1", label: "Prime 1 (squared)", placeholder: "e.g. 2", expected: 2 },
          { key: "f2", label: "Prime 2", placeholder: "e.g. 3", expected: 3 }
        ]
      }
    },
    {
      step_number: 3,
      calc_prompt: "Which required prime factor is missing from 12ⁿ?",
      calc_template: {
        format_latex: "\\text{Missing prime factor} = \\boxed{?}",
        fields: [
          { key: "f1", label: "Missing Prime", placeholder: "e.g. 5", expected: 5 }
        ]
      }
    }
  ]
};

// Type 4 Templates
const t4Templates = {
  "fta_t4_p01_tree42": [
    {
      step_number: 1,
      calc_prompt: "Calculate the unknown node value x (where 42 = 2 × x):",
      calc_template: {
        format_latex: "x = 42 \\div 2 = \\boxed{?}",
        fields: [
          { key: "f1", label: "Value of x", placeholder: "e.g. 21", expected: 21 }
        ]
      }
    },
    {
      step_number: 2,
      calc_prompt: "Calculate the unknown node value y (where 21 = 3 × y):",
      calc_template: {
        format_latex: "y = 21 \\div 3 = \\boxed{?}",
        fields: [
          { key: "f1", label: "Value of y", placeholder: "e.g. 7", expected: 7 }
        ]
      }
    }
  ],
  "fta_t4_p02_tree70": [
    {
      step_number: 1,
      calc_prompt: "Calculate node x from child branches 5 and 7 (x = 5 × 7):",
      calc_template: {
        format_latex: "x = 5 \\times 7 = \\boxed{?}",
        fields: [
          { key: "f1", label: "Value of x", placeholder: "e.g. 35", expected: 35 }
        ]
      }
    },
    {
      step_number: 2,
      calc_prompt: "Calculate node y from child branches 2 and 35 (y = 2 × 35):",
      calc_template: {
        format_latex: "y = 2 \\times 35 = \\boxed{?}",
        fields: [
          { key: "f1", label: "Value of y", placeholder: "e.g. 70", expected: 70 }
        ]
      }
    }
  ],
  "fta_t4_p03_tree1001": [
    {
      step_number: 1,
      calc_prompt: "Calculate unknown node a (where 1001 = 7 × a):",
      calc_template: {
        format_latex: "a = 1001 \\div 7 = \\boxed{?}",
        fields: [
          { key: "f1", label: "Value of a", placeholder: "e.g. 143", expected: 143 }
        ]
      }
    },
    {
      step_number: 2,
      calc_prompt: "Calculate unknown node b (where 143 = 11 × b):",
      calc_template: {
        format_latex: "b = 143 \\div 11 = \\boxed{?}",
        fields: [
          { key: "f1", label: "Value of b", placeholder: "e.g. 13", expected: 13 }
        ]
      }
    }
  ]
};

// Apply templates to fta.json
data.question_types.forEach(qt => {
  qt.pool.forEach(prob => {
    let tplList = null;
    if (t2Templates[prob.id]) tplList = t2Templates[prob.id];
    else if (t3Templates[prob.id]) tplList = t3Templates[prob.id];
    else if (t4Templates[prob.id]) tplList = t4Templates[prob.id];

    if (tplList) {
      tplList.forEach(tpl => {
        const step = prob.steps.find(s => s.step_number === tpl.step_number);
        if (step) {
          step.calc_prompt = tpl.calc_prompt;
          step.calc_template = tpl.calc_template;
        }
      });
    }
  });
});

fs.writeFileSync(ftaPath, JSON.stringify(data, null, 2), 'utf8');
console.log('Successfully enriched all Type 2, 3, 4 steps with numeric calc_template!');
