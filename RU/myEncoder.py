#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
class MyEncoder(json.JSONEncoder):
    def default(self, o):
        # return {k.lstrip('_'): v for k, v in vars(o).items()}
        return {k[k.find("__")+2:]: v for k, v in vars(o).items()}