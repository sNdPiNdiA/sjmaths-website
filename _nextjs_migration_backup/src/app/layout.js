import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

export const metadata = {
  title: "SJMaths | AI-Powered Maths Learning, NCERT Notes & PYQs",
  description: "Master Mathematics with SJMaths. Get Free NCERT Solutions, Notes, PYQs & Live Classes for Class 9–12.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        {/* Google Fonts */}
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true" />
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet" />

        {/* Font Awesome */}
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />

        {/* Legacy Global Styles */}
        <link rel="stylesheet" href="/assets/css/main.min.css" />
        <link rel="stylesheet" href="/assets/css/layout.min.css" />
        <link rel="stylesheet" href="/assets/css/component.min.css" />
        <link rel="stylesheet" href="/assets/css/improved-ui.min.css" />
        <link rel="stylesheet" href="/assets/css/hero.min.css" />
        <link rel="stylesheet" href="/assets/css/ai-button.min.css" />
      </head>
      <body>
        <Header />

        {/* Main Content Wrapper usually expected by legacy CSS */}
        {children}

        <Footer />

        {/* Legacy Scripts */}
        <script src="/assets/js/main.min.js" defer></script>
      </body>
    </html>
  );
}
