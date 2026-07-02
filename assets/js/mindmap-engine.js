(function (win) {
    'use strict';

    /* ═══════════════════════════════════════════════════════════════
       MINDMAP RENDERING ENGINE (LEFT-TO-RIGHT HIERARCHY)
       Usage:  renderMindmap( treeData, containerId, englishOrHindi )
       - treeData : tree object
       - containerId : DOM element id (default 'prehistory-mindmap-container')
       - enOrHi : 'en' or 'hi' (default 'en')
       ═══════════════════════════════════════════════════════════════ */

    var DEVFONT = "'Noto Sans Devanagari','Inter',system-ui,sans-serif";

    /* ── DEFAULT LAYOUT CONFIG (L-to-R) ────────────────────────── */
    var CFG = {
        root: { w: 160, h: 50, fs: 14 },
        branch: { w: 160, h: 54, fs: 12 },
        sub: { w: 170, h: 54, fs: 12 },
        leaf: { w: 250, h: 58, fs: 11.5 },
        gapX: 70, // Horizontal space between columns
        gapY: 18, // Vertical space between sibling nodes
        pad: 22,
        tr: 9
    };
    var CFG_HI = {
        root: { w: 170, h: 52, fs: 13.5 },
        branch: { w: 170, h: 56, fs: 11.5 },
        sub: { w: 180, h: 56, fs: 11.5 },
        leaf: { w: 260, h: 60, fs: 11.5 },
        gapX: 70,
        gapY: 18,
        pad: 22,
        tr: 9
    };

    /* ── STATE ──────────────────────────────────────────────────── */
    var expanded = new Set();
    var seq = 0;
    var _treeRef = null;  /* root tree reference for re-rendering after toggle */
    function stamp(n, p) { n._id = seq++; n._parent = p; (n.children || []).forEach(function (c) { stamp(c, n) }); }

    /* ── MEASURE ────────────────────────────────────────────────── */
    function cfg(n) { return n._cfg || n._config[n.type] || n._config.leaf; }
    function nW(n) { return cfg(n).w; }
    function nH(n) {
        var baseH = cfg(n).h;
        var lines = (n.label || '').split('\n').length;
        if (lines > 2) {
            return baseH + (lines - 2) * 15;
        }
        return baseH;
    }

    function subtreeH(node) {
        var config = node._config;
        var open = (node.type === 'root') || expanded.has(node._id);
        if (!open || !node.children || !node.children.length) return nH(node);
        
        var kidsH = node.children.reduce(function (s, c) { return s + subtreeH(c); }, 0)
            + config.gapY * (node.children.length - 1);
            
        return Math.max(nH(node), kidsH);
    }

    function subtreeW(node) {
        var config = node._config;
        var open = (node.type === 'root') || expanded.has(node._id);
        if (!open || !node.children || !node.children.length) return nW(node);
        
        var maxKidW = Math.max.apply(null, node.children.map(function (c) { return subtreeW(c); }));
        return nW(node) + config.gapX + maxKidW;
    }

    /* ── ACCORDION ──────────────────────────────────────────────── */
    function collapseTree(node) {
        expanded.delete(node._id);
        (node.children || []).forEach(function (c) { collapseTree(c); });
    }
    function doToggle(node) {
        if (node.type === 'root') return;
        var wasExpanded = expanded.has(node._id);
        if (wasExpanded) {
            collapseTree(node);
        } else {
            if (node._parent) {
                node._parent.children.forEach(function (sib) {
                    if (sib._id !== node._id) collapseTree(sib);
                });
            }
            expanded.add(node._id);
        }
        if (_treeRef) {
            renderTree(_treeRef);
            
            // Smooth scroll to the newly expanded column
            if (!wasExpanded && node.children && node.children.length) {
                setTimeout(function () {
                    var host = document.getElementById('prehistory-mindmap-container');
                    if (host && node._leftX !== undefined) {
                        host.scrollTo({
                            left: node._leftX - 24, // Show parent node at the left margin
                            behavior: 'smooth'
                        });
                    }
                }, 100);
            }
        }
    }

    /* ── SVG HELPERS ────────────────────────────────────────────── */
    var NS = 'http://www.w3.org/2000/svg';
    function el(tag, attrs, txt) {
        var e = document.createElementNS(NS, tag);
        Object.keys(attrs).forEach(function (k) { e.setAttribute(k, attrs[k]); });
        if (txt !== undefined) e.textContent = txt;
        return e;
    }

    /* ── RENDER ─────────────────────────────────────────────────── */
    function renderTree(tree) {
        var host = document.getElementById('prehistory-mindmap-container');
        if (!host) return;
        host.innerHTML = '';
        var config = tree._config;
        var svgW = subtreeW(tree) + config.pad * 2;
        var svgH = subtreeH(tree) + config.pad * 2;
        var svg = el('svg', {
            id: 'prehistory-mindmap-svg',
            viewBox: '0 0 ' + svgW + ' ' + svgH,
            xmlns: NS, width: svgW, height: svgH,
            style: 'display:inline-block;vertical-align:top;'
        });
        var lG = el('g', { id: 'mm-links' });
        var nG = el('g', { id: 'mm-nodes' });
        svg.appendChild(lG);
        svg.appendChild(nG);
        drawNode(lG, nG, tree, config.pad, svgH / 2);
        host.appendChild(svg);

        // Append scroll hint for mobile/desktop if content overflows
        var hint = document.createElement('div');
        hint.className = 'mindmap-scroll-hint';
        if (tree._lang === 'hi') {
            hint.innerHTML = '<i class="fas fa-right-left" style="margin-right:6px;"></i><span>पूरा माइंडमैप देखने के लिए स्क्रॉल करें</span>';
        } else {
            hint.innerHTML = '<i class="fas fa-right-left" style="margin-right:6px;"></i><span>Scroll or drag horizontally to view full mindmap</span>';
        }
        host.appendChild(hint);

        // Drag to scroll on desktop
        var isDown = false;
        var startX, startY;
        var scrollLeft;
        var hasMoved = false;

        host.addEventListener('mousedown', function (e) {
            if (e.button !== 0) return;
            if (e.target.closest && e.target.closest('.mm-toggle')) return;
            
            isDown = true;
            hasMoved = false;
            host.classList.add('active');
            startX = e.pageX - host.offsetLeft;
            startY = e.pageY - host.offsetTop;
            scrollLeft = host.scrollLeft;
        });
        host.addEventListener('mouseleave', function () {
            isDown = false;
            host.classList.remove('active');
        });
        host.addEventListener('mouseup', function (e) {
            isDown = false;
            host.classList.remove('active');
            if (hasMoved) {
                e.preventDefault();
            }
        });
        host.addEventListener('mousemove', function (e) {
            if (!isDown) return;
            var x = e.pageX - host.offsetLeft;
            var y = e.pageY - host.offsetTop;
            var walkX = x - startX;
            var walkY = y - startY;

            if (Math.abs(walkX) > 6 || Math.abs(walkY) > 6) {
                hasMoved = true;
                e.preventDefault();
                host.scrollLeft = scrollLeft - walkX * 1.5;
            }
        });

        // Dynamic overflow checking
        function checkOverflow() {
            if (host.scrollWidth > host.clientWidth) {
                hint.style.setProperty('display', 'flex', 'important');
            } else {
                hint.style.setProperty('display', 'none', 'important');
            }
        }
        setTimeout(checkOverflow, 150);
        window.addEventListener('resize', checkOverflow);
    }

    /* ── DRAW NODE ──────────────────────────────────────────────── */
    function drawNode(lG, nG, node, leftX, cy) {
        node._leftX = leftX; // Store coordinates on node for scrolling lookup
        var config = node._config;
        var w = nW(node), h = nH(node), fc = cfg(node);
        var y = cy - h / 2;
        var isRoot = (node.type === 'root');
        var hasDate = (node.type === 'branch' || node.type === 'sub') && !!node.date;
        var isGreen = (node.type === 'sub' || node.type === 'leaf');
        var fontStack = node._font || "'Inter',system-ui,sans-serif";

        var g = el('g', { 'class': 'mm-g mm-' + node.type });
        g.appendChild(el('rect', { x: leftX, y: y, width: w, height: h, rx: 8, ry: 8, 'class': 'mm-rect' }));

        var lines = node.label.split('\n');
        var mainFs = fc.fs, mainLh = mainFs * 1.42;
        var dateFs = 9.5, dateLh = dateFs * 1.28;
        var totalH = lines.length * mainLh + (hasDate ? dateLh : 0);
        var blockTop = cy - totalH / 2 + mainLh / 2;
        var cx = leftX + w / 2;

        lines.forEach(function (line, i) {
            g.appendChild(el('text', {
                x: cx, y: blockTop + i * mainLh,
                'text-anchor': 'middle', 'dominant-baseline': 'central',
                'font-size': mainFs, 'font-family': fontStack
            }, line));
        });

        if (hasDate) {
            g.appendChild(el('text', {
                x: cx, y: blockTop + lines.length * mainLh,
                'text-anchor': 'middle', 'dominant-baseline': 'central',
                'font-size': dateFs, 'font-family': "'Inter',system-ui,sans-serif",
                'class': 'mm-date'
            }, node.date));
        }
        
        // Make the entire card clickable if it has children and is not root
        if (!isRoot && node.children && node.children.length) {
            g.addEventListener('click', function (e) {
                e.stopPropagation();
                doToggle(node);
            });
        }
        
        nG.appendChild(g);

        if (!node.children || !node.children.length) return;
        var isOpen = isRoot || expanded.has(node._id);

        if (!isRoot) {
            var tx = leftX + w + 7 + config.tr;
            var ty = cy;
            var tog = el('g', { 'class': 'mm-toggle' + (isGreen ? ' green' : '') });
            tog.appendChild(el('circle', { cx: tx, cy: ty, r: config.tr }));
            tog.appendChild(el('text', {
                x: tx, y: ty, 'font-size': 14, 'font-family': "'Inter',sans-serif",
                'text-anchor': 'middle', 'dominant-baseline': 'central'
            }, isOpen ? '\u2212' : '+'));
            tog.addEventListener('click', function (e) { e.stopPropagation(); doToggle(node); });
            nG.appendChild(tog);
        }
        if (!isOpen) return;

        var childLeftX = leftX + w + config.gapX;
        var kidsH = node.children.reduce(function (s, c) { return s + subtreeH(c); }, 0)
            + config.gapY * (node.children.length - 1);
        var childY = cy - kidsH / 2;
        var linkX = isRoot ? (leftX + w) : (leftX + w + 7 + config.tr * 2 + 5);

        node.children.forEach(function (child) {
            var ch = subtreeH(child), childCY = childY + ch / 2;
            var x1 = linkX, x2 = childLeftX, mcx = (x1 + x2) / 2;
            lG.appendChild(el('path', {
                d: 'M ' + x1 + ' ' + cy + ' C ' + mcx + ' ' + cy + ', ' + mcx + ' ' + childCY + ', ' + x2 + ' ' + childCY,
                'class': 'mm-link' + (isGreen ? ' green' : '')
            }));
            drawNode(lG, nG, child, childLeftX, childCY);
            childY += ch + config.gapY;
        });
    }

    /* ── PUBLIC API ─────────────────────────────────────────────── */
    win.renderMindmap = function (treeData, containerId, language) {
        language = language || 'en';
        seq = 0;
        expanded = new Set();

        var config = (language === 'hi') ? CFG_HI : CFG;
        var font = (language === 'hi') ? DEVFONT : "'Inter',system-ui,sans-serif";

        function wrapText(text, maxChars) {
            if (!text) return '';
            if (text.indexOf('\n') !== -1) return text;
            var words = text.split(' ');
            var lines = [];
            var currentLine = '';
            words.forEach(function (word) {
                if ((currentLine + ' ' + word).trim().length <= maxChars) {
                    currentLine = (currentLine + ' ' + word).trim();
                } else {
                    if (currentLine) lines.push(currentLine);
                    currentLine = word;
                }
            });
            if (currentLine) lines.push(currentLine);
            return lines.join('\n');
        }

        /* Deep-clone and attach config/font/parent refs/language */
        function cloneAndAttach(n, p) {
            var c = JSON.parse(JSON.stringify(n));
            c._config = config;
            c._font = font;
            c._lang = language;
            c._id = seq++;
            c._parent = p;

            var maxChars = 28;
            if (c.type === 'root') maxChars = 18;
            else if (c.type === 'branch') maxChars = 22;
            else if (c.type === 'sub') maxChars = 24;
            c.label = wrapText(c.label, maxChars);

            if (c.children) c.children = c.children.map(function (ch) { return cloneAndAttach(ch, c); });
            return c;
        }
        var tree = cloneAndAttach(treeData, null);
        _treeRef = tree;
        expanded.add(tree._id);

        /* Override container if provided */
        if (containerId) {
            var oldHost = document.getElementById('prehistory-mindmap-container');
            if (oldHost) oldHost.id = 'prehistory-mindmap-container-old';
            var newHost = document.getElementById(containerId);
            if (newHost) newHost.id = 'prehistory-mindmap-container';
        }

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function () { renderTree(tree); });
        } else {
            renderTree(tree);
        }
    };

})(window);