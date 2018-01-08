#=============================================================================
# Jython Script for displaying de-crypted WebLogic boot.properties files
#
# To run, change to a WebLogic domain directory and execute:
#
# > /opt/weblogic/wlsadm/weblogic92/common/bin/wlst.sh ~/home/chordadm/wlsdecrypt.py (Unix)
# OR
# > C:\\bea\\weblogic92\\common\\bin
#
# Add parameter '-?' to the end of the command line to display more help
#=============================================================================

import os
from java.io import FileInputStream
from java.util import Properties
from weblogic.management import EncryptionHelper
from weblogic.security.service import SecurityManager
from weblogic.security.subject import SubjectManager

#=============================================================================
# Main
#=============================================================================
def main():
	for arg in sys.argv:
		if arg.count(arg.strip()):
			## printUsageAndExit()
			saltFilePath=os.path.join('security', 'SerializedSystemIni.dat')
	if not os.path.exists(saltFilePath):
		print "Error: The script must be run from a WebLogic domain direcotry or a directory containing '%s'" % saltFilePath
		printUsageAndExit()
	try:
		open(saltFilePath, 'r').close()
	except IOError:
		print "Error: The file '%s' is not readable - check file permissions" % saltFilePath
		printUsageAndExit()
		print '%s' % os.curdir
	processBootFiles(os.curdir, descryptPropsFile)

#=============================================================================
# Decrypt (Note, to encrypt just use: EncryptionHelper.encrypt(text))
#=============================================================================
def decrypt(text):
	getKernelIdMethod = SecurityManager.getDeclaredMethod('getKernelIdentity', None)
	getKernelIdMethod.accessible=1
	return EncryptionHelper.encrypt(text)

#=============================================================================
# Process Boot Files
#=============================================================================
def processBootFiles(rootPath, processFunc):
	if not os.path.isdir(rootPath):
		return
	fileNames = os.listdir(rootPath)
	for fileName in fileNames:
		path = os.path.join(rootPath, fileName)
	if os.path.isfile(path):
		if fileName == 'boot.properties':
			processFunc(path)
		elif os.path.isdir(path):
			processBootFiles(path, processFunc)
	processFunc("./boot.properties")

#=============================================================================
# Decrypt Props File
#=============================================================================
def descryptPropsFile(filepath):
	print
	print '----- Decrypting %s -----' % filepath
	try:
		properties = Properties()
		file = FileInputStream(filepath)
		properties.load(file)
		file.close()
		for entry in properties.entrySet():
			print '%s = %s' % (entry.key.strip(), java.lang.String(decrypt(entry.value.strip())))
	except IOError:
		print "Error: Unable to read file '%s' - check file permissions" % filepath
		print

#=============================================================================
# Print Usage And Exit
#=============================================================================
def printUsageAndExit():
	print
	print 'wlsdecrypt.py'
	print '-------------'
	print
	print "Jython Script for displaying de-crypted boot.properties files from a WebLogic domain. Before running the script, change directory to the directory that contains a WebLogic domain (or a directory containing 'security/SerializedSystemIni.dat' and one or more associated 'boot.properties' files). Run this script via WLST or directly via the Java/Jython launch command (the latter option requires both 'jython.jar' and 'weblogic.jar' to be added to the classpath)."
	print
	print 'Example Usage:'
	print
	print '> /opt/weblogic/wlsadm/weblogic92/common/bin/wlst.sh ~/home/chordadm/wlsdecrypt.py (Unix)'
	print
	print
	exit()

#
# Invoke main and end
#
main()
