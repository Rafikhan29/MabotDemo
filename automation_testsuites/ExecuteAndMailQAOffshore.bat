set SOURCE=%~dp0

SET today=%Date:~10,4%%Date:~4,2%%Date:~7,2%
set t=%time:~0,8%
set t=%t::=%
set t="010000"


echo "drive change"
cd D:
echo "drive path"
cd D:\Mabot\MabotDemo\automation_testsuites\

echo ********** Executing MM Scripts on Firefox and Chrome *****************

call pybot --variable Browser_Name:firefox --name Firefox --outputdir results\Firefox_%today%_%t% TestCases




