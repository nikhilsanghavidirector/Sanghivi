# -*- coding: utf-8 -*-
"""Page bodies for the KP Sanghvi static site. Imported by generate.py."""

# ---------------------------------------------------------------- helpers ----
def banner(title, desc, crumbs, bg=None):
    style = ' style="background-image:linear-gradient(rgba(12,9,6,.45),rgba(12,9,6,.65)),url(\'{}\');"'.format(bg) if bg else ""
    return """    <section class="page-banner"{style}>
      <div class="container">
        <p class="breadcrumbs reveal"><a href="index.html">Home</a> &nbsp;/&nbsp; {crumbs}</p>
        <h1 class="reveal delay-1">{title}</h1>
        <p class="reveal delay-2">{desc}</p>
      </div>
    </section>
""".format(style=style, crumbs=crumbs, title=title, desc=desc)

def cta(title, text, btn_txt="Contact Us", btn_href="contact.html"):
    return """    <section class="section cta-band">
      <div class="container">
        <h2 class="section-title light reveal">{title}</h2>
        <p class="lead reveal delay-1" style="color:rgba(255,255,255,.8);max-width:640px;margin:0 auto 1.8rem">{text}</p>
        <a class="btn on-dark reveal delay-2" href="{href}">{btn} <span class="arrow">&rarr;</span></a>
      </div>
    </section>
""".format(title=title, text=text, href=btn_href, btn=btn_txt)

PLACEHOLDER_SVG = '<svg viewBox="0 0 100 125" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="50" cy="46" r="20" fill="#c2a65c"/><path d="M18 112c0-19 15-32 32-32s32 13 32 32z" fill="#c2a65c"/></svg>'

