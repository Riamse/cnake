COMPILE=gcc -g -Wall
LINK=gcc -g -Wall
OPTS=$$(python3-config --libs --cflags | perl -pe 's/-W\S+\s//g')

all:
	$(COMPILE) main.c $(OPTS)
