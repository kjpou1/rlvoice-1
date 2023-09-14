# Supported synthesizers
<hr>

Version 1.2.1 of rlvoice includes drivers for the following text-to-speech synthesizers. Only operating systems on which a driver is tested and known to work are listed. The drivers may work on other systems.

- SAPI5 on Windows XP and Windows Vista and Windows 8,8.1 , 10
- NSSpeechSynthesizer on Mac OS X 10.5 (Leopard) and 10.6 (Snow Leopard)
- espeak on Ubuntu Desktop Edition 8.10 (Intrepid), 9.04 (Jaunty), and 9.10 (Karmic)
- CoquiTTS on all of it's supported platforms (not tested yet, but the official website should have more information)

The `rlvoice.init()` documentation explains how to select a specific synthesizer by name as well as the default for each platform.
