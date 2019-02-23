<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math" exclude-result-prefixes="#all"
    xpath-default-namespace="http://www.w3.org/1999/xhtml" version="3.0"> 
    <xsl:output method="json" indent="yes"/>
    <xsl:template match="/">
        <xsl:apply-templates select="//tr[position() &gt; 1]"/>
    </xsl:template>
    <xsl:template match="tr">
        <xsl:message>hit</xsl:message>
        <xsl:value-of select="th"/>
    </xsl:template>
</xsl:stylesheet>
