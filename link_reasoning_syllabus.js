const fs = require('fs');

const syllabusPath = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/syllabus/index.html';
let html = fs.readFileSync(syllabusPath, 'utf8');

const newItemsHtml = `
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-6" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/analytical-reasoning/coding-and-decoding-numerical-operations-venn-diagrams/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Coding, Decoding, Numerical Operations & Venn Diagrams</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-7" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/blood-relations/blood-relations-family-tree-drawing-coded-relations/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Family Tree Drawing & Coded Relations</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-8" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/blood-relations-relationship-concepts/seating-arrangement-blood-relations/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Seating Arrangement & Blood Relations</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-9" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/coding-and-decoding/coding-decoding-letter-to-letter-letter-to-number-matrix-coding/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Matrix & Letter-Number Coding</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-10" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/critical-emotional-social-intelligence/critical-reasoning-statement-assumption-statement-conclusion/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Statement Assumption & Critical Reasoning</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-11" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/figural-classification/classification-semantic-number-and-symbol-odd-one-out/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Odd One Out (Semantic, Number & Symbol)</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-12" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/figural-classification/semantic-number-and-figural-classification/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Semantic & Figural Classification</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-13" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/figural-classification/space-orientation-space-visualization-venn-logic/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Space Visualization & Venn Logic</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-14" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/non-verbal-series/non-verbal-series-figural-classification/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Non-Verbal Series & Figural Classification</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-15" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/number-series/semantic-number-and-figural-series/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Semantic, Number & Figural Series</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-16" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/problem-solving-analysis/direction-sense-test-angles-of-turn-final-direction-distance/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Direction Sense Test (Angles & Distance)</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-17" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/problem-solving-analysis/order-ranking-row-positioning-top-bottom-comparisons/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Order & Ranking (Row Positioning)</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-18" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/problem-solving-analysis/venn-diagrams-logical-representation-of-classes/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Logical Representation of Classes (Venn Diagrams)</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-19" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/space-visualisation/paper-folding-cutting-mirror-and-water-image-logic/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Paper Folding, Cutting, Mirror & Water Image</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-20" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/space-visualisation/space-visualisation-spatial-orientation/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Space Visualisation & Spatial Orientation</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-21" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/statement-conclusion/statement-conclusion-critical-reasoning/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Statement Conclusion & Critical Reasoning</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-22" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/syllogism/syllogism-statements-and-conclusions-venn-representation/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Syllogism & Venn Representation</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-23" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/topics/address-date-and-city-matching/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Address, Date & City Matching</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-24" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/topics/classification-of-roll-numberscentre-codes/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Classification of Roll Numbers & Centre Codes</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-25" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/topics/critical-thinking/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Critical Thinking</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-26" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/topics/decision-making/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Decision Making</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-27" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/topics/discrimination/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Discrimination & Spatial Ability</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-28" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/topics/emotional-intelligence/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Emotional Intelligence</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-29" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/topics/numerical-operations/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Numerical Operations</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-30" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/topics/social-intelligence/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Social Intelligence</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-31" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/topics/trends-and-patterns/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Trends & Patterns</a>
</span>
</li>
<li class="syllabus-item">
<input class="syllabus-checkbox" id="tier1-c1-cb-4-32" type="checkbox"/>
<span class="syllabus-text">
<a class="syllabus-link" href="../reasoning/topics/word-building/" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">Word Building</a>
</span>
</li>
`;

const targetStr = `../reasoning/critical-emotional-social-intelligence/`;

const idx = html.indexOf(targetStr);
if (idx !== -1) {
    const endLiIdx = html.indexOf('</li>', idx);
    if (endLiIdx !== -1) {
        const insertPos = endLiIdx + 5;
        html = html.slice(0, insertPos) + '\n' + newItemsHtml + html.slice(insertPos);
        fs.writeFileSync(syllabusPath, html, 'utf8');
        console.log('✅ Successfully linked all 27 new microtopics in ssc-cgl/syllabus/index.html!');
    }
} else {
    console.log('❌ Target string not found');
}
