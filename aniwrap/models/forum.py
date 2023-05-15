"""Module for Forums related models."""

from __future__ import annotations
from datetime import datetime

from .base import BaseModel
import attrs
from .common import CommonModel

__all__ = (
    "ForumSubBoard",
    "ForumBoard",
    "Forum",
    "ForumTopic",
    "PostCreator",
    "ForumPost",
    "ForumTopicDetails",
)


@attrs.define
class ForumSubBoard(BaseModel):
    """Represents a forum subboard model."""

    id: int
    """The id of the sub board."""

    title: str
    """The title of the sub board."""


@attrs.define(init=False)
class ForumBoard(BaseModel):
    """Represnts a forum board model."""

    id: int
    """The id of the forum board."""

    title: str
    """The title of the forum board."""

    description: str | None = attrs.field(default=None)
    """The description of the board."""

    subboards: list[ForumSubBoard] | None = attrs.field(default=None)
    """The list of sub boards."""


@attrs.define(init=False)
class Forum(BaseModel):
    """Represents all fields a forum can contain."""

    title: str
    """The title of the forum."""

    boards: list[ForumBoard]
    """The list of boards in the forum"""


@attrs.define(init=False)
class ForumTopic(BaseModel):
    """Represents all fields a forum topic can contain."""

    id: int
    """The id of the topic."""

    title: str
    """The title of the topic."""

    created_at: datetime
    """The date at which the topic was created."""

    number_of_posts: int
    """The total number of posts under the topic."""

    last_post_created_at: datetime
    """The date of the latest post under the topic."""

    is_locked: bool
    """Whether the topic is locked."""

    created_by: CommonModel
    """The details of the user that created the topic."""

    last_post_created_by: CommonModel
    """The details of the user that created the last post under the topic."""


@attrs.define(init=False)
class PostCreator(BaseModel):
    """Represents post creator model."""

    id: int
    """The Id of the post's author."""

    name: str
    """The name of the post's author."""

    forum_avator: str | None = attrs.field(default=None)
    """The url for the avatar of the post's author."""


@attrs.define(init=False)
class ForumPost(BaseModel):
    """Represents a forum post model."""

    id: int
    """The Id of the fourm post."""

    number: int
    """The number(sequence?) of this particular post."""

    created_at: datetime
    """The data on which the post was created."""

    created_by: PostCreator
    """The details of the post's author."""

    body: str
    """The content of the post."""

    signature: str | None = attrs.field(default=None)
    """The signature on the post."""


@attrs.define(init=False)
class ForumTopicDetails(BaseModel):
    """Represents the forum topic details model."""

    title: str
    """The title of the forum."""

    posts: list[ForumPost] | None = attrs.field(default=None)
    """The list of posts in the forum."""
