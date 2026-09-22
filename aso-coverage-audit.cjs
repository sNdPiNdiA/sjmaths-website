// Per-day coverage audit: does each plan topic have a folder in its subject pillar?
const fs = require('fs'), path = require('path');
const BASE = path.join(__dirname, 'upsc-aso');
const PILLARS = { fluid: 'fluid-mechanics-machinery', systems: 'aircraft-systems-instrumentation-maintenance', propulsion: 'propulsion' };
const folders = {};
for (const k of Object.keys(PILLARS)) folders[k] = new Set(fs.readdirSync(path.join(BASE, PILLARS[k])));
// curated: plan topic -> pillar:folder-slug (existence verified against disk)
const M = {
  'Density / specific weight / specific gravity': 'fluid:density-specific-gravity-specific-volume',
  'Dynamic & kinematic viscosity': 'fluid:viscosity-dynamic-kinematic',
  'Newtonian & non-Newtonian fluids': 'fluid:non-newtonian-fluids',
  'Compressibility & bulk modulus': 'fluid:compressibility-and-bulk-modulus',
  'Surface tension & capillarity': 'fluid:surface-tension-soap-bubble-pressure',
  'Continuum hypothesis': 'fluid:continuum-hypothesis',
  'Manometers (U-tube & differential)': 'fluid:manometers-u-tube-differential',
  'Barometer / pressure altitude': 'fluid:barometric-pressure-altitude-calculation',
  'Streamline / pathline / streakline': 'fluid:streamlines-pathlines-streaklines',
  'Vorticity & circulation': 'fluid:biot-savart-law-for-vortex-tubes',
  'Helmholtz theorems': 'fluid:helmholtz-theorems',
  'Continuity equation (1D/2D/3D)': 'fluid:continuity-equation-1d-3d',
  'Bernoulli equation': 'fluid:bernoulli-s-equation-derivation-assumptions',
  'Venturimeter / pitot / orifice meter': 'fluid:venturimeter-pitot-tube-orifice-meter',
  'Reynolds number, laminar vs turbulent': 'fluid:reynolds-number-laminar-vs-turbulent',
  'Hagen–Poiseuille flow': 'fluid:hagen-poiseuille-flow-in-pipes',
  'Minor losses (sudden expansion/contraction)': 'fluid:sudden-expansion-sudden-contraction-losses',
  'Boundary layer development & thickness (Blasius)': 'fluid:boundary-layer-development-thickness-blasius',
  'Boundary-layer separation': 'fluid:boundary-layer-separation',
  'Buckingham π theorem': 'fluid:buckingham-pi-theorem',
  'Similarity laws (geometric/kinematic/dynamic)': 'fluid:similarity-laws-geometric-kinematic-dynamic',
  'Stream function & velocity potential': 'fluid:stream-function-velocity-potential',
  'Source, sink & doublet': 'fluid:source-and-sink-doublet',
  'Free & forced vortex': 'fluid:free-vortex-and-forced-vortex',
  'Speed of sound & Mach number': 'fluid:speed-of-sound-mach-number',
  'Stagnation / total temperature & pressure': 'fluid:stagnation-total-temperature-and-pressure',
  'Isentropic flow relations': 'fluid:isentropic-flow-relations',
  'Normal shock relations (Rankine–Hugoniot)': 'fluid:normal-shock-relations-rankine-hugoniot',
  'Oblique shock deflection angle': 'fluid:oblique-shock-deflection-angle',
  'Fanno flow': 'fluid:fanno-flow-subsonic-friction-fanno-curve',
  'Rayleigh flow': 'fluid:rayleigh-flow-heat-addition',
  'Centrifugal pump (velocity triangles, head)': 'fluid:centrifugal-pump-velocity-triangles-head',
  'Cavitation, NPSH & specific speed': 'fluid:cavitation-npsh-specific-speed',
  'Pump performance curves (H–Q, efficiency)': 'fluid:pump-performance-curves-h-q-efficiency',
  'Pumps in series vs parallel': 'fluid:pumps-in-series-vs-parallel',
  'Pelton / Francis / Kaplan turbines': 'fluid:pelton-francis-kaplan-turbines',
  'Turbine specific speed & affinity laws': 'propulsion:turbine-specific-speed-affinity-laws',
  'Navier–Stokes equation': 'fluid:ns-equation-form-and-physical-meaning',
  'Relief valve – pressure protection': 'systems:relief-valve-system-pressure-protection',
  'Actuators (linear, rotary, tandem)': 'systems:actuator-linear-rotary-tandem',
  'Hydraulic fluids (MIL-O-5606, Skydrol)': 'systems:hydraulic-fluids-mil-o-5606-mil-o-83282-skydrol-500b-4-barco-882',
  'Landing gear retraction & sequence valves': 'systems:landing-gear-retraction-extension-sequence-valves',
  'Brakes, anti-skid, autobrake': 'systems:brakes-anti-skid-autobrake-dunlop-brake-control',
  'Nose wheel steering': 'systems:nose-wheel-steering-hydraulic-electric-pneumatic',
  'Depressurisation & engine start sequence': 'systems:depressurisation-engine-start-sequence',
  'Hydraulic fluid cooling / heat exchanger': 'systems:cooling-of-hydraulic-fluid-heat-exchanger-loop',
  'AC/DC power generation': 'systems:ac-dc-power-generation-in-aircraft',
  'Transformer Rectifier Unit (TRU)': 'systems:transformer-rectifier-unit-tru-3-phase-to-dc',
  'DC machine – lap-wound armature, EMF': 'systems:dc-machine-lap-wound-armature-emf-calculation',
  'Commutator in DC generator': 'systems:commutator-function-in-dc-generator',
  'Compound generator': 'systems:compound-generator-speed-packaging-limitation',
  'AC frequency calculation': 'systems:ac-frequency-cycles-per-time-calculation',
  'Axial & centrifugal compressors': 'propulsion:axial-and-centrifugal-compressors',
};
// day -> [pillar, 'topic1|topic2|...']  ('(...)' days have no trackable topics)
const PLAN = {
  1: ['fluid', 'Density / specific weight / specific gravity|Dynamic & kinematic viscosity|Newtonian & non-Newtonian fluids|Compressibility & bulk modulus|Vapour pressure & cavitation|Surface tension & capillarity|Continuum hypothesis'],
  2: ['fluid', "Pressure at a point / Pascal's law|Absolute, gauge & vacuum pressure|Pressure variation in static fluids|Piezometer|Manometers (U-tube & differential)|Barometer / pressure altitude"],
  3: ['fluid', 'Force on submerged plane surfaces|Centre of pressure|Curved-surface forces|Buoyancy & Archimedes principle|Metacentre & metacentric height|Stability of floating bodies'],
  4: ['fluid', 'Lagrangian vs Eulerian description|Streamline / pathline / streakline|Steady/unsteady & uniform/non-uniform flow|Velocity & acceleration fields|Rotational & irrotational flow|Vorticity & circulation|Helmholtz theorems|Navier–Stokes equation'],
  5: ['fluid', 'Continuity equation (1D/2D/3D)|Euler equation of motion|Bernoulli equation|Venturimeter / pitot / orifice meter'],
  6: ['fluid', 'Linear momentum equation|Angular momentum equation|Reynolds Transport Theorem|Force on bends & nozzles|Jet propulsion fundamentals'],
  7: ['fluid', '(Revision Test — no topics)'],
  8: ['fluid', 'Reynolds number, laminar vs turbulent|Hagen–Poiseuille flow|Velocity distribution in laminar pipe flow|Shear stress distribution'],
  9: ['fluid', 'Darcy–Weisbach equation|Friction factor & Moody chart|Major losses|Minor losses (sudden expansion/contraction)|Pipes in series & parallel|HGL & EGL'],
  10: ['fluid', 'Boundary layer development & thickness (Blasius)|Laminar & turbulent boundary layers|Displacement / momentum / energy thickness|Skin-friction drag|Boundary-layer separation|Adverse pressure gradient'],
  11: ['fluid', 'Dimensional homogeneity|Buckingham π theorem|Model & prototype similarity|Similarity laws (geometric/kinematic/dynamic)|Re / Fr / Mach / We / Eu numbers'],
  12: ['fluid', 'Stream function & velocity potential|Equipotential lines|Source, sink & doublet|Free & forced vortex|Superposition|Flow around a cylinder'],
  13: ['fluid', 'Speed of sound & Mach number|Subsonic/transonic/supersonic/hypersonic|Stagnation / total temperature & pressure|Isentropic flow relations|Area–velocity relation & choking'],
  14: ['fluid', 'Normal shock relations (Rankine–Hugoniot)|Oblique shock deflection angle|Mach angle|Prandtl–Meyer expansion|Fanno flow|Rayleigh flow|C–D nozzle concepts'],
  15: ['fluid', 'Centrifugal pump (velocity triangles, head)|Priming & manometric efficiency|Cavitation, NPSH & specific speed|Pump performance curves (H–Q, efficiency)|Pumps in series vs parallel|Reciprocating pump basics'],
  16: ['fluid', 'Pelton / Francis / Kaplan turbines|Turbine specific speed & affinity laws|Hydraulic efficiency & unit quantities|Compressor/blower basics'],
  17: ['fluid', '(Fluid full revision — no topics)'],
  18: ['heat', "Fourier law & 1D conduction|Plane/cylindrical/spherical walls|Composite walls & thermal resistance|Contact resistance"],
  19: ['heat', 'Critical radius of insulation|Fins: efficiency & effectiveness|Lumped capacitance, Biot & Fourier numbers|Transient conduction'],
  20: ['heat', "Newton's law of cooling, forced/free convection|Re/Nu/Pr/Gr numbers|Black body, grey body, Stefan–Boltzmann|Kirchhoff law & view factors|Heat exchangers: LMTD & NTU|Boiling & condensation"],
  21: ['heat', '(Heat transfer test — no topics)'],
  22: ['aero', 'International Standard Atmosphere|Pressure/density/true altitude|Effect of atmosphere on performance'],
  23: ['aero', 'Fuselage, wing, empennage, landing gear|Aircraft axes: pitch, roll, yaw|Primary & secondary controls|Reference geometry'],
  24: ['aero', 'Chord, camber, thickness|NACA 4-digit designation|Symmetric vs cambered airfoils|Pressure distribution'],
  25: ['aero', 'CL, CD, Cm coefficients|Aerodynamic centre & centre of pressure|Zero-lift angle & lift-curve slope|Stall angle'],
  26: ['aero', 'Circulation & Kutta condition|Kutta–Joukowski theorem|Thin-airfoil theory'],
  27: ['aero', 'Parasite & induced drag|Wave drag|Drag polar|Minimum drag & max L/D'],
  28: ['aero', 'Aspect ratio & wing loading|Taper, sweep, dihedral|Downwash & induced angle|Wing-tip vortices|Oswald efficiency'],
  29: ['aero', 'Lifting-line theory|Elliptical lift distribution|Span efficiency|Planform effects'],
  30: ['aero', 'Transition & skin friction on wings|Stall mechanisms|Stall warning & recovery'],
  31: ['aero', 'Flaps (plain/split/slotted/Fowler)|Leading-edge slats & slots|Spoilers & speed brakes'],
  32: ['aero', 'Thrust & power required/available|Minimum drag speed|Glide angle & best glide'],
  33: ['aero', 'Climb performance|Absolute & service ceiling|Range & endurance|Propeller vs jet performance'],
  34: ['aero', 'Take-off & landing distances|Ground effect|Turning flight, bank angle & load factor'],
  35: ['aero', 'V–n diagram|Limit & ultimate load|Manoeuvring & gust envelope'],
  36: ['aero', 'Static vs dynamic stability|CG & neutral point|Static margin|Tail contribution & trim'],
  37: ['aero', 'Dihedral effect|Weathercock stability|Aileron & rudder effectiveness|Adverse yaw'],
  38: ['aero', 'Phugoid & short-period modes|Dutch roll, roll subsidence, spiral|Tabs & powered controls|Stability augmentation'],
  39: ['aero', 'Critical Mach number|Drag divergence|Transonic flow|Supersonic airfoils & area rule'],
  40: ['aero', '(Aero mega test — no topics)'],
  41: ['structures', "Normal & shear stress/strain|Hooke's law & elastic constants|Principal stresses & Mohr circle"],
  42: ['structures', 'SFD & BMD|Flexure formula & section modulus|Shear-stress distribution|Deflection'],
  43: ['structures', 'Torsion equation|Open/closed thin-walled sections|Shear flow & shear centre|Bredt–Batho'],
  44: ['structures', 'Aerodynamic, inertia, manoeuvre & gust loads|Pressurisation loads|Load factor & load paths'],
  45: ['structures', 'Spars, ribs, stringers, skin|Torsion box & stressed-skin|Fuel tank integration'],
  46: ['structures', 'Monocoque & semi-monocoque|Frames, bulkheads, longerons|Pressure cabin'],
  47: ['structures', 'Aluminium, steel, titanium, Mg, Ni alloys|Composites & sandwich construction|Material selection'],
  48: ['structures', 'S–N curve, HCF/LCF fatigue|Stress concentration & fracture toughness|Creep|Safe-life, fail-safe, damage tolerance'],
  49: ['structures', 'Euler buckling & effective length|Plate & local buckling|Post-buckling'],
  50: ['structures', 'Strain gauges & gauge factor|Bridge circuits & Wheatstone bridge'],
  51: ['structures', 'Strain rosettes|Photoelasticity|Brittle coating & moiré'],
  52: ['structures', 'Kirchhoff plate theory|Plate bending & boundary conditions|Rectangular/circular plates'],
  53: ['structures', 'Membrane theory|Cylindrical & spherical shells|Thin pressure vessels|Shell buckling'],
  54: ['structures', 'NDT: dye penetrant, MPI, ultrasonic, radiography, eddy current|Bond testing'],
  55: ['structures', '(Structures test — no topics)'],
  56: ['propulsion', 'First & second laws, enthalpy, entropy|Ideal-gas & isentropic processes|Nozzle/diffuser thermodynamics'],
  57: ['propulsion', 'Ideal Brayton cycle & pressure ratio|Compressor & turbine work|Back-work ratio & thermal efficiency|Regeneration, intercooling, reheating'],
  58: ['propulsion', 'Four-stroke engine & Otto cycle|Carburetion & fuel injection|Ignition/magneto|Supercharging & turbocharging|Detonation & pre-ignition'],
  59: ['propulsion', 'Intake/diffuser|Compressor|Combustion chamber|Turbine|Exhaust/nozzle|Accessory gearbox & engine stations'],
  60: ['propulsion', 'Momentum & pressure thrust|Gross/net thrust & specific thrust|TSFC|Propulsive/thermal/overall efficiency'],
  61: ['propulsion', 'Low-bypass vs high-bypass|Fan pressure ratio|Bypass ratio & thrust contribution|Civil vs military applications'],
  62: ['propulsion', 'Turboprop & turboshaft|Free turbine|Ramjet principle|Scramjet principle|Rocket propulsion orientation'],
  63: ['propulsion', 'Axial compressor|Centrifugal compressor|Compressor pressure ratio & maps|Stall, surge, rotating stall|Inlet/diffuser performance|Axial & centrifugal compressors'],
  64: ['propulsion', 'Combustion chambers & flame stability|Turbine cooling & work|Nozzle choking & C-D nozzles|Engine matching|Afterburner & thrust augmentation'],
  65: ['propulsion', 'Propeller geometry & pitch|Advance ratio|Propeller efficiency|Fixed/variable/constant-speed props|Feathering & reversing'],
  66: ['systems', 'Hydraulic systems: reservoir, pumps, accumulators, actuators|Pressure regulation & failures'],
  67: ['systems', 'Pneumatic & bleed-air systems|Air-cycle applications|Anti-ice & de-icing|Rain removal'],
  68: ['systems', 'Fuel tanks, venting, boost pumps|Cross-feed & transfer|Fuel quantity indication|Refuelling & contamination'],
  69: ['systems', 'Wet/dry sump lubrication|Oil pumps, filters & cooling|Fire & smoke detection|Fire extinguishing & zones'],
  70: ['systems', 'DC & AC generation|Batteries, TRU, inverters|Busbars & essential buses|Electrical protection'],
  71: ['systems', 'Flight controls: aileron, elevator, rudder|Trim & tabs|Powered controls & artificial feel|Fly-by-wire & redundancy'],
  72: ['systems', 'Autopilot & flight director|Auto-throttle|Yaw damper|Automatic landing'],
  73: ['systems', 'Fixed/retractable gear & oleo strut|Uplock/downlock|Wheel brakes & anti-skid|Emergency extension'],
  74: ['systems', 'Air-cycle machine|Cabin pressurisation & outflow valve|Oxygen systems|Decompression'],
  75: ['systems', 'Pitot-static system|ASI, altimeter, VSI|IAS/CAS/EAS/TAS|Blockage effects'],
  76: ['systems', 'Gyroscopic rigidity & precession|Attitude & heading indicators|Turn coordinator & compass|Tachometer, EGT/ITT, fuel flow'],
  77: ['systems', 'Engineering drawings, fits & tolerances|Fasteners, rivets & locking devices|Bearings & gears'],
  78: ['systems', 'Drilling, reaming, welding, brazing|Sheet metal & riveting|Composite repair|Corrosion types & prevention'],
  79: ['systems', 'Scheduled vs unscheduled maintenance|Line vs base maintenance|Hard-time, on-condition, condition monitoring|Reliability programmes'],
  80: ['systems', '(Systems/maintenance test — no topics)'],
// __PART6__
  81: ['avionics', 'Analogue vs digital avionics|Sensors & signal conditioning|LRUs & redundancy|Data buses & ARINC 429|Integrated modular avionics'],
  82: ['avionics', 'VHF & HF communication|Frequency bands & AM basics|Antennas|SELCAL & emergency frequencies'],
  83: ['avionics', 'ADF/NDB|VOR radials, bearing & errors|DME & slant range'],
  84: ['avionics', 'ILS: localizer, glide slope, marker beacon|DME substitution|Approach categories'],
  85: ['avionics', 'GPS/GNSS & trilateration|Satellite geometry & error sources|RAIM|INS/IRS gyros & accelerometers|GPS/INS integration'],
  86: ['avionics', 'Primary radar|SSR & transponder Modes A/C/S|ADS-B|Weather radar|Radio altimeter'],
  87: ['avionics', 'TCAS/ACAS advisories|GPWS/EGPWS/TAWS|Windshear warning|FDR & CVR'],
  88: ['avionics', 'EFIS: PFD & ND|EICAS/ECAM|FMS|Air Data Computer|AHRS|Glass cockpit failure modes'],
  89: ['atc', 'Bluff-body flow & vortex shedding|Strouhal number|Wind loading & atmospheric boundary layer|Wind-tunnel testing|Aeroelasticity'],
  90: ['atc', 'ATS/ATC/FIS/alerting services|Controlled/uncontrolled airspace & FIR|ATS routes, control zones & terminal areas|VFR/IFR basics'],
  91: ['atc', 'Vertical/longitudinal/lateral separation|Radar surveillance separation|RVSM|Wake turbulence categories & separation|Flight levels & altimeter settings'],
  92: ['atc', 'ICAO flight plan fields|Route & fuel planning|Alternate aerodrome|SID/STAR/holding|Approach procedures|NOTAM & AIP'],
  93: ['atc', 'Runway numbering & markings|Runway/approach lights & PAPI/VASI|Taxiways & holding points|Runway strip, clearway, stopway|TORA/TODA/ASDA/LDA|Runway incursion/excursion'],
  94: ['atc', '(ATC/aerodrome test - no topics)'],
  95: ['rules', 'MoCA, DGCA, AAIB, AAI, BCAS roles|Indian civil-aviation legislation|Aircraft Rules 1937|Civil Aviation Requirements (CAR)|Airworthiness & licensing'],
  96: ['rules', 'Chicago Convention & ICAO structure|Annexes 6/8/10/11/13/14/19|Accident investigation definitions|Notification & investigation concepts|SSP & SMS'],
  97: ['rules', 'Human error, SHELL & Swiss-cheese models|CRM & TEM|Situational awareness & fatigue|Safety culture|Occurrence reporting|Risk matrix & SPIs'],
  98: ['rules', '(PYQ + error repair - no topics)'],
  99: ['rules', '(Full mock + rapid revision - no topics)'],
  100: ['rules', '(Final mock + revision book - no topics)'],
};

