<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns:map="http://www.w3.org/2005/xpath-functions/map"
    xmlns:array="http://www.w3.org/2005/xpath-functions/array"
    xpath-default-namespace="http://www.w3.org/1999/xhtml" exclude-result-prefixes="#all"
    version="3.0">
    <!-- =================================== -->
    <!-- convert xhtml feature chart to json -->
    <!-- =================================== -->
    <xsl:output method="json" indent="yes"/>
    <xsl:strip-space elements="*"/>

    <xsl:template match="/">
        <xsl:variable name="segments" as="map(*)*">
            <xsl:apply-templates select="//table/tr[position() gt 1]"/>
        </xsl:variable>
        <xsl:sequence select="map {'segments': array {$segments}}"/>
    </xsl:template>

    <xsl:template match="tr">
        <xsl:variable name="features" as="item()*">
            <xsl:apply-templates select="td"/>
        </xsl:variable>
        <xsl:sequence select="map {th[1]: array {$features}}"/>
    </xsl:template>

    <xsl:template match="td">
        <xsl:map-entry key="../preceding-sibling::tr[last()]/th[position() eq current()/count(preceding-sibling::*) + 1]">
            <xsl:value-of select="."/>
        </xsl:map-entry>
    </xsl:template>

</xsl:stylesheet>
