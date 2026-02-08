import Link from 'next/link';

export const metadata = {
    title: 'About Us | SJMaths',
    description: 'Learn about SJMaths, our mission to provide high-quality free mathematics education for Class 9-12.',
};

export default function AboutPage() {
    return (
        <main className="container" style={{ maxWidth: '900px', margin: '4rem auto', padding: '0 20px' }}>

            {/* Glass Container */}
            <div style={{
                background: 'rgba(255, 255, 255, 0.95)',
                backdropFilter: 'blur(10px)',
                border: '1px solid rgba(255, 255, 255, 0.2)',
                borderRadius: '1.5rem',
                boxShadow: '0 10px 30px -5px rgba(0, 0, 0, 0.1)',
                padding: '3rem',
            }}>

                <h1 style={{ color: '#8e44ad', marginBottom: '0.5rem', fontSize: '2.5rem' }}>About Us</h1>
                <p style={{ color: '#7f8c8d', fontSize: '1.1rem', marginBottom: '2.5rem' }}>
                    Empowering students to master mathematics with confidence.
                </p>

                <h2 style={{ color: '#2c3e50', marginTop: '2rem', marginBottom: '1rem', fontSize: '1.5rem' }}>Who We Are</h2>
                <p style={{ color: '#555', lineHeight: '1.8', marginBottom: '1rem' }}>
                    SJMaths is a premier online learning platform dedicated to providing high-quality mathematics education for students from Class 9 to 12. We believe that math is not just about numbers, but about developing a problem-solving mindset.
                </p>
                <p style={{ color: '#555', lineHeight: '1.8', marginBottom: '1rem' }}>
                    Our resources are curated by expert educators to align perfectly with the CBSE curriculum, ensuring that you stay ahead in your exams. Whether you are looking for comprehensive notes, previous year questions, or interactive quizzes, we have it all.
                </p>

                {/* Mission Grid */}
                <div style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
                    gap: '2rem',
                    marginTop: '3rem'
                }}>

                    {/* Mission */}
                    <div style={{
                        background: 'rgba(255, 255, 255, 0.8)',
                        padding: '2rem',
                        borderRadius: '20px',
                        boxShadow: '0 10px 30px rgba(0,0,0,0.05)',
                        textAlign: 'center',
                        border: '1px solid rgba(0,0,0,0.05)'
                    }}>
                        <div style={{
                            fontSize: '2.5rem',
                            color: '#8e44ad',
                            marginBottom: '1rem',
                            background: 'rgba(142, 68, 173, 0.1)',
                            width: '70px',
                            height: '70px',
                            display: 'inline-flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            borderRadius: '50%'
                        }}>
                            <i className="fas fa-bullseye"></i>
                        </div>
                        <h3 style={{ marginBottom: '0.8rem', color: '#2c3e50', fontSize: '1.2rem' }}>Our Mission</h3>
                        <p style={{ fontSize: '0.95rem', margin: 0, color: '#555' }}>
                            To make quality education accessible to every student and remove the fear of mathematics through simplified learning.
                        </p>
                    </div>

                    {/* Vision */}
                    <div style={{
                        background: 'rgba(255, 255, 255, 0.8)',
                        padding: '2rem',
                        borderRadius: '20px',
                        boxShadow: '0 10px 30px rgba(0,0,0,0.05)',
                        textAlign: 'center',
                        border: '1px solid rgba(0,0,0,0.05)'
                    }}>
                        <div style={{
                            fontSize: '2.5rem',
                            color: '#8e44ad',
                            marginBottom: '1rem',
                            background: 'rgba(142, 68, 173, 0.1)',
                            width: '70px',
                            height: '70px',
                            display: 'inline-flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            borderRadius: '50%'
                        }}>
                            <i className="fas fa-eye"></i>
                        </div>
                        <h3 style={{ marginBottom: '0.8rem', color: '#2c3e50', fontSize: '1.2rem' }}>Our Vision</h3>
                        <p style={{ fontSize: '0.95rem', margin: 0, color: '#555' }}>
                            To become India's most trusted companion for mathematics board exam preparation and conceptual clarity.
                        </p>
                    </div>

                </div>

            </div>
        </main>
    );
}
