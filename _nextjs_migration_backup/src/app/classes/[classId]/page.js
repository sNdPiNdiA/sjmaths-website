import Link from 'next/link';
import { notFound } from 'next/navigation';

// Mock data loader
async function getClassData(classId) {
    try {
        const data = await import('@/data/class-structure.json');
        return data.default[classId];
    } catch (e) {
        return null;
    }
}

// 1. generateStaticParams: Pre-builds these paths
export async function generateStaticParams() {
    return [
        { classId: 'class-9' },
        { classId: 'class-10' },
        { classId: 'class-11' },
        { classId: 'class-12' },
    ];
}

// 2. Metadata
export async function generateMetadata({ params }) {
    const { classId } = await params;
    const data = await getClassData(classId);

    if (!data) return { title: 'Class Not Found' };

    return {
        title: `${data.title} | SJMaths`,
        description: data.description,
    };
}

// 3. Page Component
export default async function ClassLandingPage({ params }) {
    const { classId } = await params;
    const data = await getClassData(classId);

    if (!data) notFound();

    return (
        <div className="class-landing-page">
            {/* Hero Section */}
            <section className="page-hero" style={{
                background: 'linear-gradient(135deg, #8e44ad, #9b59b6)',
                color: 'white',
                padding: '80px 20px',
                textAlign: 'center'
            }}>
                <div className="breadcrumbs" style={{ marginBottom: '15px', fontSize: '0.9rem', opacity: '0.9' }}>
                    <Link href="/" style={{ color: 'white', textDecoration: 'none' }}>Home</Link>
                    <span style={{ margin: '0 10px' }}>&rsaquo;</span>
                    <span>{classId.replace('-', ' ').replace(/\b\w/g, c => c.toUpperCase())}</span>
                </div>
                <h1 style={{ fontSize: '2.8rem', marginBottom: '1rem' }}>{data.title}</h1>
                <p style={{ fontSize: '1.2rem', maxWidth: '700px', margin: '0 auto', opacity: '0.95' }}>
                    {data.description}
                </p>
            </section>

            <main className="dashboard-grid" style={{
                maxWidth: '1200px',
                margin: '-40px auto 60px',
                padding: '0 20px',
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
                gap: '20px',
                position: 'relative',
                zIndex: 10
            }}>
                {data.features.map((feature, index) => (
                    <Link href={feature.link} key={index} className="feature-card" style={{
                        background: 'white',
                        padding: '30px',
                        borderRadius: '12px',
                        boxShadow: '0 10px 30px rgba(0,0,0,0.08)',
                        textDecoration: 'none',
                        transition: 'transform 0.3s ease',
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'flex-start'
                    }}>
                        <div className="f-icon" style={{
                            fontSize: '2rem',
                            color: '#8e44ad',
                            marginBottom: '1rem',
                            background: '#f3e5f5',
                            width: '60px',
                            height: '60px',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            borderRadius: '50%'
                        }}>
                            <i className={feature.icon}></i>
                        </div>
                        <h2 style={{ fontSize: '1.4rem', color: '#2c3e50', marginBottom: '0.5rem' }}>{feature.title}</h2>
                        <p style={{ color: '#7f8c8d', marginBottom: '1.5rem', lineHeight: '1.5' }}>{feature.description}</p>
                        <span className="feature-link" style={{
                            marginTop: 'auto',
                            color: '#8e44ad',
                            fontWeight: 600,
                            display: 'flex',
                            alignItems: 'center',
                            gap: '5px'
                        }}>
                            Explore <i className="fas fa-arrow-right"></i>
                        </span>
                    </Link>
                ))}
            </main>

            {/* FAQ Section */}
            <section style={{ maxWidth: '800px', margin: '40px auto', padding: '0 20px 80px' }}>
                <h2 style={{ textAlign: 'center', marginBottom: '30px', color: '#2c3e50' }}>Frequently Asked Questions</h2>
                {data.faq.map((item, i) => (
                    <div key={i} style={{ marginBottom: '20px', background: '#f8f9fa', padding: '20px', borderRadius: '8px' }}>
                        <h3 style={{ fontSize: '1.1rem', fontWeight: 600, marginBottom: '0.5rem', color: '#34495e' }}>{item.question}</h3>
                        <p style={{ color: '#555', margin: 0 }}>{item.answer}</p>
                    </div>
                ))}
            </section>
        </div>
    );
}
