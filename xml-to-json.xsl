<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns:map="http://www.w3.org/2005/xpath-functions/map"
    xmlns:array="http://www.w3.org/2005/xpath-functions/array"
    xpath-default-namespace="http://www.w3.org/1999/xhtml" exclude-result-prefixes="#all"
    version="3.0">

    <xsl:output method="json" indent="yes"/>
    <xsl:strip-space elements="*"/>

    <xsl:template match="/">
        <xsl:variable name="classes" as="item()*">
            <xsl:apply-templates select="//table"/>
        </xsl:variable>
        <xsl:sequence select="map {'classes': array {$classes}}"/>
    </xsl:template>

    <xsl:template match="table">
        <xsl:variable name="phonemes" as="item()*">
            <xsl:apply-templates select="tr[position() gt 1]">
                <xsl:with-param name="fnames" as="xs:string+" select="tr[1]/th[position() gt 1]" tunnel="yes"/>
            </xsl:apply-templates>
        </xsl:variable>
        <xsl:sequence select="map {preceding-sibling::h2[1]: array {$phonemes}}"/>
    </xsl:template>

    <xsl:template match="tr">
        <xsl:variable name="features" as="item()*">
            <xsl:apply-templates select="td"/>
        </xsl:variable>
        <xsl:sequence select="map {th: array {$features}}"/>
    </xsl:template>

    <xsl:template match="td">
        <xsl:param name="fnames" tunnel="yes"/>
        <xsl:message select="$fnames"/>
        <xsl:map-entry key="$fnames[current()/count(preceding-sibling::td) + 1]">
            <xsl:value-of select="."/>
        </xsl:map-entry>
    </xsl:template>
</xsl:stylesheet>
