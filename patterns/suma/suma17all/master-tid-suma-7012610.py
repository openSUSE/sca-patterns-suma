#!/usr/bin/python

# Title:       Master TID: SUSE Manager
# Description: Checks if SUSE Manager is installed
# Modified:    2014 Nov 13
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

import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SUMA"
META_CATEGORY = "Master TID"
META_COMPONENT = "All"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7012610|META_LINK_Docs=https://www.suse.com/documentation/suse_manager/"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Main Program Execution
##############################################################################

if( SUSE.packageInstalled('susemanager') ):
	Core.updateStatus(Core.REC, "Consider TID7012610 - SUSE Manager Master TID")
elif( SUSE.packageInstalled('susemanager-proxy') ):
	Core.updateStatus(Core.REC, "Consider TID7012610 - SUSE Manager Master TID")
else:
	Core.updateStatus(Core.IGNORE, "SUMA not found, not applicable")

Core.printPatternResults()


