# Local-only preview. No external binding, registration or deployment.
$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$bundledPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
Write-Host 'Open http://127.0.0.1:8755/05-Mockup/final-v4/index.html'
Write-Host 'Press Ctrl+C here to stop the preview.'
if (Test-Path -LiteralPath $bundledPython) {
    & $bundledPython -m http.server 8755 --bind 127.0.0.1 --directory $projectRoot
} else {
    python -m http.server 8755 --bind 127.0.0.1 --directory $projectRoot
}