# ---------------------------------------------------------------- build ------
def build(write):

    # ================================================================= HOME
    home = """    <section class="hero" aria-label="Introduction">
      <div class="hero-slides">
        <div class="hero-slide plain active"></div>
        <div class="hero-slide" style="background-image:url('assets/images/home/hero-1.jpg')"></div>
        <div class="hero-slide" style="background-image:url('assets/images/home/hero-2.jpg')"></div>
        <div class="hero-slide" style="background-image:url('assets/images/home/hero-3.jpg')"></div>
      </div>
      <div class="hero-inner">
        <img class="hero-emblem" src="assets/images/home/emblem.png" alt="KP Sanghvi crest" width="150" height="185">
        <h1>Forged by Time.<br>Fuelled by Tomorrow.</h1>
        <p class="hero-sub">A Global Legacy Since 1965</p>
        <a class="btn on-dark" href="about.html">Discover the Group <span class="arrow">&rarr;</span></a>
      </div>
      <div class="hero-dots" role="tablist" aria-label="Hero slides"></div>
      <span class="scroll-cue" aria-hidden="true">Scroll</span>
    </section>

    <section class="section intro">
      <img class="watermark" src="assets/images/home/watermark-1965.png" alt="" aria-hidden="true">
      <div class="container">
        <p class="eyebrow reveal">About Us</p>
        <h2 class="section-title reveal delay-1">A Legacy of Trust &amp; Craftsmanship</h2>
        <hr class="divider reveal delay-1">
        <p class="lead reveal delay-2" style="margin-top:1.8rem">KP Sanghvi is a diversified, third-generation family-led global conglomerate with a footprint across multiple sectors. Founded in 1965, we began as pioneers in diamond trading and manufacturing, later expanding into fine jewellery, infrastructure, real estate, venture capital, energy systems and other strategic investments &mdash; all driven by a commitment to sustainable growth and lasting value creation.</p>
        <p class="reveal delay-3">Guided by integrity and excellence, we drive progress that uplifts communities, safeguards the environment, and creates enduring impact &mdash; shaping a responsible, sustainable future.</p>
        <a class="btn reveal delay-3" href="our-journey.html" style="margin-top:2rem">Explore Our Journey <span class="arrow">&rarr;</span></a>
      </div>
    </section>

    <section class="section cream">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Our Ethos</p>
          <h2 class="section-title center reveal delay-1">Values that Propel Us Forward</h2>
          <hr class="divider reveal delay-1">
          <p class="reveal delay-2">Values don&rsquo;t just give a foundation &mdash; they are a propeller towards success.</p>
        </div>
        <div class="grid grid-3">
          {ethos}
        </div>
      </div>
    </section>

    <section class="section" style="padding-bottom:0">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Our Businesses</p>
          <h2 class="section-title center reveal delay-1">Four Pillars, One Vision</h2>
          <hr class="divider reveal delay-1">
        </div>
      </div>
      <div class="showcase">
        {showcase}
      </div>
    </section>

    <section class="section dark">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Our Impact</p>
          <h2 class="section-title light center reveal delay-1">Six Decades of Meaningful Progress</h2>
          <hr class="divider reveal delay-1">
        </div>
        <div class="stats reveal-scale">
          <div class="stat"><div class="num" data-count="60" data-suffix="+">60+</div><div class="lbl">Years of Heritage</div></div>
          <div class="stat"><div class="num" data-count="8" data-prefix="" data-suffix=" Countries">8 Countries</div><div class="lbl">Global Presence</div></div>
          <div class="stat"><div class="num" data-count="7000" data-suffix="+">7000+</div><div class="lbl">Strong Workforce</div></div>
          <div class="stat"><div class="num" data-count="4">4</div><div class="lbl">Business Verticals</div></div>
        </div>
      </div>
    </section>
""".format(ethos=_ethos_cards(), showcase=_showcase_rows())

    home += cta("Partner with a Legacy of Excellence",
                "From ethically sourced diamonds to intelligent energy systems, discover how the KP Sanghvi Group creates enduring value.",
                "Get in Touch")
    write("index.html", "KP Sanghvi Group | Forged by Time. Fuelled by Tomorrow.",
          "KP Sanghvi is a third-generation, family-led global conglomerate founded in 1965 — spanning diamonds, fine jewellery, infrastructure and energy systems across the world.",
          home)

    # ================================================================ ABOUT
    about = banner("The KP Sanghvi Group",
                   "Sixty years of trust, innovation and excellence — built across three generations.",
                   "About Us", "assets/images/home/hero-2.jpg")
    about += """    <section class="section intro">
      <img class="watermark" src="assets/images/home/watermark-1965.png" alt="" aria-hidden="true">
      <div class="container">
        <p class="eyebrow reveal">Our Origin Story</p>
        <h2 class="section-title reveal delay-1">From a Single Idea to a Global Enterprise</h2>
        <hr class="divider reveal delay-1">
        <p class="lead reveal delay-2" style="margin-top:1.8rem">Founded in 1965 by the visionary Late Shri Hajirimalji Sanghvi and Late Shri Babulaji Sanghvi, KP Sanghvi began as a modest non-ferrous metals trading enterprise in India.</p>
        <p class="reveal delay-2">Over the decades the company evolved into a manufacturer of natural and traceable diamonds for retailers, jewellery houses and watch manufacturers globally. Operating as a third-generation family business, KP Sanghvi now spans fine jewellery, infrastructure, real estate, venture capital and energy systems.</p>
      </div>
    </section>

    <section class="section cream">
      <div class="container split">
        <div class="body reveal-left">
          <p class="eyebrow">Our Mission</p>
          <h2 class="section-title" style="font-size:clamp(1.8rem,3.2vw,2.6rem)">Innovate, Enable &amp; Impact</h2>
          <hr class="divider left">
          <p style="margin-top:1.4rem">Our mission is to create lasting value grounded in integrity, excellence and trust &mdash; through purposeful innovation, collaborative growth and sustainable practices that benefit every stakeholder we serve.</p>
          <p class="eyebrow" style="margin-top:2.4rem">Our Vision</p>
          <h2 class="section-title" style="font-size:clamp(1.8rem,3.2vw,2.6rem)">Inspire, Empower &amp; Lead</h2>
          <hr class="divider left">
          <p style="margin-top:1.4rem">We aspire to drive excellence through innovation, empower our stakeholders to achieve their full potential, and uphold integrity as a global force generating enduring value across generations.</p>
        </div>
        <div class="media framed reveal-right">
          <img src="assets/images/diamonds/diamond.jpg" alt="Precision-crafted diamonds by KP Sanghvi" loading="lazy">
        </div>
      </div>
    </section>

    <section class="section dark">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Global Presence</p>
          <h2 class="section-title light center reveal delay-1">Local Expertise, Global Perspective</h2>
          <hr class="divider reveal delay-1">
          <p class="reveal delay-2">Headquartered in India, with operations spanning six countries &mdash; fostering collaboration between deep local expertise and a truly global outlook.</p>
        </div>
        <div class="grid grid-4 reveal">
          {presence}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Our Ethos</p>
          <h2 class="section-title center reveal delay-1">The Principles We Live By</h2>
          <hr class="divider reveal delay-1">
        </div>
        <div class="grid grid-3">{ethos}</div>
      </div>
    </section>
""".format(presence=_presence(), ethos=_ethos_cards())
    about += cta("Explore Six Decades of Our Journey",
                 "Every milestone reflects our pursuit of excellence and enduring commitment to creating value.",
                 "View Our Journey", "our-journey.html")
    write("about.html", "About Us | KP Sanghvi Group — 60 Years of Trust & Excellence",
          "Founded in 1965, KP Sanghvi is a third-generation family business spanning diamonds, jewellery, infrastructure and energy — guided by a mission to innovate, enable and impact.",
          about)

    # ============================================================== JOURNEY
    journey = banner("Our Journey Since 1965",
                     "From humble beginnings to a global enterprise — evolving with vision, purpose and integrity.",
                     "About Us &nbsp;/&nbsp; Our Journey", "assets/images/home/hero-3.jpg")
    journey += """    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Milestones</p>
          <h2 class="section-title center reveal delay-1">A Legacy That Transcends Generations</h2>
          <hr class="divider reveal delay-1">
          <p class="reveal delay-2">Each milestone reflects our pursuit of excellence and enduring commitment to creating value, fostering trust and shaping a legacy that lasts.</p>
        </div>
        <div class="timeline">
          {tl}
        </div>
      </div>
    </section>
""".format(tl=_timeline())
    journey += cta("Be Part of the Next Chapter", "Sixty years on, our story is still being written. Discover how you can grow with us.", "Contact Us")
    write("our-journey.html", "Our Journey | KP Sanghvi Group — Milestones Since 1965",
          "The KP Sanghvi journey since 1965 — from diamond trading to a global conglomerate spanning jewellery, infrastructure and energy, told through six decades of milestones.",
          journey)

    # ============================================================= DIAMONDS
    diamonds = banner("Diamond",
                      "Founded in 1965. Shaped by Generations. Defined by Excellence.",
                      "Businesses &nbsp;/&nbsp; Diamond", "assets/images/diamonds/diamond.jpg")
    diamonds += _business_intro(
        "Est. 1965",
        "From Origin to Execution",
        ["KP Sanghvi is a trusted supplier of the world&rsquo;s finest natural diamonds, serving leading maisons, watchmakers, jewellery manufacturers and luxury retailers worldwide. For over 60 years and across three generations, quality and customer service have remained at the heart of everything we do.",
         "Every diamond we supply is fully traceable and ethically sourced, backed by a rigorously audited global supply chain &mdash; a commitment that extends to our employees and the communities in which we operate."],
        "assets/images/diamonds/diamond.jpg", reverse=False)
    diamonds += """    <section class="section cream">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Capabilities</p>
          <h2 class="section-title center reveal delay-1">Precision at Every Facet</h2>
          <hr class="divider reveal delay-1">
        </div>
        <div class="grid grid-3">
          {cards}
        </div>
      </div>
    </section>

    <section class="section dark">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Partnerships</p>
          <h2 class="section-title light center reveal delay-1">Trusted at the Source</h2>
          <hr class="divider reveal delay-1">
          <p class="reveal delay-2">As a De Beers Sightholder and a Rio Tinto Select Diamantaire, we hold direct access to the world&rsquo;s major mining sources &mdash; enabling us to source diamonds precisely to our clients&rsquo; requirements.</p>
        </div>
      </div>
    </section>
""".format(cards=_cards([
        ("Calibrated Diamonds", "Round brilliant expertise, delivered in a full range of calibrated cuts and sizes."),
        ("Microscopic Assortments", "Meticulous grading and assortment for exacting client specifications."),
        ("Jewellery Layouts", "Layouts, bagging and fluting prepared for seamless manufacturing."),
        ("Ethical Sourcing", "Fully traceable diamonds from a rigorously audited global supply chain."),
        ("Custom Curation", "Exceptional diamonds curated for bespoke and special orders."),
        ("Global Delivery", "A worldwide office network ensuring reliable, responsive service."),
    ]))
    diamonds += cta("Source Extraordinary Diamonds", "Speak with our team about calibrated, traceable and bespoke natural diamonds.", "Enquire Now")
    write("diamonds.html", "Diamonds | KP Sanghvi Group — Natural, Traceable, Ethically Sourced",
          "KP Sanghvi is a trusted supplier of the world's finest natural diamonds — a De Beers Sightholder and Rio Tinto Select Diamantaire delivering calibrated, fully traceable stones worldwide.",
          diamonds)

    # ============================================================ JEWELLERY
    jewel = banner("Jewellery",
                   "Designed to Spec. Built to Impress.",
                   "Businesses &nbsp;/&nbsp; Jewellery", "assets/images/jewellery/jewellery.jpg")
    jewel += _business_intro(
        "Launched 2000",
        "Craftsmanship Without Compromise",
        ["The jewellery vertical builds on over 60 years of expertise to craft fine and high-end jewellery rooted in ethics and craftsmanship. Every piece begins with a vision &mdash; yours. Our artisans merge creativity with precision, transforming your briefs into finished jewellery through continuous design innovation.",
         "With advanced manufacturing in Mumbai and Surat and a global presence, we serve big-box retailers, independent stores and brands across domestic and international markets."],
        "assets/images/jewellery/jewellery.jpg", reverse=True)
    jewel += """    <section class="section cream">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">What Sets Us Apart</p>
          <h2 class="section-title center reveal delay-1">From Concept to Creation</h2>
          <hr class="divider reveal delay-1">
        </div>
        <div class="grid grid-4">
          {cards}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Our Divisions</p>
          <h2 class="section-title center reveal delay-1">Three Ways We Deliver</h2>
          <hr class="divider reveal delay-1">
        </div>
        <div class="grid grid-3">
          {divs}
        </div>
      </div>
    </section>
""".format(cards=_cards([
        ("Design &amp; Production", "Continuous design innovation turns your brief into finished, wearable art."),
        ("Innovation", "In-house R&amp;D and the latest technology &mdash; from CNC machining to Rolling Tube."),
        ("Quality Assurance", "Quality is built into every stage, with multiple checks from first step to last."),
        ("Sustainability", "LEED Platinum facilities, renewable energy and a circular ecosystem."),
    ]), divs=_cards([
        ("Global Export &amp; Distribution", "Since 2007 &mdash; our SEEPZ facility serves the USA, Europe, the Middle East, Asia-Pacific and Australia with collections from bridal to fashion-forward."),
        ("Domestic Manufacturing", "Established 2000 &mdash; multi-factory operations across India serving national chains, regional players and independent jewellers."),
        ("Studio65 by KP Sanghvi", "A high-jewellery atelier for discerning clientele in India and the Middle East &mdash; bespoke, heritage-driven pieces."),
    ]))
    jewel += cta("Create Something Extraordinary", "Partner with our artisans to bring your jewellery vision to life.", "Start a Project")
    write("jewellery.html", "Jewellery | KP Sanghvi Group — Fine & High Jewellery Craftsmanship",
          "KP Sanghvi's jewellery vertical crafts fine and high-end jewellery rooted in ethics and craftsmanship — with advanced manufacturing in Mumbai and Surat and a global presence.",
          jewel)

    # ========================================================= INFRASTRUCTURE
    infra = banner("Infrastructure",
                   "Building Landmarks for Modern Living.",
                   "Businesses &nbsp;/&nbsp; Infrastructure", "assets/images/infrastructure/infra.jpg")
    infra += _business_intro(
        "Established 2007",
        "KP Infra &mdash; Shaping Skylines",
        ["KP Infra is focused on developing high-quality infrastructure across key cities in Gujarat such as Ahmedabad, Surat and Vadodara. Our residential portfolio includes well-planned high-rise towers and premium villas designed for modern living.",
         "On the commercial side, we develop office spaces and buildings &mdash; some of which are leased to corporates and multinational companies &mdash; delivering enduring value through thoughtful design and quality construction."],
        "assets/images/infrastructure/infra.jpg", reverse=False,
        extra_btn=("Visit KP Infra", "https://kpinfra.com/"))
    infra += """    <section class="section cream">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Our Focus</p>
          <h2 class="section-title center reveal delay-1">Residential &amp; Commercial Excellence</h2>
          <hr class="divider reveal delay-1">
        </div>
        <div class="grid grid-3">
          {cards}
        </div>
      </div>
    </section>
""".format(cards=_cards([
        ("High-Rise Towers", "Well-planned residential high-rises designed for contemporary urban living."),
        ("Premium Villas", "Thoughtfully crafted villas that balance privacy, comfort and elegance."),
        ("Commercial Spaces", "Grade-A office spaces and buildings leased to corporates and multinationals."),
        ("Key Cities", "A growing footprint across Ahmedabad, Surat and Vadodara in Gujarat."),
        ("Quality Construction", "Enduring value delivered through robust engineering and finishes."),
        ("Modern Living", "Amenities and layouts designed around how people live and work today."),
    ]))
    infra += cta("Discover Our Developments", "Explore KP Infra's residential and commercial projects.", "Visit KP Infra", "https://kpinfra.com/")
    write("infrastructure.html", "Infrastructure | KP Sanghvi Group — KP Infra Real Estate",
          "KP Infra develops high-quality residential and commercial infrastructure across Ahmedabad, Surat and Vadodara — high-rise towers, premium villas and Grade-A office spaces.",
          infra)

    # ================================================================ ENERGY
    energy = banner("Energy Systems",
                    "Powering the Future, Intelligently.",
                    "Businesses &nbsp;/&nbsp; Energy Systems", "assets/images/energy/energy.jpg")
    energy += _business_intro(
        "Established 2025",
        "Emfex Energy &mdash; Intelligent by Design",
        ["Emfex Energy marks our evolution &mdash; channelling 60 years of excellence into intelligent energy systems that power the future. It is an energy-systems company focused on the design and manufacturing of intelligent Battery Energy Storage Systems (BESS) and advanced EV charging solutions.",
         "By combining deep engineering discipline with a future-first outlook, Emfex is building the clean, connected infrastructure that tomorrow&rsquo;s mobility and grids demand."],
        "assets/images/energy/energy.jpg", reverse=True,
        extra_btn=("Visit Emfex Energy", "https://emfexenergy.com/"))
    energy += """    <section class="section cream">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Capabilities</p>
          <h2 class="section-title center reveal delay-1">Storage &amp; Charging, Reimagined</h2>
          <hr class="divider reveal delay-1">
        </div>
        <div class="grid grid-3">
          {cards}
        </div>
      </div>
    </section>
""".format(cards=_cards([
        ("Battery Energy Storage", "Intelligent BESS engineered for reliability, safety and scale."),
        ("EV Charging Solutions", "Advanced charging technology for a connected, electric future."),
        ("Smart Engineering", "Design and manufacturing driven by precision and innovation."),
        ("Sustainable Power", "Clean-energy systems that reduce carbon and increase resilience."),
        ("Future-First Outlook", "Built to meet the demands of tomorrow&rsquo;s mobility and grids."),
        ("Six Decades of Rigour", "The KP Sanghvi discipline, applied to intelligent energy."),
    ]))
    energy += cta("Energise What&rsquo;s Next", "Learn how Emfex Energy is building intelligent storage and charging systems.", "Visit Emfex Energy", "https://emfexenergy.com/")
    write("energy.html", "Energy Systems | KP Sanghvi Group — Emfex Energy (BESS & EV)",
          "Emfex Energy designs and manufactures intelligent Battery Energy Storage Systems (BESS) and advanced EV charging solutions — channelling 60 years of KP Sanghvi excellence into clean power.",
          energy)

    # ============================================================= DIRECTORS
    write("directors.html", "Directors | KP Sanghvi Group — Leadership",
          "Meet the leadership guiding the KP Sanghvi Group — the directors stewarding six decades of heritage across diamonds, jewellery, infrastructure and energy.",
          _directors())

    # ======================================================== SUSTAINABILITY
    sust = banner("Sustainability",
                  "People, Planet &amp; Responsible Practices.",
                  "Sustainability", "assets/images/home/hero-1.jpg")
    sust += """    <section class="section intro">
      <div class="container">
        <p class="eyebrow reveal">A Way of Doing Business</p>
        <h2 class="section-title reveal delay-1">&ldquo;Responsibility is not an initiative &mdash; it is a way of doing business.&rdquo;</h2>
        <hr class="divider reveal delay-1">
        <p class="lead reveal delay-2" style="margin-top:1.8rem">At KP Sanghvi, sustainability is woven into every decision we make &mdash; empowering people and communities, protecting the planet, and pioneering responsible practices across our operations.</p>
      </div>
    </section>

    <section class="section dark">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Our Impact in Numbers</p>
          <h2 class="section-title light center reveal delay-1">Measurable, Meaningful Change</h2>
          <hr class="divider reveal delay-1">
        </div>
        <div class="stats reveal-scale">
          <div class="stat"><div class="num" data-count="35" data-suffix="%">35%</div><div class="lbl">Women in the Workforce</div></div>
          <div class="stat"><div class="num" data-count="300000" data-suffix="+">300,000+</div><div class="lbl">Trees Planted</div></div>
          <div class="stat"><div class="num" data-count="250" data-suffix="M+ L">250M+ L</div><div class="lbl">Water Conserved Annually</div></div>
          <div class="stat"><div class="num" data-count="1" data-suffix="M+">1M+</div><div class="lbl">Lives Touched</div></div>
        </div>
        <div class="stats reveal-scale" style="margin-top:1px">
          <div class="stat"><div class="num" data-count="230" data-suffix="+ acres">230+ acres</div><div class="lbl">Land Restored</div></div>
          <div class="stat"><div class="num" data-count="5000" data-suffix="+">5000+</div><div class="lbl">Animals Sheltered</div></div>
          <div class="stat"><div class="num">LEED Platinum</div><div class="lbl">Certified Facilities</div></div>
          <div class="stat"><div class="num" data-count="7000" data-suffix="+">7000+</div><div class="lbl">Diverse Workforce</div></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Three Pillars</p>
          <h2 class="section-title center reveal delay-1">How We Create Lasting Value</h2>
          <hr class="divider reveal delay-1">
        </div>
        <div class="grid grid-3">
          {cards}
        </div>
      </div>
    </section>
""".format(cards=_cards([
        ("Empowering People &amp; Communities", "The KPS Group works continuously towards the development and upliftment of its members and the extended community &mdash; through education, healthcare and gender empowerment."),
        ("Protecting the Planet", "We actively implement programmes to conserve every essential natural resource, protect wildlife and advance animal welfare &mdash; from afforestation to water conservation."),
        ("Pioneering Sustainable Practices", "We have successfully embedded sustainable practices across our operations and processes, powered increasingly by green energy and LEED Platinum facilities."),
    ]))
    sust += cta("Building a Responsible Future, Together", "Learn more about our people, planet and governance commitments.", "Contact Us")
    write("sustainability.html", "Sustainability | KP Sanghvi Group — People, Planet & Practices",
          "Sustainability at KP Sanghvi: 300,000+ trees planted, 250M+ litres of water conserved, LEED Platinum facilities and 35% women in the workforce — responsibility as a way of doing business.",
          sust)

    # ============================================================ NEWS/EVENTS
    write("news-events.html", "News & Events | KP Sanghvi Group",
          "The latest milestones and announcements from the KP Sanghvi Group — from LEED Platinum certification and Studio65 to Emfex Energy and the UN Women's Empowerment Principles.",
          _news())

    # =============================================================== CONTACT
    write("contact.html", "Contact Us | KP Sanghvi Group — Reach Out",
          "Reach out to the KP Sanghvi Group. Find our offices in Mumbai, Surat, Ahmedabad, Antwerp, New York, Dubai, Hong Kong and Botswana, or send us a message.",
          _contact())

    # =============================================================== LEGAL
    write("privacy.html", "Privacy Policy | KP Sanghvi Group",
          "Privacy Policy for the KP Sanghvi Group website.",
          _legal("Privacy Policy", [
            ("Introduction", "This Privacy Policy explains how KP Sanghvi Group (&ldquo;we&rdquo;, &ldquo;us&rdquo;) handles information in connection with this website. This is a general template; please review and adapt it to your specific practices and applicable law before publishing."),
            ("Information We Collect", "We may collect information you voluntarily provide through our contact form &mdash; such as your name, email address, phone number and message &mdash; as well as standard technical information (for example, browser type) that your device sends when visiting a website."),
            ("How We Use Information", "Information you submit is used solely to respond to your enquiry and to improve our services. We do not sell your personal information."),
            ("Data Sharing", "We do not share your personal information with third parties except as necessary to respond to your enquiry or where required by law."),
            ("Your Rights", "You may request access to, correction of, or deletion of your personal information by contacting us at legal@kpsanghvi.com."),
            ("Contact", "For any privacy-related questions, please email legal@kpsanghvi.com."),
          ]))
    write("terms.html", "Terms &amp; Conditions | KP Sanghvi Group",
          "Terms and Conditions for the KP Sanghvi Group website.",
          _legal("Terms &amp; Conditions", [
            ("Acceptance of Terms", "By accessing this website you agree to these Terms &amp; Conditions. This is a general template; please review and adapt it before publishing."),
            ("Use of the Website", "This website and its content are provided for general information about the KP Sanghvi Group. You agree not to misuse the website or its content."),
            ("Intellectual Property", "All branding, logos, text and imagery on this website are the property of the KP Sanghvi Group and may not be reproduced without permission."),
            ("Disclaimer", "Content is provided &ldquo;as is&rdquo; without warranties of any kind. We are not liable for any loss arising from the use of this website."),
            ("Governing Law", "These terms are governed by the applicable laws of India, without regard to conflict-of-law principles."),
            ("Contact", "Questions about these terms may be sent to legal@kpsanghvi.com."),
          ]))
    write("cookies.html", "Cookies Policy | KP Sanghvi Group",
          "Cookies Policy for the KP Sanghvi Group website.",
          _legal("Cookies Policy", [
            ("What Are Cookies", "Cookies are small text files placed on your device by websites you visit. This is a general template; adapt it to the cookies your final deployment actually uses."),
            ("How This Site Uses Cookies", "This static website does not set tracking cookies by default. If you add analytics or embedded maps, those third-party services may set their own cookies."),
            ("Managing Cookies", "You can control and delete cookies through your browser settings at any time."),
            ("Contact", "For questions about this policy, email legal@kpsanghvi.com."),
          ]))
    write("sitemap.html", "Sitemap | KP Sanghvi Group",
          "Sitemap of the KP Sanghvi Group website.",
          _sitemap())


