#!/usr/bin/env python3
"""
generate_topic_json.py

Automated Generator for CBSE Class 10 Mathematics Topic Datasets (Universal Schema v1.0.0).
Powered by Google Gemini 3.7 / 2.5 Flash API.

Features:
- Granular Atomic Steps: Zero step-jumping, single-action progression.
- Dual Calculations Per Step: Vertical math stacking computing 2 values at a time.
- High-Fidelity Distractors: 4 balanced options with diagnostic explanations for common student errors.
- Responsive SVG Diagrams: Inline geometry / coordinate graph diagrams for visual topics.
- CBSE Exam Typologies: Authentic Class 10 Board exam problem types and high-capacity question pools.
- Batch Processing with Resume: Checkpoints completed topics (>25KB) and limits API calls (default 20).
"""

import os
import sys
import json
import time
import re
import warnings
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Any

warnings.filterwarnings("ignore")

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Try importing google.generativeai
try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

# Workspace Root & Topics Base Directory
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
TOPICS_BASE_DIR = WORKSPACE_ROOT / "learning" / "topics" / "class-10" / "mathematics"

# ==============================================================================
# 1. CURRICULUM TOPIC REGISTRY & METADATA
# ==============================================================================
TOPIC_REGISTRY: List[Dict[str, Any]] = [
    # Chapter 1: Real Numbers (Already completed)
    {
        "chapter_folder": "chapter-1-real-numbers",
        "topic_slug": "fta",
        "topic_id": "cbse10-real-numbers-fta",
        "chapter_title": "Chapter 1 - Real Numbers",
        "topic_title": "Fundamental Theorem of Arithmetic",
        "short_title": "FTA",
        "prev_id": None,
        "next_id": "cbse10-real-numbers-hcf-lcm",
        "requires_svg": False,
        "typologies": [
            "Prime factorisation of composite numbers",
            "Checking whether 4^n or 6^n can end with digit 0",
            "Factor tree decomposition and missing factor calculation"
        ]
    },
    {
        "chapter_folder": "chapter-1-real-numbers",
        "topic_slug": "hcf-lcm",
        "topic_id": "cbse10-real-numbers-hcf-lcm",
        "chapter_title": "Chapter 1 - Real Numbers",
        "topic_title": "HCF & LCM by Prime Factorisation",
        "short_title": "HCF & LCM",
        "prev_id": "cbse10-real-numbers-fta",
        "next_id": "cbse10-real-numbers-proof-of-irrationality",
        "requires_svg": False,
        "typologies": [
            "Finding HCF and LCM of 2 and 3 numbers",
            "Verifying HCF(a,b) * LCM(a,b) = a * b and finding unknown",
            "Word problems (meeting times, maximum capacity/tiles)"
        ]
    },
    {
        "chapter_folder": "chapter-1-real-numbers",
        "topic_slug": "proof-of-irrationality",
        "topic_id": "cbse10-real-numbers-proof-of-irrationality",
        "chapter_title": "Chapter 1 - Real Numbers",
        "topic_title": "Proof of Irrationality",
        "short_title": "Irrationality",
        "prev_id": "cbse10-real-numbers-hcf-lcm",
        "next_id": "cbse10-polynomials-zeroes",
        "requires_svg": False,
        "typologies": [
            "Proving sqrt(2), sqrt(3), sqrt(5) is irrational by contradiction",
            "Proving composite expressions (a + b*sqrt(p)) are irrational",
            "Proving fraction forms (a / sqrt(p)) are irrational"
        ]
    },

    # Chapter 2: Polynomials (Already completed)
    {
        "chapter_folder": "chapter-2-polynomials",
        "topic_slug": "zeroes",
        "topic_id": "cbse10-polynomials-zeroes",
        "chapter_title": "Chapter 2 - Polynomials",
        "topic_title": "Geometrical Meaning of Zeroes of a Polynomial",
        "short_title": "Zeroes",
        "prev_id": "cbse10-real-numbers-proof-of-irrationality",
        "next_id": "cbse10-polynomials-zeroes-coefficients",
        "requires_svg": True,
        "typologies": [
            "Identifying number of zeroes from y = p(x) graphs",
            "Finding zeroes of linear polynomials algebraically and graphically",
            "Determining parabolic orientation (a > 0 / a < 0) and intercept properties"
        ]
    },
    {
        "chapter_folder": "chapter-2-polynomials",
        "topic_slug": "zeroes-coefficients",
        "topic_id": "cbse10-polynomials-zeroes-coefficients",
        "chapter_title": "Chapter 2 - Polynomials",
        "topic_title": "Relationship between Zeroes and Coefficients",
        "short_title": "Zeroes & Coefficients",
        "prev_id": "cbse10-polynomials-zeroes",
        "next_id": "cbse10-linear-equations-graphical-consistency",
        "requires_svg": False,
        "typologies": [
            "Factoring quadratic polynomial and verifying sum/product relationships",
            "Forming quadratic polynomial given sum and product of zeroes",
            "Evaluating symmetric expressions (alpha^2 + beta^2, 1/alpha + 1/beta)"
        ]
    },

    # Chapter 3: Pair of Linear Equations in Two Variables
    {
        "chapter_folder": "chapter-3-linear-equations",
        "topic_slug": "graphical-consistency",
        "topic_id": "cbse10-linear-equations-graphical-consistency",
        "chapter_title": "Chapter 3 - Pair of Linear Equations in Two Variables",
        "topic_title": "Consistency & Graphical Interpretation of Linear Systems",
        "short_title": "Consistency",
        "prev_id": "cbse10-polynomials-zeroes-coefficients",
        "next_id": "cbse10-linear-equations-substitution-method",
        "requires_svg": True,
        "typologies": [
            "Testing consistency using ratio comparison (a1/a2, b1/b2, c1/c2)",
            "Finding unknown parameter k for unique, infinite, or no solution",
            "Graphical representation and finding vertices of formed triangle"
        ]
    },
    {
        "chapter_folder": "chapter-3-linear-equations",
        "topic_slug": "substitution-method",
        "topic_id": "cbse10-linear-equations-substitution-method",
        "chapter_title": "Chapter 3 - Pair of Linear Equations in Two Variables",
        "topic_title": "Solving Linear Equations by Substitution Method",
        "short_title": "Substitution",
        "prev_id": "cbse10-linear-equations-graphical-consistency",
        "next_id": "cbse10-linear-equations-elimination-method",
        "requires_svg": False,
        "typologies": [
            "Standard algebraic substitution for linear pairs",
            "Solving pairs with fractional or decimal coefficients",
            "Transformable equations with radicals or bracket expressions"
        ]
    },
    {
        "chapter_folder": "chapter-3-linear-equations",
        "topic_slug": "elimination-method",
        "topic_id": "cbse10-linear-equations-elimination-method",
        "chapter_title": "Chapter 3 - Pair of Linear Equations in Two Variables",
        "topic_title": "Solving Linear Equations by Elimination Method",
        "short_title": "Elimination",
        "prev_id": "cbse10-linear-equations-substitution-method",
        "next_id": "cbse10-linear-equations-linear-word-problems",
        "requires_svg": False,
        "typologies": [
            "Multiplying one equation to equalize coefficients and eliminate variables",
            "Multiplying both equations by non-zero constants to match coefficients",
            "Special symmetric pairs (ax + by = c and bx + ay = d) using addition & subtraction",
            "Pairs with fractional coefficients requiring LCM simplification"
        ]
    },
    {
        "chapter_folder": "chapter-3-linear-equations",
        "topic_slug": "linear-word-problems",
        "topic_id": "cbse10-linear-equations-linear-word-problems",
        "chapter_title": "Chapter 3 - Pair of Linear Equations in Two Variables",
        "topic_title": "Word Problems on Pair of Linear Equations",
        "short_title": "Linear Word Problems",
        "prev_id": "cbse10-linear-equations-elimination-method",
        "next_id": "cbse10-quadratic-equations-standard-form-roots",
        "requires_svg": False,
        "typologies": [
            "Age relationships and linear year progressions",
            "Number and two-digit reversal problems (10x + y vs 10y + x)",
            "Fixed charges vs per-unit / daily costs (taxis, library, hostels)",
            "Speed, distance, time, and upstream / downstream boat problems",
            "Fractions adjustment and geometric dimensions (perimeter and angles)"
        ]
    },

    # Chapter 4: Quadratic Equations
    {
        "chapter_folder": "chapter-4-quadratic-equations",
        "topic_slug": "standard-form-roots",
        "topic_id": "cbse10-quadratic-equations-standard-form-roots",
        "chapter_title": "Chapter 4 - Quadratic Equations",
        "topic_title": "Standard Form of Quadratic Equations & Checking Roots",
        "short_title": "Standard Form",
        "prev_id": "cbse10-linear-equations-linear-word-problems",
        "next_id": "cbse10-quadratic-equations-solving-by-factorisation",
        "requires_svg": False,
        "typologies": [
            "Checking whether given equations represent quadratic equations (a != 0)",
            "Converting complex/fractional algebraic equations into standard form ax^2 + bx + c = 0",
            "Testing whether a given value is a root of the quadratic equation",
            "Finding unknown coefficient k when one root of the quadratic equation is given"
        ]
    },
    {
        "chapter_folder": "chapter-4-quadratic-equations",
        "topic_slug": "solving-by-factorisation",
        "topic_id": "cbse10-quadratic-equations-solving-by-factorisation",
        "chapter_title": "Chapter 4 - Quadratic Equations",
        "topic_title": "Solving Quadratic Equations by Factorisation",
        "short_title": "Factoring",
        "prev_id": "cbse10-quadratic-equations-standard-form-roots",
        "next_id": "cbse10-quadratic-equations-quadratic-formula",
        "requires_svg": False,
        "typologies": [
            "Middle-term splitting with integer coefficients (a = 1)",
            "Middle-term splitting with leading coefficient a > 1 and negative products",
            "Factoring quadratics with irrational square-root coefficients (e.g. sqrt(3)x^2 + 10x + 7sqrt(3) = 0)",
            "Factoring binomial differences of squares and missing linear/constant terms",
            "Fractional algebraic equations reducible to quadratics and solved by factorisation"
        ]
    },
    {
        "chapter_folder": "chapter-4-quadratic-equations",
        "topic_slug": "quadratic-formula",
        "topic_id": "cbse10-quadratic-equations-quadratic-formula",
        "chapter_title": "Chapter 4 - Quadratic Equations",
        "topic_title": "Solving Quadratic Equations using the Quadratic Formula",
        "short_title": "Quadratic Formula",
        "prev_id": "cbse10-quadratic-equations-solving-by-factorisation",
        "next_id": "cbse10-quadratic-equations-nature-of-roots",
        "requires_svg": False,
        "typologies": [
            "Direct application of x = (-b +- sqrt(b^2 - 4ac)) / (2a)",
            "Quadratic equations with large numerical coefficients or fractions",
            "Quadratic equations with square root / radical coefficients",
            "Variable substitution / transformable higher-order equations"
        ]
    },
    {
        "chapter_folder": "chapter-4-quadratic-equations",
        "topic_slug": "nature-of-roots",
        "topic_id": "cbse10-quadratic-equations-nature-of-roots",
        "chapter_title": "Chapter 4 - Quadratic Equations",
        "topic_title": "Nature of Roots & Discriminant Analysis",
        "short_title": "Nature of Roots",
        "prev_id": "cbse10-quadratic-equations-quadratic-formula",
        "next_id": "cbse10-quadratic-equations-quadratic-word-problems",
        "requires_svg": False,
        "typologies": [
            "Determining nature of roots (real & distinct, real & equal, no real roots) using D = b^2 - 4ac",
            "Finding unknown parameter k for two equal real roots (D = 0)",
            "Finding range of k for real roots (D >= 0) or distinct real roots (D > 0)",
            "Quadratic equations with parameter k in leading coefficient (a = k)",
            "Theoretical proofs on roots being rational or real based on coefficient relations"
        ]
    },
    {
        "chapter_folder": "chapter-4-quadratic-equations",
        "topic_slug": "quadratic-word-problems",
        "topic_id": "cbse10-quadratic-equations-quadratic-word-problems",
        "chapter_title": "Chapter 4 - Quadratic Equations",
        "topic_title": "Word Problems Leading to Quadratic Equations",
        "short_title": "Quadratic Word Problems",
        "prev_id": "cbse10-quadratic-equations-nature-of-roots",
        "next_id": "cbse10-ap-basics-nth-term",
        "requires_svg": False,
        "typologies": [
            "Consecutive integer, natural number, and product-difference problems",
            "Geometric areas, perimeter relations, and right-triangle Pythagorean dimensions",
            "Speed, distance, time, and delayed train / flight journey problems",
            "Work rate, pipes and cisterns filling tanks simultaneously",
            "Commercial cost per item vs total expenditure problems"
        ]
    },

    # Chapter 5: Arithmetic Progressions
    {
        "chapter_folder": "chapter-5-arithmetic-progressions",
        "topic_slug": "ap-basics-nth-term",
        "topic_id": "cbse10-ap-basics-nth-term",
        "chapter_title": "Chapter 5 - Arithmetic Progressions",
        "topic_title": "Arithmetic Progressions & General nth Term",
        "short_title": "nth Term of AP",
        "prev_id": "cbse10-quadratic-equations-quadratic-word-problems",
        "next_id": "cbse10-ap-nth-term-from-end",
        "requires_svg": False,
        "typologies": [
            "Identifying first term a, common difference d, and verifying whether a sequence is an AP",
            "Finding nth term using an = a + (n - 1)d",
            "Finding which term of an AP is a given number (finding n) or first negative term",
            "Determining a and d from two given terms (forming simultaneous linear equations)",
            "3 or 4 consecutive terms in AP (a-d, a, a+d) given their sum and product"
        ]
    },
    {
        "chapter_folder": "chapter-5-arithmetic-progressions",
        "topic_slug": "nth-term-from-end",
        "topic_id": "cbse10-ap-nth-term-from-end",
        "chapter_title": "Chapter 5 - Arithmetic Progressions",
        "topic_title": "Finding the nth Term from the End of an AP",
        "short_title": "nth Term from End",
        "prev_id": "cbse10-ap-basics-nth-term",
        "next_id": "cbse10-ap-sum-of-n-terms",
        "requires_svg": False,
        "typologies": [
            "Direct calculation using l - (n - 1)d",
            "Reverse AP sequence method",
            "Finding middle term(s) of a finite AP",
            "Term positioned equidistant from beginning and end"
        ]
    },
    {
        "chapter_folder": "chapter-5-arithmetic-progressions",
        "topic_slug": "sum-of-n-terms",
        "topic_id": "cbse10-ap-sum-of-n-terms",
        "chapter_title": "Chapter 5 - Arithmetic Progressions",
        "topic_title": "Sum of First n Terms of an Arithmetic Progression",
        "short_title": "Sum of n Terms",
        "prev_id": "cbse10-ap-nth-term-from-end",
        "next_id": "cbse10-ap-relation-an-sn",
        "requires_svg": False,
        "typologies": [
            "Direct evaluation of Sn using n/2 * [2a + (n - 1)d] and n/2 * [a + l]",
            "Finding number of terms n needed to obtain a given sum",
            "Sum of arithmetic ranges (multiples of k, two-digit integers, odd/even numbers)",
            "Linear simultaneous equations in a and d from two given sums (Sm and Sn)",
            "AP sum problems involving fractions and negative common differences"
        ]
    },
    {
        "chapter_folder": "chapter-5-arithmetic-progressions",
        "topic_slug": "relation-an-sn",
        "topic_id": "cbse10-ap-relation-an-sn",
        "chapter_title": "Chapter 5 - Arithmetic Progressions",
        "topic_title": "Relationship between nth Term (an) and Sum (Sn)",
        "short_title": "an & Sn Relation",
        "prev_id": "cbse10-ap-sum-of-n-terms",
        "next_id": "cbse10-ap-applications",
        "requires_svg": False,
        "typologies": [
            "Finding nth term an from a given quadratic sum formula Sn using an = Sn - Sn-1",
            "Finding first term a, common difference d, and specific term ak from Sn",
            "Ratio of sums of two different APs to find ratio of their m-th terms",
            "Proofs of identities relating Sn, S2n, S3n (e.g. S3n = 3(S2n - Sn))"
        ]
    },
    {
        "chapter_folder": "chapter-5-arithmetic-progressions",
        "topic_slug": "ap-applications",
        "topic_id": "cbse10-ap-applications",
        "chapter_title": "Chapter 5 - Arithmetic Progressions",
        "topic_title": "Real-Life Applications & Word Problems on AP",
        "short_title": "AP Applications",
        "prev_id": "cbse10-ap-relation-an-sn",
        "next_id": "cbse10-triangles-bpt-theorem",
        "requires_svg": False,
        "typologies": [
            "Savings, loan installments, and penalty escalation problems",
            "Physical/structural arrangement problems (ladder rungs, stacked logs, stadium seating rows)",
            "Production targets and annual manufacturing increments",
            "CBSE Case-study style multi-part contextual word problems"
        ]
    },

    # Chapter 6: Triangles
    {
        "chapter_folder": "chapter-6-triangles",
        "topic_slug": "bpt-theorem",
        "topic_id": "cbse10-triangles-bpt-theorem",
        "chapter_title": "Chapter 6 - Triangles",
        "topic_title": "Basic Proportionality Theorem (Thales' Theorem)",
        "short_title": "BPT (Thales Theorem)",
        "prev_id": "cbse10-ap-applications",
        "next_id": "cbse10-triangles-converse-bpt",
        "requires_svg": True,
        "typologies": [
            "Finding unknown segment length in triangle ABC with DE || BC (AD/DB = AE/EC)",
            "Finding x when side segments are given as linear/quadratic algebraic expressions",
            "Applying BPT with full sides (AD/AB = AE/AC)",
            "Applications in trapeziums with line parallel to parallel bases",
            "Multi-step geometric proof deductions using BPT in intersecting triangles"
        ]
    },
    {
        "chapter_folder": "chapter-6-triangles",
        "topic_slug": "converse-bpt",
        "topic_id": "cbse10-triangles-converse-bpt",
        "chapter_title": "Chapter 6 - Triangles",
        "topic_title": "Converse of Basic Proportionality Theorem",
        "short_title": "Converse of BPT",
        "prev_id": "cbse10-triangles-bpt-theorem",
        "next_id": "cbse10-triangles-criteria-similarity",
        "requires_svg": True,
        "typologies": [
            "Testing whether segment DE is parallel to side BC by calculating ratio equality",
            "Finding variable value that forces lines to be parallel",
            "Geometric deductions in quadrilaterals using converse of BPT",
            "Midpoint segment parallelism and intercept proofs"
        ]
    },
    {
        "chapter_folder": "chapter-6-triangles",
        "topic_slug": "criteria-similarity",
        "topic_id": "cbse10-triangles-criteria-similarity",
        "chapter_title": "Chapter 6 - Triangles",
        "topic_title": "Criteria for Similarity of Triangles (AAA, SSS, SAS)",
        "short_title": "Similarity Criteria",
        "prev_id": "cbse10-triangles-converse-bpt",
        "next_id": "cbse10-coordinate-geometry-distance-formula",
        "requires_svg": True,
        "typologies": [
            "AA/AAA similarity criterion to find missing angles and side lengths",
            "SAS similarity criterion with proportional sides and included angle",
            "SSS similarity criterion and identifying corresponding vertices",
            "Right triangles with altitude to hypotenuse similarity relations",
            "Shadow casting, vertical poles, and mirror reflection height problems"
        ]
    },

    # Chapter 7: Coordinate Geometry
    {
        "chapter_folder": "chapter-7-coordinate-geometry",
        "topic_slug": "distance-formula",
        "topic_id": "cbse10-coordinate-geometry-distance-formula",
        "chapter_title": "Chapter 7 - Coordinate Geometry",
        "topic_title": "Distance Formula & Geometric Applications",
        "short_title": "Distance Formula",
        "prev_id": "cbse10-triangles-criteria-similarity",
        "next_id": "cbse10-coordinate-geometry-section-formula-internal",
        "requires_svg": True,
        "typologies": [
            "Direct distance calculation between two points P(x1, y1) and Q(x2, y2)",
            "Testing collinearity of three points using distance addition (AB + BC = AC)",
            "Classifying geometric figures (equilateral/isosceles/right triangle, square, rhombus, rectangle)",
            "Finding equidistant point on x-axis (x, 0) or y-axis (0, y)",
            "Finding unknown coordinate parameter k given distance between two points"
        ]
    },
    {
        "chapter_folder": "chapter-7-coordinate-geometry",
        "topic_slug": "section-formula-internal",
        "topic_id": "cbse10-coordinate-geometry-section-formula-internal",
        "chapter_title": "Chapter 7 - Coordinate Geometry",
        "topic_title": "Section Formula for Internal Division",
        "short_title": "Section Formula",
        "prev_id": "cbse10-coordinate-geometry-distance-formula",
        "next_id": "cbse10-coordinate-geometry-midpoint-trisection",
        "requires_svg": True,
        "typologies": [
            "Finding coordinates of point P(x, y) dividing segment AB internally in ratio m1 : m2",
            "Section formula with negative coordinates and fractional ratios",
            "Finding centroid of a triangle given its three vertices",
            "Finding missing vertex coordinates given division points"
        ]
    },
    {
        "chapter_folder": "chapter-7-coordinate-geometry",
        "topic_slug": "midpoint-trisection",
        "topic_id": "cbse10-coordinate-geometry-midpoint-trisection",
        "chapter_title": "Chapter 7 - Coordinate Geometry",
        "topic_title": "Midpoint Formula & Points of Trisection",
        "short_title": "Midpoint & Trisection",
        "prev_id": "cbse10-coordinate-geometry-section-formula-internal",
        "next_id": "cbse10-coordinate-geometry-finding-ratio",
        "requires_svg": True,
        "typologies": [
            "Midpoint calculation ((x1+x2)/2, (y1+y2)/2) and diameter endpoints of circle",
            "Points of trisection dividing segment AB in 1:2 and 2:1",
            "Finding the fourth vertex of a parallelogram using diagonals bisecting each other",
            "Dividing segment into 4 equal parts using successive midpoints"
        ]
    },
    {
        "chapter_folder": "chapter-7-coordinate-geometry",
        "topic_slug": "finding-ratio",
        "topic_id": "cbse10-coordinate-geometry-finding-ratio",
        "chapter_title": "Chapter 7 - Coordinate Geometry",
        "topic_title": "Finding Division Ratio & Axis Intercepts",
        "short_title": "Finding Ratio",
        "prev_id": "cbse10-coordinate-geometry-midpoint-trisection",
        "next_id": "cbse10-trigonometry-trig-ratios-right-triangle",
        "requires_svg": True,
        "typologies": [
            "Finding ratio k:1 in which point P(x, y) divides segment AB",
            "Finding ratio in which x-axis (y = 0) divides segment and finding coordinates of intersection",
            "Finding ratio in which y-axis (x = 0) divides segment and finding coordinates of intersection",
            "Finding ratio in which a given line ax + by + c = 0 divides segment AB"
        ]
    },

    # Chapter 8: Introduction to Trigonometry
    {
        "chapter_folder": "chapter-8-introduction-to-trigonometry",
        "topic_slug": "trig-ratios-right-triangle",
        "topic_id": "cbse10-trigonometry-trig-ratios-right-triangle",
        "chapter_title": "Chapter 8 - Introduction to Trigonometry",
        "topic_title": "Trigonometric Ratios in a Right Triangle",
        "short_title": "Trig Ratios",
        "prev_id": "cbse10-coordinate-geometry-finding-ratio",
        "next_id": "cbse10-trigonometry-specific-angles-values",
        "requires_svg": True,
        "typologies": [
            "Finding all 6 trig ratios from one given ratio using Pythagoras theorem",
            "Evaluating composite trig expressions in terms of sin, cos, tan",
            "Multi-angle right triangle expressions (sin A cos C + cos A sin C)",
            "Given a cot theta = b, evaluating algebraic expressions in sin theta and cos theta",
            "Finding side lengths of right triangle given one angle ratio and one side"
        ]
    },
    {
        "chapter_folder": "chapter-8-introduction-to-trigonometry",
        "topic_slug": "specific-angles-values",
        "topic_id": "cbse10-trigonometry-specific-angles-values",
        "chapter_title": "Chapter 8 - Introduction to Trigonometry",
        "topic_title": "Trigonometric Ratios of Specific Angles (0°, 30°, 45°, 60°, 90°)",
        "short_title": "Standard Angle Values",
        "prev_id": "cbse10-trigonometry-trig-ratios-right-triangle",
        "next_id": "cbse10-trigonometry-trigonometric-identities",
        "requires_svg": False,
        "typologies": [
            "Direct numerical evaluation of expressions with 0°, 30°, 45°, 60°, 90°",
            "Verifying trigonometric identities at specific standard angles",
            "Solving simultaneous linear systems for acute angles A and B (e.g. tan(A+B)=sqrt(3), tan(A-B)=1/sqrt(3))",
            "Finding unknown geometric sides/angles in right triangles using standard values"
        ]
    },
    {
        "chapter_folder": "chapter-8-introduction-to-trigonometry",
        "topic_slug": "trigonometric-identities",
        "topic_id": "cbse10-trigonometry-trigonometric-identities",
        "chapter_title": "Chapter 8 - Introduction to Trigonometry",
        "topic_title": "Fundamental Trigonometric Identities",
        "short_title": "Trig Identities",
        "prev_id": "cbse10-trigonometry-specific-angles-values",
        "next_id": "cbse10-heights-distances-single-angle",
        "requires_svg": False,
        "typologies": [
            "Proving identities using sin^2 theta + cos^2 theta = 1 and reciprocal forms",
            "Proving identities involving 1 + tan^2 theta = sec^2 theta and 1 + cot^2 theta = cosec^2 theta",
            "Rationalising binomial trig denominators (e.g. sqrt((1+sin theta)/(1-sin theta)) = sec theta + tan theta)",
            "Complex fractional trig proofs with factoring (sec theta - tan theta)",
            "Eliminating parameter theta from parametric equations (e.g. x = a sec theta, y = b tan theta)"
        ]
    },

    # Chapter 9: Some Applications of Trigonometry
    {
        "chapter_folder": "chapter-9-applications-of-trigonometry",
        "topic_slug": "single-angle-heights-distances",
        "topic_id": "cbse10-heights-distances-single-angle",
        "chapter_title": "Chapter 9 - Some Applications of Trigonometry",
        "topic_title": "Heights and Distances with Single Angle of Elevation/Depression",
        "short_title": "Single-Angle Problems",
        "prev_id": "cbse10-trigonometry-trigonometric-identities",
        "next_id": "cbse10-heights-distances-two-angles",
        "requires_svg": True,
        "typologies": [
            "Finding height of object given shadow length and angle of elevation",
            "Finding distance of observer from base given height and angle of depression",
            "Broken tree / leaning pole touching ground problems",
            "Kite flying string length with angle of inclination"
        ]
    },
    {
        "chapter_folder": "chapter-9-applications-of-trigonometry",
        "topic_slug": "two-angles-heights-distances",
        "topic_id": "cbse10-heights-distances-two-angles",
        "chapter_title": "Chapter 9 - Some Applications of Trigonometry",
        "topic_title": "Heights and Distances with Two Angles (Moving Observer / Dual Observation)",
        "short_title": "Two-Angle Problems",
        "prev_id": "cbse10-heights-distances-single-angle",
        "next_id": "cbse10-circles-tangent-radius-theorem",
        "requires_svg": True,
        "typologies": [
            "Two observation points on same side of tower with changing elevation (30° -> 60°)",
            "Two observation points on opposite sides of a tower / river",
            "Observation of top and bottom of a statue/flagstaff standing on a pedestal",
            "Observation from top of a building looking at top and bottom of another tower",
            "Cloud and its reflection in a lake problems (angle of elevation vs angle of depression)"
        ]
    },

    # Chapter 10: Circles
    {
        "chapter_folder": "chapter-10-circles",
        "topic_slug": "tangent-radius-theorem",
        "topic_id": "cbse10-circles-tangent-radius-theorem",
        "chapter_title": "Chapter 10 - Circles",
        "topic_title": "Tangent-Radius Perpendicularity Theorem",
        "short_title": "Tangent & Radius",
        "prev_id": "cbse10-heights-distances-two-angles",
        "next_id": "cbse10-circles-lengths-tangents-external-point",
        "requires_svg": True,
        "typologies": [
            "Finding tangent length or radius in right triangle OPT using Pythagoras theorem",
            "Finding angles between radius and tangent (OP perp PT)",
            "Concentric circles and length of chord touching inner circle",
            "Angle subtended between two tangents from an external point and chord of contact"
        ]
    },
    {
        "chapter_folder": "chapter-10-circles",
        "topic_slug": "lengths-tangents-external-point",
        "topic_id": "cbse10-circles-lengths-tangents-external-point",
        "chapter_title": "Chapter 10 - Circles",
        "topic_title": "Lengths of Tangents from an External Point",
        "short_title": "External Tangents",
        "prev_id": "cbse10-circles-tangent-radius-theorem",
        "next_id": "cbse10-circles-circle-tangent-proofs",
        "requires_svg": True,
        "typologies": [
            "Direct calculations using equal tangent lengths PA = PB",
            "Circumscribed triangles and computing perimeter / unknown segments",
            "Circumscribed quadrilaterals proving AB + CD = AD + BC and calculating missing sides",
            "Finding radius of incircle in right-angled and general triangles",
            "Tangent segments with angles subtended at the centre"
        ]
    },
    {
        "chapter_folder": "chapter-10-circles",
        "topic_slug": "circle-tangent-proofs",
        "topic_id": "cbse10-circles-circle-tangent-proofs",
        "chapter_title": "Chapter 10 - Circles",
        "topic_title": "Geometric Proofs and Theorems on Circle Tangents",
        "short_title": "Tangent Proofs",
        "prev_id": "cbse10-circles-lengths-tangents-external-point",
        "next_id": "cbse10-areas-circles-sector-area-arc-length",
        "requires_svg": True,
        "typologies": [
            "Proving tangents at endpoints of a diameter are parallel",
            "Proving a parallelogram circumscribing a circle is a rhombus",
            "Proving opposite sides of circumscribed quadrilateral subtend supplementary angles at centre",
            "Proving angle between two tangents is supplementary to angle subtended by contact points at centre"
        ]
    },

    # Chapter 11: Areas Related to Circles
    {
        "chapter_folder": "chapter-11-areas-related-to-circles",
        "topic_slug": "sector-area-arc-length",
        "topic_id": "cbse10-areas-circles-sector-area-arc-length",
        "chapter_title": "Chapter 11 - Areas Related to Circles",
        "topic_title": "Area of Sector and Arc Length of a Circle",
        "short_title": "Sector & Arc Length",
        "prev_id": "cbse10-circles-circle-tangent-proofs",
        "next_id": "cbse10-areas-circles-segment-area",
        "requires_svg": True,
        "typologies": [
            "Direct calculation of sector area (theta/360 * pi*r^2) and arc length (theta/360 * 2*pi*r)",
            "Finding central angle theta or radius r given sector area or arc length",
            "Perimeter of a sector P = 2r + l and optimization calculations",
            "Clock hands sweep area (minute hand angle in t minutes)",
            "Wiper blades, circular grazing field ropes, and pendulum sweep areas"
        ]
    },
    {
        "chapter_folder": "chapter-11-areas-related-to-circles",
        "topic_slug": "segment-area",
        "topic_id": "cbse10-areas-circles-segment-area",
        "chapter_title": "Chapter 11 - Areas Related to Circles",
        "topic_title": "Area of Minor and Major Segments of a Circle",
        "short_title": "Segment Area",
        "prev_id": "cbse10-areas-circles-sector-area-arc-length",
        "next_id": "cbse10-surface-areas-volumes-combination-solids-surface-area",
        "requires_svg": True,
        "typologies": [
            "Area of minor segment for central angle theta = 60° (equilateral triangle subtraction)",
            "Area of minor segment for central angle theta = 90° (right triangle subtraction)",
            "Area of minor segment for central angle theta = 120° (isosceles triangle subtraction)",
            "Area of major segment and shaded circular border designs"
        ]
    },

    # Chapter 12: Surface Areas and Volumes
    {
        "chapter_folder": "chapter-12-surface-areas-volumes",
        "topic_slug": "combination-solids-surface-area",
        "topic_id": "cbse10-surface-areas-volumes-combination-solids-surface-area",
        "chapter_title": "Chapter 12 - Surface Areas and Volumes",
        "topic_title": "Surface Area of Combinations of Solids",
        "short_title": "Combination Surface Area",
        "prev_id": "cbse10-areas-circles-segment-area",
        "next_id": "cbse10-surface-areas-volumes-combination-solids-volume",
        "requires_svg": True,
        "typologies": [
            "Toy combining cone mounted on a hemisphere",
            "Cylinder surmounted by conical roof or hemispherical dome",
            "Medicine capsule (cylinder with two hemispherical ends)",
            "Solid cube / cylinder with hemispherical depression carved out",
            "Conversion of shapes / canvas tent area calculation"
        ]
    },
    {
        "chapter_folder": "chapter-12-surface-areas-volumes",
        "topic_slug": "combination-solids-volume",
        "topic_id": "cbse10-surface-areas-volumes-combination-solids-volume",
        "chapter_title": "Chapter 12 - Surface Areas and Volumes",
        "topic_title": "Volume of Combinations of Solids",
        "short_title": "Combination Volume",
        "prev_id": "cbse10-surface-areas-volumes-combination-solids-surface-area",
        "next_id": "cbse10-statistics-mean-direct-assumed",
        "requires_svg": True,
        "typologies": [
            "Volume of solid composed of cylinder with conical or hemispherical ends",
            "Gulab jamun syrup absorption (percentage volume of combination solids)",
            "Water displacement and overflow when solid shapes are submerged",
            "Emptying water from conical vessel into cylindrical vessel",
            "Embankment formed from earth dug out of cylindrical well"
        ]
    },

    # Chapter 13: Statistics
    {
        "chapter_folder": "chapter-13-statistics",
        "topic_slug": "mean-direct-assumed",
        "topic_id": "cbse10-statistics-mean-direct-assumed",
        "chapter_title": "Chapter 13 - Statistics",
        "topic_title": "Mean of Grouped Data (Direct & Assumed Mean Methods)",
        "short_title": "Mean of Grouped Data",
        "prev_id": "cbse10-surface-areas-volumes-combination-solids-volume",
        "next_id": "cbse10-statistics-mode-grouped-data",
        "requires_svg": False,
        "typologies": [
            "Direct Method calculation mean = Sum(fi * xi) / Sum(fi)",
            "Assumed Mean Method mean = a + Sum(fi * di) / Sum(fi)",
            "Finding single missing frequency f given the mean",
            "Finding two missing frequencies f1, f2 given total frequency and mean"
        ]
    },
    {
        "chapter_folder": "chapter-13-statistics",
        "topic_slug": "mode-grouped-data",
        "topic_id": "cbse10-statistics-mode-grouped-data",
        "chapter_title": "Chapter 13 - Statistics",
        "topic_title": "Mode of Grouped Data",
        "short_title": "Mode of Grouped Data",
        "prev_id": "cbse10-statistics-mean-direct-assumed",
        "next_id": "cbse10-statistics-median-grouped-data",
        "requires_svg": False,
        "typologies": [
            "Identifying modal class and computing mode using l + [(f1 - f0) / (2f1 - f0 - f2)] * h",
            "Finding missing frequency given the mode",
            "Comparing mean and mode in contextual real-world datasets",
            "Continuous vs discontinuous class interval mode calculations"
        ]
    },
    {
        "chapter_folder": "chapter-13-statistics",
        "topic_slug": "median-grouped-data",
        "topic_id": "cbse10-statistics-median-grouped-data",
        "chapter_title": "Chapter 13 - Statistics",
        "topic_title": "Median of Grouped Data",
        "short_title": "Median of Grouped Data",
        "prev_id": "cbse10-statistics-mode-grouped-data",
        "next_id": "cbse10-statistics-empirical-relationship",
        "requires_svg": False,
        "typologies": [
            "Constructing cumulative frequency (cf) table and computing median using l + [(n/2 - cf)/f] * h",
            "Finding two missing frequencies x and y given total frequency N and median",
            "Converting 'Less than' / 'More than' cumulative distributions to continuous tables",
            "Interpreting median in income, age, and test score distributions"
        ]
    },
    {
        "chapter_folder": "chapter-13-statistics",
        "topic_slug": "empirical-relationship",
        "topic_id": "cbse10-statistics-empirical-relationship",
        "chapter_title": "Chapter 13 - Statistics",
        "topic_title": "Empirical Relationship between Mean, Median, and Mode",
        "short_title": "Empirical Relation",
        "prev_id": "cbse10-statistics-median-grouped-data",
        "next_id": "cbse10-probability-classical-probability",
        "requires_svg": False,
        "typologies": [
            "Calculating unknown measure using 3 Median = Mode + 2 Mean",
            "Algebraic differences and linear relations between mean, median, and mode",
            "CBSE 1-mark and 2-mark board exam conceptual applications"
        ]
    },

    # Chapter 14: Probability
    {
        "chapter_folder": "chapter-14-probability",
        "topic_slug": "classical-probability",
        "topic_id": "cbse10-probability-classical-probability",
        "chapter_title": "Chapter 14 - Probability",
        "topic_title": "Classical Definition of Probability & Basic Events",
        "short_title": "Classical Probability",
        "prev_id": "cbse10-statistics-empirical-relationship",
        "next_id": "cbse10-probability-coins-dice-cards",
        "requires_svg": False,
        "typologies": [
            "Fundamental probability P(E) = favourable outcomes / total outcomes",
            "Complementary events P(not E) = 1 - P(E) and impossible/sure events",
            "Coloured balls, defective items, and numbered disc selections",
            "Odds in favour and simple compound single-draw events"
        ]
    },
    {
        "chapter_folder": "chapter-14-probability",
        "topic_slug": "coins-dice-cards",
        "topic_id": "cbse10-probability-coins-dice-cards",
        "chapter_title": "Chapter 14 - Probability",
        "topic_title": "Probability Models: Coins, Dice & Playing Cards",
        "short_title": "Coins, Dice & Cards",
        "prev_id": "cbse10-probability-classical-probability",
        "next_id": "cbse10-probability-real-life-probability",
        "requires_svg": False,
        "typologies": [
            "Tossing 2 or 3 coins (at least, at most, exactly k heads/tails)",
            "Rolling 2 dice (sample space of 36, sum of numbers, doublet, product)",
            "Standard deck of 52 cards (face cards, red/black honours, specific suits)",
            "Card draws after removing specific cards (e.g. all kings and queens removed)",
            "Prime numbers, perfect squares, and composite number dice rolls"
        ]
    },
    {
        "chapter_folder": "chapter-14-probability",
        "topic_slug": "real-life-probability",
        "topic_id": "cbse10-probability-real-life-probability",
        "chapter_title": "Chapter 14 - Probability",
        "topic_title": "Geometric & Real-Life Probability Applications",
        "short_title": "Real-Life Probability",
        "prev_id": "cbse10-probability-coins-dice-cards",
        "next_id": None,
        "requires_svg": True,
        "typologies": [
            "Geometric area probability (target board, rectangular region with circle)",
            "Calendar, leap year and non-leap year 53 Sundays/Mondays probability",
            "Game of chance with spinning arrow / pointer",
            "Board game scenarios, defective pen packages, and lottery draws"
        ]
    }
]


