<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns:map="http://www.w3.org/2005/xpath-functions/map"
    xmlns:array="http://www.w3.org/2005/xpath-functions/array"
    xpath-default-namespace="http://www.w3.org/1999/xhtml" exclude-result-prefixes="#all"
    version="3.0">
    <!-- =================================== -->
    <!-- convert xhtml feature chart to list -->
    <!-- =================================== -->
    <xsl:output method="json" indent="yes"/>
    <xsl:strip-space elements="*"/>

    <xsl:variable name="c_labels" as="xs:string+" select="//table[1]/tr[1]/th"/>
    <xsl:variable name="v_labels" as="xs:string+" select="//table[2]/tr[1]/th"/>

    <xsl:template match="/">
        <xsl:variable name="consonants" as="map(*)*">
            <xsl:apply-templates select="//table[1]/tr[position() gt 1]" mode="c"/>
        </xsl:variable>
        <xsl:variable name="vowels" as="map(*)*">
            <xsl:apply-templates select="//table[2]/tr[position() gt 1]" mode="v"/>
        </xsl:variable>
        <xsl:result-document href="consonants.json">
            <xsl:sequence select="map:merge($consonants)"/>
        </xsl:result-document>
        <xsl:result-document href="vowels.json">
            <xsl:sequence select="map:merge($vowels)"/>
        </xsl:result-document>
    </xsl:template>

    <xsl:template match="tr" mode="c">
        <xsl:variable name="row" select="current()" as="element(tr)"/>
        <xsl:variable name="segment" select="th" as="xs:string"/>
        <xsl:variable name="features" as="map(*)*">
            <xsl:for-each select="2 to count(*)">
                <xsl:variable name="label" as="xs:string" select="$c_labels[current()]"/>
                <xsl:variable name="value" as="xs:integer" select="$row/*[position() = current()]"/>
                <xsl:sequence select="map:entry($label, $value)"/>
            </xsl:for-each>
        </xsl:variable>
        <xsl:sequence select="map:entry($segment, map:merge($features))"/>
    </xsl:template>

    <xsl:template match="tr" mode="v">
        <xsl:variable name="row" select="current()" as="element(tr)"/>
        <xsl:variable name="segment" select="th" as="xs:string"/>
        <xsl:variable name="features" as="map(*)*">
            <xsl:for-each select="2 to count(*)">
                <xsl:variable name="label" as="xs:string" select="$v_labels[current()]"/>
                <xsl:variable name="value" as="xs:integer" select="$row/*[position() = current()]"/>
                <xsl:sequence select="map:entry($label, $value)"/>
            </xsl:for-each>
        </xsl:variable>
        <xsl:sequence select="map:entry($segment, map:merge($features))"/>
    </xsl:template>
</xsl:stylesheet>