# ------------------------------------------------------------- fragments -----
def _ethos_cards():
    data = [
        ("integrity", "Integrity", "We build lasting partnerships founded on trust, transparency and decades of experience."),
        ("diversity", "Diversity", "We champion diversity as a source of strength, fostering inclusivity where varied perspectives drive innovation."),
        ("sustainability", "Sustainability", "We are committed to responsible and ethical practices that build a better future for our communities."),
        ("innovation", "Innovation", "We continually embrace innovation and emerging technologies with a future-first outlook."),
        ("excellence", "Excellence", "We pursue and deliver unmatched quality and everlasting value in all our ventures."),
        ("collaboration", "Collaboration", "We believe in shared success, working hand in hand with key partners to achieve our collective goals."),
    ]
    out = []
    for i, (ic, t, d) in enumerate(data):
        out.append(
            '<article class="value-card reveal delay-{dl}">'
            '<img class="ic" src="assets/icons/{ic}.png" alt="" aria-hidden="true" loading="lazy" width="78" height="78">'
            '<h3>{t}</h3><p>{d}</p></article>'.format(dl=(i % 3) + 1, ic=ic, t=t, d=d))
    return "\n          ".join(out)

def _showcase_rows():
    data = [
        ("Est. 1965", "Diamond", "A global leader in natural diamond manufacturing and ethical sourcing, delivering precision-crafted, responsibly sourced diamonds and jewellery to leading maisons worldwide.", "assets/images/diamonds/diamond.jpg", "diamonds.html"),
        ("Launched 2000", "Jewellery", "Over 60 years of expertise crafting fine and high-end jewellery rooted in ethics and craftsmanship, serving retailers and brands across domestic and international markets.", "assets/images/jewellery/jewellery.jpg", "jewellery.html"),
        ("Established 2007", "Infrastructure", "KP Infra develops high-quality residential and commercial infrastructure across key cities in Gujarat &mdash; from high-rise towers and villas to Grade-A office spaces.", "assets/images/infrastructure/infra.jpg", "infrastructure.html"),
        ("Established 2025", "Energy Systems", "Emfex Energy designs and manufactures intelligent Battery Energy Storage Systems (BESS) and advanced EV charging solutions &mdash; powering the future.", "assets/images/energy/energy.jpg", "energy.html"),
    ]
    out = []
    for est, t, d, img, href in data:
        out.append(
            """<div class="row">
          <div class="visual reveal-scale" style="background-image:url('{img}')"></div>
          <div class="panel">
            <p class="est reveal">{est}</p>
            <h3 class="reveal delay-1">{t}</h3>
            <p class="reveal delay-2">{d}</p>
            <a class="btn on-dark reveal delay-3" href="{href}">Explore {t} <span class="arrow">&rarr;</span></a>
          </div>
        </div>""".format(img=img, est=est, t=t, d=d, href=href))
    return "\n        ".join(out)

