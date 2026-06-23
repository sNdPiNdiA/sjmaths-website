const http = require('http');
http.get('http://localhost:8085/assets/css/current-affairs.min.css', function (res) {
    let data = '';
    res.on('data', function (chunk) { data += chunk; });
    res.on('end', function () {
        console.log('body.dark-mode with --text-dark:', data.includes('body.dark-mode {\n    --text-dark'));
        console.log('.ca-card-title color #fff:', data.includes('color: #fff'));
        console.log('.ca-card-desc color #2d3748:', data.includes('color: #2d3748'));
        console.log('.ca-card-desc dark #e2e8f0:', data.includes('color: #e2e8f0'));
        console.log('correct option #1a7a3a:', data.includes('color: #1a7a3a'));
        console.log('wrong option #b5201a:', data.includes('color: #b5201a'));
        console.log('Light card-desc #2d3748:', data.includes('color: #2d3748'));
        console.log('Total CSS size:', data.length, 'bytes');
    });
});