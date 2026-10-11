/* ITL shared script: data + behaviour. Every render is guarded, so each page only uses what it contains. */
const directors=[['Ganesh Pawar','Director, marketing and techno-commercial','12+ years in design, manufacturing and prove-out of fixtures','+91-9579121883'],['Shivraj Alme','Director, accounts and purchase','8+ years in design, manufacturing and prove-out of fixtures','+91-8605445964'],['Ganesh Misal','Director, manufacturing','7+ years in design, manufacturing and prove-out of fixtures','+91-9096439473']];
const products=[['Hydraulic cylinders','products-cylinder.jpg'],['Hydraulic double acting pusher','products-double.jpg'],['Hydraulic single acting pusher','products-single.jpg'],['Rotary joint, 4 to 16 ports','products-rotary.jpg'],['Tail support assembly','products-tail.jpg'],['Hydraulic / manual VMC fixtures','products-vmc.jpg'],['Hydraulic / manual HMC fixtures','products-hmc.jpg'],['Cradle arrangement','products-cradle.jpg'],['Leak testing machine fixture','products-leak.jpg']];
const machines=['VMC (BFW BMV50)','Lathe','Milling','Surface grinding','DRO','Smart tap','Laser marking'];
const team=['Lathe operator','DRO operator','Milling operator','Surface grinding operator','VMC operator','Assembly'];
const fixtures=[['Cylinder cover head fixture','3 Axis','f3-cylinder-cover.jpg'],['Acute bracket fixture','3 Axis','f3-bracket.jpg'],['Housing OP-10 fixture','3 Axis','f3-housing10.jpg'],['Housing OP-20 fixture','3 Axis','f3-housing20.jpg'],['Clutch cover OP10 to OP50 fixtures','3 Axis','f3-clutch.jpg'],['Cover generator fixture','3 Axis','f3-generator.jpg'],['Tesla component (Commscope) fixture','4th Axis','f4-tesla.jpg'],['Handle bar fixture','4th Axis','f4-handlebar.jpg'],['Brake panel fixture','4th Axis','f4-brake-panel.jpg'],['Brake lever and holder bracket fixture','4th Axis','f4-brake-lever.jpg'],['Differential housing fixture','5th Axis','f5-differential.jpg'],['Knuckle joint fixture for HMC','5th Axis','f5-knuckle.jpg'],['8-port, 600 mm rotary joint (pallet changer VMC)','5th Axis','f5-rotary.jpg'],['Cover fixture for VMC','Other','o-cover-vmc.jpg'],['Cylinder block fixture','Other','o-cylinder-block.jpg'],['Water pump cover fixture','Other','o-water-pump.jpg'],['Manual fixture for HMC','Other','o-manual-hmc.jpg'],['Chain clamping fixture with cradle','Other','o-chain.jpg'],['Leak testing fixture','Other','o-leak.jpg'],['HMC tower fixture, 1000 kg, 1500 mm high','Other','o-hmc-tower.jpg'],['Relation gauges','Gauges','g-relation.jpg']];
const customers=['Tata Motors','Samvardhana Motherson','Endurance','Pitti Engineering','Continental Engines','Alicon','Taural India','Pavna Group of Industries'];

const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const put=(s,h)=>{const e=$(s);if(e)e.innerHTML=h;return e};
const img=(f,a)=>`<img src="images/${f}" alt="${a}" loading="lazy" class="ph w-full aspect-[4/3] object-cover">`;

put('#directors',directors.map(d=>`<div class="border-l-4 border-brass bg-steel p-5"><h3 class="text-2xl font-bold">${d[0]}</h3><p class="font-medium">${d[1]}</p><p class="text-sm text-slate2 mt-1">${d[2]}</p></div>`).join(''));
const pg=$('#productGrid');if(pg){const n=+(pg.dataset.limit||products.length);pg.innerHTML=products.slice(0,n).map(p=>`<article class="border border-steel bg-white">${img(p[1],p[0])}<h3 class="p-4 text-2xl font-semibold">${p[0]}</h3></article>`).join('')}
put('#machineList',machines.map(m=>`<li class="border-b border-steel py-2">${m}</li>`).join(''));
put('#teamGrid',team.map(t=>`<div class="bg-steel text-center px-2 py-4 font-head text-lg leading-tight">${t}</div>`).join(''));
put('#customerGrid',customers.map(c=>`<div class="bg-white border border-steel h-28 grid place-items-center font-head text-xl text-center px-2">${c}</div>`).join(''));
put('#contactList',directors.map(d=>`<li><a href="tel:${d[3].replace(/-/g,'')}" class="font-semibold hover:text-brass">${d[0]}</a><span class="text-slate2"> (${d[1].split(', ')[1]}) ${d[3]}</span></li>`).join(''));
const yr=$('#yr');if(yr)yr.textContent=new Date().getFullYear();

