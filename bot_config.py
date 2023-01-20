#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Bot Configuration"""

    ############## Azure Bot Service ###############
    PORT = 3978
    # APP_ID = os.environ.get("MicrosoftAppId", "") 
    # APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    APP_ID = os.environ.get("MicrosoftAppId", "b0f22e08-bfcf-4ac3-b637-82efc5278d37") 
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "41fd1518-b497-4e9e-9406-95fde84ac7e2")

    ############## LUIS Service ###############
    LUIS_APP_ID = os.environ.get("LuisAppId", "109b72ce-ba2e-48f4-b3e6-06889b9320a4") #109b72ce-ba2e-48f4-b3e6-06889b9320a4
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "10cf4c925d3640e39afc9c76af3488c8")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://luis-oc.cognitiveservices.azure.com/")

    ############## App Insights Service ###############
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "7bd90414-f4b1-46a2-ab4b-e2d57675fa9f")
    # AppInsight API Key: leidc4yesmvlrjy8u3n0b78l6s0s2z1e4cnnxrb1
