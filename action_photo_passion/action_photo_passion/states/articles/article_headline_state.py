"""Defines the states for the headlines of the article."""

import reflex as rx

from action_photo_passion.services.articles.service_article_reader import (
    ServiceArticleHeadlineReader,
)


class ArticleHeadlineState(rx.State):
    """State for article headlines."""

    category: str
    title: str
    headline: str
