import fs from 'fs';
import path from 'path';
import * as cheerio from 'cheerio';
import { notFound } from 'next/navigation';
import Link from 'next/link';

// Helper to read and parse legacy HTML
async function getLegacyContent(classId, resourceType, slugArray) {
    // Construct path: src/content/classes/class-9/chapter-wise-notes/chapter-1/index.html
    // slugArray is usually ['chapter-1-sets'] or similar.

    const contentBase = path.join(process.cwd(), 'src', 'content', 'classes');

    // Try mapping slug to a directory with index.html
    const directoryPath = path.join(contentBase, classId, resourceType, ...slugArray);
    const filePath = path.join(directoryPath, 'index.html');

    if (!fs.existsSync(filePath)) {
        return null;
    }

    const html = fs.readFileSync(filePath, 'utf-8');
    const $ = cheerio.load(html);

    // Extract Metadata
    const title = $('title').text() || `${slugArray.join(' ')} | SJMaths`;
    const description = $('meta[name="description"]').attr('content') || '';

    // 1. Extract Styles
    const headStyles = $('head style').map((i, el) => $(el).html()).get().join('\n');
    const headLinks = $('head link[rel="stylesheet"]').map((i, el) => {
        let href = $(el).attr('href');
        // Fix Link Href: ../../assets/ -> /assets/
        // Common pattern in legacy: ../../assets/css/main.min.css
        if (href && href.includes('assets/')) {
            href = '/assets/' + href.split('assets/')[1];
        }
        return `<link rel="stylesheet" href="${href}" />`;
    }).get().join('\n');

    // 2. Extract Scripts (Custom page-specific scripts often checking for interactive elements)
    const bodyScripts = $('body script').map((i, el) => {
        const src = $(el).attr('src');
        const content = $(el).html();
        if (src) {
            // Fix Script Src
            let newSrc = src;
            if (src.includes('assets/')) {
                newSrc = '/assets/' + src.split('assets/')[1];
            }
            // Avoid loading main layout scripts if possible, but keeping for compatibility
            return `<script src="${newSrc}"></script>`;
        }
        return `<script>${content}</script>`;
    }).get().join('\n');

    // 3. Extract Main Body Content
    let $content = $('.content-wrapper').length ? $('.content-wrapper') : $('body');

    // Manipulate content before extracting HTML
    $content.find('img').each((i, el) => {
        let src = $(el).attr('src');
        if (src && src.includes('assets/')) {
            $(el).attr('src', '/assets/' + src.split('assets/')[1]);
        }
    });

    $content.find('a').each((i, el) => {
        let href = $(el).attr('href');
        if (href) {
            // Fix Assets
            if (href.includes('assets/')) {
                $(el).attr('href', '/assets/' + href.split('assets/')[1]);
            }
            // Fix Home
            else if (href.includes('index.html') && (href.startsWith('../../') || href === '../index.html')) {
                if (href.endsWith('/index.html')) {
                    let clean = href.replace(/\.\.\//g, '').replace('index.html', '');
                    if (clean === '') clean = '/';
                    else if (!clean.startsWith('/')) clean = '/' + clean;
                    $(el).attr('href', clean);
                }
            }
        }
    });

    let contentHtml = $content.html();

    return {
        title,
        description,
        contentHtml,
        styles: headStyles,
        links: headLinks,
        scripts: bodyScripts
    };
}

export async function generateMetadata({ params }) {
    const { classId, resourceType, slug } = await params;
    const data = await getLegacyContent(classId, resourceType, slug);

    if (!data) return { title: 'Resource Not Found' };

    return {
        title: data.title,
        description: data.description,
    };
}

export default async function LegacyResourcePage({ params }) {
    const { classId, resourceType, slug } = await params;
    const data = await getLegacyContent(classId, resourceType, slug);

    if (!data) notFound();

    return (
        <div className="legacy-wrapper">
            {/* Inject Extracted Styles & Links */}
            <div dangerouslySetInnerHTML={{ __html: data.links }} />
            <style dangerouslySetInnerHTML={{ __html: data.styles }} />

            {/* Breadcrumb / Nav (Modern Wrapper) */}
            <div style={{ background: '#f8f9fa', padding: '1rem', borderBottom: '1px solid #eee' }}>
                <div className="container" style={{ maxWidth: '1200px', margin: '0 auto', fontSize: '0.9rem' }}>
                    <Link href={`/classes/${classId}`} style={{ color: '#8e44ad', textDecoration: 'none', fontWeight: '600' }}>
                        {classId.replace('-', ' ').toUpperCase()}
                    </Link>
                    <span style={{ margin: '0 10px', color: '#999' }}>/</span>
                    <span style={{ color: '#555', textTransform: 'capitalize' }}>{resourceType.replace(/-/g, ' ')}</span>
                </div>
            </div>

            {/* Legacy Content Injection */}
            <div
                className="legacy-content-container"
                dangerouslySetInnerHTML={{ __html: data.contentHtml }}
            />

            {/* Inject Scripts (Legacy interactions like Accordions/Slideshows) */}
            <div dangerouslySetInnerHTML={{ __html: data.scripts }} />

            {/* Fallback for global styles if extraction missed them */}
            <link rel="stylesheet" href="/assets/css/main.min.css" />
            <link rel="stylesheet" href="/assets/css/improved-ui.min.css" />

            {/* MathJax for specific pages */}
            <script src="https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js"></script>
            <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        </div>
    );
}
