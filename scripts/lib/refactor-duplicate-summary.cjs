// Reporting only: repeated bytes do not establish that content can be removed.
function summarizeDuplicateBlocks(map) {
  const groups = [...map.values()].filter(group => group.occurrences > 1).map(group => ({
    ...group,
    uniquePages: group.files.length,
    withinPageRepeats: group.occurrences - group.files.length,
    crossPageRepeats: Math.max(0, group.files.length - 1),
  }));
  groups.sort((a, b) => (b.occurrences - 1) * b.bytes - (a.occurrences - 1) * a.bytes);
  return {
    extraBytes: groups.reduce((sum, group) => sum + (group.occurrences - 1) * group.bytes, 0),
    withinPageRepeatedBytes: groups.reduce((sum, group) => sum + group.withinPageRepeats * group.bytes, 0),
    crossPageRepeatedBytes: groups.reduce((sum, group) => sum + group.crossPageRepeats * group.bytes, 0),
    withinPageGroups: groups.filter(group => group.withinPageRepeats > 0).length,
    crossPageGroups: groups.filter(group => group.crossPageRepeats > 0).length,
    groups,
  };
}
module.exports = { summarizeDuplicateBlocks };
