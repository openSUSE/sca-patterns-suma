#!/usr/bin/python3
#
# Title:       Important SUMA Security Announcement for Proxy SUSE-SU-2011:0648-1
# Description: Security fixes for SUSE Manager 2.1
# Source:      SUMA Security Announcement Parser v1.0.3
# Modified:    2014 Dec 05
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

import os
import Core
import SUSE
import suma

META_CLASS = "Security"
META_CATEGORY = "SUMA"
META_COMPONENT = "Proxy"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2011-06/msg00006.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'Proxy'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2011:0648-1'
PACKAGES = {}
SUMA = suma.getSumaInfo()

if ( SUMA['Installed'] ):
	if ( SUMA['Version'] == '2.1' ):
		PACKAGES = {
			'spacewalk-backend': '1.2.74-0.30.2',
			'spacewalk-backend-libs': '1.2.74-0.30.2',
			'spacewalk-proxy-installer': '1.2.3-0.16.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the SUMA version scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: SUMA Not Installed")
Core.printPatternResults()

