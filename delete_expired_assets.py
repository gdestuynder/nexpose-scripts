#!/usr/bin/env python2
import imp
import os
import sys
from lxml import etree

cfg_path = ['pnexpose.conf', '/etc/pnexpose.conf']
config = None

for cfg in cfg_path:
    if os.path.isfile(cfg):
        try:
            config = imp.load_source('config', cfg)
        except:
            pass

if config == None:
    print("Failed to load config")
sys.exit(1)

sys.path.append('pnexpose')

import pnexpose

nxp = pnexpose.nexposeClient(config.SERVER, config.PORT, config.USERNAME, config.PASSWORD)

def empty_asset_group(gid):
    xdev = etree.fromstring(nxp.asset_group_config(gid))
    #AssetGroup>Devices>device
    for d in xdev[0][0]:
        #device.items()>('id', '9999')
        did = d.items()[0][1]
        if config.DRY_RUN:
            print("Would delete asset", did)
            continue
        nxp.device_delete(did)

# Asset is generally an old/expired asset. if you change this, be careful, it deletes assets!
# find assets at https://your-nxp-host:3780/asset/group/listing.jsp
# The group asset URL listed there, among other things, have the group ie. e.g.:
# https://your-nxp-host:3780/group.jsp?groupid=xx
empty_asset_group(config.ASSET_GROUP_EXPIRED_ID)
