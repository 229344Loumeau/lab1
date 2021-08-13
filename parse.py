#
#Script that parses the log file and returns counts of unique events and the total number of log events.

import re

path = r"/var/log/auth.log"
#regex = '(<property name="(.*?)">(.*?)<\/property>)'
read_line = True
with open(path, "r") as file:
        matches = []
        if read_line == True:
                for line in file:
            cript that parses the log file and returns counts of unique events and the total number of log events.

            import re

            path = r"/var/log/auth.log"
            #regex = '(<property name="(.*?)">(.*?)<\/property>)'
            read_line = True
            with open(path, "r") as file:
                        matches = []
                            if read_line == True:
                                            for line in file:
                                                      for match in re.finditer(regex, line, re.S):
                                                                     match_text = match.group()
                                                                           matches.append(match_text)
                                                                                  print match_text
                                                                              else: 
                                                                                                          data = f.read()
                                                                                                                 for match in re.finditer(regex, data, re.S):
                                                                                                                                                 match_text = match.group()
                                                                                                                                                 matches.append(match_text)
                                                                                                                                                             file.close()
                                                                                                                                                             ~                                        
                                match_text = match.group()
                                matches.append(match_text)
                                print match_text
                    else:
                            data = f.read()
                            for match in re.finditer(regex, data, re.S):
                                    match_text = match.group()
                                    matches.append(match_text)
                        file.close()
