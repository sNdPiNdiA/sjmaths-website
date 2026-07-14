const fs = require('fs');

// Fix 1
let file1 = 'class-9-maths/chapter-mastery/chapter-1-use-of-coordinates/concepts/introduction.html';
if (fs.existsSync(file1)) {
    let content = fs.readFileSync(file1, 'utf8');
    content = content.replace('src="../../../../../assets/js/main.min.js"', 'src="/assets/js/main.min.js"');
    fs.writeFileSync(file1, content);
}

// Fix 2
let file2 = 'class-9-maths/chapter-mastery/chapter-1-use-of-coordinates/index.html';
if (fs.existsSync(file2)) {
    let content = fs.readFileSync(file2, 'utf8');
    content = content.replace('src="../../assets/js/main.min.js"', 'src="/assets/js/main.min.js"');
    fs.writeFileSync(file2, content);
}

// Fix 3 & 4
let file3 = 'class-9-maths/chapter-mastery/index.html';
if (fs.existsSync(file3)) {
    let content = fs.readFileSync(file3, 'utf8');
    content = content.replace('src=" /assets/js/global-header.min.js"', 'src="/assets/js/global-header.min.js"');
    content = content.replace('src=" /assets/js/global-footer.min.js"', 'src="/assets/js/global-footer.min.js"');
    fs.writeFileSync(file3, content);
}

// Fix 5
let file5 = 'scratch/test_hindi.html';
if (fs.existsSync(file5)) {
    let content = fs.readFileSync(file5, 'utf8');
    content = content.replace('href="../../index.html"', 'href="../index.html"');
    fs.writeFileSync(file5, content);
}

console.log("Fixed final 5 manual 404s!");
