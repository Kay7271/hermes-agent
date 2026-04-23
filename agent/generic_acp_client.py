"""Generic ACP client built on top of the Copilot ACP transport shim."""

from __future__ import annotations

from agent.copilot_acp_client import CopilotACPClient


class GenericACPClient(CopilotACPClient):
    """ACP client for non-Copilot external ACP providers."""

    def __init__(self, **kwargs):
        kwargs = dict(kwargs)
        kwargs.setdefault("api_key", "generic-acp")
        kwargs.setdefault("base_url", "acp://generic")
        super().__init__(**kwargs)
