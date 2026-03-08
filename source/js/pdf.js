(function () {
    const MARKER_RE = /\[spirit of fire,please show me a pdf (.*?)\]/i;
    let pdfJsLoaded = null;


    function loadPdfJs() {
        if (window.pdfjsLib) {
            return Promise.resolve(window.pdfjsLib);
        }
        if (pdfJsLoaded) {
            return pdfJsLoaded;
        }
        pdfJsLoaded = new Promise((resolve, reject) => {
            const script = document.createElement("script");
            script.src = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js";
            script.onload = () => {
                window.pdfjsLib.GlobalWorkerOptions.workerSrc =
                    "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";
                resolve(window.pdfjsLib);
            };
            script.onerror = () => reject(new Error("Failed to load pdf.js"));
            document.head.appendChild(script);
        });
        return pdfJsLoaded;
    }

    function renderPdf(pdfPath, container) {
        return loadPdfJs()
            .then((pdfjsLib) => pdfjsLib.getDocument(pdfPath).promise)
            .then((pdfDoc) => {
                container.innerHTML = "";
                const totalPages = pdfDoc.numPages;
                let pageNum = 1;

                function renderPage(num) {
                    return pdfDoc.getPage(num).then((page) => {
                        const pageContainer = document.createElement("div");
                        pageContainer.className = "pdf-page-container";
                        const canvas = document.createElement("canvas");
                        const context = canvas.getContext("2d");
                        pageContainer.appendChild(canvas);
                        container.appendChild(pageContainer);

                        const containerWidth = pageContainer.clientWidth || container.clientWidth;
                        const unscaledViewport = page.getViewport({ scale: 0.5 });
                        const scale = containerWidth / unscaledViewport.width;
                        const viewport = page.getViewport({ scale: scale });

                        canvas.height = viewport.height;
                        canvas.width = viewport.width;

                        const renderContext = {
                            canvasContext: context,
                            viewport: viewport,
                        };
                        return page.render(renderContext).promise;
                    });
                }

                function renderAll() {
                    return renderPage(pageNum).then(() => {
                        if (pageNum < totalPages) {
                            pageNum += 1;
                            return renderAll();
                        }
                    });
                }

                return renderAll();
            })
            .catch((reason) => {
                console.error("PDF load failed:", reason);
                container.innerHTML =
                    "<p style=\"color:red\">PDF 加载失败：" +
                    reason +
                    "</p><p>请检查路径是否正确，并使用本地服务器访问。</p>";
            });
    }

    function handleMarkers() {
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null);
        const targets = [];

        while (walker.nextNode()) {
            const node = walker.currentNode;
            if (MARKER_RE.test(node.nodeValue)) {
                targets.push(node);
            }
        }

        if (!targets.length) {
            return;
        }
        
        targets.forEach((node) => {
            const match = node.nodeValue.match(MARKER_RE);
            if (!match) {
                return;
            }
            const pdfPath = match[1].trim();
            const parent = node.parentElement;
            const container = document.createElement("div");
            container.className = "pdf-wrapper";
            container.dataset.pdf = pdfPath;
            container.innerHTML = "<div class=\"loading\">正在加载 PDF...</div>";

            if (parent) {
                const newText = node.nodeValue.replace(MARKER_RE, "").trim();
                if (newText) {
                    node.nodeValue = newText;
                    parent.insertAdjacentElement("afterend", container);
                } else {
                    parent.replaceWith(container);
                }
            } else {
                document.body.appendChild(container);
            }

            renderPdf(pdfPath, container);
        });

        let resizeTimeout;
        window.addEventListener("resize", () => {
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(() => {
                document.querySelectorAll(".pdf-wrapper").forEach((wrapper) => {
                    const path = wrapper.dataset.pdf;
                    if (!path) {
                        return;
                    }
                    wrapper.innerHTML = "<div class=\"loading\">重新调整大小...</div>";
                    renderPdf(path, wrapper);
                });
            }, 300);
        });
    }

    document.addEventListener("DOMContentLoaded", handleMarkers);
})();
