import os
OUT=os.path.dirname(os.path.abspath(__file__))
NAV=[('about','About'),('products','Products'),('facilities','Facilities'),('fixtures','Our Fixtures'),('quality','Quality'),('customers','Customers'),('careers','Careers')]

def head(title,desc):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#1a2342">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com/3.4.17"></script><script src="assets/tw-config.js"></script>
<link rel="stylesheet" href="assets/site.css"></head>
<body class="bg-white text-ink antialiased">
'''

def header(active):
    links=''.join(f'<a href="{k}.html" class="hover:text-brass {"text-brass border-b-2 border-brass" if k==active else ""}" {"aria-current=page" if k==active else ""}>{n}</a>' for k,n in NAV)
    mlinks=''.join(f'<a href="{k}.html">{n}</a>' for k,n in NAV)+'<a href="contact.html">Contact</a>'
    return f'''<!-- TOP BAR -->
<div class="bg-ink text-white text-sm"><div class="max-w-6xl mx-auto px-4 py-2 flex flex-wrap gap-x-6 gap-y-1 justify-between">
<span>Call +91 95791 21883 · +91 86054 45964 · +91 90964 39473 <span class="gst-label">GSTIN:</span></span><span class="hidden md:inline">Plot E24/31, Chikalthana MIDC, Chh. Sambhajinagar 431006</span></div></div>
<!-- HEADER + NAV -->
<header class="sticky top-0 z-40 bg-white/95 backdrop-blur border-b border-steel"><div class="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
<a href="index.html" class="flex items-center gap-3" aria-label="ITL home"><img src="assets/logo.svg" alt="" class="w-11 h-11">
<span class="hidden sm:block font-head text-lg leading-none">Instinctive Technologies<br><span class="text-slate2">Private Limited</span></span></a>
<nav class="hidden md:flex gap-6 text-sm font-medium py-1">{links}</nav>
<div class="flex items-center gap-3"><a href="contact.html" class="hidden sm:inline-block bg-brass text-ink font-semibold px-4 py-2 text-sm hover:bg-ink hover:text-white transition">Request a quote</a>
<button id="menuBtn" class="md:hidden p-2" aria-label="Open menu" aria-expanded="false"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button></div></div>
<div id="mobileNav" class="hidden md:hidden border-t border-steel bg-white px-4 py-3 flex flex-col gap-3 text-sm font-medium">{mlinks}</div></header>
'''

FOOT='''<!-- FOOTER -->
<footer class="bg-ink text-white/80 text-sm"><div class="max-w-6xl mx-auto px-4 py-10 grid md:grid-cols-3 gap-8">
<div><p class="font-head text-2xl text-white">Instinctive Technologies Pvt. Ltd.</p><p class="mt-2">Workholding. Cost. Quality. Delivery.</p></div>
<div><p class="text-white font-medium mb-2">Pages</p><a class="block" href="about.html">About</a><a class="block" href="products.html">Products</a><a class="block" href="facilities.html">Facilities</a><a class="block" href="fixtures.html">Our Fixtures</a><a class="block" href="quality.html">Quality</a><a class="block" href="customers.html">Customers</a><a class="block" href="careers.html">Careers</a><a class="block" href="contact.html">Contact</a></div>
<div><p class="text-white font-medium mb-2">Visit</p><p>Plot E24/31, Chikalthana MIDC, Near Dekson Casting Ltd, Chh. Sambhajinagar, Maharashtra 431006</p></div></div>
<div class="border-t border-white/15 text-center py-4">&copy; <span id="yr"></span> Instinctive Technologies Private Limited. All rights reserved.</div></footer>
<script src="assets/site.js"></script></body></html>
'''

def banner(h,sub=''):
    return f'<section class="bg-ink text-white grid-bg"><div class="max-w-6xl mx-auto px-4 py-14"><h1 class="text-5xl md:text-6xl font-bold">{h}</h1><p class="mt-3 text-white/75 max-w-2xl">{sub}</p></div></section>\n'

def cta():
    return '<section class="bg-brass"><div class="max-w-6xl mx-auto px-4 py-10 flex flex-wrap items-center justify-between gap-4"><p class="font-head text-3xl md:text-4xl font-bold text-ink">Have a component that needs a fixture?</p><a href="contact.html" class="bg-ink text-white font-semibold px-6 py-3">Send us a drawing</a></div></section>\n'

def page(name,active,title,desc,body):
    open(f'{OUT}/{name}.html','w').write(head(title,desc)+header(active)+body+FOOT)

T=' | Instinctive Technologies Pvt. Ltd.'

# ---------- HOME ----------
def slide(on,h,p,btn,href):
    return f'<div class="slide{" on" if on else ""} absolute inset-0 px-4 flex flex-col justify-center"><h1 class="text-5xl md:text-7xl font-bold leading-none max-w-3xl">{h}</h1><p class="mt-5 max-w-xl text-lg text-white/80">{p}</p><a href="{href}" class="mt-8 self-start bg-brass text-ink font-semibold px-6 py-3">{btn}</a></div>'
home=f'''<!-- HERO SLIDER -->
<section class="home-hero relative text-white overflow-hidden" style="min-height:580px"><div class="relative max-w-6xl mx-auto px-4" style="min-height:580px">
{slide(1,"Hydraulic Fixtures for VMC, HMC, 4th and 5th Axis Machines","Precision workholding solutions designed, manufactured and proved out for demanding machining applications.","Browse delivered fixtures","fixtures.html")}
{slide(0,"Cost. Quality. Delivery.","Workholding fixtures built by experienced design engineers with expertise in manufacturing and prove-out.","See our products","products.html")}
{slide(0,"ISO 9001:2015 certified since March 2024","Certified for manufacture of hydraulic fixture elements and hydraulic fixtures.","View certificate","quality.html")}
</div><div id="dots" class="absolute bottom-5 left-0 right-0 flex justify-center gap-2"></div></section>
<!-- ABOUT TEASER -->
<section class="py-20"><div class="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-12 items-center">
<div><h2 class="text-4xl md:text-5xl font-bold">Fixture makers who stick to the basics</h2>
<p class="mt-5 leading-relaxed max-w-prose">Founded in June 2023 by three design engineers from the workholding industry, we build quality fixtures at the lowest workable cost, delivered in a short lead time.</p>
<a href="about.html" class="inline-block mt-6 font-semibold border-b-2 border-brass hover:text-brass">About the company</a></div>
<img src="https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&amp;fit=crop&amp;w=1200&amp;q=85" alt="Engineer working with industrial manufacturing equipment" class="w-full aspect-video object-cover" loading="lazy"></div></section>
<!-- MANUFACTURING SERVICES -->
<section class="bg-steel py-20"><div class="max-w-6xl mx-auto px-4">
<p class="text-brass font-semibold uppercase tracking-widest text-sm">Capabilities</p><h2 class="mt-2 text-4xl md:text-5xl font-bold">Manufacturing Services</h2>
<p class="mt-4 max-w-3xl leading-relaxed">End-to-end workholding support, from fixture design and component manufacture to assembly and prove-out.</p>
<div class="mt-10 grid sm:grid-cols-2 lg:grid-cols-4 gap-5">
<article class="bg-white p-6 border-t-4 border-brass"><h3 class="text-2xl font-bold">Fixture design</h3><p class="mt-2 text-slate2">Hydraulic and mechanical workholding designed for VMC, HMC and multi-axis machining.</p></article>
<article class="bg-white p-6 border-t-4 border-brass"><h3 class="text-2xl font-bold">Fixture elements</h3><p class="mt-2 text-slate2">Hydraulic cylinders, pushers, rotary joints and tail-support assemblies.</p></article>
<article class="bg-white p-6 border-t-4 border-brass"><h3 class="text-2xl font-bold">Machining</h3><p class="mt-2 text-slate2">In-house machining capabilities for fixture components and workholding assemblies.</p></article>
<article class="bg-white p-6 border-t-4 border-brass"><h3 class="text-2xl font-bold">Assembly &amp; prove-out</h3><p class="mt-2 text-slate2">Fixture assembly, setup and prove-out to support reliable production.</p></article>
</div></div></section>
<!-- COMPANY STATISTICS -->
<section class="bg-ink text-white py-20"><div class="max-w-6xl mx-auto px-4">
<p class="text-brass font-semibold uppercase tracking-widest text-sm">Our track record</p><h2 class="mt-2 text-4xl md:text-5xl font-bold">Experience you can build on</h2>
<div class="mt-10 grid grid-cols-2 lg:grid-cols-5 gap-4">
<div class="stat-card"><span class="stat-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span><p class="font-head text-4xl font-bold">27+</p><p class="text-white/70">Years of combined experience</p></div>
<div class="stat-card"><span class="stat-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v2"/><circle cx="9.5" cy="7" r="4"/><path d="M20 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg></span><p class="font-head text-4xl font-bold">8+</p><p class="text-white/70">Client partners listed</p></div>
<div class="stat-card"><span class="stat-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 3 3 8l9 5 9-5-9-5Z"/><path d="M3 8v8l9 5 9-5V8M12 13v8"/></svg></span><p class="font-head text-4xl font-bold">250+</p><p class="text-white/70">Fixtures delivered to date</p></div>
<div class="stat-card"><span class="stat-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M3 17 9 11l4 4 8-9"/><path d="M15 6h6v6"/></svg></span><p class="font-head text-4xl font-bold">1,000+</p><p class="text-white/70">Fixture delivery target in the next two years</p></div>
<div class="stat-card"><span class="stat-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="4"/><path d="M3 21v-2a6 6 0 0 1 12 0v2M17 8h4m-2-2v4"/></svg></span><p class="font-head text-4xl font-bold">—</p><p class="text-white/70">Total manpower</p></div>
</div></div></section>
<!-- FIXTURE CATEGORIES -->
<section class="py-20"><div class="max-w-6xl mx-auto px-4">
<p class="text-brass font-semibold uppercase tracking-widest text-sm">Workholding solutions</p><h2 class="mt-2 text-4xl md:text-5xl font-bold">Fixture Categories</h2>
<div class="mt-10 grid md:grid-cols-3 gap-6">
<article class="fixture-card"><img src="https://images.unsplash.com/photo-1567789884554-0b844b597180?auto=format&amp;fit=crop&amp;w=900&amp;q=85" alt="Industrial machining equipment for a multi-axis cradle fixture application" loading="lazy"><div class="p-6"><h3 class="text-3xl font-bold">Cradle Fixtures</h3><p class="mt-2 text-slate2">Multi-face workholding for machining complex parts with repeatable access across multiple axes.</p></div></article>
<article class="fixture-card"><img src="https://images.unsplash.com/photo-1581092795360-fd1ca04f0952?auto=format&amp;fit=crop&amp;w=900&amp;q=85" alt="Precision engineering and inspection for gauge fixtures" loading="lazy"><div class="p-6"><h3 class="text-3xl font-bold">Gauge Fixtures</h3><p class="mt-2 text-slate2">Relation gauges and inspection fixtures that help verify component dimensions consistently.</p></div></article>
<article class="fixture-card"><img src="https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?auto=format&amp;fit=crop&amp;w=900&amp;q=85" alt="Hydraulic manufacturing equipment for cylinder fixture components" loading="lazy"><div class="p-6"><h3 class="text-3xl font-bold">Cylinder Fixtures</h3><p class="mt-2 text-slate2">Hydraulic cylinder and clamping solutions to locate and secure components during machining.</p></div></article>
</div></div></section>
<!-- FEATURED PRODUCTS (first 3) -->
<section class="py-20"><div class="max-w-6xl mx-auto px-4"><div class="flex flex-wrap items-end justify-between gap-4"><h2 class="text-4xl md:text-5xl font-bold">What we make</h2><a href="products.html" class="font-semibold border-b-2 border-brass hover:text-brass">All products</a></div>
<div id="productGrid" data-limit="3" class="mt-10 grid sm:grid-cols-3 gap-6"></div></div></section>
<!-- QUALITY TEASER -->
<section class="bg-ink text-white grid-bg py-16"><div class="max-w-6xl mx-auto px-4 flex flex-wrap items-center justify-between gap-6"><p class="font-head text-3xl md:text-4xl max-w-2xl leading-tight">ISO 9001:2015 certified for hydraulic fixture elements and hydraulic fixtures.</p><a href="quality.html" class="bg-brass text-ink font-semibold px-6 py-3">See the certificate</a></div></section>
'''+cta()
page('index','', 'Instinctive Technologies Pvt. Ltd. | Hydraulic and Mechanical Workholding Fixtures','ISO 9001:2015 certified maker of hydraulic fixture elements and VMC, HMC, 4th and 5th axis fixtures in Chh. Sambhajinagar.',home)

# ---------- ABOUT ----------
about=banner('About us','Founded June 2023 by three design engineers from the workholding industry.')+'''
<section class="py-20"><div class="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-12 items-start"><div>
<h2 class="text-4xl font-bold">Our story</h2>
<p class="mt-5 leading-relaxed max-w-prose">Instinctive Technologies Private Limited was founded in June 2023 by three design engineers, each with 7 to 12+ years in design, manufacturing and prove-out of fixtures. We started with fixtures and we keep our designs simple: good quality, at the lowest workable cost, delivered in a short lead time.</p>
<p class="mt-4 leading-relaxed max-w-prose">Our approach is cost, quality, delivery, in that order of conversation with every customer.</p></div>
<div><h2 class="text-4xl font-bold mb-5">Management team</h2><div class="grid gap-4" id="directors"></div></div></div></section>
<section class="bg-ink text-white py-20 grid-bg"><div class="max-w-4xl mx-auto px-4">
<div class="flex gap-2 mb-8" role="tablist"><button class="vm-tab tab-on px-5 py-2 font-head text-xl border border-white/40" data-t="vision" role="tab">Vision</button><button class="vm-tab px-5 py-2 font-head text-xl border border-white/40" data-t="mission" role="tab">Mission</button></div>
<div id="vision" class="vm-panel"><p class="font-head text-3xl md:text-5xl leading-tight">Achieve excellence in value-based manufacturing of automobile machined components.</p></div>
<div id="mission" class="vm-panel hidden"><p class="text-white/80 mb-4">To breathe life into our vision we will:</p><ul class="space-y-3 font-head text-2xl md:text-3xl"><li>Adhere to customer delivery dates.</li><li>Improve processes continuously toward zero-defect manufacturing.</li><li>Motivate our associates to work as a team toward organisational goals.</li></ul></div></div></section>
'''+cta()
page('about','about','About us'+T,'Founded in June 2023 by three fixture design engineers. Our vision, mission and management team.',about)

# ---------- PRODUCTS ----------
page('products','products','Products'+T,'Hydraulic cylinders, pushers, rotary joints, tail supports, VMC and HMC fixtures, cradles and leak testing fixtures.',
 banner('Products','Hydraulic fixture elements and complete fixtures, manual or hydraulic.')+'<section class="py-16"><div class="max-w-6xl mx-auto px-4"><div id="productGrid" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6"></div></div></section>'+cta())

# ---------- FACILITIES ----------
page('facilities','facilities','Facilities'+T,'Creo Parametric design facility, in-house machine shop and manufacturing team.',
 banner('Facilities','Design, machining and assembly under one roof.')+'''<section class="py-20"><div class="max-w-6xl mx-auto px-4 space-y-20">
