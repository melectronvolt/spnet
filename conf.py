
project = 'Sciences-Physiques.NET'
copyright = '2024, Rémi MEVAERE'
author = 'Rémi MEVAERE'

extensions = ["myst_parser","sphinx_copybutton","sphinx_togglebutton","sphinx_tippy"]
html_theme = 'sphinx_book_theme'

tippy_skip_anchor_classes = ("headerlink", "sd-stretched-link", "sd-rounded-pill")
tippy_anchor_parent_selector = "article.bd-article"

myst_enable_extensions = [
    "dollarmath",
"amsmath",
]


html_logo = "_static/logo.png"
html_theme_options = {
    "repository_url": "https://github.com/melectronvolt/spnet",
    "repository_branch": "main",  # Branch where docs are located
    "use_repository_button": True,
    "collapse_navigation": False,  # This keeps the sidebar expanded
    "show_navbar_depth": 3,  # Adjust this to control depth if needed
    "home_page_in_toc": True,
}
html_css_files = [
    'custom.css',
]

html_context = {
   "default_mode": "dark"
}

html_favicon = "_static/favicon.png"
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'

html_static_path = ['_static']
