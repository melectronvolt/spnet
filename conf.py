
project = 'Sciences-Physiques.NET'
copyright = '2024, Rémi MEVAERE'
author = 'Rémi MEVAERE'

extensions = []

extensions = ["myst_parser","sphinx_copybutton"]
html_theme = 'sphinx_book_theme'
html_logo = "_static/logo.png"
html_theme_options = {
    "logo_only": True,
}
html_favicon = "_static/favicon.png"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'

html_static_path = ['_static']
