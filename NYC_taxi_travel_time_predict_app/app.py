#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ericyuan
"""

import dash
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True