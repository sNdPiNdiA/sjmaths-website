# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "cpu-architecture-registers"
TOPIC_DISPLAY = "CPU Architecture & Registers"
TOPIC_DISPLAY_HI = "सीपीयू आर्किटेक्चर और रजिस्टर"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\computer-knowledge\{TOPIC}"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "Computer Knowledge",
    "parentUrl": "../",
    "current": "CPU Architecture & Registers"
}

hero_en = {
    "title": "CPU Architecture & Registers",
    "description": "Master the inner workings of the Central Processing Unit. Learn about the Control Unit (CU), Arithmetic Logic Unit (ALU), the Fetch-Decode-Execute machine cycle, RISC vs CISC, Von Neumann vs Harvard designs, system buses, and CPU registers (PC, IR, Accumulator, MAR, MDR)."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive CPU Architecture Mock Test",
        "description": "Test your grasp on register functions, bus types, processor cycles, and architecture differences. Timed 15-question mock test.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Milestones in CPU Architecture Design",
    "description": "Key stages in the evolution of microprocessors and computer architecture.",
    "cards": [
        {
            "period": "First Draft of a Report on the EDVAC",
            "date": "1945",
            "details": "John von Neumann described a computer architecture where program data and instruction code are stored in the same memory space (**Von Neumann Architecture**)."
        },
        {
            "period": "Intel 4004 Microprocessor",
            "date": "1971",
            "details": "The first commercially available single-chip microprocessor. A 4-bit CPU designed by Federico Faggin, Ted Hoff, and Masatoshi Shima."
        },
        {
            "period": "Rise of RISC Architecture",
            "date": "1980s",
            "details": "Pioneered by John Cocke at IBM, David Patterson at Berkeley, and John Hennessy at Stanford. Focused on simple, single-cycle instructions to boost clock speed."
        },
        {
            "period": "x86-64 64-bit Extension",
            "date": "2000s",
            "details": "AMD introduced AMD64, extending Intel's 32-bit x86 CISC architecture to 64-bit, allowing processors to address vast amounts of memory directly."
        }
    ]
}

