import Link from 'next/link';
import { notFound } from 'next/navigation';

// Mock data loader - in real app this could be a utility function
async function getChapterData(classId, chapterId) {
    try {
        // In strict Next.js, dynamic imports for JSON need to be absolute or careful with paths
        // For this migration, we'll map class names to files manually or use a switch
        // This is a POC for Class 11 Sets
        if (classId === 'class-11' && chapterId === 'chapter-1-sets') {
            const data = await import('@/data/class-11/sets.json');
            return data.default || data;
        }
    } catch (e) {
        return null;
    }
    return null;
}

// 1. generateStaticParams: Pre-builds these paths at build time (SSG)
export async function generateStaticParams() {
    return [
        { classId: 'class-11', chapterId: 'chapter-1-sets', level: 'basic' },
        { classId: 'class-11', chapterId: 'chapter-1-sets', level: 'standard' },
        { classId: 'class-11', chapterId: 'chapter-1-sets', level: 'hots' },
    ];
}

// 2. generateMetadata: Dynamic SEO tags
export async function generateMetadata({ params }) {
    const { classId, chapterId, level } = await params;
    const data = await getChapterData(classId, chapterId);

    if (!data || !data.levels[level]) {
        return {
            title: 'Worksheet Not Found | SJMaths',
        };
    }

    const levelData = data.levels[level];
    const className = classId.replace('-', ' ').toUpperCase(); // CLASS 11

    return {
        title: `${levelData.title} - ${data.chapterName} | ${className} | SJMaths`,
        description: levelData.description,
        openGraph: {
            title: `${levelData.title} - ${data.chapterName}`,
            description: levelData.description,
        }
    };
}

// 3. Page Component
export default async function WorksheetPage({ params }) {
    const { classId, chapterId, level } = await params;
    const data = await getChapterData(classId, chapterId);

    if (!data || !data.levels[level]) {
        notFound();
    }

    const levelData = data.levels[level];

    return (
        <div className="container" style={{ maxWidth: '800px', margin: '120px auto 40px', padding: '0 20px' }}>

            {/* Breadcrumb / Header */}
            <div style={{ marginBottom: '2rem' }}>
                <Link href={`/classes/${classId}`} style={{ color: '#8e44ad', fontWeight: '600' }}>
                    &larr; Back to {classId.replace('-', ' ')}
                </Link>
                <h1 style={{ fontSize: '2.5rem', marginTop: '1rem', marginBottom: '0.5rem', color: '#2c3e50' }}>
                    {levelData.title}
                </h1>
                <p style={{ fontSize: '1.2rem', color: '#7f8c8d' }}>
                    {data.chapterName} &bull; {classId.replace('-', ' ').toUpperCase()}
                </p>
                <p style={{ marginTop: '1rem', color: '#555', lineHeight: '1.6' }}>
                    {levelData.description}
                </p>
            </div>

            {/* Questions List */}
            <div className="worksheet-paper" style={{
                background: 'white',
                padding: '40px',
                boxShadow: '0 4px 20px rgba(0,0,0,0.05)',
                borderRadius: '12px',
                border: '1px solid #eee'
            }}>
                {levelData.questions.map((q, index) => (
                    <div key={q.id} className="question-item" style={{ marginBottom: '25px', display: 'flex', gap: '15px' }}>
                        <span style={{
                            fontWeight: 'bold',
                            color: '#8e44ad',
                            minWidth: '30px'
                        }}>Q{index + 1}.</span>
                        <div style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#34495e' }}>
                            {q.text}
                        </div>
                    </div>
                ))}
            </div>

            {/* Action Buttons */}
            <div style={{ marginTop: '3rem', textAlign: 'center', display: 'flex', gap: '1rem', justifyContent: 'center' }}>
                {/* Simplified navigation between levels */}
                {level !== 'basic' && (
                    <Link href={`/classes/${classId}/worksheets/${chapterId}/basic`} className="btn-secondary"
                        style={{ padding: '10px 20px', borderRadius: '50px', background: '#f8f9fa', textDecoration: 'none', color: '#333' }}>
                        Basic
                    </Link>
                )}
                {level !== 'standard' && (
                    <Link href={`/classes/${classId}/worksheets/${chapterId}/standard`} className="btn-secondary"
                        style={{ padding: '10px 20px', borderRadius: '50px', background: '#f8f9fa', textDecoration: 'none', color: '#333' }}>
                        Standard
                    </Link>
                )}
                {level !== 'hots' && (
                    <Link href={`/classes/${classId}/worksheets/${chapterId}/hots`} className="btn-secondary"
                        style={{ padding: '10px 20px', borderRadius: '50px', background: '#f8f9fa', textDecoration: 'none', color: '#333' }}>
                        HOTS
                    </Link>
                )}
            </div>

        </div>
    );
}
