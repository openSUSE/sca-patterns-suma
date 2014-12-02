#!/usr/bin/python

# Title:       Jabberd Initialization Failure
# Description: db: couldn't open environment: Resource temporarily unavailable
# Modified:    2014 Dec 02
#
##############################################################################
# Copyright (C) 2014 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record (jrecord@suse.com)
#
##############################################################################

##############################################################################
# Module Definition
##############################################################################

import re
import os
import Core
import suma

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SUMA"
META_CATEGORY = "Jabberd"
META_COMPONENT = "Initialization"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7015878"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def errorsFound():
	fileOpen = "messages.txt"
	section = "/var/log/messages"
	content = {}
	ERR_SM = re.compile("jabberd/sm\[\d*\]: initiali.ation of storage driver 'db' failed", re.IGNORECASE)
	FOUND_SM = False
	ERR_C2S = re.compile("jabberd/c2s\[\d*\]: failed to initiali.e auth module 'db'", re.IGNORECASE)
	FOUND_C2S = False

	if Core.getSection(fileOpen, section, content):
		for line in content:
			if ERR_SM.search(content[line]):
				FOUND_SM = True
			elif ERR_C2S.search(content[line]):
				FOUND_C2S = True

	if( FOUND_SM and FOUND_C2S ):
		return True
	else:
		return False

##############################################################################
# Main Program Execution
##############################################################################

if( suma.jabberdRunning() ):
	Core.updateStatus(Core.IGNORE, "Jabberd is running, not applicable")
else:
	if( errorsFound() ):
		Core.updateStatus(Core.CRIT, "Detected initialization errors, check the jabberd database")
	else:
		Core.updateStatus(Core.WARN, "Jabberd is not running, check the jabberd database")

Core.printPatternResults()


