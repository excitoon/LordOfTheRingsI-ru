echo off
cls
echo Lord of the Rings Installation Program
md %1\lord
copy install2.bat %1\lord
%1\lord\install2.bat %1

