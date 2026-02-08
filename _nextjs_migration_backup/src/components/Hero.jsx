import Link from 'next/link';

export default function Hero() {
    return (
        <section className="hero" id="main-content">
            {/* LCP Optimization: Explicit Image Element with Fetch Priority */}
            <picture className="hero-bg-image">
                <source media="(max-width: 768px)" srcSet="/assets/images/sjmaths-mobile.webp" />
                <img src="/assets/images/sjmaths-bg-desktop.webp" alt="Mathematics Background" fetchPriority="high"
                    width="1920" height="1080" loading="lazy" />
            </picture>

            <div className="blob blob-1"></div>
            <div className="blob blob-2"></div>

            {/* Note: Carousel logic will need React state if we want it interactive. 
          For Phase 1 MVP, we can just show the first slide or keep the static structure 
          and let the legacy main.js handle it (if it selects by class). 
          However, legacy JS might not attach to React DOM elements easily.
          We will keep the structure exactly as is. */}

            <button className="hero-arrow prev" id="heroPrev" aria-label="Previous Slide"><i
                className="fas fa-chevron-left"></i></button>
            <button className="hero-arrow next" id="heroNext" aria-label="Next Slide"><i
                className="fas fa-chevron-right"></i></button>

            <div className="carousel-track" id="heroCarousel">
                {/* Slide 1: Main */}
                <div className="carousel-slide active">
                    <div className="hero-content" data-href="#classes">
                        <h1>Master Mathematics<br />with Confidence</h1>
                        <p>Your one-stop destination for NCERT Solutions, Notes, PYQs, and Sample Papers. Designed for
                            students to excel in exams.</p>
                        <p className="seo-text">
                            SJMaths by Sandeep Jaiswal (PGT Maths) provides free NCERT Solutions, Class 9 to 12 Maths Notes,
                            Previous Year Questions, Sample Papers, Board Exam Strategies and Board-focused concept mastery
                            for Indian students.
                        </p>

                        <div className="cta-group" data-animation-delay="0.4s">
                            <Link href="#classes" className="btn btn-primary">Start Learning <i className="fas fa-arrow-right"></i></Link>
                            <Link href="#resources" className="btn btn-secondary">Explore Resources</Link>
                        </div>
                    </div>
                </div>

                {/* Slide 2: Live Classes / Ebooks */}
                <div className="carousel-slide">
                    <div className="hero-content" data-href="/classes/live-class">
                        <h2>Live Classes &<br />Premium Resources</h2>
                        <p>Join interactive live sessions or download exclusive e-books to boost your preparation.</p>
                        <div className="cta-group">
                            <Link href="/pages/pricing" className="btn btn-primary">Join Live Class <i
                                className="fas fa-video"></i></Link>
                            <Link href="/ebooks" className="btn btn-secondary">Get E-books <i
                                className="fas fa-book"></i></Link>
                        </div>
                    </div>
                </div>
            </div>

            <div className="carousel-indicators">
                <button className="indicator active" data-slide="0" aria-label="Go to slide 1"></button>
                <button className="indicator" data-slide="1" aria-label="Go to slide 2"></button>
            </div>
        </section>
    );
}