def _presence():
    for_ = ["India (HQ)", "Belgium", "United Arab Emirates", "Botswana", "USA", "Hong Kong"]
    return "\n          ".join(
        '<div class="value-card" style="padding:1.6rem 1rem"><h3 style="font-size:1.4rem;color:var(--gold)">{c}</h3></div>'.format(c=c)
        for c in for_)

def _cards(items):
    out = []
    for i, (t, d) in enumerate(items):
        out.append(
            '<article class="value-card reveal delay-{dl}"><h3>{t}</h3><p>{d}</p></article>'.format(
                dl=(i % 3) + 1, t=t, d=d))
    return "\n          ".join(out)

def _business_intro(est, title, paras, img, reverse=False, extra_btn=None):
    body = "".join('<p{cls}>{p}</p>'.format(cls=(' style="margin-top:1.1rem"' if i else ' style="margin-top:1.4rem"'), p=p)
                   for i, p in enumerate(paras))
    btn = ""
    if extra_btn:
        btn = '<a class="btn" href="{h}" target="_blank" rel="noopener" style="margin-top:2rem">{t} <span class="arrow">&rarr;</span></a>'.format(h=extra_btn[1], t=extra_btn[0])
    rev = " reverse" if reverse else ""
    ml = "reveal-right" if reverse else "reveal-left"
    mr = "reveal-left" if reverse else "reveal-right"
    return """    <section class="section">
      <div class="container split{rev}">
        <div class="body {ml}">
          <p class="eyebrow">{est}</p>
          <h2 class="section-title" style="font-size:clamp(1.9rem,3.4vw,2.8rem)">{title}</h2>
          <hr class="divider left">
          {body}
          {btn}
        </div>
        <div class="media framed {mr}">
          <img src="{img}" alt="{title}" loading="lazy">
        </div>
      </div>
    </section>
""".format(rev=rev, ml=ml, mr=mr, est=est, title=title, body=body, btn=btn, img=img)