<div class="grid md:grid-cols-2 gap-10 items-center"><div><h2 class="text-4xl font-bold">Design facility</h2><p class="mt-4 leading-relaxed">Four design engineers, each with more than 12 years in hydraulic and mechanical fixtures, design and simulate every fixture in <strong>Creo Parametric</strong> before any metal is cut.</p></div>
<img src="images/design-1.jpg" alt="Creo 3D model of a fixture" class="ph w-full aspect-video object-cover" loading="lazy"></div>
<div class="grid md:grid-cols-2 gap-10 items-center"><img src="images/vmc-machine.jpg" alt="BFW BMV50 VMC machine" class="ph w-full aspect-video object-cover order-2 md:order-1" loading="lazy">
<div class="order-1 md:order-2"><h2 class="text-4xl font-bold">Machine setup</h2><ul class="mt-4 grid grid-cols-2 gap-x-6" id="machineList"></ul></div></div>
<div><h2 class="text-4xl font-bold">Manufacturing team</h2><div class="mt-8 flex flex-col items-center"><div class="bg-ink text-white px-8 py-3 font-head text-xl">Supervisor</div><div class="w-px h-6 bg-ink"></div>
<div class="w-full grid grid-cols-2 md:grid-cols-6 gap-3 border-t border-ink pt-6" id="teamGrid"></div></div></div></div></section>'''+cta())

# ---------- FIXTURES ----------
page('fixtures','fixtures','Our Fixtures'+T,'Recently delivered 3 axis, 4th axis and 5th axis fixtures, manual fixtures, leak testing fixtures and relation gauges.',
 banner('Our fixtures','Recently delivered work. Filter by machine axis and click an image to enlarge.')+'''<section class="bg-steel py-16"><div class="max-w-6xl mx-auto px-4"><div id="filters" class="flex flex-wrap gap-2"></div><div id="gallery" class="mt-8 grid sm:grid-cols-2 lg:grid-cols-3 gap-6"></div></div></section>
