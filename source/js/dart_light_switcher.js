(function () {
    const STORAGE_KEY = 'theme-preference';
    const DARK_VALUE = 'dark';
    const LIGHT_VALUE = 'light';
    const DARK_CSS_HREF = '/css/dark.css';
    const THEME_LINK_ID = 'dark-theme-stylesheet';
    const BUTTON_ID = 'theme-toggle-button';

    function ensureDarkStylesheet() {
        let link = document.getElementById(THEME_LINK_ID);
        if (!link) {
            link = document.createElement('link');
            link.id = THEME_LINK_ID;
            link.rel = 'stylesheet';
            link.href = DARK_CSS_HREF;
            document.head.appendChild(link);
        }
        return link;
    }

    function removeDarkStylesheet() {
        const link = document.getElementById(THEME_LINK_ID);
        if (link) {
            link.parentNode.removeChild(link);
        }
    }

    function applyTheme(theme) {
        if (theme === DARK_VALUE) {
            ensureDarkStylesheet();
            document.documentElement.setAttribute('data-theme', DARK_VALUE);
        } else {
            removeDarkStylesheet();
            document.documentElement.setAttribute('data-theme', LIGHT_VALUE);
        }
        localStorage.setItem(STORAGE_KEY, theme);
        updateButton(theme);
    }

    function resolveInitialTheme() {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored === DARK_VALUE || stored === LIGHT_VALUE) {
            return stored;
        }
        const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        return prefersDark ? DARK_VALUE : LIGHT_VALUE;
    }

    function createToggleButton() {
        let button = document.getElementById(BUTTON_ID);
        if (button) return button;

        button = document.createElement('button');
        button.id = BUTTON_ID;
        button.type = 'button';
        button.style.position = 'fixed';
        button.style.right = '1rem';
        button.style.bottom = '1rem';
        button.style.zIndex = '9999';
        button.style.border = '1px solid var(--primary-color)';
        button.style.borderRadius = '999px';
        button.style.padding = '0.5rem 0.9rem';
        button.style.background = 'var(--content-bg-color)';
        button.style.color = 'var(--text-color)';
        button.style.cursor = 'pointer';
        button.style.boxShadow = '0 4px 12px rgba(0,0,0,0.2)';
        button.addEventListener('click', function () {
            const nextTheme = (localStorage.getItem(STORAGE_KEY) === DARK_VALUE) ? LIGHT_VALUE : DARK_VALUE;
            applyTheme(nextTheme);
        });

        document.body.appendChild(button);
        return button;
    }

    function updateButton(theme) {
        const button = document.getElementById(BUTTON_ID);
        if (!button) return;
        button.textContent = theme === DARK_VALUE ? 'Switch to Light' : 'Switch to Dark';
    }

    function init() {
        const initialTheme = resolveInitialTheme();
        if (initialTheme === DARK_VALUE) {
            ensureDarkStylesheet();
        }
        document.documentElement.setAttribute('data-theme', initialTheme);

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function () {
                createToggleButton();
                updateButton(initialTheme);
            });
        } else {
            createToggleButton();
            updateButton(initialTheme);
        }
    }

    init();
})();