# ==============================================================================
# 2. PROMPT TEMPLATE WITH STRICT UNIVERSAL SCHEMA v1.0.0 RULES
# ==============================================================================
SYSTEM_PROMPT = """You are an expert CBSE Class 10 Mathematics Curriculum Designer and Senior Pedagogy Specialist.
Your task is to generate a comprehensive, highly rigorous, production-ready topic JSON file conforming 100% strictly to Universal Schema v1.0.0.

CRITICAL PEDAGOGICAL & ARCHITECTURAL REQUIREMENTS:

1. DYNAMIC & COMPREHENSIVE QUESTION TYPOLOGIES (NO FIXED 3-TYPE LIMIT):
   - Every topic has its own unique pedagogical depth. Some topics have 3 types, others have 4, 5, 6, or more types.
   - You MUST generate ALL the Question Typologies specified in the prompt for this topic.
   - For EVERY typology:
     * Provide 1 complete step-by-step worked model in `worked_examples` (type_id matching).
     * Provide a dedicated question type block in `question_types` with a high-capacity pool of 12-15 questions partitioned across Easy, Medium, and Hard difficulty.

2. STEP GRANULARITY & DUAL CALCULATIONS:
   - ZERO STEP JUMPING: Every problem must be broken into single-action atomic pedagogical steps. Never combine multiple algebraic moves into one step.
   - DUAL CALCULATIONS PER STEP IN GUIDED CALC:
     Whenever mathematical values are calculated in `calc_template`, the step must prompt for TWO related quantities at a time (e.g. numerator & denominator, x-coordinate & y-coordinate, coefficient a & b, split pair p & q, intermediate simplification & final root, ratio 1 & ratio 2, etc.).
     Format `calc_template.format_latex` with clean multiline stacked LaTeX:
     "format_latex": "\\\\begin{aligned} \\\\text{First Value} &= \\\\boxed{?} \\\\\\\\ \\\\text{Second Value} &= \\\\boxed{?} \\\\end{aligned}"
     and provide exactly 2 objects in `calc_template.fields` with neutral placeholders ("placeholder": "Enter value").

3. CLOSE DISTRACTORS & BALANCED STRATEGY CHOICES:
   - In Stage 1 (Strategy Choices), provide exactly 4 options.
   - BALANCED LENGTH & PARALLEL STRUCTURE: All 4 options must have virtually equal word counts and identical sentence grammar.
   - CLOSE REALISTIC DISTRACTORS: Distractors must reflect common student errors (sign inversion, forgetting to square, inverted reciprocal, swapping coordinates, applying wrong formula).
   - DIAGNOSTIC FEEDBACK: In `option_details`, provide a specific pedagogical reason for every option (why it is correct or the exact mistake made).

4. DIAGRAMS & RESPONSIVE SVGs:
   - For geometry, trigonometry, coordinate geometry, circles, areas, or graphical topics, provide a semantic, responsive inline SVG in `diagram_svg` and question visuals.
   - SVG properties: viewBox='0 0 500 240', width='100%', height='100%', stroke-width, clear labels (<text>), coordinate axes, and high-contrast styling.

5. STRICT LATEX EQUATION FORMATTING:
   - Single equals sign per line in all LaTeX `\\\\begin{aligned} ... \\\\end{aligned}` equations.

6. ZERO LEAK RULE:
   - Never write answers or parenthetical hints in `calc_prompt`, `strategy_question`, or field `label`.
   - Placeholders in `calc_template.fields` MUST ALWAYS be strictly `"Enter value"`.

7. OUTPUT FORMAT:
   - Return ONLY pure, valid JSON (UTF-8). Do NOT include markdown commentary outside the JSON.
"""


