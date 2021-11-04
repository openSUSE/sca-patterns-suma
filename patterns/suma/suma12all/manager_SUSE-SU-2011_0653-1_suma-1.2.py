#!/usr/bin/python3
#
# Title:       Important SUMA Security Announcement for Manager SUSE-SU-2011:0653-1
# Description: Security fixes for SUSE Manager 1.2
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
META_COMPONENT = "Manager"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2011-06/msg00007.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'Manager'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2011:0653-1'
PACKAGES = {}
SUMA = suma.getSumaInfo()

if ( SUMA['Installed'] ):
	if ( SUMA['Version'] == '1.2' ):
		PACKAGES = {
			'spacewalk-backend': '1.2.74-0.30.3',
			'spacewalk-backend-app': '1.2.74-0.30.3',
			'spacewalk-backend-applet': '1.2.74-0.30.3',
			'spacewalk-backend-config-files': '1.2.74-0.30.3',
			'spacewalk-backend-config-files-common': '1.2.74-0.30.3',
			'spacewalk-backend-config-files-tool': '1.2.74-0.30.3',
			'spacewalk-backend-iss': '1.2.74-0.30.3',
			'spacewalk-backend-iss-export': '1.2.74-0.30.3',
			'spacewalk-backend-libs': '1.2.74-0.30.3',
			'spacewalk-backend-package-push-server': '1.2.74-0.30.3',
			'spacewalk-backend-server': '1.2.74-0.30.3',
			'spacewalk-backend-sql': '1.2.74-0.30.3',
			'spacewalk-backend-sql-oracle': '1.2.74-0.30.3',
			'spacewalk-backend-tools': '1.2.74-0.30.3',
			'spacewalk-backend-xml-export-libs': '1.2.74-0.30.3',
			'spacewalk-backend-xmlrpc': '1.2.74-0.30.3',
			'spacewalk-backend-xp': '1.2.74-0.30.3',
			'spacewalk-base': '1.2.31-0.25.1',
			'spacewalk-base-minimal': '1.2.31-0.25.1',
			'spacewalk-branding': '1.2.2-0.18.2',
			'spacewalk-grail': '1.2.31-0.25.1',
			'spacewalk-html': '1.2.31-0.25.1',
			'spacewalk-java': '1.2.115-0.42.1',
			'spacewalk-java-config': '1.2.115-0.42.1',
			'spacewalk-java-lib': '1.2.115-0.42.1',
			'spacewalk-java-oracle': '1.2.115-0.42.1',
			'spacewalk-pxt': '1.2.31-0.25.1',
			'spacewalk-setup': '1.2.16-0.18.1',
			'spacewalk-sniglets': '1.2.31-0.25.1',
			'spacewalk-taskomatic': '1.2.115-0.42.1',
			'susemanager': '1.2.0-0.38.1',
			'susemanager-client-config_en-pdf': '1.2-0.34.1',
			'susemanager-install_en-pdf': '1.2-0.34.1',
			'susemanager-jsp_en': '1.2-0.26.3',
			'susemanager-manuals_en': '1.2-0.34.1',
			'susemanager-proxy-quick_en-pdf': '1.2-0.34.1',
			'susemanager-quick_en-pdf': '1.2-0.34.1',
			'susemanager-reference_en-pdf': '1.2-0.34.1',
			'susemanager-tools': '1.2.0-0.38.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the SUMA version scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: SUMA Not Installed")
Core.printPatternResults()

