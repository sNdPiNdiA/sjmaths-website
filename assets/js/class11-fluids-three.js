/* Purposeful, lazy-initialised Three.js models for fluid mechanics. */
(() => {
  'use strict';
  if (!window.THREE) return;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const emerald = 0x059669, amber = 0xd97706, water = 0x38bdf8;
  const material = (color, extra={}) => new THREE.MeshStandardMaterial({color, roughness:.55, ...extra});
  function mount(card) {
    const host=card.querySelector('.fluid-sim-canvas'), fallback=card.querySelector('.fluid-sim-fallback');
    if(!host||!fallback) return;
    let renderer;
    try { renderer=new THREE.WebGLRenderer({antialias:true,alpha:false,powerPreference:'low-power'}); } catch { return; }
    const scene=new THREE.Scene(); scene.background=new THREE.Color(0xf8fafc);
    scene.add(new THREE.HemisphereLight(0xffffff,0xcbd5e1,1.25));
    const light=new THREE.DirectionalLight(0xffffff,1.35); light.position.set(4,6,7); scene.add(light);
    const camera=new THREE.PerspectiveCamera(34,1,.1,40); camera.position.set(0,3.1,7.6); camera.lookAt(0,0,0);
    renderer.setPixelRatio(Math.min(devicePixelRatio||1,1.5)); renderer.domElement.setAttribute('aria-hidden','true'); renderer.domElement.tabIndex=-1; host.append(renderer.domElement);
    const kind=card.dataset.fluidSim, slider=card.querySelector('input[type=range]'), output=card.querySelector('output'), readout=card.querySelector('[data-fluid-readout]'), play=card.querySelector('[data-fluid-play]');
    const objects=[], tracers=[];
    const add=(geo,mat,x,y,z)=>{const mesh=new THREE.Mesh(geo,mat);mesh.position.set(x,y,z);scene.add(mesh);objects.push(mesh);return mesh;};
    const tubeMat=material(0x94a3b8,{metalness:.22,transparent:true,opacity:.75});
    if(kind==='continuity'||kind==='bernoulli'){
      const left=add(new THREE.CylinderGeometry(.72,.72,2.5,28,1,true),tubeMat,-2.3,0,0); left.rotation.z=Math.PI/2;
      const throat=add(new THREE.CylinderGeometry(.43,.72,1.8,28,1,true),tubeMat,-.15,0,0); throat.rotation.z=Math.PI/2;
      const right=add(new THREE.CylinderGeometry(.72,.43,1.8,28,1,true),tubeMat,1.65,0,0); right.rotation.z=Math.PI/2;
      const axis=add(new THREE.CylinderGeometry(.025,.025,6.5,12),material(emerald),0,-.16,0); axis.rotation.z=Math.PI/2;
      for(let i=0;i<9;i++){const bead=add(new THREE.SphereGeometry(.095,14,10),material(i%2?amber:emerald),-2.8+i*.65,.04,(i%3-1)*.12);tracers.push(bead);}
      if(kind==='bernoulli'){
        for(const x of [-1.85,1.25]){
          add(new THREE.CylinderGeometry(.045,.045,.55,12),material(0x475569),x,.32,0);
          const column=add(new THREE.CylinderGeometry(.11,.11,.55,18),material(x<0?0xfbbf24:water,{transparent:true,opacity:.75}),x,.72,0);column.userData.pressureColumn=true;
        }
      }
    } else {
      // Open reservoir, glass capillary and an adjustable water column.
      const capillary=add(new THREE.CylinderGeometry(.17,.17,3.7,24,1,true),material(0x64748b,{transparent:true,opacity:.48}),0,0,0);
      const pool=add(new THREE.CylinderGeometry(2.4,2.4,.18,48),material(water,{transparent:true,opacity:.65}),0,-1.5,0);
      const column=add(new THREE.CylinderGeometry(.105,.105,1,22),material(water,{transparent:true,opacity:.82}),0,-1,0); column.userData.column=true;
    }
    const resize=()=>{const w=Math.max(1,host.clientWidth),h=Math.max(1,host.clientHeight);renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix();};
    const observer=new ResizeObserver(resize); observer.observe(host); resize();
    let raf=0, running=false, time=0;
    function update(){
      const value=Number(slider.value), ratio=Math.max(.35,Math.min(1,value));
      if(output) output.textContent=kind==='capillary'?`${value.toFixed(1)} mm`:`A₂/A₁ = ${ratio.toFixed(2)}`;
      if(kind==='continuity') readout.textContent=`Throat speed is ${(1/ratio).toFixed(2)}× the wide-section speed (A₁v₁=A₂v₂).`;
      if(kind==='bernoulli') readout.textContent=`At the throat, v₂/v₁=${(1/ratio).toFixed(2)} and pressure head falls as speed rises.`;
      if(kind==='capillary'){
        const radius=value/1000, height=2*.073/(1000*9.8*radius); const column=objects.find(o=>o.userData.column);
        if(column){const display=Math.min(2.2,Math.max(.25,height*22));column.scale.y=display;column.position.y=-1.41+display/2;}
        readout.textContent=`Ideal water rise h=${(height*100).toFixed(1)} cm for θ≈0° (shown height is scaled).`;
      }
      for(const mesh of objects) if(mesh.userData.pressureColumn){mesh.scale.y=mesh.position.x<0?1.3:Math.max(.45,1.5*ratio);}
      renderer.render(scene,camera);
    }
    function frame(){if(!running)return;time+=.012;const speed=(kind==='bernoulli'?1.1:1)/Math.max(.35,Number(slider.value));tracers.forEach((p,i)=>{p.position.x=((i*.74+time*speed)%6)-3;});renderer.render(scene,camera);raf=requestAnimationFrame(frame);}
    slider.addEventListener('input',update); update();
    if(kind==='capillary'&&play)play.hidden=true;
    if(play){play.addEventListener('click',()=>{running=!running;play.setAttribute('aria-pressed',String(running));play.textContent=running?'Pause flow':'Start flow';if(running&&!reduceMotion.matches)frame();else{cancelAnimationFrame(raf);renderer.render(scene,camera);}});}
    reduceMotion.addEventListener('change',()=>{if(reduceMotion.matches){running=false;cancelAnimationFrame(raf);if(play){play.setAttribute('aria-pressed','false');play.textContent='Start flow';}}});
    let resumeAfterCache=false;
    const dispose=()=>{running=false;cancelAnimationFrame(raf);observer.disconnect();slider.removeEventListener('input',update);window.removeEventListener('pagehide',onPageHide);window.removeEventListener('pageshow',onPageShow);objects.forEach(m=>{m.geometry.dispose();if(Array.isArray(m.material))m.material.forEach(x=>x.dispose());else m.material.dispose();scene.remove(m);});renderer.dispose();renderer.domElement.remove();};
    const onPageHide=event=>{if(event.persisted){resumeAfterCache=running;running=false;cancelAnimationFrame(raf);return;}dispose();};
    const onPageShow=event=>{if(!event.persisted)return;resize();renderer.render(scene,camera);if(resumeAfterCache&&!reduceMotion.matches){running=true;frame();}resumeAfterCache=false;};
    window.addEventListener('pagehide',onPageHide);
    window.addEventListener('pageshow',onPageShow);
    fallback.hidden=true;host.hidden=false;
  }
  const cards=[...document.querySelectorAll('.fluid-sim')];
  if(!cards.length)return;
  const start=()=>{if(!window.IntersectionObserver){cards.forEach(mount);return;}const io=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){io.unobserve(e.target);mount(e.target);}}),{rootMargin:'160px'});cards.forEach(card=>io.observe(card));};
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start,{once:true});else start();
})();
