<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:djb="http://www.obdurodon.org"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math" exclude-result-prefixes="#all"
    version="3.0">
    <xsl:output method="xml" indent="yes"/>
    <xsl:mode on-no-match="shallow-copy"/>
    <xsl:function name="djb:octify" as="element(stanza)+">
        <xsl:param name="remaining" as="element()*"/>
        <xsl:param name="stanzaNo" as="xs:integer"/>
        <xsl:choose>
            <xsl:when test="count($remaining[self::line]) le 8">
                <stanza stanzaNo="{format-number($stanzaNo,'000')}">
                    <xsl:copy-of select="$remaining"/>
                </stanza>
            </xsl:when>
            <xsl:otherwise>
                <xsl:variable name="milestone" as="element(line)"
                    select="$remaining[self::line][position() eq 8]"/>
                <stanza stanzaNo="{format-number($stanzaNo, '000')}">
                    <xsl:copy-of select="$remaining[. &lt;&lt; $milestone], $milestone"/>
                </stanza>
                <xsl:sequence select="djb:octify($remaining[. >> $milestone], $stanzaNo + 1)"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:function>
    <xsl:template match="/">
        <xsl:variable name="flattened" as="document-node()">
            <xsl:copy>
                <xsl:apply-templates/>
            </xsl:copy>
        </xsl:variable>
        <xsl:sequence select="djb:octify(($flattened//line | $flattened//sb), 1)"/>
    </xsl:template>
    <xsl:template match="stanza">
        <sb>
            <xsl:copy-of select="@*"/>
        </sb>
        <xsl:apply-templates/>
    </xsl:template>
</xsl:stylesheet>
