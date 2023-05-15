"""Module for base model."""

from __future__ import annotations
from typing import Any

import attrs


@attrs.define
class BaseModel:
    """The base model from which all the other models inherit from."""
