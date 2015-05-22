#!/usr/bin/python
#
# Title:       Important SUMA Security Announcement for 1.7 SUSE-SU-2015:0928-1
# Description: Security fixes for SUSE Manager 1.7
# Source:      SUMA Security Announcement Parser v1.0.3
# Modified:    2015 May 22
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
META_COMPONENT = "susemanager"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2015-05/msg00020.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'susemanager'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2015:0928-1'
PACKAGES = {}
SUMA = suma.getSumaInfo()

if ( SUMA['Installed'] ):
	if ( SUMA['Version'] == '1.7' ):
		PACKAGES = {
			'sm-ncc-sync-data': '1.7.21-0.5.1',
			'smdba': '1.5-0.6.2.1',
			'spacecmd': '1.7.7.12-0.5.1',
			'spacewalk-backend': '1.7.38.34-0.5.1',
			'spacewalk-backend-app': '1.7.38.34-0.5.1',
			'spacewalk-backend-applet': '1.7.38.34-0.5.1',
			'spacewalk-backend-config-files': '1.7.38.34-0.5.1',
			'spacewalk-backend-config-files-common': '1.7.38.34-0.5.1',
			'spacewalk-backend-config-files-tool': '1.7.38.34-0.5.1',
			'spacewalk-backend-iss': '1.7.38.34-0.5.1',
			'spacewalk-backend-iss-export': '1.7.38.34-0.5.1',
			'spacewalk-backend-libs': '1.7.38.34-0.5.1',
			'spacewalk-backend-package-push-server': '1.7.38.34-0.5.1',
			'spacewalk-backend-server': '1.7.38.34-0.5.1',
			'spacewalk-backend-sql': '1.7.38.34-0.5.1',
			'spacewalk-backend-sql-oracle': '1.7.38.34-0.5.1',
			'spacewalk-backend-sql-postgresql': '1.7.38.34-0.5.1',
			'spacewalk-backend-tools': '1.7.38.34-0.5.1',
			'spacewalk-backend-xml-export-libs': '1.7.38.34-0.5.1',
			'spacewalk-backend-xmlrpc': '1.7.38.34-0.5.1',
			'spacewalk-backend-xp': '1.7.38.34-0.5.1',
			'spacewalk-branding': '1.7.1.13-0.5.1',
			'spacewalk-java': '1.7.54.34-0.5.1',
			'spacewalk-java-config': '1.7.54.34-0.5.1',
			'spacewalk-java-lib': '1.7.54.34-0.5.1',
			'spacewalk-java-oracle': '1.7.54.34-0.5.1',
			'spacewalk-java-postgresql': '1.7.54.34-0.5.1',
			'spacewalk-setup': '1.7.9.12-0.5.1',
			'spacewalk-taskomatic': '1.7.54.34-0.5.1',
			'susemanager': '1.7.30-0.5.2',
			'susemanager-schema': '1.7.56.24-0.7.1',
			'susemanager-tools': '1.7.30-0.5.2',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the SUMA version scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: SUMA Not Installed")
Core.printPatternResults()

