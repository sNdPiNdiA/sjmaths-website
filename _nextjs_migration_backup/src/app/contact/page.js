import Link from 'next/link';

export const metadata = {
    title: 'Contact Us | SJMaths',
    description: 'Get in touch with SJMaths for queries regarding study materials, live classes, or technical support.',
};

export default function ContactPage() {
    return (
        <main className="container" style={{ maxWidth: '600px', margin: '4rem auto', padding: '0 20px' }}>

            {/* Glass Container */}
            <div style={{
                background: 'rgba(255, 255, 255, 0.95)',
                backdropFilter: 'blur(10px)',
                border: '1px solid rgba(255, 255, 255, 0.2)',
                borderRadius: '1.5rem',
                boxShadow: '0 10px 30px -5px rgba(0, 0, 0, 0.1)',
                padding: '3rem',
            }}>

                <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                    <h1 style={{ color: '#8e44ad', marginBottom: '0.5rem', fontSize: '2.5rem' }}>Get in Touch</h1>
                    <p style={{ color: '#7f8c8d' }}>Have questions? We'd love to hear from you.</p>
                </div>

                <form action="https://formspree.io/f/xkoggobv" method="POST">
                    <div style={{ marginBottom: '1.5rem' }}>
                        <label htmlFor="name" style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 500, color: '#333' }}>Name</label>
                        <input type="text" id="name" name="name" placeholder="Your Name" required
                            style={{
                                width: '100%',
                                padding: '12px',
                                border: '1px solid #ddd',
                                borderRadius: '10px',
                                background: 'rgba(255,255,255,0.5)',
                                fontFamily: 'inherit'
                            }}
                        />
                    </div>

                    <div style={{ marginBottom: '1.5rem' }}>
                        <label htmlFor="email" style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 500, color: '#333' }}>Email</label>
                        <input type="email" id="email" name="email" placeholder="student@example.com" required
                            style={{
                                width: '100%',
                                padding: '12px',
                                border: '1px solid #ddd',
                                borderRadius: '10px',
                                background: 'rgba(255,255,255,0.5)',
                                fontFamily: 'inherit'
                            }}
                        />
                    </div>

                    <div style={{ marginBottom: '1.5rem' }}>
                        <label htmlFor="message" style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 500, color: '#333' }}>Message</label>
                        <textarea id="message" name="message" rows="5" placeholder="How can we help you?" required
                            style={{
                                width: '100%',
                                padding: '12px',
                                border: '1px solid #ddd',
                                borderRadius: '10px',
                                background: 'rgba(255,255,255,0.5)',
                                fontFamily: 'inherit'
                            }}
                        ></textarea>
                    </div>

                    <button type="submit" style={{
                        width: '100%',
                        padding: '12px',
                        background: '#8e44ad',
                        color: 'white',
                        border: 'none',
                        borderRadius: '10px',
                        fontWeight: 600,
                        cursor: 'pointer',
                        fontSize: '1rem',
                        transition: 'background-color 0.2s'
                    }}>
                        Send Message
                    </button>
                </form>

            </div>
        </main>
    );
}
