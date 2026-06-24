# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "sound-light"
TOPIC_DISPLAY = "Sound & Light"
TOPIC_DISPLAY_HI = "ध्वनि और प्रकाश"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\general-science\{TOPIC}"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "General Science",
    "parentUrl": "../",
    "current": "Sound & Light"
}

hero_en = {
    "title": "Sound & Light",
    "description": "Master wave motion, characteristics of sound (pitch, loudness, quality), speed of sound in different media, echo, sonar, Doppler effect, and light phenomena including reflection, refraction, dispersion, scattering, total internal reflection, mirrors, lenses, and human eye defects."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive Sound & Light Mock Test",
        "description": "Assess your understanding of sound waves, light propagation, reflection, refraction, optical instruments, and eye defects. This timed mock test consists of 15 questions.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Historical Progression of Optics & Acoustics",
    "description": "Key milestones in understanding the nature of sound and light.",
    "cards": [
        {
            "period": "Wave Theory of Light",
            "date": "1678",
            "details": "Christiaan Huygens proposes the wave theory of light, suggesting light travels as wavefronts through a hypothetical ether."
        },
        {
            "period": "Newton's Opticks",
            "date": "1704",
            "details": "Sir Isaac Newton publishes 'Opticks', proposing the corpuscular (particle) theory of light and detailing light dispersion using prisms."
        },
        {
            "period": "Young's Double-Slit Experiment",
            "date": "1801",
            "details": "Thomas Young demonstrates the wave nature of light through interference, dealing a major blow to Newton's corpuscular theory."
        },
        {
            "period": "Electromagnetic Wave Theory",
            "date": "1865",
            "details": "James Clerk Maxwell formulates equations showing that light is an electromagnetic wave, moving at a speed matching experimental values."
        },
        {
            "period": "Quantum Theory & Wave-Particle Duality",
            "date": "1905",
            "details": "Albert Einstein explains the Photoelectric Effect using light quanta (photons), establishing the dual wave-particle nature of light."
        }
    ]
}

