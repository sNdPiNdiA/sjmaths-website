const path = require('node:path');
// Resolve from this module, not the caller's working directory.
const BASE = path.resolve(__dirname, '../../upsc-aso');
const asoFile = (...parts) => path.join(BASE, ...parts);
module.exports = { BASE, asoFile };