// Generator (old-site day 57-65) slugs -> verify those pages exist
const GEN_SLUGS = {
  'relief-valve-system-pressure-protection': 'systems',
  'actuator-linear-rotary-tandem': 'systems',
  'hydraulic-fluids-mil-o-5606-mil-o-83282-skydrol-500b-4-barco-882': 'systems',
  'landing-gear-retraction-extension-sequence-valves': 'systems',
  'brakes-anti-skid-autobrake-dunlop-brake-control': 'systems',
  'nose-wheel-steering-hydraulic-electric-pneumatic': 'systems',
  'depressurisation-engine-start-sequence': 'systems',
  'cooling-of-hydraulic-fluid-heat-exchanger-loop': 'systems',
  'ac-dc-power-generation-in-aircraft': 'systems',
  'transformer-rectifier-unit-tru-3-phase-to-dc': 'systems',
  'dc-machine-lap-wound-armature-emf-calculation': 'systems',
  'commutator-function-in-dc-generator': 'systems',
  'compound-generator-speed-packaging-limitation': 'systems',
  'magnetically-coupled-coils-inductance-calculation': 'systems',
  'ac-frequency-cycles-per-time-calculation': 'systems',
  'bjt-biasing-saturation-voltage-base-current': 'systems',
  'logic-gates-and-or-not-boolean-algebra': 'systems',
  'number-system-conversion-octal-decimal-binary': 'systems',
  'bleed-air-source-high-pressure-compressor': 'systems',
  'air-cycle-refrigeration-bootstrap-cycle': 'systems',
  'cabin-pressurisation-outflow-valve-differential-pressure': 'systems',
  'humidity-control-dehumidifiers-separators': 'systems',
  'pressure-regulator-unloading-valve': 'systems',
  'gaseous-oxygen-system-high-pressure-cylinders': 'systems',
  'lox-liquid-oxygen-system-combat-aircraft': 'systems',
  'hypoxia-symptoms-altitude-thresholds': 'systems',
  'pressure-regulating-valve-in-o2-system': 'systems',
  'fuel-booster-pumps-cavitation-prevention': 'systems',
  'fuel-temperature-at-altitude-effect-on-system': 'systems',
  'engine-feed-pumps-purpose-aeration-cavitation': 'systems',
  'thermal-de-icing-hot-bleed-air-system': 'systems',
  'pneumatic-boots-inflation-cycle': 'systems',
  'windscreen-wipers-limitation-on-plastic': 'systems',
  'windscreen-misting-fogging-at-altitude': 'systems',
  'primary-control-surfaces-aileron-elevator-rudder': 'systems',
  'control-axes-roll-aileron-pitch-elevator-yaw-rudder': 'systems',
  'fly-by-wire-fbw-first-aircraft-airbus-a320': 'systems',
  'fadec-full-authority-digital-engine-control': 'systems',
  'spoiler-function-on-landing-lift-dump-drag': 'systems',
  'flap-types-and-effect-on-landing-distance': 'systems',
  'airspeed-indicator-asi-pitot-static': 'systems',
  'altimeter-pressure-altitude-encoding': 'systems',
  'attitude-indicator-artificial-horizon': 'systems',
  'heading-indicator-directional-gyro': 'systems',
  'turn-coordinator-turn-and-slip-indicator': 'systems',
  'vertical-speed-indicator-vsi': 'systems',
  'manifold-pressure-gauge-fuel-oil-pressure-instrument': 'systems',
  'ratiometer-pressure-indicator': 'systems',
  'adf-loop-antenna-sense-antenna-bearing-indicator': 'systems',
  'vor-ground-transmitter-obs-cdi-short-range': 'systems',
  'ils-localizer-glideslope-marker-beacons-3-transmitters': 'systems',
  'dme-uhf-range-960-1215-mhz-receiving-range': 'systems',
  'gps-pseudo-range-concept-satellite-geometry': 'systems',
  'gps-receiver-components-antenna-processor-clock': 'systems',
};

