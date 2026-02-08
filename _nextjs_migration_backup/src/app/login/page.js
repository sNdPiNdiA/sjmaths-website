'use client';

import Link from 'next/link';
import { useEffect } from 'react';

// NOTE: This uses the existing legacy auth script for now.
// In a full refactor, we should move to `firebase/auth` npm package.

export default function LoginPage() {

    // Dynamically load the legacy auth script
    useEffect(() => {
        // We check if script is already present to avoid duplicates
        /*
        const script = document.createElement('script');
        script.src = "/assets/js/auth.js";
        script.type = "module";
        script.async = true;
        document.body.appendChild(script);
    
        return () => {
          document.body.removeChild(script);
        }
        */
        // NOTE: The legacy auth.js relies on firebase-config.js being in the same directory.
        // Since we moved assets to /public/assets, the relative imports in auth.js (import ... from "./firebase-config.js") might break
        // if served from /login.
        // However, since we copied `_legacy_site/assets` to `public/assets`, the path `/assets/js/auth.js` exists.
        // BUT common issue: ES modules in browser require correct paths.
        // We will render the UI for now. The functionality requires a deeper refactor correctly identified as "Out of Scope" for Phase 3.
    }, []);

    return (
        <div className="auth-page" style={{
            display: 'flex',
            minHeight: '100vh',
            background: '#f8f9fa'
        }}>
            {/* Branding Side */}
            <div className="auth-branding" style={{
                flex: 1,
                background: 'linear-gradient(135deg, #8e44ad, #9b59b6)',
                color: 'white',
                padding: '4rem',
                display: 'none', // Hidden on mobile by default, desktop logic handled by CSS or media query
                flexDirection: 'column',
                justifyContent: 'center'
            }}>
                <Link href="/" className="logo" style={{ color: 'white', fontSize: '2rem', fontWeight: 'bold', textDecoration: 'none', marginBottom: '2rem' }}>
                    <span style={{ fontSize: '2.5rem' }}>&int;</span> SJMaths
                </Link>
                <div className="branding-content">
                    <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>Unlock Your Mathematical Potential.</h2>
                    <p style={{ fontSize: '1.2rem', opacity: 0.9 }}>Gain access to a world of resources designed for your success.</p>
                    <ul style={{ listStyle: 'none', padding: 0, marginTop: '2rem', fontSize: '1.1rem', lineHeight: 2 }}>
                        <li><i className="fas fa-check-circle"></i> Comprehensive NCERT Solutions</li>
                        <li><i className="fas fa-star"></i> Curated Previous Year Questions (PYQs)</li>
                        <li><i className="fas fa-chart-line"></i> In-depth Topic-wise Notes</li>
                    </ul>
                </div>
            </div>

            {/* Login Container */}
            <div className="login-container" style={{
                flex: 1,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                padding: '2rem'
            }}>
                <div className="form-content" style={{ maxWidth: '400px', width: '100%', textAlign: 'center' }}>
                    <Link href="/" style={{
                        display: 'inline-block',
                        marginBottom: '2rem',
                        color: '#8e44ad',
                        textDecoration: 'none',
                        fontWeight: 600
                    }}>
                        &larr; Back to Home
                    </Link>

                    <h1 style={{ fontSize: '2rem', marginBottom: '0.5rem', color: '#2c3e50' }}>Login</h1>
                    <p style={{ color: '#7f8c8d', marginBottom: '2rem' }}>Sign in with your Google account.</p>

                    <button id="googleLoginBtn" style={{
                        width: '100%',
                        padding: '12px',
                        background: 'white',
                        border: '1px solid #ddd',
                        borderRadius: '50px',
                        fontSize: '1rem',
                        color: '#333',
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        gap: '10px',
                        boxShadow: '0 2px 4px rgba(0,0,0,0.05)'
                    }}>
                        <i className="fab fa-google" style={{ color: '#DB4437' }}></i> Sign in with Google
                    </button>

                    <div style={{ marginTop: '2rem', fontSize: '0.85rem', color: '#999' }}>
                        By continuing, you agree to the SJMaths <Link href="/pages/terms.html" style={{ color: '#8e44ad' }}>Terms</Link> and <Link href="/pages/privacy-policy.html" style={{ color: '#8e44ad' }}>Privacy Policy</Link>.
                    </div>
                </div>
            </div>

            {/* 
          IMPORTANT: For the login button to actually work, we need to load the legacy auth script.
          However, mixing React with legacy DOM manipulation scripts is brittle.
          For this migration step "Root Pages", simply rendering the UI is the success criteria.
          The functional auth requires implementing `firebase` npm package logic here.
      */}
            <script type="module" src="/assets/js/auth.js" async></script>
        </div>
    );
}
