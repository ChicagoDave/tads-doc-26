

# Part IV: The Intrinsics


This part describes the "intrinsic" functions and classes, which
are features built into the VM itself.


Although the intrinsics are built into the VM, they look and behave
much the same as ordinary functions and objects that you would define
in your own program.  You access their functionality the same way you
would access ordinary functions and objects, using the standard
function call syntax and the standard object and method syntax.


There are two main reasons that certain features are built into the
VM, rather than provided as library code.  The first is that the VM
doesn't itself provide any access to the external operating system
environment, so the only way to gain access to that environment is
through these native-code extensions to the VM.  Any features that
require OS interaction thus have to be implemented as intrinsics.  The
second reason is that certain common operations are very
computationally expensive, so they run much faster when implemented as
native machine code rather than as interpreted VM byte-code.  When
an operation is both computationally intensive and common enough that
many programs will benefit substantially from the speed improvement,
an intrinsic implementation might be justified.


[t3vm Function Set](functions/t3vm.md)  

[tads-gen Function Set](functions/tadsgen.md)  

[Regular Expressions](functions/regex.md)  

[tads-io Function Set](functions/tadsio.md)  

[tads-net Function Set](functions/tadsnet.md)  

[Network Safety](functions/netsec.md)  

[Input Scripts](functions/scripts.md)  

[Byte Packing](functions/pack.md)  

[BigNumber](classes/bignum.md)  

[ByteArray](classes/bytearr.md)  

[CharacterSet](classes/charset.md)  

[Collection](classes/collect.md)  

[Date](classes/date.md)  

[Dictionary](classes/dict.md)  

[DynamicFunc](classes/dynfunc.md)  

[File](classes/file.md)  

[FileName](classes/filename.md)  

[GrammarProd](classes/gramprod.md)  

[HTTPRequest](classes/httpreq.md)  

[HTTPServer](classes/httpsrv.md)  

[IntrinsicClass](classes/icic.md)  

[Iterator](classes/iter.md)  

[List](classes/list.md)  

[LookupTable](classes/lookup.md)  

[Object](classes/objic.md)  

[RexPattern](classes/rexpat.md)  

[StackFrameDesc](classes/framedesc.md)  

[String](classes/string.md)  

[StringBuffer](classes/strbuf.md)  

[StringComparator](classes/strcomp.md)  

[TadsObject](classes/tadsobj.md)  

[TemporaryFile](classes/tempfile.md)  

[TimeZone](classes/timezone.md)  

[Vector](classes/vector.md)  

[WeakRefLookupTable](classes/wlookup.md)
