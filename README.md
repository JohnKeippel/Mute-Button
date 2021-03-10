# Mute-Button

I saw various people making and selling mute buttons this past year, including [Microsoft](https://www.onmsft.com/news/iot-enthusiasts-can-now-create-their-own-mute-button-for-microsoft-teams), and thought it would be a fun project. Like others, this project uses the Trinket as a HID/keyboard to maximize compatibility with things like corporate machines which might prevent fancier integrations. I figured since I wanted a case that would be sort of stable, I might as well throw in a second button and then I realized I had extra switches laying around and thought why not make it more extensible!

The electronics and code aren't too complex, but for me the learning was primarily in designing a case in Fusion 360 and also dabbling with CircuitPython for the first time. The learning curve in Fusion is steep but I picked up many new skills along the way!

## Repo Contents
- CircuitPython Code
- Fritzing diagram
- Models (Fusion, STL)
- Silhouette Labels

## BOM
 - [Trinket M0](https://www.adafruit.com/product/3500) x1
 - Arcade or other momentary switches x2 (I used [these](https://www.amazon.com/gp/product/B01N5JRU2R/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1), but [Adafruit](http://adafruit.com/) has many to choose from and if the Trinket wasn't available on Amazon when I was already placing an order I would have picked up everything from Adafruit!)
 - Toggle switches x2 (I had these lying around from an old water cooler I disassembled)
 - USB cable that supports data transfer (not just power)
 - Screws for mounting the board to the case x2 (these were laying around as well from another random disassembly, the ones I used are about 6-8mm long and about 2mm wide and just fit in the Trinket mounting holes)

## Helpful Links
- [Fusion 360 Tutorial – Easy Snap Fit Cases!](https://www.youtube.com/watch?v=VVmOtM60VWw)
  - I learned so much from this video. A quick, repeatable method for making snapfit cases that uses mirroring, offsets, section analysis, shell, and rigid joints
- [Designing a 3D Printed Enclosure for Arduino Uno](https://www.youtube.com/watch?v=E0bhdr84FNU)
  - Another great quick tutorial on how to make cases. Learned about importing other models, creating rigid joints, and then projecting geometry from those models into my sketch. Used this to drop the Trinket model into my sketch and project the necessary USB cutout
- On non-express Adafruit boards, space is quite limited. If you're dev-ing with a Mac, hidden files can exacerbate the problem.
  - [Prevent & Remove MacOS Hidden Files](https://learn.adafruit.com/welcome-to-circuitpython/troubleshooting#prevent-and-remove-macos-hidden-files-2978468-48)
  - [Copy Files on MacOS Without Creating Hidden Files](https://learn.adafruit.com/welcome-to-circuitpython/troubleshooting#copy-files-on-macos-without-creating-hidden-files-2978473-53)
    - This was the big one for me because I was unable to fit all the necessary keyboard libraries on the Trinket otherwise; clearing out all libs and copying files this way did the trick.
- List of [key codes](https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html) for deriving the necessary shortcuts

## Future Enhancements

- Standoffs too small (one broke off), plus they should really be a tiny bit wider than the through hole 🤦
- OS/App selection could be performed with a rotary encoder to eliminate switches and add additional options
- Use proper debounce instead of sleep
- Have the buttons trigger configurable hot keys on the host system that can control the appropriate apps if they are not in the foreground

## Initial Design Notes

Button Dimensions
- 27.1 mm wide
- 23.5 mm for hole diameter
- 27.5 mm deep (inside to contacts)

Board Dimensions
- 27 mm x 15.3 mm x [3.5 mm (usb), 2.75 otherwise]

Micro USB Dimensions
- 6.85 mm x 1.8 mm

Two Buttons
- One for mute/unmute
- One for raise/lower hand

Two switches?
- Mac vs PC
- Zoom vs Teams

Snap fit case
- Component with two nested components for top and bottom
- Length, width, height, shell, and gap (.2 mm and 45 degree for 3D  printing)