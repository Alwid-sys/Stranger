$paths = @(
    "HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*",
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*",
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*"
)
$search = Read-Host "Please enter the program to search for"
$LogPath = "$env:USERPROFILE\Desktop\log.txt"
Out-File $LogPath

try {
    foreach ($path in $paths) {
        $programs = Get-ItemProperty -Path $path -ErrorAction SilentlyContinue
        $foundPrograms = $programs | Where-Object { $_.DisplayName -Like "*$search*" }

        foreach ($program in $foundPrograms) {
            Write-Output "Found: $($program.DisplayName), $path"
            Add-Content -Path $LogPath -Value "
Program: `t $($program.DisplayName)
Version: `t $($program.DisplayVersion)
Install path: `t $($program.InstallLocation)
Searched path: `t $($path)`n
"   
        }
    }
} 
catch {
    Write-Output "An error occurred: $($_)"
}
