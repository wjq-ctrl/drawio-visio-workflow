param(
    [string]$OutputPath = ""
)

$ErrorActionPreference = "Stop"
$HelperPath = Join-Path $PSScriptRoot "..\..\scripts\visio_helpers.ps1"
if (!(Test-Path -LiteralPath $HelperPath)) {
    throw "visio_helpers.ps1 not found relative to demo script."
}
. $HelperPath

if ([string]::IsNullOrWhiteSpace($OutputPath)) {
    $OutputPath = Join-Path $PSScriptRoot "transformer-architecture.vsdx"
}
$outDir = Split-Path -Parent $OutputPath
if ($outDir -and !(Test-Path -LiteralPath $outDir)) {
    New-Item -ItemType Directory -Path $outDir | Out-Null
}

$Scale = 0.01
$XOffset = 0.5
$TopMargin = 0.35
$PageHeight = 8.5

$visio = New-Object -ComObject Visio.Application
$visio.Visible = $false
$doc = $visio.Documents.Add("")
$page = $visio.ActivePage
$page.Name = "TransformerDemo"

Set-CellFormula $page.PageSheet "PageWidth" "11 in"
Set-CellFormula $page.PageSheet "PageHeight" "8.5 in"

$null = Add-TextBox -Page $page -X 270 -Y 20 -Width 260 -Height 30 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Transformer Architecture" -FontSize "16 pt" -FontRgb "31,41,55" -Bold:$true -Align 1

$null = Add-Rect -Page $page -X 200 -Y 110 -Width 210 -Height 170 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Encoder" -FillRgb "248,250,252" -LineRgb "203,213,225" -LineWeight "1.2 pt" -FontSize "11 pt" -FontRgb "51,65,85" -Bold:$true
$null = Add-Rect -Page $page -X 420 -Y 110 -Width 210 -Height 170 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Decoder" -FillRgb "248,250,252" -LineRgb "203,213,225" -LineWeight "1.2 pt" -FontSize "11 pt" -FontRgb "51,65,85" -Bold:$true

$null = Add-Rect -Page $page -X 40 -Y 150 -Width 110 -Height 42 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Input Tokens" -FillRgb "224,242,254" -LineRgb "2,132,199" -LineWeight "1.2 pt" -FontSize "9 pt" -FontRgb "15,23,42"
$null = Add-Rect -Page $page -X 40 -Y 210 -Width 140 -Height 56 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Token Embedding + Positional Encoding" -FillRgb "219,234,254" -LineRgb "37,99,235" -LineWeight "1.2 pt" -FontSize "9 pt" -FontRgb "15,23,42"
$null = Add-Rect -Page $page -X 235 -Y 150 -Width 140 -Height 110 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "N x Encoder Block`r`nMulti-Head Self-Attention`r`nAdd & Norm`r`nFeed-Forward" -FillRgb "219,234,254" -LineRgb "37,99,235" -LineWeight "1.2 pt" -FontSize "9 pt" -FontRgb "15,23,42"

$null = Add-Rect -Page $page -X 455 -Y 145 -Width 140 -Height 36 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Masked Self-Attention" -FillRgb "237,233,254" -LineRgb "124,58,237" -LineWeight "1.2 pt" -FontSize "9 pt" -FontRgb "15,23,42"
$null = Add-Rect -Page $page -X 455 -Y 192 -Width 140 -Height 36 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Encoder-Decoder Attention" -FillRgb "237,233,254" -LineRgb "124,58,237" -LineWeight "1.2 pt" -FontSize "9 pt" -FontRgb "15,23,42"
$null = Add-Rect -Page $page -X 455 -Y 239 -Width 140 -Height 36 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Feed-Forward + Add & Norm" -FillRgb "237,233,254" -LineRgb "124,58,237" -LineWeight "1.2 pt" -FontSize "9 pt" -FontRgb "15,23,42"

$null = Add-Rect -Page $page -X 420 -Y 315 -Width 110 -Height 42 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Shifted Output Tokens" -FillRgb "224,242,254" -LineRgb "2,132,199" -LineWeight "1.2 pt" -FontSize "9 pt" -FontRgb "15,23,42"
$null = Add-Rect -Page $page -X 645 -Y 170 -Width 70 -Height 36 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Linear" -FillRgb "220,252,231" -LineRgb "22,163,74" -LineWeight "1.2 pt" -FontSize "9 pt" -FontRgb "15,23,42"
$null = Add-Rect -Page $page -X 645 -Y 220 -Width 70 -Height 36 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Softmax" -FillRgb "220,252,231" -LineRgb "22,163,74" -LineWeight "1.2 pt" -FontSize "9 pt" -FontRgb "15,23,42"
$null = Add-Rect -Page $page -X 650 -Y 275 -Width 90 -Height 42 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Output Tokens" -FillRgb "253,230,138" -LineRgb "217,119,6" -LineWeight "1.2 pt" -FontSize "9 pt" -FontRgb "15,23,42" -Bold:$true

$null = Add-TextBox -Page $page -X 250 -Y 365 -Width 320 -Height 20 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -Text "Residual connections omitted for clarity" -FontSize "8 pt" -FontRgb "100,116,139" -Align 1

$null = Add-Arrow -Page $page -X1 150 -Y1 171 -X2 110 -Y2 210 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -LineRgb "100,116,139" -LineWeight "1.2 pt"
$null = Add-Arrow -Page $page -X1 180 -Y1 238 -X2 235 -Y2 205 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -LineRgb "100,116,139" -LineWeight "1.2 pt"
$null = Add-Arrow -Page $page -X1 375 -Y1 205 -X2 455 -Y2 210 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -LineRgb "100,116,139" -LineWeight "1.2 pt"
$null = Add-Arrow -Page $page -X1 475 -Y1 315 -X2 475 -Y2 181 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -LineRgb "100,116,139" -LineWeight "1.2 pt"
$null = Add-Arrow -Page $page -X1 525 -Y1 181 -X2 525 -Y2 192 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -LineRgb "100,116,139" -LineWeight "1.2 pt"
$null = Add-Arrow -Page $page -X1 525 -Y1 228 -X2 525 -Y2 239 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -LineRgb "100,116,139" -LineWeight "1.2 pt"
$null = Add-Arrow -Page $page -X1 595 -Y1 257 -X2 645 -Y2 188 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -LineRgb "100,116,139" -LineWeight "1.2 pt"
$null = Add-Arrow -Page $page -X1 680 -Y1 206 -X2 680 -Y2 220 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -LineRgb "100,116,139" -LineWeight "1.2 pt"
$null = Add-Arrow -Page $page -X1 680 -Y1 256 -X2 695 -Y2 275 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -LineRgb "100,116,139" -LineWeight "1.2 pt"
$null = Add-DashedArrow -Page $page -X1 695 -Y1 317 -X2 475 -Y2 336 -Scale $Scale -XOffset $XOffset -PageHeight $PageHeight -TopMargin $TopMargin -LineRgb "148,163,184" -LineWeight "1 pt"

$doc.SaveAs($OutputPath)
$doc.Close()
$visio.Quit()
Write-Output "CREATED: $OutputPath"
