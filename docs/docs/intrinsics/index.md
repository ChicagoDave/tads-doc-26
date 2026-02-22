# Intrinsic Classes & Functions

The TADS 3 virtual machine provides a rich set of built-in classes and function sets that are available to every program. These intrinsics handle everything from string manipulation and file I/O to networking and regular expressions.

- **[Overview](builtins.md)** — Introduction to the intrinsic class and function set system

## Function Sets

- **[t3vm Function Set](functions/t3vm.md)** — Core VM functions (runtime type info, undo, restart)
- **[tads-gen Function Set](functions/tadsgen.md)** — General utility functions (dataType, toString, rand, etc.)
- **[Regular Expressions](functions/regex.md)** — Pattern matching with `rexMatch`, `rexSearch`, `rexReplace`
- **[tads-io Function Set](functions/tadsio.md)** — Input/output functions (input, display, file dialogs)
- **[tads-net Function Set](functions/tadsnet.md)** — Networking support for web-based play
- **[Network Safety](functions/netsec.md)** — Security settings for network operations
- **[Input Scripts](functions/scripts.md)** — Replay scripting and automated testing
- **[Byte Packing](functions/pack.md)** — Binary data packing and unpacking

## Intrinsic Classes

- **[BigNumber](classes/bignum.md)** — Arbitrary-precision decimal arithmetic
- **[ByteArray](classes/bytearr.md)** — Raw byte buffer for binary data
- **[CharacterSet](classes/charset.md)** — Character encoding conversions
- **[Collection](classes/collect.md)** — Abstract base for Lists and Vectors
- **[Date](classes/date.md)** — Date and time representation
- **[Dictionary](classes/dict.md)** — Word-to-object lookup for the parser
- **[DynamicFunc](classes/dynfunc.md)** — Dynamically compiled functions
- **[File](classes/file.md)** — File reading and writing
- **[FileName](classes/filename.md)** — File path manipulation
- **[GrammarProd](classes/gramprod.md)** — Grammar production rules for the parser
- **[HTTPRequest](classes/httpreq.md)** — Incoming HTTP request objects
- **[HTTPServer](classes/httpsrv.md)** — Embedded HTTP server
- **[IntrinsicClass](classes/icic.md)** — Metaclass representing intrinsic classes
- **[Iterator](classes/iter.md)** — Sequential element access for collections
- **[List](classes/list.md)** — Immutable ordered sequences
- **[LookupTable](classes/lookup.md)** — Hash-based key/value mapping
- **[Object](classes/objic.md)** — Root intrinsic class for all objects
- **[RexPattern](classes/rexpat.md)** — Compiled regular expression patterns
- **[StackFrameDesc](classes/framedesc.md)** — Stack frame introspection
- **[String](classes/string.md)** — Immutable character strings
- **[StringBuffer](classes/strbuf.md)** — Mutable string builder
- **[StringComparator](classes/strcomp.md)** — Custom string comparison rules
- **[TadsObject](classes/tadsobj.md)** — Base metaclass for user-defined objects
- **[TemporaryFile](classes/tempfile.md)** — Temporary file management
- **[TimeZone](classes/timezone.md)** — Time zone data and conversions
- **[Vector](classes/vector.md)** — Mutable ordered sequences
- **[WeakRefLookupTable](classes/wlookup.md)** — Lookup table with weak references

See the [Overview](builtins.md) for an introduction to how intrinsic classes and function sets work.