mnemonics_en = {
    "title": "Recall Mnemonics",
    "description": "Memory hooks to associate CPU registers and concepts with their correct functions.",
    "items": [
        {
            "title": "Mnemonic 1: The Machine Cycle",
            "phrase": "\"F-D-E-S (Fetch - Decode - Execute - Store)\"",
            "decryption": "The four main stages of the CPU execution cycle:<br>• **F** — **F**etch (grabs instruction from RAM)<br>• **D** — **D**ecode (Control Unit interprets the instruction)<br>• **E** — **E**xecute (ALU performs computation)<br>• **S** — **S**tore (writes results back to memory/registers)"
        },
        {
            "title": "Mnemonic 2: Register Identification",
            "phrase": "\"P-I-M-D-A (PC - IR - MAR - MDR - Accumulator)\"",
            "decryption": "Key registers inside the CPU:<br>• **P** — **P**rogram Counter (holds **next** instruction address)<br>• **I** — **I**nstruction Register (holds **current** instruction being executed)<br>• **M** — **M**emory Address Register (holds address of memory **location**)<br>• **D** — **M**emory Data Register (holds **actual data** read or write)<br>• **A** — **A**ccumulator (holds **intermediate results** of ALU)"
        },
        {
            "title": "Mnemonic 3: System Bus Roles",
            "phrase": "\"C-A-D (Control - Address - Data)\"",
            "decryption": "The three buses in system design:<br>• **C** — **C**ontrol Bus (carries command signals; bidirectional)<br>• **A** — **A**ddress Bus (carries memory locations; **unidirectional from CPU**)<br>• **D** — **D**ata Bus (carries actual content data; bidirectional)"
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Hover or click to reveal the answers. Revisit these cards to build instant recall.",
    "items": [
        {
            "question": "Which CPU register stores the address of the next instruction to be fetched from memory?",
            "answer": "**Program Counter (PC)**. Once an instruction is fetched, the PC automatically increments to point to the next instruction in sequence.",
            "icon": "fa-clock"
        },
        {
            "question": "What is the key structural difference between Von Neumann and Harvard architectures?",
            "answer": "**Von Neumann** uses a single shared memory and bus for both instructions and data. **Harvard Architecture** uses physically separate memories and buses for instructions and data, avoiding the Von Neumann bottleneck.",
            "icon": "fa-microchip"
        },
        {
            "question": "Which register holds the output of the ALU's latest arithmetic or logical operation?",
            "answer": "**Accumulator (AC)**. It acts as a temporary buffer for immediate calculations before they are stored back in RAM.",
            "icon": "fa-calculator"
        },
        {
            "question": "What are the characteristics of RISC processors compared to CISC?",
            "answer": "**RISC (Reduced Instruction Set Computer)** uses simple instructions of fixed length that execute in a single clock cycle, relies heavily on software optimization, and has many general-purpose registers (e.g., ARM). **CISC (Complex Instruction Set Computer)** uses complex instructions of variable length that execute in multiple cycles, focusing on hardware-level complexity (e.g., Intel x86).",
            "icon": "fa-bolt"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid",
    "items": [
        "<strong>Trap 1:</strong> Confusing Program Counter (PC) with Instruction Register (IR). The **PC** holds the address of the **NEXT** instruction to be executed, whereas the **IR** holds the **CURRENT** instruction that is currently being decoded/executed.",
        "<strong>Trap 2:</strong> Assuming the Address Bus is bidirectional. The **Address Bus is strictly unidirectional** (transmitting addresses only from the CPU to memory/IO devices). The **Data Bus** and **Control Bus** are bidirectional.",
        "<strong>Trap 3:</strong> Confusing MAR with MDR/MBR. The **Memory Address Register (MAR)** holds the memory *location (address)*, while the **Memory Data Register (MDR)** holds the actual *data value* that is written to or read from that location.",
        "<strong>Trap 4:</strong> Thinking CISC uses more registers than RISC. Actually, **RISC uses a larger number of general-purpose registers** to minimize slower memory accesses, whereas CISC has fewer registers because it supports complex instructions that access memory directly."
    ]
}

deep_dive_en = [
    {
        "title": "1. CPU Organization & Control Unit Dynamics",
        "content": """<p>The Central Processing Unit (CPU) is the brain of the computer system, composed of three main internal components: the Control Unit (CU), the Arithmetic Logic Unit (ALU), and the Registers.</p>
        
        <h3>A. Internal Components of the CPU</h3>
        <ul>
          <li><strong>Control Unit (CU):</strong> Coordinates the execution of instructions. It directs the flow of signals between the CPU and other peripherals, decoding instructions using a microprogram or hardwired logic.</li>
          <li><strong>Arithmetic Logic Unit (ALU):</strong> Performs all calculations (addition, subtraction, multiplication, division) and logical comparisons (AND, OR, NOT, comparisons).</li>
          <li><strong>Registers:</strong> High-speed internal storage locations situated directly inside the processor chip. They operate at the CPU core speed, which is much faster than cache memory and RAM.</li>
        </ul>

        <h3>B. The Fetch-Decode-Execute Cycle (Machine Cycle)</h3>
        <ol>
          <li><strong>Fetch:</strong> The Control Unit retrieves the instruction from the memory address specified by the Program Counter (PC) and loads it into the Instruction Register (IR).</li>
          <li><strong>Decode:</strong> The Control Unit decodes the instruction inside the IR to determine what action is required.</li>
          <li><strong>Execute:</strong> The ALU performs the decoded operation (e.g., adding two numbers or comparing values).</li>
          <li><strong>Store (Write-back):</strong> The result generated by the execution phase is written back to a register or memory location.</li>
        </ol>"""
    },
    {
        "title": "2. Special Purpose Registers (SPRs)",
        "content": """<p>CPU Registers are classified into general-purpose (accessible to assembly programmers) and special-purpose registers, which have dedicated hardware functions.</p>
        
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Register Name</th>
                <th>Abbreviation</th>
                <th>Primary Function & Technical Working</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Program Counter</strong></td>
                <td>PC</td>
                <td>Holds the memory address of the next instruction to be fetched. It automatically increments by the size of the instruction.</td>
              </tr>
              <tr>
                <td><strong>Instruction Register</strong></td>
                <td>IR</td>
                <td>Holds the binary code of the instruction currently being executed/decoded by the Control Unit.</td>
              </tr>
              <tr>
                <td><strong>Memory Address Register</strong></td>
                <td>MAR</td>
                <td>Holds the physical memory address that the CPU wants to read from or write data to. Connected directly to the Address Bus.</td>
              </tr>
              <tr>
                <td><strong>Memory Data / Buffer Register</strong></td>
                <td>MDR / MBR</td>
                <td>Holds the actual data content fetched from RAM, or data waiting to be written to RAM. Connected to the Data Bus.</td>
              </tr>
              <tr>
                <td><strong>Accumulator</strong></td>
                <td>AC / ACC</td>
                <td>Holds intermediate arithmetic and logical results. Inputs and outputs of the ALU frequently route through it.</td>
              </tr>
              <tr>
                <td><strong>Stack Pointer</strong></td>
                <td>SP</td>
                <td>Points to the current top address of the stack memory region in RAM, used for tracking return addresses during subroutine calls.</td>
              </tr>
              <tr>
                <td><strong>Program Status Word / Flags</strong></td>
                <td>PSW / FR</td>
                <td>Contains status bits (flags) like Carry Flag (CF), Zero Flag (ZF), Sign Flag (SF), and Overflow Flag (OF) indicating properties of the last ALU result.</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "3. Architecture Models & System Buses",
        "content": """<p>Computer performance depends heavily on the memory layout and the interconnecting buses.</p>
        
        <h3>A. Von Neumann vs. Harvard Architecture</h3>
        <ul>
          <li><strong>Von Neumann Architecture:</strong> Uses a single memory space and shared bus system for both instructions (code) and data. This leads to the **Von Neumann Bottleneck**, as the CPU cannot read an instruction and read/write data at the exact same time.</li>
          <li><strong>Harvard Architecture:</strong> Uses physically separate memory units and separate bus lines for code and data. This allows simultaneous instruction fetch and data access, which is highly utilized in Digital Signal Processors (DSPs) and modern microcontrollers.</li>
        </ul>

        <h3>B. System Buses (Interconnects)</h3>
        <p>A bus is a set of parallel wires used to transmit signals between computer components:</p>
        <ul>
          <li><strong>Address Bus:</strong> Carries the physical memory address from the CPU to the RAM/IO. **Unidirectional**. Width of address bus determines maximum addressable memory capacity ($2^N$ locations).</li>
          <li><strong>Data Bus:</strong> Transmits actual data/instructions between memory, CPU, and IO devices. **Bidirectional**. Width determines processor word size (e.g., 32-bit or 64-bit).</li>
          <li><strong>Control Bus:</strong> Carries control signals (read/write commands, clock pulses, interrupts) to coordinate system operations. **Bidirectional**.</li>
        </ul>

        <h3>C. Processor design philosophy: RISC vs. CISC</h3>
        <ul>
          <li><strong>RISC (Reduced Instruction Set Computer):</strong> Uses a small set of simple, uniform-length instructions. Executes most instructions in **one clock cycle** using pipelining. Has a large register file and relies on compilers. Examples: ARM (used in mobile phones), MIPS, RISC-V.</li>
          <li><strong>CISC (Complex Instruction Set Computer):</strong> Focuses on complex instructions that can perform multiple operations (like loading from memory, adding, and storing with one instruction). Instructions have variable lengths and take multiple clock cycles. Fewer registers. Examples: Intel x86, AMD64.</li>
        </ul>"""
    }
]

# ----------------- HINDI DATA DEFINITIONS -----------------
breadcrumbs_hi = {
    "parent": "कंप्यूटर ज्ञान",
    "parentUrl": "../",
    "current": "सीपीयू आर्किटेक्चर और रजिस्टर"
}

hero_hi = {
    "title": "सीपीयू आर्किटेक्चर और रजिस्टर",
    "description": "सेंट्रल प्रोसेसिंग यूनिट (CPU) की आंतरिक कार्यप्रणाली पर महारत हासिल करें। कंट्रोल यूनिट (CU), अर्थमेटिक लॉजिक यूनिट (ALU), मशीन चक्र (Fetch-Decode-Execute), RISC बनाम CISC, वॉन न्यूमैन बनाम हार्वर्ड डिजाइन, सिस्टम बस और सीपीयू रजिस्टर (PC, IR, Accumulator, MAR, MDR) के बारे में सीखें।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "इंटरएक्टिव सीपीयू आर्किटेक्चर मॉक टेस्ट",
        "description": "रजिस्टर के कार्यों, बस के प्रकारों, प्रोसेसर चक्रों और आर्किटेक्चर के अंतर पर आधारित 15-प्रश्न मॉक टेस्ट।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "सीपीयू आर्किटेक्चर डिजाइन के मील का पत्थर",
    "description": "माइक्रोप्रोसेसरों और कंप्यूटर वास्तुकला के विकास में प्रमुख चरण।",
    "cards": [
        {
            "period": "EDVAC पर एक रिपोर्ट का पहला मसौदा",
            "date": "1945",
            "details": "जॉन वॉन न्यूमैन ने एक कंप्यूटर वास्तुकला का वर्णन किया जहाँ प्रोग्राम डेटा और निर्देश कोड एक ही मेमोरी स्पेस में संग्रहीत होते हैं (**वॉन न्यूमैन आर्किटेक्चर**)।"
        },
        {
            "period": "इंटेल 4004 माइक्रोप्रोसेसर",
            "date": "1971",
            "details": "व्यावसायिक रूप से उपलब्ध पहला सिंगल-चिप माइक्रोप्रोसेसर। यह फेडेरिको फागिन, टेड हॉफ और मासातोशी शिमा द्वारा डिजाइन किया गया 4-बिट सीपीयू था।"
        },
        {
            "period": "RISC आर्किटेक्चर का उदय",
            "date": "1980 का दशक",
            "details": "आईबीएम में जॉन कॉके, बर्कले में डेविड पैटरसन और स्टैनफोर्ड में जॉन हेनेसी द्वारा शुरू किया गया। इसमें घड़ी की गति को बढ़ाने के लिए सरल, एकल-चक्र निर्देशों पर ध्यान केंद्रित किया गया।"
        },
        {
            "period": "x86-64 64-बिट विस्तार",
            "date": "2000 का दशक",
            "details": "AMD ने AMD64 पेश किया, जिसने इंटेल के 32-बिट x86 CISC आर्किटेक्चर को 64-बिट तक बढ़ा दिया, जिससे प्रोसेसर सीधे भारी मात्रा में मेमोरी एड्रेस कर सकते हैं।"
        }
    ]
}

mnemonics_hi = {
    "title": "त्वरित याद रखने की ट्रिक्स (Mnemonics)",
    "description": "सीपीयू रजिस्टरों और अवधारणाओं को उनके सही कार्यों के साथ याद रखने के लिए आसान मेमोरी ट्रिक्स।",
    "items": [
        {
            "title": "स्मृति सूत्र 1: मशीन चक्र (F-D-E-S)",
            "phrase": "\"F-D-E-S\"",
            "decryption": "सीपीयू निष्पादन चक्र के चार मुख्य चरण:<br>• **F** — **F**etch (रैम से निर्देश प्राप्त करना)<br>• **D** — **D**ecode (कंट्रोल यूनिट निर्देश की व्याख्या करती है)<br>• **E** — **E**xecute (ALU गणना निष्पादित करता है)<br>• **S** — **S**tore (परिणामों को वापस मेमोरी/रजिस्टर में लिखना)"
        },
        {
            "title": "स्मृति सूत्र 2: मुख्य रजिस्टर (P-I-M-D-A)",
            "phrase": "\"P-I-M-D-A\"",
            "decryption": "सीपीयू के भीतर महत्वपूर्ण रजिस्टर:<br>• **P** — **P**rogram Counter (अगले निर्देश का पता रखता है)<br>• **I** — **I**nstruction Register (वर्तमान में निष्पादित हो रहे निर्देश को रखता है)<br>• **M** — **M**emory Address Register (मेमोरी के पते को रखता है)<br>• **D** — **M**emory Data Register (वास्तविक डेटा मान को रखता है)<br>• **A** — **A**ccumulator (ALU के अंतरिम परिणामों को रखता है)"
        },
        {
            "title": "स्मृति सूत्र 3: सिस्टम बस भूमिकाएं (C-A-D)",
            "phrase": "\"C-A-D\"",
            "decryption": "सिस्टम बस प्रकार:<br>• **C** — **C**ontrol Bus (नियंत्रण संकेत ले जाती है; द्वि-दिशात्मक)<br>• **A** — **A**ddress Bus (मेमोरी का पता ले जाती है; **केवल सीपीयू से बाहर**)<br>• **D** — **D**ata Bus (वास्तविक डेटा/निर्देश ले जाती है; द्वि-दिशात्मक)"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय रिकॉल फ्लैशकार्ड",
    "description": "उत्तर देखने के लिए होवर करें या क्लिक करें। त्वरित याददाश्त बनाने के लिए इन कार्डों को दोबारा देखें।",
    "items": [
        {
            "question": "कौन सा सीपीयू रजिस्टर मेमोरी से लाए जाने वाले अगले निर्देश का पता संग्रहीत करता है?",
            "answer": "**प्रोग्राम काउंटर (PC)**। एक बार निर्देश प्राप्त हो जाने के बाद, PC स्वचालित रूप से अगले निर्देश को इंगित करने के लिए बढ़ जाता है।",
            "icon": "fa-clock"
        },
        {
            "question": "वॉन न्यूमैन और हार्वर्ड आर्किटेक्चर के बीच मुख्य संरचनात्मक अंतर क्या है?",
            "answer": "**वॉन न्यूमैन** निर्देश और डेटा दोनों के लिए एक ही मेमोरी और बस का उपयोग करता है। **हार्वर्ड आर्किटेक्चर** निर्देश और डेटा के लिए अलग-अलग मेमोरी और बस का उपयोग करता है, जिससे 'वॉन न्यूमैन बॉटलनैक' से बचा जा सकता है।",
            "icon": "fa-microchip"
        },
        {
            "question": "कौन सा रजिस्टर ALU के नवीनतम गणितीय या तार्किक संचालन के आउटपुट को संग्रहीत करता है?",
            "answer": "**एक्यूमुलेटर (Accumulator - AC)**। यह गणनाओं के परिणाम को रैम में वापस भेजने से पहले अस्थायी रूप से रखता है।",
            "icon": "fa-calculator"
        },
        {
            "question": "CISC की तुलना में RISC प्रोसेसर की क्या विशेषताएं हैं?",
            "answer": "**RISC (रिड्यूस्ड इंस्ट्रक्शन सेट कंप्यूटर)** सरल, निश्चित लंबाई के निर्देशों का उपयोग करता है जो एक चक्र में चलते हैं, और इसमें अधिक जनरल-पर्पज रजिस्टर होते हैं (जैसे, ARM)। **CISC (कॉम्प्लेक्स इंस्ट्रक्शन सेट कंप्यूटर)** जटिल और परिवर्तनशील लंबाई के निर्देशों का उपयोग करता है और हार्डवेयर-स्तरीय जटिलता पर ध्यान केंद्रित करता है (जैसे, इंटेल x86)।",
            "icon": "fa-bolt"
        }
    ]
}

traps_hi = {
    "title": "परीक्षा में बचाव योग्य सामान्य भ्रम (Traps)",
    "items": [
        "<strong>भ्रम 1:</strong> प्रोग्राम काउंटर (PC) और इंस्ट्रक्शन रजिस्टर (IR) में भ्रमित होना। **PC अगले** निर्देश का पता रखता है, जबकि **IR वर्तमान** निर्देश को रखता है जो अभी निष्पादित या डिकोड हो रहा है।",
        "<strong>भ्रम 2:</strong> एड्रेस बस को द्वि-दिशात्मक (Bidirectional) मानना। **एड्रेस बस केवल एक दिशा में (Unidirectional)** काम करती है (सीपीयू से रैम/आईओ की तरफ पते ले जाती है)। **डेटा बस** और **कंट्रोल बस** द्वि-दिशात्मक होते हैं।",
        "<strong>भ्रम 3:</strong> MAR और MDR/MBR में अंतर भूलना। **Memory Address Register (MAR)** मेमोरी की *जगह (पता)* रखता है, जबकि **Memory Data Register (MDR)** उस जगह लिखा या पढ़ा जाने वाला *वास्तविक डेटा मान* रखता है।",
        "<strong>भ्रम 4:</strong> यह सोचना कि CISC में RISC से अधिक रजिस्टर होते हैं। इसके विपरीत, **RISC में जनरल-पर्पज रजिस्टरों की संख्या अधिक होती है** ताकि धीमी मेमोरी (RAM) एक्सेस को कम किया जा सके।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. सीपीयू संगठन और कंट्रोल यूनिट की कार्यप्रणाली",
        "content": """<p>सेंट्रल प्रोसेसिंग यूनिट (CPU) कंप्यूटर सिस्टम का मस्तिष्क है, जो तीन मुख्य घटकों से मिलकर बनता है: कंट्रोल यूनिट (CU), अर्थमेटिक लॉजिक यूनिट (ALU) और रजिस्टर।</p>
        
        <h3>A. सीपीयू के आंतरिक घटक (Internal Components)</h3>
        <ul>
          <li><strong>कंट्रोल यूनिट (CU):</strong> निर्देशों के निष्पादन का समन्वय करती है। यह निर्देशों को डिकोड करती है और सीपीयू तथा अन्य उपकरणों के बीच संकेतों को नियंत्रित करती है।</li>
          <li><strong>अर्थमेटिक लॉजिक यूनिट (ALU):</strong> सभी गणितीय गणनाएं (जोड़, घटाव, गुणा, भाग) और तार्किक तुलनाएं (AND, OR, NOT, छोटा/बड़ा) निष्पादित करती है।</li>
          <li><strong>रजिस्टर (Registers):</strong> प्रोसेसर के अंदर स्थित अत्यधिक तेज़ गति वाले स्टोरेज सेल होते हैं, जो रैम और कैश मेमोरी से भी तेज काम करते हैं।</li>
        </ul>

        <h3>B. फेच-डिकोड-एक्जीक्यूट चक्र (मशीन चक्र)</h3>
        <ol>
          <li><strong>फेच (Fetch):</strong> कंट्रोल यूनिट रैम से उस निर्देश को लाती है जिसका पता प्रोग्राम काउंटर (PC) में होता है और इसे इंस्ट्रक्शन रजिस्टर (IR) में रखती है।</li>
          <li><strong>डिकोड (Decode):</strong> कंट्रोल यूनिट IR में रखे निर्देश का विश्लेषण (डिकोड) करती है कि क्या कार्य किया जाना है।</li>
          <li><strong>एक्जीक्यूट (Execute):</strong> ALU डिकोड किए गए ऑपरेशन को पूरा करता है (जैसे दो संख्याओं को जोड़ना)।</li>
          <li><strong>स्टोर (Store / Write-back):</strong> परिणाम को रजिस्टर या रैम में वापस लिख दिया जाता है।</li>
        </ol>"""
    },
    {
        "title": "2. विशिष्ट प्रयोजन रजिस्टर (Special Purpose Registers)",
        "content": """<p>सीपीयू रजिस्टरों को जनरल-पर्पज (जीपीआर) और स्पेशल-पर्पज रजिस्टरों (एसपीआर) में वर्गीकृत किया जाता है, जिनके पास समर्पित हार्डवेयर कार्य होते हैं।</p>
        
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>रजिस्टर का नाम</th>
                <th>संक्षिप्त नाम</th>
                <th>प्राथमिक कार्य और तकनीकी विवरण</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>प्रोग्राम काउंटर</strong></td>
                <td>PC</td>
                <td>लाए जाने वाले अगले निर्देश का मेमोरी एड्रेस रखता है। निर्देश फेच होने के बाद यह स्वचालित रूप से बढ़ जाता है।</td>
              </tr>
              <tr>
                <td><strong>इंस्ट्रक्शन रजिस्टर</strong></td>
                <td>IR</td>
                <td>वर्तमान में निष्पादित या डिकोड हो रहे निर्देश का बाइनरी कोड रखता है।</td>
              </tr>
              <tr>
                <td><strong>मेमोरी एड्रेस रजिस्टर</strong></td>
                <td>MAR</td>
                <td>उस भौतिक मेमोरी लोकेशन (पते) को रखता है जहाँ से डेटा पढ़ना या लिखना है। यह एड्रेस बस से जुड़ा होता है।</td>
              </tr>
              <tr>
                <td><strong>मेमोरी डेटा / बफ़र रजिस्टर</strong></td>
                <td>MDR / MBR</td>
                <td>मेमोरी से पढ़ा गया या मेमोरी में लिखा जाने वाला वास्तविक डेटा मान रखता है। यह डेटा बस से जुड़ा होता है।</td>
              </tr>
              <tr>
                <td><strong>एक्यूमुलेटर</strong></td>
                <td>AC / ACC</td>
                <td>ALU के गणनाओं के अंतरिम (बीच के) परिणामों को संग्रहीत करता है।</td>
              </tr>
              <tr>
                <td><strong>स्टैक पॉइंटर</strong></td>
                <td>SP</td>
                <td>रैम में स्टैक मेमोरी के सबसे ऊपरी पते (Top address) को दर्शाता है।</td>
              </tr>
              <tr>
                <td><strong>प्रोग्राम स्टेटस वर्ड / फ्लैग्स</strong></td>
                <td>PSW / FR</td>
                <td>ALU के पिछले परिणाम की स्थिति (जैसे कैरी, जीरो, ओवरफ्लो, साइन) दर्शाने वाले बिट्स को रखता है।</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "3. आर्किटेक्चर मॉडल और सिस्टम बसें",
        "content": """<p>कंप्यूटर का प्रदर्शन उसकी मेमोरी संरचना और इंटरकनेक्टिंग बसों पर निर्भर करता है।</p>
        
        <h3>A. वॉन न्यूमैन बनाम हार्वर्ड आर्किटेक्चर</h3>
        <ul>
          <li><strong>वॉन न्यूमैन आर्किटेक्चर:</strong> निर्देश (कोड) और डेटा दोनों के लिए एक ही मेमोरी और एक ही बस का उपयोग करता है। इसे **वॉन न्यूमैन बॉटलनैक (Von Neumann Bottleneck)** कहा जाता है क्योंकि सीपीयू एक ही समय में निर्देश लाने और डेटा पढ़ने/लिखने का कार्य नहीं कर सकता।</li>
          <li><strong>हार्वर्ड आर्किटेक्चर:</strong> निर्देश और डेटा के लिए अलग-अलग भौतिक मेमोरी और बस लाइनों का उपयोग करता है। यह माइक्रो-कंट्रोलर और डीएसपी (DSP) प्रोसेसर में काफी लोकप्रिय है।</li>
        </ul>

        <h3>B. सिस्टम बसें (System Buses)</h3>
        <p>बस तारों का एक समूह है जो कंप्यूटर के घटकों के बीच डेटा और संकेत ले जाता है:</p>
        <ul>
          <li><strong>एड्रेस बस (Address Bus):</strong> सीपीयू से मेमोरी या इनपुट/आउटपुट उपकरणों तक पता ले जाती है। यह **एक-दिशात्मक (Unidirectional)** होती है।</li>
          <li><strong>डेटा बस (Data Bus):</strong> वास्तविक डेटा और निर्देशों को स्थानांतरित करती है। यह **द्वि-दिशात्मक (Bidirectional)** होती है।</li>
          <li><strong>कंट्रोल बस (Control Bus):</strong> टाइमिंग और नियंत्रण संकेत (रीड/राइट निर्देश, इंटरप्ट) ले जाती है। यह **द्वि-दिशात्मक** होती है।</li>
        </ul>

        <h3>C. प्रोसेसर डिजाइन दर्शन: RISC बनाम CISC</h3>
        <ul>
          <li><strong>RISC (रिड्यूस्ड इंस्ट्रक्शन सेट कंप्यूटर):</strong> इसमें निर्देश सरल और एक समान लंबाई के होते हैं। अधिकांश निर्देश **एक क्लॉक साइकिल** में चलते हैं। इसमें रजिस्टरों की संख्या बहुत अधिक होती है। उदाहरण: ARM, RISC-V।</li>
          <li><strong>CISC (कॉम्प्लेक्स इंस्ट्रक्शन सेट कंप्यूटर):</strong> इसमें निर्देश जटिल होते हैं जो एक ही निर्देश में कई कार्य कर सकते हैं। निर्देश अलग-अलग लंबाई के होते हैं और निष्पादन में कई चक्र लेते हैं। इसमें रजिस्टर कम होते हैं। उदाहरण: इंटेल x86।</li>
        </ul>"""
    }
]

# ----------------- PRACTICE QUESTIONS (50 Qs) -----------------
practice_questions = [
    {
        "q": "Which of the following registers inside the CPU holds the address of the next instruction to be fetched from memory?",
        "q_hi": "सीपीयू के भीतर निम्नलिखित में से कौन सा रजिस्टर मेमोरी से लाए जाने वाले अगले निर्देश का पता (address) रखता है?",
        "opts": ["Instruction Register (IR)", "Memory Address Register (MAR)", "Program Counter (PC)", "Accumulator (AC)"],
        "opts_hi": ["इंस्ट्रक्शन रजिस्टर (IR)", "मेमोरी एड्रेस रजिस्टर (MAR)", "प्रोग्राम काउंटर (PC)", "एक्यूमुलेटर (AC)"],
        "ans": 2,
        "sol": "The Program Counter (PC) stores the address of the next instruction to be executed. Once the instruction is fetched, the PC is incremented to point to the next instruction in memory.",
        "sol_hi": "प्रोग्राम काउंटर (PC) उस अगले निर्देश का पता संग्रहीत करता है जिसे निष्पादित किया जाना है। निर्देश लाने के बाद यह बढ़ जाता है।"
    },
    {
        "q": "Which system bus is strictly unidirectional, carrying signals only from the CPU to memory or peripheral interfaces?",
        "q_hi": "कौन सी सिस्टम बस विशुद्ध रूप से एक-दिशात्मक (unidirectional) होती है, जो केवल सीपीयू से मेमोरी या बाहरी उपकरणों तक संकेत ले जाती है?",
        "opts": ["Data Bus", "Address Bus", "Control Bus", "All of the above"],
        "opts_hi": ["डेटा बस", "एड्रेस बस (Address Bus)", "कंट्रोल बस", "उपरोक्त सभी"],
        "ans": 1,
        "sol": "The Address Bus is unidirectional. The CPU generates address values to select specific memory locations or hardware ports, sending these signals outwards. Data and Control buses are bidirectional.",
        "sol_hi": "एड्रेस बस एक-दिशात्मक होती है। सीपीयू मेमोरी एड्रेस उत्पन्न करके बाहर भेजता है। डेटा और कंट्रोल बस द्वि-दिशात्मक होते हैं।"
    },
    {
        "q": "Consider the following statements:\n1. The Instruction Register (IR) holds the instruction currently being executed or decoded.\n2. The Memory Address Register (MAR) holds the actual data value read from memory.\nWhich of the statements given above is/are correct?",
        "q_hi": "निम्नलिखित कथनों पर विचार करें:\n1. इंस्ट्रक्शन रजिस्टर (IR) वर्तमान में निष्पादित या डिकोड हो रहे निर्देश को रखता है।\n2. मेमोरी एड्रेस रजिस्टर (MAR) मेमोरी से पढ़े गए वास्तविक डेटा मान को रखता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1 (1 only)", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect because the MAR holds the address of the memory location, whereas the MDR (Memory Data Register) or MBR (Memory Buffer Register) holds the actual data.",
        "sol_hi": "पहला कथन सही है। दूसरा कथन गलत है क्योंकि MAR मेमोरी का पता रखता है, जबकि वास्तविक डेटा MDR या MBR में संग्रहीत होता है।"
    },
    {
        "q": "What is the phenomenon in Von Neumann architecture where the throughput is limited because the CPU cannot read/write data and fetch instructions at the same time over a shared bus?",
        "q_hi": "वॉन न्यूमैन आर्किटेक्चर में वह कौन सी स्थिति है जहाँ प्रोसेसर की गति सीमित हो जाती है क्योंकि सीपीयू साझा बस पर एक ही समय में डेटा पढ़ने/लिखने और निर्देश लाने का काम नहीं कर सकता?",
        "opts": ["Harvard Restriction", "Von Neumann Bottleneck", "Pipelining Hazard", "Bus Contention Limit"],
        "opts_hi": ["हार्वर्ड प्रतिबंध", "वॉन न्यूमैन बॉटलनैक (Von Neumann Bottleneck)", "पाइपलाइनिंग हैजर्ड", "बस कंटेंशन लिमिट"],
        "ans": 1,
        "sol": "The Von Neumann Bottleneck refers to the performance limitation caused by sharing a single bus and memory space for both instructions and data, preventing simultaneous access.",
        "sol_hi": "वॉन न्यूमैन बॉटलनैक (Von Neumann Bottleneck) निर्देश और डेटा के लिए एक ही बस और मेमोरी साझा करने के कारण होने वाली प्रदर्शन सीमा को संदर्भित करता है।"
    },
    {
        "q": "Which register holds intermediate arithmetic and logical results generated by the ALU before they are transferred to memory?",
        "q_hi": "ALU द्वारा उत्पन्न मध्यवर्ती (intermediate) गणितीय और तार्किक परिणामों को मेमोरी में स्थानांतरित करने से पहले कौन सा रजिस्टर रखता है?",
        "opts": ["Instruction Register", "Program Counter", "Accumulator", "Stack Pointer"],
        "opts_hi": ["इंस्ट्रक्शन रजिस्टर", "प्रोग्राम काउंटर", "एक्यूमुलेटर (Accumulator)", "स्टैक पॉइंटर"],
        "ans": 2,
        "sol": "The Accumulator (AC) is a register in which intermediate arithmetic and logic results are stored. It acts as a temporary working space for the ALU.",
        "sol_hi": "एक्यूमुलेटर (AC) एक रजिस्टर है जिसमें मध्यवर्ती अंकगणितीय और तार्किक परिणाम संग्रहीत किए जाते हैं। यह ALU के लिए अस्थायी बफ़र है।"
    },
    {
        "q": "Which design philosophy utilizes simple instructions of fixed length that execute in a single clock cycle, relying heavily on software/compiler optimization?",
        "q_hi": "कौन सा डिज़ाइन दर्शन निश्चित लंबाई के सरल निर्देशों का उपयोग करता है जो एक ही क्लॉक साइकिल में चलते हैं, और सॉफ्टवेयर/कंपाइलर अनुकूलन पर अत्यधिक निर्भर करते हैं?",
        "opts": ["CISC", "RISC", "VLIW", "SIMD"],
        "opts_hi": ["CISC", "RISC (RISC)", "VLIW", "SIMD"],
        "ans": 1,
        "sol": "RISC (Reduced Instruction Set Computer) focuses on simple instructions, single-cycle execution, pipelining, and a large number of registers. CISC focuses on complex multi-cycle instructions.",
        "sol_hi": "RISC (रिड्यूस्ड इंस्ट्रक्शन सेट कंप्यूटर) सरल निर्देशों और एक-चक्र निष्पादन पर केंद्रित है। इसके विपरीत CISC जटिल बहु-चक्र निर्देशों पर ध्यान देता है।"
    },
    {
        "q": "Which special CPU register contains individual 1-bit status flags (such as Carry, Zero, Sign, Overflow) reflecting the outcome of the most recent ALU operation?",
        "q_hi": "किस विशेष सीपीयू रजिस्टर में अलग-अलग 1-बिट स्थिति फ़्लैग (जैसे कैरी, ज़ीरो, साइन, ओवरफ़्लो) होते हैं जो सबसे हालिया ALU ऑपरेशन के परिणाम को दर्शाते हैं?",
        "opts": ["Instruction Register", "Program Status Word / Flag Register", "Stack Pointer", "Memory Buffer Register"],
        "opts_hi": ["इंस्ट्रक्शन रजिस्टर", "प्रोग्राम स्टेटस वर्ड / फ़्लैग रजिस्टर (Flag Register)", "स्टैक पॉइंटर", "मेमोरी बफ़र रजिस्टर"],
        "ans": 1,
        "sol": "The Flag Register (or Program Status Word - PSW) holds status bits that indicate results of calculations, such as whether the result was zero, negative, or caused a carry.",
        "sol_hi": "फ़्लैग रजिस्टर या प्रोग्राम स्टेटस वर्ड (PSW) अंतिम गणना की स्थिति (जैसे शून्य, ऋणात्मक या कैरी परिणाम) दर्शाने वाले बिट्स रखता है।"
    },
    {
        "q": "The width of the Address Bus determines which of the following features of a computer system?",
        "q_hi": "एड्रेस बस की चौड़ाई (width) कंप्यूटर सिस्टम की निम्नलिखित में से किस विशेषता को निर्धारित करती है?",
        "opts": [
            "The data transfer speed in bits per second",
            "The maximum addressable memory capacity of the CPU",
            "The word size of the CPU registers",
            "The clock frequency of the processor"
        ],
        "opts_hi": [
            "डेटा ट्रांसफर की गति बिट प्रति सेकंड में",
            "सीपीयू की अधिकतम एड्रेस करने योग्य मेमोरी क्षमता (Max Memory Capacity)",
            "सीपीयू रजिस्टरों का वर्ड आकार (Word size)",
            "प्रोसेसर की क्लॉक फ़्रीक्वेंसी"
        ],
        "ans": 1,
        "sol": "The width of the address bus determines how many unique memory locations the CPU can address. For a bus width of N bits, the CPU can address $2^N$ memory locations.",
        "sol_hi": "एड्रेस बस की चौड़ाई यह तय करती है कि सीपीयू कितने मेमोरी लोकेशनों को एड्रेस कर सकता है। N-बिट चौड़ाई होने पर अधिकतम $2^N$ पते संभव हैं।"
    },
    {
        "q": "Which CPU register points to the memory address of the last data item pushed onto the stack in RAM?",
        "q_hi": "रैम में स्टैक मेमोरी में पुश किए गए अंतिम डेटा आइटम के मेमोरी एड्रेस को कौन सा सीपीयू रजिस्टर दर्शाता है?",
        "opts": ["Program Counter", "Stack Pointer", "Accumulator", "Memory Data Register"],
        "opts_hi": ["प्रोग्राम काउंटर", "स्टैक पॉइंटर (Stack Pointer)", "एक्यूमुलेटर", "मेमोरी डेटा रजिस्टर"],
        "ans": 1,
        "sol": "The Stack Pointer (SP) is a register that stores the memory address of the top of the stack. It changes as items are pushed or popped from the stack.",
        "sol_hi": "स्टैक पॉइंटर (SP) रैम में स्टैक के शीर्ष (Top of the Stack) का मेमोरी पता संग्रहीत रखता है।"
    },
    {
        "q": "What architecture uses physically separate memory units and separate bus lines for instruction codes and data, allowing simultaneous access?",
        "q_hi": "कौन सा आर्किटेक्चर निर्देश कोड और डेटा के लिए भौतिक रूप से अलग-अलग मेमोरी यूनिट और अलग-अलग बस लाइनों का उपयोग करता है, जिससे एक साथ एक्सेस संभव होता है?",
        "opts": ["Von Neumann Architecture", "Harvard Architecture", "Systolic Array Architecture", "None of the above"],
        "opts_hi": ["वॉन न्यूमैन आर्किटेक्चर", "हार्वर्ड आर्किटेक्चर (Harvard Architecture)", "सिस्टोलिक ऐरे आर्किटेक्चर", "उपरोक्त में से कोई नहीं"],
        "ans": 1,
        "sol": "Harvard Architecture uses separate memory blocks and buses for instructions and data, allowing the CPU to fetch an instruction and read/write data at the same time.",
        "sol_hi": "हार्वर्ड आर्किटेक्चर में कोड (निर्देश) और डेटा के लिए अलग-अलग मेमोरी स्पेस और बस होते हैं, जिससे समानांतर डेटा और कोड एक्सेस मिलता है।"
    },
    {
        "q": "Which of the following processor families is based on the CISC architecture?",
        "q_hi": "निम्नलिखित में से कौन सा प्रोसेसर परिवार CISC आर्किटेक्चर पर आधारित है?",
        "opts": ["Intel x86", "ARM", "MIPS", "RISC-V"],
        "opts_hi": ["इंटेल x86 (Intel x86)", "ARM", "MIPS", "RISC-V"],
        "ans": 0,
        "sol": "Intel's x86 series (used in PCs and laptops) is a classic example of CISC. ARM, MIPS, and RISC-V are architectures based on RISC.",
        "sol_hi": "इंटेल x86 (डेस्कटॉप और लैपटॉप में प्रयुक्त) CISC वास्तुकला का सबसे प्रसिद्ध उदाहरण है। ARM, MIPS और RISC-V सभी RISC आधारित हैं।"
    },
    {
        "q": "The internal clock speed of a microprocessor is measured in which of the following units?",
        "q_hi": "माइक्रोप्रोसेसर की आंतरिक क्लॉक स्पीड (clock speed) निम्नलिखित में से किस इकाई में मापी जाती है?",
        "opts": ["Megabytes (MB)", "Gigahertz (GHz)", "Bits per second (bps)", "DPI"],
        "opts_hi": ["मेगाबाइट (MB)", "गीगाहर्ट्ज़ (GHz)", "बिट प्रति सेकंड (bps)", "DPI"],
        "ans": 1,
        "sol": "Processor clock speed is measured in Gigahertz (GHz) or Megahertz (MHz), representing billions or millions of electrical cycles per second.",
        "sol_hi": "प्रोसेसर की क्लॉक स्पीड (घड़ी की गति) गीगाहर्ट्ज़ (GHz) में मापी जाती है, जो प्रति सेकंड विद्युत पल्स चक्रों की संख्या है।"
    },
    {
        "q": "Match the following CPU components with their descriptions:\n1. CU - A. Executes calculations and logical comparisons\n2. ALU - B. High-speed internal processor storage cells\n3. Registers - C. Decodes instructions and directs execution signals\nSelect the correct code:",
        "q_hi": "निम्नलिखित सीपीयू घटकों का उनके विवरणों के साथ मिलान करें:\n1. CU - A. गणना और तार्किक तुलना निष्पादित करता है\n2. ALU - B. उच्च गति वाले आंतरिक प्रोसेसर स्टोरेज सेल\n3. Registers - C. निर्देशों को डिकोड करता है और नियंत्रण संकेत भेजता है\nसही कोड चुनें:",
        "opts": [
            "1-C, 2-A, 3-B",
            "1-A, 2-C, 3-B",
            "1-C, 2-B, 3-A",
            "1-B, 2-A, 3-C"
        ],
        "opts_hi": [
            "1-C, 2-A, 3-B",
            "1-A, 2-C, 3-B",
            "1-C, 2-B, 3-A",
            "1-B, 2-A, 3-C"
        ],
        "ans": 0,
        "sol": "CU decodes instructions (1-C), ALU executes calculations (2-A), and Registers are internal processor storage cells (3-B).",
        "sol_hi": "कंट्रोल यूनिट निर्देशों को डिकोड करती है (1-C), ALU गणना करता है (2-A), और रजिस्टर आंतरिक स्टोरेज सेल हैं (3-B)।"
    },
    {
        "q": "During which phase of the machine cycle does the Control Unit interpret the binary instruction to determine what operation to perform?",
        "q_hi": "मशीन चक्र के किस चरण के दौरान कंट्रोल यूनिट बाइनरी निर्देश की व्याख्या (interpret) करती है ताकि यह निर्धारित किया जा सके कि कौन सा ऑपरेशन किया जाना है?",
        "opts": ["Fetch", "Decode", "Execute", "Write-back"],
        "opts_hi": ["फेच (Fetch)", "डिकोड (Decode)", "एक्जीक्यूट (Execute)", "राइट-बैक"],
        "ans": 1,
        "sol": "During the Decode phase, the instruction inside the Instruction Register (IR) is interpreted by the CU decoder circuitry to determine the operands and operation.",
        "sol_hi": "डिकोड (Decode) चरण के दौरान, इंस्ट्रक्शन रजिस्टर (IR) में मौजूद निर्देश का अर्थ निकाला जाता है ताकि नियंत्रण संकेत भेजे जा सकें।"
    },
    {
        "q": "Which system bus carries memory write and read enable commands, clock pulses, and interrupt request signals?",
        "q_hi": "कौन सी सिस्टम बस मेमोरी राइट/रीड कमांड, क्लॉक पल्स और इंटरप्ट रिक्वेस्ट सिग्नल ले जाती है?",
        "opts": ["Address Bus", "Data Bus", "Control Bus", "I/O Bus"],
        "opts_hi": ["एड्रेस बस", "डेटा बस", "कंट्रोल बस (Control Bus)", "I/O बस"],
        "ans": 2,
        "sol": "The Control Bus carries synchronization, status, and control signals (like read/write lines, clock pulses, and interrupts) to manage overall system components.",
        "sol_hi": "कंट्रोल बस (Control Bus) सिस्टम के विभिन्न अंगों के तालमेल के लिए नियंत्रण संकेत जैसे रीड, राइट, क्लॉक पल्स और इंटरप्ट ले जाती है।"
    },
    {
        "q": "What CPU register is directly connected to the Address Bus to specify the physical location of memory to be read or written?",
        "q_hi": "मेमोरी से डेटा पढ़ने या लिखने के लिए उसकी भौतिक जगह (लोकेशन) को दर्शाने के लिए कौन सा सीपीयू रजिस्टर सीधे एड्रेस बस से जुड़ा होता है?",
        "opts": ["Memory Address Register (MAR)", "Memory Data Register (MDR)", "Instruction Register (IR)", "Accumulator (AC)"],
        "opts_hi": ["मेमोरी एड्रेस रजिस्टर (MAR)", "मेमोरी डेटा रजिस्टर (MDR)", "इंस्ट्रक्शन रजिस्टर (IR)", "एक्यूमुलेटर (AC)"],
        "ans": 0,
        "sol": "The Memory Address Register (MAR) is connected directly to the Address Bus. It holds the address of the memory location currently being accessed.",
        "sol_hi": "मेमोरी एड्रेस रजिस्टर (MAR) सीधे एड्रेस बस से जुड़ा होता है और लक्षित मेमोरी सेल का पता रखता है।"
    },
    {
        "q": "Which register holds the actual data value fetched from memory or the data value about to be written into a memory location?",
        "q_hi": "कौन सा रजिस्टर मेमोरी से लाए गए वास्तविक डेटा मान को, या मेमोरी में लिखे जाने वाले डेटा मान को संग्रहीत करता है?",
        "opts": ["Memory Address Register (MAR)", "Memory Data Register (MDR)", "Program Counter (PC)", "Stack Pointer (SP)"],
        "opts_hi": ["मेमोरी एड्रेस रजिस्टर (MAR)", "मेमोरी डेटा रजिस्टर (MDR)", "प्रोग्राम काउंटर (PC)", "स्टैक पॉइंटर (SP)"],
        "ans": 1,
        "sol": "The Memory Data Register (MDR), also known as the Memory Buffer Register (MBR), acts as a buffer holding data retrieved from RAM or data waiting to be written to RAM.",
        "sol_hi": "मेमोरी डेटा रजिस्टर (MDR) या मेमोरी बफ़र रजिस्टर (MBR) उस डेटा को रखता है जो मेमोरी से पढ़ा गया है या जिसे मेमोरी में लिखा जाना है।"
    },
    {
        "q": "The concept of 'Pipelining' in CPU design allows which of the following operations?",
        "q_hi": "सीपीयू डिज़ाइन में 'पाइपलाइनिंग' (Pipelining) की अवधारणा निम्नलिखित में से किस ऑपरेशन की अनुमति देती है?",
        "opts": [
            "Accessing data and code from the same bus simultaneously",
            "Executing multiple steps of different instructions in parallel",
            "Storing variables in registers instead of cache memory",
            "Eliminating clock cycles completely"
        ],
        "opts_hi": [
            "एक ही समय में एक ही बस से डेटा और कोड प्राप्त करना",
            "विभिन्न निर्देशों के कई चरणों को समानांतर में निष्पादित करना (Pipelining)",
            "कैश मेमोरी के बजाय रजिस्टरों में वेरिएबल स्टोर करना",
            "क्लॉक साइकिल को पूरी तरह से समाप्त करना"
        ],
        "ans": 1,
        "sol": "Pipelining is a technique where multiple instructions are overlapped in execution. While one instruction is being executed, the next is decoded, and the one after that is fetched.",
        "sol_hi": "पाइपलाइनिंग (Pipelining) वह तकनीक है जहाँ प्रोसेसर एक साथ कई निर्देशों के अलग-अलग चरणों (जैसे फेच, डिकोड, एक्जीक्यूट) को ओवरलैप करके काम करता है।"
    },
    {
        "q": "How many bits are in a 64-bit CPU register?",
        "q_hi": "एक 64-बिट सीपीयू रजिस्टर में कितने बिट्स होते हैं?",
        "opts": ["8 bits", "32 bits", "64 bits", "128 bits"],
        "opts_hi": ["8 बिट्स", "32 बिट्स", "64 बिट्स (64 bits)", "128 बिट्स"],
        "ans": 2,
        "sol": "A 64-bit CPU has registers that are 64 bits wide, which allows it to handle data values up to $2^{64}-1$ and address huge amounts of physical memory.",
        "sol_hi": "एक 64-बिट रजिस्टर 64 बाइनरी बिट्स (0 या 1) की चौड़ाई रखता है, जो एक बार में बड़े मानों को प्रोसेस कर सकता है।"
    },
    {
        "q": "Consider the following statements regarding RISC and CISC:\n1. RISC architecture uses variable-length instructions, making decoder design complex.\n2. CISC architecture focuses on minimizing instruction count per program, using complex instructions at the hardware level.\nWhich of the statements given above is/are correct?",
        "q_hi": "RISC और CISC के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. RISC आर्किटेक्चर परिवर्तनशील-लंबाई (variable) के निर्देशों का उपयोग करता है, जिससे डिकोडर जटिल हो जाता है।\n2. CISC आर्किटेक्चर प्रत्येक प्रोग्राम में निर्देशों की संख्या को न्यूनतम करने पर ध्यान केंद्रित करता है, हार्डवेयर स्तर पर जटिल निर्देशों का उपयोग करके।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2 (2 only)", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect because RISC uses fixed-length instructions (e.g. 32-bit) which makes decoding extremely simple. Statement 2 is correct; CISC focuses on complex instructions to do more work per instruction line.",
        "sol_hi": "पहला कथन गलत है क्योंकि RISC निश्चित लंबाई के निर्देशों का उपयोग करता है जिससे डिकोडिंग सरल होती है। दूसरा कथन सही है क्योंकि CISC हार्डवेयर स्तर पर निर्देश पंक्तियों को घटाने के लिए जटिल कार्य करता है।"
    },
    {
        "q": "Which register holds the output of the most recent ALU computation, serving as an accumulator?",
        "q_hi": "कौन सा रजिस्टर सबसे हालिया ALU गणना के आउटपुट को संग्रहीत करता है, एक एक्यूमुलेटर के रूप में कार्य करते हुए?",
        "opts": ["Program Counter", "Accumulator", "Instruction Register", "Stack Pointer"],
        "opts_hi": ["प्रोग्राम काउंटर", "एक्यूमुलेटर (Accumulator)", "इंस्ट्रक्शन रजिस्टर", "स्टैक पॉइंटर"],
        "ans": 1,
        "sol": "The Accumulator (ACC) acts as the register holding immediate results from the Arithmetic Logic Unit.",
        "sol_hi": "एक्यूमुलेटर (Accumulator) वह रजिस्टर है जो ALU के जोड़, घटाव आदि गणनाओं के तुरंत बाद मिलने वाले मान को अपने पास रखता है।"
    },
    {
        "q": "What name is given to the set of lines linking the CPU to the RAM/ROM memory, carrying addressing signals?",
        "q_hi": "सीपीयू को रैम/रोम मेमोरी से जोड़ने वाली और पते (addressing signals) ले जाने वाली लाइनों के समूह को क्या नाम दिया गया है?",
        "opts": ["Data Bus", "Address Bus", "Control Bus", "PCI Bus"],
        "opts_hi": ["डेटा बस", "एड्रेस बस (Address Bus)", "कंट्रोल बस", "PCI बस"],
        "ans": 1,
        "sol": "The Address Bus carries addresses generated by the CPU to point to locations in system memory.",
        "sol_hi": "एड्रेस बस (Address Bus) उन तारों का समूह है जो मेमोरी चिप के किस खास सेल से डेटा उठाना है, उसका पता ले जाती हैं।"
    },
    {
        "q": "Which of the following is NOT a flag bit commonly found in a CPU Status Register (Flag Register)?",
        "q_hi": "निम्नलिखित में से कौन सा फ्लैग बिट आमतौर पर सीपीयू स्टेटस रजिस्टर (फ़्लैग रजिस्टर) में नहीं पाया जाता है?",
        "opts": ["Zero Flag", "Carry Flag", "Overflow Flag", "Interrupt Count Flag"],
        "opts_hi": ["ज़ीरो फ़्लैग", "कैरी फ़्लैग", "ओवरफ़्लो फ़्लैग", "इंटरप्ट काउंट फ़्लैग (Interrupt Count Flag)"],
        "ans": 3,
        "sol": "Zero Flag (ZF), Carry Flag (CF), and Overflow Flag (OF) are standard flags reflecting ALU results. Interrupt Count Flag is not a standard status register flag.",
        "sol_hi": "ज़ीरो, कैरी और ओवरफ़्लो फ़्लैग मानक स्टेटस बिट्स हैं। इंटरप्ट काउंट फ़्लैग जैसा कोई स्टेटस फ़्लैग नहीं होता।"
    },
    {
        "q": "Which architectural layout has instructions and data residing in different memory chips and accessed through different physical buses?",
        "q_hi": "किस आर्किटेक्चरल लेआउट में निर्देश और डेटा अलग-अलग मेमोरी चिप्स में होते हैं और उन्हें अलग-अलग भौतिक बसों के माध्यम से एक्सेस किया जाता है?",
        "opts": ["Harvard Architecture", "Von Neumann Architecture", "Shared Bus Design", "None of the above"],
        "opts_hi": ["हार्वर्ड आर्किटेक्चर (Harvard Architecture)", "वॉन न्यूमैन आर्किटेक्चर", "साझा बस डिजाइन", "उपरोक्त में से कोई नहीं"],
        "ans": 0,
        "sol": "Harvard Architecture separates data memory from instruction memory, avoiding bus contention.",
        "sol_hi": "हार्वर्ड आर्किटेक्चर निर्देश मेमोरी और डेटा मेमोरी को अलग-अलग रखकर बस संघर्ष (contention) को समाप्त करता है।"
    },
    {
        "q": "The instruction cycle stages occur in which chronological order?",
        "q_hi": "निर्देश चक्र (Instruction cycle) के चरण किस कालानुक्रमिक क्रम में होते हैं?",
        "opts": [
            "Decode, Fetch, Execute, Store",
            "Fetch, Decode, Execute, Store",
            "Fetch, Execute, Decode, Store",
            "Decode, Execute, Fetch, Store"
        ],
        "opts_hi": [
            "डिकोड, फेच, एक्जीक्यूट, स्टोर",
            "फेच, डिकोड, एक्जीक्यूट, स्टोर (Fetch, Decode, Execute, Store)",
            "फेच, एक्जीक्यूट, डिकोड, स्टोर",
            "डिकोड, एक्जीक्यूट, फेच, स्टोर"
        ],
        "ans": 1,
        "sol": "The proper sequence is Fetch (retrieve instruction), Decode (interpret it), Execute (perform action), and Store (save result).",
        "sol_hi": "सही क्रम है: फेच (लाना), डिकोड (व्याख्या), एक्जीक्यूट (निष्पादित करना) और स्टोर (सुरक्षित करना)।"
    },
    {
        "q": "A processor with a 32-bit address bus can theoretically address how many unique bytes of physical memory?",
        "q_hi": "32-बिट एड्रेस बस वाला प्रोसेसर सैद्धांतिक रूप से भौतिक मेमोरी के कितने अद्वितीय बाइट्स को एड्रेस कर सकता है?",
        "opts": ["32 Megabytes", "4 Gigabytes", "64 Gigabytes", "16 Terabytes"],
        "opts_hi": ["32 मेगाबाइट", "4 गीगाबाइट (4 GB)", "64 गीगाबाइट", "16 टेराबाइट"],
        "ans": 1,
        "sol": "A 32-bit address bus allows addressing $2^{32}$ bytes = 4,294,967,296 bytes = 4 Gigabytes (GB) of RAM.",
        "sol_hi": "$2^{32}$ बाइट्स लगभग 4 बिलियन बाइट्स के बराबर होते हैं, जो ठीक 4 Gigabytes (GB) मेमोरी क्षमता है।"
    },
    {
        "q": "Which of the following is a general-purpose register family widely used in modern smartphone microprocessors?",
        "q_hi": "निम्नलिखित में से कौन सा आधुनिक स्मार्टफोन माइक्रोप्रोसेसरों में व्यापक रूप से उपयोग किया जाने वाला जनरल-पर्पज रजिस्टर परिवार है?",
        "opts": ["Intel x86 registers", "ARM Registers", "DEC PDP registers", "Z80 registers"],
        "opts_hi": ["इंटेल x86 रजिस्टर", "ARM रजिस्टर (ARM Registers)", "DEC PDP रजिस्टर", "Z80 रजिस्टर"],
        "ans": 1,
        "sol": "ARM processors (based on RISC) power almost all modern smartphones and utilize a large set of general-purpose registers.",
        "sol_hi": "स्मार्टफोन में मुख्य रूप से ARM आर्किटेक्चर वाले प्रोसेसर होते हैं, जिनमें ARM जनरल-पर्पज रजिस्टरों का उपयोग किया जाता है।"
    },
    {
        "q": "Which register holds the current instruction that is being decoded by the Control Unit?",
        "q_hi": "कौन सा रजिस्टर वर्तमान निर्देश को संग्रहीत करता है जो कंट्रोल यूनिट द्वारा डिकोड किया जा रहा है?",
        "opts": ["Instruction Register (IR)", "Program Counter (PC)", "Memory Address Register (MAR)", "Accumulator (AC)"],
        "opts_hi": ["इंस्ट्रक्शन रजिस्टर (IR)", "प्रोग्राम काउंटर (PC)", "मेमोरी एड्रेस रजिस्टर (MAR)", "एक्यूमुलेटर (AC)"],
        "ans": 0,
        "sol": "The Instruction Register (IR) holds the binary code of the instruction currently being executed or decoded.",
        "sol_hi": "डिकोड होने वाला वर्तमान निर्देश इंस्ट्रक्शन रजिस्टर (IR) में होता है।"
    },
    {
        "q": "Which CPU register's contents are loaded into the Address Bus at the beginning of the Fetch phase?",
        "q_hi": "फेच चरण (Fetch phase) के प्रारंभ में किस सीपीयू रजिस्टर की सामग्री को एड्रेस बस में लोड किया जाता है?",
        "opts": ["Instruction Register", "Program Counter", "Accumulator", "Flag Register"],
        "opts_hi": ["इंस्ट्रक्शन रजिस्टर", "प्रोग्राम काउंटर (Program Counter)", "एक्यूमुलेटर", "फ्लैग रजिस्टर"],
        "ans": 1,
        "sol": "At the start of Fetch, the CPU copies the address inside the Program Counter (PC) to the Memory Address Register (MAR), which then drives the Address Bus.",
        "sol_hi": "फेच चरण की शुरुआत में प्रोग्राम काउंटर (PC) का पता ही एड्रेस बस पर भेजा जाता है ताकि संबंधित निर्देश को लाया जा सके।"
    },
    {
        "q": "Consider the following statements:\n1. The Control Bus is unidirectional.\n2. The Data Bus is bidirectional.\nWhich of the statements given above is/are correct?",
        "q_hi": "निम्नलिखित कथनों पर विचार करें:\n1. कंट्रोल बस एक-दिशात्मक (unidirectional) होती है।\n2. डेटा बस द्वि-दिशात्मक (bidirectional) होती है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2 (2 only)", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect because the Control Bus is bidirectional (transmitting read/write enable signals, clocks, and interrupt signals to and from devices). Statement 2 is correct.",
        "sol_hi": "कंट्रोल बस द्वि-दिशात्मक होती है क्योंकि यह प्रोसेसर और रैम के बीच तालमेल संकेत दोनों तरफ भेजती है। डेटा बस भी द्वि-दिशात्मक है।"
    },
    {
        "q": "What is the primary function of the Arithmetic Logic Unit (ALU)?",
        "q_hi": "अर्थमेटिक लॉजिक यूनिट (ALU) का प्राथमिक कार्य क्या है?",
        "opts": [
            "To decode instruction codes",
            "To perform mathematical operations and logic comparisons",
            "To store data long-term",
            "To coordinate keyboard inputs"
        ],
        "opts_hi": [
            "निर्देश कोड को डिकोड करना",
            "गणितीय संचालन और तार्किक तुलना निष्पादित करना (ALU functions)",
            "डेटा को लंबे समय तक संग्रहीत करना",
            "कीबोर्ड इनपुट का समन्वय करना"
        ],
        "ans": 1,
        "sol": "The ALU performs all calculations (addition, subtraction, logic operations like AND/OR) inside the processor core.",
        "sol_hi": "ALU का कार्य गणितीय गणनाएं और तुलनात्मक तार्किक निर्णय लेना है।"
    },
    {
        "q": "Which register is updated when the CPU executes a 'Push' stack operation in assembly language?",
        "q_hi": "असेंबली भाषा में जब सीपीयू 'Push' स्टैक ऑपरेशन निष्पादित करता है तो कौन सा रजिस्टर अपडेट होता है?",
        "opts": ["Stack Pointer (SP)", "Program Counter (PC)", "Instruction Register (IR)", "Accumulator (AC)"],
        "opts_hi": ["स्टैक पॉइंटर (SP)", "प्रोग्राम काउंटर (PC)", "इंस्ट्रक्शन रजिस्टर (IR)", "एक्यूमुलेटर (AC)"],
        "ans": 0,
        "sol": "Push and Pop instructions alter the address value inside the Stack Pointer (SP) register as data is added or removed from the stack.",
        "sol_hi": "पुश (Push) ऑपरेशन करने पर डेटा स्टैक में जमा होता है और स्टैक पॉइंटर (SP) अपडेट हो जाता है।"
    },
    {
        "q": "A processor with a 64-bit data bus can transfer how many bytes of data per bus cycle?",
        "q_hi": "64-बिट डेटा बस वाला प्रोसेसर प्रति बस चक्र में कितने बाइट्स डेटा स्थानांतरित कर सकता है?",
        "opts": ["4 bytes", "8 bytes", "16 bytes", "64 bytes"],
        "opts_hi": ["4 बाइट्स", "8 बाइट्स (8 bytes)", "16 बाइट्स", "64 बाइट्स"],
        "ans": 1,
        "sol": "A 64-bit bus can transmit 64 bits of data simultaneously. Since 8 bits = 1 byte, 64 bits = 8 bytes of data.",
        "sol_hi": "64 बिट = 8 बाइट (क्योंकि 1 बाइट में 8 बिट्स होते हैं)। अतः प्रति चक्र 8 बाइट डेटा भेजा जा सकता है।"
    },
    {
        "q": "Which architecture is optimized for execution speed through the use of pipelined simple instructions, avoiding complex hardware decode logic?",
        "q_hi": "जटिल हार्डवेयर डिकोड लॉजिक से बचते हुए, पाइपलाइनयुक्त सरल निर्देशों के माध्यम से निष्पादन गति को कौन सा आर्किटेक्चर अनुकूलित करता है?",
        "opts": ["RISC", "CISC", "VON NEUMANN", "MISD"],
        "opts_hi": ["RISC (RISC)", "CISC", "VON NEUMANN", "MISD"],
        "ans": 0,
        "sol": "RISC (Reduced Instruction Set Computer) optimizes execution cycles by executing simple instructions of uniform size using pipelines.",
        "sol_hi": "RISC आर्किटेक्चर कम और सरल निर्देशों का उपयोग करता है जो पाइपलाइन में तेजी से चलते हैं।"
    },
    {
        "q": "What register is used to store the binary instruction currently fetched from memory while it is decoded?",
        "q_hi": "मेमोरी से लाए गए बाइनरी निर्देश को डिकोड करते समय किस रजिस्टर में संग्रहीत किया जाता है?",
        "opts": ["Program Counter", "Instruction Register", "Memory Address Register", "Memory Data Register"],
        "opts_hi": ["प्रोग्राम काउंटर", "इंस्ट्रक्शन रजिस्टर (Instruction Register)", "मेमोरी एड्रेस रजिस्टर", "मेमोरी डेटा रजिस्टर"],
        "ans": 1,
        "sol": "The Instruction Register (IR) stores the instruction code fetched from RAM while the Control Unit decodes it.",
        "sol_hi": "लाए गए निर्देश को डिकोड होने तक इंस्ट्रक्शन रजिस्टर (IR) में संग्रहीत रखा जाता है।"
    },
    {
        "q": "Which register holds the memory address of the operand currently being read from RAM?",
        "q_hi": "रैम (RAM) से पढ़े जा रहे ऑपरेंड के मेमोरी एड्रेस को कौन सा रजिस्टर रखता है?",
        "opts": ["Memory Address Register", "Memory Data Register", "Instruction Register", "Program Counter"],
        "opts_hi": ["मेमोरी एड्रेस रजिस्टर (MAR)", "मेमोरी डेटा रजिस्टर", "इंस्ट्रक्शन रजिस्टर", "प्रोग्राम काउंटर"],
        "ans": 0,
        "sol": "The Memory Address Register (MAR) holds the address of the operand or instruction being accessed in memory.",
        "sol_hi": "मेमोरी एड्रेस रजिस्टर (MAR) लक्षित ऑपरेंड के एड्रेस (पते) को स्टोर करता है।"
    },
    {
        "q": "The Von Neumann bottleneck occurs due to which of the following reasons?",
        "q_hi": "वॉन न्यूमैन बॉटलनैक निम्नलिखित में से किस कारण से होता है?",
        "opts": [
            "Having too many registers inside the CPU core",
            "Sharing a single memory bus for both instructions and data",
            "Using physically separate cache levels",
            "Excessive clock speeds leading to thermal throttling"
        ],
        "opts_hi": [
            "सीपीयू कोर के भीतर बहुत अधिक रजिस्टर होना",
            "निर्देशों और डेटा दोनों के लिए एक ही मेमोरी बस साझा करना (Shared Bus)",
            "अलग-अलग भौतिक कैश स्तरों का उपयोग करना",
            "अत्यधिक क्लॉक स्पीड के कारण थर्मल थ्रॉटलिंग"
        ],
        "ans": 1,
        "sol": "Because the same physical bus carries instructions and data, the CPU must wait for memory operations to complete, creating a bottleneck.",
        "sol_hi": "चूँकि एक ही बस डेटा और निर्देश दोनों लाती है, इसलिए दोनों कार्यों को एक साथ नहीं किया जा सकता, जिससे डेटा ट्रांसफर में देरी होती है।"
    },
    {
        "q": "Which of the following describes the function of the Accumulator register?",
        "q_hi": "निम्नलिखित में से कौन सा एक्यूमुलेटर (Accumulator) रजिस्टर के कार्य का वर्णन करता है?",
        "opts": [
            "Points to the next instruction in RAM",
            "Holds the intermediate outcomes of ALU computations",
            "Decodes macro-operation signals",
            "Drives the system clock rate"
        ],
        "opts_hi": [
            "रैम में अगले निर्देश को इंगित करता है",
            "ALU गणनाओं के मध्यवर्ती परिणामों को रखता है (Holds ALU intermediate outcomes)",
            "मैक्रो-ऑपरेशन सिग्नलों को डिकोड करता है",
            "सिस्टम क्लॉक रेट को संचालित करता है"
        ],
        "ans": 1,
        "sol": "The Accumulator (AC) is a register where intermediate calculations of the ALU are temporarily stored.",
        "sol_hi": "ALU के परिणामों को रैम में भेजने से पहले एक्यूमुलेटर रजिस्टर में अस्थायी रूप से रखा जाता है।"
    },
    {
        "q": "How does the Program Counter (PC) advance to the next instruction in normal sequential execution?",
        "q_hi": "सामान्य अनुक्रमिक निष्पादन (sequential execution) में प्रोग्राम काउंटर (PC) अगले निर्देश पर कैसे आगे बढ़ता है?",
        "opts": [
            "It is manually reset by the user",
            "It is automatically incremented by the control unit",
            "It is cleared to zero after every cycle",
            "It queries the accumulator for the next address"
        ],
        "opts_hi": [
            "यह उपयोगकर्ता द्वारा मैन्युअल रूप से रीसेट किया जाता है",
            "यह कंट्रोल यूनिट द्वारा स्वचालित रूप से बढ़ा दिया जाता है (Auto-increment)",
            "यह प्रत्येक चक्र के बाद शून्य हो जाता है",
            "यह अगले पते के लिए एक्यूमुलेटर से पूछता है"
        ],
        "ans": 1,
        "sol": "During or after the fetch phase, the Program Counter (PC) is automatically incremented by the size of the fetched instruction to point to the next instruction.",
        "sol_hi": "फेच चरण के दौरान प्रोग्राम काउंटर का मान स्वचालित रूप से बढ़ जाता है ताकि वह अगले निर्देश का पता रख सके।"
    },
    {
        "q": "Which bus transmits synchronization timing pulses generated by the system clock?",
        "q_hi": "कौन सी बस सिस्टम क्लॉक द्वारा उत्पन्न सिंक्रोनाइज़ेशन टाइमिंग पल्स को संचालित करती है?",
        "opts": ["Data Bus", "Address Bus", "Control Bus", "PCI Bus"],
        "opts_hi": ["डेटा बस", "एड्रेस बस", "कंट्रोल बस (Control Bus)", "PCI बस"],
        "ans": 2,
        "sol": "Clock pulses, read/write strobes, and synchronization timing are part of the Control Bus lines.",
        "sol_hi": "सिस्टम घड़ी के टाइमिंग संकेत और तालमेल पल्स कंट्रोल बस का हिस्सा होते हैं।"
    },
    {
        "q": "What register is used by the CPU to save state flags indicating arithmetic sign, carry, overflow, and zero conditions?",
        "q_hi": "सीपीयू द्वारा गणितीय चिह्न, कैरी, ओवरफ़्लो और शून्य स्थितियों को दर्शाने वाले स्टेट फ़्लैग को सहेजने के लिए किस रजिस्टर का उपयोग किया जाता है?",
        "opts": ["Stack Pointer", "Instruction Register", "Flag Register / Program Status Word", "Memory Address Register"],
        "opts_hi": ["स्टैक पॉइंटर", "इंस्ट्रक्शन रजिस्टर", "फ्लैग रजिस्टर / प्रोग्राम स्टेटस वर्ड (Flag Register)", "मेमोरी एड्रेस रजिस्टर"],
        "ans": 2,
        "sol": "The Flag Register (PSW) holds the conditional flags indicating status of the ALU operations.",
        "sol_hi": "फ़्लैग रजिस्टर में कैरी, ओवरफ़्लो, साइन आदि फ़्लैग स्टोर किए जाते हैं।"
    },
    {
        "q": "Which processor design utilizes variable-length instructions that perform multi-cycle operations directly in hardware?",
        "q_hi": "कौन सा प्रोसेसर डिज़ाइन परिवर्तनशील-लंबाई वाले निर्देशों का उपयोग करता है जो सीधे हार्डवेयर में बहु-चक्र संचालन निष्पादित करते हैं?",
        "opts": ["CISC", "RISC", "HARVARD", "MISD"],
        "opts_hi": ["CISC (CISC)", "RISC", "HARVARD", "MISD"],
        "ans": 0,
        "sol": "CISC (Complex Instruction Set Computer) utilizes complex, variable-length instructions that take multiple cycles to execute.",
        "sol_hi": "CISC डिज़ाइन जटिल, परिवर्तनशील लंबाई के निर्देशों का उपयोग करता है।"
    },
    {
        "q": "Which of the following buses is bidirectional?",
        "q_hi": "निम्नलिखित में से कौन सी बस द्वि-दिशात्मक (bidirectional) होती है?",
        "opts": ["Address Bus only", "Data Bus only", "Control Bus and Data Bus", "Address Bus and Control Bus"],
        "opts_hi": ["केवल एड्रेस बस", "केवल डेटा बस", "कंट्रोल बस और डेटा बस (Control & Data)", "एड्रेस बस और कंट्रोल बस"],
        "ans": 2,
        "sol": "Both the Data Bus (transfers data back and forth) and Control Bus (transfers read/write signals and interrupts in both directions) are bidirectional. The Address Bus is unidirectional.",
        "sol_hi": "डेटा बस और कंट्रोल बस दोनों द्वि-दिशात्मक होती हैं, जबकि एड्रेस बस केवल एक दिशा में संकेत भेजती है।"
    },
    {
        "q": "In which part of the CPU is the instruction decoding logic physically located?",
        "q_hi": "सीपीयू के किस हिस्से में निर्देश डिकोडिंग लॉजिक (decoding logic) भौतिक रूप से स्थित होता है?",
        "opts": ["Arithmetic Logic Unit", "Control Unit", "Internal Registers", "System Cache"],
        "opts_hi": ["अर्थमेटिक लॉजिक यूनिट", "कंट्रोल यूनिट (Control Unit)", "आंतरिक रजिस्टर", "सिस्टम कैश"],
        "ans": 1,
        "sol": "The instruction decoding logic is located inside the Control Unit (CU), which interprets the instruction code loaded in the IR.",
        "sol_hi": "निर्देशों को डिकोड करने और समझने की कार्यप्रणाली कंट्रोल यूनिट (CU) के भीतर होती है।"
    },
    {
        "q": "Which register is directly connected to the Data Bus to store values read from or written to memory?",
        "q_hi": "मेमोरी से पढ़े गए या लिखे गए मानों को संग्रहीत करने के लिए कौन सा रजिस्टर सीधे डेटा बस से जुड़ा होता है?",
        "opts": ["Memory Data Register (MDR)", "Memory Address Register (MAR)", "Program Counter (PC)", "Flag Register"],
        "opts_hi": ["मेमोरी डेटा रजिस्टर (MDR)", "मेमोरी एड्रेस रजिस्टर (MAR)", "प्रोग्राम काउंटर", "फ्लैग रजिस्टर"],
        "ans": 0,
        "sol": "The Memory Data Register (MDR) is connected directly to the Data Bus to buffer the data elements transferred between CPU and memory/IO.",
        "sol_hi": "मेमोरी डेटा रजिस्टर (MDR) सीधे डेटा बस से जुड़ा होता है और ट्रांसफर हो रहे मानों को बफ़र करता है।"
    },
    {
        "q": "The time required to complete the fetch, decode, and execute cycle of an instruction is called which of the following?",
        "q_hi": "एक निर्देश के फेच, डिकोड और निष्पादन चक्र को पूरा करने के लिए आवश्यक समय को निम्नलिखित में से क्या कहा जाता है?",
        "opts": ["Access Time", "Execution Time / Instruction Cycle", "Seek Time", "Refresh Delay"],
        "opts_hi": ["एक्सेस टाइम", "निष्पादन समय / निर्देश चक्र (Instruction Cycle)", "सीक टाइम", "रिफ्रेश डिले"],
        "ans": 1,
        "sol": "The Instruction Cycle (or Machine Cycle) represents the complete sequence of fetch, decode, execute, and store operations.",
        "sol_hi": "निर्देश चक्र (Instruction Cycle) वह समय है जिसमें निर्देश को लाने, समझने और चलाने की पूरी प्रक्रिया पूरी होती है।"
    },
    {
        "q": "What is the typical word length of modern desktop computer processor registers?",
        "q_hi": "आधुनिक डेस्कटॉप कंप्यूटर प्रोसेसर रजिस्टरों की विशिष्ट वर्ड लंबाई (word length) क्या है?",
        "opts": ["8 bits", "16 bits", "32 bits", "64 bits"],
        "opts_hi": ["8 बिट्स", "16 बिट्स", "32 बिट्स", "64 बिट्स (64 bits)"],
        "ans": 3,
        "sol": "Modern desktop processors use 64-bit architectures, meaning their main general-purpose registers are 64 bits wide.",
        "sol_hi": "वर्तमान डेस्कटॉप प्रोसेसर 64-बिट वास्तुकला पर आधारित होते हैं, जो एक बार में 64-बिट चौड़ा डेटा मान प्रोसेस कर सकते हैं।"
    },
    {
        "q": "Which register tracks the return addresses during recursive function calls or subroutine jumps?",
        "q_hi": "पुनरावर्ती (recursive) फ़ंक्शन कॉल या सबरूटीन जंप के दौरान रिटर्न पते (return addresses) पर नज़र रखने के लिए किस रजिस्टर का उपयोग किया जाता है?",
        "opts": ["Program Counter", "Stack Pointer", "Instruction Register", "Accumulator"],
        "opts_hi": ["प्रोग्राम काउंटर", "स्टैक पॉइंटर (Stack Pointer)", "इंस्ट्रक्शन रजिस्टर", "एक्यूमुलेटर"],
        "ans": 1,
        "sol": "The Stack Pointer (SP) manages the stack memory, which dynamically stores return addresses and local variables during nested function calls.",
        "sol_hi": "सबरूटीन या फ़ंक्शन कॉल के दौरान लौटने वाले पते को स्टैक में सुरक्षित किया जाता है, जिसका प्रबंधन स्टैक पॉइंटर (SP) करता है।"
    },
    {
        "q": "What is the primary benefit of Harvard Architecture compared to Von Neumann Architecture?",
        "q_hi": "वॉन न्यूमैन आर्किटेक्चर की तुलना में हार्वर्ड आर्किटेक्चर का प्राथमिक लाभ क्या है?",
        "opts": [
            "Simpler circuitry and lower manufacturing cost",
            "Avoidance of bus conflicts during simultaneous code and data fetch",
            "Ability to run CISC instruction sets in a single cycle",
            "Compatibility with x86 assembly code"
        ],
        "opts_hi": [
            "सरल सर्किट और कम विनिर्माण लागत",
            "एक साथ कोड और डेटा प्राप्त करने के दौरान बस संघर्ष से बचाव (No Bus conflict)",
            "एक चक्र में CISC निर्देश सेट चलाने की क्षमता",
            "x86 असेंबली कोड के साथ अनुकूलता"
        ],
        "ans": 1,
        "sol": "Harvard architecture's separate buses for instruction and data eliminate conflicts (Von Neumann Bottleneck), allowing concurrent memory access.",
        "sol_hi": "हार्वर्ड आर्किटेक्चर में अलग बस और मेमोरी होने से निर्देश और डेटा को एक साथ एक्सेस किया जा सकता है, जिससे गति बढ़ती है।"
    },
    {
        "q": "Which of the following registers is NOT accessible directly by assembly language instructions?",
        "q_hi": "निम्नलिखित में से कौन सा रजिस्टर असेंबली भाषा के निर्देशों द्वारा सीधे एक्सेस करने योग्य नहीं है?",
        "opts": ["Accumulator", "Instruction Register (IR)", "Stack Pointer", "General Purpose Register R1"],
        "opts_hi": ["एक्यूमुलेटर", "इंस्ट्रक्शन रजिस्टर - IR (Not directly accessible)", "स्टैक पॉइंटर", "जनरल पर्पज रजिस्टर R1"],
        "ans": 1,
        "sol": "The Instruction Register (IR) is used internally by the Control Unit decoder and cannot be read or modified directly by programmer instructions.",
        "sol_hi": "इंस्ट्रक्शन रजिस्टर (IR) आंतरिक रजिस्टर है जिसका उपयोग कंट्रोल यूनिट स्वयं करती है, इसे प्रोग्रामर असेंबली भाषा में सीधे बदल नहीं सकता।"
    }
]

# ----------------- MOCK TEST QUESTIONS (15 Qs) -----------------
mock_test_questions = [
    {
        "q": "Which of the following special registers stores the address of the memory location currently being accessed for read or write?",
        "q_hi": "निम्नलिखित विशिष्ट रजिस्टरों में से कौन सा उस मेमोरी लोकेशन के एड्रेस को संग्रहीत करता है जिसे वर्तमान में पढ़ने या लिखने के लिए एक्सेस किया जा रहा है?",
        "opts": ["Memory Data Register (MDR)", "Memory Address Register (MAR)", "Instruction Register (IR)", "Program Counter (PC)"],
        "opts_hi": ["मेमोरी डेटा रजिस्टर (MDR)", "मेमोरी एड्रेस रजिस्टर (MAR)", "इंस्ट्रक्शन रजिस्टर (IR)", "प्रोग्राम काउंटर (PC)"],
        "ans": 1,
        "sol": "The Memory Address Register (MAR) is loaded with the memory address to be read/written before memory access is triggered.",
        "sol_hi": "मेमोरी एड्रेस रजिस्टर (MAR) में लक्षित मेमोरी लोकेशन का पता होता है जिसे प्रोसेस किया जाना है।"
    },
    {
        "q": "The 'Von Neumann Bottleneck' is primarily a result of which physical limitation?",
        "q_hi": "वॉन न्यूमैन बॉटलनैक (Von Neumann Bottleneck) मुख्य रूप से किस भौतिक सीमा का परिणाम है?",
        "opts": [
            "Sharing a single physical bus for both instructions and data",
            "Using registers that are too small to address RAM",
            "Excessive heat generated by high-speed execution units",
            "Slow decoding speed of the Control Unit"
        ],
        "opts_hi": [
            "निर्देशों और डेटा दोनों के लिए एक ही भौतिक बस साझा करना (Shared Bus)",
            "रैम को एड्रेस करने के लिए बहुत छोटे रजिस्टरों का उपयोग करना",
            "उच्च गति निष्पादन इकाइयों द्वारा उत्पन्न अत्यधिक गर्मी",
            "कंट्रोल यूनिट की धीमी डिकोडिंग गति"
        ],
        "ans": 0,
        "sol": "In Von Neumann architecture, a shared bus carries both instruction codes and data. The CPU cannot fetch instructions and read/write data at the same time.",
        "sol_hi": "एक ही साझा बस के माध्यम से डेटा और निर्देश दोनों ले जाने के कारण सीपीयू को मेमोरी ऑपरेशन्स के लिए इंतजार करना पड़ता है।"
    },
    {
        "q": "What register holds the instruction code currently fetched from memory while it is being decoded by the Control Unit?",
        "q_hi": "मेमोरी से लाया गया वह निर्देश कोड किस रजिस्टर में संग्रहीत रहता है जब वह कंट्रोल यूनिट द्वारा डिकोड किया जा रहा होता है?",
        "opts": ["Program Counter (PC)", "Instruction Register (IR)", "Memory Address Register (MAR)", "Accumulator (AC)"],
        "opts_hi": ["प्रोग्राम काउंटर (PC)", "इंस्ट्रक्शन रजिस्टर (IR)", "मेमोरी एड्रेस रजिस्टर (MAR)", "एक्यूमुलेटर (AC)"],
        "ans": 1,
        "sol": "The Instruction Register (IR) holds the fetched instruction during decoding and execution stages.",
        "sol_hi": "फेच किए गए निर्देश को इंस्ट्रक्शन रजिस्टर (IR) में रखा जाता है जब तक कि उसे डिकोड न किया जा सके।"
    },
    {
        "q": "Which processor architecture executes simple instructions of fixed length in a single clock cycle, relying heavily on registers and software optimization?",
        "q_hi": "कौन सा प्रोसेसर आर्किटेक्चर एक क्लॉक साइकिल में निश्चित लंबाई के सरल निर्देशों को निष्पादित करता है, जो रजिस्टरों और सॉफ़्टवेयर अनुकूलन पर अत्यधिक निर्भर करता है?",
        "opts": ["RISC", "CISC", "Von Neumann", "Harvard"],
        "opts_hi": ["RISC (RISC)", "CISC", "वॉन न्यूमैन", "हार्वर्ड"],
        "ans": 0,
        "sol": "RISC (Reduced Instruction Set Computer) focuses on simple instructions, single-cycle execution, and a large number of registers to optimize pipelining.",
        "sol_hi": "RISC (रिड्यूस्ड इंस्ट्रक्शन सेट कंप्यूटर) में छोटे, सरल और तीव्र निर्देश सेट होते हैं।"
    },
    {
        "q": "Which of the following system buses carries address locations from the CPU to memory chips, and is strictly unidirectional?",
        "q_hi": "निम्नलिखित में से कौन सी सिस्टम बस सीपीयू से मेमोरी चिप्स तक एड्रेस लोकेशन ले जाती है, और पूरी तरह से एक-दिशात्मक होती है?",
        "opts": ["Data Bus", "Control Bus", "Address Bus", "Expansion Bus"],
        "opts_hi": ["डेटा बस", "कंट्रोल बस", "एड्रेस बस (Address Bus)", "एक्सपेंशन बस"],
        "ans": 2,
        "sol": "The Address Bus carries addresses from the CPU to memory/IO. It is unidirectional because only the CPU generates address targets.",
        "sol_hi": "एड्रेस बस (Address Bus) केवल एक दिशा में (सीपीयू से बाहर की ओर) पते ले जाती है।"
    },
    {
        "q": "Which CPU register stores the intermediate results of arithmetic and logical computations?",
        "q_hi": "कौन सा सीपीयू रजिस्टर गणितीय और तार्किक गणनाओं के मध्यवर्ती (intermediate) परिणामों को संग्रहीत करता है?",
        "opts": ["Program Counter (PC)", "Accumulator (AC)", "Instruction Register (IR)", "Stack Pointer (SP)"],
        "opts_hi": ["प्रोग्राम काउंटर (PC)", "एक्यूमुलेटर (AC)", "इंस्ट्रक्शन रजिस्टर (IR)", "स्टैक पॉइंटर (SP)"],
        "ans": 1,
        "sol": "The Accumulator (AC) is a register that acts as a temporary buffer for immediate results from the ALU.",
        "sol_hi": "एक्यूमुलेटर (AC) अस्थायी रूप से बीच के परिणामों को सहेजता है।"
    },
    {
        "q": "A CPU with a 32-bit address bus can directly reference how many bytes of physical RAM memory?",
        "q_hi": "32-बिट एड्रेस बस वाला सीपीयू सीधे भौतिक रैम मेमोरी के कितने बाइट्स को संदर्भित (reference) कर सकता है?",
        "opts": ["32 MB", "4 GB", "64 GB", "16 TB"],
        "opts_hi": ["32 MB", "4 GB (4 Gigabytes)", "64 GB", "16 TB"],
        "ans": 1,
        "sol": "A 32-bit address bus provides $2^{32}$ addresses, allowing direct access to 4 Gigabytes (GB) of memory.",
        "sol_hi": "$2^{32}$ = 4 GB (गीगाबाइट) मेमोरी एड्रेस स्पेस।"
    },
    {
        "q": "In which phase of the instruction cycle is the Program Counter (PC) value incremented to point to the next instruction?",
        "q_hi": "निर्देश चक्र के किस चरण में प्रोग्राम काउंटर (PC) का मान बढ़ाकर अगले निर्देश की ओर इंगित किया जाता है?",
        "opts": ["Fetch Phase", "Decode Phase", "Execute Phase", "Write-back Phase"],
        "opts_hi": ["फेच चरण (Fetch Phase)", "डिकोड चरण", "एक्जीक्यूट चरण", "राइट-बैक चरण"],
        "ans": 0,
        "sol": "During the Fetch phase, once the current instruction is fetched, the PC automatically increments to point to the next instruction in sequence.",
        "sol_hi": "निर्देश लाते ही (Fetch phase में), प्रोग्राम काउंटर स्वतः बढ़ जाता है।"
    },
    {
        "q": "Which register holds status flags such as Carry, Zero, Sign, and Overflow flag?",
        "q_hi": "कौन सा रजिस्टर स्टेटस फ़्लैग जैसे कैरी, ज़ीरो, साइन और ओवरफ़्लो फ़्लैग रखता है?",
        "opts": ["Program Counter", "Flag Register / Program Status Word (PSW)", "Instruction Register", "Memory Data Register"],
        "opts_hi": ["प्रोग्राम काउंटर", "फ्लैग रजिस्टर / प्रोग्राम स्टेटस वर्ड (Flag Register)", "इंस्ट्रक्शन रजिस्टर", "मेमोरी डेटा रजिस्टर"],
        "ans": 1,
        "sol": "The Flag Register (PSW) holds individual bits that register specific condition flags of the last ALU execution result.",
        "sol_hi": "फ्लैग रजिस्टर या प्रोग्राम स्टेटस वर्ड (PSW) में विभिन्न स्थिति फ़्लैग सहेजे जाते हैं।"
    },
    {
        "q": "Which bus carries clock pulses, read/write commands, and interrupt signals between the CPU and memory?",
        "q_hi": "कौन सी बस सीपीयू और मेमोरी के बीच क्लॉक पल्स, रीड/राइट कमांड और इंटरप्ट सिग्नल ले जाती है?",
        "opts": ["Address Bus", "Data Bus", "Control Bus", "PCI Express Bus"],
        "opts_hi": ["एड्रेस बस", "डेटा बस", "कंट्रोल बस (Control Bus)", "PCI एक्सप्रेस बस"],
        "ans": 2,
        "sol": "The Control Bus carries commands, clocks, read/write strobes, and hardware interrupt lines to synchronize operations.",
        "sol_hi": "कंट्रोल बस (Control Bus) सिस्टम के नियंत्रण एवं समन्वय वाले संकेत ले जाती है।"
    },
    {
        "q": "Which of the following registers is directly accessible to assembly level programmers?",
        "q_hi": "निम्नलिखित में से कौन सा रजिस्टर असेंबली स्तर के प्रोग्रामर के लिए सीधे सुलभ (accessible) है?",
        "opts": ["Instruction Register (IR)", "Accumulator (AC)", "Memory Address Register (MAR) internally", "Microprogram Counter"],
        "opts_hi": ["इंस्ट्रक्शन रजिस्टर (IR)", "एक्यूमुलेटर - AC (Directly accessible)", "मेमोरी एड्रेस रजिस्टर (MAR)", "माइक्रोप्रोग्राम काउंटर"],
        "ans": 1,
        "sol": "Programmers can write instructions to read from or load values into the Accumulator. The IR is managed internally by the CPU Control Unit.",
        "sol_hi": "असेंबली भाषा में एक्यूमुलेटर (AC) को कोड द्वारा बदला या पढ़ा जा सकता है, जबकि IR पूरी तरह से आंतरिक रूप से काम करता है।"
    },
    {
        "q": "Which processor design features complex instructions that may take several clock cycles, prioritizing hardware-level complexity?",
        "q_hi": "कौन सा प्रोसेसर डिज़ाइन जटिल निर्देशों की विशेषता रखता है जो कई क्लॉक साइकिल ले सकते हैं, और हार्डवेयर-स्तरीय जटिलता को प्राथमिकता देते हैं?",
        "opts": ["CISC", "RISC", "Harvard", "Von Neumann Architecture"],
        "opts_hi": ["CISC (CISC)", "RISC", "हार्वर्ड", "वॉन न्यूमैन आर्किटेक्चर"],
        "ans": 0,
        "sol": "CISC (Complex Instruction Set Computer) focuses on complex hardware instructions that can carry out multiple steps (like fetch, calculate, store) in one instruction.",
        "sol_hi": "CISC प्रोसेसर जटिल बहु-चक्र निर्देशों पर आधारित होता है।"
    },
    {
        "q": "What register acts as a buffer holding data elements transferred to or from RAM memory?",
        "q_hi": "रैम मेमोरी से भेजे गए या प्राप्त किए गए डेटा तत्वों को बफ़र करने का काम कौन सा रजिस्टर करता है?",
        "opts": ["Memory Address Register (MAR)", "Memory Data Register (MDR) / MBR", "Instruction Register (IR)", "Program Counter (PC)"],
        "opts_hi": ["मेमोरी एड्रेस रजिस्टर (MAR)", "मेमोरी डेटा रजिस्टर (MDR) / MBR", "इंस्ट्रक्शन रजिस्टर (IR)", "प्रोग्राम काउंटर (PC)"],
        "ans": 1,
        "sol": "The Memory Data Register (MDR), or Memory Buffer Register (MBR), acts as a temporary buffer for data being transferred between RAM and the CPU.",
        "sol_hi": "मेमोरी डेटा रजिस्टर (MDR) या MBR डेटा को रैम और सीपीयू के बीच बफ़र करता है।"
    },
    {
        "q": "What architecture has separate memories and physically separate bus lines for instructions and data?",
        "q_hi": "किस आर्किटेक्चर में निर्देशों और डेटा के लिए अलग-अलग मेमोरी और भौतिक रूप से अलग बस लाइनें होती हैं?",
        "opts": ["Harvard Architecture", "Von Neumann Architecture", "Shared Memory Design", "Single Bus Model"],
        "opts_hi": ["हार्वर्ड आर्किटेक्चर (Harvard Architecture)", "वॉन न्यूमैन आर्किटेक्चर", "साझा मेमोरी डिजाइन", "सिंगल बस मॉडल"],
        "ans": 0,
        "sol": "Harvard Architecture employs separate memories and paths for instructions and data, allowing parallel memory cycles.",
        "sol_hi": "हार्वर्ड आर्किटेक्चर कोड और डेटा को समानांतर एक्सेस करने के लिए अलग-अलग बसों का उपयोग करता है।"
    },
    {
        "q": "The word length of a CPU register refers to which of the following?",
        "q_hi": "सीपीयू रजिस्टर की वर्ड लंबाई (word length) निम्नलिखित में से किसे संदर्भित करती है?",
        "opts": [
            "The physical size of the silicon chip",
            "The number of bits the register can hold and process in a single operation",
            "The length of the instruction execution pipeline",
            "The maximum length of the system clock cycle"
        ],
        "opts_hi": [
            "सिलिकॉन चिप का भौतिक आकार",
            "रजिस्टर में स्टोर और प्रोसेस किए जा सकने वाले कुल बिट्स की संख्या (Bits per operation)",
            "निर्देश निष्पादन पाइपलाइन की लंबाई",
            "सिस्टम क्लॉक चक्र की अधिकतम लंबाई"
        ],
        "ans": 1,
        "sol": "Word length or register width is the number of bits (e.g., 32-bit or 64-bit) that the CPU can process simultaneously in a single register operation.",
        "sol_hi": "वर्ड लंबाई का अर्थ रजिस्टर की बिट-क्षमता (जैसे 32-बिट या 64-बिट) है जो एक चक्र में प्रोसेस होती है।"
    }
]

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_theory():
    return {
        "breadcrumbs": breadcrumbs_en,
        "hero": hero_en,
        "labels": labels_en,
        "timeline": timeline_en,
        "mnemonics": mnemonics_en,
        "flashcards": flashcards_en,
        "traps": traps_en,
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Review CPU internal organization, cycle steps, and registers.", "sections": deep_dive_en}
    }

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. CPU Organization & Cycles",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which CPU unit performs logical comparisons?", "opts": ["Control Unit", "ALU", "Registers", "Buses"], "ans": 1, "sol": "ALU performs all arithmetic calculations and logical comparisons."},
                    {"type": "MCQ", "q": "What is the second step of the instruction cycle?", "opts": ["Fetch", "Execute", "Decode", "Store"], "ans": 2, "sol": "Decode is the second step, where the instruction in the IR is interpreted."},
                    {"type": "True/False", "q": "True or False: Registers reside outside the CPU chip on the motherboard.", "ans": False, "sol": "False. Registers are located directly inside the CPU core for speed."},
                    {"type": "One-Liner", "q": "What is the third stage of the machine cycle?", "sol": "Execute"}
                ]
            },
            {
                "title": "2. CPU Registers & Functions",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which register holds the current instruction being executed?", "opts": ["PC", "MAR", "IR", "MDR"], "ans": 2, "sol": "Instruction Register (IR) holds the current instruction binary code."},
                    {"type": "MCQ", "q": "Which register holds ALU intermediate calculation results?", "opts": ["Accumulator", "Program Counter", "Stack Pointer", "Memory Buffer Register"], "ans": 0, "sol": "Accumulator holds intermediate arithmetic and logical results."},
                    {"type": "True/False", "q": "True or False: The Program Counter (PC) holds the address of the current instruction being executed.", "ans": False, "sol": "False. PC holds the address of the NEXT instruction to be executed."},
                    {"type": "One-Liner", "q": "Which register connects directly to the Address Bus?", "sol": "MAR (Memory Address Register)"}
                ]
            },
            {
                "title": "3. Architectures & Buses",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which bus is unidirectional?", "opts": ["Data Bus", "Address Bus", "Control Bus", "PCI Bus"], "ans": 1, "sol": "Address Bus is strictly unidirectional, carrying targets from CPU to RAM/IO."},
                    {"type": "MCQ", "q": "Which architecture separates instruction and data memories/buses?", "opts": ["Von Neumann", "Harvard", "x86 CISC", "SIMD Architecture"], "ans": 1, "sol": "Harvard architecture uses physically separate paths and storage for code and data."},
                    {"type": "True/False", "q": "True or False: RISC architectures execute simple instructions in single clock cycles.", "ans": True, "sol": "True. RISC instructions are simplified to complete in a single cycle using pipelining."},
                    {"type": "One-Liner", "q": "What is the bottleneck called in Von Neumann design?", "sol": "Von Neumann Bottleneck"}
                ]
            }
        ]
    }

