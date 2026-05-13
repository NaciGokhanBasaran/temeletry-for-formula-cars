# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 18:51:55 2025

@author: gokhan2
"""

import json

def updateData(c_type,url,com_port,connect):
    config = {}  

    
    config["connection_type"] = c_type
    config["url"] = url
    config["com_port"] =com_port
    config["connect"] = connect

    with open("app_data.json", "w") as f:
        json.dump(config, f, indent=4)
        
        
def ReadData(data="app_data.json"):
    
    with open(data, "r") as f:
        data_config = json.load(f)
        
    return data_config