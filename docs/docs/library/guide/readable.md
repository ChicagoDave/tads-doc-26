# Readable

Readable : [Thing](thing-thebasics.md)

A Readable, as its name suggest, is an object that can be read. In fact you can READ a Thing - it has precisely the same effect as using EXAMINE on it. The main difference between a Thing and a Readable is that on a Readable you can program different responses to READ and EXAMINE. EXAMINE Readable results in the display of its desc property; but READ Readable results in the display of its readDesc (assuming readDesc is defined, i.e. non-nil, otherwise the desc property is displayed).

The other main difference between a Readable and a Thing is that a Readable is regarded as the more logical target of a READ command, so that other things being equal, the parser will choose a Readable object over other kinds of Thing when disambiguating the direct object of READ (i.e. deciding which object the player meant when the command is ambiguous).

Since the tablets all contain squares of letters, they could reasonably be regarded as Readable. We could therefore redefine the Tablet class as:

```tads3
class Tablet : Readable
  desc = "\^<<theName>> is about eight inches square and an inch thick. <<readDesc>>"
  readDesc = "On it is inscribed:\b<FONT FACE='TADS-Typewriter'><<inscription>></FONT>\b"
  bulk = 4
;
```
