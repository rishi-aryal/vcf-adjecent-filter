#!/usr/bin/env python

##vcf_filter-adjacent.py
##Rishi Aryal, 2021('reseearyal[at]gmail[dot]com') 

from __future__ import print_function
import sys
import getopt

help_doc='''
    This script selects variants that doesn't have other variants near by (specified by the distance option)

    'Usage: vcf_filter-adjacent.py -h -v <vcf-file> -d <distance>'

     -h/--help: This usage help

    OPTIONs:
    -v/--vcf-file: input vcf
    -d/--distance: distance from the target SNP to screen [default 50]
    '''

def main(argv):
    inputfile = ''
    distance=50
    if len (sys.argv[1:])==0:
        print ('Usage: vcf_filter-adjacent.py -h -v <vcf-file> -d <distance>')
        sys.exit(2)

    try:
        opts,args=getopt.getopt(argv,"hv:d:",["help","vcf-file=", "distance="])
    except getopt.GetoptError:
        print ('Usage: vcf_filter-adjacent.py -h -v <vcf-file> -d <distance>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print (help_doc)	    
            sys.exit(2)
        elif opt in ("-v", "--vcf-file"):
	        inputfile=arg
        elif opt in ("-d", "--distance"):
            distance=int(arg)



    with open (inputfile, 'r') as vf:
        pos=[]                  ## create list of 3 consequtive positions to test
        current_chr=''          ## track current chromosome
        ll=[]                   ## create list of 3 adjacent lines
        for line in vf:
            if line.startswith("#"):        ## skip vcf headers
                print(line.strip())
            else:
                if line.split()[0]==current_chr:
                    if ll:
                        if len(ll)==1:
                            ll.append(line)
                            pos.append(int(line.split()[1]))
                            continue
                        elif len(ll)==2:     ## check distance from first variant 
                            if pos[1]-pos[0] > distance:
                                print (ll[0].strip())
                            ll.append(line)
                            pos.append(int(line.split()[1]))
                            continue
                        else:
                            if pos[1]-pos[0] > distance and pos[2]-pos[1] > distance:
                                print (ll[1].strip())
                            pos.pop(0)
                            ll.pop(0)
                            ll.append(line)
                            pos.append(int(line.split()[1]))
                        continue
                
                else:
                    if len(ll)==1:         ## in case the chromosome/contig has only one variant
                        print (ll[0].strip())
                    elif len(ll)==2:          ## in case the chromosome/contig has only two chromosomes
                        if pos[1]-pos[0] > distance:
                            print (ll[1].strip())
                    current_chr=line.split()[0]         ## set the current chromosome
                    pos=[]      ## reset position for next chromosome
                    ll=[]       ## reset line list for next chromosome
                    ll.append(line)
                    pos.append(int(line.split()[1]))
        if len(ll)==3:               ## for last line in the vcf file
            if pos[2]-pos[1] > distance:
                print (ll[2].strip())


if __name__ == "__main__":
   main(sys.argv[1:])