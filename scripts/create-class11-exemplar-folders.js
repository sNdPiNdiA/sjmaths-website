const fs = require('fs');
const path = require('path');

// Target directory: classes/class-11/ncert-exemplar-practice
const targetDir = path.join(__dirname, '..', 'classes', 'class-11', 'ncert-exemplar-practice');

// Structure extracted from index.html
const chapters = [
    { name: 'chapter-1-sets', files: ['exemplar-1-1.html', 'exemplar-1-2.html', 'exemplar-1-3.html'] },
    { name: 'chapter-2-relations-and-functions', files: ['exemplar-2-1.html', 'exemplar-2-2.html', 'exemplar-2-3.html'] },
    { name: 'chapter-3-trigonometric-functions', files: ['exemplar-3-1.html', 'exemplar-3-2.html', 'exemplar-3-3.html'] },
    { name: 'chapter-4-complex-numbers', files: ['exemplar-4-1.html', 'exemplar-4-2.html', 'exemplar-4-3.html'] },
    { name: 'chapter-5-linear-inequalities', files: ['exemplar-5-1.html', 'exemplar-5-2.html', 'exemplar-5-3.html'] },
    { name: 'chapter-6-permutations', files: ['exemplar-6-1.html', 'exemplar-6-2.html', 'exemplar-6-3.html'] },
    { name: 'chapter-7-binomial-theorem', files: ['exemplar-7-1.html', 'exemplar-7-2.html', 'exemplar-7-3.html'] },
    { name: 'chapter-8-sequences-and-series', files: ['exemplar-8-1.html', 'exemplar-8-2.html', 'exemplar-8-3.html'] },
    { name: 'chapter-9-straight-lines', files: ['exemplar-9-1.html', 'exemplar-9-2.html', 'exemplar-9-3.html'] },
    { name: 'chapter-10-conic-sections', files: ['exemplar-10-1.html', 'exemplar-10-2.html', 'exemplar-10-3.html'] },
    { name: 'chapter-11-3d-geometry', files: ['exemplar-11-1.html', 'exemplar-11-2.html', 'exemplar-11-3.html'] },
    { name: 'chapter-12-limits-derivatives', files: ['exemplar-12-1.html', 'exemplar-12-2.html', 'exemplar-12-3.html'] },
    { name: 'chapter-13-statistics', files: ['exemplar-13-1.html', 'exemplar-13-2.html', 'exemplar-13-3.html'] },
    { name: 'chapter-14-probability', files: ['exemplar-14-1.html', 'exemplar-14-2.html', 'exemplar-14-3.html'] }
];

// Basic HTML Template for the exercise files
const getHtmlContent = (title, chapterName, jsonFileName) => `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} - ${chapterName} | SJMaths</title>
    <meta name="description" content="NCERT Exemplar Solutions for Class 11 Maths ${chapterName} - ${title}">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { font-family: 'Poppins', sans-serif; padding: 2rem; text-align: center; background: #fdfbfd; color: #1a1a2e; }
        h1 { color: #8e44ad; margin-bottom: 1rem; }
        a { color: #e74c3c; text-decoration: none; font-weight: 600; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>${chapterName} - ${title}</h1>
    <div id="questions-container">Loading questions...</div>
    <br>
    <a href="../index.html"><i class="fas fa-arrow-left"></i> Back to Chapter Index</a>

    <script>
        // Simple script to fetch and render questions
        async function loadQuestions() {
            try {
                const response = await fetch('./${jsonFileName}');
                const data = await response.json();
                const container = document.getElementById('questions-container');
                
                // TODO: Implement your rendering logic here
                // For now, just showing we found the data
                container.innerHTML = '<p>Found ' + data.sections[0].questions.length + ' questions.</p>'; 
            } catch (error) {
                console.error('Error loading questions:', error);
                document.getElementById('questions-container').innerText = 'Error loading questions.';
            }
        }
        loadQuestions();
    </script>
</body>
</html>`;

if (!fs.existsSync(targetDir)) {
    console.log(`Target directory not found: ${targetDir}`);
    process.exit(1);
}

console.log(`Creating folders in: ${targetDir}`);

chapters.forEach(chap => {
    const dirPath = path.join(targetDir, chap.name);
    
    if (!fs.existsSync(dirPath)) {
        fs.mkdirSync(dirPath, { recursive: true });
        console.log(`✅ Created folder: ${chap.name}`);
    } else {
        console.log(`ℹ️  Folder exists: ${chap.name}`);
    }

    chap.files.forEach(file => {
        const filePath = path.join(dirPath, file);
        if (!fs.existsSync(filePath)) {
            const title = file.replace('.html', '').replace(/-/g, ' ').toUpperCase();
            const chapterTitle = chap.name.replace(/chapter-\d+-/, '').replace(/-/g, ' ').toUpperCase();
            fs.writeFileSync(filePath, getHtmlContent(title, chapterTitle, file.replace('.html', '.json')));
            console.log(`   📄 Created file: ${file}`);
        }
    });
});

console.log('🎉 Class 11 Exemplar structure setup complete!');