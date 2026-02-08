import fs from 'fs';
import path from 'path';
import * as cheerio from 'cheerio';
import { notFound } from 'next/navigation';
import Link from 'next/link';

// Helper to read and parse legacy HTML
async function getLegacyPageContent(slug) {
    // Construct path: src/content/pages/terms.html
    const contentBase = path.join(process.cwd(), 'src', 'content', 'pages');
    const filePath = path.join(contentBase, `${slug}.html`);

    if (!fs.existsSync(filePath)) {
        return null;
    }

    const html = fs.readFileSync(filePath, 'utf-8');
    const $ = cheerio.load(html);

    // Extract Metadata
    const title = $('title').text() || `${slug.replace(/-/g, ' ')} | SJMaths`;
    const description = $('meta[name="description"]').attr('content') || '';

    // Extract Main Content
    // Legacy pages usually have <main> or .content-wrapper
    let contentHtml = $('main').html() ||
        $('.content-wrapper').html() ||
        $('.page-content').html() ||
        $('body').html();

    if (contentHtml) {
        // Sanitize Paths
        contentHtml = contentHtml.replace(/src="(?:\.\.\/)+assets\//g, 'src="/assets/');
        contentHtml = contentHtml.replace(/href="(?:\.\.\/)+assets\//g, 'href="/assets/');
        contentHtml = contentHtml.replace(/href="(?:\.\.\/)+index\.html"/g, 'href="/"');

        // Fix Links to other pages: /pages/about.html -> /about
        // But generic pages link to /pages/terms.html -> /pages/terms
        contentHtml = contentHtml.replace(/href="(?:\.\.\/)?pages\/([\w-]+)\.html"/g, 'href="/pages/$1"');
    }

    return {
        title,
        description,
        contentHtml
    };
}

export async function generateMetadata({ params }) {
    const { slug } = await params;
    const data = await getLegacyPageContent(slug);

    if (!data) return { title: 'Page Not Found' };

    return {
        title: data.title,
        description: data.description,
    };
}

export default async function LegacyGenericPage({ params }) {
    const { slug } = await params;
    const data = await getLegacyPageContent(slug);

    if (!data) notFound();

    return (
        <div className="legacy-page-wrapper">
            <div className="container" style={{ maxWidth: '900px', margin: '4rem auto', padding: '0 20px' }}>
                <div dangerouslySetInnerHTML={{ __html: data.contentHtml }} />
            </div>

            {/* Legacy Styles if needed */}
            <link rel="stylesheet" href="/assets/css/pages.min.css" />
        </div>
    );
}