def _timeline():
    items = [
        ("1965", "The Beginning", "On 10 May 1965, Late Hajarimal Ji Sanghvi and Late Babulal Ji Sanghvi laid the foundation of KP Sanghvi, beginning their journey with a diamond trading business."),
        ("1970", "From Trade to Creation", "With the right expertise in place, we expanded into diamond manufacturing, gaining control over quality and pricing &mdash; marking the next chapter in our growth."),
        ("1993", "Sightholder Status", "We became De Beers Sightholders, a symbol of trust, quality and industry leadership."),
        ("1998", "Compassion &amp; Technology", "A 185-acre animal shelter was inaugurated for 5,000+ rescued animals, and we pioneered the industry&rsquo;s first in-house diamond laser cutting machine."),
        ("2000", "Jewellery Venture", "Launched KP Jewellery, marking the group&rsquo;s strategic diversification from diamonds into the fine jewellery business."),
        ("2007", "Infrastructure Venture", "Unveiled KP Infra, the group&rsquo;s real estate and infrastructure division, further diversifying our portfolio."),
        ("2010", "Empowering Women", "We set up the industry&rsquo;s first all-women&rsquo;s diamond manufacturing factory, championing female empowerment in our workforce."),
        ("2012", "Ethical Excellence", "Honoured as a Rio Tinto Select Diamantaire and certified by the Responsible Jewellery Council (RJC) for ethical and sustainable practices."),
        ("2014", "Smarter Systems", "Developed a proprietary ERP system, streamlining operations and enabling end-to-end traceability across our processes."),
        ("2019", "Serena Williams Collaboration", "We partnered with tennis legend Serena Williams to help launch her jewellery brand globally."),
        ("2022", "International Expansion", "Opened our first international diamond manufacturing unit in Botswana and celebrated 165+ team members with 25+ years of service."),
        ("2023", "Venture &amp; Responsibility", "Unveiled KPS Capital, our venture arm, joined the Natural Diamond Council and aligned with the United Nations Sustainable Development Goals."),
        ("2024", "WJI 2030", "Strengthened our global responsibility by becoming a member of the World Jewellery Initiative 2030, co-founded by Kering and Cartier."),
        ("2025", "A New Era", "Earned Platinum LEED certification; launched Studio65 as a high-jewellery atelier; and introduced Emfex Energy for intelligent energy systems."),
        ("2026", "UN WEPs", "Became a signatory to the UN Women&rsquo;s Empowerment Principles (UN WEPs), deepening our commitment to gender equality."),
    ]
    out = []
    for yr, t, d in items:
        out.append(
            '<div class="tl-item reveal"><span class="dot" aria-hidden="true"></span>'
            '<div class="yr">{yr}</div><h3>{t}</h3><p>{d}</p></div>'.format(yr=yr, t=t, d=d))
    return "\n          ".join(out)

