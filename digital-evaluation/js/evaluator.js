/**
 * evaluator.js
 * Logic for Digital Evaluation Interface
 * Uses Fabric.js for the Canvas annotations.
 */

class EvaluationInterface {
    constructor() {
        this.questionsCount = 12; // Example: Q1 to Q12
        this.maxMarksPerQuestion = 5;
        this.isReadOnly = false;

        // Canvas State
        this.canvas = null;
        this.currentTool = 'tick'; // default tool
        this.imgObj = null; // The background image
        this.baseImgUrl = 'https://sjmaths.com/assets/icons/icon-512x512.png'; // Dummy base image

        this.init();
    }

    init() {
        this.buildQuestionsList();
        this.initCanvas();
        this.bindEvents();
        this.calculateTotal(); // Initial calc
    }

    buildQuestionsList() {
        const listContainer = document.getElementById('questionsList');
        if (!listContainer) return;

        let html = '';
        for (let i = 1; i <= this.questionsCount; i++) {
            const qNum = i.toString().padStart(2, '0');
            html += `
            <div class="q-row">
                <div class="col-qno">${qNum}</div>
                <div class="col-max">${this.maxMarksPerQuestion}</div>
                <div class="col-marks">
                    <input type="text" class="mark-input" data-q="${i}" value="">
                </div>
                <div class="col-steps">
                    <input type="text" class="step-input" data-q="${i}" value="0/1">
                </div>
            </div>`;
        }
        listContainer.innerHTML = html;

        // Add event listeners to inputs to trigger recalc
        const markInputs = listContainer.querySelectorAll('.mark-input');
        markInputs.forEach(input => {
            input.addEventListener('input', () => this.calculateTotal());
        });
    }

    calculateTotal() {
        const markInputs = document.querySelectorAll('.mark-input');
        if (!markInputs.length) return;

        let total = 0;
        markInputs.forEach(input => {
            const val = parseFloat(input.value);
            if (!isNaN(val)) {
                total += val;
            }
        });

        const totalBox = document.getElementById('totalScoreBox');
        if (totalBox) {
            const maxOverall = this.questionsCount * this.maxMarksPerQuestion;
            totalBox.textContent = `Total : ${total.toString().padStart(2, '0')}/${maxOverall}`;
        }
    }

    initCanvas() {
        const wrapper = document.getElementById('canvasWrapper');
        if (!wrapper) return;

        // Fabric canvas setup
        this.canvas = new fabric.Canvas('evalCanvas', {
            isDrawingMode: false,
            selection: false // Disable group selection for now
        });

        // Set dimensions (responsive)
        this.resizeCanvas();
        window.addEventListener('resize', () => this.resizeCanvas());

        // Load dummy image as background
        fabric.Image.fromURL(this.baseImgUrl, (img) => {
            this.imgObj = img;

            // Scale image to fit canvas width
            const scale = this.canvas.width / img.width;
            img.set({
                originX: 'left',
                originY: 'top',
                scaleX: scale,
                scaleY: scale
            });

            this.canvas.setBackgroundImage(img, this.canvas.renderAll.bind(this.canvas));
        }, { crossOrigin: 'anonymous' });

        this.setupCanvasInteractions();
    }

    resizeCanvas() {
        if (!this.canvas) return;
        const workspace = document.querySelector('.eval-workspace');
        if (!workspace) return;

        // Set canvas to slightly smaller than workspace
        const w = workspace.clientWidth - 40;
        const h = workspace.clientHeight - 40;
        this.canvas.setWidth(w);
        this.canvas.setHeight(h);
        this.canvas.renderAll();
    }

    setTool(toolId) {
        if (this.isReadOnly) return;

        this.currentTool = toolId.replace('tool', '').toLowerCase();

        // UI updates
        document.querySelectorAll('.tool-btn').forEach(btn => btn.classList.remove('tool-active'));
        const activeBtn = document.getElementById(toolId);
        if (activeBtn) activeBtn.classList.add('tool-active');

        // Canvas Drawing Mode
        if (this.currentTool === 'draw') {
            this.canvas.isDrawingMode = true;
            this.canvas.freeDrawingBrush.color = '#8e44ad';
            this.canvas.freeDrawingBrush.width = 3;
        } else {
            this.canvas.isDrawingMode = false;
        }
    }

