const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');

const bPath = path.join(ROOT_DIR, 'class-9-maths', 'worksheets', 'chapter-5-introduction-to-euclids-geometry', 'basic.html');
const sPath = path.join(ROOT_DIR, 'class-9-maths', 'worksheets', 'chapter-5-introduction-to-euclids-geometry', 'standard.html');

const bHead = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 9 Introduction to Euclid's Geometry Basic Worksheet | SJMaths</title>
    <meta name="description" content="Practice Class 9 Euclid’s Geometry Basic Level Worksheet with key definitions, postulates, and solution key on SJMaths.">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="https://sjmaths.com/class-9-maths/worksheets/chapter-5-introduction-to-euclids-geometry/basic.html">
`;

const sHead = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 9 Introduction to Euclid's Geometry Standard Worksheet | SJMaths</title>
    <meta name="description" content="Practice Class 9 Euclid’s Geometry Standard Level Worksheet with practice problems, postulates, and step-by-step answers on SJMaths.">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="https://sjmaths.com/class-9-maths/worksheets/chapter-5-introduction-to-euclids-geometry/standard.html">
`;

let bContent = fs.readFileSync(bPath, 'utf8');
if (!bContent.includes('<html lang="en">')) {
  bContent = bHead + bContent.substring(bContent.indexOf('<link'));
  fs.writeFileSync(bPath, bContent, 'utf8');
}

let sContent = fs.readFileSync(sPath, 'utf8');
if (!sContent.includes('<html lang="en">')) {
  sContent = sHead + sContent.substring(sContent.indexOf('<link'));
  fs.writeFileSync(sPath, sContent, 'utf8');
}

console.log('🎉 Restored clean head tags for basic and standard Euclid worksheets.');