<div id="lightbox" class="hidden fixed inset-0 z-50 bg-black/85 items-center justify-center p-4" role="dialog" aria-label="Image preview"><button id="lbClose" class="absolute top-4 right-5 text-white text-4xl" aria-label="Close">&times;</button><figure class="max-w-4xl w-full"><img id="lbImg" alt="" class="w-full max-h-[80vh] object-contain"><figcaption id="lbCap" class="text-white text-center mt-3 font-head text-xl"></figcaption></figure></div>'''+cta())

# ---------- QUALITY ----------
page('quality','quality','Quality'+T,'ISO 9001:2015 certified manufacturer of hydraulic fixture elements and hydraulic fixtures.',
 banner('Quality','ISO 9001:2015 certified.')+'''<section class="py-20"><div class="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-12 items-center"><div>
<h2 class="text-4xl font-bold">Certificate of registration</h2>
<p class="mt-4 leading-relaxed">Scope: manufacturer of hydraulic fixture elements and hydraulic fixtures (IAF code 17). Registered 18 March 2024, valid to 17 March 2027, issued by Assurance Quality Certification LLC (EGAC accredited).</p>
<p class="mt-4 leading-relaxed">We also build relation gauges and prove out fixtures before delivery.</p></div>
<img src="images/iso-certificate.jpg" alt="ISO 9001:2015 certificate of registration" class="ph w-full max-w-sm mx-auto border border-steel shadow" loading="lazy"></div></section>'''+cta())

# ---------- CUSTOMERS ----------
page('customers','customers','Customers'+T,'Automotive and engineering companies we supply fixtures to.',
 banner('Our customers','Automotive and engineering companies that rely on our fixtures.')+'<section class="bg-steel py-16"><div class="max-w-6xl mx-auto px-4"><div id="customerGrid" class="grid grid-cols-2 md:grid-cols-4 gap-4"></div></div></section>'+cta())

# ---------- CAREERS ----------
page('careers','careers','Careers'+T,'Explore careers in fixture design, machining, assembly and manufacturing at Instinctive Technologies.',
 banner('Careers','Build precision workholding solutions with our manufacturing team.')+'''<section class="py-20"><div class="max-w-6xl mx-auto px-4 grid lg:grid-cols-2 gap-12">