/* mobile menu */
const mb=$('#menuBtn');if(mb)mb.onclick=()=>{const m=$('#mobileNav');m.classList.toggle('hidden');mb.setAttribute('aria-expanded',!m.classList.contains('hidden'))};

/* hero slider (home only) */
const slides=$$('.slide');if(slides.length){let cur=0,t;put('#dots',slides.map((_,i)=>`<button class="w-3 h-3 rounded-full bg-white/40" aria-label="Slide ${i+1}"></button>`).join(''));const dots=$$('#dots button');
const show=i=>{cur=(i+slides.length)%slides.length;slides.forEach((s,k)=>s.classList.toggle('on',k===cur));dots.forEach((d,k)=>d.style.background=k===cur?'#d9892b':'rgba(255,255,255,.4)')};
const go=()=>{clearInterval(t);if(!matchMedia('(prefers-reduced-motion:reduce)').matches)t=setInterval(()=>show(cur+1),6000)};
dots.forEach((d,i)=>d.onclick=()=>{show(i);go()});show(0);go()}

/* counters */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;io.unobserve(e.target);const el=e.target,end=+el.dataset.count,suf=el.dataset.suffix||'',t0=performance.now();(function k(t){const p=Math.min((t-t0)/1200,1);el.textContent=Math.round(end*p)+(p===1?suf:'');if(p<1)requestAnimationFrame(k)})(t0)}),{threshold:.6});
$$('[data-count]').forEach(el=>io.observe(el));

/* vision / mission tabs */
$$('.vm-tab').forEach(b=>b.onclick=()=>{$$('.vm-tab').forEach(x=>x.classList.toggle('tab-on',x===b));$$('.vm-panel').forEach(p=>p.classList.toggle('hidden',p.id!==b.dataset.t))});

/* gallery filter + lightbox (fixtures page) */
if($('#gallery')){const cats=['All',...new Set(fixtures.map(f=>f[1]))];
put('#filters',cats.map((c,i)=>`<button data-c="${c}" class="f-btn px-4 py-2 border border-ink font-head text-lg ${i?'':'tab-on'}">${c}</button>`).join(''));
const draw=c=>put('#gallery',fixtures.filter(f=>c==='All'||f[1]===c).map(f=>`<figure class="bg-white cursor-zoom-in" data-src="images/${f[2]}" data-cap="${f[0]}">${img(f[2],f[0])}<figcaption class="p-4 font-head text-xl">${f[0]}</figcaption></figure>`).join(''));draw('All');
$('#filters').onclick=e=>{const b=e.target.closest('.f-btn');if(!b)return;$$('.f-btn').forEach(x=>x.classList.toggle('tab-on',x===b));draw(b.dataset.c)};
const lb=$('#lightbox'),close=()=>lb.classList.replace('flex','hidden');
$('#gallery').onclick=e=>{const f=e.target.closest('figure');if(!f)return;$('#lbImg').src=f.dataset.src;$('#lbCap').textContent=f.dataset.cap;lb.classList.replace('hidden','flex')};
$('#lbClose').onclick=close;lb.onclick=e=>{if(e.target===lb)close()};addEventListener('keydown',e=>{if(e.key==='Escape')close()})}

/* enquiry form (contact page) */
const form=$('#enquiry');if(form)form.onsubmit=async e=>{e.preventDefault();const m=$('#formMsg');try{const r=await fetch(form.action,{method:'POST',body:new FormData(form),headers:{Accept:'application/json'}});if(!r.ok)throw 0;form.reset();m.textContent='Thank you. We have received your enquiry and will call you back.'}catch{m.textContent='Could not send. Please call +91-9579121883 or try again.'}};
