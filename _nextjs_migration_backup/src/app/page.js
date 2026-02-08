import Hero from '@/components/Hero';
import ClassGrid from '@/components/ClassGrid';
import Features from '@/components/Features';

// Note: The legacy site has <script> tags for main.min.js that handle animations.
// With Next.js, we should verify if those scripts run correctly on route changes.
// For now, they are included in layout.js, so they should work on initial load.

export default function Home() {
  return (
    <main>
      <Hero />
      <ClassGrid />
      <Features />
    </main>
  );
}
