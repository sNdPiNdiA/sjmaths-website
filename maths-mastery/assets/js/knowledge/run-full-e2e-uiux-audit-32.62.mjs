import fs from "fs";
import path from "path";
import { chromium } from "playwright";


const BASE_URL =
    process.env.SJ_BASE_URL ||
    "http://localhost:8082/maths-mastery/";


const ROOT =
    path.resolve(
        process.cwd(),
        "maths-mastery"
    );


const REPORT =
    path.join(
        ROOT,
        "data",
        "taxonomy",
        "generated",
        "full-e2e-uiux-audit-32.62.json"
    );


const result = {

    step:
        "32.62",

    baseUrl:
        BASE_URL,

    startedAt:
        new Date().toISOString(),

    pageLoads: [],

    consoleErrors: [],

    pageErrors: [],

    failedRequests: [],

    brokenLinks: [],

    responsive: [],

    accessibility: [],

    interactions: [],

    readiness: [],

    issues: []
};


function addIssue(
    area,
    message
) {

    result.issues.push({
        area,
        message
    });
}


async function main() {

    const browser =
        await chromium.launch({
            headless:
                true
        });


    try {

        // ====================================================
        // DESKTOP PAGE
        // ====================================================

        const page =
            await browser.newPage({
                viewport: {
                    width:
                        1440,
                    height:
                        900
                }
            });


        page.on(
            "console",
            message => {

                if (
                    message.type() ===
                    "error"
                ) {

                    result.consoleErrors.push({
                        text:
                            message.text(),

                        location:
                            message.location()
                    });
                }
            }
        );


        page.on(
            "pageerror",
            error => {

                result.pageErrors.push(
                    error.message
                );
            }
        );


        page.on(
            "requestfailed",
            request => {

                result.failedRequests.push({
                    url:
                        request.url(),

                    method:
                        request.method(),

                    failure:
                        request.failure()
                });
            }
        );


        console.log("");
        console.log(
            "============================================================"
        );
        console.log(
            " STEP 32.62 — FULL UI/UX + END-TO-END AUDIT"
        );
        console.log(
            "============================================================"
        );
        console.log("");


        console.log(
            `BASE URL: ${BASE_URL}`
        );


        // ====================================================
        // LOAD
        // ====================================================

        const response =
            await page.goto(
                BASE_URL,
                {
                    waitUntil:
                        "networkidle",
                    timeout:
                        30000
                }
            );


        result.pageLoads.push({
            url:
                page.url(),

            status:
                response?.status() ??
                null,

            title:
                await page.title()
        });


        if (
            !response ||
            !response.ok()
        ) {

            addIssue(
                "page-load",
                `Main page HTTP failure: ${response?.status() ?? "NO_RESPONSE"}`
            );
        }
        else {

            console.log(
                "✓ Main page loaded"
            );
        }


        // ====================================================
        // INITIALIZATION / LOADING STATE
        // ====================================================

        await page.waitForTimeout(
            3000
        );


        const bodyText =
            await page.locator(
                "body"
            ).innerText();


        const preparing =
            /Preparing your learning space/i
                .test(
                    bodyText
                );


        result.readiness.push({
            stage:
                "initialization",

            preparingTextVisible:
                preparing,

            bodyText:
                bodyText.slice(
                    0,
                    3000
                )
        });


        if (
            preparing
        ) {

            addIssue(
                "application-initialization",
                "Application remains on 'Preparing your learning space...' after 3 seconds."
            );

            console.log(
                "⚠ Application still shows learning-space loading state"
            );

        }
        else {

            console.log(
                "✓ Application initialization completed"
            );
        }


        // ====================================================
        // JAVASCRIPT ERRORS
        // ====================================================

        console.log(
            `Console errors: ${result.consoleErrors.length}`
        );

        console.log(
            `Page errors: ${result.pageErrors.length}`
        );

        console.log(
            `Failed requests: ${result.failedRequests.length}`
        );


        // ====================================================
        // BROKEN LINKS
        // ====================================================

        const hrefs =
            await page.locator(
                "a[href]"
            )
            .evaluateAll(
                links =>
                    [
                        ...new Set(
                            links
                                .map(
                                    link =>
                                        link.href
                                )
                        )
                    ]
            );


        for (
            const url
            of hrefs
        ) {

            if (
                !url ||
                url.startsWith(
                    "javascript:"
                ) ||
                url.startsWith(
                    "mailto:"
                ) ||
                url.startsWith(
                    "tel:"
                ) ||
                url.startsWith(
                    "#"
                )
            ) {

                continue;
            }


            try {

                const r =
                    await page.request.get(
                        url,
                        {
                            timeout:
                                10000
                        }
                    );


                if (
                    r.status() >=
                    400
                ) {

                    result.brokenLinks.push({
                        url,
                        status:
                            r.status()
                    });
                }

            }
            catch (
                error
            ) {

                result.brokenLinks.push({
                    url,

                    status:
                        "REQUEST_FAILED",

                    error:
                        error.message
                });
            }
        }


        console.log(
            `Broken links: ${result.brokenLinks.length}`
        );


        // ====================================================
        // VIEWPORT TEST
        // ====================================================

        const viewports = [
            {
                name:
                    "desktop",
                width:
                    1440,
                height:
                    900
            },
            {
                name:
                    "laptop",
                width:
                    1280,
                height:
                    800
            },
            {
                name:
                    "tablet",
                width:
                    768,
                height:
                    1024
            },
            {
                name:
                    "mobile",
                width:
                    390,
                height:
                    844
            },
            {
                name:
                    "mobile-small",
                width:
                    320,
                height:
                    700
            }
        ];


        for (
            const viewport
            of viewports
        ) {

            await page.setViewportSize({
                width:
                    viewport.width,

                height:
                    viewport.height
            });


            await page.reload({
                waitUntil:
                    "networkidle"
            });


            await page.waitForTimeout(
                1000
            );


            const overflow =
                await page.evaluate(
                    () =>
                        document.documentElement.scrollWidth >
                        window.innerWidth + 2
                );


            result.responsive.push({
                viewport:
                    viewport.name,

                width:
                    viewport.width,

                height:
                    viewport.height,

                horizontalOverflow:
                    overflow
            });


            if (
                overflow
            ) {

                addIssue(
                    "responsive",
                    `${viewport.name} has horizontal overflow.`
                );
            }
        }


        console.log(
            "✓ Responsive viewport matrix tested"
        );


        // ====================================================
        // BASIC INTERACTIVE ELEMENTS
        // ====================================================

        const buttons =
            await page.locator(
                "button"
            ).count();


        const links =
            await page.locator(
                "a"
            ).count();


        result.interactions.push({
            buttons,
            links
        });


        console.log(
            `✓ Buttons detected: ${buttons}`
        );

        console.log(
            `✓ Links detected: ${links}`
        );


        // ====================================================
        // ACCESSIBILITY BASICS
        // ====================================================

        const controls =
            await page.locator(
                "input, select, textarea"
            ).count();


        const unlabeled =
            await page.locator(
                "input, select, textarea"
            )
            .evaluateAll(
                elements =>
                    elements.filter(
                        element => {

                            const aria =
                                element.getAttribute(
                                    "aria-label"
                                );

                            const labelledBy =
                                element.getAttribute(
                                    "aria-labelledby"
                                );

                            const id =
                                element.id;

                            const label =
                                id
                                    ? document.querySelector(
                                        `label[for="${CSS.escape(id)}"]`
                                    )
                                    : null;


                            return (
                                !aria &&
                                !labelledBy &&
                                !label
                            );
                        }
                    ).length
            );


        result.accessibility.push({
            controls,
            unlabeledControls:
                unlabeled
        });


        console.log(
            `✓ Form controls checked: ${controls}`
        );


        // ====================================================
        // READINESS UI DISCOVERY
        // ====================================================

        const readinessKeywords = [
            "readiness",
            "diagnostic",
            "adaptive",
            "target",
            "intervention",
            "progress"
        ];


        const lowerText =
            bodyText.toLowerCase();


        const foundKeywords =
            readinessKeywords.filter(
                keyword =>
                    lowerText.includes(
                        keyword
                    )
            );


        result.readiness.push({
            stage:
                "ui-discovery",

            foundKeywords
        });


        console.log(
            `✓ Readiness keywords found: ${foundKeywords.join(", ") || "none"}`
        );


        // ====================================================
        // SNAPSHOT
        // ====================================================

        result.finalUrl =
            page.url();


        result.finalTitle =
            await page.title();


    }
    finally {

        await browser.close();
    }


    result.completedAt =
        new Date().toISOString();


    result.summary = {

        consoleErrors:
            result.consoleErrors.length,

        pageErrors:
            result.pageErrors.length,

        failedRequests:
            result.failedRequests.length,

        brokenLinks:
            result.brokenLinks.length,

        issues:
            result.issues.length,

        responsiveFailures:
            result.responsive.filter(
                x =>
                    x.horizontalOverflow
            ).length,

        loadingStateStuck:
            result.readiness.some(
                x =>
                    x.preparingTextVisible
            )
    };


    fs.mkdirSync(
        path.dirname(
            REPORT
        ),
        {
            recursive:
                true
        }
    );


    fs.writeFileSync(
        REPORT,
        JSON.stringify(
            result,
            null,
            2
        ) + "\n",
        "utf8"
    );


    console.log("");
    console.log(
        "============================================================"
    );
    console.log(
        " STEP 32.62 SUMMARY"
    );
    console.log(
        "============================================================"
    );
    console.log("");

    console.log(
        `Console errors      : ${result.summary.consoleErrors}`
    );

    console.log(
        `Page errors         : ${result.summary.pageErrors}`
    );

    console.log(
        `Failed requests     : ${result.summary.failedRequests}`
    );

    console.log(
        `Broken links        : ${result.summary.brokenLinks}`
    );

    console.log(
        `Functional issues   : ${result.summary.issues}`
    );

    console.log(
        `Responsive failures : ${result.summary.responsiveFailures}`
    );

    console.log(
        `Loading stuck       : ${result.summary.loadingStateStuck}`
    );


    if (
        result.summary.issues ===
        0 &&
        result.summary.consoleErrors ===
        0 &&
        result.summary.pageErrors ===
        0 &&
        result.summary.failedRequests ===
        0 &&
        result.summary.brokenLinks ===
        0 &&
        result.summary.responsiveFailures ===
        0
    ) {

        console.log("");
        console.log(
            "✓ CORE E2E UI/UX AUDIT PASSED"
        );

    }
    else {

        console.log("");
        console.log(
            "⚠ E2E UI/UX AUDIT REQUIRES REVIEW"
        );
    }


    console.log("");
    console.log(
        "REPORT:"
    );

    console.log(
        REPORT
    );
}


main()
    .catch(
        error => {

            console.error(
                "STEP 32.62 FAILED"
            );

            console.error(
                error.stack ||
                error.message
            );

            process.exit(
                1
            );
        }
    );
