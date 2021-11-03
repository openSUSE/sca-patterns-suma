#!/usr/bin/python3
#
# Title:       Important SUMA Security Announcement for OpenSSL SUSE-SU-2015:1182-1
# Description: Security fixes for SUSE Manager 1.7
# Source:      SUMA Security Announcement Parser v1.0.3
# Modified:    2015 Jul 09
#
##############################################################################
# Copyright (C) 2015 SUSE LLC
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
META_COMPONENT = "OpenSSL"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2015-07/msg00004.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'OpenSSL'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2015:1182-1'
PACKAGES = {}
SUMA = suma.getSumaInfo()

if ( SUMA['Installed'] ):
	if ( SUMA['Version'] == '1.7' ):
		PACKAGES = {
			'libopenssl0_9_8': '0.9.8j-0.72.1',
			'libopenssl0_9_8-32bit': '0.9.8j-0.72.1',
			'libopenssl0_9_8-hmac': '0.9.8j-0.72.1',
			'libopenssl0_9_8-hmac-32bit': '0.9.8j-0.72.1',
			'openssl': '0.9.8j-0.72.1',
			'openssl-doc': '0.9.8j-0.72.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the SUMA version scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: SUMA Not Installed")
Core.printPatternResults()

