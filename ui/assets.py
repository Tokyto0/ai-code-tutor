"""Frontend CSS and JavaScript assets for the Gradio UI."""

CODE_FONT_JS = """    (fontSize) => {
        const size = Number(fontSize) || 14;
        document.documentElement.style.setProperty("--code-editor-font-size", `${size}px`);
    }
"""

CODE_EXPAND_JS = """    (expanded) => {
        const height = expanded ? "560px" : "300px";
        document.documentElement.style.setProperty("--code-editor-min-height", height);
        document.body.classList.toggle("code-area-expanded", Boolean(expanded));
    }
"""

CUSTOM_HEAD = """<script>
(() => {
    const applyLightTheme = () => {
        const targets = [
            document.documentElement,
            document.body,
            ...document.querySelectorAll(".gradio-container")
        ].filter(Boolean);
        for (const target of targets) {
            target.classList.add("app-light-theme");
        }
        document.documentElement.style.colorScheme = "light";
    };
    applyLightTheme();
    document.addEventListener("DOMContentLoaded", applyLightTheme);
    setTimeout(applyLightTheme, 50);
    setTimeout(applyLightTheme, 250);
    setTimeout(applyLightTheme, 1000);
    new MutationObserver(applyLightTheme).observe(document.documentElement, { childList: true, subtree: true });
})();
</script>
"""

