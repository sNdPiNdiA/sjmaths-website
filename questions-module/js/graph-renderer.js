/* =========================================================
   SJMaths – Graph Renderer
   Handles rendering of trigonometric curves based on JSON data
========================================================= */

(async function () {
    const graphLibTag = document.getElementById('graphLibrary');
    let graphData = {};

    // 1. Define Render Function
    window.renderGraphs = function () {
        const containers = document.querySelectorAll('.graph-container[data-ref]');
        
        containers.forEach(container => {
            if (container.hasAttribute('data-rendered')) return;
            
            const ref = container.getAttribute('data-ref');
            
            if (ref && graphData[ref]) {
                container.innerHTML = `
                    <div class="graph-wrapper" style="text-align:center; margin: 1rem 0;">
                        ${graphData[ref].svg}
                        <div class="graph-caption" style="font-size:0.85rem; color:#666; margin-top:0.5rem;">${graphData[ref].title}</div>
                    </div>
                `;
                container.setAttribute('data-rendered', 'true');
            }
        });
    };

    // 2. Observe DOM for new questions (Setup immediately)
    const qContainer = document.getElementById('questionContainer');
    if (qContainer) {
        const observer = new MutationObserver(window.renderGraphs);
        observer.observe(qContainer, { childList: true, subtree: true });
    }

    // 3. Load Graph Data
    if (graphLibTag && graphLibTag.src) {
        try {
            const res = await fetch(graphLibTag.src);
            if (res.ok) {
                graphData = await res.json();
                // Trigger render in case questions were loaded while we were fetching data
                window.renderGraphs();
            } else {
                console.warn("Graph Library not found:", res.status);
            }
        } catch (e) {
            console.error("Failed to load graph library", e);
        }
    }
})();