mnemonics_en = {
    "title": "Sound & Light Mnemonics",
    "description": "Quick memory triggers to recall properties, formulas, and eye defects for competitive exams.",
    "items": [
        {
            "title": "Mnemonic 1: Myopia and Hypermetropia Lenses",
            "phrase": "\"My Near Concave, Hyper Far Convex\"",
            "decryption": "Remember the corrective lenses:<br>• **My Near Concave**: **My**opia (nearsightedness) is corrected using a **Concave** lens.<br>• **Hyper Far Convex**: **Hyper**metropia (farsightedness) is corrected using a **Convex** lens."
        },
        {
            "title": "Mnemonic 2: Electromagnetic Spectrum Order",
            "phrase": "\"Rich Men In Venus Use X-ray Goggles\"",
            "decryption": "Order of EM waves from lowest frequency (longest wavelength) to highest:<br>• **Rich**: **R**adio waves<br>• **Men**: **M**icrowaves<br>• **In**: **I**nfrared<br>• **Venus**: **V**isible light<br>• **Use**: **U**ltraviolet (UV)<br>• **X-ray**: **X**-rays<br>• **Goggles**: **G**amma rays"
        },
        {
            "title": "Mnemonic 3: Visible Light Dispersion Spectrum",
            "phrase": "\"VIBGYOR\"",
            "decryption": "Violet, Indigo, Blue, Green, Yellow, Orange, Red.<br>• **Violet** has the shortest wavelength and bends (deviates) the **most**.<br>• **Red** has the longest wavelength and bends the **least**."
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Hover or click to reveal the answers. Revisit these cards to build instant recall.",
    "items": [
        {
            "question": "What type of wave is a sound wave in air?",
            "answer": "Sound wave is a **longitudinal mechanical wave**. It requires a material medium to travel and cannot propagate in a vacuum.",
            "icon": "fa-volume-high"
        },
        {
            "question": "What is the relation between frequency, wavelength, and speed of a wave?",
            "answer": "**Speed (v) = Frequency (f) × Wavelength (λ)**. When a wave changes medium, its speed and wavelength change, but its frequency remains constant.",
            "icon": "fa-wave-square"
        },
        {
            "question": "What phenomenon causes the blue color of the sky and the red color of sunrise/sunset?",
            "answer": "**Rayleigh Scattering of light**. Blue light has a shorter wavelength and scatters more than other colors. During sunrise/sunset, light travels a longer path, and most blue light is scattered away, leaving red light.",
            "icon": "fa-cloud-sun"
        },
        {
            "question": "What is the critical angle and its relation to Total Internal Reflection?",
            "answer": "The **critical angle** is the angle of incidence in a denser medium for which the angle of refraction in the rarer medium is 90°. If the angle of incidence exceeds this, **Total Internal Reflection (TIR)** occurs.",
            "icon": "fa-gem"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid",
    "items": [
        "<strong>Trap 1:</strong> Believing sound travels faster in vacuum than in air. Remember, sound is a mechanical wave and requires a medium; its speed in a vacuum is <strong>exactly zero</strong>.",
        "<strong>Trap 2:</strong> Confusing the effect of temperature on the speed of sound. Speed of sound <strong>increases</strong> with temperature (by about 0.61 m/s per 1°C rise) and is independent of pressure changes at constant temperature.",
        "<strong>Trap 3:</strong> Confusing Myopia corrections with Hypermetropia. In Myopia (nearsightedness), the image is formed in front of the retina, and a <strong>concave lens</strong> is used. In Hypermetropia (farsightedness), the image is formed behind the retina, and a <strong>convex lens</strong> is used.",
        "<strong>Trap 4:</strong> Assuming a higher frequency means higher speed of sound. Frequency determines the <strong>pitch</strong> of the sound, but waves of all frequencies travel at the same speed in a given medium."
    ]
}

deep_dive_en = [
    {
        "title": "1. Wave Motion & Sound Wave Characteristics",
        "content": """<p>Waves transfer energy from one point to another without transferring matter. They are classified into mechanical (require a medium) and electromagnetic (do not require a medium).</p>
        
        <!-- SVG Diagram 1: Wave Types -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .grid-label { font-family: 'Outfit', sans-serif; font-weight: 600; fill: var(--primary, #8e44ad); font-size: 13px; }
            .wave-line { fill: none; stroke: var(--primary, #8e44ad); stroke-width: 2.5px; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            
            
            
            
          </style>
          <text x="20" y="30" class="svg-title">Wave Types: Transverse (Light) vs Longitudinal (Sound)</text>
          
          <!-- Transverse Wave (Left) -->
          <g transform="translate(10, 0)">
            <text x="50" y="55" class="grid-label">1. Transverse Wave (e.g., Light)</text>
            <path d="M 50 140 Q 90 80 130 140 T 210 140 T 290 140 T 370 140" class="wave-line" />
            <line x1="45" y1="140" x2="380" y2="140" stroke="rgba(128,128,128,0.3)" stroke-width="1.5" stroke-dasharray="4" />
            
            <circle cx="90" cy="80" r="4" fill="#e74c3c" />
            <text x="90" y="72" class="annot-text" text-anchor="middle">Crest</text>
            <circle cx="170" cy="200" r="4" fill="#e74c3c" />
            <text x="170" y="215" class="annot-text" text-anchor="middle">Trough</text>
            
            <line x1="90" y1="80" x2="250" y2="80" stroke="#2ecc71" stroke-width="1.5" stroke-dasharray="2" />
            <path d="M 90 80 L 100 77 M 90 80 L 100 83 M 250 80 L 240 77 M 250 80 L 240 83" stroke="#2ecc71" stroke-width="1.5" />
            <text x="170" y="95" class="annot-text" fill="#2ecc71" text-anchor="middle">Wavelength (λ)</text>
            
            <line x1="250" y1="140" x2="250" y2="80" stroke="#e67e22" stroke-width="1.5" />
            <text x="258" y="115" class="annot-text" fill="#e67e22">Amplitude (A)</text>
          </g>
          
          <!-- Longitudinal Wave (Right) -->
          <g transform="translate(420, 0)">
            <text x="50" y="55" class="grid-label">2. Longitudinal Wave (e.g., Sound)</text>
            <g stroke="var(--primary, #8e44ad)" stroke-width="2">
              <line x1="70" y1="100" x2="70" y2="180" />
              <line x1="75" y1="100" x2="75" y2="180" />
              <line x1="80" y1="100" x2="80" y2="180" />
              <line x1="85" y1="100" x2="85" y2="180" />
              <line x1="110" y1="100" x2="110" y2="180" opacity="0.4" />
              <line x1="140" y1="100" x2="140" y2="180" opacity="0.4" />
              <line x1="170" y1="100" x2="170" y2="180" />
              <line x1="175" y1="100" x2="175" y2="180" />
              <line x1="180" y1="100" x2="180" y2="180" />
              <line x1="185" y1="100" x2="185" y2="180" />
              <line x1="210" y1="100" x2="210" y2="180" opacity="0.4" />
              <line x1="240" y1="100" x2="240" y2="180" opacity="0.4" />
              <line x1="270" y1="100" x2="270" y2="180" />
              <line x1="275" y1="100" x2="275" y2="180" />
              <line x1="280" y1="100" x2="280" y2="180" />
              <line x1="285" y1="100" x2="285" y2="180" />
            </g>
            <text x="78" y="202" class="annot-text" text-anchor="middle">Compression</text>
            <text x="125" y="220" class="annot-text" text-anchor="middle">Rarefaction</text>
            <text x="178" y="202" class="annot-text" text-anchor="middle">Compression</text>
            
            <line x1="77" y1="90" x2="177" y2="90" stroke="#2ecc71" stroke-width="1.5" />
            <path d="M 77 90 L 87 87 M 77 90 L 87 93 M 177 90 L 167 87 M 177 90 L 167 93" stroke="#2ecc71" stroke-width="1.5" />
            <text x="127" y="83" class="annot-text" fill="#2ecc71" text-anchor="middle">Wavelength (λ)</text>
          </g>
        </svg>

        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Feature</th>
                <th>Sound Waves (in Air)</th>
                <th>Light Waves</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Type of Wave</strong></td>
                <td>Longitudinal Mechanical</td>
                <td>Transverse Electromagnetic</td>
              </tr>
              <tr>
                <td><strong>Medium Required</strong></td>
                <td>Yes (cannot travel in vacuum)</td>
                <td>No (travels fastest in vacuum)</td>
              </tr>
              <tr>
                <td><strong>Speed</strong></td>
                <td>~343 m/s in air (at 20°C)</td>
                <td>3 × 10⁸ m/s in vacuum</td>
              </tr>
              <tr>
                <td><strong>Nature of Particle Motion</strong></td>
                <td>Parallel to wave propagation (compressions & rarefactions)</td>
                <td>Perpendicular to wave propagation (crests & troughs)</td>
              </tr>
              <tr>
                <td><strong>Effect of Medium Density</strong></td>
                <td>Speed is highest in solids, then liquids, lowest in gases</td>
                <td>Speed is highest in vacuum/gases, lowest in solids</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <p><strong>Speed of Sound in Different Media:</strong> Speed of sound is given by Laplace's formula: <code>v = √(γP/ρ)</code>. Speed is directly proportional to temperature and humidity, but independent of pressure at constant temperature.</p>"""
    },
    {
        "title": "2. Acoustics: Reflection, Echo, Sonar & Doppler Effect",
        "content": """<p>Sound waves undergo reflection, refraction, diffraction, and interference. Some key phenomena include:</p>
        <ul>
          <li><strong>Echo</strong>: The repetition of sound due to its reflection from a distant obstacle. The minimum distance to hear a distinct echo in air is <strong>~17.2 meters</strong> (since the persistence of hearing is 0.1 seconds).</li>
          <li><strong>Reverberation</strong>: Persistence of sound due to multiple reflections. Reduced using sound-absorbing materials.</li>
          <li><strong>Sonar (Sound Navigation and Ranging)</strong>: Uses <strong>ultrasonic waves</strong> (frequency > 20,000 Hz) to measure depth or locate underwater objects. <code>Distance (d) = v × t / 2</code>.</li>
          <li><strong>Doppler Effect</strong>: The apparent change in frequency of a wave due to the relative motion between the source and the observer. As they approach, apparent frequency increases; as they recede, it decreases.</li>
        </ul>"""
    },
    {
        "title": "3. Light: Reflection, Spherical Mirrors & Lenses",
        "content": """<p>Light is a transverse electromagnetic wave. The laws of reflection apply to all types of mirrors:</p>
        
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Optical Element</th>
                <th>Type of Image Formed</th>
                <th>Key Applications</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Concave Mirror</strong></td>
                <td>Real & inverted (except when object is between F and P: virtual & magnified)</td>
                <td>Shaving mirrors, searchlights, dentist mirrors, solar furnaces</td>
              </tr>
              <tr>
                <td><strong>Convex Mirror</strong></td>
                <td>Always Virtual, erect, and diminished</td>
                <td>Rear-view mirrors in vehicles (gives a wider field of view)</td>
              </tr>
              <tr>
                <td><strong>Convex Lens (Converging)</strong></td>
                <td>Real & inverted (except when object is within focal length)</td>
                <td>Magnifying glass, camera, microscope, correcting Hypermetropia</td>
              </tr>
              <tr>
                <td><strong>Concave Lens (Diverging)</strong></td>
                <td>Always Virtual, erect, and diminished</td>
                <td>Flashlights, peepholes, correcting Myopia</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <p><strong>Mirror Formula:</strong> <code>1/f = 1/v + 1/u</code> | <strong>Lens Formula:</strong> <code>1/f = 1/v - 1/u</code> | <strong>Power of Lens:</strong> <code>P = 1/f (in meters)</code> (unit: Dioptre, D).</p>"""
    },
    {
        "title": "4. Refraction, Total Internal Reflection & Dispersion",
        "content": """<p>Refraction is the bending of light as it passes from one medium to another due to a change in speed. Snell's Law: <code>n₁ sin(i) = n₂ sin(r)</code>.</p>
        
        <!-- SVG Diagram 2: Refraction & TIR -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .medium-label { font-family: 'Outfit', sans-serif; font-weight: 600; fill: var(--primary, #8e44ad); font-size: 13px; }
            .ray-line { fill: none; stroke-width: 2px; }
            .normal-line { stroke: rgba(128, 128, 128, 0.6); stroke-width: 1.5px; stroke-dasharray: 4; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            
            
            
          </style>
          <text x="20" y="30" class="svg-title">Light Refraction, Critical Angle & Total Internal Reflection (TIR)</text>
          
          <rect x="0" y="120" width="800" height="120" fill="rgba(52, 152, 219, 0.08)" />
          <line x1="0" y1="120" x2="800" y2="120" stroke="#3498db" stroke-width="2" />
          <text x="20" y="105" class="medium-label">Rarer Medium (Air)</text>
          <text x="20" y="145" class="medium-label">Denser Medium (Water/Glass)</text>
          
          <line x1="200" y1="40" x2="200" y2="200" class="normal-line" />
          <line x1="400" y1="40" x2="400" y2="200" class="normal-line" />
          <line x1="600" y1="40" x2="600" y2="200" class="normal-line" />
          
          <g>
            <path d="M 120 180 L 200 120 L 250 50" fill="none" stroke="#e67e22" stroke-width="2" />
            <path d="M 160 150 L 158 142 M 160 150 L 150 152" stroke="#e67e22" stroke-width="2" />
            <path d="M 225 85 L 221 77 M 225 85 L 217 88" stroke="#e67e22" stroke-width="2" />
            <text x="180" y="115" class="annot-text">i</text>
            <text x="215" y="110" class="annot-text">r</text>
            <text x="200" y="215" class="annot-text" text-anchor="middle">1. Refraction (i &lt; θc)</text>
          </g>
          
          <g>
            <path d="M 310 180 L 400 120 L 520 120" fill="none" stroke="#2ecc71" stroke-width="2.5" />
            <path d="M 355 150 L 353 142 M 355 150 L 345 152" stroke="#2ecc71" stroke-width="2" />
            <path d="M 460 120 L 450 115 M 460 120 L 450 125" stroke="#2ecc71" stroke-width="2" />
            <text x="375" y="110" class="annot-text">θc</text>
            <text x="415" y="105" class="annot-text">r = 90°</text>
            <text x="400" y="215" class="annot-text" text-anchor="middle">2. Critical Angle (r = 90°)</text>
          </g>
          
          <g>
            <path d="M 500 180 L 600 120 L 700 180" fill="none" stroke="#e74c3c" stroke-width="2.5" />
            <path d="M 550 150 L 548 142 M 550 150 L 540 152" stroke="#e74c3c" stroke-width="2" />
            <path d="M 650 150 L 642 152 M 650 150 L 648 142" stroke="#e74c3c" stroke-width="2" />
            <text x="575" y="110" class="annot-text">i &gt; θc</text>
            <text x="615" y="110" class="annot-text">r = i</text>
            <text x="600" y="215" class="annot-text" text-anchor="middle">3. TIR (i &gt; θc)</text>
          </g>
        </svg>

        <ul>
          <li><strong>Total Internal Reflection (TIR)</strong>: Occurs when light travels from a denser to a rarer medium and the angle of incidence is greater than the critical angle. 
            <br><em>Applications:</em> Sparkle of diamonds, optical fibers, mirages in deserts.
          </li>
          <li><strong>Dispersion</strong>: Splitting of white light into its constituent colors (VIBGYOR) when passing through a prism. Violet deviates the most; Red deviates the least.
            <br><em>Rainbow:</em> Formed due to dispersion, refraction, and internal reflection of sunlight inside water droplets.
          </li>
          <li><strong>Scattering</strong>: Redirection of light by small particles. Rayleigh scattering explains why the sky is blue and danger signals are red (red scatters the least).
          </li>
        </ul>"""
    },
    {
        "title": "5. Human Eye Defects and Corrective Lenses",
        "content": """<p>The human eye uses a convex crystalline lens to focus light on the retina. Common defects include:</p>
        
        <!-- SVG Diagram 3: Eye Defects -->
        <svg viewBox="0 0 800 280" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .defect-label { font-family: 'Outfit', sans-serif; font-weight: 600; fill: var(--primary, #8e44ad); font-size: 13px; }
            .eye-ball { fill: none; stroke: var(--text-dark, #2c3e50); stroke-width: 1.5px; }
            .lens-shape { fill: rgba(142, 68, 173, 0.2); stroke: var(--primary, #8e44ad); stroke-width: 1.5px; }
            .light-ray { fill: none; stroke: #e67e22; stroke-width: 1.5px; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 10px; fill: var(--text-dark, #2c3e50); }
            
            
            
            
          </style>
          <text x="20" y="25" class="svg-title">Eye Defects: Myopia vs Hypermetropia & Corrective Optics</text>
          
          <g transform="translate(10, 0)">
            <text x="40" y="55" class="defect-label">A. MYOPIA (Nearsightedness)</text>
            <path d="M 120 100 A 30 30 0 1 1 120 160 C 110 150 105 130 120 100 Z" class="eye-ball" />
            <path d="M 120 115 A 15 15 0 0 1 120 145 Z" class="lens-shape" />
            <path d="M 40 120 L 120 120 L 140 130 L 120 140 L 40 140" class="light-ray" />
            <circle cx="140" cy="130" r="3" fill="#e74c3c" />
            <text x="140" y="115" class="annot-text" text-anchor="middle">Focus in front</text>
            
            <g transform="translate(0, 100)">
              <path d="M 120 100 A 30 30 0 1 1 120 160 C 110 150 105 130 120 100 Z" class="eye-ball" />
              <path d="M 120 115 A 15 15 0 0 1 120 145 Z" class="lens-shape" />
              <path d="M 75 110 L 85 110 L 80 130 L 85 150 L 75 150 L 80 130 Z" fill="rgba(52,152,219,0.15)" stroke="#3498db" stroke-width="1.5" />
              <text x="80" y="105" class="annot-text" text-anchor="middle" fill="#3498db">Concave</text>
              <path d="M 40 120 L 78 120 L 120 116 L 149 130 L 120 144 L 78 140 L 40 140" class="light-ray" />
              <circle cx="149" cy="130" r="3" fill="#2ecc71" />
              <text x="150" y="115" class="annot-text" text-anchor="middle">Focused on Retina</text>
            </g>
          </g>
          
          <g transform="translate(410, 0)">
            <text x="40" y="55" class="defect-label">B. HYPERMETROPIA (Farsightedness)</text>
            <path d="M 120 100 A 30 30 0 1 1 120 160 C 110 150 105 130 120 100 Z" class="eye-ball" />
            <path d="M 120 115 A 15 15 0 0 1 120 145 Z" class="lens-shape" />
            <path d="M 40 125 L 120 125 L 160 130 L 120 135 L 40 135" class="light-ray" />
            <circle cx="160" cy="130" r="3" fill="#e74c3c" />
            <text x="160" y="115" class="annot-text" text-anchor="middle">Focus behind</text>
            
            <g transform="translate(0, 100)">
              <path d="M 120 100 A 30 30 0 1 1 120 160 C 110 150 105 130 120 100 Z" class="eye-ball" />
              <path d="M 120 115 A 15 15 0 0 1 120 145 Z" class="lens-shape" />
              <path d="M 75 130 Q 80 110 85 130 T 75 130 Z" fill="rgba(46,204,113,0.15)" stroke="#2ecc71" stroke-width="1.5" transform="rotate(90 80 130)" />
              <text x="80" y="105" class="annot-text" text-anchor="middle" fill="#2ecc71">Convex</text>
              <path d="M 40 125 L 78 125 L 120 122 L 149 130 L 120 138 L 78 135 L 40 135" class="light-ray" />
              <circle cx="149" cy="130" r="3" fill="#2ecc71" />
              <text x="150" y="115" class="annot-text" text-anchor="middle">Focused on Retina</text>
            </g>
          </g>
        </svg>
        
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Defect</th>
                <th>Description</th>
                <th>Focus Location</th>
                <th>Corrective Lens</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Myopia (Nearsightedness)</strong></td>
                <td>Can see near objects clearly but not far objects</td>
                <td>In front of the retina</td>
                <td><strong>Concave Lens</strong> (negative power)</td>
              </tr>
              <tr>
                <td><strong>Hypermetropia (Farsightedness)</strong></td>
                <td>Can see far objects clearly but not near objects</td>
                <td>Behind the retina</td>
                <td><strong>Convex Lens</strong> (positive power)</td>
              </tr>
              <tr>
                <td><strong>Presbyopia</strong></td>
                <td>Loss of accommodation power due to aging</td>
                <td>Behind the retina</td>
                <td><strong>Bifocal Lens</strong> (upper concave, lower convex)</td>
              </tr>
              <tr>
                <td><strong>Astigmatism</strong></td>
                <td>Cannot focus on horizontal and vertical lines simultaneously</td>
                <td>Distorted focus</td>
                <td><strong>Cylindrical Lens</strong></td>
              </tr>
            </tbody>
          </table>
        </div>"""
    }
]

# ----------------- HINDI DATA DEFINITIONS -----------------
breadcrumbs_hi = {
    "parent": "सामान्य विज्ञान",
    "parentUrl": "../",
    "current": "ध्वनि और प्रकाश"
}

hero_hi = {
    "title": "ध्वनि और प्रकाश",
    "description": "तरंग गति, ध्वनि के लक्षण (तारत्व, प्रबलता, गुणवत्ता), विभिन्न माध्यमों में ध्वनि की चाल, प्रतिध्वनि, सोनार, डॉप्लर प्रभाव, और प्रकाश की घटनाओं जैसे परावर्तन, अपवर्तन, वर्ण-विक्षेपण, प्रकीर्णन, पूर्ण आंतरिक परावर्तन, दर्पण, लेंस और मानव नेत्र दोषों में महारत हासिल करें।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "इंटरएक्टिव ध्वनि और प्रकाश मॉक टेस्ट",
        "description": "ध्वनि तरंगों, प्रकाश संचरण, परावर्तन, अपवर्तन, ऑप्टिकल उपकरणों और नेत्र दोषों की अपनी समझ का परीक्षण करें। इस समयबद्ध मॉक टेस्ट में 15 प्रश्न शामिल हैं।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "प्रकाशिकी और ध्वनिकी का ऐतिहासिक विकास",
    "description": "ध्वनि और प्रकाश की प्रकृति को समझने के प्रमुख मील के पत्थर।",
    "cards": [
        {
            "period": "प्रकाश का तरंग सिद्धांत",
            "date": "1678",
            "details": "क्रिस्टियान हाइजेंस ने प्रकाश का तरंग सिद्धांत प्रस्तुत किया, जिसमें सुझाव दिया गया कि प्रकाश एक काल्पनिक ईथर के माध्यम से तरंग के रूप में यात्रा करता है।"
        },
        {
            "period": "न्यूटन की ऑप्टिक्स",
            "date": "1704",
            "details": "सर आइजैक न्यूटन ने 'ऑप्टिक्स' प्रकाशित किया, जिसमें प्रकाश के कणिका सिद्धांत का प्रस्ताव दिया गया और प्रिज्म का उपयोग करके प्रकाश के विक्षेपण का विवरण दिया गया।"
        },
        {
            "period": "यंग का द्विक-झिरी प्रयोग",
            "date": "1801",
            "details": "थॉमस यंग ने व्यतिकरण (Interference) के माध्यम से प्रकाश की तरंग प्रकृति का प्रदर्शन किया, जिससे न्यूटन के कणिका सिद्धांत को गहरा झटका लगा।"
        },
        {
            "period": "विद्युत चुंबकीय तरंग सिद्धांत",
            "date": "1865",
            "details": "जेम्स क्लर्क मैक्सवेल ने समीकरण तैयार किए जो दर्शाते हैं कि प्रकाश एक विद्युत चुंबकीय तरंग है, जिसकी गति प्रयोगात्मक मानों से मेल खाती है।"
        },
        {
            "period": "क्वांटम सिद्धांत और तरंग-कण द्वैैतता",
            "date": "1905",
            "details": "अल्बर्ट आइंस्टीन ने प्रकाश क्वांटा (फोटॉन) का उपयोग करके प्रकाश-विद्युत प्रभाव (Photoelectric Effect) की व्याख्या की, जिससे प्रकाश की दोहरी तरंग-कण प्रकृति स्थापित हुई।"
        }
    ]
}

mnemonics_hi = {
    "title": "ध्वनि और प्रकाश के स्मृति सूत्र",
    "description": "परीक्षा के लिए गुणों, सूत्रों और नेत्र दोषों को याद रखने के त्वरित सूत्र।",
    "items": [
        {
            "title": "स्मृति सूत्र 1: मायोपिया और हाइपरमेट्रोपिया लेंस",
            "phrase": "\"मायो निकट अवतल, हाइपर दूर उत्तल\"",
            "decryption": "सुधारक लेंस याद रखें:<br>• **निकट अवतल**: निकट दृष्टि दोष (Myopia) को **अवतल (Concave)** लेंस से ठीक किया जाता है।<br>• **दूर उत्तल**: दूर दृष्टि दोष (Hypermetropia) को **उत्तल (Convex)** लेंस से ठीक किया जाता है।"
        },
        {
            "title": "स्मृति सूत्र 2: विद्युत चुंबकीय स्पेक्ट्रम का क्रम",
            "phrase": "\"रेडियो माइक्रो इन्फ्रा दृश्य यूवी एक्स गामा\"",
            "decryption": "न्यूनतम आवृत्ति से अधिकतम आवृत्ति तक विद्युत चुंबकीय तरंगों का क्रम:<br>• **रेडियो**: रेडियो तरंगें<br>• **माइक्रो**: सूक्ष्म तरंगें<br>• **इन्फ्रा**: अवरक्त किरणें<br>• **दृश्य**: दृश्य प्रकाश<br>• **यूवी**: पराबैंगनी किरणें<br>• **एक्स**: एक्स-रे किरणें<br>• **गामा**: गामा किरणें"
        },
        {
            "title": "स्मृति सूत्र 3: दृश्य प्रकाश स्पेक्ट्रम (बैंजनीहपीनाला - VIBGYOR)",
            "phrase": "\"बै-जा-नी-ह-पी-ना-ला\"",
            "decryption": "बैंगनी, जामुनी, नीला, हरा, पीला, नारंगी, लाल।<br>• **बैंगनी** रंग की तरंगदैर्ध्य सबसे कम होती है और यह सबसे **अधिक** विचलित (झुकता) होता है।<br>• **लाल** रंग की तरंगदैर्ध्य सबसे अधिक होती है और यह सबसे **कम** विचलित होता है।"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय रिकॉल फ्लैशकार्ड",
    "description": "उत्तर देखने के लिए होवर करें या क्लिक करें। त्वरित याददाश्त बनाने के लिए इन कार्डों को दोबारा देखें।",
    "items": [
        {
            "question": "हवा में ध्वनि तरंग किस प्रकार की तरंग है?",
            "answer": "ध्वनि तरंग एक **अनुदैर्ध्य यांत्रिक तरंग (Longitudinal Mechanical Wave)** है। इसे यात्रा करने के लिए एक भौतिक माध्यम की आवश्यकता होती है और यह निर्वात में संचरित नहीं हो सकती।",
            "icon": "fa-volume-high"
        },
        {
            "question": "तरंग की आवृत्ति, तरंगदैर्ध्य और चाल के बीच क्या संबंध है?",
            "answer": "**चाल (v) = आवृत्ति (f) × तरंगदैर्ध्य (λ)**. जब कोई तरंग माध्यम बदलती है, तो उसकी चाल और तरंगदैर्ध्य बदल जाती है, लेकिन उसकी आवृत्ति स्थिर रहती है।",
            "icon": "fa-wave-square"
        },
        {
            "question": "किस घटना के कारण आकाश का रंग नीला और सूर्योदय/सूर्यास्त का लाल दिखाई देता है?",
            "answer": "**रेले प्रकीर्णन (Rayleigh Scattering)** के कारण। नीले प्रकाश की तरंगदैर्ध्य छोटी होती है और यह अन्य रंगों की तुलना में अधिक प्रकीर्णित होता है। सूर्योदय/सूर्यास्त के समय, प्रकाश लंबी दूरी तय करता है, जिससे नीला प्रकाश प्रकीर्णित होकर हट जाता है और लाल प्रकाश शेष रहता है।",
            "icon": "fa-cloud-sun"
        },
        {
            "question": "क्रांतिक कोण क्या है और पूर्ण आंतरिक परावर्तन से इसका क्या संबंध है?",
            "answer": "**क्रांतिक कोण (Critical Angle)** सघन माध्यम में वह आपतन कोण है जिसके लिए विरल माध्यम में अपवर्तन कोण 90° होता है। यदि आपतन कोण इससे अधिक हो जाता है, तो **पूर्ण आंतरिक परावर्तन (TIR)** होता है।",
            "icon": "fa-gem"
        }
    ]
}

traps_hi = {
    "title": "बचाव योग्य सामान्य परीक्षा भ्रम (Traps)",
    "items": [
        "<strong>भ्रम 1:</strong> यह मानना कि ध्वनि हवा की तुलना में निर्वात में तेजी से चलती है। याद रखें, ध्वनि एक यांत्रिक तरंग है और इसे माध्यम की आवश्यकता होती है; निर्वात में इसकी चाल <strong>शून्य</strong> होती है।",
        "<strong>भ्रम 2:</strong> ध्वनि की चाल पर तापमान के प्रभाव को लेकर भ्रमित होना। तापमान बढ़ने पर ध्वनि की चाल <strong>बढ़ती है</strong> (प्रति 1°C वृद्धि पर लगभग 0.61 मीटर/सेकंड) और यह स्थिर तापमान पर दबाव परिवर्तन से स्वतंत्र होती है।",
        "<strong>भ्रम 3:</strong> निकट दृष्टि दोष (Myopia) और दूर दृष्टि दोष (Hypermetropia) के सुधार में भ्रमित होना। निकट दृष्टि दोष में छवि रेटिना के सामने बनती है और <strong>अवतल लेंस</strong> का उपयोग किया जाता है। दूर दृष्टि दोष में छवि रेटिना के पीछे बनती है और <strong>उत्तल लेंस</strong> का उपयोग किया जाता है।",
        "<strong>भ्रम 4:</strong> यह मानना कि उच्च आवृत्ति का अर्थ ध्वनि की अधिक चाल है। आवृत्ति ध्वनि का <strong>तारत्व (Pitch)</strong> तय करती है, लेकिन किसी दिए गए माध्यम में सभी आवृत्तियों की तरंगें समान चाल से चलती हैं।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. तरंग गति और ध्वनि तरंग के लक्षण",
        "content": """<p>तरंगें पदार्थ को स्थानांतरित किए बिना ऊर्जा को एक बिंदु से दूसरे बिंदु पर स्थानांतरित करती हैं। इन्हें यांत्रिक (माध्यम की आवश्यकता होती है) और विद्युत चुंबकीय (माध्यम की आवश्यकता नहीं होती) में वर्गीकृत किया जाता है।</p>
        
        <!-- SVG Diagram 1: Wave Types -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .grid-label { font-family: 'Outfit', sans-serif; font-weight: 600; fill: var(--primary, #8e44ad); font-size: 13px; }
            .wave-line { fill: none; stroke: var(--primary, #8e44ad); stroke-width: 2.5px; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            
            
            
            
          </style>
          <text x="20" y="30" class="svg-title">तरंग प्रकार: अनुप्रस्थ (प्रकाश) बनाम अनुदैर्ध्य (ध्वनि)</text>
          
          <g transform="translate(10, 0)">
            <text x="50" y="55" class="grid-label">1. अनुप्रस्थ तरंग (जैसे, प्रकाश)</text>
            <path d="M 50 140 Q 90 80 130 140 T 210 140 T 290 140 T 370 140" class="wave-line" />
            <line x1="45" y1="140" x2="380" y2="140" stroke="rgba(128,128,128,0.3)" stroke-width="1.5" stroke-dasharray="4" />
            
            <circle cx="90" cy="80" r="4" fill="#e74c3c" />
            <text x="90" y="72" class="annot-text" text-anchor="middle">श्रृंग</text>
            <circle cx="170" cy="200" r="4" fill="#e74c3c" />
            <text x="170" y="215" class="annot-text" text-anchor="middle">गर्त</text>
            
            <line x1="90" y1="80" x2="250" y2="80" stroke="#2ecc71" stroke-width="1.5" stroke-dasharray="2" />
            <path d="M 90 80 L 100 77 M 90 80 L 100 83 M 250 80 L 240 77 M 250 80 L 240 83" stroke="#2ecc71" stroke-width="1.5" />
            <text x="170" y="95" class="annot-text" fill="#2ecc71" text-anchor="middle">तरंगदैर्ध्य (λ)</text>
            
            <line x1="250" y1="140" x2="250" y2="80" stroke="#e67e22" stroke-width="1.5" />
            <text x="258" y="115" class="annot-text" fill="#e67e22">आयाम (A)</text>
          </g>
          
          <g transform="translate(420, 0)">
            <text x="50" y="55" class="grid-label">2. अनुदैर्ध्य तरंग (जैसे, ध्वनि)</text>
            <g stroke="var(--primary, #8e44ad)" stroke-width="2">
              <line x1="70" y1="100" x2="70" y2="180" />
              <line x1="75" y1="100" x2="75" y2="180" />
              <line x1="80" y1="100" x2="80" y2="180" />
              <line x1="85" y1="100" x2="85" y2="180" />
              <line x1="110" y1="100" x2="110" y2="180" opacity="0.4" />
              <line x1="140" y1="100" x2="140" y2="180" opacity="0.4" />
              <line x1="170" y1="100" x2="170" y2="180" />
              <line x1="175" y1="100" x2="175" y2="180" />
              <line x1="180" y1="100" x2="180" y2="180" />
              <line x1="185" y1="100" x2="185" y2="180" />
              <line x1="210" y1="100" x2="210" y2="180" opacity="0.4" />
              <line x1="240" y1="100" x2="240" y2="180" opacity="0.4" />
              <line x1="270" y1="100" x2="270" y2="180" />
              <line x1="275" y1="100" x2="275" y2="180" />
              <line x1="280" y1="100" x2="280" y2="180" />
              <line x1="285" y1="100" x2="285" y2="180" />
            </g>
            <text x="78" y="202" class="annot-text" text-anchor="middle">संपीड़न</text>
            <text x="125" y="220" class="annot-text" text-anchor="middle">विरलन</text>
            <text x="178" y="202" class="annot-text" text-anchor="middle">संपीड़न</text>
            
            <line x1="77" y1="90" x2="177" y2="90" stroke="#2ecc71" stroke-width="1.5" />
            <path d="M 77 90 L 87 87 M 77 90 L 87 93 M 177 90 L 167 87 M 177 90 L 167 93" stroke="#2ecc71" stroke-width="1.5" />
            <text x="127" y="83" class="annot-text" fill="#2ecc71" text-anchor="middle">तरंगदैर्ध्य (λ)</text>
          </g>
        </svg>

        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>लक्षण</th>
                <th>ध्वनि तरंगें (हवा में)</th>
                <th>प्रकाश तरंगें</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>तरंग का प्रकार</strong></td>
                <td>अनुदैर्ध्य यांत्रिक (Longitudinal Mechanical)</td>
                <td>अनुप्रस्थ विद्युत चुंबकीय (Transverse EM)</td>
              </tr>
              <tr>
                <td><strong>माध्यम की आवश्यकता</strong></td>
                <td>हाँ (निर्वात में यात्रा नहीं कर सकती)</td>
                <td>नहीं (निर्वात में सबसे तेज चलती है)</td>
              </tr>
              <tr>
                <td><strong>चाल</strong></td>
                <td>~343 मीटर/सेकंड (20°C पर)</td>
                <td>3 × 10⁸ मीटर/सेकंड (निर्वात में)</td>
              </tr>
              <tr>
                <td><strong>कणों की गति की प्रकृति</strong></td>
                <td>तरंग संचरण के समानांतर (संपीड़न और विरलन)</td>
                <td>तरंग संचरण के लंबवत (श्रृंग और गर्त)</td>
              </tr>
              <tr>
                <td><strong>माध्यम के घनत्व का प्रभाव</strong></td>
                <td>ठोस में सबसे तेज, फिर द्रव में, गैस में सबसे धीमी</td>
                <td>निर्वात/गैस में सबसे तेज, ठोस में सबसे धीमी</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <p><strong>विभिन्न माध्यमों में ध्वनि की चाल:</strong> ध्वनि की चाल लाप्लास के सूत्र द्वारा दी जाती है: <code>v = √(γP/ρ)</code>. ध्वनि की चाल तापमान और आर्द्रता के सीधे आनुपातिक होती है, लेकिन स्थिर तापमान पर दबाव से स्वतंत्र होती है।</p>"""
    },
    {
        "title": "2. ध्वनिकी: परावर्तन, प्रतिध्वनि, सोनार और डॉप्लर प्रभाव",
        "content": """<p>ध्वनि तरंगों का परावर्तन, अपवर्तन, विवर्तन और व्यतिकरण होता है। कुछ प्रमुख घटनाएं निम्नलिखित हैं:</p>
        <ul>
          <li><strong>प्रतिध्वनि (Echo)</strong>: किसी दूरस्थ बाधा से परावर्तन के कारण ध्वनि की पुनरावृत्ति। हवा में स्पष्ट प्रतिध्वनि सुनने के लिए न्यूनतम दूरी <strong>~17.2 मीटर</strong> है (क्योंकि कान पर ध्वनि का प्रभाव 0.1 सेकंड तक रहता है)।</li>
          <li><strong>अनुरणन (Reverberation)</strong>: बार-बार परावर्तन के कारण ध्वनि का बने रहना। ध्वनि-अवशोषक सामग्रियों का उपयोग करके इसे कम किया जाता है।</li>
          <li><strong>सोनार (Sonar)</strong>: पानी के नीचे की वस्तुओं की स्थिति या गहराई मापने के लिए <strong>पराबैंगनी तरंगों (Ultrasonic waves - आवृत्ति > 20,000 Hz)</strong> का उपयोग करता है। <code>दूरी (d) = v × t / 2</code>.</li>
          <li><strong>डॉप्लर प्रभाव (Doppler Effect)</strong>: स्रोत और प्रेक्षक के बीच सापेक्ष गति के कारण तरंग की आवृत्ति में आभासी परिवर्तन। जब वे पास आते हैं, तो आभासी आवृत्ति बढ़ जाती है; दूर जाने पर घट जाती है।</li>
        </ul>"""
    },
    {
        "title": "3. प्रकाश: परावर्तन, गोलीय दर्पण और लेंस",
        "content": """<p>प्रकाश एक अनुप्रस्थ विद्युत चुंबकीय तरंग है। परावर्तन के नियम सभी प्रकार के दर्पणों पर लागू होते हैं:</p>
        
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>ऑप्टिकल तत्व</th>
                <th>बनने वाली छवि का प्रकार</th>
                <th>प्रमुख अनुप्रयोग</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>अवतल दर्पण (Concave Mirror)</strong></td>
                <td>वास्तविक और उल्टा (जब वस्तु F और P के बीच हो: आभासी और आवर्धित)</td>
                <td>दाढ़ी बनाने वाले दर्पण, सर्चलाइट, दंत चिकित्सक के दर्पण, सौर भट्टियां</td>
              </tr>
              <tr>
                <td><strong>उत्तल दर्पण (Convex Mirror)</strong></td>
                <td>हमेशा आभासी, सीधा और छोटा</td>
                <td>वाहनों में पीछे देखने के लिए (रियर-व्यू दर्पण - व्यापक क्षेत्र देता है)</td>
              </tr>
              <tr>
                <td><strong>उत्तल लेंस (Convex Lens)</strong></td>
                <td>वास्तविक और उल्टा (जब वस्तु फोकस के भीतर हो तो आभासी)</td>
                <td>आवर्धक कांच, कैमरा, सूक्ष्मदर्शी, दूर दृष्टि दोष का सुधार</td>
              </tr>
              <tr>
                <td><strong>अवतल लेंस (Concave Lens)</strong></td>
                <td>हमेशा आभासी, सीधा और छोटा</td>
                <td>फ्लैशलाइट, दरवाजे के छेद (Peephole), निकट दृष्टि दोष का सुधार</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <p><strong>दर्पण सूत्र:</strong> <code>1/f = 1/v + 1/u</code> | <strong>लेंस सूत्र:</strong> <code>1/f = 1/v - 1/u</code> | <strong>लेंस की क्षमता:</strong> <code>P = 1/f (मीटर में)</code> (मात्रक: डायोप्टर, D)।</p>"""
    },
    {
        "title": "4. अपवर्तन, पूर्ण आंतरिक परावर्तन और विक्षेपण",
        "content": """<p>अपवर्तन (Refraction) चाल में परिवर्तन के कारण प्रकाश के एक माध्यम से दूसरे माध्यम में जाने पर मुड़ने की घटना है। स्नेल का नियम: <code>n₁ sin(i) = n₂ sin(r)</code>.</p>
        
        <!-- SVG Diagram 2: Refraction & TIR -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .medium-label { font-family: 'Outfit', sans-serif; font-weight: 600; fill: var(--primary, #8e44ad); font-size: 13px; }
            .ray-line { fill: none; stroke-width: 2px; }
            .normal-line { stroke: rgba(128, 128, 128, 0.6); stroke-width: 1.5px; stroke-dasharray: 4; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            
            
            
          </style>
          <text x="20" y="30" class="svg-title">प्रकाश अपवर्तन, क्रांतिक कोण और पूर्ण आंतरिक परावर्तन (TIR)</text>
          
          <rect x="0" y="120" width="800" height="120" fill="rgba(52, 152, 219, 0.08)" />
          <line x1="0" y1="120" x2="800" y2="120" stroke="#3498db" stroke-width="2" />
          <text x="20" y="105" class="medium-label">विरल माध्यम (हवा)</text>
          <text x="20" y="145" class="medium-label">सघन माध्यम (पानी/कांच)</text>
          
          <line x1="200" y1="40" x2="200" y2="200" class="normal-line" />
          <line x1="400" y1="40" x2="400" y2="200" class="normal-line" />
          <line x1="600" y1="40" x2="600" y2="200" class="normal-line" />
          
          <g>
            <path d="M 120 180 L 200 120 L 250 50" fill="none" stroke="#e67e22" stroke-width="2" />
            <path d="M 160 150 L 158 142 M 160 150 L 150 152" stroke="#e67e22" stroke-width="2" />
            <path d="M 225 85 L 221 77 M 225 85 L 217 88" stroke="#e67e22" stroke-width="2" />
            <text x="180" y="115" class="annot-text">i</text>
            <text x="215" y="110" class="annot-text">r</text>
            <text x="200" y="215" class="annot-text" text-anchor="middle">1. अपवर्तन (i &lt; θc)</text>
          </g>
          
          <g>
            <path d="M 310 180 L 400 120 L 520 120" fill="none" stroke="#2ecc71" stroke-width="2.5" />
            <path d="M 355 150 L 353 142 M 355 150 L 345 152" stroke="#2ecc71" stroke-width="2" />
            <path d="M 460 120 L 450 115 M 460 120 L 450 125" stroke="#2ecc71" stroke-width="2" />
            <text x="375" y="110" class="annot-text">θc</text>
            <text x="415" y="105" class="annot-text">r = 90°</text>
            <text x="400" y="215" class="annot-text" text-anchor="middle">2. क्रांतिक कोण (r = 90°)</text>
          </g>
          
          <g>
            <path d="M 500 180 L 600 120 L 700 180" fill="none" stroke="#e74c3c" stroke-width="2.5" />
            <path d="M 550 150 L 548 142 M 550 150 L 540 152" stroke="#e74c3c" stroke-width="2" />
            <path d="M 650 150 L 642 152 M 650 150 L 648 142" stroke="#e74c3c" stroke-width="2" />
            <text x="575" y="110" class="annot-text">i &gt; θc</text>
            <text x="615" y="110" class="annot-text">r = i</text>
            <text x="600" y="215" class="annot-text" text-anchor="middle">3. TIR (i &gt; θc)</text>
          </g>
        </svg>

        <ul>
          <li><strong>पूर्ण आंतरिक परावर्तन (TIR)</strong>: जब प्रकाश सघन से विरल माध्यम में जाता है और आपतन कोण क्रांतिक कोण से अधिक होता है, तो प्रकाश उसी माध्यम में परावर्तित हो जाता है।
            <br><em>अनुप्रयोग:</em> हीरे का चमकना, ऑप्टिकल फाइबर (प्रकाश तंतु), रेगिस्तान में मरीचिका।
          </li>
          <li><strong>वर्ण-विक्षेपण (Dispersion)</strong>: प्रिज्म से गुजरने पर सफेद प्रकाश का अपने घटक रंगों (VIBGYOR) में विभाजित होना। बैंगनी सबसे अधिक झुकता है; लाल सबसे कम झुकता है।
            <br><em>इंद्रधनुष:</em> पानी की बूंदों के भीतर सूर्य के प्रकाश के विक्षेपण, अपवर्तन और आंतरिक परावर्तन के कारण बनता है।
          </li>
          <li><strong>प्रकीर्णन (Scattering)</strong>: छोटे कणों द्वारा प्रकाश को फैलाना। रेले प्रकीर्णन बताता है कि आकाश नीला क्यों है और खतरे के संकेत लाल क्यों होते हैं (लाल रंग सबसे कम फैलता है)।
          </li>
        </ul>"""
    },
    {
        "title": "5. मानव नेत्र दोष और सुधारात्मक लेंस",
        "content": """<p>मानव आंख रेटिना पर प्रकाश केंद्रित करने के लिए एक उत्तल क्रिस्टलीय लेंस का उपयोग करती है। सामान्य नेत्र दोष निम्नलिखित हैं:</p>
        
        <!-- SVG Diagram 3: Eye Defects -->
        <svg viewBox="0 0 800 280" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .defect-label { font-family: 'Outfit', sans-serif; font-weight: 600; fill: var(--primary, #8e44ad); font-size: 13px; }
            .eye-ball { fill: none; stroke: var(--text-dark, #2c3e50); stroke-width: 1.5px; }
            .lens-shape { fill: rgba(142, 68, 173, 0.2); stroke: var(--primary, #8e44ad); stroke-width: 1.5px; }
            .light-ray { fill: none; stroke: #e67e22; stroke-width: 1.5px; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 10px; fill: var(--text-dark, #2c3e50); }
            
            
            
            
          </style>
          <text x="20" y="25" class="svg-title">नेत्र दोष: मायोपिया बनाम हाइपरमेट्रोपिया और सुधारात्मक प्रकाशिकी</text>
          
          <g transform="translate(10, 0)">
            <text x="40" y="55" class="defect-label">A. मायोपिया (निकट दृष्टि दोष)</text>
            <path d="M 120 100 A 30 30 0 1 1 120 160 C 110 150 105 130 120 100 Z" class="eye-ball" />
            <path d="M 120 115 A 15 15 0 0 1 120 145 Z" class="lens-shape" />
            <path d="M 40 120 L 120 120 L 140 130 L 120 140 L 40 140" class="light-ray" />
            <circle cx="140" cy="130" r="3" fill="#e74c3c" />
            <text x="140" y="115" class="annot-text" text-anchor="middle">रेटिना के आगे फोकस</text>
            
            <g transform="translate(0, 100)">
              <path d="M 120 100 A 30 30 0 1 1 120 160 C 110 150 105 130 120 100 Z" class="eye-ball" />
              <path d="M 120 115 A 15 15 0 0 1 120 145 Z" class="lens-shape" />
              <path d="M 75 110 L 85 110 L 80 130 L 85 150 L 75 150 L 80 130 Z" fill="rgba(52,152,219,0.15)" stroke="#3498db" stroke-width="1.5" />
              <text x="80" y="105" class="annot-text" text-anchor="middle" fill="#3498db">अवतल लेंस</text>
              <path d="M 40 120 L 78 120 L 120 116 L 149 130 L 120 144 L 78 140 L 40 140" class="light-ray" />
              <circle cx="149" cy="130" r="3" fill="#2ecc71" />
              <text x="150" y="115" class="annot-text" text-anchor="middle">रेटिना पर फोकस</text>
            </g>
          </g>
          
          <g transform="translate(410, 0)">
            <text x="40" y="55" class="defect-label">B. हाइपरमेट्रोपिया (दूर दृष्टि दोष)</text>
            <path d="M 120 100 A 30 30 0 1 1 120 160 C 110 150 105 130 120 100 Z" class="eye-ball" />
            <path d="M 120 115 A 15 15 0 0 1 120 145 Z" class="lens-shape" />
            <path d="M 40 125 L 120 125 L 160 130 L 120 135 L 40 135" class="light-ray" />
            <circle cx="160" cy="130" r="3" fill="#e74c3c" />
            <text x="160" y="115" class="annot-text" text-anchor="middle">रेटिना के पीछे फोकस</text>
            
            <g transform="translate(0, 100)">
              <path d="M 120 100 A 30 30 0 1 1 120 160 C 110 150 105 130 120 100 Z" class="eye-ball" />
              <path d="M 120 115 A 15 15 0 0 1 120 145 Z" class="lens-shape" />
              <path d="M 75 130 Q 80 110 85 130 T 75 130 Z" fill="rgba(46,204,113,0.15)" stroke="#2ecc71" stroke-width="1.5" transform="rotate(90 80 130)" />
              <text x="80" y="105" class="annot-text" text-anchor="middle" fill="#2ecc71">उत्तल लेंस</text>
              <path d="M 40 125 L 78 125 L 120 122 L 149 130 L 120 138 L 78 135 L 40 135" class="light-ray" />
              <circle cx="149" cy="130" r="3" fill="#2ecc71" />
              <text x="150" y="115" class="annot-text" text-anchor="middle">रेटिना पर फोकस</text>
            </g>
          </g>
        </svg>
        
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>दोष</th>
                <th>विवरण</th>
                <th>छवि कहाँ बनती है</th>
                <th>सुधारक लेंस</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>निकट दृष्टि दोष (Myopia)</strong></td>
                <td>निकट की वस्तुएं स्पष्ट दिखती हैं, दूर की नहीं</td>
                <td>रेटिना के सामने (In front)</td>
                <td><strong>अवतल लेंस (Concave Lens)</strong></td>
              </tr>
              <tr>
                <td><strong>दूर दृष्टि दोष (Hypermetropia)</strong></td>
                <td>दूर की वस्तुएं स्पष्ट दिखती हैं, निकट की नहीं</td>
                <td>रेटिना के पीछे (Behind)</td>
                <td><strong>उत्तल लेंस (Convex Lens)</strong></td>
              </tr>
              <tr>
                <td><strong>जरा दृष्टि दोष (Presbyopia)</strong></td>
                <td>उम्र बढ़ने के कारण समंजन क्षमता में कमी</td>
                <td>रेटिना के पीछे</td>
                <td><strong>द्विफोकसी लेंस (Bifocal Lens)</strong></td>
              </tr>
              <tr>
                <td><strong>अबिन्दुकता (Astigmatism)</strong></td>
                <td>क्षैतिज और ऊर्ध्वाडर रेखाओं पर एक साथ ध्यान केंद्रित नहीं कर पाना</td>
                <td>विकृत फोकस</td>
                <td><strong>बेलनाकार लेंस (Cylindrical Lens)</strong></td>
              </tr>
            </tbody>
          </table>
        </div>"""
    }
]

# ----------------- PRACTICE QUESTIONS (50 Qs) -----------------
# Generate 50 conceptual questions on Sound & Light
practice_questions = [
    {
        "q": "What type of wave is sound in air?",
        "q_hi": "हवा में ध्वनि किस प्रकार की तरंग है?",
        "opts": ["Transverse Electromagnetic", "Longitudinal Mechanical", "Transverse Mechanical", "Stationary Wave"],
        "opts_hi": ["अनुप्रस्थ विद्युत चुंबकीय", "अनुदैर्ध्य यांत्रिक", "अनुप्रस्थ यांत्रिक", "अप्रगामी तरंग"],
        "ans": 1,
        "sol": "Sound waves in air are longitudinal mechanical waves, consisting of compressions and rarefactions.",
        "sol_hi": "हवा में ध्वनि तरंगें अनुदैर्ध्य यांत्रिक तरंगें होती हैं, जिनमें संपीड़न और विरलन शामिल होते हैं।"
    },
    {
        "q": "Which of the following properties of sound determines its pitch?",
        "q_hi": "ध्वनि का निम्नलिखित में से कौन सा गुण उसका तारत्व (Pitch) निर्धारित करता है?",
        "opts": ["Amplitude", "Frequency", "Wavelength", "Velocity"],
        "opts_hi": ["आयाम (Amplitude)", "आवृत्ति (Frequency)", "तरंगदैर्ध्य", "वेग"],
        "ans": 1,
        "sol": "The pitch of sound depends on its frequency. Higher frequency corresponds to higher pitch.",
        "sol_hi": "ध्वनि का तारत्व उसकी आवृत्ति पर निर्भर करता है। उच्च आवृत्ति का अर्थ उच्च तारत्व होता है।"
    },
    {
        "q": "The speed of sound is maximum in which of the following media?",
        "q_hi": "निम्नलिखित में से किस माध्यम में ध्वनि की चाल अधिकतम होती है?",
        "opts": ["Air", "Water", "Steel", "Vacuum"],
        "opts_hi": ["हवा", "पानी", "इस्पात (Steel)", "निर्वात"],
        "ans": 2,
        "sol": "Sound travels fastest in solids due to high elasticity and density. Hence, it is maximum in steel.",
        "sol_hi": "उच्च प्रत्यास्थता और घनत्व के कारण ध्वनि ठोस पदार्थों में सबसे तेज चलती है। अतः यह इस्पात में अधिकतम होगी।"
    },
    {
        "q": "What is the minimum distance required between the source of sound and the obstacle to hear a clear echo at 20°C?",
        "q_hi": "20°C पर स्पष्ट प्रतिध्वनि (Echo) सुनने के लिए ध्वनि स्रोत और बाधा के बीच आवश्यक न्यूनतम दूरी क्या है?",
        "opts": ["9.1 meters", "17.2 meters", "34.4 meters", "10.0 meters"],
        "opts_hi": ["9.1 मीटर", "17.2 मीटर", "34.4 मीटर", "10.0 मीटर"],
        "ans": 1,
        "sol": "Persistence of hearing is 0.1s. Total distance traveled by sound must be v * 0.1 = 344 * 0.1 = 34.4m. The minimum distance to obstacle is half of this, i.e., 17.2m.",
        "sol_hi": "श्रवण की दृढ़ता 0.1 सेकंड होती है। ध्वनि द्वारा तय की गई कुल दूरी v * 0.1 = 344 * 0.1 = 34.4 मीटर होनी चाहिए। बाधा तक की न्यूनतम दूरी इसकी आधी यानी 17.2 मीटर है।"
    },
    {
        "q": "The unit of measurement of loudness of sound is:",
        "q_hi": "ध्वनि की प्रबलता मापने की इकाई क्या है?",
        "opts": ["Hertz", "Decibel", "Meter", "Pascal"],
        "opts_hi": ["हर्ट्ज़", "डेसीबल", "मीटर", "पास्कल"],
        "ans": 1,
        "sol": "Loudness of sound is measured in decibels (dB), which is a logarithmic scale.",
        "sol_hi": "ध्वनि की प्रबलता को डेसीबल (dB) में मापा जाता है, जो एक लघुगणकीय पैमाना है।"
    },
    {
        "q": "Light is which type of wave?",
        "q_hi": "प्रकाश किस प्रकार की तरंग है?",
        "opts": ["Longitudinal mechanical", "Transverse electromagnetic", "Longitudinal electromagnetic", "Elastic wave"],
        "opts_hi": ["अनुदैर्ध्य यांत्रिक", "अनुप्रस्थ विद्युत चुंबकीय", "अनुदैर्ध्य विद्युत चुंबकीय", "प्रत्यास्थ तरंग"],
        "ans": 1,
        "sol": "Light waves are transverse electromagnetic waves, consisting of oscillating electric and magnetic fields.",
        "sol_hi": "प्रकाश तरंगें अनुप्रस्थ विद्युत चुंबकीय तरंगें होती हैं, जिनमें कंपायमान विद्युत और चुंबकीय क्षेत्र होते हैं।"
    },
    {
        "q": "Which color of visible light has the longest wavelength?",
        "q_hi": "दृश्य प्रकाश के किस रंग की तरंगदैर्ध्य सबसे लंबी होती है?",
        "opts": ["Violet", "Blue", "Green", "Red"],
        "opts_hi": ["बैंगनी", "नीला", "हरा", "लाल"],
        "ans": 3,
        "sol": "Red light has the longest wavelength (~700 nm) and lowest frequency in the visible spectrum.",
        "sol_hi": "लाल प्रकाश की दृश्य स्पेक्ट्रम में तरंगदैर्ध्य सबसे लंबी (~700 nm) और आवृत्ति सबसे कम होती है।"
    },
    {
        "q": "Which optical phenomenon explains the sparkling of diamonds?",
        "q_hi": "कौन सी ऑप्टिकल घटना हीरे के चमकने की व्याख्या करती है?",
        "opts": ["Refraction", "Dispersion", "Total Internal Reflection", "Scattering"],
        "opts_hi": ["अपवर्तन", "वर्ण-विक्षेपण", "पूर्ण आंतरिक परावर्तन (TIR)", "प्रकीर्णन"],
        "ans": 2,
        "sol": "The sparkle of diamond is due to Total Internal Reflection (TIR) caused by its high refractive index (2.42) and small critical angle (24.4°).",
        "sol_hi": "हीरे की चमक उसके उच्च अपवर्तनांक (2.42) और छोटे क्रांतिक कोण (24.4°) के कारण होने वाले पूर्ण आंतरिक परावर्तन (TIR) के कारण होती है।"
    },
    {
        "q": "A rear-view mirror used in vehicles is a:",
        "q_hi": "वाहनों में पीछे देखने के लिए उपयोग किया जाने वाला दर्पण होता है:",
        "opts": ["Plane mirror", "Concave mirror", "Convex mirror", "Plano-concave mirror"],
        "opts_hi": ["समतल दर्पण", "अवतल दर्पण", "उत्तल दर्पण", "समतल-अवतल दर्पण"],
        "ans": 2,
        "sol": "Convex mirrors are used as rear-view mirrors because they form erect, diminished images and provide a wider field of view.",
        "sol_hi": "उत्तल दर्पणों का उपयोग पीछे देखने वाले दर्पणों के रूप में किया जाता है क्योंकि वे सीधा, छोटा प्रतिबिंब बनाते हैं और एक व्यापक दृष्टि क्षेत्र प्रदान करते हैं।"
    },
    {
        "q": "Myopia (nearsightedness) can be corrected by using a lens of which type?",
        "q_hi": "निकट दृष्टि दोष (Myopia) को किस प्रकार के लेंस का उपयोग करके ठीक किया जा सकता है?",
        "opts": ["Convex lens", "Concave lens", "Cylindrical lens", "Bifocal lens"],
        "opts_hi": ["उत्तल लेंस", "अवतल लेंस", "बेलनाकार लेंस", "द्विफोकसी लेंस"],
        "ans": 1,
        "sol": "Myopia is corrected using a diverging (concave) lens, which moves the focus back onto the retina.",
        "sol_hi": "निकट दृष्टि दोष को एक अपसारी (अवतल) लेंस का उपयोग करके ठीक किया जाता है, जो फोकस को पीछे रेटिना पर ले जाता है।"
    },
    {
        "q": "Why is the sky blue in color?",
        "q_hi": "आकाश का रंग नीला क्यों दिखाई देता है?",
        "opts": ["Reflection of sea water", "Rayleigh scattering of light", "Refraction of light in atmosphere", "Dispersion of light"],
        "opts_hi": ["समुद्र के पानी का परावर्तन", "प्रकाश का रेले प्रकीर्णन", "वायुमंडल में प्रकाश का अपवर्तन", "प्रकाश का वर्ण-विक्षेपण"],
        "ans": 1,
        "sol": "The blue color of the sky is due to Rayleigh scattering. Shorter wavelengths (blue/violet) scatter much more than longer ones (red).",
        "sol_hi": "आकाश का नीला रंग रेले प्रकीर्णन के कारण होता है। छोटी तरंगदैर्ध्य (नीला/बैंगनी) लंबी तरंगदैर्ध्य (लाल) की तुलना में बहुत अधिक प्रकीर्णित होती हैं।"
    },
    {
        "q": "In which medium does light travel fastest?",
        "q_hi": "प्रकाश किस माध्यम में सबसे तेजी से यात्रा करता है?",
        "opts": ["Air", "Water", "Glass", "Vacuum"],
        "opts_hi": ["हवा", "पानी", "कांच", "निर्वात"],
        "ans": 3,
        "sol": "Light travels fastest in a vacuum, with a speed of approximately 3 × 10⁸ m/s.",
        "sol_hi": "प्रकाश निर्वात में सबसे तेजी से यात्रा करता है, जिसकी गति लगभग 3 × 10⁸ मीटर/सेकंड होती है।"
    },
    {
        "q": "Which type of mirror is used by dentists to see large images of teeth?",
        "q_hi": "दंत चिकित्सकों द्वारा दांतों की बड़ी छवियां देखने के लिए किस प्रकार के दर्पण का उपयोग किया जाता है?",
        "opts": ["Convex mirror", "Concave mirror", "Plane mirror", "Parabolic mirror"],
        "opts_hi": ["उत्तल दर्पण", "अवतल दर्पण", "समतल दर्पण", "परवलयिक दर्पण"],
        "ans": 1,
        "sol": "Dentists use concave mirrors because they form magnified virtual images when the object (tooth) is kept close (within focus).",
        "sol_hi": "दंत चिकित्सक अवतल दर्पण का उपयोग करते हैं क्योंकि जब वस्तु (दांत) को पास (फोकस के भीतर) रखा जाता है तो वे आवर्धित आभासी प्रतिबिंब बनाते हैं।"
    },
    {
        "q": "The power of a lens is measured in:",
        "q_hi": "लेंस की क्षमता (Power) किसमें मापी जाती है?",
        "opts": ["Watts", "Joules", "Dioptres", "Lumen"],
        "opts_hi": ["वाट", "जूल", "डायोप्टर", "ल्यूमेन"],
        "ans": 2,
        "sol": "The power of a lens is defined as P = 1/f (in meters), and its unit is Dioptre (D).",
        "sol_hi": "लेंस की क्षमता को P = 1/f (मीटर में) के रूप में परिभाषित किया जाता है, और इसका मात्रक डायोप्टर (D) है।"
    },
    {
        "q": "What happens to the speed of sound when the temperature of air increases?",
        "q_hi": "हवा का तापमान बढ़ने पर ध्वनि की चाल पर क्या प्रभाव पड़ता है?",
        "opts": ["Decreases", "Increases", "Remains constant", "First decreases then increases"],
        "opts_hi": ["घटती है", "बढ़ती है", "स्थिर रहती है", "पहले घटती है फिर बढ़ती है"],
        "ans": 1,
        "sol": "The speed of sound in air increases with temperature. Speed is proportional to the square root of absolute temperature (v ∝ √T).",
        "sol_hi": "हवा में ध्वनि की चाल तापमान के साथ बढ़ती है। चाल परम तापमान के वर्गमूल के समानुपाती होती है (v ∝ √T)।"
    },
    {
        "q": "The persistence of vision for human eye is about:",
        "q_hi": "मानव नेत्र के लिए दृष्टि की दृढ़ता (Persistence of Vision) लगभग कितनी होती है?",
        "opts": ["1/10th of a second", "1/16th of a second", "1/2nd of a second", "1/5th of a second"],
        "opts_hi": ["1/10 सेकंड", "1/16 सेकंड", "1/2 सेकंड", "1/5 सेकंड"],
        "ans": 1,
        "sol": "Persistence of vision is approximately 1/16th of a second (1/10s is for persistence of hearing).",
        "sol_hi": "दृष्टि की दृढ़ता लगभग 1/16 सेकंड होती है (1/10 सेकंड ध्वनि/श्रवण की दृढ़ता के लिए है)।"
    },
    {
        "q": "Which lens is used to correct Hypermetropia (farsightedness)?",
        "q_hi": "दूर दृष्टि दोष (Hypermetropia) को ठीक करने के लिए किस लेंस का उपयोग किया जाता है?",
        "opts": ["Concave lens", "Convex lens", "Bifocal lens", "Cylindrical lens"],
        "opts_hi": ["अवतल लेंस", "उत्तल लेंस", "द्विफोकसी लेंस", "बेलनाकार लेंस"],
        "ans": 1,
        "sol": "Hypermetropia is corrected using a converging (convex) lens, which helps focus nearby light rays onto the retina.",
        "sol_hi": "दूर दृष्टि दोष को ठीक करने के लिए एक अभिसारी (उत्तल) लेंस का उपयोग किया जाता है, जो पास की प्रकाश किरणों को रेटिना पर केंद्रित करने में मदद करता है।"
    },
    {
        "q": "The phenomenon of splitting white light into seven colors is called:",
        "q_hi": "श्वेत प्रकाश के सात रंगों में विभाजित होने की घटना कहलाती है:",
        "opts": ["Refraction", "Reflection", "Dispersion", "Diffraction"],
        "opts_hi": ["अपवर्तन", "परावर्तन", "वर्ण-विक्षेपण (Dispersion)", "विवर्तन"],
        "ans": 2,
        "sol": "Dispersion is the splitting of white light into its component spectrum when it passes through a refracting medium like a prism.",
        "sol_hi": "वर्ण-विक्षेपण प्रिज्म जैसे अपवर्तक माध्यम से गुजरने पर श्वेत प्रकाश के अपने घटक रंगों के स्पेक्ट्रम में विभाजित होने की घटना है।"
    },
    {
        "q": "Ultrasonic waves have a frequency:",
        "q_hi": "पराबैंगनी (अल्ट्रासोनिक) तरंगों की आवृत्ति होती है:",
        "opts": ["Below 20 Hz", "Between 20 Hz and 20,000 Hz", "Above 20,000 Hz", "Above 10⁶ Hz"],
        "opts_hi": ["20 हर्ट्ज़ से नीचे", "20 हर्ट्ज़ और 20,000 हर्ट्ज़ के बीच", "20,000 हर्ट्ज़ से ऊपर", "10⁶ हर्ट्ज़ से ऊपर"],
        "ans": 2,
        "sol": "Ultrasonic waves are sound waves with frequencies above the upper audible limit of human hearing, which is 20,000 Hz.",
        "sol_hi": "पराबैंगनी तरंगें वे ध्वनि तरंगें हैं जिनकी आवृत्ति मानव सुनने की ऊपरी सीमा (20,000 हर्ट्ज़) से अधिक होती है।"
    },
    {
        "q": "Which waves are used in Sonar to detect obstacles or measure depth?",
        "q_hi": "बाधाओं का पता लगाने या गहराई मापने के लिए सोनार (Sonar) में किन तरंगों का उपयोग किया जाता है?",
        "opts": ["Infrasonic waves", "Radio waves", "Ultrasonic waves", "Microwaves"],
        "opts_hi": ["अपश्रव्य (Infrasonic) तरंगें", "रेडियो तरंगें", "पराबैंगनी (Ultrasonic) तरंगें", "सूक्ष्म तरंगें"],
        "ans": 2,
        "sol": "Sonar devices use ultrasonic waves due to their high frequency, short wavelength, and ability to penetrate deep into water without much deviation.",
        "sol_hi": "सोनार उपकरण उच्च आवृत्ति, कम तरंगदैर्ध्य और बिना अधिक विचलन के पानी में गहराई तक प्रवेश करने की क्षमता के कारण पराबैंगनी तरंगों का उपयोग करते हैं।"
    },
    {
        "q": "Astigmatism is corrected using which type of lens?",
        "q_hi": "अबिन्दुकता (Astigmatism) को किस प्रकार के लेंस का उपयोग करके ठीक किया जाता है?",
        "opts": ["Bifocal lens", "Cylindrical lens", "Concave lens", "Convex lens"],
        "opts_hi": ["द्विफोकसी लेंस", "बेलनाकार लेंस", "अवतल लेंस", "उत्तल लेंस"],
        "ans": 1,
        "sol": "Astigmatism, caused by irregular curvature of cornea or lens, is corrected using cylindrical lenses.",
        "sol_hi": "कॉर्निया या लेंस की अनियमित वक्रता के कारण होने वाले अबिन्दुकता दोष को बेलनाकार लेंस का उपयोग करके ठीक किया जाता है।"
    },
    {
        "q": "What is the frequency range of audible sound waves for humans?",
        "q_hi": "मनुष्यों के लिए श्रव्य ध्वनि तरंगों की आवृत्ति सीमा क्या है?",
        "opts": ["0 to 20 Hz", "20 Hz to 20 kHz", "20 kHz to 20 MHz", "Above 20 kHz"],
        "opts_hi": ["0 से 20 हर्ट्ज़", "20 हर्ट्ज़ से 20 किलोहर्ट्ज़", "20 किलोहर्ट्ज़ से 20 मेगाहर्ट्ज़", "20 किलोहर्ट्ज़ से ऊपर"],
        "ans": 1,
        "sol": "The human ear can detect frequencies in the range of 20 Hz to 20,000 Hz (20 kHz).",
        "sol_hi": "मानव कान 20 हर्ट्ज़ से 20,000 हर्ट्ज़ (20 किलोहर्ट्ज़) की सीमा में आवृत्तियों का पता लगा सकता है।"
    },
    {
        "q": "A virtual, erect, and magnified image can be formed by a concave mirror when the object is placed:",
        "q_hi": "अवतल दर्पण द्वारा एक आभासी, सीधा और आवर्धित प्रतिबिंब तब बन सकता है जब वस्तु रखी हो:",
        "opts": ["At Focus (F)", "Between Focus (F) and Pole (P)", "At Center of Curvature (C)", "Beyond Center of Curvature"],
        "opts_hi": ["फोकस (F) पर", "फोकस (F) और ध्रुव (P) के बीच", "वक्रता केंद्र (C) पर", "वक्रता केंद्र से परे"],
        "ans": 1,
        "sol": "When the object is placed close to a concave mirror (between F and P), a virtual, erect, and magnified image is formed behind the mirror.",
        "sol_hi": "जब वस्तु को अवतल दर्पण के करीब (F और P के बीच) रखा जाता है, तो दर्पण के पीछे एक आभासी, सीधा और आवर्धित प्रतिबिंब बनता है।"
    },
    {
        "q": "The refractive index of water is 1.33. What does this mean?",
        "q_hi": "पानी का अपवर्तनांक 1.33 है। इसका क्या अर्थ है?",
        "opts": ["Speed of light is 1.33 times faster in water than vacuum", "Speed of light is 1.33 times slower in water than vacuum", "Light bends by 1.33 degrees", "None of the above"],
        "opts_hi": ["पानी में प्रकाश की गति निर्वात से 1.33 गुना तेज है", "पानी में प्रकाश की गति निर्वात से 1.33 गुना धीमी है", "प्रकाश 1.33 डिग्री झुकता है", "उपरोक्त में से कोई नहीं"],
        "ans": 1,
        "sol": "Refractive index n = c/v. Thus, speed of light in water v = c / 1.33, making it 1.33 times slower in water than in a vacuum.",
        "sol_hi": "अपवर्तनांक n = c/v होता है। इस प्रकार, पानी में प्रकाश की गति v = c / 1.33 होती है, जो इसे निर्वात की तुलना में पानी में 1.33 गुना धीमा बनाती है।"
    },
    {
        "q": "Which optical fibers work on the principle of:",
        "q_hi": "ऑप्टिकल फाइबर (प्रकाश तंतु) किस सिद्धांत पर कार्य करते हैं?",
        "opts": ["Scattering of light", "Total Internal Reflection", "Refraction of light", "Interference of light"],
        "opts_hi": ["प्रकाश का प्रकीर्णन", "पूर्ण आंतरिक परावर्तन (TIR)", "प्रकाश का अपवर्तन", "प्रकाश का व्यतिकरण"],
        "ans": 1,
        "sol": "Optical fibers transmit light signals over long distances with minimal loss using the principle of Total Internal Reflection (TIR).",
        "sol_hi": "ऑप्टिकल फाइबर पूर्ण आंतरिक परावर्तन (TIR) के सिद्धांत का उपयोग करके न्यूनतम नुकसान के साथ लंबी दूरी तक प्रकाश संकेतों को प्रसारित करते हैं।"
    },
    {
        "q": "What color is observed at the top of a primary rainbow?",
        "q_hi": "प्राथमिक इंद्रधनुष के शीर्ष पर कौन सा रंग दिखाई देता है?",
        "opts": ["Violet", "Red", "Green", "Yellow"],
        "opts_hi": ["बैंगनी", "लाल", "हरा", "पीला"],
        "ans": 1,
        "sol": "In a primary rainbow, red light emerges at the top (outer edge) at an angle of 42°, and violet at the bottom (inner edge) at 40°.",
        "sol_hi": "प्राथमिक इंद्रधनुष में, लाल प्रकाश शीर्ष (बाहरी किनारे) पर 42° के कोण पर और बैंगनी रंग नीचे (आंतरिक किनारे) पर 40° के कोण पर दिखाई देता है।"
    },
    {
        "q": "An apparent change in frequency of sound due to relative motion of source and observer is called:",
        "q_hi": "स्रोत और प्रेक्षक की सापेक्ष गति के कारण ध्वनि की आवृत्ति में आभासी परिवर्तन कहलाता है:",
        "opts": ["Raman Effect", "Doppler Effect", "Zeeman Effect", "Tyndall Effect"],
        "opts_hi": ["रमन प्रभाव", "डॉप्लर प्रभाव (Doppler Effect)", "जीमान प्रभाव", "टिंडल प्रभाव"],
        "ans": 1,
        "sol": "The Doppler Effect is the change in frequency of a wave in relation to an observer who is moving relative to the wave source.",
        "sol_hi": "डॉप्लर प्रभाव तरंग के स्रोत के सापेक्ष गतिमान प्रेक्षक के संबंध में तरंग की आवृत्ति में होने वाला परिवर्तन है।"
    },
    {
        "q": "Which of the following is independent of pressure changes in a gas?",
        "q_hi": "निम्नलिखित में से क्या किसी गैस में दबाव परिवर्तन से स्वतंत्र होता है?",
        "opts": ["Density of gas", "Speed of sound in gas", "Volume of gas", "Boiling point of gas"],
        "opts_hi": ["गैस का घनत्व", "गैस में ध्वनि की चाल", "गैस का आयतन", "गैस का क्वथनांक"],
        "ans": 1,
        "sol": "At a constant temperature, the speed of sound in a gas is independent of changes in pressure.",
        "sol_hi": "स्थिर तापमान पर, किसी गैस में ध्वनि की चाल दबाव में परिवर्तनों से स्वतंत्र होती है।"
    },
    {
        "q": "The speed of light in vacuum is approximately:",
        "q_hi": "निर्वात में प्रकाश की चाल लगभग कितनी होती है?",
        "opts": ["3 × 10⁵ m/s", "3 × 10⁸ m/s", "3 × 10¹⁰ m/s", "340 m/s"],
        "opts_hi": ["3 × 10⁵ मीटर/सेकंड", "3 × 10⁸ मीटर/सेकंड", "3 × 10¹⁰ मीटर/सेकंड", "340 मीटर/सेकंड"],
        "ans": 1,
        "sol": "The speed of light in a vacuum is exactly 299,792,458 m/s, rounded to 3 × 10⁸ m/s.",
        "sol_hi": "निर्वात में प्रकाश की चाल लगभग 3 × 10⁸ मीटर/सेकंड (3 लाख किमी/सेकंड) होती है।"
    },
    {
        "q": "If a wave goes from a rarer to a denser medium, what happens to its wavelength?",
        "q_hi": "यदि कोई तरंग विरल से सघन माध्यम में जाती है, तो उसकी तरंगदैर्ध्य पर क्या प्रभाव पड़ता है?",
        "opts": ["Increases", "Decreases", "Remains same", "Doubles"],
        "opts_hi": ["बढ़ती है", "घटती है", "स्थिर रहती है", "दोगुनी होती है"],
        "ans": 1,
        "sol": "In a denser medium, wave speed decreases. Since frequency remains constant, wavelength must decrease (v = fλ).",
        "sol_hi": "सघन माध्यम में तरंग की चाल कम हो जाती है। चूंकि आवृत्ति स्थिर रहती है, इसलिए तरंगदैर्ध्य को भी कम होना चाहिए (v = fλ)।"
    },
    {
        "q": "Which defect of vision is caused by the gradual weakening of ciliary muscles with aging?",
        "q_hi": "बुढ़ापे में सिलियरी मांसपेशियों के धीरे-धीरे कमजोर होने के कारण दृष्टि का कौन सा दोष होता है?",
        "opts": ["Myopia", "Hypermetropia", "Presbyopia", "Astigmatism"],
        "opts_hi": ["निकट दृष्टि दोष", "दूर दृष्टि दोष", "जरा दृष्टि दोष (Presbyopia)", "अबिन्दुकता"],
        "ans": 2,
        "sol": "Presbyopia is an age-related loss of near-focusing ability, corrected using bifocal lenses.",
        "sol_hi": "जरा दृष्टि दोष (Presbyopia) उम्र से संबंधित निकट-फोकस करने की क्षमता का ह्रास है, जिसे द्विफोकसी लेंस का उपयोग करके ठीक किया जाता है।"
    },
    {
        "q": "The focal length of a plane mirror is:",
        "q_hi": "समतल दर्पण की फोकस दूरी (Focal Length) होती है:",
        "opts": ["Zero", "One", "Infinity", "Negative"],
        "opts_hi": ["शून्य", "एक", "अनंत", "ऋणात्मक"],
        "ans": 2,
        "sol": "A plane mirror has no curvature, so its focal length is infinite. Its power is zero.",
        "sol_hi": "समतल दर्पण में कोई वक्रता नहीं होती है, इसलिए इसकी फोकस दूरी अनंत होती है। इसकी क्षमता शून्य होती है।"
    },
    {
        "q": "An echo is heard only when the reflected sound reaches our ear after a interval of at least:",
        "q_hi": "प्रतिध्वनि तभी सुनाई देती है जब परावर्तित ध्वनि हमारे कान तक कम से कम कितने समय के अंतराल के बाद पहुंचे?",
        "opts": ["0.01 seconds", "0.1 seconds", "0.5 seconds", "1 second"],
        "opts_hi": ["0.01 सेकंड", "0.1 सेकंड", "0.5 सेकंड", "1 सेकंड"],
        "ans": 1,
        "sol": "The persistence of hearing for human ears is 0.1 seconds. Any reflected sound arriving before this is merged with the original sound.",
        "sol_hi": "मानव कान के लिए श्रवण की दृढ़ता 0.1 सेकंड होती है। इससे पहले पहुंचने वाली कोई भी परावर्तित ध्वनि मूल ध्वनि में मिल जाती है।"
    },
    {
        "q": "Which type of waves cannot travel through vacuum?",
        "q_hi": "किस प्रकार की तरंगें निर्वात में यात्रा नहीं कर सकती हैं?",
        "opts": ["Light waves", "X-rays", "Sound waves", "Radio waves"],
        "opts_hi": ["प्रकाश तरंगें", "एक्स-रे", "ध्वनि तरंगें", "रेдио तरंगें"],
        "ans": 2,
        "sol": "Sound waves are mechanical waves and require a medium to travel. Electromagnetic waves (light, X-rays, radio) can travel in vacuum.",
        "sol_hi": "ध्वनि तरंगें यांत्रिक तरंगें हैं और इन्हें यात्रा के लिए माध्यम चाहिए। विद्युत चुंबकीय तरंगें (प्रकाश, एक्स-रे, रेडियो) निर्वात में यात्रा कर सकती हैं।"
    },
    {
        "q": "A lens has a focal length of +50 cm. What is its power?",
        "q_hi": "एक लेंस की फोकस दूरी +50 सेमी है। इसकी क्षमता (Power) क्या है?",
        "opts": ["+2 D", "-2 D", "+0.5 D", "+5 D"],
        "opts_hi": ["+2 D", "-2 D", "+0.5 D", "+5 D"],
        "ans": 0,
        "sol": "f = +50 cm = +0.5 m. Power P = 1 / f = 1 / 0.5 = +2 Dioptres. It is a convex lens.",
        "sol_hi": "f = +50 सेमी = +0.5 मीटर। क्षमता P = 1 / f = 1 / 0.5 = +2 डायोप्टर। यह एक उत्तल लेंस है।"
    },
    {
        "q": "The sky looks black to an astronaut in space because:",
        "q_hi": "अंतरिक्ष में अंतरिक्ष यात्री को आकाश काला दिखाई देता है क्योंकि:",
        "opts": ["There is no light in space", "There is no atmosphere to scatter light", "Space absorbs all light", "Astronauts wear black helmets"],
        "opts_hi": ["अंतरिक्ष में कोई प्रकाश नहीं है", "प्रकाश को प्रकीर्णित करने के लिए कोई वायुमंडल नहीं है", "अंतरिक्ष सभी प्रकाश को अवशोषित करता है", "अंतरिक्ष यात्री काले हेलमेट पहनते हैं"],
        "ans": 1,
        "sol": "Without an atmosphere, there are no particles to scatter sunlight. Hence, space appears black.",
        "sol_hi": "वायुमंडल के बिना, सूर्य के प्रकाश को प्रकीर्णित करने के लिए कोई कण नहीं होते हैं। इसलिए, अंतरिक्ष काला दिखाई देता है।"
    },
    {
        "q": "Which mirror is used as a headlamp reflector in cars?",
        "q_hi": "कारों के हेडलैंप परावर्तक के रूप में किस दर्पण का उपयोग किया जाता है?",
        "opts": ["Convex mirror", "Concave mirror", "Plane mirror", "Cylindrical mirror"],
        "opts_hi": ["उत्तल दर्पण", "अवतल दर्पण", "समतल दर्पण", "बेलनाकार दर्पण"],
        "ans": 1,
        "sol": "Concave mirrors are used in car headlights. The bulb is placed at the focus to produce a powerful parallel beam of light.",
        "sol_hi": "कार की हेडलाइट्स में अवतल दर्पण का उपयोग किया जाता है। शक्तिशाली समानांतर किरण पुंज उत्पन्न करने के लिए बल्ब को फोकस पर रखा जाता है।"
    },
    {
        "q": "Which wavelength is scattered most by air molecules in Earth's atmosphere?",
        "q_hi": "पृथ्वी के वायुमंडल में वायु के अणुओं द्वारा किस तरंगदैर्ध्य का सबसे अधिक प्रकीर्णन होता है?",
        "opts": ["Red", "Yellow", "Green", "Blue"],
        "opts_hi": ["लाल", "पीला", "हरा", "नीला"],
        "ans": 3,
        "sol": "According to Rayleigh scattering, scattering intensity is inversely proportional to the fourth power of wavelength (I ∝ 1/λ⁴). Blue light (short wavelength) scatters much more than red.",
        "sol_hi": "रेले प्रकीर्णन के अनुसार, प्रकीर्णन की तीव्रता तरंगदैर्ध्य के चौथे घात के व्युत्क्रमानुपाती होती है (I ∝ 1/λ⁴)। नीला प्रकाश (कम तरंगदैर्ध्य) लाल की तुलना में बहुत अधिक प्रकीर्णित होता है।"
    },
    {
        "q": "What kind of lens is present in the human eye?",
        "q_hi": "मानव नेत्र में किस प्रकार का लेंस उपस्थित होता है?",
        "opts": ["Concave", "Convex", "Biconcave", "Cylindrical"],
        "opts_hi": ["अवतल", "उत्तल", "उभयावतल", "बेलनाकार"],
        "ans": 1,
        "sol": "The human eye has a natural double convex crystalline lens that converges light onto the retina.",
        "sol_hi": "मानव आंख में एक प्राकृतिक उभयोत्तल क्रिस्टलीय लेंस होता है जो प्रकाश को रेटिना पर अभिसरित करता है।"
    },
    {
        "q": "When light passes from air to glass, which parameters change?",
        "q_hi": "जब प्रकाश हवा से कांच में प्रवेश करता है, तो कौन से पैरामीटर बदलते हैं?",
        "opts": ["Frequency and Wavelength", "Frequency and Velocity", "Wavelength and Velocity", "Frequency only"],
        "opts_hi": ["आवृत्ति और तरंगदैर्ध्य", "आवृत्ति और वेग", "तरंगदैर्ध्य और वेग", "केवल आवृत्ति"],
        "ans": 2,
        "sol": "When light changes medium, its frequency remains unchanged (as it depends on the source), while its velocity and wavelength change.",
        "sol_hi": "जब प्रकाश माध्यम बदलता है, तो उसकी आवृत्ति अपरिवर्तित रहती है (क्योंकि यह स्रोत पर निर्भर करती है), जबकि उसका वेग और तरंगदैर्ध्य बदल जाते हैं।"
    },
    {
        "q": "In a mirage, which light phenomenon is predominantly responsible?",
        "q_hi": "मरीचिका (Mirage) में मुख्य रूप से कौन सी प्रकाश घटना जिम्मेदार होती है?",
        "opts": ["Dispersion", "Scattering", "Total Internal Reflection", "Interference"],
        "opts_hi": ["वर्ण-विक्षेपण", "प्रकीर्णन", "पूर्ण आंतरिक परावर्तन (TIR)", "व्यतिकरण"],
        "ans": 2,
        "sol": "Mirage is an optical illusion caused by the refraction of light through air layers of different temperatures, resulting in Total Internal Reflection (TIR).",
        "sol_hi": "मरीचिका एक ऑप्टिकल भ्रम है जो विभिन्न तापमानों की हवा की परतों के माध्यम से प्रकाश के अपवर्तन के कारण होता है, जिसके परिणामस्वरूप पूर्ण आंतरिक परावर्तन (TIR) होता है।"
    },
    {
        "q": "Speed of sound in dry air at 0°C is approximately:",
        "q_hi": "0°C पर शुष्क हवा में ध्वनि की चाल लगभग कितनी होती है?",
        "opts": ["300 m/s", "332 m/s", "344 m/s", "1500 m/s"],
        "opts_hi": ["300 मीटर/सेकंड", "332 मीटर/सेकंड", "344 मीटर/सेकंड", "1500 मीटर/सेकंड"],
        "ans": 1,
        "sol": "The speed of sound in dry air at 0°C is approximately 331.5 m/s (commonly rounded to 332 m/s). At 20°C, it is ~343 m/s.",
        "sol_hi": "0°C पर शुष्क हवा में ध्वनि की चाल लगभग 332 मीटर/सेकंड होती है। 20°C पर यह लगभग 343 मीटर/सेकंड होती है।"
    },
    {
        "q": "Which part of the eye controls the amount of light entering it?",
        "q_hi": "आँख का कौन सा भाग उसमें प्रवेश करने वाले प्रकाश की मात्रा को नियंत्रित करता है?",
        "opts": ["Cornea", "Iris", "Retina", "Ciliary muscles"],
        "opts_hi": ["कॉर्निया", "आइरिस (Iris)", "रेटिना", "सिलियरी मांसपेशियां"],
        "ans": 1,
        "sol": "The iris regulates the size of the pupil, controlling the amount of light that enters the eye.",
        "sol_hi": "आइरिस पुतली के आकार को नियंत्रित करता है, जिससे आंख में प्रवेश करने वाले प्रकाश की मात्रा नियंत्रित होती है।"
    },
    {
        "q": "An object is placed at the center of curvature of a concave mirror. The image formed will be:",
        "q_hi": "एक वस्तु अवतल दर्पण के वक्रता केंद्र (C) पर रखी गई है। बनने वाला प्रतिबिंब होगा:",
        "opts": ["Virtual and erect", "Real, inverted and same size", "Real, inverted and diminished", "Real, inverted and magnified"],
        "opts_hi": ["आभासी और सीधा", "वास्तविक, उल्टा और समान आकार का", "वास्तविक, उल्टा और छोटा", "वास्तविक, उल्टा और बड़ा"],
        "ans": 1,
        "sol": "When an object is at the center of curvature (C) of a concave mirror, the image is formed at C. It is real, inverted, and of the same size.",
        "sol_hi": "जब कोई वस्तु अवतल दर्पण के वक्रता केंद्र (C) पर होती है, तो प्रतिबिंब C पर ही बनता है। यह वास्तविक, उल्टा और समान आकार का होता है।"
    },
    {
        "q": "What is the unit of frequency?",
        "q_hi": "आवृत्ति का मात्रक क्या है?",
        "opts": ["Meter", "Second", "Hertz", "Newton"],
        "opts_hi": ["मीटर", "सेकंड", "हर्ट्ज़", "न्यूटन"],
        "ans": 2,
        "sol": "Hertz (Hz) is the SI unit of frequency, representing cycles per second.",
        "sol_hi": "हर्ट्ज़ (Hz) आवृत्ति का SI मात्रक है, जो प्रति सेकंड चक्रों को दर्शाता है।"
    },
    {
        "q": "In a vacuum, all colors of visible light travel with:",
        "q_hi": "निर्वात में, दृश्य प्रकाश के सभी रंग यात्रा करते हैं:",
        "opts": ["Different speeds", "The same speed", "Speed dependent on intensity", "None of these"],
        "opts_hi": ["अलग-अलग चाल से", "समान चाल से", "तीव्रता पर निर्भर चाल से", "इनमें से कोई नहीं"],
        "ans": 1,
        "sol": "In vacuum, all electromagnetic waves, including all colors of visible light, travel at the same speed (c = 3 × 10⁸ m/s).",
        "sol_hi": "निर्वात में, सभी विद्युत चुंबकीय तरंगें, जिनमें दृश्य प्रकाश के सभी रंग शामिल हैं, समान चाल (c = 3 × 10⁸ मीटर/सेकंड) से यात्रा करती हैं।"
    },
    {
        "q": "Which phenomenon of light is responsible for the formation of a rainbow?",
        "q_hi": "इंद्रधनुष के निर्माण के लिए प्रकाश की कौन सी घटना जिम्मेदार है?",
        "opts": ["Refraction, Dispersion and Total Internal Reflection", "Scattering and Reflection", "Only Refraction", "Only Interference"],
        "opts_hi": ["अपवर्तन, वर्ण-विक्षेपण और पूर्ण आंतरिक परावर्तन", "प्रकीर्णन और परावर्तन", "केवल अपवर्तन", "केवल व्यतिकरण"],
        "ans": 0,
        "sol": "A rainbow is formed due to dispersion, refraction, and internal reflection of sunlight inside atmospheric water droplets acting as tiny prisms.",
        "sol_hi": "इंद्रधनुष का निर्माण वायुमंडलीय पानी की बूंदों के भीतर सूर्य के प्रकाश के अपवर्तन, वर्ण-विक्षेपण और आंतरिक परावर्तन के कारण होता है जो छोटे प्रिज्म के रूप में कार्य करते हैं।"
    },
    {
        "q": "Which instrument is used to measure the depth of the ocean using sound waves?",
        "q_hi": "ध्वनि तरंगों का उपयोग करके समुद्र की गहराई मापने के लिए किस उपकरण का उपयोग किया जाता है?",
        "opts": ["Altimeter", "Fathometer", "Hydrometer", "Barometer"],
        "opts_hi": ["अल्टीमीटर", "फैडोमीटर (Fathometer)", "हाइड्रोमीटर", "बैरोमीटर"],
        "ans": 1,
        "sol": "A fathometer is a depth finder that uses echo-sounding (ultrasonic waves) to determine ocean depth.",
        "sol_hi": "फैडोमीटर गहराई मापने का यंत्र है जो समुद्र की गहराई निर्धारित करने के लिए प्रतिध्वनि-ध्वनिक (पराबैंगनी तरंगों) का उपयोग करता है।"
    },
    {
        "q": "Audible range sound waves can also be referred to as:",
        "q_hi": "श्रव्य सीमा की ध्वनि तरंगों को यह भी कहा जा सकता है:",
        "opts": ["Ultrasonic waves", "Sonic waves", "Infrasonic waves", "Supersonic waves"],
        "opts_hi": ["पराबैंगनी तरंगें", "श्रव्य (Sonic) तरंगें", "अपश्रव्य तरंगें", "पराध्वनिक तरंगें"],
        "ans": 1,
        "sol": "Sonic waves are sound waves in the frequency range audible to humans (20 Hz - 20,000 Hz).",
        "sol_hi": "श्रव्य (Sonic) तरंगें मानव को सुनाई देने वाली आवृत्ति सीमा (20 हर्ट्ज़ - 20,000 हर्ट्ज़) में ध्वनि तरंगें होती हैं।"
    },
    {
        "q": "If the wavelength of a light wave is decreased, what happens to its energy?",
        "q_hi": "यदि किसी प्रकाश तरंग की तरंगदैर्ध्य कम कर दी जाए, तो उसकी ऊर्जा पर क्या प्रभाव पड़ता है?",
        "opts": ["Decreases", "Increases", "Remains same", "Becomes zero"],
        "opts_hi": ["घटती है", "बढ़ती है", "स्थिर रहती है", "शून्य हो जाती है"],
        "ans": 1,
        "sol": "According to Planck's equation, E = hc/λ. Energy is inversely proportional to wavelength, so decreasing wavelength increases energy.",
        "sol_hi": "प्लांक के समीकरण के अनुसार, E = hc/λ. ऊर्जा तरंगदैर्ध्य के व्युत्क्रमानुपाती होती है, इसलिए तरंगदैर्ध्य कम करने से ऊर्जा बढ़ती है।"
    }
]

# ----------------- MOCK TEST QUESTIONS (15 Qs) -----------------
mock_test_questions = [
    {
        "q": "Consider the following statements regarding waves:<br>1. Sound waves in air are longitudinal mechanical waves.<br>2. Light waves are transverse electromagnetic waves.<br>Which of the statements given above is/are correct?",
        "q_hi": "तरंगों के संबंध में निम्नलिखित कथनों पर विचार करें:<br>1. हवा में ध्वनि तरंगें अनुदैर्ध्य यांत्रिक तरंगें हैं।<br>2. प्रकाश तरंगें अनुप्रस्थ विद्युत चुंबकीय तरंगें हैं।<br>उपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 2,
        "sol": "Both statements are correct. Sound is longitudinal and mechanical; light is transverse and electromagnetic.",
        "sol_hi": "दोनों कथन सही हैं। ध्वनि अनुदैर्ध्य और यांत्रिक है; प्रकाश अनुप्रस्थ और विद्युत चुंबकीय है।"
    },
    {
        "q": "Match the following:<br>A. Myopia &rarr; 1. Convex lens<br>B. Hypermetropia &rarr; 2. Cylindrical lens<br>C. Astigmatism &rarr; 3. Concave lens",
        "q_hi": "सुमेलित करें:<br>A. निकट दृष्टि दोष &rarr; 1. उत्तल लेंस<br>B. दूर दृष्टि दोष &rarr; 2. बेलनाकार लेंस<br>C. अबिन्दुकता &rarr; 3. अवतल लेंस",
        "opts": ["A-3, B-1, C-2", "A-1, B-3, C-2", "A-3, B-2, C-1", "A-2, B-1, C-3"],
        "opts_hi": ["A-3, B-1, C-2", "A-1, B-3, C-2", "A-3, B-2, C-1", "A-2, B-1, C-3"],
        "ans": 0,
        "sol": "Myopia requires concave lens (A-3), Hypermetropia requires convex lens (B-1), Astigmatism requires cylindrical lens (C-2).",
        "sol_hi": "निकट दृष्टि दोष के लिए अवतल लेंस (A-3), दूर दृष्टि दोष के लिए उत्तल लेंस (B-1), अबिन्दुकता के लिए बेलनाकार लेंस (C-2) की आवश्यकता होती है।"
    },
    {
        "q": "A lens has a power of -2.5 D. What is its focal length and type?",
        "q_hi": "एक लेंस की क्षमता -2.5 D है। इसकी फोकस दूरी और प्रकार क्या है?",
        "opts": ["-40 cm, Concave lens", "+40 cm, Convex lens", "-25 cm, Concave lens", "+25 cm, Convex lens"],
        "opts_hi": ["-40 सेमी, अवतल लेंस", "+40 सेमी, उत्तल लेंस", "-25 सेमी, अवतल लेंस", "+25 सेमी, उत्तल लेंस"],
        "ans": 0,
        "sol": "f = 1/P = 1/(-2.5) = -0.4 m = -40 cm. The negative focal length indicates a diverging (concave) lens.",
        "sol_hi": "f = 1/P = 1/(-2.5) = -0.4 मीटर = -40 सेमी। ऋणात्मक फोकस दूरी एक अपसारी (अवतल) लेंस को दर्शाती है।"
    },
    {
        "q": "Which of the following optical phenomena is responsible for mirages in deserts?",
        "q_hi": "रेगिस्तान में मरीचिका (Mirage) बनने के लिए निम्नलिखित में से कौन सी प्रकाश घटना जिम्मेदार है?",
        "opts": ["Scattering of light", "Total Internal Reflection", "Dispersion of light", "Interference of light"],
        "opts_hi": ["प्रकाश का प्रकीर्णन", "पूर्ण आंतरिक परावर्तन (TIR)", "प्रकाश का वर्ण-विक्षेपण", "प्रकाश का व्यतिकरण"],
        "ans": 1,
        "sol": "A mirage is formed due to refraction through air layers of different temperatures, resulting in Total Internal Reflection (TIR) near the ground.",
        "sol_hi": "मरीचिका हवा की विभिन्न तापमान की परतों से अपवर्तन के कारण बनती है, जिसके परिणामस्वरूप जमीन के पास पूर्ण आंतरिक परावर्तन (TIR) होता है।"
    },
    {
        "q": "What is the speed of sound in air at 0°C compared to 20°C?",
        "q_hi": "20°C की तुलना में 0°C पर हवा में ध्वनि की चाल:",
        "opts": ["It is higher at 0°C", "It is lower at 0°C", "It is the same", "It depends on pressure"],
        "opts_hi": ["0°C पर अधिक होती है", "0°C पर कम होती है", "समान होती है", "दबाव पर निर्भर करती है"],
        "ans": 1,
        "sol": "The speed of sound in air increases with temperature (v ∝ √T). Therefore, speed of sound is lower at 0°C (~332 m/s) than at 20°C (~343 m/s).",
        "sol_hi": "हवा में ध्वनि की चाल तापमान के साथ बढ़ती है (v ∝ √T)। इसलिए, 0°C (~332 मीटर/सेकंड) पर ध्वनि की चाल 20°C (~343 मीटर/सेकंड) की तुलना में कम होती है।"
    },
    {
        "q": "Why are danger signal lights red in color?",
        "q_hi": "खतरे के संकेत वाले प्रकाश लाल रंग के क्यों होते हैं?",
        "opts": ["Red light scatters the most", "Red light scatters the least", "Red light has the highest frequency", "Red light is pleasant to eyes"],
        "opts_hi": ["लाल प्रकाश का प्रकीर्णन सबसे अधिक होता है", "लाल प्रकाश का प्रकीर्णन सबसे कम होता है", "लाल प्रकाश की आवृत्ति सबसे अधिक होती है", "लाल प्रकाश आँखों को अच्छा लगता है"],
        "ans": 1,
        "sol": "Red has the longest wavelength in the visible spectrum. Since scattering intensity is inversely proportional to λ⁴, red scatters the least and can travel long distances through fog or smoke.",
        "sol_hi": "लाल रंग की दृश्य स्पेक्ट्रम में तरंगदैर्ध्य सबसे लंबी होती है। चूंकि प्रकीर्णन की तीव्रता λ⁴ के व्युत्क्रमानुपाती होती है, लाल रंग सबसे कम प्रकीर्णित होता है और कोहरे या धुएं में लंबी दूरी तय कर सकता है।"
    },
    {
        "q": "An object is placed at a distance of 10 cm in front of a concave mirror of focal length 15 cm. The image formed will be:",
        "q_hi": "15 सेमी फोकस दूरी वाले अवतल दर्पण के सामने 10 सेमी की दूरी पर एक वस्तु रखी गई है। बनने वाला प्रतिबिंब होगा:",
        "opts": ["Real, inverted and magnified", "Virtual, erect and magnified", "Real, inverted and diminished", "Virtual, erect and diminished"],
        "opts_hi": ["वास्तविक, उल्टा और बड़ा", "आभासी, सीधा और बड़ा", "वास्तविक, उल्टा और छोटा", "आभासी, सीधा और छोटा"],
        "ans": 1,
        "sol": "Here, object distance u = -10 cm and focal length f = -15 cm. Since the object is placed within the focal length (u < f), a virtual, erect, and magnified image is formed behind the mirror.",
        "sol_hi": "यहाँ, वस्तु की दूरी u = -10 सेमी और फोकस दूरी f = -15 सेमी है। चूंकि वस्तु फोकस दूरी के भीतर रखी गई है (u < f), दर्पण के पीछे एक आभासी, सीधा और आवर्धित प्रतिबिंब बनता है।"
    },
    {
        "q": "If the critical angle for a medium-to-air interface is 30°, what is the refractive index of the medium?",
        "q_hi": "यदि किसी माध्यम-हवा इंटरफ़ेस के लिए क्रांतिक कोण 30° है, तो माध्यम का अपवर्तनांक क्या है?",
        "opts": ["1.5", "2.0", "1.33", "2.5"],
        "opts_hi": ["1.5", "2.0", "1.33", "2.5"],
        "ans": 1,
        "sol": "Refractive index n = 1 / sin(C). Since C = 30°, n = 1 / sin(30°) = 1 / 0.5 = 2.0.",
        "sol_hi": "अपवर्तनांक n = 1 / sin(C). चूंकि C = 30° है, n = 1 / sin(30°) = 1 / 0.5 = 2.0."
    },
    {
        "q": "Which phenomenon causes the optical illusion of water on hot roads?",
        "q_hi": "गर्म सड़कों पर पानी होने का भ्रम (ऑप्टिकल भ्रम) किस घटना के कारण होता है?",
        "opts": ["Reflection of light", "Total Internal Reflection", "Scattering of light", "Diffraction of light"],
        "opts_hi": ["प्रकाश का परावर्तन", "पूर्ण आंतरिक परावर्तन (TIR)", "प्रकाश का प्रकीर्णन", "प्रकाश का विवर्तन"],
        "ans": 1,
        "sol": "The illusion is a mirage, caused by total internal reflection resulting from refraction in air layers of varying temperatures (and densities) near the hot road surface.",
        "sol_hi": "यह भ्रम एक मरीचिका है, जो गर्म सड़क की सतह के पास अलग-अलग तापमान (और घनत्व) की हवा की परतों में अपवर्तन के परिणामस्वरूप होने वाले पूर्ण आंतरिक परावर्तन के कारण होता है।"
    },
    {
        "q": "What is the speed of sound in water compared to air?",
        "q_hi": "हवा की तुलना में पानी में ध्वनि की चाल:",
        "opts": ["Lower", "Higher", "Same", "Zero"],
        "opts_hi": ["कम होती है", "अधिक होती है", "समान होती है", "शून्य होती है"],
        "ans": 1,
        "sol": "Sound travels faster in liquids than in gases because liquids are less compressible (higher bulk modulus) than gases. Speed of sound in water is ~1500 m/s compared to ~343 m/s in air.",
        "sol_hi": "गैसों की तुलना में द्रवों में ध्वनि तेजी से चलती है क्योंकि द्रव गैसों की तुलना में कम संपीड्य होते हैं। पानी में ध्वनि की चाल लगभग 1500 मीटर/सेकंड होती है, जबकि हवा में यह लगभग 343 मीटर/सेकंड होती है।"
    },
    {
        "q": "A person cannot see objects clearly beyond 2 meters. Which defect of vision does he have?",
        "q_hi": "एक व्यक्ति 2 मीटर से अधिक दूरी की वस्तुओं को स्पष्ट नहीं देख सकता। उसे कौन सा नेत्र दोष है?",
        "opts": ["Myopia", "Hypermetropia", "Presbyopia", "Cataract"],
        "opts_hi": ["निकट दृष्टि दोष (Myopia)", "दूर दृष्टि दोष", "जरा दृष्टि दोष", "मोतियाबिंद"],
        "ans": 0,
        "sol": "In Myopia (nearsightedness), a person can see near objects clearly but cannot focus on distant objects beyond a certain far point.",
        "sol_hi": "निकट दृष्टि दोष (Myopia) में, व्यक्ति पास की वस्तुओं को स्पष्ट देख सकता है लेकिन एक निश्चित दूर बिंदु से आगे की दूर की वस्तुओं पर ध्यान केंद्रित नहीं कर सकता है।"
    },
    {
        "q": "The magnification produced by a convex rear-view mirror is:",
        "q_hi": "वाहनों के उत्तल रियर-व्यू दर्पण द्वारा उत्पन्न आवर्धन (Magnification) होता है:",
        "opts": ["Less than 1", "More than 1", "Equal to 1", "Infinite"],
        "opts_hi": ["1 से कम", "1 से अधिक", "1 के बराबर", "अनंत"],
        "ans": 0,
        "sol": "A convex mirror always forms a virtual, erect, and diminished image, meaning the size of the image is smaller than the object. Therefore, magnification (m = h_i / h_o) is less than 1.",
        "sol_hi": "उत्तल दर्पण हमेशा एक आभासी, सीधा और छोटा प्रतिबिंब बनाता है, यानी प्रतिबिंब का आकार वस्तु से छोटा होता है। इसलिए, आवर्धन (m = h_i / h_o) 1 से कम होता है।"
    },
    {
        "q": "In which medium does sound travel slowest?",
        "q_hi": "ध्वनि किस माध्यम में सबसे धीमी गति से यात्रा करती है?",
        "opts": ["Wood", "Water", "Air", "Iron"],
        "opts_hi": ["लकड़ी", "पानी", "हवा", "लोहा"],
        "ans": 2,
        "sol": "Sound travels slowest in gases (like air) because gases are highly compressible, and their particles are far apart, slowing wave transmission.",
        "sol_hi": "गैसों (जैसे हवा) में ध्वनि सबसे धीमी गति से चलती है क्योंकि गैसें अत्यधिक संपीड्य होती हैं और उनके कण दूर-दूर होते हैं, जिससे तरंग संचरण धीमा हो जाता है।"
    },
    {
        "q": "A ray of light enters from glass to water. What happens to its direction?",
        "q_hi": "प्रकाश की एक किरण कांच (सघन) से पानी (विरल) में प्रवेश करती है। इसकी दिशा पर क्या प्रभाव पड़ता है?",
        "opts": ["Bends towards the normal", "Bends away from the normal", "Goes straight without bending", "Reflected back completely"],
        "opts_hi": ["अभिलंब की ओर झुकती है", "अभिलंब से दूर झुकती है", "बिना झुके सीधी चली जाती है", "पूरी तरह से परावर्तित हो जाती है"],
        "ans": 1,
        "sol": "Refractive index of glass is ~1.5 and water is ~1.33. Glass is denser than water. When light travels from a denser to a rarer medium, it speeds up and bends away from the normal.",
        "sol_hi": "कांच का अपवर्तनांक लगभग 1.5 और पानी का लगभग 1.33 है। कांच पानी से सघन है। जब प्रकाश सघन से विरल माध्यम में जाता है, तो इसकी चाल बढ़ जाती है और यह अभिलंब से दूर झुक जाता है।"
    },
    {
        "q": "What determines the quality or timbre of a musical sound?",
        "q_hi": "किसी संगीत ध्वनि की गुणवत्ता या स्वर-रंग (Timbre) किससे निर्धारित होता है?",
        "opts": ["Frequency", "Amplitude", "Waveform / Overtones", "Velocity"],
        "opts_hi": ["आवृत्ति", "आयाम", "तरंग रूप (Waveform) / अधिस्वरक (Overtones)", "वेग"],
        "ans": 2,
        "sol": "The quality or timbre of sound depends on the waveform and the presence of overtones/harmonics, allowing us to distinguish between different instruments playing the same note.",
        "sol_hi": "ध्वनि की गुणवत्ता या स्वर-रंग तरंग रूप और अधिस्वरक/हारमोनिक्स की उपस्थिति पर निर्भर करता है, जिससे हमें एक ही नोट बजाने वाले विभिन्न उपकरणों के बीच अंतर करने में मदद मिलती है।"
    }
]

# ----------------- BUILD FINAL JSON OBJECTS -----------------
def build_theory():
    return {
        "breadcrumbs": breadcrumbs_en,
        "hero": hero_en,
        "labels": labels_en,
        "timeline": timeline_en,
        "mnemonics": mnemonics_en,
        "flashcards": flashcards_en,
        "traps": traps_en,
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Thoroughly review wave motion, properties of sound, optics laws, mirrors, lenses, and eye defects.", "sections": deep_dive_en}
    }

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. Wave Motion & Sound waves",
                "masteryZone": [
                    {"type": "MCQ", "q": "Sound waves in air are:", "opts": ["Longitudinal mechanical waves", "Transverse mechanical waves", "Longitudinal electromagnetic waves", "Transverse electromagnetic waves"], "ans": 0, "sol": "Sound waves in air are longitudinal mechanical waves, requiring a medium and propagating via compressions and rarefactions."},
                    {"type": "True/False", "q": "True or False: The speed of sound is faster in humid air than in dry air.", "ans": True, "sol": "True. Humid air has a lower density than dry air because water vapor is lighter than nitrogen and oxygen. Since v ∝ 1/√ρ, sound travels faster in humid air."},
                    {"type": "Fill in the Blank", "q": "The frequency range of infrasonic waves is below ________ Hz.", "ans": "20", "sol": "Infrasonic waves have frequencies below 20 Hz, which is below the human hearing limit."}
                ]
            },
            {
                "title": "2. Optics: Mirrors & Images",
                "masteryZone": [
                    {"type": "MCQ", "q": "A rear-view mirror in vehicles always forms:", "opts": ["Real and diminished image", "Virtual and magnified image", "Virtual and diminished image", "Real and magnified image"], "ans": 2, "sol": "Convex mirrors are used for rear-view because they always form virtual, erect, and diminished images, providing a wide field of view."},
                    {"type": "MCQ", "q": "An object is placed at focus of a concave mirror. Where is the image formed?", "opts": ["At Center of Curvature", "Between Focus and Center of Curvature", "At Infinity", "At Pole"], "ans": 2, "sol": "When the object is at focus of a concave mirror, the reflected rays are parallel and meet at infinity. The image is real, inverted, and highly magnified."}
                ]
            },
            {
                "title": "3. Refraction & TIR",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which optical phenomenon is responsible for the working of optical fibers?", "opts": ["Dispersion", "Total Internal Reflection", "Scattering", "Interference"], "ans": 1, "sol": "Optical fibers work on the principle of Total Internal Reflection (TIR), trapping light signals inside the core."},
                    {"type": "True/False", "q": "True or False: Sparkling of diamond is primarily due to scattering of light.", "ans": False, "sol": "False. Sparkling of diamond is due to Total Internal Reflection (TIR) combined with its high refractive index and dispersion."}
                ]
            },
            {
                "title": "4. Human Eye Defects",
                "masteryZone": [
                    {"type": "MCQ", "q": "Myopia or Nearsightedness is corrected by using which lens?", "opts": ["Convex lens", "Concave lens", "Bifocal lens", "Cylindrical lens"], "ans": 1, "sol": "Myopia is corrected using a concave (diverging) lens to bring the focus back onto the retina."},
                    {"type": "True/False", "q": "True or False: Hypermetropia is corrected using a concave lens.", "ans": False, "sol": "False. Hypermetropia (farsightedness) is corrected using a convex (converging) lens."}
                ]
            },
            {
                "title": "5. Dispersion & Scattering",
                "masteryZone": [
                    {"type": "MCQ", "q": "Why is the sky blue?", "opts": ["Reflection of sunlight from oceans", "Rayleigh scattering of light", "Dispersion of light through cloud water droplets", "Refraction of light"], "ans": 1, "sol": "Rayleigh scattering states that shorter wavelengths (blue) scatter much more than longer ones (red) by air molecules, making sky blue."},
                    {"type": "One-Liner", "q": "Which color of light bends the most when passing through a prism?", "sol": "Violet."}
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
        "deepDive": {"title": f"{TOPIC_DISPLAY_HI} के मुख्य अध्ययन नोट्स", "description": "तरंग गति, ध्वनि के गुणों, प्रकाशिकी के नियमों, दर्पणों, लेंसों और नेत्र दोषों की गहन समीक्षा करें।", "sections": deep_dive_hi}
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
                "title": "1. तरंग गति और ध्वनि तरंगें",
                "masteryZone": [
                    {"type": "MCQ", "q": "हवा में ध्वनि तरंगें होती हैं:", "opts": ["अनुदैर्ध्य यांत्रिक तरंगें", "अनुप्रस्थ यांत्रिक तरंगें", "अनुदैर्ध्य विद्युत चुंबकीय तरंगें", "अनुप्रस्थ विद्युत चुंबकीय तरंगें"], "ans": 0, "sol": "हवा में ध्वनि तरंगें अनुदैर्ध्य यांत्रिक तरंगें होती हैं, जिन्हें एक माध्यम की आवश्यकता होती है और वे संपीड़न और विरलन के माध्यम से फैलती हैं।"},
                    {"type": "True/False", "q": "सही या गलत: आर्द्र हवा में ध्वनि की चाल शुष्क हवा की तुलना में तेज होती है।", "ans": True, "sol": "सही। आर्द्र हवा का घनत्व शुष्क हवा की तुलना में कम होता है क्योंकि जल वाष्प नाइट्रोजन और ऑक्सीजन से हल्की होती है। चूंकि v ∝ 1/√ρ, ध्वनि आर्द्र हवा में तेजी से चलती है।"},
                    {"type": "Fill in the Blank", "q": "अपश्रव्य (Infrasonic) तरंगों की आवृत्ति __________ हर्ट्ज़ से कम होती है।", "ans": "20", "sol": "अपश्रव्य तरंगों की आवृत्तियां 20 हर्ट्ज़ से कम होती हैं, जो मानव सुनने की सीमा से नीचे हैं।"}
                ]
            },
            {
                "title": "2. प्रकाशिकी: दर्पण और प्रतिबिंब",
                "masteryZone": [
                    {"type": "MCQ", "q": "वाहनों में पीछे देखने वाला दर्पण हमेशा बनाता है:", "opts": ["वास्तविक और छोटा प्रतिबिंब", "आभासी और बड़ा प्रतिबिंब", "आभासी और छोटा प्रतिबिंब", "वास्तविक और बड़ा प्रतिबिंब"], "ans": 2, "sol": "उत्तल दर्पणों का उपयोग पीछे देखने के लिए किया जाता है क्योंकि वे हमेशा आभासी, सीधा और छोटा प्रतिबिंब बनाते हैं, जिससे एक व्यापक दृष्टि क्षेत्र प्राप्त होता है।"},
                    {"type": "MCQ", "q": "एक वस्तु अवतल दर्पण के फोकस पर रखी गई है। प्रतिबिंब कहाँ बनेगा?", "opts": ["वक्रता केंद्र पर", "फोकस और वक्रता केंद्र के बीच", "अनंत पर", "ध्रुव पर"], "ans": 2, "sol": "जब वस्तु अवतल दर्पण के फोकस पर होती है, तो परावर्तित किरणें समानांतर होती हैं और अनंत पर मिलती हैं। प्रतिबिंब वास्तविक, उल्टा और अत्यधिक आवर्धित होता है।"}
                ]
            },
            {
                "title": "3. अपवर्तन और पूर्ण आंतरिक परावर्तन",
                "masteryZone": [
                    {"type": "MCQ", "q": "ऑप्टिकल फाइबर के काम करने के लिए कौन सी ऑप्टिकल घटना जिम्मेदार है?", "opts": ["वर्ण-विक्षेपण", "पूर्ण आंतरिक परावर्तन (TIR)", "प्रकीर्णन", "व्यतिकरण"], "ans": 1, "sol": "ऑप्टिकल फाइबर पूर्ण आंतरिक परावर्तन (TIR) के सिद्धांत पर काम करते हैं, जो प्रकाश संकेतों को कोर के भीतर फंसाकर रखते हैं।"},
                    {"type": "True/False", "q": "सही या गलत: हीरे का चमकना मुख्य रूप से प्रकाश के प्रकीर्णन के कारण होता है।", "ans": False, "sol": "गलत। हीरे की चमक उसके उच्च अपवर्तनांक और वर्ण-विक्षेपण के साथ जुड़े पूर्ण आंतरिक परावर्तन (TIR) के कारण होती है।"}
                ]
            },
            {
                "title": "4. मानव नेत्र दोष",
                "masteryZone": [
                    {"type": "MCQ", "q": "निकट दृष्टि दोष (Myopia) को किस लेंस के उपयोग से ठीक किया जाता है?", "opts": ["उत्तल लेंस", "अवतल लेंस", "द्विफोकसी लेंस", "बेलनाकार लेंस"], "ans": 1, "sol": "निकट दृष्टि दोष को एक अवतल (अपसारी) लेंस का उपयोग करके ठीक किया जाता है ताकि फोकस वापस रेटिना पर आ सके।"},
                    {"type": "True/False", "q": "सही या गलत: दूर दृष्टि दोष (Hypermetropia) को अवतल लेंस का उपयोग करके ठीक किया जाता है।", "ans": False, "sol": "गलत। दूर दृष्टि दोष (Hypermetropia) को उत्तल (अभिसारी) लेंस का उपयोग करके ठीक किया जाता है।"}
                ]
            },
            {
                "title": "5. वर्ण-विक्षेपण और प्रकीर्णन",
                "masteryZone": [
                    {"type": "MCQ", "q": "आकाश नीला क्यों दिखाई देता है?", "opts": ["महासागरों से सूर्य के प्रकाश का परावर्तन", "प्रकाश का रेले प्रकीर्णन", "बादलों की पानी की बूंदों के माध्यम से प्रकाश का विक्षेपण", "प्रकाश का अपवर्तन"], "ans": 1, "sol": "रेले प्रकीर्णन के अनुसार, कम तरंगदैर्ध्य (नीला) वायु के अणुओं द्वारा लंबी तरंगदैर्ध्य (लाल) की तुलना में बहुत अधिक प्रकीर्णित होती है, जिससे आकाश नीला दिखाई देता है।"},
                    {"type": "One-Liner", "q": "प्रिज्म से गुजरने पर प्रकाश का कौन सा रंग सबसे अधिक झुकता है?", "sol": "बैंगनी।"}
                ]
            }
        ]
    }


# ----------------- FILE GENERATION -----------------
def write_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Written: {filepath}")

# Write English files
write_json(os.path.join(BASE_DIR, "theory.json"), build_theory())
write_json(os.path.join(BASE_DIR, "practice.json"), build_practice())
write_json(os.path.join(BASE_DIR, "mastery.json"), build_mastery())

# Write Hindi files
write_json(os.path.join(HI_DIR, "theory.json"), build_theory_hi())
write_json(os.path.join(HI_DIR, "practice.json"), build_practice_hi())
write_json(os.path.join(HI_DIR, "mastery.json"), build_mastery_hi())
