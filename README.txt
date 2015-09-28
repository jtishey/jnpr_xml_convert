README.txt

Usage: python jnpr_xml_convert.py -f <file.xml>

Intended to try a best-effort conversion from Juniper XML
router configuration to Juniper 'set' commands.  The original
idea was to parse the file as XML, but the tag/text
relationships being a little funky made it difficult.  As
it stands, parsing as text is not a great solution either.

