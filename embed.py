from mod_pbxproj import XcodeProject
import os
import sys
import argparse

# Arguments are fun!
parser = argparse.ArgumentParser()
parser.add_argument("project", metavar='project', help='The xcodeproj to modify.')
parser.add_argument('frameworks', metavar='frameworks', nargs='+', help='A set of .framework files to embed (specify the full path).')
args = parser.parse_args()

# Check if we can see a 'project.pbxproj' in the project directory
if os.path.isfile(args.project + '/project.pbxproj') == False:
	print 'Error: ' + args.project + ' is not an xcodeproj.'
	sys.exit(-1)

# Check that each framework is a directory
for framework in args.frameworks:
	if os.path.isdir(framework) == False:
		print 'Error: ' + framework + ' does not exist.'
		sys.exit(-1)

# Load the project using mod_pbxproj
project = XcodeProject.Load(args.project + '/project.pbxproj')

# Add each framework as a file
for framework in args.frameworks:
	project.add_file_if_doesnt_exist(framework);

# Embed each framework
project.add_embed_binaries(args.frameworks)

# Save our updated project file
project.save()