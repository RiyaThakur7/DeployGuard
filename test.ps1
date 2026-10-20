
$ErrorActionPreference = "Stop"

$url = "http://localhost:8081/health"

try {
    $response = Invoke-RestMethod -Uri $url -TimeoutSec 5

    if ($response.status -eq "healthy") {
        Write-Output "PASS: Application health check succeeded"
        exit 0
    }

    Write-Output "FAIL: Application returned an unhealthy status"
    exit 1
}
catch {
    Write-Output "FAIL: Application health check failed"
    Write-Output $_.Exception.Message
    exit 1
}
