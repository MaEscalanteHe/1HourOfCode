#!/bin/bash

### Colors ###
YELLOW='\033[1;33m'
RED='\033[1;31m'
BLUE='\033[1;34m'
GREEN='\033[1;32m'
NC='\033[0m' # No Color

function csvParse {

### Vars ###
OLDIFS=$IFS
IFS=","
I=1
	
sed 1d $1 | while read Title Publication Series Volume Issue Item Authors Year URL Type
do
	echo -e "${BLUE}[$I]\t${YELLOW}${Title}${NC} \n \
	${BLUE}============================================== \n \
	${YELLOW}Index:${NC} \t $I\n \
	${YELLOW}Title:${NC} \t $Title\n \
	${YELLOW}Authors:${NC} $Authors\n \
	${YELLOW}URL:${NC} \t $URL"
	I=$(( $I + 1 ))
	sleep 0.5
	echo $URL | sed "s+/book/+/content/pdf/+g" | xargs wget -cq --no-verbose --progress=bar --show-progress -O $(echo $Title | cut -d '"' -f 2).pdf;
	if [ $? -ne 0 ]; then
	echo -e "\n${YELLOW}STATUS:${NC} \t ${RED}ERROR.\n"
	else
	echo -e "\n${YELLOW}STATUS:${NC} \t ${GREEN}OK.\n"
	fi
	sleep 1
done
	
IFS=$OLDIFS

}

csvParse $1
