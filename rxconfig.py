import reflex as rx

config = rx.Config(
    app_name="portafolio",
    language="es",
    disable_plugins=[
        "reflex.plugins.sitemap.SitemapPlugin",
        "reflex.plugins.i18n.I18nPlugin",
    ],
)
