# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


_RECIPE_LIST = ["finetune_llm"]
_CONFIG_LISTS = {"finetune_llm": ["alpaca_llama2_finetune"]}


def list_recipes():
    """List of availabe recipes available from the CLI"""
    return _RECIPE_LIST


def list_configs(recipe: str):
    """List of availabe configs available from the CLI given a recipe"""
    if recipe not in _CONFIG_LISTS:
        raise ValueError(f"Unknown recipe: {recipe}")
    return _CONFIG_LISTS[recipe]