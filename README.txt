README.txt

Usage: python jnpr_xml_convert.py <file.xml>

Does a best-effort conversion from Juniper XML
router configuration to Juniper 'set' commands.  The
original idea was to parse the file as XML, but the tag/text
relationships being a little funky made it difficult.

As it stands, parsing as text isn't that wonderful either,
but it seems to work on all the test configs so far.
  (Even though its very ugly and ineffecient.)
