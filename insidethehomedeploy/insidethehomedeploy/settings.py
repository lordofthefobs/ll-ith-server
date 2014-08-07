"""
Define confab environments and roles.
"""

environmentdefs = {
    'vagrant': ['insidethehome-vagrant']
}

componentdefs = {
    'web': ['python', 'nginx', 'supervisor', 'insidethehome'],
}

roledefs = {
    'web': ['insidethehome-vagrant'],
}
