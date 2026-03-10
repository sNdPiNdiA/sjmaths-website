(function () {
    const PDFJS_SCRIPT_CDN = "/assets/vendor/pdfjs/pdf.min.js";
    const PDFJS_CDN = "/assets/vendor/pdfjs/pdf.worker.min.js";

    function getPdfLib() {
        return window.pdfjsLib || window["pdfjs-dist/build/pdf"] || null;
    }

    function loadPdfLib() {
        const existingLib = getPdfLib();

        if (existingLib) {
            return Promise.resolve(existingLib);
        }

        if (window.__sjmathsPdfLibPromise) {
            return window.__sjmathsPdfLibPromise;
        }

        window.__sjmathsPdfLibPromise = new Promise(function (resolve, reject) {
            const script = document.createElement("script");
            script.src = PDFJS_SCRIPT_CDN;
            script.async = true;
            script.crossOrigin = "anonymous";

            script.onload = function () {
                const loadedLib = getPdfLib();

                if (loadedLib) {
                    resolve(loadedLib);
                    return;
                }

                reject(new Error("pdf.js loaded without exposing a global."));
            };

            script.onerror = function () {
                reject(new Error("pdf.js failed to load."));
            };

            document.head.appendChild(script);
        });

        return window.__sjmathsPdfLibPromise;
    }

    function initPdfReader(root) {
        if (!root) {
            return;
        }

        const pdfUrl = root.dataset.pdfSrc;
        const bookTitle = root.dataset.bookTitle || "This book";
        const canvas = root.querySelector("[data-pdf-canvas]");
        const canvasWrap = root.querySelector("[data-pdf-canvas-wrap]");
        const status = root.querySelector("[data-pdf-status]");
        const prevBtns = root.querySelectorAll("[data-prev-page]");
        const nextBtns = root.querySelectorAll("[data-next-page]");
        const zoomOutBtn = root.querySelector("[data-zoom-out]");
        const zoomInBtn = root.querySelector("[data-zoom-in]");
        const pageIndicator = root.querySelector("[data-page-indicator]");
        const zoomIndicator = root.querySelector("[data-zoom-indicator]");
        const loader = root.querySelector("[data-pdf-loader]");
        const ctx = canvas.getContext("2d", { alpha: false });

        let pdfDoc = null;
        let pageNum = 1;
        let zoomLevel = 1;
        let renderNonce = 0;
        let resizeTimer = null;

        const minZoom = 0.8;
        const maxZoom = 2.4;
        const zoomStep = 0.15;

        function loadPdfDocument(pdfjsLib) {
            pdfjsLib.GlobalWorkerOptions.workerSrc = PDFJS_CDN;

            return fetch(pdfUrl, {
                credentials: "same-origin",
                cache: "no-store"
            }).then(function (response) {
                if (!response.ok) {
                    throw new Error("PDF fetch failed with status " + response.status);
                }

                return response.arrayBuffer();
            }).then(function (buffer) {
                return pdfjsLib.getDocument({
                    data: new Uint8Array(buffer),
                    disableAutoFetch: true,
                    disableStream: true,
                    disableRange: true
                }).promise;
            }).catch(function (initialError) {
                console.error("PDF reader primary load failed:", initialError);
                return Promise.reject(initialError);
            });
        }

        function setStatus(message, isError) {
            status.textContent = message;
            status.dataset.state = isError ? "error" : "info";
        }

        function updateControls() {
            if (!pdfDoc) {
                if (pageIndicator) pageIndicator.textContent = "Loading...";
                if (zoomIndicator) zoomIndicator.textContent = "100%";
                if (prevBtns.length) prevBtns.forEach(btn => btn.disabled = true);
                if (nextBtns.length) nextBtns.forEach(btn => btn.disabled = true);
                if (zoomOutBtn) zoomOutBtn.disabled = true;
                if (zoomInBtn) zoomInBtn.disabled = true;
                return;
            }

            if (pageIndicator) pageIndicator.textContent = "Page " + pageNum + " of " + pdfDoc.numPages;
            if (zoomIndicator) zoomIndicator.textContent = Math.round(zoomLevel * 100) + "%";
            if (prevBtns.length) prevBtns.forEach(btn => btn.disabled = pageNum <= 1);
            if (nextBtns.length) nextBtns.forEach(btn => btn.disabled = pageNum >= pdfDoc.numPages);
            if (zoomOutBtn) zoomOutBtn.disabled = zoomLevel <= minZoom;
            if (zoomInBtn) zoomInBtn.disabled = zoomLevel >= maxZoom;
        }

        async function renderPage() {
            if (!pdfDoc) {
                return;
            }

            const currentNonce = ++renderNonce;
            setStatus("Loading page " + pageNum + "...", false);

            try {
                const page = await pdfDoc.getPage(pageNum);

                if (currentNonce !== renderNonce) {
                    return;
                }

                const baseViewport = page.getViewport({ scale: 1 });
                const availableWidth = Math.max(canvasWrap.clientWidth - 32, 280);
                const fitScale = availableWidth / baseViewport.width;

                // High-fidelity rendering: Scale based on device pixel ratio for super-sharp text
                const outputScale = window.devicePixelRatio || 1;
                const viewport = page.getViewport({ scale: fitScale * zoomLevel * outputScale });

                // Internal canvas resolution (high resolution)
                canvas.width = Math.floor(viewport.width);
                canvas.height = Math.floor(viewport.height);

                // Visible canvas size (scaled down in browser to maintain sharpness)
                canvas.style.width = Math.floor(viewport.width / outputScale) + "px";
                canvas.style.height = Math.floor(viewport.height / outputScale) + "px";

                ctx.setTransform(1, 0, 0, 1, 0, 0);
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                // High-quality image smoothing
                ctx.imageSmoothingEnabled = true;
                ctx.imageSmoothingQuality = 'high';

                await page.render({
                    canvasContext: ctx,
                    viewport: viewport
                }).promise;

                if (currentNonce !== renderNonce) {
                    return;
                }

                setStatus("Read " + bookTitle + " on SJMaths. Printing and download controls are hidden in this reader.", false);
                updateControls();

                // Hide loader on first successful render
                if (loader && loader.style.display !== 'none') {
                    loader.style.opacity = '0';
                    loader.style.visibility = 'hidden';
                    setTimeout(() => {
                        loader.style.display = 'none';
                    }, 600);
                }
            } catch (error) {
                console.error("PDF reader render failed:", error);
                setStatus("The book could not be loaded right now. Refresh the page and try again.", true);
            }
        }

        function queueRender() {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(function () {
                renderPage();
            }, 120);
        }

        if (prevBtns.length) {
            prevBtns.forEach(btn => {
                btn.addEventListener("click", function () {
                    if (pageNum <= 1) {
                        return;
                    }

                    pageNum -= 1;
                    renderPage();
                });
            });
        }

        if (nextBtns.length) {
            nextBtns.forEach(btn => {
                btn.addEventListener("click", function () {
                    if (!pdfDoc || pageNum >= pdfDoc.numPages) {
                        return;
                    }

                    pageNum += 1;
                    renderPage();
                });
            });
        }

        if (zoomOutBtn) {
            zoomOutBtn.addEventListener("click", function () {
                zoomLevel = Math.max(minZoom, zoomLevel - zoomStep);
                renderPage();
            });
        }

        if (zoomInBtn) {
            zoomInBtn.addEventListener("click", function () {
                zoomLevel = Math.min(maxZoom, zoomLevel + zoomStep);
                renderPage();
            });
        }

        canvasWrap.addEventListener("contextmenu", function (event) {
            event.preventDefault();
            setStatus("Right-click is disabled in this reader. Continue reading on SJMaths.", true);
        });

        document.addEventListener("keydown", function (event) {
            const key = event.key.toLowerCase();
            const isModifier = event.ctrlKey || event.metaKey;

            if (isModifier && (key === "p" || key === "s")) {
                event.preventDefault();
                setStatus("Printing and saving are disabled in this reader. Continue reading on SJMaths.", true);
            }
        });

        window.addEventListener("resize", queueRender);
        updateControls();
        setStatus("Preparing reader...", false);

        loadPdfLib().then(function (pdfjsLib) {
            return loadPdfDocument(pdfjsLib);
        }).then(function (pdf) {
            pdfDoc = pdf;
            updateControls();
            renderPage();
        }).catch(function (error) {
            console.error("PDF reader load failed:", error);
            setStatus("The book could not be loaded right now. Refresh the page and try again.", true);
        });
    }

    function bootReaders() {
        document.querySelectorAll("[data-pdf-reader]").forEach(initPdfReader);
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", bootReaders);
        return;
    }

    bootReaders();
}());
