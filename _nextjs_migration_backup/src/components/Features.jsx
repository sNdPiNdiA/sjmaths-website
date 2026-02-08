import Link from 'next/link';

export default function Features() {
    return (
        <section id="resources" className="features">
            <div className="section-header animate-on-scroll">
                <h2>Why Choose SJMaths?</h2>
                <p>Premium resources curated for your success</p>
            </div>

            <div className="feature-grid">
                <Link href="/classes/class-10/chapter-wise-notes" className="feature-card animate-on-scroll stagger-1">
                    <div className="f-icon"><i className="fas fa-book-open"></i></div>
                    <h3>Comprehensive Notes</h3>
                    <p>Detailed chapter-wise notes with clear explanations.</p>
                    <span className="feature-link">View Notes <i className="fas fa-arrow-right"></i></span>
                </Link>

                <Link href="/classes/class-10/previous-year-questions" className="feature-card animate-on-scroll stagger-2">
                    <div className="f-icon"><i className="fas fa-clock-rotate-left"></i></div>
                    <h3>Chapterwise PYQs</h3>
                    <p>Practice past 10 years' questions sorted by chapter.</p>
                    <span className="feature-link">Solve PYQs <i className="fas fa-arrow-right"></i></span>
                </Link>

                <Link href="/classes/class-10/ncert-exercise-practice" className="feature-card animate-on-scroll stagger-3">
                    <div className="f-icon"><i className="fas fa-pen-to-square"></i></div>
                    <h3>NCERT Practice Exercises</h3>
                    <p>Step-by-step solutions for every textbook exercise.</p>
                    <span className="feature-link">Start Practice <i className="fas fa-arrow-right"></i></span>
                </Link>
            </div>
        </section>
    );
}
