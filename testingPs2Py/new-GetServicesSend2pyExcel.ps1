$snames = Get-Service -Name a* | Select-Object -First 2
$count = 2
foreach($sname in $snames){
    python add_service_to_excel.py $sname.Status $sname.Name $sname.DisplayName $count
    $count++
}