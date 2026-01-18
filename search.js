export function getSearchConfig() {
    const path = window.location.pathname;

    if (path.includes('class-9')) return class9Search;
    if (path.includes('class-10')) return class10Search;
    if (path.includes('class-11')) return class11Search;
    if (path.includes('class-12')) return class12Search;

    return null;
}

const class9Search = {
    placeholder: "Search Class 9 topics...",
    onSearch: (query) => {
        if (query.includes("notes")) window.location.href = "chapter-wise-notes/index.html";
        else if (query.includes("ncert")) window.location.href = "ncert-exercise-practice/index.html";
        else if (query.includes("exemplar")) window.location.href = "ncert-examplar-practice/index.html";
        else if (query.includes("sample")) window.location.href = "sample-papers/index.html";
        else if (query.includes("worksheet")) window.location.href = "worksheets/index.html";
        else alert("Topic not found in Class 9. Try 'Notes', 'NCERT', 'Worksheets', etc.");
    }
};

const class10Search = {
    placeholder: "Search Class 10 topics...",
    onSearch: (query) => {
        if (query.includes("notes")) window.location.href = "chapter-wise-notes/index.html";
        else if (query.includes("pyq")) window.location.href = "previous-year-questions/index.html";
        else if (query.includes("ncert")) window.location.href = "ncert-exercise-practice/index.html";
        else if (query.includes("sample")) window.location.href = "sample-papers/index.html";
        else if (query.includes("additional")) window.location.href = "additional-questions/index.html";
        // Cross-class navigation
        else if (query.includes("class 9")) window.location.href = "../class-9/index.html";
        else if (query.includes("class 11")) window.location.href = "../class-11/index.html";
        else alert("Topic not found in Class 10. Try 'Notes', 'PYQ', 'Sample Papers', etc.");
    }
};

const class11Search = {
    placeholder: "Search Class 11 topics...",
    onSearch: (query) => {
        if (query.includes("notes")) window.location.href = "chapter-wise-notes/index.html";
        else if (query.includes("ncert")) window.location.href = "ncert-exercise-practice/index.html";
        else if (query.includes("exemplar")) window.location.href = "ncert-examplar-practice/index.html";
        else if (query.includes("sample")) window.location.href = "sample-papers/index.html";
        // Topic specific
        else if (query.includes("calculus") || query.includes("limits")) window.location.href = "chapter-wise-notes/index.html";
        else alert("Topic not found in Class 11. Try 'Notes', 'Exemplar', 'Calculus', etc.");
    }
};

const class12Search = {
    placeholder: "Search Class 12 topics...",
    onSearch: (query) => {
        if (query.includes("notes")) window.location.href = "chapter-wise-notes/index.html";
        else if (query.includes("ncert")) window.location.href = "ncert-exercise-practice/index.html";
        // Specific PYQ check
        else if (query.includes("chapter") && query.includes("pyq")) window.location.href = "previous-years-questions-chapter-wise/index.html";
        else if (query.includes("pyq")) window.location.href = "previous-year-questions/index.html";

        else if (query.includes("sample")) window.location.href = "sample-papers/index.html";
        else if (query.includes("additional")) window.location.href = "additional-questions/index.html";
        // Topic specific
        else if (query.includes("calculus") || query.includes("integration") || query.includes("vectors")) window.location.href = "chapter-wise-notes/index.html";
        else alert("Topic not found in Class 12. Try 'Notes', 'PYQ', 'Calculus', etc.");
    }
};