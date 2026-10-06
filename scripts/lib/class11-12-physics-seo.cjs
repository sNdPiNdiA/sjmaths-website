const fs = require('node:fs');
const path = require('node:path');
const {ROOT, setMetadata} = require('../seo-html.cjs');

const rows = [
  ['class-11-physics/index.html','Class 11 Physics','Class 11 Physics NCERT Solutions, Notes, Formulas & Tests | SJMaths','Study all 14 NCERT Class 11 Physics chapters with clear concepts, formula derivations, worked examples and practice for CBSE exams.'],
  ['class-11-physics/chapter-1-units-and-measurements/index.html','Units and Measurements','Class 11 Physics Chapter 1: Units and Measurements | NCERT Notes & Solutions | SJMaths','Review SI units, measurement errors, significant figures and dimensional analysis with clear notes, worked examples and NCERT exercises.'],
  ['class-11-physics/chapter-2-motion-in-a-straight-line/index.html','Motion in a Straight Line','Class 11 Physics Chapter 2: Motion in a Straight Line | NCERT Notes & Solutions | SJMaths','Study position, velocity, acceleration, motion graphs, free fall and relative motion through concise notes, solved examples and NCERT exercises.'],
  ['class-11-physics/chapter-3-motion-in-a-plane/index.html','Motion in a Plane','Class 11 Physics Chapter 3: Motion in a Plane | Vectors & Projectile Motion | SJMaths','Learn vectors, projectile motion and circular motion with clear derivations, worked examples and NCERT practice for Class 11 Physics.'],
  ['class-11-physics/chapter-4-laws-of-motion/index.html','Laws of Motion','Class 11 Physics Chapter 4: Laws of Motion | NCERT Notes & Solutions | SJMaths','Understand Newton’s laws, momentum, friction and circular motion with worked examples and NCERT exercise solutions.'],
  ['class-11-physics/chapter-5-work-energy-power/index.html','Work, Energy and Power','Class 11 Physics Chapter 5: Work, Energy and Power | NCERT Notes & Solutions | SJMaths','Study work by constant and variable forces, kinetic energy, power and collisions with concise notes and solved NCERT questions.'],
  ['class-11-physics/chapter-6-systems-of-particles-and-rotational-motion/index.html','Systems of Particles and Rotational Motion','Class 11 Physics Chapter 6: Systems of Particles and Rotational Motion | NCERT Solutions | SJMaths','Learn centre of mass, torque, angular momentum, moment of inertia and rotational dynamics through derivations and worked problems.'],
  ['class-11-physics/chapter-7-gravitation/index.html','Gravitation','Class 11 Physics Chapter 7: Gravitation | NCERT Notes & Solutions | SJMaths','Explore Newtonian gravitation, Kepler’s laws, variation in g, escape speed and satellite motion with examples and NCERT exercises.'],
  ['class-11-physics/chapter-8-mechanical-properties-of-solids/index.html','Mechanical Properties of Solids','Class 11 Physics Chapter 8: Mechanical Properties of Solids | NCERT Solutions | SJMaths','Review stress, strain, elasticity and elastic moduli with derivations, worked examples and NCERT exercise solutions.'],
  ['class-11-physics/chapter-9-mechanical-properties-of-fluids/index.html','Mechanical Properties of Fluids','Class 11 Physics Chapter 9: Mechanical Properties of Fluids | NCERT Solutions | SJMaths','Study pressure, buoyancy, fluid flow, viscosity and surface tension with concise notes, worked examples and NCERT solutions.'],
  ['class-11-physics/chapter-10-thermal-properties-of-matter/index.html','Thermal Properties of Matter','Class 11 Physics Chapter 10: Thermal Properties of Matter | NCERT Notes & Solutions | SJMaths','Learn temperature, thermal expansion, calorimetry, phase changes and heat transfer with clear explanations and solved NCERT exercises.'],
  ['class-11-physics/chapter-11-thermodynamics/index.html','Thermodynamics','Class 11 Physics Chapter 11: Thermodynamics | NCERT Notes & Solutions | SJMaths','Understand heat, work, thermodynamic laws, gas processes and heat engines through derivations, examples and revision questions.'],
  ['class-11-physics/chapter-12-kinetic-theory/index.html','Kinetic Theory','Class 11 Physics Chapter 12: Kinetic Theory | NCERT Notes & Solutions | SJMaths','Connect molecular motion to gas pressure, temperature, molecular speeds, heat capacities and mean free path with worked examples.'],
  ['class-11-physics/chapter-13-oscillations/index.html','Oscillations','Class 11 Physics Chapter 13: Oscillations | SHM Notes & NCERT Solutions | SJMaths','Build simple harmonic motion from its equation, then study phase, energy, restoring forces and the small-angle pendulum.'],
  ['class-11-physics/chapter-14-waves/index.html','Waves','Class 11 Physics Chapter 14: Waves | NCERT Notes & Solutions | SJMaths','Learn progressive waves, sound speed, interference, standing waves, resonance and beats with examples and all 19 NCERT exercises.'],
  ['class-12-physics/index.html','Class 12 Physics','Class 12 Physics NCERT Solutions, Notes, Formulas & Tests | SJMaths','Explore Class 12 Physics chapter notes, derivations, solved examples, exercises and previous-year questions for CBSE revision.'],
  ['class-12-physics/chapter-1-electric-fields-and-charges/index.html','Electric Charges and Fields','Class 12 Physics Chapter 1: Electric Charges and Fields | NCERT Solutions | SJMaths','Study Coulomb’s law, electric fields, dipoles, flux and Gauss’s law with derivations, examples and NCERT exercise solutions.'],
  ['class-12-physics/chapter-2-electrostatic-potential-and-capacitance/index.html','Electrostatic Potential and Capacitance','Class 12 Physics Chapter 2: Electrostatic Potential and Capacitance | NCERT Solutions | SJMaths','Learn electric potential, potential energy, equipotential surfaces, capacitors and dielectrics with solved examples and NCERT practice.'],
  ['class-12-physics/chapter-3-current-electricity/index.html','Current Electricity','Class 12 Physics Chapter 3: Current Electricity | NCERT Notes & Solutions | SJMaths','Review current, drift velocity, resistance, Kirchhoff’s laws and Wheatstone bridge with clear notes and worked NCERT examples.'],
  ['class-12-physics/chapter-4-moving-charges-and-magnetism/index.html','Moving Charges and Magnetism','Class 12 Physics Chapter 4: Moving Charges and Magnetism | NCERT Solutions | SJMaths','Understand magnetic forces, charged-particle motion, Biot–Savart and Ampere’s laws, solenoids and galvanometers.'],
  ['class-12-physics/chapter-5-magnetism-and-matter/index.html','Magnetism and Matter','Class 12 Physics Chapter 5: Magnetism and Matter | NCERT Notes & Solutions | SJMaths','Study bar magnets, magnetic dipoles, magnetisation, susceptibility and magnetic materials with worked examples and NCERT questions.'],
  ['class-12-physics/chapter-6-electromagnetic-induction/index.html','Electromagnetic Induction','Class 12 Physics Chapter 6: Electromagnetic Induction | NCERT Solutions | SJMaths','Learn magnetic flux, Faraday’s and Lenz’s laws, motional EMF and inductance through concise notes and solved numericals.'],
  ['class-12-physics/chapter-7-alternating-current/index.html','Alternating Current','Class 12 Physics Chapter 7: Alternating Current | NCERT Notes & Solutions | SJMaths','Explore AC circuits, impedance, resonance, power factor and transformers with derivations, examples and NCERT exercises.'],
  ['class-12-physics/chapter-8-electromagnetic-waves/index.html','Electromagnetic Waves','Class 12 Physics Chapter 8: Electromagnetic Waves | NCERT Notes & Solutions | SJMaths','Review displacement current, electromagnetic wave properties and the spectrum with concise notes, applications and solved questions.'],
  ['class-12-physics/chapter-9-ray-optics-and-optical-instruments/index.html','Ray Optics and Optical Instruments','Class 12 Physics Chapter 9: Ray Optics and Optical Instruments | NCERT Solutions | SJMaths','Study reflection, refraction, lenses, prisms, optical fibres, microscopes and telescopes with notes and NCERT exercise solutions.'],
  ['class-12-physics/chapter-10-wave-optics/index.html','Wave Optics','Class 12 Physics Chapter 10: Wave Optics | NCERT Notes & Solutions | SJMaths','Learn Huygens’ principle, interference, Young’s double-slit experiment and diffraction with derivations and solved NCERT problems.'],
  ['class-12-physics/chapter-11-dual-nature-of-radiation-and-matter/index.html','Dual Nature of Radiation and Matter','Class 12 Physics Chapter 11: Dual Nature of Radiation and Matter | NCERT Solutions | SJMaths','Understand the photoelectric effect, Einstein’s equation, threshold frequency and de Broglie matter waves with worked examples.'],
  ['class-12-physics/chapter-12-atoms/index.html','Atoms','Class 12 Physics Chapter 12: Atoms | Bohr Model & NCERT Solutions | SJMaths','Study Rutherford scattering, Bohr’s model, hydrogen energy levels and spectral series with clear explanations and solved exercises.'],
  ['class-12-physics/chapter-13-nuclei/index.html','Nuclei','Class 12 Physics Chapter 13: Nuclei | NCERT Notes & Solutions | SJMaths','Review nuclear composition, mass defect, binding energy, nuclear forces, fission and fusion with worked examples and NCERT practice.'],
  ['class-12-physics/chapter-14-semiconductor-electronics/index.html','Semiconductor Electronics','Class 12 Physics Chapter 14: Semiconductor Electronics | NCERT Notes & Solutions | SJMaths','Learn energy bands, semiconductors, p–n junctions, biasing and rectifiers with diagrams, examples and NCERT exercise solutions.']
].map(([file,topic,title,description])=>({file,topic,title,description}));

