import os
import re

def build_office_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Word Processing (MS Word) &amp; Spreadsheet Processing (MS Excel)</span>
    <span class="lang-hi">माइंड मैप: वर्ड प्रोसेसिंग (MS Word) एवं स्प्रेडशीट प्रोसेसिंग (MS Excel)</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[MS Office Elements: Word & Excel] --> B[MS Word Fundamentals]
    A --> C[MS Word Formatting & Features]
    A --> D[MS Excel Fundamentals & Grid]
    A --> E[MS Excel Formulas & Functions]
    A --> F[Essential Shortcuts Comparison]

    B --> B1[Default: .docx XML based font Calibri/Aptos 11pt]
    B --> B2[Interface: Title Bar, Ribbon, Quick Access Toolbar, Status Bar]
    B --> B3[Zoom Range: Minimum 10% to Maximum 500%]

    C --> C1[Paragraph Alignment: Left Ctrl+L, Center Ctrl+E, Right Ctrl+R, Justify Ctrl+J]
    C --> C2[Mail Merge: Main Document + Data Source + Merged Document]
    C --> C3[Drop Cap: In margin/Dropped default 3 lines max 10 lines]
    C --> C4[Spelling & Thesaurus: F7 Spell Check, Shift+F7 Thesaurus Synonyms]

    D --> D1[Grid Capacity: 1048576 Rows numbered + 16384 Columns A to XFD]
    D --> D2[Default: .xlsx Workbook contains worksheets default 1 sheet]
    D --> D3[Cell References: Relative A1, Absolute $A$1 F4 toggle, Mixed $A1]

    E --> E1[Formulas always start with = equal sign]
    E --> E2[Statistical: SUM, AVERAGE, COUNT numbers, COUNTA non-empty, MAX, MIN]
    E --> E3[Lookups: VLOOKUP vertical, HLOOKUP horizontal, XLOOKUP flexible]
    E --> E4[Shortcuts: Alt+= AutoSum, F2 edit cell, Ctrl+; current date, Ctrl+Shift+: time]

    F --> F1[Common: Ctrl+A Select All, Ctrl+Z Undo, Ctrl+Y Redo, Ctrl+S Save]
    F --> F2[Navigation: Ctrl+Enter Page Break, F12 Save As, Shift+F11 New Sheet]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[MS ऑफिस तत्व: वर्ड एवं एक्सेल] --> B[MS Word की मूल संरचना]
    A --> C[MS Word फॉर्मेटिंग एवं विशेषताएं]
    A --> D[MS Excel ग्रिड एवं कार्यक्षेत्र]
    A --> E[MS Excel सूत्र एवं फंक्शन]
    A --> F[महत्वपूर्ण शॉर्टकट कुंजियों की तुलना]

    B --> B1[डिफ़ॉल्ट: .docx एक्सटेंशन, कैलिबरी/एप्टोस 11pt फॉन्ट]
    B --> B2[इंटरफेस: टाइटल बार, रिबन टैब्स, क्विक एक्सेस, स्टेटस बार]
    B --> B3[ज़ूम परास: न्यूनतम 10% से अधिकतम 500%]

    C --> C1[संरेखण Alignment: बायाँ Ctrl+L, मध्य Ctrl+E, दायाँ Ctrl+R, जस्टिफाई Ctrl+J]
    C --> C2[मेल मर्ज: मुख्य दस्तावेज + डेटा स्रोत + विलय दस्तावेज]
    C --> C3[ड्रॉप कैप: डिफ़ॉल्ट 3 पंक्तियाँ, अधिकतम 10 पंक्तियाँ]
    C --> C4[वर्तनी व पर्यायवाची: F7 स्पेलिंग जांच, Shift+F7 थिसॉरस शब्दकोश]

    D --> D1[ग्रिड सीमा: 10,48,576 पंक्तियाँ संख्या + 16,384 कॉलम A से XFD]
    D --> D2[डिफ़ॉल्ट: .xlsx वर्कबुक में वर्कशीट डिफ़ॉल्ट 1 शीट]
    D --> D3[सेल संदर्भ: सापेक्ष A1, निरपेक्ष $A$1 F4 टॉगल, मिश्रित $A1]

    E --> E1[सूत्र सदैव बराबर = चिन्ह से प्रारंभ होते हैं]
    E --> E2[फंक्शन: SUM, AVERAGE, COUNT केवल संख्याएं, COUNTA गैर-रिक्त, MAX, MIN]
    E --> E3[लुकअप: VLOOKUP ऊर्ध्वाधर, HLOOKUP क्षैतिज, XLOOKUP आधुनिक]
    E --> E4[शॉर्टकट: Alt+= ऑटोसम, F2 सेल संपादन, Ctrl+; वर्तमान तिथि, Ctrl+Shift+: समय]

    F --> F1[सामान्य: Ctrl+A सब चुनें, Ctrl+Z पूर्ववत Undo, Ctrl+Y पुनः Redo]
    F --> F2[नेविगेशन: Ctrl+Enter पेज ब्रेक, F12 Save As, Shift+F11 नई शीट]
    </div>
  </div>
</div>