def build_theory_hi():
    return {
        "breadcrumbs": breadcrumbs_hi,
        "hero": hero_hi,
        "labels": labels_hi,
        "timeline": timeline_hi,
        "mnemonics": mnemonics_hi,
        "flashcards": flashcards_hi,
        "traps": traps_hi,
        "deepDive": {"title": f"{TOPIC_DISPLAY_HI} के मुख्य अध्ययन नोट्स", "description": "सीपीयू के आंतरिक घटकों, चक्रों और विशेष प्रयोजन रजिस्टरों की समीक्षा।", "sections": deep_dive_hi}
    }

def build_practice_hi():
    practice_obj = {
        "practiceQuestions": [
            {"q": pq["q_hi"], "opts": pq["opts_hi"], "ans": pq["ans"], "sol": pq["sol_hi"]} for pq in practice_questions
        ],
        "mockTestQuestions": [
            {"q": mtq["q_hi"], "opts": mtq["opts_hi"], "ans": mtq["ans"], "sol": mtq["sol_hi"]} for mtq in mock_test_questions
        ]
    }
    return practice_obj

def build_mastery_hi():
    return {
        "sections": [
            {
                "title": "1. सीपीयू संगठन और चक्र",
                "masteryZone": [
                    {"type": "MCQ", "q": "कौन सी सीपीयू इकाई तार्किक तुलना करती है?", "opts": ["कंट्रोल यूनिट", "ALU", "रजिस्टर", "बसें"], "ans": 1, "sol": "ALU सभी गणितीय गणनाएं और तार्किक तुलनाएं करता है।"},
                    {"type": "MCQ", "q": "निर्देश चक्र का दूसरा चरण क्या है?", "opts": ["फेच", "एक्जीक्यूट", "डिकोड", "स्टोर"], "ans": 2, "sol": "डिकोड दूसरा चरण है, जहाँ IR में निर्देश का विश्लेषण किया जाता है।"},
                    {"type": "True/False", "q": "सही या गलत: रजिस्टर प्रोसेसर चिप के बाहर मदरबोर्ड पर स्थित होते हैं।", "ans": False, "sol": "गलत। रजिस्टर तीव्र गति के लिए प्रोसेसर चिप के अंदर होते हैं।"},
                    {"type": "One-Liner", "q": "मशीन चक्र का तीसरा चरण क्या है?", "sol": "एक्जीक्यूट (Execute)"}
                ]
            },
            {
                "title": "2. सीपीयू रजिस्टर और कार्य",
                "masteryZone": [
                    {"type": "MCQ", "q": "कौन सा रजिस्टर निष्पादित हो रहे वर्तमान निर्देश को रखता है?", "opts": ["PC", "MAR", "IR", "MDR"], "ans": 2, "sol": "इंस्ट्रक्शन रजिस्टर (IR) वर्तमान निर्देश का बाइनरी कोड रखता है।"},
                    {"type": "MCQ", "q": "ALU के मध्यवर्ती परिणामों को कौन सा रजिस्टर रखता है?", "opts": ["एक्यूमुलेटर", "प्रोग्राम काउंटर", "स्टैक पॉइंटर", "मेमोरी बफ़र रजिस्टर"], "ans": 0, "sol": "एक्यूमुलेटर (Accumulator) गणनाओं के परिणामों को सहेजता है।"},
                    {"type": "True/False", "q": "सही या गलत: प्रोग्राम काउंटर (PC) वर्तमान में चलने वाले निर्देश का पता रखता है।", "ans": False, "sol": "गलत। PC अगले (NEXT) निर्देश का पता रखता है।"},
                    {"type": "One-Liner", "q": "कौन सा रजिस्टर सीधे एड्रेस बस से जुड़ा होता है?", "sol": "MAR"}
                ]
            },
            {
                "title": "3. आर्किटेक्चर और बसें",
                "masteryZone": [
                    {"type": "MCQ", "q": "कौन सी बस एक-दिशात्मक होती है?", "opts": ["डेटा बस", "एड्रेस बस", "कंट्रोल बस", "PCI बस"], "ans": 1, "sol": "एड्रेस बस पूरी तरह से एक-दिशात्मक होती है, जो सीपीयू से पता बाहर ले जाती है।"},
                    {"type": "MCQ", "q": "कौन सा आर्किटेक्चर निर्देश और डेटा के लिए अलग-अलग मेमोरी और बस का उपयोग करता है?", "opts": ["वॉन न्यूमैन", "हार्वर्ड", "x86 CISC", "SIMD"], "ans": 1, "sol": "हार्वर्ड आर्किटेक्चर निर्देश और डेटा के लिए अलग-अलग भौतिक मेमोरी और पथों का उपयोग करता है।"},
                    {"type": "True/False", "q": "सही या गलत: RISC प्रोसेसर सरल निर्देशों को एक ही क्लॉक साइकिल में चला सकते हैं।", "ans": True, "sol": "सही। RISC निर्देशों को पाइपलाइनिंग के माध्यम से तेजी से पूरा करने के लिए सरल बनाया जाता है।"},
                    {"type": "One-Liner", "q": "वॉन न्यूमैन डिज़ाइन में गति बाधा (bottleneck) को क्या कहते हैं?", "sol": "वॉन न्यूमैन बॉटलनैक"}
                ]
            }
        ]
    }

# ----------------- FILE GENERATION -----------------
import re

def parse_markdown(data):
    if isinstance(data, str):
        return re.sub(r'\*\*(.*?)\*\*', r'<strong style="color: #e67e22; font-weight: 700;">\1</strong>', data)
    elif isinstance(data, dict):
        return {k: parse_markdown(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [parse_markdown(item) for item in data]
    return data

def write_json(filepath, data):
    formatted_data = parse_markdown(data)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(formatted_data, f, indent=2, ensure_ascii=False)
    print(f"Written: {filepath}")

# Write English files
write_json(os.path.join(BASE_DIR, "theory.json"), build_theory())
write_json(os.path.join(BASE_DIR, "practice.json"), build_practice())
write_json(os.path.join(BASE_DIR, "mastery.json"), build_mastery())

# Write Hindi files
write_json(os.path.join(HI_DIR, "theory.json"), build_theory_hi())
write_json(os.path.join(HI_DIR, "practice.json"), build_practice_hi())
write_json(os.path.join(HI_DIR, "mastery.json"), build_mastery_hi())