CUSTOM_CSS = """    :root {
        --code-editor-font-size: 14px;
        --code-editor-min-height: 300px;
        --app-bg: #f4f7fb;
        --app-bg-soft: #eef6f6;
        --app-surface: #ffffff;
        --app-surface-muted: #f8fafc;
        --app-border: #dbe3ee;
        --app-border-strong: #bfd4ef;
        --app-text: #102033;
        --app-text-muted: #5b6b7f;
        --app-primary: #2563eb;
        --app-primary-strong: #1d4ed8;
        --app-indigo: #4338ca;
        --app-teal: #0f766e;
        --app-amber: #b45309;
        --app-rose: #be123c;
        --app-shadow: 0 18px 42px rgba(15, 23, 42, 0.08);
        --app-shadow-soft: 0 10px 26px rgba(15, 23, 42, 0.06);
        --app-font-sans: "Inter", "Segoe UI", "Microsoft YaHei UI", "Microsoft YaHei", "PingFang SC", "Noto Sans CJK SC", Arial, sans-serif;
        --app-font-mono: Consolas, "Cascadia Code", "JetBrains Mono", "Fira Code", "SFMono-Regular", "Liberation Mono", monospace;
    }
    body {
        background:
            radial-gradient(circle at top left, rgba(15, 118, 110, 0.10), transparent 28rem),
            linear-gradient(180deg, #f8fbff 0%, var(--app-bg) 46%, #eef2f7 100%) !important;
        color: var(--app-text);
        font-family: var(--app-font-sans);
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
    }
    .gradio-container,
    .gradio-container * {
        font-family: var(--app-font-sans);
    }
    code,
    pre,
    .cm-editor,
    .cm-editor *,
    .cm-content,
    .cm-content *,
    .cm-line,
    .cm-line *,
    .cm-gutters,
    .cm-gutters * {
        font-family: var(--app-font-mono) !important;
    }
    .main-title {
        text-align: center;
        margin-bottom: 10px;
    }
    .app-light-theme,
    .app-light-theme .gradio-container {
        color-scheme: light;
        --body-background-fill: #f8fafc;
        --body-text-color: #0f172a;
        --block-background-fill: #ffffff;
        --block-border-color: #e5e7eb;
        --input-background-fill: #ffffff;
        --input-border-color: #d1d5db;
        --button-secondary-background-fill: #f8fafc;
    }
    .status-bar {
        padding: 14px 16px;
        border-radius: 8px;
        background:
            linear-gradient(135deg, rgba(29, 78, 216, 0.96) 0%, rgba(15, 118, 110, 0.98) 100%),
            #1d4ed8;
        color: #ffffff !important;
        box-shadow: var(--app-shadow-soft);
        font-weight: 750;
        letter-spacing: 0;
        text-shadow: 0 1px 1px rgba(15, 23, 42, 0.28);
    }
    .status-bar,
    .status-bar *,
    .status-bar p,
    .status-bar span,
    .status-bar strong,
    .status-bar em,
    .status-bar a {
        color: #ffffff !important;
    }
    .status-bar p {
        margin: 0 !important;
        font-size: 1.03rem;
        line-height: 1.6;
    }
    .gradio-container {
        max-width: 1680px !important;
        padding: 24px !important;
        background: transparent !important;
    }
    .app-header {
        border: 1px solid rgba(191, 212, 239, 0.78);
        border-radius: 8px;
        padding: 22px 26px 20px;
        margin-bottom: 18px;
        background:
            linear-gradient(135deg, rgba(255, 255, 255, 0.96), rgba(248, 250, 252, 0.90)),
            linear-gradient(90deg, rgba(37, 99, 235, 0.08), rgba(15, 118, 110, 0.10));
        box-shadow: var(--app-shadow);
    }
    .app-header h1 {
        margin: 0 0 6px !important;
        color: var(--app-primary-strong);
        font-size: clamp(2rem, 3.2vw, 3rem);
        font-weight: 900;
        letter-spacing: 0;
    }
    .app-header h3,
    .app-header p {
        margin-top: 6px !important;
        color: var(--app-text-muted);
        font-weight: 600;
    }
    .config-panel {
        border: 1px solid var(--app-border) !important;
        border-radius: 8px !important;
        margin-bottom: 18px !important;
        background: rgba(255, 255, 255, 0.78) !important;
        box-shadow: var(--app-shadow-soft);
        overflow: hidden;
    }
    .main-tabs .tab-nav {
        border-bottom: 1px solid var(--app-border);
        margin-bottom: 16px;
    }
    .main-tabs button[role="tab"] {
        border-radius: 8px 8px 0 0 !important;
        font-weight: 700 !important;
    }
    .main-tabs button[aria-selected="true"] {
        color: var(--app-primary) !important;
        border-bottom-color: var(--app-primary) !important;
    }
    .work-panel,
    .result-panel,
    .library-panel,
    .guide-panel {
        border: 1px solid var(--app-border);
        border-radius: 8px;
        padding: 16px;
        background: rgba(255, 255, 255, 0.88);
        box-shadow: var(--app-shadow-soft);
    }
    .result-panel {
        background: rgba(255, 255, 255, 0.94);
    }
    .panel-heading h3 {
        margin-top: 0 !important;
        padding-bottom: 10px;
        border-bottom: 1px solid var(--app-border);
        color: var(--app-indigo);
        font-weight: 850;
    }
    .section-panel {
        border: 1px solid var(--app-border);
        border-radius: 8px;
        padding: 16px;
        background: var(--app-surface);
    }
    label,
    .wrap label,
    .block label {
        color: var(--app-text) !important;
        font-weight: 750 !important;
    }
    input,
    textarea,
    select {
        border-radius: 8px !important;
    }
    .form,
    .block {
        border-color: var(--app-border) !important;
    }
    button {
        border-radius: 8px !important;
    }
    button.primary {
        background: linear-gradient(135deg, #2563eb, #0f766e) !important;
        border: none !important;
        box-shadow: 0 10px 20px rgba(37, 99, 235, 0.18);
    }
    button.secondary {
        border-color: var(--app-border-strong) !important;
        color: var(--app-primary) !important;
        background: var(--app-surface-muted) !important;
    }
    button:hover {
        transform: translateY(-1px);
        transition: transform 0.14s ease, box-shadow 0.14s ease;
    }
    .code-settings-row {
        align-items: center;
        gap: 12px;
        padding: 10px 14px;
        margin: 12px 0 10px;
        border: 1px solid var(--app-border-strong);
        border-radius: 8px;
        background:
            linear-gradient(180deg, rgba(255, 255, 255, 0.88), rgba(248, 250, 252, 0.92)),
            var(--app-surface-muted);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.75);
    }
    #code-font-size {
        min-width: 260px;
    }
    #code-font-size,
    #code-expand-toggle {
        margin: 0 !important;
    }
    #code-font-size label,
    #code-expand-toggle label {
        font-size: 0.92rem !important;
        color: var(--app-primary-strong) !important;
        font-weight: 800 !important;
    }
    #code-font-size .wrap,
    #code-font-size .container,
    #code-expand-toggle .wrap,
    #code-expand-toggle .container {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
    }
    #code-font-size input[type="number"] {
        max-width: 76px;
        text-align: center;
        font-weight: 750;
        color: var(--app-text);
        background: var(--app-surface) !important;
        border: 1px solid var(--app-border-strong) !important;
        border-radius: 8px !important;
    }
    #code-font-size button {
        box-shadow: none !important;
    }
    #code-expand-toggle {
        max-width: 180px;
        padding: 7px 10px !important;
        border: 1px solid var(--app-border);
        border-radius: 8px;
        background: var(--app-surface);
    }
    #code-expand-toggle label {
        color: var(--app-text) !important;
    }
    .code-editor-shell {
        margin-top: 12px;
        border: 1px solid var(--app-border-strong);
        border-radius: 8px;
        padding: 10px;
        background:
            linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(248, 250, 252, 0.96)),
            var(--app-surface);
        box-shadow: var(--app-shadow-soft);
    }
    #code-input .cm-editor,
    #code-input .cm-editor *,
    #code-input .cm-content,
    #code-input .cm-content *,
    #code-input .cm-line,
    #code-input .cm-line *,
    #code-input .cm-gutters,
    #code-input .cm-gutters *,
    #code-input textarea,
    #code-input pre,
    #code-input pre *,
    #code-input code {
        font-size: var(--code-editor-font-size) !important;
        font-family: Consolas, "Cascadia Code", "JetBrains Mono", "Fira Code", "SFMono-Regular", "Liberation Mono", monospace !important;
    }
    #code-input .cm-editor {
        min-height: var(--code-editor-min-height) !important;
    }
    #code-input .cm-scroller {
        min-height: var(--code-editor-min-height) !important;
    }
    #code-input {
        --font-mono: Consolas, "Cascadia Code", "JetBrains Mono", "Fira Code", "SFMono-Regular", "Liberation Mono", monospace;
        --mono-font: Consolas, "Cascadia Code", "JetBrains Mono", "Fira Code", "SFMono-Regular", "Liberation Mono", monospace;
        transition: min-height 0.2s ease;
        margin: 0 !important;
        border-radius: 8px !important;
        overflow: hidden;
    }
    #code-input > label,
    #code-input .label-wrap {
        border-radius: 8px 8px 0 0 !important;
        background: linear-gradient(90deg, #dbeafe, #e0f2fe) !important;
        color: #0f172a !important;
        font-weight: 850 !important;
        padding: 8px 10px !important;
        border: 1px solid var(--app-border) !important;
        border-bottom: none !important;
    }
    #code-input .cm-editor {
        border-radius: 0 0 8px 8px;
        border-color: var(--app-border) !important;
        background: #ffffff !important;
        outline: none !important;
    }
    #code-input .cm-gutters {
        background: #f8fafc !important;
        border-right: 1px solid var(--app-border) !important;
        color: #8a9ab0 !important;
    }
    .code-area-expanded #code-input {
        width: 100%;
    }
    .report-view .report-nav {
        border: 1px solid var(--app-border-strong);
        border-radius: 8px;
        padding: 12px 14px;
        margin: 12px 0 18px;
        background: linear-gradient(180deg, #f8fbff, #eef6ff);
    }
    .report-view .report-nav-title {
        font-weight: 700;
        margin-bottom: 6px;
        color: var(--app-indigo);
    }
    .report-view .report-nav ul {
        margin: 0;
        padding-left: 18px;
    }
    .report-view .report-nav li {
        margin: 4px 0;
    }
    .report-view .report-nav a {
        color: var(--app-primary);
        text-decoration: none;
        font-weight: 650;
    }
    .report-view .report-nav a:hover {
        text-decoration: underline;
    }
    .report-view .report-section {
        border-top: 1px solid var(--app-border);
        padding: 10px 0 14px;
        scroll-margin-top: 16px;
    }
    .report-view .report-section-summary {
        cursor: pointer;
        font-size: 1.55rem;
        font-weight: 800;
        line-height: 1.35;
        color: var(--app-indigo);
        list-style-position: inside;
    }
    .report-view .report-section-summary:hover {
        color: var(--app-primary);
    }
    .report-view .report-section[open] .report-section-summary {
        margin-bottom: 10px;
    }
    .report-view a[id] {
        scroll-margin-top: 16px;
    }
    .report-view pre {
        border-radius: 8px !important;
        border: 1px solid var(--app-border);
        background: #f8fafc !important;
    }
    .report-view code {
        border-radius: 6px;
        padding: 1px 4px;
        color: #0f4f78;
        background: #eef6ff;
        font-weight: 650;
    }
    .report-view h1,
    .report-view h2,
    .report-view h3,
    .report-view h4 {
        color: var(--app-indigo);
        font-weight: 850;
    }
    .report-view strong {
        color: var(--app-primary-strong);
        font-weight: 850;
    }
    .report-view li::marker {
        color: var(--app-teal);
    }
    .report-view p,
    .report-view li {
        color: var(--app-text);
        line-height: 1.82;
    }
    .library-panel .dataframe,
    .library-panel table {
        border-radius: 8px !important;
        overflow: hidden;
    }
    .footer-note {
        color: var(--app-text-muted);
        text-align: center;
        margin-top: 20px;
    }
    footer {
        display: none !important;
    }
"""
