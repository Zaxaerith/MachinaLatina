# De Rete Nodorum (1998–2005)
## 《节点之网：类型化网页与对象引用的诞生》

> **DRAFT / 纸面研究 · 2026-11-24.** NODVS-98/R1、LIGAMEN-99/R1、RETE-00/R1、年代与市场结局均为候选架空设想；没有实现服务器、浏览器或网络程序。

## 1998—2005 候选叙事

1998 年的学术出版者从 TABVLA 继承结构化文献：网页先是一组有长度的记录，然后才由客户端排版。1999 年的 LIGAMEN 把链接从文字中的标记分离出来，用可引用的文档身份、版次和记录号描述对象。2000 年的 RETE 候选资源交换协议以显式长度发送文档。此时 COS 的 W1/C24 仍在设计，早期 CVL-only 前身与这里综合形成的 R1 不应被误作同一份已发行标准。

2001—2003 年，小型 Nova 用户抱怨二进制文档不能直接手写，传统文本标记派因此继续竞争。NODVS 工具作者提出可读的编辑器源格式和可视化文档工具，但不把它们与网络字节格式混为一谈。SERMO 可能先成为服务器端记录构造语言，后来才进入浏览器。2004—2005 年可能出现基础阅读配置与高级 TABVLA 出版配置的分化：普通浏览器显示文字与引用，科研软件另读地图、公式和数据附件。

真实世界的 HTML 2.0 (1995)、XML 1.0 (1998) 以及 HTTP/1.1 (1999) 提供时代尺度，而非虚构标准的直接祖先：[RFC 1866](https://www.rfc-editor.org/rfc/rfc1866)、[XML 1.0](https://www.w3.org/TR/1998/REC-xml-19980210/)、[RFC 2616](https://www.rfc-editor.org/rfc/rfc2616)。

## 1. 一份网页的编辑器视图（非规定语法）

    NODVS 1 / EDITIO 1
      TITVLVS 1: SALVE
      PARAGRAPHVS 2: AΑ中文
      LIGAMEN 3: paragraph 2, CID span [2,4)
                 → authority 1 / resource 2 / revision 1 / whole document

Latin A and Greek Α are distinct. 中 and 文 use the sandbox trial identities 020000 and 020001 from COS-97/R1, not approved global assignments. The link selects 中文 (two CIDs at indices 2,3). It does not select four arbitrary bytes or depend on a font. This source view is illustrative pseudocode, not an implemented SERMO grammar.

## 2. Exact W1 binary example

Serving authority = 1 externally; resource 1, revision 1. Registry FFFF is a sandbox-only release fixture. Text title SALVE = 52 41 4B 54 45; paragraph AΑ中文 = 41 80 D0 00 D0 01. All fields below are hex octets.

| Part | Byte count | Hex sequence |
| --- | ---: | --- |
| NODVS header | 28 | D7 4E 44 01 01 00 FF FF 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 6F 00 03 00 00 |
| Title record header | 12 | 01 01 00 00 00 00 00 01 00 00 00 05 |
| Title payload | 5 | 52 41 4B 54 45 |
| Paragraph record header | 12 | 02 01 00 00 00 00 00 02 00 00 00 06 |
| Paragraph payload | 6 | 41 80 D0 00 D0 01 |
| Link record header | 12 | 03 01 00 00 00 00 00 03 00 00 00 24 |
| Link payload | 36 | 00 00 00 02 00 00 00 02 00 00 00 02 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 02 00 00 00 01 00 00 00 00 |
| Total | 111 | 0x6F |

W1 has 11 text payload octets and 100 structural octets in this tiny example. This is substantial overhead for very short pages. No claim that this is more efficient than HTML.

C24 serialization of the same logical revision changes title payload to 15 bytes and paragraph to 12 bytes, total 127 bytes (0x7F). Set codec 02, total 0000007F, title length 0000000F and paragraph length 0000000C. The link payload is byte-identical because its offsets are CID indices. No automatic padding.

## 3. RETE request and response

FETCH request ID 1, authority 1, resource 1, revision 1, accept both codecs.

    Frame header (16):
    D7 52 45 01 01 01 00 00 00 00 00 01 00 00 00 18
    Payload (24):
    00 00 00 00 00 00 00 01
    00 00 00 00 00 00 00 01
    00 00 00 01 03 00 00 00

RESULT returns W1, sandbox document above; this is a paper fixture, not permitted production traffic with registry FFFF.

    Frame header (16):
    D7 52 45 01 01 81 00 00 00 00 00 01 00 00 00 73
    Status/reserved (4): 00 00 00 00
    NODVS payload (111): exactly the document above

Request 40 bytes; result 131 bytes; response payload length 115 (0x73). C24 result would be 147 bytes including header/status. Counts exclude lower-layer network framing.

## 4. Failure cases

| Case | Required result |
| --- | --- |
| D0 00 in W1 paragraph | One trial character, never NUL terminator |
| Unknown optional record | Skip by declared bounded length; report omitted content |
| Unknown critical record | Reject validated rendering |
| Duplicate record ID | Reject document |
| Truncated or excessive record length | Reject document/frame; no signature scan |
| Link source span beyond decoded CID count | Reject document |
| Latest revision with nonzero target record | Reject link |
| Target does not exist | Show broken reference on retrieval |
| RESULT mismatches request ID/resource/revision | Reject response |

## 5. Long-term consequences

Typed records make stable scientific references, multilingual text boundaries and opaque attachments natural, but require authoring tools and careful binary parsing. A basic reader cannot claim perfect GIS or mathematical display merely because it can skip attachments. RETE is an application layer, with routing, DNS-like directory, authentication and secure transport left independent. The next major question is how ordinary programmers produce dynamic NODVS documents: a readable authoring notation, SERMO's type semantics, forms, event handling and security.

Related: [NODVS](../specifications/NODVS-98-R1.md), [LIGAMEN](../specifications/LIGAMEN-99-R1.md), [RETE](../specifications/RETE-00-R1.md), [prior network study](network-document-protocols-1995-2005.md).