def _news():
    banner_ = banner("News &amp; Events",
                     "Milestones, announcements and moments that define our journey.",
                     "News &amp; Events", "assets/images/home/hero-2.jpg")
    items = [
        ("2026", "Milestone", "Signatory to UN Women&rsquo;s Empowerment Principles", "KP Sanghvi deepens its commitment to gender equality by becoming a signatory to the UN Women&rsquo;s Empowerment Principles (UN WEPs)."),
        ("2025", "Launch", "Emfex Energy Powers a New Era", "The group channels 60 years of excellence into intelligent energy systems &mdash; introducing Emfex Energy&rsquo;s BESS and EV charging solutions."),
        ("2025", "Launch", "Studio65 High-Jewellery Atelier Debuts", "Studio65 transforms six decades of heritage into bold design and master craftsmanship for discerning clientele."),
        ("2025", "Recognition", "Platinum LEED Certification Achieved", "Our state-of-the-art factories earn Platinum LEED certification &mdash; the highest recognition in green building."),
        ("2024", "Membership", "Joining WJI 2030", "We become a member of the World Jewellery Initiative 2030, co-founded by Kering and Cartier."),
        ("2023", "Expansion", "KPS Capital &amp; Global Alliances", "We unveil our venture arm KPS Capital, join the Natural Diamond Council and align with the UN Sustainable Development Goals."),
    ]
    cards = []
    for yr, tag, t, d in items:
        cards.append(
            """<article class="biz-card reveal" style="min-height:340px">
            <div class="bg" style="background-image:url('assets/images/home/hero-3.jpg')"></div>
            <div class="content">
              <p class="est">{yr} &nbsp;&middot;&nbsp; {tag}</p>
              <h3>{t}</h3>
              <p>{d}</p>
            </div>
          </article>""".format(yr=yr, tag=tag, t=t, d=d))
    body = banner_ + """    <section class="section cream">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Latest Milestones</p>
          <h2 class="section-title center reveal delay-1">In the News</h2>
          <hr class="divider reveal delay-1">
          <p class="reveal delay-2">A selection of recent milestones from across the KP Sanghvi Group. For media enquiries, please reach out to our team.</p>
        </div>
        <div class="grid grid-3">
          {cards}
        </div>
      </div>
    </section>
""".format(cards="\n          ".join(cards))
    body += cta("For Media &amp; Press Enquiries", "Our communications team is happy to help with interviews, assets and information.", "Contact Us")
    return body

