import LegacyResourcePage, { generateMetadata as baseMetadata } from './[...slug]/page';

// Reuse the logic from the catch-all page, but with empty slug.
// This handles /classes/class-9/chapter-wise-notes

export async function generateMetadata({ params }) {
    // Pass empty slug array explicitly
    return baseMetadata({ params: { ...params, slug: [] } });
}

export default async function ResourceTypeIndexPage({ params }) {
    // Pass empty slug array explicitly
    return LegacyResourcePage({ params: { ...params, slug: [] } });
}
