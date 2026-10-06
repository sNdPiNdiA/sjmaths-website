/* Small, user-controlled 3D visualisations for Class 11 Thermodynamics. */
(() => {
  'use strict';
  if (!window.THREE) return;
  const cards=[...document.querySelectorAll('[data-thermo]')];
  const renderers=[];
  const material=(color)=>new THREE.MeshStandardMaterial({color,roughness:.62});
  const mat={hot:material(0xb45309),warm:material(0xf59e0b),cool:material(0x0891b2),green:material(0x059669),dark:material(0x334155),light:material(0xfde68a)};
  function mount(card){
    const host=card.querySelector('.thermal-sim-canvas'),fallback=card.querySelector('.thermal-sim-fallback');
    let renderer;try{renderer=new THREE.WebGLRenderer({antialias:true,alpha:false,powerPreference:'low-power'});}catch{return;}
    const scene=new THREE.Scene();scene.background=new THREE.Color(0xf8fafc);scene.add(new THREE.HemisphereLight(0xffffff,0xcbd5e1,1.3));
    const light=new THREE.DirectionalLight(0xffffff,1.4);light.position.set(4,6,7);scene.add(light);
    const camera=new THREE.PerspectiveCamera(38,1,.1,100);camera.position.set(0,2.7,7.5);camera.lookAt(0,.2,0);
    renderer.setPixelRatio(Math.min(devicePixelRatio||1,1.5));renderer.domElement.setAttribute('aria-hidden','true');renderer.domElement.tabIndex=-1;host.append(renderer.domElement);host.hidden=false;fallback.hidden=true;
    const geometries=[],lineMaterials=[];
    const mesh=(g,m,x=0,y=0,z=0)=>{geometries.push(g);const o=new THREE.Mesh(g,m);o.position.set(x,y,z);scene.add(o);return o;};
    const line=(points,color=0x64748b)=>{const geometry=new THREE.BufferGeometry().setFromPoints(points.map(p=>new THREE.Vector3(...p)));const lineMat=new THREE.LineBasicMaterial({color});geometries.push(geometry);lineMaterials.push(lineMat);scene.add(new THREE.Line(geometry,lineMat));};
    const draw=()=>{const w=host.clientWidth||360,h=host.clientHeight||220;renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix();renderer.render(scene,camera);};
    line([[-2,-1,0],[2,-1,0]]);line([[-2,-1,0],[-2,1.8,0]]);
    const kind=card.dataset.thermo;
    const dynamic=[],flow=[],rotors=[];
    if(kind==='pv'){
      line([[-1.7,.9,0],[-1.2,.68,0],[-.7,.49,0],[-.2,.33,0],[.3,.18,0],[.8,.05,0],[1.4,-.07,0]],0xb45309);
      line([[-1.7,.9,.05],[-1.3,.46,.05],[-.9,.15,.05],[-.5,-.07,.05]],0x047857);
      dynamic.push(mesh(new THREE.SphereGeometry(.11,16,12),mat.hot,-.65,.51,.1));
      const s=card.querySelector('input[type=range]'),out=card.querySelector('[data-readout]');
      s.addEventListener('input',()=>{const ratio=Number(s.value)/10;out.textContent=`V₂/V₁ = ${ratio.toFixed(1)}`;const x=-1.7+Math.min(2.95,(ratio-1.2)*2.2);dynamic[0].position.set(x,.9/(ratio),.1);draw();});
    }else if(kind==='carnot'){
      mesh(new THREE.BoxGeometry(1.1,.62,.8),mat.hot,-1.5,1,0);mesh(new THREE.BoxGeometry(1.1,.62,.8),mat.cool,1.5,-.35,0);mesh(new THREE.CylinderGeometry(.34,.34,.62,24),mat.dark,0,.2,0);
      const shaft=mesh(new THREE.CylinderGeometry(.055,.055,1.1,12),mat.green,.85,.5,0);shaft.rotation.z=Math.PI/2;rotors.push(shaft);
      for(let i=0;i<4;i++)flow.push(mesh(new THREE.SphereGeometry(.09,12,8),i%2?mat.warm:mat.hot,-1.3+i*.25,.64,.48));
      const sliders=[...card.querySelectorAll('input[type=range]')],outs=card.querySelectorAll('output');
      const update=()=>{const t2=+sliders[0].value,t1=+sliders[1].value,eta=1-t2/t1;outs[0].textContent=`T₂ = ${t2} K · η = ${(eta*100).toFixed(0)}%`;outs[1].textContent=`T₁ = ${t1} K`;mat.hot.color.setHex(t1>700?0x9f1239:0xb45309);mat.cool.color.setHex(t2>350?0x0e7490:0x0891b2);draw();};sliders.forEach(s=>s.addEventListener('input',update));update();
    }else if(kind==='equilibrium'){
      mesh(new THREE.BoxGeometry(1.5,1.15,1),mat.light,0,.1,0);mesh(new THREE.BoxGeometry(.42,.42,.5),mat.hot,-1.3,.15,0);mesh(new THREE.BoxGeometry(.42,.42,.5),mat.green,1.3,.15,0);
      const bar=mesh(new THREE.BoxGeometry(.2,.22,.6),mat.warm,0,-.72,.05);dynamic.push(bar);
      for(let i=0;i<4;i++)flow.push(mesh(new THREE.SphereGeometry(.075,12,8),i<2?mat.hot:mat.green,-1.04+i*.17,.16,.42));
      const slider=card.querySelector('input[type=range]'),out=card.querySelector('[data-readout]');slider.addEventListener('input',()=>{const w=+slider.value,q=600;bar.scale.x=Math.max(.08,(q-w)/300);out.textContent=`Q=${q} J, W=${w} J, ΔU=${q-w} J`;draw();});
    }
    const resizeObserver=new ResizeObserver(draw);resizeObserver.observe(host);draw();
    renderer.userData={geometries,lineMaterials};
    let raf=0,phase=0,playing=false;
    const play=card.querySelector('[data-thermo-play]'),reduced=matchMedia('(prefers-reduced-motion: reduce)');
    const stop=()=>{playing=false;if(raf)cancelAnimationFrame(raf);raf=0;if(play){play.setAttribute('aria-pressed','false');play.textContent='Play model';}};
    const frame=()=>{
      if(!playing||document.hidden)return;
      phase=(phase+.012)%1;
      if(kind==='pv'){const p=dynamic[0],slider=card.querySelector('input[type=range]'),span=(+slider.value/10)-1.2;p.position.x=-1.7+span*phase;p.position.y=.9/(1+phase*span);}
      if(kind==='carnot'){flow.forEach((p,i)=>{const t=(phase+i/flow.length)%1;p.position.set(-1.25+2.5*t,.6-.58*t,.48);});rotors[0].rotation.x=phase*Math.PI*2;}
      if(kind==='equilibrium'){flow.forEach((p,i)=>{const t=(phase+i/flow.length)%1;p.position.set(t<.5?-1.04+2.08*t:1.04-2.08*(t-.5),.16,.42);});dynamic[0].scale.x=.2+.75*(.5+.5*Math.sin(phase*Math.PI*2));}
      draw();raf=requestAnimationFrame(frame);
    };
    const start=()=>{if(reduced.matches||document.hidden||playing)return;playing=true;play.setAttribute('aria-pressed','true');play.textContent='Pause model';raf=requestAnimationFrame(frame);};
    play.disabled=reduced.matches;play.title=reduced.matches?'Animation disabled by reduced-motion preference':'Animate this model';
    play.addEventListener('click',()=>playing?stop():start());
    reduced.addEventListener('change',()=>{play.disabled=reduced.matches;play.title=reduced.matches?'Animation disabled by reduced-motion preference':'Animate this model';if(reduced.matches)stop();});
    const visibilityObserver=new IntersectionObserver(entries=>{if(!entries[0].isIntersecting)stop();},{threshold:.01});visibilityObserver.observe(card);
    document.addEventListener('visibilitychange',()=>{if(document.hidden)stop();});
    renderers.push({renderer,resizeObserver,visibilityObserver,stop});
  }
  let index=0;
  const observer=new IntersectionObserver(entries=>{for(const e of entries){if(e.isIntersecting){observer.unobserve(e.target);mount(e.target);}}},{rootMargin:'180px'});
  cards.forEach(c=>observer.observe(c));
  window.addEventListener('pagehide',()=>{observer.disconnect();renderers.forEach(({renderer,resizeObserver,visibilityObserver,stop})=>{stop();resizeObserver.disconnect();visibilityObserver.disconnect();renderer.userData.geometries.forEach(g=>g.dispose());renderer.userData.lineMaterials.forEach(m=>m.dispose());renderer.dispose();renderer.domElement.remove();});Object.values(mat).forEach(m=>m.dispose());},{once:true});
})();
