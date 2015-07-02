#!/usr/bin/env python
import re, argparse

level = ['set']
needs_quotes = ['description', 'message']
blacklist = ['name', 'instance', 'contents', 'rd-type']
blacklist_combine = ['vrf-targetcommunity', 'interfacesinterface','any/any']
cur_lvl, mod, mod_loop = 0, 0, 0
added, un_mod = False, False
source_file, out_file = '', ''

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="source XML file to convert", metavar="FILE", required=True)
    args = vars(parser.parse_args())
    if args['file']:
        source_file = args['file']
    return source_file

source_file = arguments()

f1 = open(source_file,"r")
lines = f1.readlines()

for line in lines:
    line = line.rstrip()
    line = re.split("[<>]",line)
    x = 0
    while x < len(line):
        if re.search("^  ",line[x]) != None:
            del line[x]
        elif line[x] == '':
            del line[x]
        else:
            x = x + 1
        if x == 100:
            print "x es muy grande"
            break
    for y in range(len(line)):
        if line[y].startswith('/'):
            output = ''
            mod = 0
            un_mod = False
            mod_loop = cur_lvl
            while mod < mod_loop:
                if level[cur_lvl - mod] == (line[y][1:]):
                    if added == True:
                        if str(level[-2]) in needs_quotes:
                            level[-1] = '"' + str(level[-1]) + '"'
                        for z in range(len(level)):
                            if str(level[z]) not in blacklist:
                                if str(level[z-1]) + str(level[z]) not in blacklist_combine:
                                    output = output + ' ' + str(level[z])
                        print output
                        added = False
                    for r in range(mod + 1):
                        del level[-1]
                    cur_lvl = cur_lvl - (mod + 1)
                    mod = 1000
                mod = mod + 1
        elif re.search("/$",str(line[y])) != None:
            level.append(str(line[y][:-1]))
            cur_lvl = cur_lvl + 1
            output = ''
            for z in range(len(level)):
                if str(level[z]) not in blacklist:
                    if str(level[z-1]) + str(level[z]) not in blacklist_combine:
                        output = output + ' ' + str(level[z])
            print output
            del level[cur_lvl]
            cur_lvl = cur_lvl - 1
            if str(line[y]) + str(level[cur_lvl]) in blacklist_combine:
                del level[cur_lvl]
                cur_lvl = cur_lvl - 1
            added = False
        elif line[y] not in blacklist:
            if re.search("^configuration",str(line[y])) == None:
                level.append(line[y])
                cur_lvl = cur_lvl + 1
                added = True