    setupCanvasInteractions() {
        if (this.isReadOnly) return;

        this.canvas.on('mouse:down', (options) => {
            if (this.canvas.isDrawingMode) return;

            // Eraser Tool - identify clicked object and remove
            if (this.currentTool === 'eraser' && options.target) {
                this.canvas.remove(options.target);
                return;
            }

            // Ignore if we clicked on an existing object
            if (options.target && this.currentTool !== 'text' && this.currentTool !== 'tick' && this.currentTool !== 'cross') {
                return;
            }

            const pointer = this.canvas.getPointer(options.e);

            if (this.currentTool === 'tick') {
                this.addStamp('\uf00c', pointer, '#2e7d32'); // FontAwesome Check
            } else if (this.currentTool === 'cross') {
                this.addStamp('\uf00d', pointer, '#c62828'); // FontAwesome Times
            } else if (this.currentTool === 'text') {
                this.addInteractiveText(pointer);
            }
        });
    }

    addStamp(char, pointer, color) {
        const text = new fabric.Text(char, {
            left: pointer.x,
            top: pointer.y - 15,
            fontFamily: '"Font Awesome 5 Free"', // Needs to match loaded FA
            fontWeight: 900,
            fontSize: 40,
            fill: color,
            originX: 'center',
            originY: 'center',
            hasControls: true,    // Evaluator can move/resize stamp later if Select tool is chosen
            hasBorders: true,
            selectable: true
        });

        // Small border around cross as seen in screenshot
        if (char === '\uf00d') {
            const rect = new fabric.Rect({
                left: pointer.x,
                top: pointer.y - 15,
                width: 45,
                height: 45,
                originX: 'center',
                originY: 'center',
                fill: 'transparent',
                stroke: 'black',
                strokeWidth: 1
            });
            const group = new fabric.Group([rect, text], {
                left: pointer.x,
                top: pointer.y - 15,
                originX: 'center',
                originY: 'center',
            });
            this.canvas.add(group);
            this.canvas.setActiveObject(group);
        } else {
            this.canvas.add(text);
            this.canvas.setActiveObject(text);
        }

        // Revert to 'Select' tool implicitly so they don't spam stamps by accident
        // Or keep spamming if they want? We'll keep it active for faster grading.
    }

    addInteractiveText(pointer) {
        // Red badge for marks as seen in screenshot (e.g. 0.5 25S1)
        const markText = prompt("Enter Marks / Text annotation:", "");
        if (!markText) return;

        const text = new fabric.Text(markText, {
            left: pointer.x,
            top: pointer.y,
            fontFamily: 'sans-serif',
            fontWeight: 'bold',
            fontSize: 16,
            fill: '#c62828',
            backgroundColor: 'rgba(255, 255, 255, 0.8)',
            padding: 5
        });

        // Add rounded capsule background
        const rx = 10, ry = 10;
        const rect = new fabric.Rect({
            width: text.width + 10,
            height: text.height + 10,
            fill: 'transparent',
            stroke: '#c62828',
            strokeWidth: 2,
            rx: 15,
            ry: 15,
            left: pointer.x - 5,
            top: pointer.y - 5
        });

        const group = new fabric.Group([rect, text], {
            left: pointer.x,
            top: pointer.y,
            hasControls: true
        });

        this.canvas.add(group);
        this.canvas.setActiveObject(group);
    }

