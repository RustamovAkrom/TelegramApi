JAZZMIN_SETTINGS = {
    "site_title": "Django Admin",
    "site_header": "Django Admin",
    "site_brand": "Django Admin",
    "welcome_sign": "Welcome Django Admin",
    "site_title_short": "Django Admin",
    "site_icon": "img/user.png",
    "site_logo": "img/user.png",
    "login_logo": "img/user.png",
    "login_logo_dark":"img/user.png",
    "user_avatar": "img/user.png",
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "topmenu_links": [
        {"name": "Home", "url": "/", "new_window": False},
        {"name": "Swager-ui", "url": "/en/swagger-ui/", "new_window": False},
        {"name": "Reodoc", "url": "/en/reodoc/", "new_window": False},
        {"name": "Token", "url": "/en/api/v1/account/token/", "new_window":False},
        {"name": "Token Refresh", "url": "/en/api/v1/account/token/refresh/", "new_window":False}
    ],
    "usermenu_links": [],
    "copyright": "Telegram Api Admin",
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_js": "js/main.js",
    "custom_css": "css/main.css",
    "use_google_fonts_cdn": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "site_logo_classes": "img-circle",
    "language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-navy",
    "accent": "accent-primary",
    "navbar": "navbar-navy navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-navy",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "minty",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
    "actions_sticky_top": False,
}