function imagePath(row){
  const stem=row.file.replace(/\/index\.html$/,'').replace(/\//g,'-');
  return `/assets/images/og/physics/${stem}.png`;
}
function applyPhysicsSeo(source,row){
  const canonical=`https://sjmaths.com/${row.file.replace(/\/index\.html$/,'/')}`;
  const image=`https://sjmaths.com${imagePath(row)}`;
  const alt=`SJMaths ${row.topic} — Physics study notes and NCERT solutions`;
  return setMetadata(source,{
    title:row.title,description:row.description,canonical,
    'og:title':row.title,'og:description':row.description,'og:url':canonical,
    'og:image':image,'og:image:type':'image/png','og:image:width':'1200','og:image:height':'630','og:image:alt':alt,
    'twitter:card':'summary_large_image','twitter:title':row.title,
    'twitter:description':row.description,'twitter:image':image,'twitter:image:alt':alt
  });
}

function applyAll(){
  for(const row of rows){
    const file=path.join(ROOT,row.file);
    if(!fs.existsSync(file))throw new Error(`Missing Physics page: ${row.file}`);
    if(!fs.existsSync(path.join(ROOT,imagePath(row).slice(1))))throw new Error(`Missing social image for ${row.file}`);
    const old=fs.readFileSync(file,'utf8'),next=applyPhysicsSeo(old,row);
    if(next!==old)fs.writeFileSync(file,next,'utf8');
  }
  const indexPath=path.join(ROOT,'assets/js/search-index.json');
  const index=JSON.parse(fs.readFileSync(indexPath,'utf8'));
  for(const row of rows){
    const route=`/${row.file.replace(/\/index\.html$/,'/')}`;
    const entry=index.find(item=>item.url===route);
    if(entry)entry.title=row.title.replace(/\s*\|\s*SJMaths$/,'');
  }
  fs.writeFileSync(indexPath,JSON.stringify(index,null,2)+'\n','utf8');
  return rows.length;
}
function applyOne(file){
  const row=rows.find(item=>item.file===file);
  if(!row)throw new Error(`No Physics SEO record for ${file}`);
  const target=path.join(ROOT,row.file);
  if(!fs.existsSync(target))throw new Error(`Missing Physics page: ${row.file}`);
  if(!fs.existsSync(path.join(ROOT,imagePath(row).slice(1))))throw new Error(`Missing social image for ${row.file}`);
  const old=fs.readFileSync(target,'utf8'),next=applyPhysicsSeo(old,row);
  if(next!==old)fs.writeFileSync(target,next,'utf8');
  return row;
}
module.exports={rows,imagePath,applyPhysicsSeo,applyAll,applyOne};