def _directors():
    body = banner("Directors",
                  "The leadership stewarding six decades of heritage and the vision for tomorrow.",
                  "Directors", "assets/images/home/hero-1.jpg")
    body += """    <section class="section intro">
      <div class="container">
        <p class="eyebrow reveal">Our Leadership</p>
        <h2 class="section-title reveal delay-1">Guided by Vision, United by Values</h2>
        <hr class="divider reveal delay-1">
        <p class="lead reveal delay-2" style="margin-top:1.8rem">Across three generations, the leadership of the KP Sanghvi Group has combined entrepreneurial vision with an unwavering commitment to integrity, excellence and responsible growth.</p>
      </div>
    </section>

    <section class="section cream">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Board of Directors</p>
          <h2 class="section-title center reveal delay-1">Meet the Directors</h2>
          <hr class="divider reveal delay-1">
        </div>

        <!-- =====================================================================
             DIRECTOR MANAGEMENT  —  HOW TO ADD / EDIT A DIRECTOR
             ---------------------------------------------------------------------
             1. Put the photograph in:      assets/images/directors/
                (recommended: portrait, roughly 800 x 1000 px, .jpg)
             2. Copy ONE <div class="director-card"> ... </div> block below.
             3. Change the image filename in  src="assets/images/directors/........"
             4. Change the name inside  <h3>...</h3>
             5. Change the designation inside  <p>...</p>
             6. Update the alt="" text to the director's name.
             7. Save the file. That's it — no code, no database, no build step.

             TIP: To REMOVE a director, delete their whole <div class="director-card"> block.
             The grid automatically shows 3 per row (desktop), 2 (tablet), 1 (mobile).
             ===================================================================== -->

        <div class="director-grid">

          <!-- ===== DIRECTOR CARD (copy this whole block to add a director) ===== -->
          <div class="director-card reveal">
            <div class="director-image">
              <!-- Replace director-01.jpg with your photo file -->
              <img src="assets/images/directors/director-01.jpg" alt="Director Name" loading="lazy"
                   onerror="this.parentElement.classList.add('placeholder');this.style.display='none';this.parentElement.insertAdjacentHTML('beforeend',DIRECTOR_PLACEHOLDER);">
            </div>
            <div class="director-info">
              <h3>Director Name</h3>
              <p>Director Designation</p>
            </div>
          </div>
          <!-- ===== END DIRECTOR CARD ===== -->

          <div class="director-card reveal delay-1">
            <div class="director-image">
              <img src="assets/images/directors/director-02.jpg" alt="Director Name" loading="lazy"
                   onerror="this.parentElement.classList.add('placeholder');this.style.display='none';this.parentElement.insertAdjacentHTML('beforeend',DIRECTOR_PLACEHOLDER);">
            </div>
            <div class="director-info">
              <h3>Director Name</h3>
              <p>Director Designation</p>
            </div>
          </div>

          <div class="director-card reveal delay-2">
            <div class="director-image">
              <img src="assets/images/directors/director-03.jpg" alt="Director Name" loading="lazy"
                   onerror="this.parentElement.classList.add('placeholder');this.style.display='none';this.parentElement.insertAdjacentHTML('beforeend',DIRECTOR_PLACEHOLDER);">
            </div>
            <div class="director-info">
              <h3>Director Name</h3>
              <p>Director Designation</p>
            </div>
          </div>

          <div class="director-card reveal">
            <div class="director-image">
              <img src="assets/images/directors/director-04.jpg" alt="Director Name" loading="lazy"
                   onerror="this.parentElement.classList.add('placeholder');this.style.display='none';this.parentElement.insertAdjacentHTML('beforeend',DIRECTOR_PLACEHOLDER);">
            </div>
            <div class="director-info">
              <h3>Director Name</h3>
              <p>Director Designation</p>
            </div>
          </div>

          <div class="director-card reveal delay-1">
            <div class="director-image">
              <img src="assets/images/directors/director-05.jpg" alt="Director Name" loading="lazy"
                   onerror="this.parentElement.classList.add('placeholder');this.style.display='none';this.parentElement.insertAdjacentHTML('beforeend',DIRECTOR_PLACEHOLDER);">
            </div>
            <div class="director-info">
              <h3>Director Name</h3>
              <p>Director Designation</p>
            </div>
          </div>

          <div class="director-card reveal delay-2">
            <div class="director-image">
              <img src="assets/images/directors/director-06.jpg" alt="Director Name" loading="lazy"
                   onerror="this.parentElement.classList.add('placeholder');this.style.display='none';this.parentElement.insertAdjacentHTML('beforeend',DIRECTOR_PLACEHOLDER);">
            </div>
            <div class="director-info">
              <h3>Director Name</h3>
              <p>Director Designation</p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- Placeholder graphic used automatically when a director photo is missing -->
    <script>
      var DIRECTOR_PLACEHOLDER = '""" + PLACEHOLDER_SVG.replace("'", "\\'") + """';
    </script>
"""
    body += cta("Building the Future, Responsibly", "Learn more about the group our directors lead.", "About the Group", "about.html")
    return body

