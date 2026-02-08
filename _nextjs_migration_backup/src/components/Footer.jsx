import Link from 'next/link';

export default function Footer() {
    return (
        <div id="footer-container">
            <footer style={{ backgroundColor: 'var(--surface, #ffffff)', padding: '4rem 1rem 2rem', marginTop: 'auto', borderTop: '1px solid rgba(0,0,0,0.05)' }}>
                <div style={{ maxWidth: '1200px', margin: '0 auto', display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '2rem' }}>

                    {/* Brand */}
                    <div className="footer-col">
                        <Link href="/" className="logo" style={{ fontSize: '1.5rem', fontWeight: 800, color: 'var(--primary-600, #6f42c1)', textDecoration: 'none', display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem' }}>
                            <span style={{ color: 'var(--primary-500, #8e44ad)', fontSize: '1.8rem' }}>&int;</span> SJMaths
                        </Link>
                        <p style={{ color: 'var(--muted, #6b7280)', fontSize: '0.95rem', lineHeight: 1.6, marginBottom: '1.5rem' }}>
                            Empowering students with AI-driven resources, comprehensive notes, and expert guidance to master mathematics.
                        </p>
                        <div className="social-links" style={{ display: 'flex', gap: '1rem' }}>
                            <a href="#" aria-label="Facebook" style={{ color: 'var(--muted, #6b7280)', fontSize: '1.2rem', transition: 'color 0.3s' }}><i className="fab fa-facebook"></i></a>
                            <a href="#" aria-label="Twitter" style={{ color: 'var(--muted, #6b7280)', fontSize: '1.2rem', transition: 'color 0.3s' }}><i className="fab fa-twitter"></i></a>
                            <a href="#" aria-label="Instagram" style={{ color: 'var(--muted, #6b7280)', fontSize: '1.2rem', transition: 'color 0.3s' }}><i className="fab fa-instagram"></i></a>
                            <a href="#" aria-label="YouTube" style={{ color: 'var(--muted, #6b7280)', fontSize: '1.2rem', transition: 'color 0.3s' }}><i className="fab fa-youtube"></i></a>
                        </div>
                    </div>

                    {/* Quick Links */}
                    <div className="footer-col">
                        <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: '1.2rem', color: 'var(--text-dark, #1f2937)' }}>Quick Links</h3>
                        <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
                            <li><Link href="/" style={{ color: 'var(--muted, #6b7280)', textDecoration: 'none', transition: 'color 0.2s' }}>Home</Link></li>
                            <li><Link href="/about" style={{ color: 'var(--muted, #6b7280)', textDecoration: 'none', transition: 'color 0.2s' }}>About Us</Link></li>
                            <li><Link href="/contact" style={{ color: 'var(--muted, #6b7280)', textDecoration: 'none', transition: 'color 0.2s' }}>Contact</Link></li>
                            <li><Link href="/pages/privacy-policy" style={{ color: 'var(--muted, #6b7280)', textDecoration: 'none', transition: 'color 0.2s' }}>Privacy Policy</Link></li>
                            <li><Link href="/pages/terms" style={{ color: 'var(--muted, #6b7280)', textDecoration: 'none', transition: 'color 0.2s' }}>Terms of Service</Link></li>
                            <li><Link href="/pages/sitemap" style={{ color: 'var(--muted, #6b7280)', textDecoration: 'none', transition: 'color 0.2s' }}>Sitemap</Link></li>
                        </ul>
                    </div>

                    {/* Classes */}
                    <div className="footer-col">
                        <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: '1.2rem', color: 'var(--text-dark, #1f2937)' }}>Classes</h3>
                        <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
                            <li><Link href="/classes/class-9" style={{ color: 'var(--muted, #6b7280)', textDecoration: 'none', transition: 'color 0.2s' }}>Class 9</Link></li>
                            <li><Link href="/classes/class-10" style={{ color: 'var(--muted, #6b7280)', textDecoration: 'none', transition: 'color 0.2s' }}>Class 10</Link></li>
                            <li><Link href="/classes/class-11" style={{ color: 'var(--muted, #6b7280)', textDecoration: 'none', transition: 'color 0.2s' }}>Class 11</Link></li>
                            <li><Link href="/classes/class-12" style={{ color: 'var(--muted, #6b7280)', textDecoration: 'none', transition: 'color 0.2s' }}>Class 12</Link></li>
                        </ul>
                    </div>

                    {/* Get in Touch */}
                    <div className="footer-col">
                        <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: '1.2rem', color: 'var(--text-dark, #1f2937)' }}>Get in Touch</h3>
                        <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
                            <li style={{ display: 'flex', alignItems: 'center', gap: '10px', color: 'var(--muted, #6b7280)' }}>
                                <i className="fas fa-envelope" style={{ color: 'var(--primary-500, #8e44ad)' }}></i>
                                <a href="mailto:sjmaths.help@gmail.com" style={{ color: 'inherit', textDecoration: 'none', transition: 'color 0.2s' }}>sjmaths.help@gmail.com</a>
                            </li>
                            <li style={{ display: 'flex', alignItems: 'center', gap: '10px', color: 'var(--muted, #6b7280)' }}>
                                <i className="fas fa-phone" style={{ color: 'var(--primary-500, #8e44ad)' }}></i>
                                <a href="tel:+919170940900" style={{ color: 'inherit', textDecoration: 'none', transition: 'color 0.2s' }}>+91 9170940900</a>
                            </li>
                        </ul>
                    </div>
                </div>

                <div style={{ maxWidth: '1200px', margin: '3rem auto 0', paddingTop: '2rem', borderTop: '1px solid rgba(0,0,0,0.05)', textAlign: 'center', color: 'var(--muted, #6b7280)', fontSize: '0.9rem' }}>
                    &copy; <span id="footer-year">2026</span> SJMaths. All Rights Reserved.
                </div>
            </footer>
        </div>
    );
}
