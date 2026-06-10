from ui.assets import CUSTOM_CSS, CUSTOM_HEAD


def test_custom_head_forces_light_color_scheme():
    assert 'colorScheme = "light"' in CUSTOM_HEAD
    assert "app-light-theme" in CUSTOM_HEAD


def test_ui_assets_do_not_reintroduce_dark_theme_logic():
    combined = f"{CUSTOM_HEAD}\n{CUSTOM_CSS}"

    assert "app-dark-theme" not in combined
    assert "prefers-color-scheme" not in combined
    assert "theme_mode" not in combined
    assert "body:not(.app-light-theme)" not in combined
