function Set-CellFormula {
    param($Shape, [string]$CellName, [string]$Formula)
    try { $Shape.CellsU($CellName).FormulaU = $Formula } catch {}
}

function Convert-X {
    param([double]$X, [double]$Scale, [double]$XOffset)
    return ($XOffset + ($X * $Scale))
}

function Convert-Y {
    param([double]$Y, [double]$Scale, [double]$PageHeight, [double]$TopMargin)
    return ($PageHeight - $TopMargin - ($Y * $Scale))
}

function Add-Rect {
    param(
        $Page,
        [double]$X, [double]$Y, [double]$Width, [double]$Height,
        [double]$Scale, [double]$XOffset, [double]$PageHeight, [double]$TopMargin,
        [string]$Text = "",
        [string]$FillRgb = "",
        [string]$LineRgb = "",
        [string]$LineWeight = "1 pt",
        [string]$FontSize = "10 pt",
        [bool]$Bold = $false,
        [bool]$NoLine = $false,
        [bool]$NoFill = $false,
        [int]$Align = 1
    )

    $x1 = Convert-X -X $X -Scale $Scale -XOffset $XOffset
    $y1 = Convert-Y -Y ($Y + $Height) -Scale $Scale -PageHeight $PageHeight -TopMargin $TopMargin
    $x2 = Convert-X -X ($X + $Width) -Scale $Scale -XOffset $XOffset
    $y2 = Convert-Y -Y $Y -Scale $Scale -PageHeight $PageHeight -TopMargin $TopMargin

    $shape = $Page.DrawRectangle($x1, $y1, $x2, $y2)
    $shape.Text = $Text

    if ($NoFill) { Set-CellFormula $shape "FillPattern" "0" } elseif ($FillRgb) { Set-CellFormula $shape "FillForegnd" "RGB($FillRgb)" }
    if ($NoLine) { Set-CellFormula $shape "LinePattern" "0" } elseif ($LineRgb) { Set-CellFormula $shape "LineColor" "RGB($LineRgb)" }

    Set-CellFormula $shape "LineWeight" $LineWeight
    Set-CellFormula $shape "Rounding" "0"
    Set-CellFormula $shape "Char.Size" $FontSize
    Set-CellFormula $shape "Para.HorzAlign" $Align.ToString()
    Set-CellFormula $shape "VerticalAlign" "1"
    if ($Bold) { Set-CellFormula $shape "Char.Style" "1" }
    return $shape
}

function Add-TextBox {
    param(
        $Page,
        [double]$X, [double]$Y, [double]$Width, [double]$Height,
        [double]$Scale, [double]$XOffset, [double]$PageHeight, [double]$TopMargin,
        [string]$Text,
        [string]$FontSize = "10 pt",
        [bool]$Bold = $false,
        [int]$Align = 0
    )

    return Add-Rect -Page $Page -X $X -Y $Y -Width $Width -Height $Height -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text $Text -NoFill $true -NoLine $true -FontSize $FontSize -Bold:$Bold -Align $Align
}

function Add-Arrow {
    param(
        $Page,
        [double]$X1, [double]$Y1, [double]$X2, [double]$Y2,
        [double]$Scale, [double]$XOffset, [double]$PageHeight, [double]$TopMargin,
        [string]$LineRgb = "107,114,128",
        [string]$LineWeight = "1.1 pt"
    )

    $shape = $Page.DrawLine(
        (Convert-X -X $X1 -Scale $Scale -XOffset $XOffset),
        (Convert-Y -Y $Y1 -Scale $Scale -PageHeight $PageHeight -TopMargin $TopMargin),
        (Convert-X -X $X2 -Scale $Scale -XOffset $XOffset),
        (Convert-Y -Y $Y2 -Scale $Scale -PageHeight $PageHeight -TopMargin $TopMargin)
    )
    Set-CellFormula $shape "LineColor" "RGB($LineRgb)"
    Set-CellFormula $shape "LineWeight" $LineWeight
    Set-CellFormula $shape "EndArrow" "13"
    return $shape
}