<div><p class="text-brass font-semibold uppercase tracking-widest text-sm">Work with us</p><h2 class="mt-2 text-4xl font-bold">A hands-on manufacturing workplace</h2>
<p class="mt-5 leading-relaxed">Join a team working across fixture design, machining, assembly and prove-out for automotive and engineering applications. Our Chikalthana MIDC facility brings design and manufacturing capabilities together.</p>
<h3 class="mt-10 text-3xl font-bold">Current openings</h3><p class="mt-3 leading-relaxed">There are no specific openings listed at this time. Candidates with experience in fixture design, CNC/VMC operations, machining or assembly are welcome to send a general enquiry.</p>
<p class="mt-6">For a career enquiry, call <a class="font-semibold underline" href="tel:+919579121883">+91 95791 21883</a>.</p></div>
<div class="bg-steel p-6 md:p-8"><h2 class="text-3xl font-bold">Career enquiry</h2>
<p class="mt-2 text-slate2">Share your details and resume. Online submission will be available once the application service is configured; please call us for now.</p>
<form id="careerApplication" class="mt-6 space-y-4">
<label class="block text-sm font-medium">Full name<input name="name" required autocomplete="name" class="mt-1 w-full border border-slate2/40 bg-white px-3 py-2"></label>
<label class="block text-sm font-medium">Email<input name="email" type="email" required autocomplete="email" class="mt-1 w-full border border-slate2/40 bg-white px-3 py-2"></label>
<label class="block text-sm font-medium">Phone<input name="phone" type="tel" required autocomplete="tel" class="mt-1 w-full border border-slate2/40 bg-white px-3 py-2"></label>
<label class="block text-sm font-medium">Area of interest<input name="role" placeholder="e.g. VMC operator, fixture design" class="mt-1 w-full border border-slate2/40 bg-white px-3 py-2"></label>
<label class="block text-sm font-medium">Resume (PDF, DOC or DOCX)<input name="resume" type="file" accept=".pdf,.doc,.docx" class="mt-1 block w-full text-sm"></label>
<label class="block text-sm font-medium">Message<textarea name="message" rows="4" class="mt-1 w-full border border-slate2/40 bg-white px-3 py-2"></textarea></label>
<button class="bg-ink text-white px-6 py-3 font-semibold hover:bg-brass hover:text-ink transition">Send career enquiry</button>
<p id="careerFormMsg" class="text-sm" role="status"></p></form></div></div></section>''')

# ---------- CONTACT ----------
inp='class="mt-1 w-full border border-slate2/40 px-3 py-2"'
page('contact','contact','Contact'+T,'Send a drawing or enquiry to Instinctive Technologies, Chikalthana MIDC, Chh. Sambhajinagar.',
 banner('Contact us','Share your part drawing and the machine type. We reply with a fixture concept and quote.')+f'''<section class="py-20"><div class="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-12"><div>
<h2 class="text-4xl font-bold">Visit or call</h2>
<address class="not-italic mt-4 leading-relaxed">Plot no. E24/31, Chikalthana MIDC, Millennium Park Road,<br>Near Dekson Casting Ltd, Chh. Sambhajinagar (Aurangabad),<br>Maharashtra 431006</address><ul class="mt-6 space-y-3" id="contactList"></ul></div>
<!-- Replace action with your Formspree / backend URL -->
<form id="enquiry" class="space-y-4" action="https://formspree.io/f/your-id" method="POST">
<label class="block text-sm font-medium">Name<input name="name" required {inp}></label>
<label class="block text-sm font-medium">Phone or email<input name="contact" required {inp}></label>
<label class="block text-sm font-medium">Component and machine type<input name="part" placeholder="e.g. Housing, VMC" {inp}></label>
<label class="block text-sm font-medium">Message<textarea name="message" rows="4" {inp}></textarea></label>
<button class="bg-ink text-white px-6 py-3 font-semibold hover:bg-brass hover:text-ink transition">Send enquiry</button><p id="formMsg" class="text-sm" role="status"></p></form></div></section>''')
print(sorted(os.listdir(OUT)))
