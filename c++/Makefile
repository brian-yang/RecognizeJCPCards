SHORT_TERM=short-term
LONG_TERM=long-term
OUTPUT=$(SHORT_TERM) $(LONG_TERM)

make: neural-net hard-code
	echo "Compiled short term code."
	echo "Compiled long term code."

neural-net:
	g++ $(LONG_TERM).cpp -o $(LONG_TERM) `pkg-config opencv --cflags --libs opencv`

hard-code:
	g++ $(SHORT_TERM).cpp -o $(SHORT_TERM) `pkg-config opencv --cflags --libs opencv`
clean:
	rm -f $(OUTPUT)
