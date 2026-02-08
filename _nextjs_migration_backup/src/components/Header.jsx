import Link from 'next/link';

export default function Header() {
    return (
        <div id="header-container">
            <header className="glass-header">
                <div className="header-container">
                    {/* Left: Logo */}
                    <div className="header-left">
                        <Link href="/" className="logo">
                            <span className="logo-symbol">&int;</span> SJMaths
                        </Link>
                    </div>

                    {/* Center: Search (Desktop) / Right (Mobile) */}
                    <div className="header-center">
                        <div className="header-search">
                            <label htmlFor="site-search" className="sr-only">Search</label>
                            <button type="button" aria-label="Search">
                                <i className="fas fa-search search-icon"></i>
                            </button>
                            <input type="text" id="site-search" placeholder="Search topics..." />
                        </div>
                    </div>

                    {/* Right: Actions */}
                    <div className="header-right">
                        <nav className="desktop-nav">
                            <ul>
                                <li><Link href="/">Home</Link></li>
                                <li><Link href="/classes/class-9">Class 9</Link></li>
                                <li><Link href="/classes/class-10">Class 10</Link></li>
                                <li><Link href="/classes/class-11">Class 11</Link></li>
                                <li><Link href="/classes/class-12">Class 12</Link></li>
                            </ul>
                        </nav>

                        <Link href="/login" className="auth-btn-pill" id="authBtn">Login</Link>
                        <div className="mobile-toggle"><i className="fas fa-bars"></i></div>
                    </div>
                </div>
            </header>
        </div>
    );
}