def build_user_prompt(meta: Dict[str, Any]) -> str:
    """Builds the targeted generation prompt for a specific curriculum topic."""
    typology_list_str = "\n".join([f"   - Typology {i+1}: {t}" for i, t in enumerate(meta["typologies"])])
    
    prev_topic_obj = {
        "id": meta["prev_id"],
        "title": meta["prev_id"],
        "url": f"/learning/ui/concept-mastery/?topic={meta['prev_id']}"
    } if meta["prev_id"] else None
    
    next_topic_obj = {
        "id": meta["next_id"],
        "title": meta["next_id"],
        "url": f"/learning/ui/concept-mastery/?topic={meta['next_id']}"
    } if meta["next_id"] else None

    prev_topic_str = json.dumps(prev_topic_obj, indent=2)
    next_topic_str = json.dumps(next_topic_obj, indent=2)

    prompt = f"""Generate the complete Universal Schema v1.0.0 JSON dataset for the following CBSE Class 10 topic:

TOPIC METADATA:
- Chapter: {meta['chapter_title']}
- Topic Title: {meta['topic_title']}
- Topic ID: {meta['topic_id']}
- Short Title: {meta['short_title']}
- Class: 10
- Board: CBSE
- Subject: Mathematics
- Previous Topic ID: {meta['prev_id'] or 'null'}
- Next Topic ID: {meta['next_id'] or 'null'}
- Requires SVG Diagram in Concepts: {'Yes' if meta['requires_svg'] else 'No'}

MANDATORY QUESTION TYPOLOGIES TO INCLUDE:
{typology_list_str}

REQUIRED JSON STRUCTURE & SECTIONS:
{{
  "schema_version": "1.0.0",
  "content_type": "learning_topic",
  "unlock_all_types": false,
  "topic": {{
    "id": "{meta['topic_id']}",
    "class": 10,
    "board": "CBSE",
    "subject": "Mathematics",
    "chapter": "{meta['chapter_title']}",
    "title": "{meta['topic_title']}",
    "short_title": "{meta['short_title']}",
    "status": "active",
    "learning_format": "concept_mastery",
    "student_journey": "Concepts → Worked Solutions → Strategy Choices → Guided Calculation → Notebook Solve"
  }},
  "previous_topic": {prev_topic_str},
  "next_topic": {next_topic_str},
  "prerequisites": {{
    "required_skills": ["foundational_algebra", "arithmetic_computation"],
    "dependency_policy": {{
      "diagnose_before_backtracking": true,
      "preserve_current_topic_state": true,
      "return_to_same_stage_after_dependency_practice": true
    }}
  }},
  "stages": {{
    "progression": [
      {{ "id": "concepts", "title": "1. Concepts", "description": "Understand core definitions, formulas, and theorems" }},
      {{ "id": "worked_examples", "title": "2. Solutions", "description": "Study step-by-step worked model solutions for every question type" }},
      {{ "id": "stage_1_strategy", "title": "3. Strategy", "description": "Master strategic sequencing and decision moves" }},
      {{ "id": "stage_2_calc", "title": "4. Guided Calc", "description": "Fill in the blank numbers in structured mathematical templates" }},
      {{ "id": "stage_3_notebook", "title": "5. Notebook", "description": "Solve in notebook and self-audit against board marking schemes" }}
    ]
  }},
  "reference_drawer": {{
    "title": "📖 {meta['topic_title']} Reference Guide",
    "description": "Essential theorems, formulas, and rules:",
    "items": [
      {{
        "tag": "<Rule Tag>",
        "rule": "<Explanation>",
        "formula": "<LaTeX formula>",
        "example": "<Concrete numeric example>"
      }}
    ]
  }},
  "concepts": [
    {{
      "id": "concept_01",
      "title": "1. <Concept Name>",
      "subtitle": "<Concise Subtitle>",
      "summary": "<Core principle in 1 clear sentence>",
      "points": [
        {{ "icon": "✓", "text": "<strong><Keyword>:</strong> <Clear explanation>" }},
        {{ "icon": "★", "text": "<strong><Takeaway>:</strong> <Clear takeaway>" }}
      ],
      "formula": "<Pure math identity>",
      "diagram_svg": "<Clean SVG string if visual/geometry topic, else empty string>",
      "trap": "<Common misconception to avoid>"
    }}
  ],
  "worked_examples": [
    {{
      "id": "we_t1_model",
      "type_id": "type_1_standard",
      "type_label": "Type 1",
      "title": "Type 1: {meta['typologies'][0]}",
      "problem": "<Complete model problem statement>",
      "steps": [
        {{
          "step_number": 1,
          "statement": "<Description of atomic single action>",
          "calculation": "\\\\begin{{aligned}} <Left> &= <Right> \\\\end{{aligned}}",
          "reason": "<Mathematical justification with single equals per line>"
        }}
      ],
      "conclusion": "<Summary conclusion>",
      "final_answer": "<Final answer>"
    }}
  ],
  "question_types": [
    {{
      "type_id": "type_1_standard",
      "type_title": "Type 1: {meta['typologies'][0]}",
      "description": "<Description of problem archetype>",
      "pool": [
        {{
          "id": "t1_p01",
          "statement": "<Clear mathematical problem statement>",
          "difficulty": "easy",
          "steps": [
            {{
              "step_number": 1,
              "focus": "<Step Focus>",
              "strategy_question": "<Clear strategy question prompting next move>",
              "strategy_options": [
                "<Balanced distractor 1>",
                "<Correct option>",
                "<Balanced distractor 2>",
                "<Balanced distractor 3>"
              ],
              "correct_strategy_index": 1,
              "option_details": [
                {{ "text": "<Option 1>", "is_correct": false, "explanation": "<Diagnostic reason for distractor>" }},
                {{ "text": "<Option 2>", "is_correct": true, "explanation": "Correct! <Pedagogical rationale>" }},
                {{ "text": "<Option 3>", "is_correct": false, "explanation": "<Diagnostic reason for distractor>" }},
                {{ "text": "<Option 4>", "is_correct": false, "explanation": "<Diagnostic reason for distractor>" }}
              ],
              "calc_prompt": "<Neutral directive e.g. Calculate the intermediate values:>",
              "calc_template": {{
                "format_latex": "\\\\begin{{aligned}} \\\\text{{First Value}} &= \\\\boxed{{?}} \\\\\\\\ \\\\text{{Second Value}} &= \\\\boxed{{?}} \\\\end{{aligned}}",
                "fields": [
                  {{
                    "key": "f1",
                    "label": "First Value",
                    "placeholder": "Enter value",
                    "expected": "<Numeric or algebraic value>"
                  }},
                  {{
                    "key": "f2",
                    "label": "Second Value",
                    "placeholder": "Enter value",
                    "expected": "<Numeric or algebraic value>"
                  }}
                ]
              }},
              "expected_value": "<Value 1, Value 2>",
              "rubric_text": "<Clear self-audit criteria for notebook stage>",
              "rubric_math": "\\\\begin{{aligned}} <Line 1> \\\\\\\\ <Line 2> \\\\end{{aligned}}",
              "hint": "<Actionable diagnostic hint>",
              "revisit_topic": {{
                "title": "{meta['short_title']} Concepts",
                "url": "/learning/ui/concept-mastery/?topic={meta['topic_id']}#concept_01",
                "tip": "<Concise memory anchor rule>"
              }}
            }}
          ],
          "final_canonical_answer": "<Final authoritative answer>"
        }}
      ]
    }}
  ]
}}

Generate ALL {len(meta['typologies'])} question typologies listed above with a dedicated worked example and a high capacity pool of 12-15 questions for EACH typology. Output ONLY valid JSON."""
    return prompt


