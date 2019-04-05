# Copyright (C) 2005-2019 IP2Location.com
# All Rights Reserved
#
# This library is free software: you can redistribute it and/or
# modify it under the terms of the MIT license

import os
import ip2location_python_c

ip = "8.8.8.8"

database = ip2location_python_c.IP2Location()

database.open(os.path.join("data", "IPV6-COUNTRY.BIN"))

rec = database.get_all(ip)

print rec.country_short
print rec.country_long
print rec.region
print rec.city
print rec.isp
print rec.latitude
print rec.longitude
print rec.domain
print rec.zipcode
print rec.timezone
print rec.netspeed
print rec.idd_code
print rec.area_code
print rec.weather_code
print rec.weather_name
print rec.mcc
print rec.mnc
print rec.mobile_brand
print rec.elevation
print rec.usage_type
print("\nYou may download the DB24 sample BIN at https://www.ip2location.com/downloads/sample6.bin.db24.zip for full data display.")

database.close()