def _contact():
    body = banner("We&rsquo;d Love to Hear From You",
                  "Take the first step &mdash; we will take care of the rest.",
                  "Contact Us", "assets/images/home/hero-2.jpg")
    body += """    <section class="section">
      <div class="container contact-grid">
        <div class="reveal-left">
          <p class="eyebrow">Reach Out</p>
          <h2 class="section-title" style="font-size:clamp(1.9rem,3.4vw,2.6rem)">Send Us a Message</h2>
          <hr class="divider left">
          <form id="contact-form" novalidate style="margin-top:1.8rem">
            <div class="form-row">
              <div class="form-field">
                <label for="enquiry">Enquiry Type</label>
                <select id="enquiry" name="enquiry" required>
                  <option value="">Select&hellip;</option>
                  <option>General Enquiry</option>
                  <option>Business / Partnership</option>
                  <option>Careers</option>
                  <option>Media &amp; Press</option>
                </select>
              </div>
              <div class="form-field">
                <label for="vertical">Business Vertical</label>
                <select id="vertical" name="vertical" required>
                  <option value="">Select&hellip;</option>
                  <option>Diamond</option>
                  <option>Jewellery</option>
                  <option>Infrastructure</option>
                  <option>Energy Systems</option>
                  <option>Corporate</option>
                </select>
              </div>
            </div>
            <div class="form-row">
              <div class="form-field">
                <label for="fname">First Name</label>
                <input type="text" id="fname" name="fname" required autocomplete="given-name">
              </div>
              <div class="form-field">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" autocomplete="tel">
              </div>
            </div>
            <div class="form-field">
              <label for="email">Email</label>
              <input type="email" id="email" name="email" required autocomplete="email">
            </div>
            <div class="form-field">
              <label for="message">Message</label>
              <textarea id="message" name="message" required></textarea>
            </div>
            <button class="btn solid" type="submit">Send Message <span class="arrow">&rarr;</span></button>
            <p class="form-note" id="form-status" tabindex="-1" hidden></p>
            <p class="form-note">This form is part of a static website and is not yet connected to a mail service. See the README for how to connect it.</p>
          </form>
        </div>

        <div class="reveal-right">
          <p class="eyebrow">Head Office</p>
          <h2 class="section-title" style="font-size:clamp(1.9rem,3.4vw,2.6rem)">Mumbai</h2>
          <hr class="divider left">
          <p style="margin-top:1.2rem;color:var(--muted)">GW 7011/7012, G Block, Bharat Diamond Bourse, Bandra-Kurla Complex, Bandra (E), Mumbai - 400 051</p>
          <p style="color:var(--muted)"><a href="tel:+912261233333">+91-22-6123 3333</a> &middot; <a href="tel:+912223630315">+91-22-2363 0315</a><br><a href="mailto:info@kpsanghvi.com">info@kpsanghvi.com</a></p>
          <div class="map-wrap" style="margin-top:1.4rem">
            <iframe title="KP Sanghvi Mumbai — Bharat Diamond Bourse" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
              src="https://maps.google.com/maps?q=Bharat%20Diamond%20Bourse%2C%20Bandra%20Kurla%20Complex%2C%20Mumbai&t=&z=15&ie=UTF8&iwloc=&output=embed"></iframe>
          </div>
        </div>
      </div>
    </section>

    <section class="section cream">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow center reveal">Global Offices</p>
          <h2 class="section-title center reveal delay-1">Find Us Around the World</h2>
          <hr class="divider reveal delay-1">
        </div>
        <div class="office-list">
          {offices}
        </div>
      </div>
    </section>
""".format(offices=_offices())
    return body

def _legal(title, sections):
    body = banner(title, "", title.replace("&amp;", "&amp;"), "assets/images/home/hero-2.jpg")
    inner = ['<div class="container" style="max-width:900px">']
    for h, p in sections:
        inner.append('<h2 class="section-title reveal" style="font-size:clamp(1.5rem,2.6vw,2rem);margin:2.2rem 0 .8rem">{h}</h2><p class="reveal delay-1">{p}</p>'.format(h=h, p=p))
    inner.append('</div>')
    body += '    <section class="section intro" style="text-align:left">\n      ' + "\n      ".join(inner) + "\n    </section>\n"
    return body

def _sitemap():
    body = banner("Sitemap", "Find your way around the KP Sanghvi Group website.", "Sitemap", "assets/images/home/hero-3.jpg")
    groups = [
        ("Main", [("Home", "index.html"), ("About Us", "about.html"), ("Our Journey", "our-journey.html"),
                  ("Directors", "directors.html"), ("Sustainability", "sustainability.html"),
                  ("News &amp; Events", "news-events.html"), ("Contact Us", "contact.html")]),
        ("Businesses", [("Diamond", "diamonds.html"), ("Jewellery", "jewellery.html"),
                        ("Infrastructure", "infrastructure.html"), ("Energy Systems", "energy.html")]),
        ("Legal", [("Terms &amp; Conditions", "terms.html"), ("Privacy Policy", "privacy.html"),
                   ("Cookies Policy", "cookies.html")]),
    ]
    cols = []
    for name, links in groups:
        lis = "".join('<li style="margin-bottom:.6rem"><a href="{h}" style="color:var(--body)">{l}</a></li>'.format(h=h, l=l) for l, h in links)
        cols.append('<div class="reveal"><h3 style="color:var(--gold);font-size:1.4rem;margin-bottom:1rem">{n}</h3><ul>{lis}</ul></div>'.format(n=name, lis=lis))
    body += """    <section class="section">
      <div class="container">
        <div class="grid grid-3">
          {cols}
        </div>
      </div>
    </section>
""".format(cols="\n          ".join(cols))
    return body

def _offices():
    data = [
        ("Mumbai", "GW 7011/7012, G Block, Bharat Diamond Bourse, Bandra-Kurla Complex, Bandra (E), Mumbai - 400 051", ["+91-22-6123 3333", "+91-22-2363 0315"], "info@kpsanghvi.com"),
        ("Surat", "Nr. Umiya Mata Temple, Umiya Chowk, A.K. Road, Surat - 395 008, Gujarat, India", ["+91-261-256 9100"], "info@kpsanghvi.com"),
        ("Ahmedabad", "1004-1005, Shapath V, Opp. Karnavati Club, S.G. Highway, Vejalpur, Ahmedabad - 380 051, Gujarat, India", [], "info@kpsanghvi.com"),
        ("Antwerp", "Hoveniersstraat 30, box 192, 2018 Antwerp, Belgium", ["+32 3 201 30 00"], "antwerp@kpsanghvi.eu"),
        ("New York", "12E, 46th Street, Floor 8, New York, NY 10017, USA", ["+1-212-575-2358"], "info@kpsanghvi.us"),
        ("Dubai", "ALMAS-29-A&J, Almas Tower, Plot No. JLT-PH1-A0, Jumeirah Lakes Towers, Dubai, UAE", ["+971-4-453-73-80"], "info@kpsanghvi.ae"),
        ("Hong Kong", "Flat/Rm 2001, 20/F, Empress Plaza, 17-19 Chatham Road, Tsim Sha Tsui, Kowloon, Hong Kong", ["+852-2316-2123"], "info@kpsanghvi.hk"),
        ("Botswana", "Plot 54734, Unit 3, Block B, Grand Union Building, Central Business District, Gaborone, Botswana", ["+267 316 4965"], "info@kpsanghvi.co.bw"),
    ]
    out = []
    for city, addr, phones, email in data:
        ph = "".join('<a href="tel:{cl}">{p}</a><br>'.format(cl=p.replace(" ", "").replace("-", ""), p=p) for p in phones)
        out.append(
            '<div class="office reveal"><h4>{city}</h4><p>{addr}</p>'
            '<p>{ph}<a href="mailto:{email}">{email}</a></p></div>'.format(
                city=city, addr=addr, ph=ph, email=email))
    return "\n          ".join(out)