# ==============================================================================
# 3. GEMINI API CLIENT & RETRY ENGINE
# ==============================================================================
class TopicGenerator:
    def __init__(self, api_key: str, model_name: str = "gemini-2.5-flash", delay: float = 15.0):
        self.api_key = api_key
        self.model_name = model_name
        self.delay = delay
        
        if HAS_GENAI:
            genai.configure(api_key=self.api_key)
            self._init_model(self.model_name)
        else:
            self.model = None

    def _init_model(self, model_name: str):
        self.model_name = model_name
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=SYSTEM_PROMPT,
            generation_config={
                "response_mime_type": "application/json",
                "temperature": 0.2,
                "max_output_tokens": 65536,
            }
        )

    def clean_json_response(self, text: str) -> str:
        """Strips markdown backticks and cleans response string."""
        text = text.strip()
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?\s*", "", text)
            text = re.sub(r"\s*```$", "", text)
        return text.strip()

    def generate_skeleton(self, meta: Dict[str, Any], max_retries: int = 3) -> Optional[Dict[str, Any]]:
        """Generates topic metadata, reference drawer, concepts with SVG, and worked examples."""
        typology_list_str = "\n".join([f"   - Typology {i+1}: {t}" for i, t in enumerate(meta["typologies"])])
        
        prev_topic_obj = {
            "id": meta["prev_id"],
            "title": meta["prev_id"],
            "url": f"/learning/ui/concept-mastery/?topic={meta['prev_id']}"
        } if meta["prev_id"] else None
        
        next_topic_obj = {
            "id": meta["next_id"],
            "title": meta["next_id"],
            "url": f"/learning/ui/concept-mastery/?topic={meta['next_id']}"
        } if meta["next_id"] else None

        prompt = f"""Generate the core Topic Skeleton JSON for CBSE Class 10:

TOPIC METADATA:
- Chapter: {meta['chapter_title']}
- Topic Title: {meta['topic_title']}
- Topic ID: {meta['topic_id']}
- Short Title: {meta['short_title']}
- Previous Topic ID: {meta['prev_id'] or 'null'}
- Next Topic ID: {meta['next_id'] or 'null'}
- Requires SVG Diagram: {'Yes' if meta['requires_svg'] else 'No'}

TYPOLOGIES:
{typology_list_str}

SCHEMA TO GENERATE (JSON ONLY):
{{
  "schema_version": "1.0.0",
  "content_type": "learning_topic",
  "unlock_all_types": false,
  "topic": {{
    "id": "{meta['topic_id']}",
    "class": 10,
    "board": "CBSE",
    "subject": "Mathematics",
    "chapter": "{meta['chapter_title']}",
    "title": "{meta['topic_title']}",
    "short_title": "{meta['short_title']}",
    "status": "active",
    "learning_format": "concept_mastery",
    "student_journey": "Concepts → Worked Solutions → Strategy Choices → Guided Calculation → Notebook Solve"
  }},
  "previous_topic": {json.dumps(prev_topic_obj, indent=2)},
  "next_topic": {json.dumps(next_topic_obj, indent=2)},
  "stages": {{
    "progression": [
      {{ "id": "concepts", "title": "1. Concepts", "description": "Understand core definitions, formulas, and theorems" }},
      {{ "id": "worked_examples", "title": "2. Solutions", "description": "Study step-by-step worked model solutions for every question type" }},
      {{ "id": "stage_1_strategy", "title": "3. Strategy", "description": "Master strategic sequencing and decision moves" }},
      {{ "id": "stage_2_calc", "title": "4. Guided Calc", "description": "Fill in the blank numbers in structured mathematical templates" }},
      {{ "id": "stage_3_notebook", "title": "5. Notebook", "description": "Solve in notebook and self-audit against board marking schemes" }}
    ]
  }},
  "reference_drawer": {{
    "title": "📖 {meta['topic_title']} Reference Guide",
    "description": "Essential theorems, formulas, and rules:",
    "items": [
      {{
        "tag": "<Rule Tag>",
        "rule": "<Explanation>",
        "formula": "<LaTeX formula>",
        "example": "<Concrete numeric example>"
      }}
    ]
  }},
  "concepts": [
    {{
      "id": "concept_01",
      "title": "1. <Concept Name>",
      "subtitle": "<Subtitle>",
      "summary": "<Core principle in 1 clear sentence>",
      "points": [
        {{ "icon": "✓", "text": "<strong><Keyword>:</strong> <Clear explanation>" }},
        {{ "icon": "★", "text": "<strong><Takeaway>:</strong> <Clear takeaway>" }}
      ],
      "formula": "<Pure math identity>",
      "diagram_svg": "<Inline responsive SVG if geometry/visual, else empty string>",
      "trap": "<Common misconception to avoid>"
    }}
  ],
  "worked_examples": [
    {{
      "id": "we_t1_model",
      "type_id": "type_1",
      "type_label": "Type 1",
      "title": "Type 1: {meta['typologies'][0]}",
      "problem": "<Complete model problem statement>",
      "steps": [
        {{
          "step_number": 1,
          "statement": "<Action>",
          "calculation": "\\\\begin{{aligned}} <Left> &= <Right> \\\\end{{aligned}}",
          "reason": "<Justification with at most 1 equals sign per line>"
        }}
      ],
      "conclusion": "<Summary>",
      "final_answer": "<Final Answer>"
    }}
  ],
  "question_types": []
}}

Provide 1 worked example model for each of the {len(meta['typologies'])} typologies. Output ONLY valid JSON."""

        for attempt in range(1, max_retries + 1):
            try:
                print(f"  [API Call] Generating skeleton & concepts for '{meta['topic_title']}' (Attempt {attempt}/{max_retries}, Model: {self.model_name})...")
                response = self.model.generate_content(prompt)
                if response and response.text:
                    data = json.loads(self.clean_json_response(response.text))
                    if "topic" in data and "concepts" in data:
                        return data
                time.sleep(self.delay)
            except Exception as e:
                err_str = str(e)
                print(f"  [API Error] Skeleton: {err_str[:150]}")
                if "429" in err_str and self.model_name != "gemini-2.5-flash":
                    print("  [Fallback] Switching to 'gemini-2.5-flash' due to quota limits...")
                    self._init_model("gemini-2.5-flash")
                time.sleep(self.delay)
        return None

    def generate_typology_pool(self, meta: Dict[str, Any], typ_index: int, typ_title: str, max_retries: int = 3) -> Optional[Dict[str, Any]]:
        """Generates a high-capacity pool of 12-15 questions for a specific typology."""
        type_id = f"type_{typ_index + 1}_{re.sub(r'[^a-zA-Z0-9]+', '_', typ_title).strip('_').lower()}"
        
        prompt = f"""Generate the Question Typology Pool JSON for CBSE Class 10 Mathematics:
Topic: {meta['topic_title']}
Chapter: {meta['chapter_title']}
Typology {typ_index + 1}: {typ_title}

REQUIREMENTS:
1. Pool capacity: Generate 12 unique questions (4 Easy, 4 Medium, 4 Hard).
2. Granular steps: 3-4 atomic steps per question.
3. Dual calculations: Each guided calc step must calculate TWO quantities at a time in calc_template.format_latex (stacked multiline aligned LaTeX) with 2 fields in fields array. Neutral placeholder "Enter value".
4. Close distractors: 4 balanced options of equal length in Stage 1 with specific diagnostic explanations for each option.
5. Rubric math: Multiline LaTeX with single equals sign per line.

JSON FORMAT TO RETURN (ONLY THIS BLOCK):
{{
  "type_id": "{type_id}",
  "type_title": "Type {typ_index + 1}: {typ_title}",
  "description": "Mastery problem pool for {typ_title}",
  "pool": [
    {{
      "id": "t{typ_index + 1}_p01",
      "statement": "<Clear mathematical problem statement>",
      "difficulty": "easy",
      "steps": [
        {{
          "step_number": 1,
          "focus": "<Step Focus>",
          "strategy_question": "<Strategy prompt>",
          "strategy_options": [
            "<Distractor 1>",
            "<Correct Option>",
            "<Distractor 2>",
            "<Distractor 3>"
          ],
          "correct_strategy_index": 1,
          "option_details": [
            {{ "text": "<Option 1>", "is_correct": false, "explanation": "<Diagnostic explanation>" }},
            {{ "text": "<Option 2>", "is_correct": true, "explanation": "Correct! <Rationale>" }},
            {{ "text": "<Option 3>", "is_correct": false, "explanation": "<Diagnostic explanation>" }},
            {{ "text": "<Option 4>", "is_correct": false, "explanation": "<Diagnostic explanation>" }}
          ],
          "calc_prompt": "<Neutral prompt>",
          "calc_template": {{
            "format_latex": "\\\\begin{{aligned}} \\\\text{{First Value}} &= \\\\boxed{{?}} \\\\\\\\ \\\\text{{Second Value}} &= \\\\boxed{{?}} \\\\end{{aligned}}",
            "fields": [
              {{ "key": "f1", "label": "First Value", "placeholder": "Enter value", "expected": "<Val 1>" }},
              {{ "key": "f2", "label": "Second Value", "placeholder": "Enter value", "expected": "<Val 2>" }}
            ]
          }},
          "expected_value": "<Val 1, Val 2>",
          "rubric_text": "<Self-audit text>",
          "rubric_math": "\\\\begin{{aligned}} <Line 1> \\\\\\\\ <Line 2> \\\\end{{aligned}}",
          "hint": "<Actionable hint>",
          "revisit_topic": {{
            "title": "{meta['short_title']} Concepts",
            "url": "/learning/ui/concept-mastery/?topic={meta['topic_id']}#concept_01",
            "tip": "<Rule>"
          }}
        }}
      ],
      "final_canonical_answer": "<Answer>"
    }}
  ]
}}

Output ONLY valid JSON."""

        for attempt in range(1, max_retries + 1):
            try:
                print(f"  [API Call] Generating Typology {typ_index + 1}/{len(meta['typologies'])}: '{typ_title}'...")
                response = self.model.generate_content(prompt)
                if response and response.text:
                    data = json.loads(self.clean_json_response(response.text))
                    if "type_id" in data and "pool" in data and len(data["pool"]) > 0:
                        return data
                time.sleep(self.delay)
            except Exception as e:
                err_str = str(e)
                print(f"  [API Error] Typology {typ_index + 1}: {err_str[:150]}")
                time.sleep(self.delay)
        return None

    def generate_topic(self, meta: Dict[str, Any], max_retries: int = 5) -> Optional[Dict[str, Any]]:
        """Generates a complete topic using modular, resilient multi-pass synthesis."""
        if not HAS_GENAI:
            raise RuntimeError("google-generativeai package is not installed. Run 'pip install google-generativeai'.")

        # Step 1: Generate Skeleton
        skeleton = self.generate_skeleton(meta)
        if not skeleton:
            print(f"  [Warning] Modular skeleton generation failed. Falling back to single-pass...")
            return self.generate_topic_single_pass(meta)

        # Step 2: Generate each Typology Pool
        question_types = []
        for i, typ_title in enumerate(meta["typologies"]):
            time.sleep(self.delay)
            typ_data = self.generate_typology_pool(meta, i, typ_title)
            if typ_data:
                question_types.append(typ_data)
                print(f"    -> [Success] Typology {i + 1} generated with {len(typ_data.get('pool', []))} questions.")
            else:
                print(f"    -> [Warning] Typology {i + 1} failed.")

        if len(question_types) > 0:
            skeleton["question_types"] = question_types
            skeleton["schema_version"] = "1.0.0"
            skeleton["content_type"] = "learning_topic"
            return skeleton

        return None

    def generate_topic_single_pass(self, meta: Dict[str, Any], max_retries: int = 3) -> Optional[Dict[str, Any]]:
        """Fallback single-pass generator."""
        prompt = build_user_prompt(meta)
        for attempt in range(1, max_retries + 1):
            try:
                response = self.model.generate_content(prompt)
                if response and response.text:
                    data = json.loads(self.clean_json_response(response.text))
                    if "schema_version" in data and "question_types" in data:
                        data["schema_version"] = "1.0.0"
                        data["content_type"] = "learning_topic"
                        return data
                time.sleep(self.delay)
            except Exception as e:
                time.sleep(self.delay)
        return None


