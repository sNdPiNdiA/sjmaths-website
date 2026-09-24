const fs = require('fs');
const path = require('path');

const filePath = path.resolve('upsc-aso/fluid-mechanics-machinery/fluid-statics/index.html');
let html = fs.readFileSync(filePath, 'utf8');

const newTab1 = `        <!-- ================= TAB 1: STUDY NOTES (EXHAUSTIVE TEXTBOOK MODULES) ================= -->
        <div id="tab-study" class="tab-content active">
            
            <!-- ------------------------------------------------------------- -->
            <!-- SUBTOPIC 01: PRESSURE AT A POINT & FLUID STRESS TENSOR        -->
            <!-- ------------------------------------------------------------- -->
            <div class="concept-card">
                <div class="concept-header">
                    <div>
                        <div class="breadcrumbs" style="margin-bottom: 0.25rem;">Subtopic 01 • Fundamental Fluid Statics</div>
                        <h2 class="concept-title">Pressure at a Point & Fluid Stress Tensor (Isotropy)</h2>
                    </div>
                    <div class="badge-group">
                        <span class="badge badge-must-know">Must Know</span>
                        <span class="badge badge-formula">Core Theory</span>
                        <span class="badge badge-safety">Airframe Sensor Physics</span>
                    </div>
                </div>

                <div class="box-sub" style="border-left: 4px solid var(--accent-cyan); margin-bottom: 1.25rem;">
                    <h6><i class="fa-solid fa-book-bookmark"></i> Formal Technical Definition</h6>
                    <p style="font-size: 0.92rem; color: #f1f5f9; line-height: 1.7; margin: 0;">
                        <strong>Fluid Pressure ($P$)</strong> at a point is defined as the normal compressive force exerted by continuous fluid molecules per unit area on an infinitesimally small boundary plane passing through that point in the limit as the area shrinks to zero:
                        $$P = \lim_{\Delta A \to 0} \frac{\Delta F_n}{\Delta A}$$
                        In a static fluid, pressure is an <strong>isotropic scalar</strong>—it acts with identical magnitude in every conceivable direction on any planar orientation.
                    </p>
                </div>

                <div class="grid-2">
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-microscope"></i> Basic Concept & Physical Mechanism</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                A fluid at rest cannot sustain any shear stress ($\tau = 0$). By definition, any shear stress would initiate continuous angular deformation (flow). Because shear components vanish identically in static equilibrium, the general second-order <strong>Cauchy Stress Tensor</strong> ($\sigma_{ij}$) collapses purely to normal diagonal compressive stresses:
                                $$\sigma_{ij} = \begin{bmatrix} \sigma_{xx} & \tau_{xy} & \tau_{xz} \\ \tau_{yx} & \sigma_{yy} & \tau_{yz} \\ \tau_{zx} & \tau_{zy} & \sigma_{zz} \end{bmatrix} \implies \begin{bmatrix} -P & 0 & 0 \\ 0 & -P & 0 \\ 0 & 0 & -P \end{bmatrix} = -P \delta_{ij}$$
                                where $\delta_{ij}$ is the Kronecker delta. Negative sign denotes thermodynamic compression.
                            </p>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-calculator"></i> Proof of Directional Independence (Wedge Equilibrium)</h6>
                            <div class="formula-box">
                                Consider a microscopic triangular wedge of fluid of width $b$ into the plane:
                                $$\sum F_x = 0 \implies P_x (b \Delta y) - P_n (b \Delta s) \sin \theta = 0$$
                                Since $\Delta y = \Delta s \sin \theta$, it follows immediately that:
                                $$P_x = P_n$$
                                Similarly, in the vertical direction including gravity:
                                $$\sum F_z = 0 \implies P_z (b \Delta x) - P_n (b \Delta s) \cos \theta - \frac{1}{2}\rho g (b \Delta x \Delta y) = 0$$
                                As $\Delta x, \Delta y \to 0$, the second-order weight term vanishes:
                                $$P_z = P_n \implies P_x = P_z = P_n$$
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-shield-halved"></i> Aircraft Systems & Air Safety Connection</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                <strong>Flush Static Port Orientation:</strong> Because pressure is isotropic, flush static pressure ports installed on the fuselage skin measure true ambient static pressure ($P_s$) <em>only</em> if the local boundary layer streamlines flow strictly parallel to the surface without local flow detachment or crossflow.
                            </p>
                            <div style="margin-top: 0.75rem;">
                                <div class="effect-arrow"><i class="fa-solid fa-arrow-right"></i> <span>Fuselage Sideslip / Angle of Attack change $\rightarrow$ Crossflow introduces dynamic component into static port $\rightarrow$ Static Position Error ($\Delta P_s$).</span></div>
                                <div class="effect-arrow"><i class="fa-solid fa-arrow-right"></i> <span>Air Data Computer (ADC) compensates using calibrated position error correction (PEC) curves mandated under DGCA CAR Section 2.</span></div>
                            </div>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-triangle-exclamation"></i> UPSC Trap & Exam Pitfall</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                <strong>Exam Trap:</strong> "Is pressure a vector because it exerts a directed force on a surface?"
                                <br><strong style="color: var(--accent-rose);">Correction:</strong> Pressure is strictly a <strong>scalar</strong>. It has magnitude but no intrinsic direction in the fluid. Direction only emerges when a physical surface of area vector $\vec{A}$ is placed into the fluid, producing normal compressive force $\vec{F} = -P \vec{A}$.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Worked Numerical 1 -->
                <div class="worked-example">
                    <h5><i class="fa-solid fa-calculator"></i> Worked Numerical Example 1: Static Pressure Force on a Cockpit Window</h5>
                    <p style="font-size: 0.9rem; color: var(--text-muted);"><strong>Problem:</strong> A rectangular cockpit inspection window on a pressurized transport aircraft measures $0.40\text{ m} \times 0.30\text{ m}$. At FL350, internal cabin static pressure is maintained at $78.0\text{ kPa}$, while outside atmospheric pressure is $23.8\text{ kPa}$. Calculate: (a) Net outward normal force exerted on the window, and (b) Verify whether window orientation angle affects the local pressure magnitude.</p>
                    <div style="background: rgba(0,0,0,0.4); padding: 1rem; border-radius: 6px; margin-top: 0.75rem; font-family: 'Fira Code', monospace; font-size: 0.85rem; color: #93c5fd; line-height: 1.7;">
                        Step 1: Compute window area:
                        $$A = 0.40\text{ m} \times 0.30\text{ m} = 0.12\text{ m}^2$$
                        Step 2: Differential static pressure across the window pane:
                        $$\Delta P = P_{\text{cabin}} - P_{\text{outside}} = 78.0\text{ kPa} - 23.8\text{ kPa} = 54.2\text{ kPa} = 54,200\text{ N/m}^2$$
                        Step 3: Calculate net outward force:
                        $$F_{\text{net}} = \Delta P \times A = 54,200\text{ N/m}^2 \times 0.12\text{ m}^2 = \mathbf{6,504\text{ N}} \quad (\approx 663.2\text{ kgf})$$
                        Step 4: Orientation effect: Because pressure at a point in a static fluid is isotropic ($P_x = P_y = P_z$), window tilt angle does NOT alter the static pressure intensity; the force vector remains strictly normal to the window plane.
                    </div>
                    <p style="font-size: 0.85rem; color: #34d399; margin-top: 0.5rem;"><strong>ASO Takeaway:</strong> A differential pressure of just 54.2 kPa creates a massive 6.5 kN ejection force on the windshield. Retention bolts must be torqued and inspected in accordance with DGCA CAR 145 standards to prevent in-flight cockpit blowout (e.g., British Airways Flight 5390).</p>
                </div>
            </div>

            <!-- ------------------------------------------------------------- -->
            <!-- SUBTOPIC 02: PASCAL'S LAW & AIRCRAFT HYDRAULIC SYSTEMS        -->
            <!-- ------------------------------------------------------------- -->
            <div class="concept-card">
                <div class="concept-header">
                    <div>
                        <div class="breadcrumbs" style="margin-bottom: 0.25rem;">Subtopic 02 • Fluid Power Transmission</div>
                        <h2 class="concept-title">Pascal's Law & Aircraft Hydraulic Actuation</h2>
                    </div>
                    <div class="badge-group">
                        <span class="badge badge-must-know">Must Know</span>
                        <span class="badge badge-formula">Core Formula</span>
                        <span class="badge badge-safety">Primary Flight Controls</span>
                    </div>
                </div>

                <div class="box-sub" style="border-left: 4px solid var(--accent-cyan); margin-bottom: 1.25rem;">
                    <h6><i class="fa-solid fa-book-bookmark"></i> Formal Technical Definition</h6>
                    <p style="font-size: 0.92rem; color: #f1f5f9; line-height: 1.7; margin: 0;">
                        <strong>Pascal's Principle:</strong> A pressure change applied to an enclosed, incompressible fluid at rest is transmitted completely and undiminished to every portion of the fluid and to the walls of the containing vessel:
                        $$\Delta P_1 = \Delta P_2 \implies \frac{F_1}{A_1} = \frac{F_2}{A_2}$$
                    </p>
                </div>

                <div class="grid-2">
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-gears"></i> Hydraulic Multiplication Mechanism</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                Pascal's Law enables vast <strong>Mechanical Advantage (MA)</strong>. By exerting a small control force $F_1$ over a master cylinder of small cross-sectional area $A_1$, the generated hydrostatic pressure transmits across the hydraulic lines to a slave cylinder of large area $A_2$, producing a giant force:
                                $$F_2 = F_1 \left(\frac{A_2}{A_1}\right) = F_1 \left(\frac{d_2}{d_1}\right)^2$$
                                By conservation of energy ($W = F_1 s_1 = F_2 s_2$), the piston displacement is inversely proportional to the area:
                                $$s_2 = s_1 \left(\frac{A_1}{A_2}\right)$$
                            </p>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-table-list"></i> Aircraft Hydraulic Pressure Specifications</h6>
                            <div style="overflow-x: auto; margin-top: 0.5rem;">
                                <table style="width: 100%; font-size: 0.82rem; border-collapse: collapse; text-align: left;">
                                    <thead>
                                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1); color: #fff;">
                                            <th style="padding: 4px 6px;">Aircraft Type</th>
                                            <th style="padding: 4px 6px;">Nominal Pressure</th>
                                            <th style="padding: 4px 6px;">Hydraulic Fluid</th>
                                        </tr>
                                    </thead>
                                    <tbody style="color: #cbd5e1;">
                                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                                            <td style="padding: 4px 6px;">B737 / A320</td>
                                            <td style="padding: 4px 6px;">3,000 psi ($20.68\text{ MPa}$)</td>
                                            <td style="padding: 4px 6px;">Skydrol LD-4 / Type IV</td>
                                        </tr>
                                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                                            <td style="padding: 4px 6px;">A380 / B787</td>
                                            <td style="padding: 4px 6px;">5,000 psi ($34.47\text{ MPa}$)</td>
                                            <td style="padding: 4px 6px;">Skydrol 500B-4 (Low weight)</td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 4px 6px;">General Aviation</td>
                                            <td style="padding: 4px 6px;">1,500 psi ($10.34\text{ MPa}$)</td>
                                            <td style="padding: 4px 6px;">MIL-PRF-5606 (Mineral base)</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-triangle-exclamation"></i> Air Safety Breakdown: Fluid Aeration & Sponginess</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                Pascal's Law assumes strict <strong>incompressibility</strong>. If air enters the hydraulic lines (aeration from loose seals or pump cavitation), the effective bulk modulus ($K$) collapses:
                                $$\frac{1}{K_{\text{effective}}} = \frac{1 - x}{K_{\text{liquid}}} + \frac{x}{K_{\text{air}}}$$
                                Even $0.5\%$ entrained air by volume reduces effective stiffness by over $70\%$, causing delayed control surface response, hydraulic "sponginess", pilot-induced oscillations (PIO), and uncommanded rudder runaway (e.g., USAir Flight 427).
                            </p>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-triangle-exclamation"></i> UPSC Trap</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                <strong>Exam Trap:</strong> Does Pascal's Law apply to dynamic fluid systems?
                                <br><strong style="color: var(--accent-rose);">Trap Clarification:</strong> No. Pascal's Law is strictly a <strong>hydrostatic theorem</strong> for static, enclosed, continuous fluids. When fluid flows rapidly through valves, Bernoulli's equation, Navier-Stokes shear stresses, and pipe friction losses must be accounted for.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Worked Numerical 2 -->
                <div class="worked-example">
                    <h5><i class="fa-solid fa-calculator"></i> Worked Numerical Example 2: Elevator Flight Control Power Unit</h5>
                    <p style="font-size: 0.9rem; color: var(--text-muted);"><strong>Problem:</strong> In a Fly-By-Wire hydraulic elevator power control unit (PCU), a pilot input servo-valve applies a command force of $180\text{ N}$ onto an input piston of diameter $d_1 = 12\text{ mm}$. The output ram connected to the elevator horn has a diameter $d_2 = 72\text{ mm}$. Calculate: (a) System hydraulic pressure transmitted, (b) Output hinge actuation force $F_2$, and (c) Stroke displacement of the elevator ram if the servo input piston moves $15\text{ mm}$.</p>
                    <div style="background: rgba(0,0,0,0.4); padding: 1rem; border-radius: 6px; margin-top: 0.75rem; font-family: 'Fira Code', monospace; font-size: 0.85rem; color: #93c5fd; line-height: 1.7;">
                        Step 1: Compute input piston area:
                        $$A_1 = \frac{\pi}{4} (0.012\text{ m})^2 = 1.131 \times 10^{-4}\text{ m}^2$$
                        Step 2: Calculate hydraulic pressure generated:
                        $$P = \frac{F_1}{A_1} = \frac{180}{1.131 \times 10^{-4}} = 1.5915 \times 10^6\text{ Pa} \approx \mathbf{1.592\text{ MPa}} \quad (\approx 230.9\text{ psi})$$
                        Step 3: Calculate mechanical advantage and output force:
                        $$\text{MA} = \left(\frac{d_2}{d_1}\right)^2 = \left(\frac{72}{12}\right)^2 = 6^2 = 36$$
                        $$F_2 = F_1 \times \text{MA} = 180\text{ N} \times 36 = \mathbf{6,480\text{ N}} \quad (\approx 6.48\text{ kN})$$
                        Step 4: Calculate output ram displacement:
                        $$s_2 = s_1 \times \left(\frac{d_1}{d_2}\right)^2 = 15\text{ mm} \times \frac{1}{36} = \mathbf{0.417\text{ mm}}$$
                    </div>
                </div>
            </div>

            <!-- ------------------------------------------------------------- -->
            <!-- SUBTOPIC 03: ABSOLUTE, GAUGE & VACUUM PRESSURE                -->
            <!-- ------------------------------------------------------------- -->
            <div class="concept-card">
                <div class="concept-header">
                    <div>
                        <div class="breadcrumbs" style="margin-bottom: 0.25rem;">Subtopic 03 • Pressure Datums & Scales</div>
                        <h2 class="concept-title">Absolute, Gauge & Vacuum Pressure (Cabin Pressurization & Altimetry)</h2>
                    </div>
                    <div class="badge-group">
                        <span class="badge badge-must-know">Must Know</span>
                        <span class="badge badge-formula">Core Formula</span>
                        <span class="badge badge-safety">Cabin Structural Integrity</span>
                    </div>
                </div>

                <div class="box-sub" style="border-left: 4px solid var(--accent-cyan); margin-bottom: 1.25rem;">
                    <h6><i class="fa-solid fa-book-bookmark"></i> Formal Technical Definitions</h6>
                    <p style="font-size: 0.92rem; color: #f1f5f9; line-height: 1.7; margin: 0;">
                        Pressure measurement depends fundamentally on the chosen reference datum:
                        <br>• <strong>Absolute Pressure ($P_{\text{abs}}$):</strong> Pressure measured relative to a perfect absolute vacuum (zero molecular collision datum). It is always non-negative ($P_{\text{abs}} \ge 0$).
                        <br>• <strong>Gauge Pressure ($P_{\text{gauge}}$):</strong> Pressure measured relative to the local ambient atmospheric pressure ($P_{\text{atm}}$). Standard Bourdon gauges read zero at ambient atmosphere.
                        <br>• <strong>Vacuum Pressure ($P_{\text{vac}}$):</strong> The negative difference below atmospheric pressure when $P_{\text{abs}} < P_{\text{atm}}$:
                        $$P_{\text{abs}} = P_{\text{atm}} + P_{\text{gauge}}$$
                        $$P_{\text{vac}} = P_{\text{atm}} - P_{\text{abs}} = -P_{\text{gauge}}$$
                    </p>
                </div>

                <div class="grid-2">
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-plane-up"></i> Aircraft Cabin Differential Pressure ($\Delta P$)</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                Commercial aircraft cabins are pressurized to maintain an equivalent physiological altitude of $\le 8,000\text{ ft}$ ($P_{\text{cabin}} \approx 75.3\text{ kPa}$). At cruising altitude of FL390 ($11,887\text{ m}$), outside atmospheric pressure drops to just $19.6\text{ kPa}$.
                                The fuselage structure acts as a thin-walled cylindrical pressure vessel subjected to continuous differential hoop stress:
                                $$\sigma_{\text{hoop}} = \frac{\Delta P \cdot r}{t}, \quad \text{where } \Delta P = P_{\text{cabin}} - P_{\text{outside}}$$
                                Standard maximum $\Delta P_{\text{limit}}$ is $8.6\text{ psi}$ ($59.3\text{ kPa}$).
                            </p>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-crosshairs"></i> Altimeter Subscale Settings: QNH, QFE, QNE</h6>
                            <div style="font-size: 0.85rem; color: #cbd5e1; line-height: 1.6;">
                                • <strong>QNH:</strong> Altimeter subscale set to sea-level pressure calculated from aerodrome station pressure. Altimeter indicates <em>Altitude above Mean Sea Level (MSL)</em>. Reads aerodrome elevation on runway.
                                <br>• <strong>QFE:</strong> Subscale set so altimeter reads <em>Height above Aerodrome Elevation</em>. Reads zero on touchdown.
                                <br>• <strong>QNE:</strong> Standard pressure datum of $1013.25\text{ hPa} = 29.92\text{ inHg}$. Used above transition altitude to fly assigned <em>Flight Levels (FL)</em>.
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-shield-halved"></i> Air Safety Investigation Case Study: Explosive Decompression</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                <strong>Aloha Airlines Flight 243 (1988):</strong> Cyclic pressurization-depressurization loads ($\Delta P \approx 50\text{ kPa}$ over 89,000 flights) caused multi-site fatigue cracking along lap joints. The upper fuselage crown tore open in explosive decompression.
                                <br><strong>Helios Airways Flight 522 (2005):</strong> Pressurization selector left in MANUAL; crew failed to notice slow cabin depressurization, leading to hypoxia, loss of consciousness, and fuel-exhaustion crash.
                            </p>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-triangle-exclamation"></i> UPSC Trap</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                <strong>Exam Trap:</strong> Using gauge pressure in the Ideal Gas Equation ($P = \rho R T$) or Mach number relations!
                                <br><strong style="color: var(--accent-rose);">Mandatory Rule:</strong> All thermodynamic, aerodynamic, and gas dynamic formulas require <strong>ABSOLUTE pressure ($P_{\text{abs}}$)</strong> in Kelvins and Pascals. Never use gauge pressure in gas calculations!
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Worked Numerical 3 -->
                <div class="worked-example">
                    <h5><i class="fa-solid fa-calculator"></i> Worked Numerical Example 3: Cabin Outflow Valve Differential Calculation</h5>
                    <p style="font-size: 0.9rem; color: var(--text-muted);"><strong>Problem:</strong> An airliner cruises at FL370 where ambient static pressure is $21.4\text{ kPa}$. The cabin pressure altitude is maintained at $6,000\text{ ft}$ ($P_{\text{cabin}} = 81.2\text{ kPa}$). A Bourdon pressure gauge mounted on the forward bulkhead reads cabin pressure with reference to ambient outside atmosphere. Calculate: (a) The gauge reading in kPa and psi, (b) Absolute pressure of the cabin, and (c) Outward force exerted on a cabin door of area $1.85\text{ m}^2$.</p>
                    <div style="background: rgba(0,0,0,0.4); padding: 1rem; border-radius: 6px; margin-top: 0.75rem; font-family: 'Fira Code', monospace; font-size: 0.85rem; color: #93c5fd; line-height: 1.7;">
                        Step 1: Absolute cabin pressure:
                        $$P_{\text{abs, cabin}} = \mathbf{81.2\text{ kPa}}$$
                        Step 2: Differential gauge reading:
                        $$P_{\text{gauge}} = P_{\text{abs, cabin}} - P_{\text{outside}} = 81.2\text{ kPa} - 21.4\text{ kPa} = \mathbf{59.8\text{ kPa}}$$
                        $$\text{In psi: } 59.8\text{ kPa} \times \frac{14.696\text{ psi}}{101.325\text{ kPa}} = \mathbf{8.67\text{ psi}}$$
                        Step 3: Calculate net outward bursting force on cabin door:
                        $$F_{\text{door}} = \Delta P \times A_{\text{door}} = 59,800\text{ N/m}^2 \times 1.85\text{ m}^2 = \mathbf{110,630\text{ N}} \quad (\approx 110.63\text{ kN} \text{ or } 11.28\text{ tonnes!})$$
                    </div>
                    <p style="font-size: 0.85rem; color: #34d399; margin-top: 0.5rem;"><strong>Safety Note:</strong> Because the door experiences over 11 tonnes of outward force, transport aircraft use "plug-type" doors that wedge wider than the fuselage doorframe, making it aerodynamically and physically impossible to open the door in flight.</p>
                </div>
            </div>

            <!-- ------------------------------------------------------------- -->
            <!-- SUBTOPIC 04: HYDROSTATIC LAW & PRESSURE VARIATION             -->
            <!-- ------------------------------------------------------------- -->
            <div class="concept-card">
                <div class="concept-header">
                    <div>
                        <div class="breadcrumbs" style="margin-bottom: 0.25rem;">Subtopic 04 • Vertical Equilibrium</div>
                        <h2 class="concept-title">Pressure Variation in Static Fluids & Hydrostatic Law</h2>
                    </div>
                    <div class="badge-group">
                        <span class="badge badge-must-know">Must Know</span>
                        <span class="badge badge-formula">Core Derivation</span>
                        <span class="badge badge-safety">Altimeter Calibration</span>
                    </div>
                </div>

                <div class="box-sub" style="border-left: 4px solid var(--accent-cyan); margin-bottom: 1.25rem;">
                    <h6><i class="fa-solid fa-book-bookmark"></i> Formal Technical Definition & Equation</h6>
                    <p style="font-size: 0.92rem; color: #f1f5f9; line-height: 1.7; margin: 0;">
                        <strong>The Hydrostatic Law</strong> states that the rate of vertical increase of pressure in a static fluid in the direction of gravity is directly proportional to the local specific weight ($\gamma = \rho g$) of the fluid:
                        $$\frac{dP}{dz} = -\rho g = -\gamma \quad \text{or} \quad \frac{dP}{dh} = \rho g = \gamma$$
                        where $z$ is vertical coordinate measured upward, and $h$ is fluid depth measured downward from a free surface.
                    </p>
                </div>

                <div class="grid-2">
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-calculator"></i> Step-by-Step Derivation from Fluid Element</h6>
                            <div class="formula-box">
                                Consider an infinitesimal vertical cylinder of cross-sectional area $dA$ and height $dz$:
                                <br>1. Upward pressure force on bottom face: $+P \cdot dA$
                                <br>2. Downward pressure force on top face: $-(P + dP) \cdot dA$
                                <br>3. Downward gravitational weight of element: $-dW = -\rho g (dA \cdot dz)$
                                <br>Equating static vertical forces $\sum F_z = 0$:
                                $$P \cdot dA - (P + dP) \cdot dA - \rho g \cdot dA \cdot dz = 0$$
                                $$-dP \cdot dA - \rho g \cdot dA \cdot dz = 0 \implies \mathbf{\frac{dP}{dz} = -\rho g}$$
                            </div>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-layer-group"></i> Incompressible Liquid vs. Compressible Atmosphere</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                • <strong>Incompressible Liquid ($\rho = \text{const}$):</strong>
                                $$P_2 - P_1 = -\rho g (z_2 - z_1) = \rho g h$$
                                Pressure increases linearly with depth regardless of container geometry (Hydrostatic Paradox).
                                <br>• <strong>Compressible Gas (Atmosphere):</strong> Air density depends on pressure and temperature ($\rho = P / RT$). Substituting into Hydrostatic Law yields the <em>Barometric Differential Equation</em>:
                                $$\frac{dP}{P} = -\frac{g}{RT} dz$$
                            </p>
                        </div>
                    </div>
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-cloud"></i> International Standard Atmosphere (ISA) Tropospheric Derivation</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                In the troposphere (Sea Level to $11,000\text{ m}$), temperature decreases linearly with altitude at the standard lapse rate $\alpha = 0.0065\text{ K/m}$ ($6.5^\circ\text{C/km}$):
                                $$T = T_0 - \alpha h$$
                                Integrating the barometric differential equation:
                                $$\int_{P_0}^P \frac{dP}{P} = -\frac{g}{R} \int_0^h \frac{dh}{T_0 - \alpha h} \implies \mathbf{P(h) = P_0 \left(1 - \frac{\alpha h}{T_0}\right)^{\frac{g}{\alpha R}}}$$
                                where for standard air: $\frac{g}{\alpha R} = \frac{9.80665}{0.0065 \times 287.05} \approx \mathbf{5.2561}$.
                            </p>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-shield-halved"></i> Altimetry Safety Rule: Temperature Error</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                Aircraft pressure altimeters assume ISA standard temperature. In cold air, air density is higher, so atmospheric pressure drops more rapidly with altitude.
                                <br><strong style="color: var(--accent-rose);">Golden Aviation Rule:</strong> <em>"Flying from High to Low (pressure or temperature), look out below!"</em>
                                In cold weather, true altitude is dangerously LOWER than indicated altitude $\rightarrow$ risk of Controlled Flight Into Terrain (CFIT).
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Worked Numerical 4 -->
                <div class="worked-example">
                    <h5><i class="fa-solid fa-calculator"></i> Worked Numerical Example 4: ISA Pressure Altitude at Cruising Flight Level</h5>
                    <p style="font-size: 0.9rem; color: var(--text-muted);"><strong>Problem:</strong> An aircraft climbs to a pressure altitude of $h = 8,000\text{ m}$ ($26,247\text{ ft}$) under standard ISA atmospheric conditions. Taking $T_0 = 288.15\text{ K}$ ($15^\circ\text{C}$), $P_0 = 101.325\text{ kPa}$, lapse rate $\alpha = 0.0065\text{ K/m}$, $g = 9.80665\text{ m/s}^2$, and $R = 287.05\text{ J/(kg}\cdot\text{K)}$. Calculate: (a) Ambient temperature at 8,000 m, (b) Atmospheric static pressure $P$, and (c) Air density $\rho$.</p>
                    <div style="background: rgba(0,0,0,0.4); padding: 1rem; border-radius: 6px; margin-top: 0.75rem; font-family: 'Fira Code', monospace; font-size: 0.85rem; color: #93c5fd; line-height: 1.7;">
                        Step 1: Compute temperature at 8,000 m:
                        $$T = T_0 - \alpha h = 288.15 - (0.0065 \times 8000) = 288.15 - 52.0 = \mathbf{236.15\text{ K}} \quad (-37.0^\circ\text{C})$$
                        Step 2: Calculate temperature ratio:
                        $$\frac{T}{T_0} = \frac{236.15}{288.15} = 0.81954$$
                        Step 3: Apply the ISA barometric power formula:
                        $$\text{Exponent: } \frac{g}{\alpha R} = \frac{9.80665}{0.0065 \times 287.05} = 5.25588$$
                        $$P = P_0 \left(\frac{T}{T_0}\right)^{5.25588} = 101.325 \times (0.81954)^{5.25588} = 101.325 \times 0.35178 = \mathbf{35.644\text{ kPa}}$$
                        Step 4: Calculate air density via Equation of State:
                        $$\rho = \frac{P}{R T} = \frac{35,644}{287.05 \times 236.15} = \frac{35,644}{67,786.86} = \mathbf{0.5258\text{ kg/m}^3}$$
                    </div>
                </div>
            </div>

            <!-- ------------------------------------------------------------- -->
            <!-- SUBTOPIC 05: PIEZOMETER                                       -->
            <!-- ------------------------------------------------------------- -->
            <div class="concept-card">
                <div class="concept-header">
                    <div>
                        <div class="breadcrumbs" style="margin-bottom: 0.25rem;">Subtopic 05 • Pressure Measurement Instruments</div>
                        <h2 class="concept-title">Piezometer Tube & Capillarity Limits</h2>
                    </div>
                    <div class="badge-group">
                        <span class="badge badge-must-know">Must Know</span>
                        <span class="badge badge-formula">Core Formula</span>
                        <span class="badge badge-safety">Fuel Sump Inspection</span>
                    </div>
                </div>

                <div class="box-sub" style="border-left: 4px solid var(--accent-cyan); margin-bottom: 1.25rem;">
                    <h6><i class="fa-solid fa-book-bookmark"></i> Formal Technical Definition</h6>
                    <p style="font-size: 0.92rem; color: #f1f5f9; line-height: 1.7; margin: 0;">
                        A <strong>Piezometer</strong> is the simplest liquid manometer, consisting of a vertical transparent tube connected to a vessel or pipe containing liquid under pressure. The liquid rises in the tube until hydrostatic pressure head balances the fluid static pressure:
                        $$P = \rho g h = \gamma h$$
                        where $h$ is the vertical height of the liquid meniscus above the point of measurement.
                    </p>
                </div>

                <div class="grid-2">
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-ban"></i> 4 Critical Operational Limitations of Piezometers</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                1. <strong>Cannot Measure Gas Pressure:</strong> Gases possess negligible specific weight compared to atmosphere. Gas would escape directly into ambient air without forming a measurable liquid interface.
                                <br>2. <strong>Cannot Measure Vacuum (Negative Gauge Pressure):</strong> Atmospheric pressure pushes outside air into the pipe, sucking liquid in rather than rising.
                                <br>3. <strong>Impractical Tube Height for High Pressures:</strong> For an aircraft 3,000 psi hydraulic line, a piezometer tube using hydraulic oil would need to be over $2,400\text{ meters}$ tall!
                                <br>4. <strong>Capillary Meniscus Error:</strong> In tubes with bore diameter $< 12\text{ mm}$, surface tension causes capillary rise/depression, distorting the true pressure head.
                            </p>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-droplet"></i> Capillary Error Correction Formula</h6>
                            <div class="formula-box">
                                True pressure head $h_{\text{true}} = h_{\text{measured}} - h_c$, where capillary rise is:
                                $$h_c = \frac{4 \sigma \cos \theta}{\rho g d}$$
                                To keep capillary meniscus error below $1\%$, piezometer tube internal bore diameter must satisfy:
                                $$d \ge 12\text{ mm}$$
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-plane-circle-check"></i> Aviation Ground Operations Application</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                <strong>Aircraft Fuel Tank Sight Gauges:</strong> Maintenance personnel and flight dispatchers use external glass sight-gauge piezometers on auxiliary power unit (APU) day tanks and ground refueling refueler bowsers to visually verify hydrostatic fuel height before flight release, avoiding electronic capacitance probe calibration errors.
                            </p>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-triangle-exclamation"></i> UPSC Trap</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                <strong>Exam Question:</strong> "Why is piezometer never used for wind tunnel static pressure measurement?"
                                <br><strong style="color: var(--accent-rose);">Trap Answer:</strong> Because wind tunnel working fluid is air (a gas). A piezometer requires a liquid with an exposed free meniscus and cannot measure gas pressures.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Worked Numerical 5 -->
                <div class="worked-example">
                    <h5><i class="fa-solid fa-calculator"></i> Worked Numerical Example 5: Piezometer Capillary Error Correction</h5>
                    <p style="font-size: 0.9rem; color: var(--text-muted);"><strong>Problem:</strong> A piezometer tube of internal diameter $d = 6\text{ mm}$ is connected to a ground fuel testing tank containing Jet A-1 fuel ($\rho = 804\text{ kg/m}^3$). The observed meniscus height in the tube is $h_{\text{obs}} = 350\text{ mm}$. If the surface tension of Jet A-1 is $\sigma = 0.028\text{ N/m}$ and its contact angle with clean glass is $\theta = 0^\circ$ (complete wetting), calculate: (a) Capillary rise error $h_c$, (b) True pressure head $h_{\text{true}}$, and (c) True gauge pressure in the fuel tank.</p>
                    <div style="background: rgba(0,0,0,0.4); padding: 1rem; border-radius: 6px; margin-top: 0.75rem; font-family: 'Fira Code', monospace; font-size: 0.85rem; color: #93c5fd; line-height: 1.7;">
                        Step 1: Compute capillary rise:
                        $$h_c = \frac{4 \sigma \cos \theta}{\rho g d} = \frac{4 \times 0.028 \times \cos 0^\circ}{804 \times 9.81 \times 0.006} = \frac{0.112}{47.323} = 0.002367\text{ m} \approx \mathbf{2.37\text{ mm}}$$
                        Step 2: Correct observed head:
                        $$h_{\text{true}} = h_{\text{obs}} - h_c = 350\text{ mm} - 2.37\text{ mm} = \mathbf{347.63\text{ mm}} = 0.34763\text{ m}$$
                        Step 3: Calculate true gauge pressure:
                        $$P = \rho g h_{\text{true}} = 804 \times 9.81 \times 0.34763 = \mathbf{2,741.8\text{ Pa}} \quad (\approx 2.742\text{ kPa})$$
                    </div>
                </div>
            </div>

            <!-- ------------------------------------------------------------- -->
            <!-- SUBTOPIC 06: U-TUBE & DIFFERENTIAL MANOMETERS                 -->
            <!-- ------------------------------------------------------------- -->
            <div class="concept-card">
                <div class="concept-header">
                    <div>
                        <div class="breadcrumbs" style="margin-bottom: 0.25rem;">Subtopic 06 • Differential Pressure Metrology</div>
                        <h2 class="concept-title">U-Tube, Differential & Inclined Manometers (Pitot-Static Sensing)</h2>
                    </div>
                    <div class="badge-group">
                        <span class="badge badge-must-know">Must Know</span>
                        <span class="badge badge-formula">Core Formula</span>
                        <span class="badge badge-safety">Airspeed Sensor Calibration</span>
                    </div>
                </div>

                <div class="box-sub" style="border-left: 4px solid var(--accent-cyan); margin-bottom: 1.25rem;">
                    <h6><i class="fa-solid fa-book-bookmark"></i> Formal Technical Definition & Principle</h6>
                    <p style="font-size: 0.92rem; color: #f1f5f9; line-height: 1.7; margin: 0;">
                        A <strong>U-Tube Manometer</strong> consists of a bent glass tube containing one or more immiscible manometric fluids of high specific gravity (commonly mercury, $\text{SG} = 13.6$, or light oils for low pressures).
                        It overcomes piezometer limitations by measuring positive pressures, vacuums, and differential pressures in both liquids and gases using continuous hydrostatic balancing across a common horizontal datum:
                        $$P_A + \sum (\rho_i g h_i)_{\text{left}} = P_B + \sum (\rho_j g h_j)_{\text{right}}$$
                    </p>
                </div>

                <div class="grid-2">
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-sliders"></i> Inclined Tube Manometer for High Sensitivity</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                When measuring tiny differential pressures (such as boundary-layer wind tunnel pressure drops), standard vertical U-tubes provide unreadable meniscus movements. An <strong>Inclined Manometer</strong> has one limb tilted at an angle $\theta$ to the horizontal.
                                The observed meniscus displacement along the slant $L$ is magnified:
                                $$L = \frac{h}{\sin \theta} \implies \text{Magnification Factor } S = \frac{1}{\sin \theta}$$
                                For $\theta = 15^\circ$, $S = 1/\sin 15^\circ \approx 3.86$ times greater visual resolution!
                            </p>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-calculator"></i> Differential Manometer Governing Equation</h6>
                            <div class="formula-box">
                                For pipe sections A and B connected to a U-tube with manometric fluid $\rho_m$:
                                $$P_A + \rho_1 g h_1 - \rho_m g h_m - \rho_2 g h_2 = P_B$$
                                If fluid in both pipes is identical ($\rho_1 = \rho_2 = \rho$) and pipe centers are level:
                                $$P_A - P_B = (\rho_m - \rho) g h_m$$
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-plane-circle-exclamation"></i> Aircraft Airspeed Indicator (ASI) Connection</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                The aircraft Airspeed Indicator (ASI) is conceptually an aneroid differential manometer that measures dynamic pressure:
                                $$q = P_{\text{total}} - P_{\text{static}} = \frac{1}{2}\rho V^2$$
                                <strong>Birgenair Flight 301 (1996):</strong> Mud dauber wasps nested inside the captain's pitot tube. Static air was trapped inside the pitot line. During climb, outside static pressure dropped while trapped pitot pressure remained constant $\rightarrow$ ASI falsely indicated excessive airspeed, leading to stall and crash.
                            </p>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-triangle-exclamation"></i> UPSC Trap</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                <strong>Exam Trap:</strong> Inverting differential manometer equations when using an <em>Inverted U-Tube Manometer</em>!
                                <br><strong style="color: var(--accent-rose);">Trap Rule:</strong> In an inverted U-tube, the manometric fluid is LIGHTER than the line fluid ($\rho_m < \rho$). Moving upward subtracts pressure head:
                                $$P_A - \rho_1 g h_1 + \rho_m g h_m + \rho_2 g h_2 = P_B$$
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Worked Numerical 6 -->
                <div class="worked-example">
                    <h5><i class="fa-solid fa-calculator"></i> Worked Numerical Example 6: Wind Tunnel Pitot-Static Differential Reading</h5>
                    <p style="font-size: 0.9rem; color: var(--text-muted);"><strong>Problem:</strong> A pitot-static probe in a low-speed aeronautical wind tunnel is connected to an inclined U-tube manometer containing alcohol ($\text{SG} = 0.82$). The manometer tube is inclined at an angle of $\theta = 30^\circ$ to the horizontal. Air density in the tunnel is $\rho_{\text{air}} = 1.20\text{ kg/m}^3$. If the observed slant displacement of the meniscus along the tube is $L = 120\text{ mm}$, calculate: (a) Vertical differential pressure head $h$, (b) Differential dynamic pressure $\Delta P$ in Pa, and (c) Airflow speed $V$ in the test section.</p>
                    <div style="background: rgba(0,0,0,0.4); padding: 1rem; border-radius: 6px; margin-top: 0.75rem; font-family: 'Fira Code', monospace; font-size: 0.85rem; color: #93c5fd; line-height: 1.7;">
                        Step 1: Compute vertical height of manometric liquid:
                        $$h = L \sin \theta = 0.120\text{ m} \times \sin 30^\circ = 0.120 \times 0.5 = \mathbf{0.060\text{ m}} = 60\text{ mm}$$
                        Step 2: Calculate dynamic pressure difference ($\Delta P = \rho_{\text{alc}} g h$):
                        $$\rho_{\text{alc}} = 0.82 \times 1000 = 820\text{ kg/m}^3$$
                        $$\Delta P = 820 \times 9.81 \times 0.060 = \mathbf{482.65\text{ Pa}}$$
                        Step 3: Calculate wind tunnel airspeed via Bernoulli dynamic pressure relation:
                        $$\Delta P = \frac{1}{2} \rho_{\text{air}} V^2 \implies V = \sqrt{\frac{2 \Delta P}{\rho_{\text{air}}}} = \sqrt{\frac{2 \times 482.65}{1.20}} = \sqrt{804.42} = \mathbf{28.36\text{ m/s}} \quad (\approx 102.1\text{ km/h} \text{ or } 55.1\text{ knots})$$
                    </div>
                </div>
            </div>

            <!-- ------------------------------------------------------------- -->
            <!-- SUBTOPIC 07: BAROMETER & ALTIMETRY STANDARDS                  -->
            <!-- ------------------------------------------------------------- -->
            <div class="concept-card">
                <div class="concept-header">
                    <div>
                        <div class="breadcrumbs" style="margin-bottom: 0.25rem;">Subtopic 07 • Atmospheric Pressure Instrumentation</div>
                        <h2 class="concept-title">Barometers & Aircraft Altimetry Standards</h2>
                    </div>
                    <div class="badge-group">
                        <span class="badge badge-must-know">Must Know</span>
                        <span class="badge badge-formula">Core Formula</span>
                        <span class="badge badge-safety">Altimeter Calibration</span>
                    </div>
                </div>

                <div class="box-sub" style="border-left: 4px solid var(--accent-cyan); margin-bottom: 1.25rem;">
                    <h6><i class="fa-solid fa-book-bookmark"></i> Formal Technical Definition & Torricellian Principle</h6>
                    <p style="font-size: 0.92rem; color: #f1f5f9; line-height: 1.7; margin: 0;">
                        A <strong>Barometer</strong> measures local absolute atmospheric pressure ($P_{\text{atm}}$). In Evangelista Torricelli's classic mercury barometer, an inverted glass tube filled with mercury is inverted into a mercury cistern. The liquid column falls until hydrostatic pressure matches atmospheric pressure:
                        $$P_{\text{atm}} = \rho_{\text{Hg}} g h + P_{\text{vapor}}$$
                        Because the saturation vapor pressure of mercury at room temperature is negligible ($P_{\text{vapor}} \approx 0.173\text{ Pa}$), the sealed space above the mercury is effectively a pure <strong>Torricellian Vacuum</strong>.
                    </p>
                </div>

                <div class="grid-2">
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-gauge-high"></i> Aneroid Barometer & Aircraft Sensitive Altimeter</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                Mercury barometers are hazardous and unusable in aircraft. Modern flight decks use <strong>Aneroid Capsules</strong>—sealed corrugated metal discs (beryllium copper) evacuated to internal vacuum.
                                As aircraft climbs, ambient static pressure decreases; the internal spring expands the capsule. Highly precise mechanical gearing amplifies this minute deflection to drive the altimeter needles.
                                The <strong>Kollsman Window</strong> allows pilots to dial in local aerodrome altimeter setting ($QNH$).
                            </p>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-table-list"></i> Standard Atmosphere Equivalent Pressure Units</h6>
                            <div style="overflow-x: auto; margin-top: 0.5rem;">
                                <table style="width: 100%; font-size: 0.82rem; border-collapse: collapse; text-align: left;">
                                    <thead>
                                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1); color: #fff;">
                                            <th style="padding: 4px 6px;">Unit System</th>
                                            <th style="padding: 4px 6px;">ISA Sea-Level Value</th>
                                            <th style="padding: 4px 6px;">Aviation Domain</th>
                                        </tr>
                                    </thead>
                                    <tbody style="color: #cbd5e1;">
                                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                                            <td style="padding: 4px 6px;">SI (Pascal / Bar)</td>
                                            <td style="padding: 4px 6px;">$101,325\text{ Pa} = 1.01325\text{ bar}$</td>
                                            <td style="padding: 4px 6px;">Aerodynamic & Gas Dynamics</td>
                                        </tr>
                                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                                            <td style="padding: 4px 6px;">Meteorology / ICAO</td>
                                            <td style="padding: 4px 6px;">$1013.25\text{ hPa} = 1013.25\text{ mbar}$</td>
                                            <td style="padding: 4px 6px;">QNH Barometric Altimeter Setting</td>
                                        </tr>
                                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                                            <td style="padding: 4px 6px;">Inches of Mercury</td>
                                            <td style="padding: 4px 6px;">$29.92\text{ inHg}$</td>
                                            <td style="padding: 4px 6px;">FAA / North American Flight Levels</td>
                                        </tr>
                                        <tr>
                                            <td style="padding: 4px 6px;">Millimeters of Mercury</td>
                                            <td style="padding: 4px 6px;">$760\text{ mmHg} = 760\text{ Torr}$</td>
                                            <td style="padding: 4px 6px;">Laboratory Barometry</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-triangle-exclamation"></i> Why Can Water Never Be Used in a Barometer?</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                1. <strong>Gigantic Column Height:</strong> Because water density ($\rho \approx 1000\text{ kg/m}^3$) is $13.6$ times lower than mercury, standard atmospheric pressure requires:
                                $$h = \frac{P_{\text{atm}}}{\rho_{\text{water}} g} = \frac{101325}{1000 \times 9.81} = \mathbf{10.33\text{ meters tall!}}$$
                                2. <strong>High Vapor Pressure Error:</strong> Water vapor pressure at $20^\circ\text{C}$ is $2.34\text{ kPa}$ (over 13,000 times higher than mercury!), causing a major error in barometric head readings.
                            </p>
                        </div>
                        <div class="box-sub">
                            <h6><i class="fa-solid fa-triangle-exclamation"></i> UPSC Trap: Altimeter Setting Misdialing</h6>
                            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.65;">
                                <strong>Exam Rule:</strong> $1\text{ hPa}$ change in pressure setting equals approximately $27\text{ feet}$ ($8.2\text{ m}$) or $30\text{ ft}$ of indicated altitude near sea level:
                                $$\Delta h \approx 27\text{ to } 30\text{ ft per hPa (or 1,000 ft per 1 inHg)}$$
                                If a pilot forgets to change QNH from $1025\text{ hPa}$ to $995\text{ hPa}$ when flying into a low-pressure depression, the altimeter will over-read by:
                                $$(1025 - 995) \times 30 = \mathbf{900\text{ ft!}}$$
                                The aircraft is actually 900 ft closer to the ground than the pilot thinks!
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Worked Numerical 7 -->
                <div class="worked-example">
                    <h5><i class="fa-solid fa-calculator"></i> Worked Numerical Example 7: Barometric Height & Altimeter Error</h5>
                    <p style="font-size: 0.9rem; color: var(--text-muted);"><strong>Problem:</strong> A weather station barometer at a mountain aerodrome indicates a mercury column height of $h_{\text{Hg}} = 630\text{ mmHg}$ at $0^\circ\text{C}$ ($\rho_{\text{Hg}} = 13,595\text{ kg/m}^3, g = 9.80665\text{ m/s}^2$). (a) Calculate local atmospheric pressure in kPa and hPa. (b) If an inbound aircraft sets its altimeter subscale to standard sea-level pressure ($1013.25\text{ hPa}$) instead of the local aerodrome QFE, calculate the false pressure altitude reading displayed when touching down on the runway.</p>
                    <div style="background: rgba(0,0,0,0.4); padding: 1rem; border-radius: 6px; margin-top: 0.75rem; font-family: 'Fira Code', monospace; font-size: 0.85rem; color: #93c5fd; line-height: 1.7;">
                        Step 1: Compute local atmospheric pressure:
                        $$P_{\text{local}} = \rho_{\text{Hg}} g h = 13,595 \times 9.80665 \times 0.630\text{ m} = 84,008\text{ Pa} = \mathbf{84.008\text{ kPa}} = \mathbf{840.08\text{ hPa}}$$
                        Step 2: Pressure difference from standard sea level:
                        $$\Delta P = P_0 - P_{\text{local}} = 1013.25\text{ hPa} - 840.08\text{ hPa} = \mathbf{173.17\text{ hPa}}$$
                        Step 3: Calculate indicated pressure altitude using standard lapse rate ($27.3\text{ ft/hPa}$):
                        $$\text{Indicated Altitude} = 173.17\text{ hPa} \times 27.3\text{ ft/hPa} = \mathbf{4,727.5\text{ ft}} \quad (\approx 1,441\text{ m})$$
                    </div>
                    <p style="font-size: 0.85rem; color: #34d399; margin-top: 0.5rem;"><strong>Operational Interpretation:</strong> An altimeter set to standard 1013.25 hPa reads the Pressure Altitude ($4,728\text{ ft}$) of the aerodrome. For safe instrument approach and landing, the pilot MUST obtain local QNH from ATIS / ATC to read true aerodrome elevation.</p>
                </div>
            </div>

        </div>`;

// Replace tab 1 in the html
const startMarker = '<!-- ================= TAB 1: STUDY NOTES ================= -->';
const endMarker = '<!-- ================= TAB 2: CONCEPT QUIZ ================= -->';

const startIndex = html.indexOf(startMarker);
const endIndex = html.indexOf(endMarker);

if (startIndex === -1 || endIndex === -1) {
    console.error('Could not find Tab 1 markers in Day 2 index.html');
    process.exit(1);
}

const updatedHtml = html.substring(0, startIndex) + newTab1 + '\n\n        ' + html.substring(endIndex);

fs.writeFileSync(filePath, updatedHtml, 'utf8');
console.log('✓ Successfully updated Day 2 with all 7 comprehensive subtopics!');
