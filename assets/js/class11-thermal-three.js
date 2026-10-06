/* Four lazy, user-controlled Three.js models for thermal physics. */
(() => {
  'use strict';
  if (!window.THREE) return;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const colors = {hot:0xdc5a27,warm:0xf59e0b,cool:0x38bdf8,green:0x059669,dark:0x334155};
  const mat = (color, extra={}) => new THREE.MeshStandardMaterial({color,roughness:.58,...extra});
  const cards=[...document.querySelectorAll('.thermal-sim-card')];
  if(!cards.length)return;

  function mount(card){
    const host=card.querySelector('.thermal-sim-canvas'), fallback=card.querySelector('.thermal-sim-fallback');
    if(!host||!fallback)return;
    let renderer;
    try{renderer=new THREE.WebGLRenderer({antialias:true,alpha:false,powerPreference:'low-power'});}catch{return;}
    const scene=new THREE.Scene();scene.background=new THREE.Color(0xf8fafc);
    scene.add(new THREE.HemisphereLight(0xffffff,0xcbd5e1,1.3));
    const light=new THREE.DirectionalLight(0xffffff,1.2);light.position.set(4,6,7);scene.add(light);
    const camera=new THREE.PerspectiveCamera(36,1,.1,50);camera.position.set(0,2.5,7.5);camera.lookAt(0,0,0);
    renderer.setPixelRatio(Math.min(devicePixelRatio||1,1.5));renderer.domElement.setAttribute('aria-hidden','true');renderer.domElement.tabIndex=-1;host.append(renderer.domElement);
    const kind=card.dataset.thermalSim,slider=card.querySelector('input[type=range]'),out=card.querySelector('output'),readout=card.querySelector('[data-thermal-readout]'),play=card.querySelector('[data-thermal-play]');
    const objects=[],moving=[];
    const add=(geometry,material,x=0,y=0,z=0)=>{const mesh=new THREE.Mesh(geometry,material);mesh.position.set(x,y,z);scene.add(mesh);objects.push(mesh);return mesh;};
    const sphere=(x,y,z,color,r=.11)=>add(new THREE.SphereGeometry(r,14,10),mat(color),x,y,z);
    if(kind==='expansion'){
      const fixed=sphere(-2.2,0,0,colors.dark,.16);fixed.scale.set(.65,2.8,1);
      const rod=add(new THREE.BoxGeometry(3.2,.46,.5),mat(colors.warm,{metalness:.2}),-.4,0,0);rod.userData.thermalRod=true;
      const end=add(new THREE.BoxGeometry(.18,1.5,.8),mat(colors.dark),1.24,0,0);end.userData.thermalEnd=true;
      for(let i=0;i<9;i++){const p=sphere(-1.75+i*.34,.39,.02,i%2?colors.hot:colors.warm,.08);p.userData.index=i;p.userData.homeY=.39;moving.push(p);}
    }else if(kind==='phase'){
      for(let i=0;i<25;i++){const x=(i%5-2)*.4,y=(Math.floor(i/5)-2)*.34;const p=sphere(x,y,0,colors.cool,.105);p.userData.particle=i;p.userData.homeX=x;p.userData.homeY=y;moving.push(p);}
      add(new THREE.BoxGeometry(2.2,.12,.8),mat(colors.dark),0,-1.05,0);
    }else if(kind==='transfer'){
      add(new THREE.BoxGeometry(.55,1.5,.75),mat(colors.hot),-2.35,0,0);
      add(new THREE.BoxGeometry(.55,1.5,.75),mat(colors.cool),2.35,0,0);
      for(let i=0;i<7;i++){const p=sphere(-1.6+i*.53,0,0,i<3?colors.hot:colors.warm,.16);p.userData.index=i;moving.push(p);}
      for(let i=0;i<5;i++){const p=sphere(-.9+(i%3)*.8,-.2+Math.floor(i/3)*.5,.42,colors.cool,.09);p.userData.convection=i;moving.push(p);}
      const rays=[];for(let i=0;i<4;i++)rays.push(add(new THREE.CylinderGeometry(.025,.025,2.5,8),mat(colors.warm,{emissive:colors.warm,emissiveIntensity:.3}),0,.18,(i-1.5)*.17));
      rays.forEach((r,i)=>{r.rotation.z=Math.PI/2;r.userData.ray=i;});
    }else if(kind==='cooling'){
      const body=sphere(0,0,0,colors.hot,.9);body.userData.coolingBody=true;
      add(new THREE.CylinderGeometry(2.1,2.1,.1,48),mat(colors.cool,{transparent:true,opacity:.25}),0,-1.4,0);
      for(let i=0;i<8;i++){const p=sphere(Math.cos(i*Math.PI/4)*2.3,Math.sin(i*Math.PI/4)*1.25,0,colors.cool,.08);p.userData.ambient=true;}
    }
    const resize=()=>{const w=Math.max(1,host.clientWidth),h=Math.max(1,host.clientHeight);renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix();};
    const observer=new ResizeObserver(resize);observer.observe(host);resize();
    let raf=0,running=false,elapsed=0,visible=true;
    const modeButtons=[...card.querySelectorAll('[data-thermal-mode]')];let mode='conduction';
    function update(){
      const value=Number(slider?.value||0);
      if(kind==='expansion'){
        const scale=1+0.000012*value*110;
        const rod=objects.find(o=>o.userData.thermalRod),end=objects.find(o=>o.userData.thermalEnd);
        if(rod){rod.scale.x=scale;rod.position.x=-.4+(scale-1)*1.6;}
        if(end)end.position.x=1.24+(scale-1)*3.2;
        if(out)out.textContent=`ΔT = ${value} °C`;
        readout.textContent=`For steel, ΔL/L = αΔT = 1.2×10⁻⁵ × ${value}; the drawn change is enlarged so it is visible.`;
      }else if(kind==='phase'){
        const f=value/100, melting=f>=.25&&f<=.5, boiling=f>=.75;
        moving.forEach((p,i)=>{const x=(i%5-2)*.4,y=(Math.floor(i/5)-2)*.34;
          if(f<.25){p.position.set(x,y,0);p.material.color.setHex(colors.cool);}
          else if(melting){const liquid=(i/24-Math.max(0,(f-.25)/.25))<.5;p.position.set(liquid?x*.9:x,y+(liquid?Math.sin(i*2)*.08:0),liquid?.25:0);p.material.color.setHex(liquid?colors.cool:0xffffff);}
          else if(f<.75){p.position.set(x*.92,y*.92,.2);p.material.color.setHex(colors.cool);}
          else{const spread=(f-.75)*3;p.position.set(x+(i%2?spread:-spread),y+(i%3-1)*spread,.2);p.material.color.setHex(colors.hot);}
        });
        if(out)out.textContent=`Heat supplied: ${value}%`;
        readout.textContent=melting?'Melting plateau: ice and water coexist at 0 °C; added heat changes phase, not temperature.':boiling?'Boiling plateau: water and steam coexist at 100 °C; latent heat converts the liquid.':f<.25?`Ice warms from −20 °C toward 0 °C (model stage ${Math.round(f*100)}%).`:`Liquid water warms from 0 °C toward 100 °C (model stage ${Math.round((f-.5)*400)}%).`;
      }else if(kind==='transfer'){
        const active=mode;
        for(const p of moving){if(p.userData.index!==undefined)p.visible=active==='conduction';if(p.userData.convection!==undefined)p.visible=active==='convection';if(p.userData.ray!==undefined)p.visible=active==='radiation';}
        if(out)out.textContent=active[0].toUpperCase()+active.slice(1);
        readout.textContent=active==='conduction'?'Energy passes between neighbouring particles; the material itself has no bulk flow.':active==='convection'?'Warm, less-dense fluid rises while cooler fluid sinks: heat moves with the circulating matter.':'Thermal electromagnetic waves carry energy across space; a material medium is not required.';
      }else{
        const t=value,ambient=Number(card.querySelector('[data-ambient]')?.value||20),initial=100,k=.006;
        const temp=ambient+(initial-ambient)*Math.exp(-k*t),body=objects.find(o=>o.userData.coolingBody);
        if(body){const blend=Math.max(0,Math.min(1,(temp-ambient)/(initial-ambient)));body.material.color.setRGB(0.22+0.62*blend,0.48-0.12*blend,0.78-0.4*blend);}
        if(out)out.textContent=`T ≈ ${temp.toFixed(1)} °C`;
        readout.textContent=`Newton model: T(t)=Tₛ+(T₀−Tₛ)e⁻ᵏᵗ. At t=${t} min and Tₛ=${ambient} °C, T≈${temp.toFixed(1)} °C (illustrative k=${k} min⁻¹).`;
      }
      renderer.render(scene,camera);
    }
    function frame(){if(!running||!visible)return;elapsed+=.025;
      if(kind==='expansion'){const amplitude=.008+Number(slider.value)*.00016;moving.forEach(p=>{p.position.y=p.userData.homeY+amplitude*Math.sin(elapsed*5+p.userData.index);});}
      if(kind==='cooling'&&Number(slider.value)<Number(slider.max)){slider.value=String(Math.min(Number(slider.max),Number(slider.value)+1));update();if(Number(slider.value)>=Number(slider.max))stop();}
      if(kind==='transfer'&&mode==='conduction')moving.filter(p=>p.userData.index!==undefined).forEach((p,i)=>{p.position.y=.035*Math.sin(elapsed*5+i);});
      if(kind==='transfer'&&mode==='convection')moving.filter(p=>p.userData.convection!==undefined).forEach((p,i)=>{const a=elapsed+i*1.1;p.position.x=.95*Math.cos(a);p.position.y=.45+.55*Math.sin(a);});
      if(kind==='transfer'&&mode==='radiation')objects.filter(o=>o.userData.ray!==undefined).forEach(o=>o.scale.y=.72+.25*Math.sin(elapsed*3+o.userData.ray));
      if(kind==='phase'){const value=Number(slider.value)/100;if(valueInMeltingPlateau())moving.forEach((p,i)=>{if(i%2===0)p.position.set(p.userData.homeX+.025*Math.sin(elapsed*2+i),p.userData.homeY+.02*Math.cos(elapsed*2+i),.25);});else{const amplitude=.008+.035*Math.min(1,Math.max(0,value<.25?value*4:(value-.5)*4));moving.forEach((p,i)=>p.position.y=p.userData.homeY+amplitude*Math.sin(elapsed*4+i));}}
      renderer.render(scene,camera);raf=requestAnimationFrame(frame);
    }
    function valueInMeltingPlateau(){const n=Number(slider?.value||0);return kind==='phase'&&n>=25&&n<=50;}
    function stop(){running=false;cancelAnimationFrame(raf);if(play){play.setAttribute('aria-pressed','false');play.textContent='Play model';}}
    function togglePlay(){running=!running;play.setAttribute('aria-pressed',String(running));play.textContent=running?'Pause model':'Play model';if(running&&!reduced.matches&&visible)frame();else{cancelAnimationFrame(raf);renderer.render(scene,camera);}}
    slider?.addEventListener('input',update);card.querySelector('[data-ambient]')?.addEventListener('input',update);
    modeButtons.forEach(btn=>btn.addEventListener('click',()=>{mode=btn.dataset.thermalMode;modeButtons.forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));update();}));
    play?.addEventListener('click',togglePlay);
    const tabObserver=new MutationObserver(()=>{const active=card.closest('.tab')?.classList.contains('active');visible=Boolean(active);if(!visible){cancelAnimationFrame(raf);}else if(running&&!reduced.matches)frame();});
    const parentTab=card.closest('.tab');if(parentTab)tabObserver.observe(parentTab,{attributes:true,attributeFilter:['class']});
    const onMotion=()=>{if(play)play.disabled=reduced.matches;if(reduced.matches){cancelAnimationFrame(raf);running=false;if(play){play.setAttribute('aria-pressed','false');play.textContent='Play model';}}else if(running&&visible)frame();};reduced.addEventListener('change',onMotion);if(play)play.disabled=reduced.matches;
    let resume=false;
    const dispose=()=>{stop();observer.disconnect();tabObserver.disconnect();reduced.removeEventListener('change',onMotion);slider?.removeEventListener('input',update);card.querySelector('[data-ambient]')?.removeEventListener('input',update);objects.forEach(o=>{o.geometry.dispose();o.material.dispose();scene.remove(o);});renderer.dispose();renderer.domElement.remove();};
    const onHide=e=>{if(e.persisted){resume=running;cancelAnimationFrame(raf);return;}dispose();};
    const onShow=e=>{if(!e.persisted)return;resize();renderer.render(scene,camera);if(resume&&!reduced.matches&&visible)frame();resume=false;};
    window.addEventListener('pagehide',onHide);window.addEventListener('pageshow',onShow);
    update();fallback.hidden=true;host.hidden=false;
  }
  const start=()=>{if(!('IntersectionObserver' in window)){cards.forEach(mount);return;}const io=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){io.unobserve(e.target);mount(e.target);}}),{rootMargin:'2400px'});cards.forEach(c=>io.observe(c));};
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start,{once:true});else start();
})();