<!-- Card 2: MS Word Comprehensive Fundamentals -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. MS Word: Architecture, Text Formatting &amp; Key Features</span>
    <span class="lang-hi">1. MS Word: वास्तुकला, टेक्स्ट फॉर्मेटिंग एवं महत्वपूर्ण विशेषताएं</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>File Specifications &amp; Default Settings:</strong>
          <br>&bull; <strong>File Extension:</strong> <code>.docx</code> (XML-based format introduced in Word 2007; older versions used <code>.doc</code>). Macro-enabled template is <code>.dotm</code>.
          <br>&bull; <strong>Default Font:</strong> Calibri (11 pt) in Word 2007-2021; Aptos in modern Microsoft 365.
          <br>&bull; <strong>Font Size Limits:</strong> Dropdown menu lists sizes from <strong>8 to 72 pt</strong>. Can be manually set anywhere from <strong>1 to 1638 pt</strong>.
          <br>&bull; <strong>Zoom Slider Range:</strong> Minimum zoom is <strong>10%</strong>; Maximum zoom is <strong>500%</strong> (default 100%).</span>
        <span class="lang-hi"><strong>फाइल विनिर्देश एवं डिफ़ॉल्ट सेटिंग्स:</strong>
          <br>&bull; <strong>फाइल एक्सटेंशन:</strong> <code>.docx</code> (Word 2007 से XML आधारित; पुराने संस्करणों में <code>.doc</code> था)।
          <br>&bull; <strong>डिफ़ॉल्ट फॉन्ट:</strong> कैलिबरी (Calibri 11 pt) या एप्टोस (Aptos)।
          <br>&bull; <strong>फॉन्ट आकार सीमा:</strong> ड्रॉपडाउन मेनू में <strong>8 से 72 pt</strong>; मैनुअल रूप से <strong>1 से 1638 pt</strong> तक सेट किया जा सकता है।
          <br>&bull; <strong>ज़ूम स्लाइडर सीमा:</strong> न्यूनतम <strong>10%</strong> से अधिकतम <strong>500%</strong> (डिफ़ॉल्ट 100%)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Paragraph Alignment &amp; Formatting:</strong>
          <br>&bull; <strong>Left Align (Ctrl + L):</strong> Aligns text against left margin (Default in English).
          <br>&bull; <strong>Center Align (Ctrl + E):</strong> Centers text between margins (used for titles).
          <br>&bull; <strong>Right Align (Ctrl + R):</strong> Aligns text against right margin.
          <br>&bull; <strong>Justify (Ctrl + J):</strong> Distributes text evenly between left and right margins, creating clean flush edges on both sides (used in books/newspapers).
          <br>&bull; <strong>Line Spacing:</strong> Single (<strong>Ctrl + 1</strong>), Double (<strong>Ctrl + 2</strong>), 1.5 Lines (<strong>Ctrl + 5</strong>).
          <br>&bull; <strong>Case Conversion (Shift + F3):</strong> Toggles between Sentence case, lowercase, and UPPERCASE.
          <br>&bull; <strong>Subscript (Ctrl + =):</strong> Lowers character below baseline (e.g., $H_2O$).
          <br>&bull; <strong>Superscript (Ctrl + Shift + +):</strong> Raises character above baseline (e.g., $X^2$).</span>
        <span class="lang-hi"><strong>पैराग्राफ संरेखण (Alignment) एवं फॉर्मेटिंग:</strong>
          <br>&bull; <strong>बायाँ अलाइन (Ctrl + L):</strong> टेक्स्ट को बायीं ओर संरेखित करता है (डिफ़ॉल्ट)।
          <br>&bull; <strong>सेंटर अलाइन (Ctrl + E):</strong> टेक्स्ट को ठीक बीच में लाता है (शीर्षक हेतु)।
          <br>&bull; <strong>दायाँ अलाइन (Ctrl + R):</strong> टेक्स्ट को दायीं ओर संरेखित करता है।
          <br>&bull; <strong>जस्टिफाई (Ctrl + J):</strong> टेक्स्ट को दोनों ओर (बाएं व दाएं) एक समान चौड़ाई में फैलाता है (किताबों/समाचार पत्रों में)।
          <br>&bull; <strong>लाइन स्पेसिंग:</strong> 1.0 (<strong>Ctrl + 1</strong>), 2.0 (<strong>Ctrl + 2</strong>), 1.5 (<strong>Ctrl + 5</strong>)।
          <br>&bull; <strong>सबस्क्रिप्ट (Ctrl + =):</strong> अक्षर को नीचे की ओर लिखना (जैसे $H_2O$)।
          <br>&bull; <strong>सुपरस्क्रिप्ट (Ctrl + Shift + +):</strong> अक्षर को घात/ऊपर लिखना (जैसे $X^2$)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>High-Yield Advanced Word Features:</strong>
          <br>&bull; <strong>Mail Merge (मेल मर्ज):</strong> Generates mass personalized letters, certificates, or envelopes by combining a <strong>Main Document</strong> with an external <strong>Data Source</strong> (Excel spreadsheet or Access database) to produce individual <strong>Merged Documents</strong>.
          <br>&bull; <strong>Drop Cap (ड्रॉप कैप):</strong> Formats the first letter of a paragraph as a large decorative capital letter. Two positions: <em>Dropped</em> (within text) or <em>In Margin</em>. <strong>Default lines dropped = 3</strong>; <strong>Maximum lines = 10</strong>.
          <br>&bull; <strong>Thesaurus (थिसॉरस - Shift + F7):</strong> Built-in dictionary providing synonyms and antonyms for selected words.
          <br>&bull; <strong>Spelling &amp; Grammar Check:</strong> Shortcut is <strong>F7</strong>. Red squiggly line indicates Spelling error; Blue/Green squiggly line indicates Grammar error.</span>
        <span class="lang-hi"><strong>MS Word की महत्वपूर्ण उन्नत विशेषताएं:</strong>
          <br>&bull; <strong>मेल मर्ज (Mail Merge):</strong> एक ही प्रारूप वाले पत्र को सैकड़ों लोगों के अलग-अलग नाम/पते के साथ एक क्लिक में तैयार करना (मुख्य दस्तावेज + डेटा स्रोत = विलय दस्तावेज)।
          <br>&bull; <strong>ड्रॉप कैप (Drop Cap):</strong> पैराग्राफ के पहले अक्षर को बहुत बड़ा सजावटी बनाना। <strong>डिफ़ॉल्ट पंक्तियाँ = 3</strong>; <strong>अधिकतम पंक्तियाँ = 10</strong>।
          <br>&bull; <strong>थिसॉरस (Shift + F7):</strong> शब्दों के पर्यायवाची (Synonyms) एवं विलोम शब्द खोजने वाला शब्दकोश।
          <br>&bull; <strong>स्पेलिंग व ग्रामर जांच (F7):</strong> लाल लहरदार रेखा वर्तनी की गलती दर्शाती है; नीली/हरी रेखा व्याकरण की अशुद्धि दर्शाती है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: MS Excel Grid & Specifications -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. MS Excel: Grid Architecture, Cell Referencing &amp; Formulas</span>
    <span class="lang-hi">2. MS Excel: ग्रिड वास्तुकला, सेल संदर्भ (Referencing) एवं फॉर्मूला प्रणाली</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Excel Specification</span><span class="lang-hi">एक्सेल विनिर्देश</span></th>
          <th><span class="lang-en">Exact Value / Limit</span><span class="lang-hi">मानक मान / सीमा</span></th>
          <th><span class="lang-en">Exam Context &amp; Details</span><span class="lang-hi">परीक्षा उपयोगी विवरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Total Rows in a Worksheet</span><span class="lang-hi">वर्कशीट में कुल पंक्तियाँ (Rows)</span></td>
          <td><strong>1,048,576 rows</strong></td>
          <td><span class="lang-en">Numbered <code>1</code> to <code>1048576</code> (in .xlsx; old .xls had 65,536 rows).</span><span class="lang-hi">संख्या 1 से 10,48,576 तक (पुराने .xls में 65,536 थीं)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Total Columns in a Worksheet</span><span class="lang-hi">वर्कशीट में कुल कॉलम (Columns)</span></td>
          <td><strong>16,384 columns</strong></td>
          <td><span class="lang-en">Labeled <code>A</code> to <code>Z</code>, then <code>AA</code> to <code>ZZ</code>, ending at <strong><code>XFD</code></strong> (old .xls ended at <code>IV</code> / 256 columns).</span><span class="lang-hi">A से Z, फिर AA से ZZ, अंतिम कॉलम <strong>XFD</strong> है।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Default File Extension</span><span class="lang-hi">डिफ़ॉल्ट फाइल एक्सटेंशन</span></td>
          <td><code>.xlsx</code></td>
          <td><span class="lang-en">Excel Workbook (XML Open Format). Macro-enabled workbook is <code>.xlsm</code>.</span><span class="lang-hi">एक्सेल वर्कबुक (.xlsx); मैक्रो वर्कबुक (.xlsm)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">First and Last Cell Address</span><span class="lang-hi">प्रथम एवं अंतिम सेल का पता</span></td>
          <td><code>A1</code> to <code>XFD1048576</code></td>
          <td><span class="lang-en">A cell is formed by the intersection of a row and a column. Active cell address appears in <strong>Name Box</strong>.</span><span class="lang-hi">पंक्ति व कॉलम के मिलन से सेल बनता है। सक्रिय सेल का पता <strong>नेम बॉक्स</strong> में दिखता है।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Default Number of Worksheets</span><span class="lang-hi">नई वर्कबुक में डिफ़ॉल्ट वर्कशीट संख्या</span></td>
          <td><strong>1 Worksheet</strong></td>
          <td><span class="lang-en">Modern Excel creates 1 sheet (Sheet1) by default (older Excel created 3 sheets).</span><span class="lang-hi">आधुनिक एक्सेल में 1 शीट होती है (Sheet1)।</span></td>
        </tr>
      </tbody>
    </table>

    <h4 style="margin:20px 0 10px; color:var(--primary-dark);">
      <span class="lang-en">Cell Referencing Modes (F4 Toggle Key):</span>
      <span class="lang-hi">सेल संदर्भ के तीन प्रकार (F4 शॉर्टकट कुंजी द्वारा):</span>
    </h4>
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Relative Reference (सापेक्ष संदर्भ - e.g., <code>A1</code>):</strong> The default mode. When a formula containing relative references is copied down or across, the row and column coordinates adjust automatically relative to the new position.</span>
        <span class="lang-hi"><strong>सापेक्ष संदर्भ (Relative):</strong> डिफ़ॉल्ट रूप। फॉर्मूला कॉपी करने पर सेल का पता नए स्थान के अनुसार स्वतः बदल जाता है (उदा. <code>=A1+B1</code> को नीचे खींचने पर <code>=A2+B2</code> बन जाएगा)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Absolute Reference (निरपेक्ष संदर्भ - e.g., <code>$A$1</code>):</strong> Uses the dollar sign (<strong><code>$</code></strong>) before both column letter and row number. Locks the cell completely; coordinates <strong>never change</strong> when formula is copied. Press <strong>F4</strong> while editing to toggle.</span>
        <span class="lang-hi"><strong>निरपेक्ष संदर्भ (Absolute):</strong> डॉलर चिन्ह <strong><code>$</code></strong> द्वारा कॉलम और पंक्ति दोनों को लॉक कर दिया जाता है (उदा. <code>$A$1</code>)। फॉर्मूला कॉपी करने पर यह पता कभी नहीं बदलता। <strong>F4</strong> दबाकर डॉलर चिन्ह लगाया जाता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Mixed Reference (मिश्रित संदर्भ - e.g., <code>$A1</code> or <code>A$1</code>):</strong> Either only the column is locked (<code>$A1</code>) or only the row is locked (<code>A$1</code>).</span>
        <span class="lang-hi"><strong>मिश्रित संदर्भ (Mixed):</strong> या तो केवल कॉलम लॉक होता है (<code>$A1</code>) या केवल पंक्ति लॉक होती है (<code>A$1</code>)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Essential MS Excel Functions & Error Codes -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Essential Excel Functions &amp; Formula Error Codes</span>
    <span class="lang-hi">3. महत्वपूर्ण एक्सेल फंक्शन एवं फॉर्मूला त्रुटि कोड</span>
  </div>
  <div class="content-block">
    <p>
      <span class="lang-en"><strong>Rule:</strong> In MS Excel, all formulas and functions <strong>MUST begin with an equal sign (<code>=</code>)</strong>. If entered without <code>=</code>, Excel treats the entry as plain text.</span>
      <span class="lang-hi"><strong>नियम:</strong> MS Excel में सभी सूत्र (Formulas) सदैव <strong>बराबर के चिन्ह (<code>=</code>) से शुरू होने चाहिए</strong>। यदि <code>=</code> नहीं लगाया जाए तो एक्सेल उसे साधारण टेक्स्ट मान लेता है।</span>
    </p>
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Function</span><span class="lang-hi">फंक्शन</span></th>
          <th><span class="lang-en">Syntax Example</span><span class="lang-hi">सिंटैक्स उदाहरण</span></th>
          <th><span class="lang-en">Operational Behavior</span><span class="lang-hi">कार्यप्रणाली</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>SUM</strong></td>
          <td><code>=SUM(A1:A10)</code></td>
          <td><span class="lang-en">Adds all numbers in the specified cell range. Shortcut: <strong>Alt + =</strong> (AutoSum).</span><span class="lang-hi">दिए गए सेल परास के सभी नंबरों का योग निकालता है (शॉर्टकट: <strong>Alt + =</strong>)।</span></td>
        </tr>
        <tr>
          <td><strong>COUNT vs COUNTA</strong></td>
          <td><code>=COUNT(A1:A10)</code> vs <code>=COUNTA(A1:A10)</code></td>
          <td><span class="lang-en"><strong>COUNT</strong> counts cells containing <em>numbers only</em>. <strong>COUNTA</strong> counts all <em>non-empty cells</em> (numbers, text, logical values).</span><span class="lang-hi"><strong>COUNT</strong> केवल <em>संख्याओं</em> वाले सेल गिनता है; <strong>COUNTA</strong> <em>सभी भरे हुए सेल</em> (टेक्स्ट व संख्याएं) गिनता है।</span></td>
        </tr>
        <tr>
          <td><strong>COUNTIF</strong></td>
          <td><code>=COUNTIF(B1:B20, "&gt;50")</code></td>
          <td><span class="lang-en">Counts the number of cells within a range that satisfy a given criteria or condition.</span><span class="lang-hi">दिए गए नियम/शर्त को पूरा करने वाले सेलों की संख्या गिनता है।</span></td>
        </tr>
        <tr>
          <td><strong>IF</strong></td>
          <td><code>=IF(C1&gt;=33, "Pass", "Fail")</code></td>
          <td><span class="lang-en">Returns one value if a condition evaluates to TRUE and another value if FALSE.</span><span class="lang-hi">शर्त सही होने पर पहला मान, गलत होने पर दूसरा मान लौटाता है।</span></td>
        </tr>
        <tr>
          <td><strong>VLOOKUP</strong></td>
          <td><code>=VLOOKUP(101, A2:D50, 3, FALSE)</code></td>
          <td><span class="lang-en"><strong>Vertical Lookup:</strong> Searches for a key value in the leftmost column of a table and returns a value from the specified column in the same row.</span><span class="lang-hi"><strong>ऊर्ध्वाधर लुकअप:</strong> तालिका के पहले कॉलम में मान ढूंढकर उसी पंक्ति के संबंधित कॉलम का मान लौटाता है।</span></td>
        </tr>
      </tbody>
    </table>

    <h4 style="margin:20px 0 10px; color:var(--primary-dark);">
      <span class="lang-en">Common Excel Formula Error Messages:</span>
      <span class="lang-hi">एक्सेल के सामान्य फॉर्मूला त्रुटि कोड (Error Codes):</span>
    </h4>
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong><code>#####</code> :</strong> The column is not wide enough to display the number, or negative date/time is encountered. (Fix: Double-click column header boundary to auto-fit width).</span>
        <span class="lang-hi"><strong><code>#####</code> :</strong> कॉलम की चौड़ाई संख्या दिखाने के लिए कम पड़ रही है (कॉलम को चौड़ा करें)।</span>
      </li>
      <li>
        <span class="lang-en"><strong><code>#DIV/0!</code> :</strong> The formula attempts to divide a number by zero or by an empty cell.</span>
        <span class="lang-hi"><strong><code>#DIV/0!</code> :</strong> किसी संख्या को शून्य (0) से भाग देने का प्रयास किया गया है।</span>
      </li>
      <li>
        <span class="lang-en"><strong><code>#NAME?</code> :</strong> Excel does not recognize text in the formula (typically misspelled function name, e.g. <code>=SMM(A1:A5)</code> instead of <code>=SUM</code>).</span>
        <span class="lang-hi"><strong><code>#NAME?</code> :</strong> फंक्शन के नाम की वर्तनी गलत है (जैसे SUM की जगह SMM लिख दिया गया हो)।</span>
      </li>
      <li>
        <span class="lang-en"><strong><code>#VALUE!</code> :</strong> The formula has wrong type of argument (e.g., attempting mathematical addition on a text cell: <code>=A1 + "Apple"</code>).</span>
        <span class="lang-hi"><strong><code>#VALUE!</code> :</strong> गलत डेटा प्रकार (जैसे संख्या में टेक्स्ट जोड़ने का प्रयास)।</span>
      </li>
      <li>
        <span class="lang-en"><strong><code>#REF!</code> :</strong> Invalid cell reference; occurs when cells referenced in a formula were deleted.</span>
        <span class="lang-hi"><strong><code>#REF!</code> :</strong> अमान्य सेल संदर्भ (फॉर्मूले से संबंधित मूल सेल को डिलीट कर दिया गया है)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Comprehensive Keyboard Shortcuts Comparison -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. High-Yield MS Office Keyboard Shortcuts (Word vs Excel)</span>
    <span class="lang-hi">4. महत्वपूर्ण MS Office शॉर्टकट कुंजियां (Word बनाम Excel तुलना)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Shortcut Key</span><span class="lang-hi">शॉर्टकट कुंजी</span></th>
          <th><span class="lang-en">Action in MS Word</span><span class="lang-hi">MS Word में कार्य</span></th>
          <th><span class="lang-en">Action in MS Excel</span><span class="lang-hi">MS Excel में कार्य</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>F2</strong></td>
          <td><span class="lang-en">Move text or graphics</span><span class="lang-hi">टेक्स्ट ले जाना</span></td>
          <td><strong>Edit the active cell</strong> (कर्सर सेल के अंदर डालना)</td>
        </tr>
        <tr>
          <td><strong>F4</strong></td>
          <td><strong>Repeat last action / Redo</strong></td>
          <td><strong>Toggle Cell Reference ($)</strong> (Relative &rarr; Absolute)</td>
        </tr>
        <tr>
          <td><strong>F7</strong></td>
          <td><strong>Spelling and Grammar Check</strong></td>
          <td><strong>Spelling Check</strong></td>
        </tr>
        <tr>
          <td><strong>Shift + F7</strong></td>
          <td><strong>Thesaurus</strong> (Synonyms dictionary)</td>
          <td>Thesaurus / Research pane</td>
        </tr>
        <tr>
          <td><strong>F12</strong></td>
          <td><strong>Save As dialog</strong></td>
          <td><strong>Save As dialog</strong></td>
        </tr>
        <tr>
          <td><strong>Ctrl + Enter</strong></td>
          <td><strong>Insert Page Break</strong></td>
          <td>Fill selected cells with current entry</td>
        </tr>
        <tr>
          <td><strong>Shift + F11</strong></td>
          <td>Go to previous field</td>
          <td><strong>Insert a new Worksheet</strong></td>
        </tr>
        <tr>
          <td><strong>Ctrl + ; (Semicolon)</strong></td>
          <td>Insert symbol</td>
          <td><strong>Insert Current Date</strong> (आज की तारीख दर्ज करना)</td>
        </tr>
        <tr>
          <td><strong>Ctrl + Shift + : (Colon)</strong></td>
          <td>Insert symbol</td>
          <td><strong>Insert Current Time</strong> (वर्तमान समय दर्ज करना)</td>
        </tr>
        <tr>
          <td><strong>Alt + =</strong></td>
          <td>Insert math equation</td>
          <td><strong>AutoSum</strong> (स्वतः योग फॉर्मूला <code>=SUM()</code> लगाना)</td>
        </tr>
        <tr>
          <td><strong>Ctrl + K</strong></td>
          <td><strong>Insert Hyperlink</strong></td>
          <td><strong>Insert Hyperlink</strong></td>
        </tr>
        <tr>
          <td><strong>Ctrl + H</strong></td>
          <td><strong>Find and Replace dialog</strong></td>
          <td><strong>Find and Replace dialog</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 6: One-Liner Exam Facts -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Key One-Liner Exam Facts (UPSSSC Computer Special)</span>
    <span class="lang-hi">महत्वपूर्ण वन-लाइनर परीक्षा तथ्य (UPSSSC कंप्यूटर विशेष)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Exam Question Topic</span><span class="lang-hi">परीक्षा प्रश्न विषय</span></th>
          <th><span class="lang-en">Core Exam Fact &amp; Details</span><span class="lang-hi">महत्वपूर्ण तथ्य एवं विवरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Total number of rows in an MS Excel worksheet (.xlsx)</span><span class="lang-hi">MS Excel (.xlsx) में कुल पंक्तियों (Rows) की संख्या</span></td>
          <td><span class="lang-en"><strong>1,048,576 rows</strong>.</span><span class="lang-hi"><strong>10,48,576 पंक्तियाँ</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Total number and name of last column in MS Excel</span><span class="lang-hi">MS Excel में कुल कॉलम एवं अंतिम कॉलम का नाम</span></td>
          <td><span class="lang-en"><strong>16,384 columns</strong>; last column is <strong>XFD</strong>.</span><span class="lang-hi"><strong>16,384 कॉलम</strong>; अंतिम कॉलम <strong>XFD</strong> है।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Character that MUST precede every formula in MS Excel</span><span class="lang-hi">एक्सेल में प्रत्येक फॉर्मूले से पहले अनिवार्य चिन्ह</span></td>
          <td><span class="lang-en">Equal sign (<strong><code>=</code></strong>).</span><span class="lang-hi">बराबर का चिन्ह (<strong><code>=</code></strong>)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Key used to toggle absolute cell reference ($) in Excel</span><span class="lang-hi">एक्सेल में निरपेक्ष संदर्भ ($) टॉगल करने की कुंजी</span></td>
          <td><span class="lang-en"><strong>F4 Key</strong>.</span><span class="lang-hi"><strong>F4 कुंजी</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Shortcut key to insert AutoSum formula in Excel</span><span class="lang-hi">एक्सेल में ऑटोसम लगाने की शॉर्टकट कुंजी</span></td>
          <td><span class="lang-en"><strong>Alt + =</strong>.</span><span class="lang-hi"><strong>Alt + =</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Shortcut key to edit the active cell in Excel</span><span class="lang-hi">सक्रिय सेल को संपादित (Edit) करने की कुंजी</span></td>
          <td><span class="lang-en"><strong>F2 Key</strong>.</span><span class="lang-hi"><strong>F2 कुंजी</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Default number of lines dropped by Drop Cap in MS Word</span><span class="lang-hi">MS Word में ड्रॉप कैप द्वारा डिफ़ॉल्ट रूप से घिरी पंक्तियाँ</span></td>
          <td><span class="lang-en"><strong>3 lines</strong> (Maximum allowed is 10 lines).</span><span class="lang-hi"><strong>3 पंक्तियाँ</strong> (अधिकतम सीमा: 10 पंक्तियाँ)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Shortcut to run Spelling and Grammar check in Word</span><span class="lang-hi">स्पेलिंग व ग्रामर जांच की शॉर्टकट कुंजी</span></td>
          <td><span class="lang-en"><strong>F7 Key</strong> (Thesaurus is <strong>Shift + F7</strong>).</span><span class="lang-hi"><strong>F7 कुंजी</strong> (थिसॉरस: <strong>Shift + F7</strong>)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Shortcut key to insert a Page Break in MS Word</span><span class="lang-hi">MS Word में पेज ब्रेक डालने की शॉर्टकट कुंजी</span></td>
          <td><span class="lang-en"><strong>Ctrl + Enter</strong>.</span><span class="lang-hi"><strong>Ctrl + Enter</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Error displayed in Excel when a number is divided by zero</span><span class="lang-hi">एक्सेल में किसी संख्या को 0 से भाग देने पर प्रदर्शित एरर</span></td>
          <td><span class="lang-en"><strong>#DIV/0!</strong>.</span><span class="lang-hi"><strong>#DIV/0!</strong>।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def build_india_achievements_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: India's Achievements in IT, Supercomputing, Hardware &amp; Digital Stack</span>
    <span class="lang-hi">माइंड मैप: सूचना प्रौद्योगिकी, सुपरकंप्यूटिंग, हार्डवेयर एवं इंडिया स्टैक में भारत की उपलब्धियां</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[India's Achievements in IT & Computing] --> B[Supercomputing Milestones]
    A --> C[Indigenous Hardware & Processors]
    A --> D[Digital Public Infrastructure DPI]
    A --> E[Indian Language Technologies]
    A --> F[UP State IT & Tech Achievements]

    B --> B1[Dr. Vijay Bhatkar: Father of Indian Supercomputing]
    B --> B2[PARAM 8000 1991: India's first supercomputer by C-DAC Pune]
    B --> B3[NSM 2015: PARAM Shivay at IIT BHU Varanasi first assembled]
    B --> B4[AIRAWAT C-DAC Pune: India's fastest AI supercomputer Global Top 75]

    C --> C1[SHAKTI 2018: First indigenous RISC-V processor by IIT Madras]
    C --> C2[AJIT 2019: Indigenous microprocessor by IIT Bombay]
    C --> C3[Vikram 1601: Radiation-hardened 32-bit processor by ISRO]
    C --> C4[Vega: 64-bit dual core by C-DAC Pune]

    D --> D1[Aadhaar UIDAI: 12-digit world largest biometric identity]
    D --> D2[UPI NPCI 2016: Global real-time mobile payment benchmark]
    D --> D3[DigiLocker: Cloud document vault 1GB Rule 9A legal parity]
    D --> D4[CoWIN, ONDC, GeM, FASTag, UMANG]

    E --> E1[InScript Keyboard: Standardized BIS bilingual layout]
    E --> E2[GIST C-DAC: Graphics & Intelligence Script Technology]
    E --> E3[Bhashini July 2022: AI-led translation across 22 languages]

    F --> F1[Noida: Electronics manufacturing & mega Data Center hub]
    F --> F2[Lucknow: India's premier AI City 40 acres Nadarganj]
    F --> F3[Portals: UP e-District, IGRS Jansunwai, Bhulekh UP, Nivesh Mitra]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[IT एवं कंप्यूटिंग में भारत की उपलब्धियां] --> B[सुपरकंप्यूटिंग के ऐतिहासिक मील के पत्थर]
    A --> C[स्वदेशी हार्डवेयर एवं माइक्रोप्रोसेसर]
    A --> D[डिजिटल पब्लिक इंफ्रास्ट्रक्चर DPI]
    A --> E[भारतीय भाषा कंप्यूटिंग तकनीकें]
    A --> F[उत्तर प्रदेश की प्रमुख IT उपलब्धियां]

    B --> B1[डॉ. विजय भटकर: भारतीय सुपरकंप्यूटिंग के जनक]
    B --> B2[परम 8000 1991: C-DAC पुणे द्वारा देश का पहला सुपरकंप्यूटर]
    B --> B3[NSM 2015: परम शिवाय IIT BHU वाराणसी पहला स्थापित]
    B --> B4[ऐरावत C-DAC पुणे: भारत का सबसे तेज AI सुपरकंप्यूटर]

    C --> C1[शक्ति SHAKTI 2018: IIT मद्रास द्वारा पहला स्वदेशी RISC-V प्रोसेसर]
    C --> C2[अजीत AJIT 2019: IIT बॉम्बे द्वारा निर्मित माइक्रोप्रोसेसर]
    C --> C3[विक्रम 1601: इसरो ISRO द्वारा विकसित 32-बिट अंतरिक्ष प्रोसेसर]
    C --> C4[वेगा Vega: C-DAC पुणे का 64-बिट प्रोसेसर]

    D --> D1[आधार UIDAI: 12 अंकों की विश्व की सबसे बड़ी बायोमेट्रिक पहचान]
    D --> D2[UPI 2016 NPCI: वैश्विक रीयल-टाइम मोबाइल भुगतान प्रणाली]
    D --> D3[डिजिलॉकर: 1GB क्लाउड दस्तावेज लॉकर कानूनी मान्यता]
    D --> D4[कोविन CoWIN, ONDC, GeM, फास्टैग, उमंग]

    E --> E1[इनस्क्रिप्ट InScript: BIS द्वारा प्रमाणित भारतीय कीबोर्ड लेआउट]
    E --> E2[GIST C-DAC: भारतीय लिपियों की कंप्यूटिंग तकनीक]
    E --> E3[भाषिणी Bhashini 2022: 22 भाषाओं में AI अनुवाद मिशन]

    F --> F1[नोएडा: इलेक्ट्रॉनिक विनिर्माण एवं डेटा सेंटर हब]
    F --> F2[लखनऊ: देश की पहली AI सिटी 40 एकड़ नादरगंज]
    F --> F3[पोर्टल्स: उप्र ई-डिस्ट्रिक्ट, आईजीआरएस जनसुनवाई, भूलेख, निवेश मित्र]
    </div>
  </div>
</div>

<!-- Card 2: Indian Supercomputing Journey -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. India's Supercomputing Journey: PARAM Series to AIRAWAT</span>
    <span class="lang-hi">1. भारत की सुपरकंप्यूटिंग यात्रा: परम श्रृंखला से ऐरावत तक</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Birth of Indian Supercomputing (The Denial &amp; The Triumph):</strong>
          <br>&bull; In <strong>1987</strong>, the United States denied export of the Cray X-MP supercomputer to India (which was sought for monsoon weather forecasting) due to dual-use military sanctions.
          <br>&bull; In response, the Government of India established <strong>C-DAC (Centre for Development of Advanced Computing)</strong> in Pune in <strong>1988</strong> with a mandate to develop an indigenous supercomputer.
          <br>&bull; Under the leadership of <strong>Dr. Vijay Pandurang Bhatkar</strong> (universally recognized as the <strong>"Father of Indian Supercomputing"</strong>), India launched <strong>PARAM 8000 in 1991</strong> (1 GigaFLOPS architecture using parallel processing transputers). It made India only the second nation after the US to develop a supercomputer indigenously.</span>
        <span class="lang-hi"><strong>भारतीय सुपरकंप्यूटिंग का उदय:</strong>
          <br>&bull; वर्ष <strong>1987</strong> में अमेरिका ने मौसम पूर्वानुमान हेतु भारत को क्रे (Cray X-MP) सुपरकंप्यूटर देने से मना कर दिया था।
          <br>&bull; इसके प्रत्युत्तर में भारत सरकार ने <strong>1988</strong> में पुणे में <strong>C-DAC (सेंटर फॉर डेवलपमेंट ऑफ एडवांस्ड कंप्यूटिंग)</strong> की स्थापना की।
          <br>&bull; <strong>डॉ. विजय पांडुरंग भटकर</strong> (भारतीय सुपरकंप्यूटिंग के जनक) के नेतृत्व में भारत ने <strong>1991</strong> में देश का पहला स्वदेशी सुपरकंप्यूटर <strong>परम 8000 (PARAM 8000)</strong> बनाकर विश्व को चकित कर दिया।</span>
      </li>
      <li>
        <span class="lang-en"><strong>National Supercomputing Mission (NSM - 2015):</strong>
          <br>&bull; Launched in March 2015 with an outlay of ₹4,500 crore, jointly steered by the Department of Science and Technology (DST) and Ministry of Electronics &amp; IT (MeitY), implemented by C-DAC and IISc Bangalore.
          <br>&bull; <strong>PARAM Shivay (परम शिवाय):</strong> The <strong>first supercomputer assembled indigenously under NSM</strong>, inaugurated in February 2019 by PM Narendra Modi at <strong>IIT (BHU) Varanasi, Uttar Pradesh</strong> (833 TeraFLOPS capacity).
          <br>&bull; <strong>AIRAWAT (C-DAC, Pune):</strong> India's fastest AI supercomputer (AI Research, Analytics and Knowledge Assimilation Platform), ranked <strong>75th</strong> in the Global TOP500 supercomputer list in 2023.
          <br>&bull; <strong>PARAM Pravega:</strong> Installed at IISc Bangalore (3.3 PetaFLOPS); <strong>PARAM Siddhi-AI</strong> at C-DAC Pune.</span>
        <span class="lang-hi"><strong>राष्ट्रीय सुपरकंप्यूटिंग मिशन (NSM - 2015):</strong>
          <br>&bull; मार्च 2015 में ₹4,500 करोड़ के बजट से विज्ञान एवं प्रौद्योगिकी विभाग (DST) और MeitY द्वारा C-DAC एवं IISc बैंगलोर के माध्यम से प्रारंभ।
          <br>&bull; <strong>परम शिवाय (PARAM Shivay):</strong> NSM के तहत देश में असेंबल किया गया <strong>पहला सुपरकंप्यूटर</strong>, जिसे फरवरी 2019 में <strong>IIT (BHU) वाराणसी, उत्तर प्रदेश</strong> में स्थापित किया गया (833 टेराफ्लॉप्स)।
          <br>&bull; <strong>ऐरावत (AIRAWAT):</strong> C-DAC पुणे में स्थापित भारत का सबसे तेज AI सुपरकंप्यूटर (वैश्विक टॉप 500 में <strong>75वां स्थान</strong>)।
          <br>&bull; <strong>सुपरकंप्यूटर की गति का मापक:</strong> <strong>FLOPS</strong> (फ्लोटिंग प्वाइंट ऑपरेशंस प्रति सेकंड; टेराफ्लॉप्स $10^{12}$, पेटाफ्लॉप्स $10^{15}$)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Indigenous Processors & Hardware -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Indigenous Microprocessors &amp; Hardware Initiatives (Make in India)</span>
    <span class="lang-hi">2. स्वदेशी माइक्रोप्रोसेसर एवं हार्डवेयर निर्माण पहल (मेक इन इंडिया)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Processor Name</span><span class="lang-hi">प्रोसेसर नाम</span></th>
          <th><span class="lang-en">Developing Institution</span><span class="lang-hi">विकासकर्ता संस्थान</span></th>
          <th><span class="lang-en">Architecture &amp; Launch</span><span class="lang-hi">वास्तुकला एवं वर्ष</span></th>
          <th><span class="lang-en">Strategic Importance</span><span class="lang-hi">सामरिक एवं तकनीकी महत्व</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>SHAKTI (शक्ति)</strong></td>
          <td><strong>IIT Madras</strong></td>
          <td>Open-source <strong>RISC-V</strong> architecture (2018)</td>
          <td><span class="lang-en"><strong>India's first indigenous microprocessor</strong>. Free of international licensing; powers smart IoT devices, industrial automation, and defense systems.</span><span class="lang-hi"><strong>भारत का पहला स्वदेशी माइक्रोप्रोसेसर</strong> (2018)। ओपन-सोर्स RISC-V पर आधारित; विदेशी चिप्स पर निर्भरता समाप्त करता है।</span></td>
        </tr>
        <tr>
          <td><strong>AJIT (अजीत)</strong></td>
          <td><strong>IIT Bombay</strong></td>
          <td>SPARC V8 architecture (2019)</td>
          <td><span class="lang-en">First microprocessor completely conceptualized, designed, and fabricated inside India with funding from MeitY. Used in robotics and automation.</span><span class="lang-hi">पूर्णतः भारत में डिजाइन व निर्मित माइक्रोप्रोसेसर (IIT बॉम्बे, 2019)। रोबोटिक्स व नियंत्रण प्रणालियों में प्रयुक्त।</span></td>
        </tr>
        <tr>
          <td><strong>Vikram 1601</strong></td>
          <td><strong>ISRO</strong> (Semi-Conductor Laboratory, Chandigarh)</td>
          <td>32-bit radiation-hardened processor</td>
          <td><span class="lang-en">Designed specifically for satellite launch vehicles (PSLV, GSLV) navigation and space mission onboard computers.</span><span class="lang-hi">इसरो द्वारा रॉकेट प्रक्षेपण यान (PSLV, GSLV) के नेविगेशन और उपग्रहों हेतु विकसित रेडिएशन-प्रतिरोधी चिप।</span></td>
        </tr>
        <tr>
          <td><strong>Vega (वेगा)</strong></td>
          <td><strong>C-DAC</strong> (Centre for Development of Advanced Computing)</td>
          <td>64-bit dual/quad-core RISC-V</td>
          <td><span class="lang-en">High-performance processor designed under the Microprocessor Development Programme (MDP) for telecom and strategic computing.</span><span class="lang-hi">C-DAC द्वारा दूरसंचार और रणनीतिक क्षेत्रों हेतु विकसित 64-बिट स्वदेशी प्रोसेसर।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 4: Digital Public Infrastructure (India Stack) -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Digital Public Infrastructure (India Stack): A Global Benchmark</span>
    <span class="lang-hi">3. डिजिटल पब्लिक इंफ्रास्ट्रक्चर (इंडिया स्टैक): वैश्विक स्तर पर मील का पत्थर</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>What is India Stack?</strong>
          <br>&bull; A unified set of open Application Programming Interfaces (APIs) and digital public goods that allow governments, businesses, and startups to utilize a unique digital infrastructure to solve presence-less, paperless, and cashless service delivery.</span>
        <span class="lang-hi"><strong>इंडिया स्टैक (India Stack) क्या है?</strong>
          <br>&bull; खुले API और डिजिटल सार्वजनिक अवसंरचना का ऐसा एकीकृत समूह जो उपस्थिति-मुक्त (Presence-less), कागज-रहित (Paperless) और नकदी-रहित (Cashless) शासन और वित्तीय समावेशन को संभव बनाता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Core Pillars of the India Stack:</strong>
          <br>&bull; <strong>1. Aadhaar (UIDAI):</strong> World's largest 12-digit biometric digital identity system launched in 2009 under the Unique Identification Authority of India (UIDAI). Provides online authentication via Iris and Fingerprint biometrics.
          <br>&bull; <strong>2. UPI (Unified Payments Interface):</strong> Developed by the <strong>National Payments Corporation of India (NPCI)</strong> and launched in April 2016. Powers instant, 24x7, peer-to-peer and merchant payments via simple Virtual Payment Addresses (VPAs). Recognized globally as the world's most successful real-time payments network (adopted in France, UAE, Singapore, Nepal, Sri Lanka).
          <br>&bull; <strong>3. DigiLocker:</strong> Flagship initiative under Digital India launched in 2015 offering <strong>1 GB secure cloud storage</strong> for citizens. Under Rule 9A of the IT (Preservation and Retention of Information by Intermediaries) Rules 2016, electronic documents issued in DigiLocker have equal legal standing to original physical paper documents.
          <br>&bull; <strong>4. CoWIN:</strong> Scalable cloud platform engineered for COVID-19 vaccination management, processing over 2.2 billion doses seamlessly.
          <br>&bull; <strong>5. ONDC (Open Network for Digital Commerce):</strong> Open non-profit network democratizing digital commerce in India.
          <br>&bull; <strong>6. GeM (Government e-Marketplace):</strong> National public procurement portal ensuring transparency in government buying.</span>
        <span class="lang-hi"><strong>इंडिया स्टैक के प्रमुख स्तंभ:</strong>
          <br>&bull; <strong>1. आधार (Aadhaar - UIDAI):</strong> 12 अंकों की विशिष्ट पहचान संख्या; विश्व का सबसे बड़ा बायोमेट्रिक पहचान डेटाबेस।
          <br>&bull; <strong>2. UPI (यूनिफाइड पेमेंट्स इंटरफेस):</strong> <strong>NPCI</strong> द्वारा 2016 में विकसित; मोबाइल से 24x7 तत्काल धन अंतरण की विश्व की सबसे सफल प्रणाली (फ्रांस, यूएई, सिंगापुर आदि में भी स्वीकृत)।
          <br>&bull; <strong>3. डिजिलॉकर (DigiLocker):</strong> 2015 में प्रारंभ; नागरिकों को <strong>1 GB का सुरक्षित क्लाउड स्पेस</strong> प्रदान करता है। IT नियम 9A के तहत डिजिलॉकर के दस्तावेज मूल कागजी प्रमाण पत्र के समान कानूनी रूप से मान्य हैं।
          <br>&bull; <strong>4. कोविन (CoWIN):</strong> 220 करोड़ से अधिक टीकों का प्रबंधन करने वाला राष्ट्रीय टीकाकरण पोर्टल।
          <br>&bull; <strong>5. ONDC:</strong> डिजिटल ई-कॉमर्स का लोकतंत्रीकरण करने वाला खुला नेटवर्क।
          <br>&bull; <strong>6. GeM (गवर्नमेंट ई-मार्केटप्लेस):</strong> सरकारी खरीद में पारदर्शिता हेतु ऑनलाइन पोर्टल।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Indian Language Tech & Uttar Pradesh Tech Achievements -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Indian Language Technologies &amp; Uttar Pradesh Tech Milestones</span>
    <span class="lang-hi">4. भारतीय भाषा प्रौद्योगिकी एवं उत्तर प्रदेश की तकनीकी उपलब्धियां</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Indian Language Computing Standards:</strong>
          <br>&bull; <strong>InScript (Indian Script Keyboard):</strong> The standardized keyboard layout recognized by the Bureau of Indian Standards (BIS) and Government of India for typing Devanagari (Hindi) and other scheduled Indian scripts. Uses phonetic symmetry across keys.
          <br>&bull; <strong>GIST (Graphics and Intelligence-based Script Technology):</strong> Pioneer mission by C-DAC Pune that developed Hindi font standards and phonetic transliteration algorithms.
          <br>&bull; <strong>Digital India Bhashini:</strong> AI-powered language translation mission launched in July 2022 to break language barriers across 22 official languages using neural translation and speech synthesis.</span>
        <span class="lang-hi"><strong>भारतीय भाषा कंप्यूटिंग मानक:</strong>
          <br>&bull; <strong>इनस्क्रिप्ट (InScript) कीबोर्ड:</strong> भारतीय मानक ब्यूरो (BIS) और भारत सरकार द्वारा देवनागरी एवं भारतीय भाषाओं की टाइपिंग हेतु स्वीकृत आधिकारिक कीबोर्ड लेआउट।
          <br>&bull; <strong>GIST (C-DAC पुणे):</strong> भारतीय लिपियों के कंप्यूटर पर प्रदर्शन और टाइपिंग की आधारशिला।
          <br>&bull; <strong>डिजिटल इंडिया भाषिणी (Bhashini):</strong> 22 आधिकारिक भाषाओं में AI अनुवाद और ध्वनि पहचान उपलब्ध कराने का राष्ट्रीय मिशन।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Uttar Pradesh State IT Milestones (UPSSSC Specific):</strong>
          <br>&bull; <strong>Noida &amp; Greater Noida (IT &amp; Data Center Capital):</strong> Houses mega data center campuses (e.g., Yotta D1), major software development centers of TCS, Infosys, HCL, and major mobile phone manufacturing plants.
          <br>&bull; <strong>India's First AI City in Lucknow:</strong> UP Government has allocated 40 acres in Nadarganj, Lucknow to establish India's premier dedicated Artificial Intelligence hub.
          <br>&bull; <strong>UP e-District Portal:</strong> Online delivery of citizen certificates (caste, income, domicile) without physical visits.
          <br>&bull; <strong>IGRS Jansunwai (जनसुनवाई):</strong> Integrated grievance redressal portal tracking public complaints with geo-tagging.
          <br>&bull; <strong>Bhulekh UP (भूलेख):</strong> Fully digitized online land records portal of Uttar Pradesh for instant verification of Khatauni.
          <br>&bull; <strong>Nivesh Mitra:</strong> Uttar Pradesh's single-window clearance portal for industries and entrepreneurs.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश की प्रमुख IT उपलब्धियां (UPSSSC परीक्षा विशेष):</strong>
          <br>&bull; <strong>नोएडा एवं ग्रेटर नोएडा:</strong> देश का प्रमुख इलेक्ट्रॉनिक्स, सॉफ्टवेयर और मेगा डेटा सेंटर हब (जैसे योट्टा D1 डेटा सेंटर)।
          <br>&bull; <strong>लखनऊ में देश की पहली AI सिटी:</strong> नादरगंज, लखनऊ में ~40 एकड़ में देश का पहला समर्पित AI शहर विकसित किया जा रहा है।
          <br>&bull; <strong>उप्र ई-डिस्ट्रिक्ट (e-District):</strong> जाति, आय, निवास प्रमाण पत्रों की शत-प्रतिशत ऑनलाइन व पारदर्शी डिलीवरी।
          <br>&bull; <strong>आईजीआरएस जनसुनवाई (Jansunwai):</strong> जन शिकायतों के निवारण हेतु एकीकृत ऑनलाइन पोर्टल।
          <br>&bull; <strong>भूलेख उप्र (Bhulekh UP):</strong> भूमि खतौनी और अभिलेखों का संपूर्ण डिजिटलीकरण।
          <br>&bull; <strong>निवेश मित्र (Nivesh Mitra):</strong> उद्योगों को सिंगल-विंडो मंजूरी देने वाला राज्य का अग्रणी पोर्टल।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: One-Liner Exam Facts -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Key One-Liner Exam Facts (UPSSSC Computer Special)</span>
    <span class="lang-hi">महत्वपूर्ण वन-लाइनर परीक्षा तथ्य (UPSSSC कंप्यूटर विशेष)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Exam Question Topic</span><span class="lang-hi">परीक्षा प्रश्न विषय</span></th>
          <th><span class="lang-en">Core Exam Fact &amp; Details</span><span class="lang-hi">महत्वपूर्ण तथ्य एवं विवरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Father of Indian Supercomputing</span><span class="lang-hi">भारतीय सुपरकंप्यूटिंग के जनक</span></td>
          <td><span class="lang-en"><strong>Dr. Vijay Pandurang Bhatkar</strong> (developed PARAM 8000 in 1991).</span><span class="lang-hi"><strong>डॉ. विजय पांडुरंग भटकर</strong> (1991 में परम 8000 का निर्माण)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">First supercomputer developed indigenously in India</span><span class="lang-hi">भारत का पहला स्वदेशी सुपरकंप्यूटर</span></td>
          <td><span class="lang-en"><strong>PARAM 8000</strong> (built by C-DAC Pune in 1991).</span><span class="lang-hi"><strong>परम 8000 (PARAM 8000)</strong> (1991, C-DAC पुणे)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">First supercomputer assembled under National Supercomputing Mission</span><span class="lang-hi">राष्ट्रीय सुपरकंप्यूटिंग मिशन के तहत स्थापित पहला सुपरकंप्यूटर</span></td>
          <td><span class="lang-en"><strong>PARAM Shivay</strong> at <strong>IIT (BHU) Varanasi, UP</strong> (Feb 2019).</span><span class="lang-hi"><strong>परम शिवाय</strong>, <strong>IIT (BHU) वाराणसी, उप्र</strong> (2019)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">India's fastest AI supercomputer ranked in Global TOP500</span><span class="lang-hi">वैश्विक टॉप 500 में स्थान पाने वाला भारत का सबसे तेज AI सुपरकंप्यूटर</span></td>
          <td><span class="lang-en"><strong>AIRAWAT</strong> (C-DAC, Pune - Ranked 75th globally in 2023).</span><span class="lang-hi"><strong>ऐरावत (AIRAWAT)</strong> (C-DAC पुणे, 75वां स्थान)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">First indigenous microprocessor designed and built in India</span><span class="lang-hi">भारत का पहला स्वदेशी माइक्रोप्रोसेसर</span></td>
          <td><span class="lang-en"><strong>SHAKTI</strong> (developed by <strong>IIT Madras</strong> in 2018 on RISC-V).</span><span class="lang-hi"><strong>शक्ति (SHAKTI)</strong> (IIT मद्रास द्वारा 2018 में विकसित)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Organization that developed Unified Payments Interface (UPI)</span><span class="lang-hi">यूनिफाइड पेमेंट्स इंटरफेस (UPI) को विकसित करने वाली संस्था</span></td>
          <td><span class="lang-en"><strong>NPCI</strong> (National Payments Corporation of India, 2016).</span><span class="lang-hi"><strong>NPCI</strong> (भारतीय राष्ट्रीय भुगतान निगम)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Storage capacity provided to every citizen in DigiLocker</span><span class="lang-hi">डिजिलॉकर में प्रत्येक नागरिक को मिलने वाला क्लाउड स्पेस</span></td>
          <td><span class="lang-en"><strong>1 GB</strong> (legally valid under Rule 9A of IT Rules 2016).</span><span class="lang-hi"><strong>1 GB</strong> (आईटी नियम 9A के तहत कानूनी रूप से मान्य)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Official standardized keyboard layout for typing Indian languages</span><span class="lang-hi">भारतीय भाषाओं की टाइपिंग हेतु आधिकारिक मानक कीबोर्ड</span></td>
          <td><span class="lang-en"><strong>InScript Keyboard</strong> (मानकीकृत BIS लेआउट).</span><span class="lang-hi"><strong>इनस्क्रिप्ट (InScript) कीबोर्ड</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">City in Uttar Pradesh being developed as India's first AI City</span><span class="lang-hi">उप्र का शहर जिसे देश की पहली AI सिटी के रूप में विकसित किया जा रहा है</span></td>
          <td><span class="lang-en"><strong>Lucknow</strong> (Nadarganj area, ~40 acres).</span><span class="lang-hi"><strong>लखनऊ</strong> (नादरगंज, ~40 एकड़)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Online land records verification portal of Uttar Pradesh Government</span><span class="lang-hi">उत्तर प्रदेश सरकार का ऑनलाइन भूमि खतौनी पोर्टल</span></td>
          <td><span class="lang-en"><strong>Bhulekh UP</strong> (भूलेख उत्तर प्रदेश).</span><span class="lang-hi"><strong>भूलेख उप्र (Bhulekh UP)</strong>।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def enrich_file(rel_path, theory_html):
    target_file = os.path.join("upsssc-computer", rel_path, "index.html")
    if not os.path.exists(target_file):
        print(f"Error: {target_file} not found")
        return False

    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print(f"ERROR: Could not locate tab-theory boundary in {target_file}!")
        return False

    updated_html = html[:match.start()] + theory_html.strip() + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file}")
    return True

def main():
    enrich_file("important-elements-of-word-processing-ms-word-and-excel-processing-ms-excel", build_office_theory_html())
    enrich_file("india-s-achievements-in-this-field", build_india_achievements_theory_html())

if __name__ == "__main__":
    main()
