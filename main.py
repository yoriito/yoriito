# SPDX-License-Identifier: Apache-2.0
#
# Copyright 2026 JASPAR
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from html import escape


def define_env(env):
    """
    MkDocs Macros entry point.

    Page-local section numbering helpers:
      - sec_reset(page_index)
      - h2_sec(title)
      - h3_sec(title)

    Example in Markdown:
      {{ sec_reset(page.index) }}
      {{ h2_sec("Set Up the Development Environment") }}
      {{ h3_sec("Install Dependencies") }}
    """

    states: dict[str, dict[str, object]] = {}

    def _current_page_key() -> str:
        page = env.variables.get("page")
        if page is None:
            return "__unknown_page__"

        for attr in ("src_path", "url", "title"):
            value = getattr(page, attr, None)
            if value:
                return str(value)

        return "__unknown_page__"

    def _get_state() -> dict[str, object]:
        key = _current_page_key()
        if key not in states:
            states[key] = {
                "page_index": "",
                "major": 0,
                "minor": 0,
            }
        return states[key]

    @env.macro
    def sec_reset(page_index: object) -> str:
        state = _get_state()
        state["page_index"] = str(page_index)
        state["major"] = 0
        state["minor"] = 0
        return ""

    @env.macro
    def h2_sec(title: str) -> str:
        state = _get_state()

        if not state["page_index"]:
            raise ValueError(
                "h2_sec() was called before sec_reset(page_index). "
                "Call {{ sec_reset(...) }} near the top of the page first."
            )

        heading = f'{state["page_index"]}. {title}'
        return f"{escape(heading)}"

    @env.macro
    def h3_sec(title: str) -> str:
        state = _get_state()

        if not state["page_index"]:
            raise ValueError(
                "h3_sec() was called before sec_reset(page_index). "
                "Call {{ sec_reset(...) }} near the top of the page first."
            )

        state["major"] = int(state["major"]) + 1
        state["minor"] = 0

        heading = f'{state["page_index"]}-{state["major"]}. {title}'
        return f"{escape(heading)}"

    @env.macro
    def h4_sec(title: str) -> str:
        state = _get_state()

        if not state["page_index"]:
            raise ValueError(
                "h4_sec() was called before sec_reset(page_index). "
                "Call {{ sec_reset(...) }} near the top of the page first."
            )

        if int(state["major"]) == 0:
            raise ValueError(
                "h4_sec() was called before any h3_sec(). "
                "Create a major section first."
            )

        state["minor"] = int(state["minor"]) + 1

        heading = f'{state["page_index"]}-{state["major"]}-{state["minor"]}. {title}'
        return f"{escape(heading)}"

    @env.macro
    def sec_number() -> str:
        state = _get_state()

        if not state["page_index"] or int(state["major"]) == 0:
            raise ValueError("sec_number() is not available yet.")

        return f'{state["page_index"]}-{state["major"]}'

    @env.macro
    def subsec_number() -> str:
        state = _get_state()

        if (
            not state["page_index"]
            or int(state["major"]) == 0
            or int(state["minor"]) == 0
        ):
            raise ValueError("subsec_number() is not available yet.")

        return f'{state["page_index"]}-{state["major"]}-{state["minor"]}'
