Unicode Integer
===============

A module that converts signed integers to unicode strings.


Usage
=====

```py
>>> import unicode_integer as ui
>>> ui16 = ui.UI16(0x2233)
>>> ui16.string
'∳'
>>> ui16_neg = ui.UI16(-0x2233)
>>> ui16_neg.string
'\uddcd'
>>> hex(ui16_neg.to_integer())
'-0x2233'
>>> ui53 = ui.UI53(0xabcddeadbeef)
'\x00ꯍ\udead뻯'
>>> hex(ui53.to_integer())
'0xabcddeadbeef'
>>> dir(ui)
['UI16', 'UI32', 'UI53', 'UI64', 'UnicodeInteger', 'UnicodeInteger16', 'UnicodeInteger32', 'UnicodeInteger53', 'UnicodeInteger64', ...]
```