    bindEvents() {
        // Tool Buttons
        const tools = ['toolSelect', 'toolTick', 'toolCross', 'toolDraw', 'toolText', 'toolEraser'];
        tools.forEach(id => {
            const btn = document.getElementById(id);
            if (btn) {
                btn.addEventListener('click', () => this.setTool(id));
            }
        });

        // Basic Zoom (Optional refinement)
        const btnZoomIn = document.getElementById('btnZoomIn');
        if (btnZoomIn) {
            btnZoomIn.addEventListener('click', () => {
                let zoom = this.canvas.getZoom();
                zoom *= 1.1;
                this.canvas.setZoom(zoom);
            });
        }

        const btnZoomOut = document.getElementById('btnZoomOut');
        if (btnZoomOut) {
            btnZoomOut.addEventListener('click', () => {
                let zoom = this.canvas.getZoom();
                zoom /= 1.1;
                this.canvas.setZoom(zoom);
            });
        }

        const btnFit = document.getElementById('btnFit');
        if (btnFit) {
            btnFit.addEventListener('click', () => {
                this.canvas.setZoom(1);
                this.canvas.viewportTransform[4] = 0;
                this.canvas.viewportTransform[5] = 0;
            });
        }

        // --- Action Buttons ---
        const saveBtn = document.querySelector('.save-btn');
        if (saveBtn) saveBtn.addEventListener('click', () => alert('Evaluation draft saved successfully!'));

        const submitBtn = document.querySelector('.submit');
        if (submitBtn) submitBtn.addEventListener('click', () => {
            if (confirm('Are you sure you want to submit this evaluation? This action cannot be undone.')) {
                alert('Evaluation submitted!');
                window.location.href = 'student-dashboard.html';
            }
        });

        const rejectBtn = document.querySelector('.btn-reject');
        if (rejectBtn) rejectBtn.addEventListener('click', () => {
            const reason = prompt('Please enter reason for rejection (e.g., Unclear image, Wrong subject):');
            if (reason) alert('Assignment rejected: ' + reason);
        });

        const exitBtn = document.querySelector('.exit');
        const headerExitBtn = document.querySelector('.btn-exit');
        const exitHandler = () => {
            if (confirm('Exit without saving?')) window.location.href = 'student-dashboard.html';
        };
        if (exitBtn) exitBtn.addEventListener('click', exitHandler);
        if (headerExitBtn) headerExitBtn.addEventListener('click', exitHandler);

        // Dummy buttons feedback
        document.querySelectorAll('.btn-sol, .btn-ufm, .btn-qp').forEach(btn => {
            btn.addEventListener('click', (e) => alert(e.target.innerText + ' feature currently unavailable.'));
        });

        // --- Thumbnail Navigation ---
        const thumbs = document.querySelectorAll('.thumb-btn');
        thumbs.forEach(btn => {
            btn.addEventListener('click', (e) => {
                thumbs.forEach(t => t.classList.remove('active'));
                e.target.classList.add('active');
                if (!this.isReadOnly) {
                    // Simulating a page change
                    console.log('Switched to page ' + e.target.innerText);
                }
            });
        });

        // --- Image Filters (Brightness/Contrast) ---
        const brightnessSlider = document.getElementById('brightnessSlider');
        const contrastSlider = document.getElementById('contrastSlider');
        const brightnessVal = document.getElementById('brightnessVal');
        const contrastVal = document.getElementById('contrastVal');

        const applyFilters = () => {
            if (!this.imgObj) return;
            const b = parseInt(brightnessSlider.value, 10);
            const c = parseInt(contrastSlider.value, 10);
            brightnessVal.innerText = b;
            contrastVal.innerText = c;

            // Fabric.js built-in filters
            this.imgObj.filters = [];
            if (b !== 100) this.imgObj.filters.push(new fabric.Image.filters.Brightness({ brightness: (b - 100) / 100 }));
            if (c !== 100) this.imgObj.filters.push(new fabric.Image.filters.Contrast({ contrast: (c - 100) / 100 }));

            this.imgObj.applyFilters();
            this.canvas.requestRenderAll();
        };

        if (brightnessSlider) brightnessSlider.addEventListener('input', applyFilters);
        if (contrastSlider) contrastSlider.addEventListener('input', applyFilters);

        document.querySelectorAll('.reset-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const parent = e.target.closest('.control-group');
                const slider = parent.querySelector('.slider');
                if (slider) {
                    slider.value = 100;
                    applyFilters();
                }
            });
        });
    }

    setReadOnly(bool) {
        this.isReadOnly = bool;
        if (this.canvas) {
            this.canvas.isDrawingMode = false;
            this.canvas.getObjects().forEach(o => {
                o.selectable = false;
                o.evented = false;
            });
        }

        // Disable sidebar inputs if any
        const inputs = document.querySelectorAll('.eval-sidebar input');
        inputs.forEach(i => i.disabled = true);
    }
}

// Initialize on DOM Load
document.addEventListener('DOMContentLoaded', () => {
    window.evalInterface = new EvaluationInterface();
});
