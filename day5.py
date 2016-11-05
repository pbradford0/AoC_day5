#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/5

import sys
import re

#def dupes(line)
 # for index in line:
    

def nice_calc(filename):
  input = open(filename, 'rU')
  #count all the nice strings
  nice_strings = 0
  #create regex "rules" for each nice condition
  re_vowels = re.compile('.*[aeiou].*[aeiou].*[aeiou]')
  re_dubs = re.compile('.*(.)\\1')
  re_verboten = re.compile('.*((ab)|(cd)|(pq)|(xy))')
  #loop through the strings and +1 nice string for each match
  for line in input:
    if re.match(re_vowels, line):
      if re.match(re_dubs, line):
        if not re.match(re_verboten, line):
          print line
      #if re.match(re_dubs, line):
       #if not re.match(re_verboten, line):
          nice_strings = nice_strings + 1
  
  return nice_strings

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  nice_string = nice_calc(sys.argv[1])
  print str(nice_string) + " strings are nice strings."

if __name__ == '__main__':
  main()