# ==============================================================================
# 4. ORCHESTRATOR & BATCH RUNNER
# ==============================================================================
def get_target_file_path(meta: Dict[str, Any]) -> Path:
    """Returns the absolute file path for a topic JSON file."""
    return TOPICS_BASE_DIR / meta["chapter_folder"] / meta["topic_slug"] / f"{meta['topic_slug']}.json"


def is_topic_already_full(meta: Dict[str, Any]) -> bool:
    """Checks if the topic file already exists and has full content (> 25KB)."""
    target = get_target_file_path(meta)
    if target.exists() and target.stat().st_size > 25000:
        return True
    return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate CBSE Class 10 Math Topic JSON datasets using Gemini 3.7 / 2.5 Flash."
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=os.environ.get("GEMINI_API_KEY", ""),
        help="Gemini API Key (or set GEMINI_API_KEY env variable)"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gemini-2.5-flash",
        help="Gemini model name (default: gemini-2.5-flash)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Maximum number of API calls to execute in this batch (default: 20)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process all remaining topics without batch limit"
    )
    parser.add_argument(
        "--chapter",
        type=str,
        default="",
        help="Filter generation to a specific chapter (e.g. 'chapter-4-quadratic-equations')"
    )
    parser.add_argument(
        "--topic",
        type=str,
        default="",
        help="Filter generation to a specific topic slug (e.g. 'nature-of-roots')"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview topics to be generated without executing API calls"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force overwrite existing full topic files"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=15.0,
        help="Seconds delay between consecutive API calls to prevent rate limits (default: 15.0s)"
    )

    args = parser.parse_args()

    print("=" * 80)
    print("SJMATHS CURRICULUM TOPIC DATASET GENERATOR (Universal Schema v1.0.0)")
    print(f"Model: {args.model} | Batch Limit: {'ALL' if args.all else args.limit}")
    print("=" * 80)

    # Filter queue
    queue: List[Dict[str, Any]] = []
    for meta in TOPIC_REGISTRY:
        if args.chapter and args.chapter not in meta["chapter_folder"]:
            continue
        if args.topic and args.topic != meta["topic_slug"]:
            continue
        
        target_path = get_target_file_path(meta)
        is_full = is_topic_already_full(meta)
        
        if is_full and not args.force:
            continue
            
        queue.append(meta)

    # Apply batch limit
    if not args.all and args.limit > 0:
        execution_queue = queue[:args.limit]
    else:
        execution_queue = queue

    print(f"Found {len(TOPIC_REGISTRY)} total registered topics.")
    print(f"Pending topics to generate: {len(queue)}")
    print(f"Topics scheduled for this run: {len(execution_queue)}")
    print("-" * 80)

    for i, meta in enumerate(execution_queue, 1):
        target = get_target_file_path(meta)
        cur_size = target.stat().st_size if target.exists() else 0
        status = "STUB" if cur_size < 25000 else "FULL"
        print(f" {i:02d}. [{meta['chapter_folder']}] {meta['topic_title']} ({status}, {cur_size} bytes)")

    print("-" * 80)

    if args.dry_run:
        print("[DRY RUN COMPLETE] No API calls were made. Run without '--dry-run' to generate.")
        return

    if not args.api_key:
        print("[ERROR] No Gemini API key provided!")
        print("Please provide --api-key <KEY> or set the GEMINI_API_KEY environment variable.")
        sys.exit(1)

    # Initialize Generator
    generator = TopicGenerator(api_key=args.api_key, model_name=args.model, delay=args.delay)

    success_count = 0
    fail_count = 0

    for i, meta in enumerate(execution_queue, 1):
        print(f"\n[{i}/{len(execution_queue)}] Generating '{meta['topic_title']}'...")
        start_t = time.time()
        
        data = generator.generate_topic(meta)
        
        if data:
            target_path = get_target_file_path(meta)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(target_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
            elapsed = time.time() - start_t
            file_size = target_path.stat().st_size
            print(f"  [SUCCESS] Saved {file_size:,} bytes to {target_path.name} in {elapsed:.1f}s")
            success_count += 1
        else:
            print(f"  [FAILED] Could not generate '{meta['topic_title']}'.")
            fail_count += 1

        # Delay before next call
        if i < len(execution_queue):
            time.sleep(args.delay)

    print("\n" + "=" * 80)
    print(f"RUN SUMMARY: {success_count} Generated Successfully | {fail_count} Failed")
    print("=" * 80)


if __name__ == "__main__":
    main()
