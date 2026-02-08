import Link from 'next/link';

export default function ClassGrid() {
    return (
        <section id="classes" className="classes-section">
            <div className="section-header animate-on-scroll">
                <h2>Start Your Journey</h2>
                <p>Select your class to access tailored study materials</p>
            </div>

            <div className="class-grid animate-on-scroll">
                {/* Class 9 */}
                <Link href="/classes/class-9" className="class-card card-9">
                    <div className="card-bg-icon">9</div>
                    <div className="card-content">
                        <span className="class-badge">Foundation</span>
                        <h3>Class 9</h3>
                        <p>Build a strong base with Notes, NCERT Solutions & Basics.</p>
                        <div className="card-action"><span>Explore</span> <i className="fas fa-arrow-right"></i></div>
                    </div>
                </Link>

                {/* Class 10 */}
                <Link href="/classes/class-10" className="class-card card-10">
                    <div className="card-bg-icon">10</div>
                    <div className="card-content">
                        <span className="class-badge badge-board">Board Exam</span>
                        <h3>Class 10</h3>
                        <p>Master Boards with PYQs, Sample Papers & Exam Strategy.</p>
                        <div className="card-action"><span>Explore</span> <i className="fas fa-arrow-right"></i></div>
                    </div>
                </Link>

                {/* Class 11 */}
                <Link href="/classes/class-11" className="class-card card-11">
                    <div className="card-bg-icon">11</div>
                    <div className="card-content">
                        <span className="class-badge">Concept</span>
                        <h3>Class 11</h3>
                        <p>Deep dive into advanced mathematics and core concepts.</p>
                        <div className="card-action"><span>Explore</span> <i className="fas fa-arrow-right"></i></div>
                    </div>
                </Link>

                {/* Class 12 */}
                <Link href="/classes/class-12" className="class-card card-12">
                    <div className="card-bg-icon">12</div>
                    <div className="card-content">
                        <span className="class-badge badge-final">Final Year</span>
                        <h3>Class 12</h3>
                        <p>Ace your finals with Calculus, Vectors & 3D Geometry.</p>
                        <div className="card-action"><span>Explore</span> <i className="fas fa-arrow-right"></i></div>
                    </div>
                </Link>

                {/* Maths Mastery */}
                <Link href="/maths-mastery" className="class-card card-maths-mastery">
                    <div className="card-bg-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em"
                            fill="currentColor">
                            <title>Maths Mastery Icon</title>
                            <path fillRule="evenodd"
                                d="M11.25 4.5a.75.75 0 01.75.75v13.5a.75.75 0 01-1.5 0V5.25a.75.75 0 01.75-.75zM5.25 10.5a.75.75 0 01.75-.75h12a.75.75 0 010 1.5H6a.75.75 0 01-.75-.75zM3 6.375a.75.75 0 01.75-.75h16.5a.75.75 0 010 1.5H3.75a.75.75 0 01-.75-.75zM12 17.25a.75.75 0 01.75.75v.008a.75.75 0 01-1.5 0V18a.75.75 0 01.75-.75z"
                                clipRule="evenodd" />
                        </svg>
                    </div>
                    <div className="card-content">
                        <span className="class-badge">Mastery</span>
                        <h3>Maths Mastery</h3>
                        <p>Learn maths step by step with mastery-based progression.</p>
                        <div className="card-action"><span>Start Learning</span> <i className="fas fa-arrow-right"></i></div>
                    </div>
                </Link>

                {/* Live Classes */}
                <div className="class-card">
                    <div className="card-bg-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"
                            fill="currentColor">
                            <title>Live Classes Icon</title>
                            <path
                                d="M4.5 4.5a3 3 0 00-3 3v9a3 3 0 003 3h8.25a3 3 0 003-3v-9a3 3 0 00-3-3H4.5zM19.94 18.75l-2.69-2.69V7.94l2.69-2.69c.944-.944 2.56-.276 2.56 1.06v11.38c0 1.336-1.616 2.004-2.56 1.06z" />
                        </svg>
                    </div>
                    <div className="card-content">
                        <div className="card-badge live-badge">LIVE BATCH</div>
                        <h3>Live Classes</h3>
                        <p>
                            Join interactive sessions with expert mentors. Clear doubts instantly.
                        </p>
                        <Link href="/classes/live-class" className="explore-link">
                            Join Now <i className="fas fa-arrow-right"></i>
                        </Link>
                    </div>
                </div>
            </div>
        </section>
    );
}
