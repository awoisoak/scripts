#!/bin/bash
# Script to edit metadata in order to set CC license
exiftool -overwrite_original -XMP-dc:Rights="This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. https://creativecommons.org/licenses/by-nc-sa/4.0/" -xmp:usageterms="This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. https://creativecommons.org/licenses/by-nc-sa/4.0/" -XMP-xmpRights:Marked=True -XMP-cc:AttributionName="Javier Blanco (AwOiSoAk)" -XMP-cc:AttributionURL="http://www.awoisoak.com" -XMP-cc:license="https://creativecommons.org/licenses/by-nc-sa/4.0/" *

