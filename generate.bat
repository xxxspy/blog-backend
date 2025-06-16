call hexo clean
call hexo g
echo step1
xcopy /E /I /Y .public\*.* xxxspy.github.io\
git add .
git commit -m "Update generated site"
git push
cd xxxspy.github.io
git add .
git commit -m "Update generated site"
git push
pause