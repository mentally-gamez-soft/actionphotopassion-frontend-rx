"""Welcome to Reflex! This file outlines the steps to create a basic app."""


import reflex as rx
from action_photo_passion.pages.index import index

app = rx.App()
app.add_page(index)
