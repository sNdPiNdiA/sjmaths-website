const fs = require('fs');
const path = require('path');

const CLASS11_DIR = path.join(__dirname, 'class-11-applied-mathematics');

const subdirsToDelete = [
    "1-1-binary-numbers/introduction-to-binary-number-system",
    "1-1-binary-numbers/conversion-of-decimal-numbers-to-binary-system-and-vice-versa-and-its-applications",
    "1-2-indices-logarithm-and-antilogarithm/indices-and-its-properties",
    "1-2-indices-logarithm-and-antilogarithm/common-and-natural-logarithm",
    "1-2-indices-logarithm-and-antilogarithm/laws-of-logarithms",
    "1-2-indices-logarithm-and-antilogarithm/logarithm-and-exponential-as-inverse-operations",
    "1-2-indices-logarithm-and-antilogarithm/procedure-of-finding-logarithm-and-antilogarithms-of-given-number",
    "1-2-indices-logarithm-and-antilogarithm/applications-of-logarithms",
    "1-3-introduction-to-bhartiya-system-of-numeration/introduction-to-bhartiya-system-of-numeration",
    "1-4-clocks/evaluate-the-angular-value-of-a-minute",
    "1-4-clocks/measure-of-angle-formed-between-two-hands-of-clock-at-given-time",
    "1-4-clocks/calculation-of-the-time-for-which-hands-of-clock-meet",
    "1-5-calendar/odd-days-in-a-month-year-century",
    "1-5-calendar/decode-the-day-for-the-given-date",
    "1-6-time-and-work/relationship-between-work-and-time",
    "1-6-time-and-work/comparison-of-the-work-done-by-the-individual-group-wrt-time",
    "1-7-speed-distance-and-time/the-time-taken-distance-covered-from-the-given-data",
    "1-8-seating-arrangement/creation-of-seating-plan-draft-as-per-given-conditions-linearcircular",
    "1-8-seating-arrangement/locating-the-position-of-a-person-in-a-seating-arrangement"
];

console.log("Cleaning up old microtopic subdirectories...");

subdirsToDelete.forEach(dir => {
    const fullPath = path.join(CLASS11_DIR, dir);
    if (fs.existsSync(fullPath)) {
        fs.rmSync(fullPath, { recursive: true, force: true });
        console.log(`Deleted folder: ${dir}`);
    }
});

console.log("Cleanup complete!");
