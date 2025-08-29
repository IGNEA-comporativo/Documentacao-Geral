# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Guia de Desenvolvimento"
copyright = "2025, P&D-IA"
author = "P&D-IA"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinxcontrib.mermaid"]


mermaid_version = "10.9.1"  # or a recent known-good
mermaid_init_js = """
mermaid.initialize({
  startOnLoad: true,
  theme: 'dark',
  themeVariables: {
    primaryColor: '#111827',   /* card bg */
    primaryTextColor: '#e5e7eb',
    lineColor: '#e5e7eb',
    secondaryColor: '#1f2937',
    tertiaryColor: '#374151'
  }
});
"""

templates_path = ["_templates"]
exclude_patterns = []

language = "pt-BR"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'sphinx_book_theme'
html_theme = "shibuya"
html_static_path = ["_static"]
