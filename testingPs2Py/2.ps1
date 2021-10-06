if (test-path -path Services.xlsx){
    remove-item Services.xlsx -force 
}

$snames = (Get-Service -Name a* | Select-Object -First 4)
#$sStatus = (Get-Service -Name a* | Select-Object -First 4).Status
write-host $snames -ForegroundColor Magenta

$snames | select-object Name,Status,DisplayName | export-csv psCsv.csv -IncludeTypeInformation:$false 

Start-Sleep 2 

python 2.py 

Start-Sleep 5 

if (test-path -path psCsv.csv){
    remove-item psCsv.csv -force 
}