let totTopics = 0, totCovered = 0; const missingBySubject = {};
const lines = [];
for (const d of Object.keys(PLAN).map(Number)) {
  const [pill, topics] = PLAN[d];
  const list = topics.split('|');
  let cov = 0; const miss = [];
  for (const t of list) {
    if (t.startsWith('(')) continue;
    totTopics++;
    const ref = M[t];
    let ok = false;
    if (ref) {
      const [p, slug] = ref.split(':');
      if (folders[p] && folders[p].has(slug)) ok = true;
      else console.log('MAPPED-BUT-MISSING-FOLDER:', t, '->', slug);
    }
    if (ok) cov++; else { miss.push(t); (missingBySubject[pill] = missingBySubject[pill] || []).push('Day ' + d + ': ' + t); }
  }
  totCovered += cov;
  lines.push('Day ' + String(d).padStart(3) + ' [' + pill.padEnd(10) + '] ' + cov + '/' + list.length + (miss.length ? '  missing: ' + miss.join('; ') : ''));
}
console.log(lines.join('\n'));
console.log('');
console.log('=== SUMMARY (100-day plan topics) ===');
console.log('Topics total: ' + totTopics + ' | with folders: ' + totCovered + ' | missing: ' + (totTopics - totCovered) + ' (' + Math.round(100 * (totTopics - totCovered) / totTopics) + '%)');
for (const [p, arr] of Object.entries(missingBySubject)) console.log('  ' + p + ': ' + arr.length + ' topics without folders');
console.log('');
console.log('=== Generator day-57-65 pages on disk ===');
let gOk = 0; const gMiss = [];
for (const [slug, p] of Object.entries(GEN_SLUGS)) {
  if (folders[p] && folders[p].has(slug)) gOk++; else gMiss.push(slug);
}
console.log('generator slugs on disk: ' + gOk + '/' + Object.keys(GEN_SLUGS).length + (gMiss.length ? ' | MISSING: ' + gMiss.join(', ') : ''));
console.log('');
console.log('=== Orphan folders (on disk but not mapped to any plan topic) ===');
const mapped = new Set(Object.values(M).concat(Object.entries(GEN_SLUGS).map(([s2, p]) => p + ':' + s2)));
for (const [k, set] of Object.entries(folders)) {
  const orphans = [...set].filter(s3 => !mapped.has(k + ':' + s3));
  console.log(k + ': ' + orphans.length + ' orphans' + (orphans.length ? ': ' + orphans.join(', ') : ''));
}
